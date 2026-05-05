#!/usr/bin/env python3

"""sync_dates_from_paper_db.py — push verified earliest-publication
dates from `paper_db/papers/<id>/entity.json` into `papers.yaml`.

Reads papers.yaml, looks up each entry in paper_db (by URL or title),
takes the earliest of the candidate dates from any version, and
writes the corrected ISO `date:` field back. Auto-applies only to
arXiv-backed records (link-backed entries often mix venue dates,
proceedings dates, and later archival snapshots and need manual
review).
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTER_ROOT = ROOT.parent
PAPERS_YAML = ROOT / "papers.yaml"
PAPER_DB_DIR = OUTER_ROOT / "paper_db" / "papers"


@dataclass
class PaperDbRecord:
    paper_id: str
    title: str | None
    urls: set[str]
    earliest_date: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write updates back to papers.yaml")
    parser.add_argument("--limit", type=int, default=None, help="Only apply the first N updates")
    return parser.parse_args()


def normalize_title(title: str) -> str:
    return " ".join((title or "").split()).strip()


def load_paper_db() -> tuple[dict[str, PaperDbRecord], dict[str, list[PaperDbRecord]]]:
    by_url: dict[str, PaperDbRecord] = {}
    by_title: dict[str, list[PaperDbRecord]] = {}

    if not PAPER_DB_DIR.exists():
        return by_url, by_title

    for paper_dir in sorted(PAPER_DB_DIR.iterdir()):
        if not paper_dir.is_dir() or paper_dir.name == "paper_template":
            continue

        entity_path = paper_dir / "entity.json"
        if not entity_path.exists():
            continue
        entity = json.loads(entity_path.read_text(encoding="utf-8"))
        title = (entity.get("titles") or [{}])[0].get("text")
        urls: set[str] = set()

        for value in (entity.get("canonical_links") or {}).values():
            if value:
                urls.add(value)

        for item in entity.get("links") or []:
            value = item.get("url")
            if value:
                urls.add(value)

        earliest_date = None
        date_candidates: list[str] = []
        for version in entity.get("versions") or []:
            dates = version.get("dates") or {}
            for key in ("released_at", "submitted_at", "published_at"):
                value = dates.get(key)
                if value:
                    date_candidates.append(value)
        if date_candidates:
            earliest_date = sorted(date_candidates)[0]

        record = PaperDbRecord(
            paper_id=paper_dir.name,
            title=title,
            urls=urls,
            earliest_date=earliest_date,
        )

        for url in urls:
            by_url[url] = record
        if title:
            by_title.setdefault(normalize_title(title), []).append(record)

    return by_url, by_title


# ─── YAML I/O preserving block style ─────────────────────────────────

class LiteralStr(str):
    pass


def _literal_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(LiteralStr, _literal_representer)


def main() -> int:
    args = parse_args()
    by_url, by_title = load_paper_db()
    if not PAPERS_YAML.exists():
        raise SystemExit("papers.yaml not found")
    papers: list[dict[str, Any]] = yaml.safe_load(PAPERS_YAML.read_text(encoding="utf-8")) or []

    updates: list[tuple[str, str, str, str, str]] = []
    applied_count = 0

    for entry in papers:
        url = (entry.get("link") or "").strip()
        title = (entry.get("title") or "").strip()
        record = by_url.get(url)
        if record is None:
            title_matches = by_title.get(normalize_title(title), [])
            if len(title_matches) == 1:
                record = title_matches[0]
        if record is None or not record.earliest_date:
            continue

        # Auto-sync only arXiv-backed records.
        if not record.paper_id.startswith("paper_arxiv_"):
            continue

        current = (entry.get("date") or "").strip()
        target = record.earliest_date  # already YYYY-MM-DD
        if current == target:
            continue

        updates.append((record.paper_id, title, current, target, url))
        if args.limit is not None and applied_count >= args.limit:
            continue
        if args.write:
            entry["date"] = target
            applied_count += 1

    print(f"date_updates {len(updates)}")
    for row in updates:
        print("\t".join(row))

    if args.write:
        # Re-emit YAML with literal block scalars preserved.
        out: list[dict[str, Any]] = []
        for p in papers:
            cp = dict(p)
            if cp.get("tldr"):
                cp["tldr"] = LiteralStr(str(cp["tldr"]))
            if cp.get("bibtex"):
                cp["bibtex"] = LiteralStr(str(cp["bibtex"]))
            out.append(cp)
        body = yaml.dump(out, sort_keys=False, allow_unicode=True, width=120, default_flow_style=False)
        # Preserve the file header.
        header_end = 0
        existing = PAPERS_YAML.read_text(encoding="utf-8")
        for line in existing.splitlines():
            if line.startswith("#") or line.strip() == "":
                header_end += len(line) + 1
            else:
                break
        header = existing[:header_end]
        PAPERS_YAML.write_text(header + body, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
