#!/usr/bin/env python3

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALL_PAPERS = ROOT / "ALL_PAPERS.md"
OUTPUT = ROOT / "REVIEW_TODO.md"


def extract_titles(markdown: str) -> list[str]:
    return [title.strip() for title in re.findall(r"^- \[(.*?)\]\(.*?\)$", markdown, re.MULTILINE)]


def main() -> int:
    titles = extract_titles(ALL_PAPERS.read_text(encoding="utf-8"))
    lines = [
        "# Review TODO",
        "",
        "This queue is the canonical manual-review tracker for `ALL_PAPERS.md`.",
        "",
        "Rules:",
        "- Only mark an item complete after a source-backed manual read of the paper content and a review of `Title`, `Institutions`, `Date`, `Publisher`, `Env`, `Key`, and `TLDR`.",
        "- Do not pre-check items based on prior ad-hoc edits; unchecked means the paper still needs a strict pass under this tracker.",
        f"- Total papers currently tracked: {len(titles)}",
        "",
        "Checklist:",
        "",
    ]
    lines.extend(f"- [ ] {title}" for title in titles)
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
