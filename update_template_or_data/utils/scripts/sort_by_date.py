"""
sort_by_date.py — canonical regen pipeline.

Reads papers.yaml + adjacent.yaml (the source of truth), sorts by
date (newest first), and emits:

  papers.yaml                   — re-sorted in place, all fields kept
  adjacent.yaml                 — re-sorted in place
  ALL_PAPERS.md                 — derived no-bibtex mirror (for paper_db
                                  ingestion + readers who prefer markdown)
  ADJACENT_PAPERS.md            — derived no-bibtex mirror
  README.md                     — recent 500 papers + assembled template
  update_template_or_data/
    paper_count.md
    paper_list_section.md
    env_grouping.md            — links into the website
    keyword_grouping.md
    author_grouping.md
    statistics/quarterly_trend.png
    statistics/keyword_bar_chart.png

Run from paper_repo/ root:
  uv run update_template_or_data/utils/scripts/sort_by_date.py
"""

from __future__ import annotations

import calendar
import logging
import os
import re
import shutil
import sys
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import pandas as pd
import yaml

# Resolve the repo root from cwd so the script can be run / tested
# inside a temp directory. Falls back to the script's own location
# when run directly (e.g. via `uv run …`).
def _detect_repo_root() -> Path:
    cwd = Path.cwd()
    if (cwd / "papers.yaml").exists() or (cwd / "ALL_PAPERS.md").exists():
        return cwd
    return Path(__file__).resolve().parents[3]


REPO_ROOT = _detect_repo_root()

# ─── Logging ────────────────────────────────────────────────────────
log_dir = REPO_ROOT / "update_template_or_data" / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=log_dir / "error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

_warnings: list[str] = []


def warn(msg: str) -> None:
    _warnings.append(msg)
    print(f"  WARNING: {msg}", file=sys.stderr)


# ─── YAML I/O — preserves block style, multi-line strings ───────────

class LiteralStr(str):
    pass


def _literal_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(LiteralStr, _literal_representer)


def load_yaml(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    docs = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not isinstance(docs, list):
        raise SystemExit(f"{path} did not parse as a list")
    return docs


def write_yaml(path: Path, papers: list[dict[str, Any]], header: str) -> None:
    # Convert known multi-line fields to LiteralStr.
    out: list[dict[str, Any]] = []
    for p in papers:
        cp = dict(p)
        if cp.get("tldr"):
            cp["tldr"] = LiteralStr(str(cp["tldr"]))
        if cp.get("bibtex"):
            cp["bibtex"] = LiteralStr(str(cp["bibtex"]))
        out.append(cp)
    body = yaml.dump(out, sort_keys=False, allow_unicode=True, width=120, default_flow_style=False)
    path.write_text(header + body, encoding="utf-8")


# ─── Date helpers ───────────────────────────────────────────────────

MONTHS_FULL = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
]


def parse_date_string(raw: str) -> pd.Timestamp:
    """Tolerant date parser.

    Accepts ISO YYYY-MM-DD, YYYY-MM, "Month DD, YYYY", "Month YYYY"
    and any year-only fallback. Returns a pandas Timestamp; for
    month-only inputs we anchor to the last day so sorting puts newer
    months ahead of older ones.
    """
    s = (raw or "").strip()
    m = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})$", s)
    if m:
        return pd.Timestamp(int(m[1]), int(m[2]), int(m[3]))
    m = re.match(r"^(\d{4})-(\d{1,2})$", s)
    if m:
        last = calendar.monthrange(int(m[1]), int(m[2]))[1]
        return pd.Timestamp(int(m[1]), int(m[2]), last)
    m = re.match(r"^([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})$", s)
    if m:
        idx = MONTHS_FULL.index(m[1].lower())
        return pd.Timestamp(int(m[3]), idx + 1, int(m[2]))
    m = re.match(r"^([A-Za-z]+)\s+(\d{4})$", s)
    if m:
        idx = MONTHS_FULL.index(m[1].lower())
        last = calendar.monthrange(int(m[2]), idx + 1)[1]
        return pd.Timestamp(int(m[2]), idx + 1, last)
    m = re.search(r"\b(20\d{2})\b", s)
    if m:
        return pd.Timestamp(int(m[1]), 12, 31)
    return pd.NaT


def display_date(raw: str, ts: pd.Timestamp) -> str:
    if pd.isna(ts):
        return raw or ""
    # Was it a month-only date? Then keep "Month YYYY" display.
    s = (raw or "").strip()
    if re.match(r"^(\d{4})-(\d{1,2})$|^[A-Za-z]+\s+\d{4}$", s):
        return f"{ts.strftime('%B')} {ts.year}"
    return ts.strftime("%B %d, %Y")


def date_to_iso(raw: str) -> str:
    ts = parse_date_string(raw)
    if pd.isna(ts):
        return raw or ""
    s = (raw or "").strip()
    if re.match(r"^(\d{4})-(\d{1,2})$|^[A-Za-z]+\s+\d{4}$", s):
        return f"{ts.year:04d}-{ts.month:02d}"
    return f"{ts.year:04d}-{ts.month:02d}-{ts.day:02d}"


# ─── Markdown derivation (no bibtex) ─────────────────────────────────

def env_string(envs: list[str]) -> str:
    return ", ".join(f"[{e}]" for e in envs)


def kw_string(keywords: list[str]) -> str:
    return ", ".join(f"[{k}]" for k in keywords)


def md_entry_canonical(p: dict[str, Any]) -> str:
    return (
        f"- [{p['title']}]({p.get('link', '')})\n"
        f"    - {', '.join(p.get('authors', []) or [])}\n"
        f"    - 🏛️ Institutions: {', '.join(p.get('institutions', []) or [])}\n"
        f"    - 📅 Date: {p.get('display_date', p.get('date', ''))}\n"
        f"    - 📑 Publisher: {p.get('publisher', '')}\n"
        f"    - 💻 Env: {env_string(p.get('envs', []) or [])}\n"
        f"    - 🔑 Key: {kw_string(p.get('keywords', []) or [])}\n"
        f"    - 📖 TLDR: {p.get('tldr', '')}\n"
    )


def md_entry_adjacent(p: dict[str, Any]) -> str:
    relation = p.get("relation") or "Adjacent to GUI research (not part of the canonical direct-GUI main list)"
    return (
        f"- [{p['title']}]({p.get('link', '')})\n"
        f"    - {', '.join(p.get('authors', []) or [])}\n"
        f"    - 🏛️ Institutions: {', '.join(p.get('institutions', []) or [])}\n"
        f"    - 📅 Date: {p.get('display_date', p.get('date', ''))}\n"
        f"    - 📑 Publisher: {p.get('publisher', '')}\n"
        f"    - 📌 Relation: {relation}\n"
        f"    - 🔑 Key: {kw_string(p.get('keywords', []) or [])}\n"
        f"    - 📖 TLDR: {p.get('tldr', '')}\n"
    )


# ─── Main pipeline ──────────────────────────────────────────────────

def normalize_papers(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sort newest-first; fill in display_date."""
    rows = []
    for p in papers:
        ts = parse_date_string(str(p.get("date", "")))
        p_norm = dict(p)
        p_norm["_ts"] = ts
        p_norm["display_date"] = display_date(str(p.get("date", "")), ts)
        # Re-write `date` to ISO so the YAML store stays canonical.
        iso = date_to_iso(str(p.get("date", "")))
        if iso:
            p_norm["date"] = iso
        rows.append(p_norm)
    # Sort by timestamp desc, title asc as deterministic tie-breaker.
    rows.sort(
        key=lambda r: (r.get("_ts") if r.get("_ts") is not None else pd.Timestamp.min, r.get("title", "")),
        reverse=False,
    )
    rows.sort(key=lambda r: r.get("_ts") if r.get("_ts") is not None else pd.Timestamp.min, reverse=True)
    return rows


def emit_yaml(canonical: list[dict[str, Any]], adjacent: list[dict[str, Any]]) -> None:
    canonical_clean = [{k: v for k, v in p.items() if k not in ("_ts", "display_date")} for p in canonical]
    adjacent_clean = [{k: v for k, v in p.items() if k not in ("_ts", "display_date")} for p in adjacent]
    write_yaml(
        REPO_ROOT / "papers.yaml",
        canonical_clean,
        "# papers.yaml — canonical source of truth for the GUI Agents Paper List.\n"
        "# Edit this file to add or correct papers. `bibtex` is auto-generated;\n"
        "# set `bibtex_confirmed: true` after verifying against the official source.\n\n",
    )
    write_yaml(
        REPO_ROOT / "adjacent.yaml",
        adjacent_clean,
        "# adjacent.yaml — non-canonical entries useful as supporting context.\n\n",
    )


def emit_derived_md(canonical: list[dict[str, Any]], adjacent: list[dict[str, Any]]) -> None:
    """No-bibtex mirrors of the YAML for paper_db ingestion + back-compat."""
    md = "\n".join(md_entry_canonical(p) for p in canonical)
    (REPO_ROOT / "ALL_PAPERS.md").write_text(md, encoding="utf-8")
    md = "\n".join(md_entry_adjacent(p) for p in adjacent)
    # Preserve adjacent header text.
    header = (
        "# Adjacent Papers for GUI Agent Research\n\n"
        "This file tracks papers that are important to the GUI-agent ecosystem but are **not** part of the canonical direct-GUI paper list in `ALL_PAPERS.md`.\n\n"
        "Typical examples include:\n"
        "- general-purpose foundation models later reused in GUI work\n"
        "- non-GUI agent benchmarks, infrastructure, and evaluation papers\n"
        "- general multimodal or prompting methods later adopted by GUI papers\n"
        "- Search-API or agentic-search papers that are not primarily browser-based GUI-agent research\n\n"
        "These entries are kept for reference only. The main list and generated environment pages are sourced only from `ALL_PAPERS.md`.\n\n"
    )
    (REPO_ROOT / "ADJACENT_PAPERS.md").write_text(header + md, encoding="utf-8")


def emit_readme_fragments(canonical: list[dict[str, Any]]) -> None:
    SITE_BASE = "https://osu-nlp-group.github.io/GUI-Agents-Paper-List/papers/"
    total = len(canonical)
    (REPO_ROOT / "update_template_or_data" / "paper_count.md").write_text(str(total), encoding="utf-8")

    # Recent papers section
    max_readme_papers = 500
    is_truncated = total > max_readme_papers
    recent = canonical[:max_readme_papers] if is_truncated else canonical
    paper_entries = "\n".join(md_entry_canonical(p) for p in recent)
    section_lines: list[str] = []
    section_lines.append("## Recent Papers (from most recent to oldest)" if is_truncated else "## All Papers (from most recent to oldest)")
    section_lines.append("")
    note_lines = [
        "> For adjacent, non-GUI-specific papers frequently referenced in GUI agent research, "
        "see [ADJACENT_PAPERS.md](ADJACENT_PAPERS.md).",
    ]
    if is_truncated:
        note_lines.append(">")
        note_lines.append(
            f"> This README shows the {max_readme_papers} most recent papers. "
            f"See [`papers.yaml`](papers.yaml) for the full structured source, or [`ALL_PAPERS.md`](ALL_PAPERS.md) for a derived markdown view."
        )
    section_lines.append("\n".join(note_lines))
    section_lines.append("")
    section_lines.append(paper_entries)
    (REPO_ROOT / "update_template_or_data" / "paper_list_section.md").write_text(
        "\n".join(section_lines), encoding="utf-8"
    )

    # Author / env / keyword groupings — link to the website
    author_counter: Counter[str] = Counter()
    for p in canonical:
        for a in p.get("authors", []) or []:
            author_counter[a.strip()] += 1
    top_authors = sorted(author_counter.items(), key=lambda x: x[1], reverse=True)[:20]
    author_links = [f"[{a} ({c})]({SITE_BASE}?author={quote_plus(a)})" for a, c in top_authors]
    per_line = 5
    author_lines = [" · ".join(author_links[i:i+per_line]) for i in range(0, len(author_links), per_line)]
    (REPO_ROOT / "update_template_or_data" / "author_grouping.md").write_text(
        "<br>".join(author_lines), encoding="utf-8"
    )

    env_keys = ["Web", "Desktop", "Mobile", "General GUI"]
    env_emoji = {"Web": "🌐", "Desktop": "🖥️", "Mobile": "📱", "General GUI": "🖼️"}
    env_parts: list[str] = []
    for env in env_keys:
        count = sum(1 for p in canonical if env in (p.get("envs") or []))
        env_parts.append(f"{env_emoji[env]} [{env} ({count})]({SITE_BASE}?env={quote_plus(env)})")
    (REPO_ROOT / "update_template_or_data" / "env_grouping.md").write_text(" · ".join(env_parts), encoding="utf-8")

    kw_counter: Counter[str] = Counter()
    for p in canonical:
        for k in p.get("keywords", []) or []:
            kw_counter[k.strip()] += 1
    predefined = ["model", "framework", "benchmark", "dataset", "safety", "survey"]
    pre_pairs = [(kw, kw_counter[kw]) for kw in predefined if kw in kw_counter]
    remaining = [(kw, c) for kw, c in kw_counter.most_common() if kw not in predefined]
    top_remaining = remaining[: 20 - len(predefined)]
    combined = sorted(pre_pairs + top_remaining, key=lambda x: -x[1])
    kw_links = [f"[{k} ({c})]({SITE_BASE}?key={quote_plus(k)})" for k, c in combined]
    kw_lines = [" · ".join(kw_links[i:i+per_line]) for i in range(0, len(kw_links), per_line)]
    (REPO_ROOT / "update_template_or_data" / "keyword_grouping.md").write_text(
        "<br>".join(kw_lines), encoding="utf-8"
    )

    # Drop legacy paper_by_* dirs if any remain.
    for legacy in ["paper_by_env", "paper_by_key", "paper_by_author"]:
        legacy_path = REPO_ROOT / legacy
        if legacy_path.is_dir():
            shutil.rmtree(legacy_path)


def emit_keyword_chart(canonical: list[dict[str, Any]]) -> None:
    """Quarterly trend + top-25 keyword PNGs. Best-effort — skipped
    silently when plotly isn't installed."""
    try:
        import plotly.graph_objects as go
    except ImportError:
        return

    stats_dir = REPO_ROOT / "update_template_or_data" / "statistics"
    stats_dir.mkdir(parents=True, exist_ok=True)

    kw_counter: Counter[str] = Counter()
    for p in canonical:
        for k in p.get("keywords", []) or []:
            kw_counter[k.strip()] += 1
    top = kw_counter.most_common(25)
    fig = go.Figure(go.Bar(
        x=[c for _, c in top],
        y=[k for k, _ in top],
        orientation="h",
        marker={"color": "#3057c4"},
    ))
    fig.update_layout(
        title="Top 25 keywords",
        xaxis_title="Papers",
        margin={"l": 200, "r": 16, "t": 64, "b": 40},
        plot_bgcolor="#fbf6ec",
        paper_bgcolor="#fbf6ec",
        font={"family": "Arial"},
        height=620,
        yaxis={"autorange": "reversed"},
    )
    try:
        fig.write_image(stats_dir / "keyword_bar_chart.png", scale=2)
    except Exception:
        pass

    # Quarterly trend
    by_q: Counter[str] = Counter()
    for p in canonical:
        ts = parse_date_string(str(p.get("date", "")))
        if pd.isna(ts):
            continue
        q = (ts.month - 1) // 3 + 1
        by_q[f"{ts.year} Q{q}"] += 1
    quarters = sorted(by_q.keys())
    fig = go.Figure(go.Scatter(
        x=quarters,
        y=[by_q[q] for q in quarters],
        mode="lines+markers",
        line={"color": "#3057c4", "width": 2.5},
        marker={"color": "#3057c4", "size": 6},
    ))
    fig.update_layout(
        title="Quarterly publication trend",
        xaxis_title="",
        yaxis_title="Papers",
        margin={"l": 50, "r": 16, "t": 64, "b": 60},
        plot_bgcolor="#fbf6ec",
        paper_bgcolor="#fbf6ec",
        font={"family": "Arial"},
        xaxis={"tickangle": 45},
        height=420,
    )
    try:
        fig.write_image(stats_dir / "quarterly_trend.png", scale=2)
    except Exception:
        pass


def process() -> None:
    canonical_path = REPO_ROOT / "papers.yaml"
    adjacent_path = REPO_ROOT / "adjacent.yaml"
    if not canonical_path.exists():
        raise SystemExit(
            "papers.yaml not found. Run `uv run scripts/migrate_to_yaml.py` once to create it from the legacy ALL_PAPERS.md."
        )
    canonical = load_yaml(canonical_path)
    adjacent = load_yaml(adjacent_path)

    canonical = normalize_papers(canonical)
    adjacent = normalize_papers(adjacent)

    print(f"Processed {len(canonical)} canonical and {len(adjacent)} adjacent papers.")

    emit_yaml(canonical, adjacent)
    emit_derived_md(canonical, adjacent)
    emit_readme_fragments(canonical)
    emit_keyword_chart(canonical)

    if _warnings:
        print(f"\n{len(_warnings)} warning(s) — see {log_dir / 'error.log'}")


if __name__ == "__main__":
    process()
