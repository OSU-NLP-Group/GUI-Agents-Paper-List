"""discover_sources.py — broadly search for missing source links
(homepage / dataset / code) for every paper in papers.yaml.

For each paper that is missing one of {homepage, code, dataset}, we
look in two places:

1. The paper's arXiv abstract page (via the public abs HTML). The
   page's "Comments" field plus its rendered abstract often contain
   project-page / GitHub / HuggingFace URLs.

2. The paper_db's per-paper sources/links (entity.json links[]) —
   we already enrich from canonical_links, but the looser `links`
   array sometimes contains relevant URLs we haven't promoted.

The script is conservative: it never overwrites an existing value,
and it only fills a key when at least one strong signal points to
that URL. Run from `paper_repo/`:

    uv run scripts/discover_sources.py            # dry run
    uv run scripts/discover_sources.py --write    # apply
    uv run scripts/discover_sources.py --limit 50 # only first N
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]
PAPER_DB_DIR = ROOT.parent / "paper_db" / "papers"
PAPERS_YAML = ROOT / "papers.yaml"
USER_AGENT = "Mozilla/5.0 (compatible; gui-agents-paper-list/1.0)"


# Domain → kind mapping. We only ever fill sources keys we can be
# confident about; anything ambiguous gets logged but not written.
DATASET_HOSTS = {"huggingface.co", "zenodo.org", "data.mendeley.com", "kaggle.com"}
CODE_HOSTS = {"github.com", "gitlab.com", "bitbucket.org"}
# Project-page heuristics: github.io subdomain, "project" in path,
# HTTPS HTML page that isn't arxiv / openreview / a journal site.
PUBLISHER_HOSTS = {
    "openreview.net", "aclanthology.org", "proceedings.neurips.cc",
    "openaccess.thecvf.com", "dl.acm.org", "ieeexplore.ieee.org",
    "doi.org", "link.springer.com", "papers.cool", "papers.nips.cc",
}
ARXIV_HOSTS = {"arxiv.org", "arxiv.org/abs", "export.arxiv.org"}


# ─── YAML I/O preserving block style ────────────────────────────────

class LiteralStr(str):
    pass


def _literal_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(LiteralStr, _literal_representer)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write changes back to papers.yaml")
    parser.add_argument("--limit", type=int, default=None, help="Only check first N papers")
    parser.add_argument("--sleep-seconds", type=float, default=0.6, help="Delay between arXiv fetches")
    return parser.parse_args()


def is_dataset_url(url: str) -> bool:
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        return False
    return any(host == h or host.endswith("." + h) for h in DATASET_HOSTS) and "/datasets/" in url \
        or host == "huggingface.co" and "/datasets/" in url


def is_code_url(url: str) -> bool:
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        return False
    return any(host == h or host.endswith("." + h) for h in CODE_HOSTS)


def is_publisher_url(url: str) -> bool:
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        return False
    return any(host == h or host.endswith("." + h) for h in PUBLISHER_HOSTS)


def is_arxiv_url(url: str) -> bool:
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        return False
    return host in {"arxiv.org", "www.arxiv.org", "export.arxiv.org"}


_PROJECT_PAGE_PATH_HINTS = ("/projects/", "/project/", "/paper/", "/papers/", "/research/")


def is_homepage_url(url: str) -> bool:
    """Conservative project-page heuristic. We only trust URLs that
    are either:
      - a `*.github.io` subdomain (the de-facto convention), or
      - a `huggingface.co/spaces/...` host (HF demos), or
      - a path that explicitly looks like a project page on a known
        academic / lab domain.
    Anything else is rejected to avoid pulling in random links."""
    if not url.startswith(("http://", "https://")): return False
    if is_arxiv_url(url) or is_publisher_url(url) or is_code_url(url) or is_dataset_url(url):
        return False
    try:
        host = urlparse(url).netloc.lower()
        path = urlparse(url).path.lower()
    except Exception:
        return False
    if host.endswith(".github.io"): return True
    if host == "huggingface.co" and path.startswith("/spaces/"): return True
    # University / lab / personal academic domains: accept only when the
    # path explicitly looks like a project page.
    if any(host.endswith(suffix) for suffix in (".edu", ".ac.uk", ".ac.cn", ".ac.jp", ".ai", ".dev", ".org", ".io", ".com")):
        if any(h in path for h in _PROJECT_PAGE_PATH_HINTS):
            return True
    return False


# ─── Discover from arXiv abstract page ──────────────────────────────

URL_RE = re.compile(r"https?://[^\s\"'<>)]+", re.I)


def fetch_arxiv_abs(arxiv_id: str, session: requests.Session) -> str | None:
    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        r = session.get(url, headers={"User-Agent": USER_AGENT}, timeout=20)
        if r.status_code != 200:
            return None
        return r.text
    except Exception:
        return None


_ABSTRACT_RE = re.compile(r'<blockquote class="abstract[^"]*">(.+?)</blockquote>', re.S | re.I)
_COMMENTS_RE = re.compile(r'<td class="tablecell comments[^"]*">(.+?)</td>', re.S | re.I)
# arXiv often replaces URLs in paper text with `<a href="this https URL">…`
# anchors. Extract `href="…"` directly so we get the actual destination.
_ANCHOR_HREF_RE = re.compile(r'<a [^>]*href="([^"]+)"', re.I)


def harvest_urls_from_html(html: str) -> list[str]:
    """Pull URLs that appear specifically inside the abstract or
    comments regions of an arXiv abs page. Anything in page chrome
    (sidebar, footer, "Subscribe" links, university branding) is
    deliberately ignored.
    """
    if not html:
        return []
    regions: list[str] = []
    m = _ABSTRACT_RE.search(html)
    if m: regions.append(m.group(1))
    m = _COMMENTS_RE.search(html)
    if m: regions.append(m.group(1))
    if not regions:
        return []
    seen: set[str] = set()
    out: list[str] = []
    for region in regions:
        # Prefer real anchor hrefs. arXiv normally rewrites paper text
        # URLs into anchors, so we don't miss anything.
        for u in _ANCHOR_HREF_RE.findall(region):
            u = u.rstrip(".,;:)\"]'>")
            if u and u.startswith("http") and u not in seen:
                seen.add(u); out.append(u)
        # Fallback: bare URLs (rare in modern arxiv pages but
        # appear in older comments).
        for u in URL_RE.findall(region):
            u = u.rstrip(".,;:)\"]'>")
            if u and u not in seen:
                seen.add(u); out.append(u)
    return out


# ─── Discover from paper_db's links[] array ─────────────────────────

def harvest_urls_from_paper_db(slug: str) -> list[str]:
    p = PAPER_DB_DIR / slug / "entity.json"
    if not p.exists():
        return []
    try:
        ent = json.loads(p.read_text())
    except Exception:
        return []
    urls: list[str] = []
    for it in ent.get("links") or []:
        u = it.get("url")
        if u: urls.append(u)
    return urls


# ─── Main ───────────────────────────────────────────────────────────

def main() -> int:
    args = parse_args()
    raw = PAPERS_YAML.read_text(encoding="utf-8")
    docs: list[dict[str, Any]] = yaml.safe_load(raw) or []

    session = requests.Session()
    total_changed = 0
    total_changes = 0
    n = 0

    for entry in docs:
        if not isinstance(entry, dict): continue
        if args.limit is not None and n >= args.limit: break
        sources = entry.get("sources") or {}
        if not isinstance(sources, dict): sources = {}

        # Skip if everything we'd ever discover is already filled.
        needed = [k for k in ("homepage", "code", "dataset") if not sources.get(k)]
        if not needed:
            continue
        n += 1

        # Combine candidate URLs from arXiv abs HTML + paper_db links.
        candidates: list[str] = []
        arxiv_id = entry.get("arxiv_id")
        if not arxiv_id:
            m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", str(entry.get("link", "")))
            if m: arxiv_id = m.group(1)
        if arxiv_id:
            html = fetch_arxiv_abs(arxiv_id, session)
            if html:
                candidates.extend(harvest_urls_from_html(html))
        slug = (entry.get("arxiv_id") and f"paper_arxiv_{entry['arxiv_id'].replace('.', '_')}") or None
        if slug:
            candidates.extend(harvest_urls_from_paper_db(slug))

        # Find the first matching candidate per missing key.
        changes: list[str] = []
        for url in candidates:
            if "homepage" in needed and is_homepage_url(url):
                sources["homepage"] = url
                needed.remove("homepage")
                changes.append(f"+homepage")
            if "code" in needed and is_code_url(url):
                sources["code"] = url
                needed.remove("code")
                changes.append(f"+code")
            if "dataset" in needed and is_dataset_url(url):
                sources["dataset"] = url
                needed.remove("dataset")
                changes.append(f"+dataset")
            if not needed: break

        if changes:
            entry["sources"] = sources
            total_changed += 1
            total_changes += len(changes)
            print(f"  {entry.get('title','')[:60]:60s}  {' '.join(changes)}")

        if arxiv_id and args.sleep_seconds > 0:
            time.sleep(args.sleep_seconds)

    print(f"\nentries enriched: {total_changed}    individual changes: {total_changes}")

    if args.write and total_changed > 0:
        out: list[dict[str, Any]] = []
        for d in docs:
            cp = dict(d)
            if cp.get("tldr"): cp["tldr"] = LiteralStr(str(cp["tldr"]))
            if cp.get("bibtex"): cp["bibtex"] = LiteralStr(str(cp["bibtex"]))
            out.append(cp)
        body = yaml.dump(out, sort_keys=False, allow_unicode=True, width=120, default_flow_style=False)
        # Preserve header
        header_end = 0
        for line in raw.splitlines(keepends=True):
            if line.startswith("#") or line.strip() == "":
                header_end += len(line)
            else:
                break
        PAPERS_YAML.write_text(raw[:header_end] + body, encoding="utf-8")
        print(f"\nwrote {PAPERS_YAML}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
