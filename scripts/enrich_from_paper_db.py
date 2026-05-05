"""enrich_from_paper_db.py — fill missing fields in papers.yaml from
verified data in `paper_db/papers/<id>/entity.json`.

Conservative by design: never overwrites a value that already exists in
the YAML. Only adds:

  * sources.{arxiv,openreview,publisher_page,homepage,code} — when a
    canonical_link is known and the YAML doesn't already have that key
  * institutions — when the YAML's institutions list is empty AND
    paper_db has at least one institution recorded
  * arxiv_id — when missing and the link or paper_db tells us one
  * date — only when the YAML's date is missing entirely (does not
    override existing dates; use sync_dates_from_paper_db.py for that)

Run from paper_repo/ root:
    uv run scripts/enrich_from_paper_db.py            # dry run
    uv run scripts/enrich_from_paper_db.py --write    # apply
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
PAPER_DB_DIR = ROOT.parent / "paper_db" / "papers"
PAPERS_YAML = ROOT / "papers.yaml"


# ─── YAML I/O preserving block style ────────────────────────────────

class LiteralStr(str):
    pass


def _literal_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(LiteralStr, _literal_representer)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write changes back to papers.yaml")
    parser.add_argument("--limit", type=int, default=None, help="Stop after N changes (dry run still reports all)")
    return parser.parse_args()


def normalize_title(title: str) -> str:
    return " ".join((title or "").split()).strip()


def load_paper_db() -> tuple[dict[str, dict], dict[str, list[dict]]]:
    by_url: dict[str, dict] = {}
    by_title: dict[str, list[dict]] = {}
    if not PAPER_DB_DIR.exists():
        return by_url, by_title
    for paper_dir in sorted(PAPER_DB_DIR.iterdir()):
        if not paper_dir.is_dir() or paper_dir.name == "paper_template":
            continue
        ent_path = paper_dir / "entity.json"
        if not ent_path.exists():
            continue
        try:
            entity = json.loads(ent_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        title = (entity.get("titles") or [{}])[0].get("text") or ""
        urls: set[str] = set()
        for v in (entity.get("canonical_links") or {}).values():
            if v: urls.add(v)
        for it in entity.get("links") or []:
            v = it.get("url")
            if v: urls.add(v)
        record = {"paper_id": paper_dir.name, "entity": entity, "urls": urls}
        for u in urls:
            by_url[u] = record
        if title:
            by_title.setdefault(normalize_title(title), []).append(record)
    return by_url, by_title


def lookup(entry: dict, by_url, by_title) -> dict | None:
    rec = by_url.get(entry.get("link", "").strip())
    if rec:
        return rec
    matches = by_title.get(normalize_title(entry.get("title", "")), [])
    if len(matches) == 1:
        return matches[0]
    return None


def arxiv_id_from_link(link: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", link or "", re.I)
    return m.group(1) if m else None


SOURCE_KEYS = (
    ("arxiv",          ("arxiv_abs",)),
    ("openreview",     ("openreview_forum",)),
    ("publisher_page", ("publisher_page",)),
    ("homepage",       ("homepage",)),
    ("code",           ("github",)),
)


def enrich_entry(entry: dict, record: dict) -> list[str]:
    """Mutate `entry` in place; return a list of human-readable change descriptions."""
    changes: list[str] = []
    canonical = record["entity"].get("canonical_links") or {}

    # arxiv_id
    if not entry.get("arxiv_id"):
        aid = arxiv_id_from_link(entry.get("link", ""))
        if not aid:
            arx = canonical.get("arxiv_abs") or ""
            aid = arxiv_id_from_link(arx)
        if aid:
            entry["arxiv_id"] = aid
            changes.append(f"+arxiv_id={aid}")

    # sources
    sources = entry.get("sources")
    if sources is None:
        sources = {}
    if isinstance(sources, dict):
        # Fill arxiv if known
        aid = entry.get("arxiv_id")
        if aid and not sources.get("arxiv"):
            sources["arxiv"] = f"https://arxiv.org/abs/{aid}"
            changes.append("+sources.arxiv")
        for yaml_key, candidates in SOURCE_KEYS:
            if sources.get(yaml_key):
                continue
            for cand in candidates:
                v = canonical.get(cand)
                if v:
                    sources[yaml_key] = v
                    changes.append(f"+sources.{yaml_key}")
                    break
        if sources:
            entry["sources"] = sources

    # institutions — only if empty
    cur_inst = entry.get("institutions") or []
    if not cur_inst:
        db_inst = record["entity"].get("institutions") or []
        # entity.json's institutions is a list of {"name": ..., ...}
        names = [i.get("name") for i in db_inst if isinstance(i, dict) and i.get("name")]
        if names:
            entry["institutions"] = names
            changes.append(f"+institutions={len(names)}")

    return changes


def main() -> int:
    args = parse_args()
    by_url, by_title = load_paper_db()
    if not PAPERS_YAML.exists():
        raise SystemExit("papers.yaml not found")
    raw = PAPERS_YAML.read_text(encoding="utf-8")
    docs: list[dict] = yaml.safe_load(raw) or []

    total_changed = 0
    total_changes = 0
    for entry in docs:
        if not isinstance(entry, dict):
            continue
        rec = lookup(entry, by_url, by_title)
        if rec is None:
            continue
        changes = enrich_entry(entry, rec)
        if changes:
            total_changed += 1
            total_changes += len(changes)
            print(f"  {entry.get('title','')[:60]:60s}  {' '.join(changes)}")
            if args.limit is not None and total_changed >= args.limit:
                break

    print(f"\nentries enriched: {total_changed}    individual changes: {total_changes}")

    if args.write and total_changed > 0:
        # Re-emit, preserving block scalars and the file header.
        out: list[dict[str, Any]] = []
        for p in docs:
            cp = dict(p)
            if cp.get("tldr"):
                cp["tldr"] = LiteralStr(str(cp["tldr"]))
            if cp.get("bibtex"):
                cp["bibtex"] = LiteralStr(str(cp["bibtex"]))
            out.append(cp)
        body = yaml.dump(out, sort_keys=False, allow_unicode=True, width=120, default_flow_style=False)
        # Preserve header comment block.
        header_end = 0
        for line in raw.splitlines(keepends=True):
            if line.startswith("#") or line.strip() == "":
                header_end += len(line)
            else:
                break
        header = raw[:header_end]
        PAPERS_YAML.write_text(header + body, encoding="utf-8")
        print(f"\nwrote {PAPERS_YAML}")
    elif args.write:
        print("\nno changes to write")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
