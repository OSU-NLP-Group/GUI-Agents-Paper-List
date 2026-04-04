#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTER_ROOT = ROOT.parent
ALL_PAPERS_PATH = ROOT / "ALL_PAPERS.md"
PAPER_DB_DIR = OUTER_ROOT / "paper_db" / "papers"


ENTRY_SPLIT_RE = re.compile(r"\n(?=- \[)")
ENTRY_URL_RE = re.compile(r"^- \[(.*?)\]\((.*?)\)")
ENTRY_DATE_RE = re.compile(r"^(\s*- 📅 Date: )(.*)$", re.MULTILINE)


@dataclass
class PaperDbRecord:
    paper_id: str
    title: str | None
    urls: set[str]
    earliest_date: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write updates back to ALL_PAPERS.md")
    parser.add_argument("--limit", type=int, default=None, help="Only apply the first N updates")
    return parser.parse_args()


def iso_to_display(date_str: str) -> str:
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %d, %Y")
    if re.fullmatch(r"\d{4}/\d{1,2}", date_str):
        year, month = date_str.split("/")
        return datetime(int(year), int(month), 1).strftime("%B %Y")
    if re.fullmatch(r"\d{4}-\d{2}", date_str):
        year, month = date_str.split("-")
        return datetime(int(year), int(month), 1).strftime("%B %Y")
    return date_str


def normalize_title(title: str) -> str:
    return " ".join(title.split()).strip()


def load_paper_db() -> tuple[dict[str, PaperDbRecord], dict[str, list[PaperDbRecord]]]:
    by_url: dict[str, PaperDbRecord] = {}
    by_title: dict[str, list[PaperDbRecord]] = {}

    for paper_dir in sorted(PAPER_DB_DIR.iterdir()):
        if not paper_dir.is_dir() or paper_dir.name == "paper_template":
            continue

        entity = json.loads((paper_dir / "entity.json").read_text(encoding="utf-8"))
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


def main() -> int:
    args = parse_args()
    by_url, by_title = load_paper_db()
    text = ALL_PAPERS_PATH.read_text(encoding="utf-8")
    chunks = ENTRY_SPLIT_RE.split(text)

    updates: list[tuple[str, str, str, str, str]] = []
    applied_count = 0
    updated_chunks: list[str] = []

    for chunk in chunks:
        if not chunk.startswith("- ["):
            updated_chunks.append(chunk)
            continue

        lines = chunk.splitlines()
        match = ENTRY_URL_RE.match(lines[0])
        if not match:
            updated_chunks.append(chunk)
            continue

        title, url = match.groups()
        record = by_url.get(url)
        if record is None:
            title_matches = by_title.get(normalize_title(title), [])
            if len(title_matches) == 1:
                record = title_matches[0]

        if record is None or not record.earliest_date:
            updated_chunks.append(chunk)
            continue

        # Auto-sync only arXiv-backed records. Link-backed records often mix venue dates,
        # proceedings dates, and later archival snapshots, which require manual review.
        if not record.paper_id.startswith("paper_arxiv_"):
            updated_chunks.append(chunk)
            continue

        date_match = ENTRY_DATE_RE.search(chunk)
        if not date_match:
            updated_chunks.append(chunk)
            continue

        current_display = date_match.group(2).strip()
        target_display = iso_to_display(record.earliest_date)
        if current_display == target_display:
            updated_chunks.append(chunk)
            continue

        updates.append((record.paper_id, title, current_display, target_display, url))
        if args.limit is not None and applied_count >= args.limit:
            updated_chunks.append(chunk)
            continue

        updated_chunk = ENTRY_DATE_RE.sub(rf"\1{target_display}", chunk, count=1)
        updated_chunks.append(updated_chunk)
        applied_count += 1

    print(f"date_updates {len(updates)}")
    for row in updates:
        print("\t".join(row))

    if args.write:
        ALL_PAPERS_PATH.write_text("\n".join(updated_chunks), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
