"""
One-shot migration from ALL_PAPERS.md / ADJACENT_PAPERS.md to a
structured YAML store (papers.yaml / adjacent.yaml).

The YAML files become the canonical source of truth. Each entry
carries:
  - the original 9 fields
  - an auto-generated BibTeX block (LaTeX-paste-ready)
  - bibtex_confirmed: false
  - an optional `sources:` map populated, when available, from
    paper_db/papers/<id>/entity.json's canonical_links

Run from the paper_repo/ root:
    uv run scripts/migrate_to_yaml.py

It does NOT delete ALL_PAPERS.md — that file becomes a derived,
no-bibtex mirror written by sort_by_date.py from papers.yaml.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPER_DB = REPO_ROOT.parent / "paper_db" / "papers"

ENTRY_RE = re.compile(
    r"- \[(.*?)\]\((.*?)\)\s+"
    r"-\s*(.*?)\s+"
    r"- 🏛️\s*Institutions:\s*(.*?)\s+"
    r"- 📅\s*Date:\s*(.*?)\s+"
    r"- 📑\s*Publisher:\s*(.*?)\s+"
    r"(?:- 💻\s*Env:\s*(\[.*?\](?:,\s*\[.*?\])*)\s+)?"
    r"(?:- 📌\s*Relation:\s*(.*?)\s+)?"
    r"- 🔑\s*Key:\s*(.*?)\s+"
    r"- 📖\s*TLDR:\s*(.*?)\n",
    re.DOTALL,
)

MONTHS_FULL = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
]


def parse_date(raw: str) -> dict:
    s = raw.strip()
    # Month YYYY
    m = re.match(r"^([A-Za-z]+)\s+(\d{4})$", s)
    if m:
        idx = MONTHS_FULL.index(m.group(1).lower())
        return {"iso": f"{m.group(2)}-{idx+1:02d}", "year": int(m.group(2)), "month": idx + 1, "month_only": True}
    # Month DD, YYYY
    m = re.match(r"^([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})$", s)
    if m:
        idx = MONTHS_FULL.index(m.group(1).lower())
        return {"iso": f"{m.group(3)}-{idx+1:02d}-{int(m.group(2)):02d}", "year": int(m.group(3)), "month": idx + 1, "month_only": False}
    # YYYY-MM-DD
    m = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})$", s)
    if m:
        return {"iso": f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}", "year": int(m.group(1)), "month": int(m.group(2)), "month_only": False}
    # year only
    m = re.search(r"\b(20\d{2})\b", s)
    if m:
        return {"iso": f"{m.group(1)}-12-31", "year": int(m.group(1)), "month": 12, "month_only": False}
    return {"iso": "", "year": 0, "month": 0, "month_only": False}


def split_csv(s: str) -> list[str]:
    return [p.strip() for p in s.split(",") if p.strip()]


def parse_keywords(s: str) -> list[str]:
    return [re.sub(r"^\[|\]$", "", k.strip()).strip() for k in s.split(",") if k.strip()]


def parse_envs(s: str | None) -> list[str]:
    if not s:
        return []
    return [m.group(1).strip() for m in re.finditer(r"\[(.*?)\]", s)]


def arxiv_id_from(link: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", link, re.IGNORECASE)
    return m.group(1) if m else None


def slug_for(title: str, link: str) -> str:
    aid = arxiv_id_from(link)
    if aid:
        return f"paper_arxiv_{aid.replace('.', '_')}"
    h = hashlib.sha1(link.encode("utf-8")).hexdigest()[:12]
    return f"paper_link_{h}"


# ─── BibTeX generation (mirrors site/src/lib/venues.ts logic) ────────

# The Python migration is permitted a coarser version of the venues
# normalizer — it just drops the presentation parenthetical and
# leaves the rest. The site's normalizer (TS) gives the canonical
# value at render time.
_PRESENTATION_RE = re.compile(r"\s*\((?:Poster|Oral|Spotlight|Highlight|Findings)\)\s*$", re.IGNORECASE)
_JOURNAL_HEAD_RE = re.compile(r"^(TMLR|JMLR|TPAMI|TASLP|TACL|Nature|Science|PNAS)\b", re.IGNORECASE)


def esc_bib(s: str) -> str:
    s = s.replace("\\", "\\textbackslash ")
    s = re.sub(r"([&%$#_{}])", r"\\\1", s)
    s = s.replace("~", "\\~{}").replace("^", "\\^{}")
    return s


def bib_key(authors: list[str], title: str, year: int) -> str:
    last = (authors[0] if authors else "anon").split()[-1].lower()
    last = re.sub(r"[^a-z]", "", last) or "anon"
    word = next((re.sub(r"[^a-z0-9]", "", w.lower()) for w in title.split() if len(w) > 3), "paper")
    return f"{last}{year if year > 0 else ''}{word}"


def build_bibtex(authors: list[str], title: str, year: int, publisher: str, link: str, arxiv_id: str | None) -> str:
    venue = _PRESENTATION_RE.sub("", publisher).strip()
    is_arxiv = (not venue) or re.match(r"^arxiv$", venue, re.IGNORECASE)
    is_journal = bool(_JOURNAL_HEAD_RE.match(venue))

    fields: list[tuple[str, str]] = []
    fields.append(("title", f"{{{esc_bib(title)}}}"))
    fields.append(("author", f"{{{' and '.join(esc_bib(a) for a in authors) or 'Unknown'}}}"))
    if year > 0:
        fields.append(("year", f"{{{year}}}"))

    key = bib_key(authors, title, year)

    if is_arxiv and arxiv_id:
        fields.append(("eprint", f"{{{arxiv_id}}}"))
        fields.append(("archivePrefix", "{arXiv}"))
        fields.append(("url", f"{{https://arxiv.org/abs/{arxiv_id}}}"))
        kind = "@misc"
    elif is_arxiv:
        fields.append(("howpublished", f"{{{esc_bib(publisher or 'Preprint')}}}"))
        fields.append(("url", f"{{{link}}}"))
        kind = "@misc"
    elif is_journal:
        fields.append(("journal", f"{{{esc_bib(venue)}}}"))
        if arxiv_id:
            fields.append(("eprint", f"{{{arxiv_id}}}"))
        fields.append(("url", f"{{{link}}}"))
        kind = "@article"
    else:
        fields.append(("booktitle", f"{{{esc_bib(venue)}}}"))
        if arxiv_id:
            fields.append(("eprint", f"{{{arxiv_id}}}"))
            fields.append(("archivePrefix", "{arXiv}"))
        fields.append(("url", f"{{{link}}}"))
        kind = "@inproceedings"

    body = ",\n".join(f"  {k} = {v}" for k, v in fields)
    return f"{kind}{{{key},\n{body}\n}}"


# ─── Sources from paper_db ───────────────────────────────────────────

def sources_from_paper_db(slug: str, arxiv_id: str | None) -> dict[str, str]:
    """Build the `sources:` block for an entry.

    Schema (all keys optional):
      arxiv:          arXiv abs page                (auto-filled when known)
      openreview:     OpenReview forum page         (note: for ICLR/NeurIPS
                                                    post-2017 this is often
                                                    *also* the publisher
                                                    page; keep it here, leave
                                                    publisher_page empty)
      publisher_page: venue's proceedings page      (e.g. ACL Anthology,
                                                    NeurIPS Proceedings)
      homepage:       project / paper homepage
      code:           code repo (GitHub etc.)
      dataset:        dataset / benchmark artifact  (HuggingFace, Zenodo, …)

    paper_db's entity.json populates whatever it has discovered; the
    rest are left for contributors to fill in.
    """
    out: dict[str, str] = {}
    if arxiv_id:
        out["arxiv"] = f"https://arxiv.org/abs/{arxiv_id}"
    path = PAPER_DB / slug / "entity.json"
    if not path.exists():
        return out
    try:
        data = json.loads(path.read_text())
    except Exception:
        return out
    canonical = data.get("canonical_links") or {}
    if canonical.get("openreview_forum"):
        out["openreview"] = canonical["openreview_forum"]
    if canonical.get("publisher_page"):
        out["publisher_page"] = canonical["publisher_page"]
    if canonical.get("homepage"):
        out["homepage"] = canonical["homepage"]
    if canonical.get("github"):
        out["code"] = canonical["github"]
    return out


# ─── Migration ───────────────────────────────────────────────────────

def parse_md_blocks(markdown: str, source_kind: str) -> list[dict[str, Any]]:
    """Parse a single markdown file into a list of paper dicts.

    Uses a line-based scan (the same shape as the site's parser) since
    a regex with the s/DOTALL flag chokes on the variant adjacent
    schema. We split on title lines and then read the indented
    sub-fields linearly.
    """
    out: list[dict[str, Any]] = []
    lines = markdown.splitlines()
    title_re = re.compile(r"^- \[(.*?)\]\((.*?)\)\s*$")
    indent_re = re.compile(r"^ {2,}- (.*)$")
    # Field labels handled here; see PaperBrowser parser for parity.
    label_re = {
        "institutions": re.compile(r"^🏛️?\s*Institutions:\s*(.*)$"),
        "date":         re.compile(r"^📅\s*Date:\s*(.*)$"),
        "publisher":    re.compile(r"^📑\s*Publisher:\s*(.*)$"),
        "env":          re.compile(r"^💻\s*Env:\s*(.*)$"),
        "key":          re.compile(r"^🔑\s*Key:\s*(.*)$"),
        "tldr":         re.compile(r"^📖\s*TLDR:\s*(.*)$"),
        "relation":     re.compile(r"^📌\s*Relation:\s*(.*)$"),
    }

    i = 0
    while i < len(lines):
        m = title_re.match(lines[i])
        if not m:
            i += 1
            continue
        title = m.group(1).strip()
        link = m.group(2).strip()
        i += 1
        fields: dict[str, str] = {}
        first_sub = True
        while i < len(lines):
            sub = lines[i]
            if sub.strip() == "":
                break
            if title_re.match(sub):
                break
            im = indent_re.match(sub)
            if not im:
                break
            inner = im.group(1)
            matched = False
            for key, rgx in label_re.items():
                lm = rgx.match(inner.replace("\xa0", " ").lstrip())
                if lm:
                    if key == "tldr":
                        # consume continuation lines
                        buf = lm.group(1).strip()
                        j = i + 1
                        while j < len(lines):
                            nxt = lines[j]
                            if nxt.strip() == "" or title_re.match(nxt):
                                break
                            if indent_re.match(nxt):
                                inner_next = indent_re.match(nxt).group(1)  # type: ignore
                                if any(rgx2.match(inner_next.replace("\xa0", " ").lstrip()) for rgx2 in label_re.values()):
                                    break
                            buf += " " + nxt.strip()
                            j += 1
                        fields["tldr"] = buf
                        i = j - 1
                    else:
                        fields[key] = lm.group(1).strip()
                    matched = True
                    break
            if not matched and first_sub and "authors" not in fields:
                fields["authors"] = inner.strip()
            first_sub = False
            i += 1

        if not title:
            continue
        d = parse_date(fields.get("date", ""))
        arxiv_id = arxiv_id_from(link)
        slug = slug_for(title, link)
        entry: dict[str, Any] = {
            "title": title,
            "link": link,
            "authors": split_csv(fields.get("authors", "")),
            "institutions": split_csv(fields.get("institutions", "")),
            "date": d["iso"] or fields.get("date", "").strip(),
            "publisher": fields.get("publisher", "").strip(),
            "envs": parse_envs(fields.get("env")),
            "keywords": parse_keywords(fields.get("key", "")),
            "tldr": fields.get("tldr", "").strip(),
        }
        if fields.get("relation"):
            entry["relation"] = fields["relation"].strip()
        if arxiv_id:
            entry["arxiv_id"] = arxiv_id
        sources = sources_from_paper_db(slug, arxiv_id)
        if sources:
            entry["sources"] = sources
        # BibTeX (only generate for canonical entries — adjacent papers
        # are not the kind of thing one cites from a list).
        if source_kind == "canonical":
            entry["bibtex"] = build_bibtex(
                entry["authors"], title, d["year"], entry["publisher"], link, arxiv_id,
            )
            entry["bibtex_confirmed"] = False
        out.append(entry)
    return out


def yaml_dump(papers: list[dict[str, Any]]) -> str:
    """Pretty YAML — block style, key order preserved, BibTeX as
    literal block scalar so it stays human-readable."""

    class LiteralStr(str):
        pass

    def literal_representer(dumper, data):
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")

    yaml.add_representer(LiteralStr, literal_representer)

    # Convert known multi-line fields to LiteralStr.
    for p in papers:
        if "tldr" in p and p["tldr"]:
            p["tldr"] = LiteralStr(p["tldr"])
        if "bibtex" in p and p["bibtex"]:
            p["bibtex"] = LiteralStr(p["bibtex"])

    return yaml.dump(
        papers,
        sort_keys=False,
        allow_unicode=True,
        width=120,
        default_flow_style=False,
    )


def main() -> int:
    canonical_md = (REPO_ROOT / "ALL_PAPERS.md").read_text(encoding="utf-8")
    adjacent_md = (REPO_ROOT / "ADJACENT_PAPERS.md").read_text(encoding="utf-8")

    canonical = parse_md_blocks(canonical_md, "canonical")
    adjacent = parse_md_blocks(adjacent_md, "adjacent")

    print(f"Parsed {len(canonical)} canonical and {len(adjacent)} adjacent papers.")

    canonical_path = REPO_ROOT / "papers.yaml"
    adjacent_path = REPO_ROOT / "adjacent.yaml"

    canonical_yaml = yaml_dump(canonical)
    adjacent_yaml = yaml_dump(adjacent)

    canonical_path.write_text(
        "# papers.yaml — canonical source of truth for the GUI Agents Paper List\n"
        "# Edit this file to add or correct papers.\n"
        "# `bibtex` is auto-generated; set `bibtex_confirmed: true` after you\n"
        "# verify a record against the official source (e.g. copy/paste from\n"
        "# the venue's BibTeX export).\n\n"
        + canonical_yaml,
        encoding="utf-8",
    )
    adjacent_path.write_text(
        "# adjacent.yaml — non-canonical entries useful as supporting context\n\n"
        + adjacent_yaml,
        encoding="utf-8",
    )
    print(f"Wrote {canonical_path}")
    print(f"Wrote {adjacent_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
