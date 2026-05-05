"""discover_sources.py — broad source-link discovery for papers.yaml.

For each paper in papers.yaml, fills missing entries in `sources:` —
arxiv / openreview / publisher_page / homepage / code / dataset.

Pipeline per paper:
  1. Resolve `arxiv_id` if missing — via the arXiv API title search,
     then via Semantic Scholar's `externalIds.ArXiv`.
  2. Always set `sources.arxiv` from arxiv_id when known.
  3. Harvest URLs from these places, in order, until every gap is
     filled or sources are exhausted:
       a. arXiv abstract page (abstract + comments regions).
       b. HuggingFace papers page  (huggingface.co/papers/<id>).
       c. Semantic Scholar API     (externalIds, openAccessPdf, url).
       d. Publisher page if known  (the entry's `link:` field).
       e. Per-paper paper_db links + cached source text files.
       f. The README of any GitHub repo discovered above.
  4. Classify each candidate URL with a strict whitelist:
       - github / gitlab / bitbucket            → code
       - HF /datasets/, Zenodo, Mendeley, Kaggle → dataset
       - *.github.io, HF /spaces/, academic
         /projects|/project|/paper|/research/   → homepage
     Anything outside the whitelist is rejected.

Conservative: never overwrites an existing source key.

Run from `paper_repo/`:
    uv run scripts/discover_sources.py            # dry run
    uv run scripts/discover_sources.py --write    # apply
    uv run scripts/discover_sources.py --limit 50 --write
    uv run scripts/discover_sources.py --only-missing dataset --write
"""

from __future__ import annotations

import argparse
import json
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote_plus, urlparse

import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]
PAPER_DB_DIR = ROOT.parent / "paper_db" / "papers"
PAPERS_YAML = ROOT / "papers.yaml"
USER_AGENT = "Mozilla/5.0 (compatible; gui-agents-paper-list/1.0)"

DATASET_HOSTS = {"huggingface.co", "zenodo.org", "data.mendeley.com", "kaggle.com"}
CODE_HOSTS = {"github.com", "gitlab.com", "bitbucket.org"}
PUBLISHER_HOSTS = {
    "openreview.net", "aclanthology.org", "proceedings.neurips.cc", "papers.nips.cc",
    "openaccess.thecvf.com", "dl.acm.org", "ieeexplore.ieee.org",
    "doi.org", "link.springer.com", "papers.cool", "proceedings.iclr.cc",
    "proceedings.mlr.press",
}
ARXIV_HOSTS = {"arxiv.org", "www.arxiv.org", "export.arxiv.org"}

_PROJECT_PAGE_PATH_HINTS = ("/projects/", "/project/", "/paper/", "/papers/", "/research/")


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
    parser.add_argument(
        "--only-missing",
        choices=["arxiv", "code", "homepage", "dataset", "publisher_page", "openreview"],
        default=None,
        help="Skip a paper if it isn't missing this key (otherwise process all gaps).",
    )
    parser.add_argument("--sleep-seconds", type=float, default=0.4, help="Delay between external requests")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


# ─── URL classifiers ────────────────────────────────────────────────

def host_of(url: str) -> str:
    try:
        return urlparse(url).netloc.lower()
    except Exception:
        return ""


def host_matches(url: str, hosts: Iterable[str]) -> bool:
    h = host_of(url)
    return any(h == x or h.endswith("." + x) for x in hosts)


def is_arxiv_url(url: str) -> bool:
    return host_matches(url, ARXIV_HOSTS)


def is_publisher_url(url: str) -> bool:
    return host_matches(url, PUBLISHER_HOSTS)


def is_code_url(url: str) -> bool:
    return host_matches(url, CODE_HOSTS)


def is_dataset_url(url: str) -> bool:
    h = host_of(url)
    if h == "huggingface.co" or h.endswith(".huggingface.co"):
        return "/datasets/" in url
    return host_matches(url, DATASET_HOSTS - {"huggingface.co"})


def is_homepage_url(url: str) -> bool:
    if not url.startswith(("http://", "https://")): return False
    if is_arxiv_url(url) or is_publisher_url(url) or is_code_url(url) or is_dataset_url(url):
        return False
    h = host_of(url)
    path = urlparse(url).path.lower()
    if h.endswith(".github.io"): return True
    if h == "huggingface.co" and path.startswith("/spaces/"): return True
    # Project-page on a sufficiently academic domain.
    if any(h.endswith(suffix) for suffix in (".edu", ".ac.uk", ".ac.cn", ".ac.jp", ".ai", ".dev", ".org", ".io", ".com")):
        if any(hint in path for hint in _PROJECT_PAGE_PATH_HINTS):
            return True
    return False


# ─── HTTP helpers ───────────────────────────────────────────────────

URL_RE = re.compile(r"https?://[^\s\"'<>)\]]+", re.I)
ANCHOR_HREF_RE = re.compile(r'<a [^>]*href="([^"]+)"', re.I)
ABSTRACT_RE = re.compile(r'<blockquote class="abstract[^"]*">(.+?)</blockquote>', re.S | re.I)
COMMENTS_RE = re.compile(r'<td class="tablecell comments[^"]*">(.+?)</td>', re.S | re.I)


def http_get(session: requests.Session, url: str, *, timeout: float = 20) -> str | None:
    try:
        r = session.get(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,application/xml,application/json"}, timeout=timeout)
        if r.status_code == 200:
            return r.text
    except Exception:
        return None
    return None


def http_get_json(session: requests.Session, url: str, *, timeout: float = 20) -> Any | None:
    try:
        r = session.get(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}, timeout=timeout)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None


def harvest_urls_from_arxiv_abs(html: str | None) -> list[str]:
    if not html: return []
    out: list[str] = []
    seen: set[str] = set()
    for region_re in (ABSTRACT_RE, COMMENTS_RE):
        m = region_re.search(html)
        if not m: continue
        region = m.group(1)
        for u in ANCHOR_HREF_RE.findall(region):
            u = u.rstrip(".,;:)\"]'>")
            if u.startswith("http") and u not in seen:
                seen.add(u); out.append(u)
        for u in URL_RE.findall(region):
            u = u.rstrip(".,;:)\"]'>")
            if u not in seen:
                seen.add(u); out.append(u)
    return out


def harvest_urls_from_html(html: str | None) -> list[str]:
    """Pull every absolute URL out of an HTML page (anchor hrefs +
    bare URLs). Used for HuggingFace papers / GitHub READMEs /
    publisher pages."""
    if not html: return []
    out: list[str] = []
    seen: set[str] = set()
    for u in ANCHOR_HREF_RE.findall(html):
        u = u.rstrip(".,;:)\"]'>")
        if u.startswith("http") and u not in seen:
            seen.add(u); out.append(u)
    for u in URL_RE.findall(html):
        u = u.rstrip(".,;:)\"]'>")
        if u.startswith("http") and u not in seen:
            seen.add(u); out.append(u)
    return out


# ─── External lookups ───────────────────────────────────────────────

def arxiv_id_by_title(session: requests.Session, title: str, *, sleep: float) -> str | None:
    """Search arXiv's atom API for a title; return the id of the first
    near-exact match. arXiv's title field doesn't allow exact-match,
    so we accept the first hit whose title has high token overlap."""
    if not title or len(title) < 6: return None
    q = quote_plus(f'ti:"{title}"')
    url = f"http://export.arxiv.org/api/query?search_query={q}&start=0&max_results=3"
    text = http_get(session, url)
    if sleep > 0: time.sleep(sleep)
    if not text: return None
    try:
        ns = {"a": "http://www.w3.org/2005/Atom"}
        root = ET.fromstring(text)
        target = re.sub(r"[^a-z0-9]", "", title.lower())
        for entry in root.findall("a:entry", ns):
            t_el = entry.find("a:title", ns)
            id_el = entry.find("a:id", ns)
            if t_el is None or id_el is None: continue
            t_norm = re.sub(r"[^a-z0-9]", "", (t_el.text or "").lower())
            if not t_norm: continue
            # require that one is a prefix of the other (handles minor
            # title-rev differences)
            if t_norm.startswith(target[:60]) or target.startswith(t_norm[:60]):
                m = re.search(r"abs/(\d{4}\.\d{4,5})", id_el.text or "")
                if m: return m.group(1)
    except Exception:
        return None
    return None


def hf_paper_links(session: requests.Session, arxiv_id: str, *, sleep: float) -> list[str]:
    """huggingface.co/papers/<arxiv_id> aggregates project pages,
    code, and HF datasets. Pull every absolute URL from the page."""
    html = http_get(session, f"https://huggingface.co/papers/{arxiv_id}")
    if sleep > 0: time.sleep(sleep)
    return harvest_urls_from_html(html)


def semantic_scholar_links(session: requests.Session, arxiv_id: str | None, title: str | None, *, sleep: float) -> list[str]:
    """Hit S2's public API. Fields used: externalIds (DOI / ArXiv /
    GitHub-via-corpus), openAccessPdf.url, and url (homepage)."""
    out: list[str] = []
    base = "https://api.semanticscholar.org/graph/v1/paper"
    fields = "externalIds,openAccessPdf,url"
    js = None
    if arxiv_id:
        js = http_get_json(session, f"{base}/arXiv:{arxiv_id}?fields={fields}")
        if sleep > 0: time.sleep(sleep)
    if js is None and title:
        js = http_get_json(session, f"{base}/search?query={quote_plus(title)}&limit=1&fields={fields}")
        if sleep > 0: time.sleep(sleep)
        if isinstance(js, dict):
            data = js.get("data") or []
            js = data[0] if data else None
    if isinstance(js, dict):
        ext = js.get("externalIds") or {}
        if ext.get("DOI"):
            out.append(f"https://doi.org/{ext['DOI']}")
        if isinstance(js.get("openAccessPdf"), dict) and js["openAccessPdf"].get("url"):
            out.append(js["openAccessPdf"]["url"])
        if js.get("url"):
            out.append(js["url"])
    return out


def github_readme_links(session: requests.Session, repo_url: str, *, sleep: float) -> list[str]:
    """Pull URLs out of a GitHub repo's README (raw)."""
    m = re.match(r"^https?://github\.com/([^/]+)/([^/#?]+)", repo_url)
    if not m: return []
    owner, repo = m.group(1), m.group(2).rstrip(".git")
    out: list[str] = []
    for branch in ("main", "master"):
        for filename in ("README.md", "Readme.md", "readme.md", "README.rst"):
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{filename}"
            text = http_get(session, url, timeout=15)
            if sleep > 0: time.sleep(sleep)
            if text:
                out.extend(harvest_urls_from_html(text))
                return out
    return out


def paper_db_links(slug: str) -> list[str]:
    p = PAPER_DB_DIR / slug / "entity.json"
    if not p.exists(): return []
    try:
        ent = json.loads(p.read_text())
    except Exception:
        return []
    out: list[str] = []
    for it in ent.get("links") or []:
        u = it.get("url")
        if u: out.append(u)
    canonical = ent.get("canonical_links") or {}
    for k in ("homepage", "github", "publisher_page", "openreview_forum"):
        if canonical.get(k):
            out.append(canonical[k])
    return out


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

        title = str(entry.get("title", "")).strip()
        link = str(entry.get("link", "")).strip()

        # Determine which keys we still need.
        all_keys = ("arxiv", "openreview", "publisher_page", "homepage", "code", "dataset")
        missing: list[str] = [k for k in all_keys if not sources.get(k)]
        if args.only_missing and args.only_missing not in missing:
            continue
        if not missing:
            continue
        n += 1

        # 1. arxiv_id resolution.
        arxiv_id = entry.get("arxiv_id")
        if not arxiv_id:
            m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", link)
            arxiv_id = m.group(1) if m else None
        if not arxiv_id and title:
            arxiv_id = arxiv_id_by_title(session, title, sleep=args.sleep_seconds)
            if arxiv_id and args.verbose:
                print(f"[resolve] {title[:50]} → {arxiv_id}")
        if arxiv_id and not entry.get("arxiv_id"):
            entry["arxiv_id"] = arxiv_id
        if arxiv_id and "arxiv" in missing:
            sources["arxiv"] = f"https://arxiv.org/abs/{arxiv_id}"
            missing.remove("arxiv")

        # 2-5. Harvest candidate URLs.
        candidates: list[str] = []
        if arxiv_id:
            candidates.extend(harvest_urls_from_arxiv_abs(http_get(session, f"https://arxiv.org/abs/{arxiv_id}")))
            if args.sleep_seconds > 0: time.sleep(args.sleep_seconds)
            candidates.extend(hf_paper_links(session, arxiv_id, sleep=args.sleep_seconds))
            candidates.extend(semantic_scholar_links(session, arxiv_id, title, sleep=args.sleep_seconds))
        elif title:
            candidates.extend(semantic_scholar_links(session, None, title, sleep=args.sleep_seconds))

        # Publisher page (and openreview): scan the link itself if it
        # looks like a venue page.
        if link and (is_publisher_url(link) or "openreview.net" in link):
            candidates.extend(harvest_urls_from_html(http_get(session, link)))
            if args.sleep_seconds > 0: time.sleep(args.sleep_seconds)

        # paper_db — both stable canonical_links (already in sources)
        # and the looser links[] array.
        slug = arxiv_id and f"paper_arxiv_{arxiv_id.replace('.', '_')}"
        if slug:
            candidates.extend(paper_db_links(slug))

        # If we found a code link in candidates, follow it for README
        # cross-links (project page, dataset).
        followed_repo = False
        for url in candidates:
            if is_code_url(url) and not followed_repo:
                candidates.extend(github_readme_links(session, url, sleep=args.sleep_seconds))
                followed_repo = True
                break

        # 6. Classify candidates and fill missing keys (first match wins).
        changes: list[str] = []
        for url in candidates:
            if not url.startswith(("http://", "https://")): continue
            if "openreview" in missing and "openreview.net" in url:
                sources["openreview"] = url; missing.remove("openreview"); changes.append("+openreview")
            elif "publisher_page" in missing and is_publisher_url(url) and "openreview.net" not in url:
                sources["publisher_page"] = url; missing.remove("publisher_page"); changes.append("+publisher_page")
            elif "code" in missing and is_code_url(url):
                sources["code"] = url; missing.remove("code"); changes.append("+code")
            elif "dataset" in missing and is_dataset_url(url):
                sources["dataset"] = url; missing.remove("dataset"); changes.append("+dataset")
            elif "homepage" in missing and is_homepage_url(url):
                sources["homepage"] = url; missing.remove("homepage"); changes.append("+homepage")
            if not missing: break

        if changes or (entry.get("arxiv_id") and "arxiv" not in (entry.get("sources") or {})):
            entry["sources"] = sources
            if changes:
                total_changed += 1
                total_changes += len(changes)
                print(f"  {title[:60]:60s}  {' '.join(changes)}")

    print(f"\nentries enriched: {total_changed}    individual changes: {total_changes}")

    if args.write and total_changed > 0:
        out: list[dict[str, Any]] = []
        for d in docs:
            cp = dict(d)
            if cp.get("tldr"): cp["tldr"] = LiteralStr(str(cp["tldr"]))
            if cp.get("bibtex"): cp["bibtex"] = LiteralStr(str(cp["bibtex"]))
            out.append(cp)
        body = yaml.dump(out, sort_keys=False, allow_unicode=True, width=120, default_flow_style=False)
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
