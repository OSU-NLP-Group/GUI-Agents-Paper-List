"""
regen.py — canonical regen pipeline for paper_repo.

Reads `papers.yaml` + `adjacent.yaml` (the source of truth), sorts
by date (newest first), and writes them back. Then regenerates the
README and its assembly fragments + statistics PNGs.

Outputs:

  papers.yaml                                — re-sorted in place
  adjacent.yaml                              — re-sorted in place
  README.md                                  — recent 500 + template
  readme_template/
    paper_count.md
    paper_list_section.md
    env_grouping.md                          — links into the website
    keyword_grouping.md
    author_grouping.md
    statistics/quarterly_trend.png
    statistics/keyword_bar_chart.png

Run from `paper_repo/` root:
  uv run scripts/regen.py
"""

from __future__ import annotations

import calendar
import logging
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import pandas as pd
import yaml

# Resolve the repo root from cwd so the script can be run / tested
# inside a temp directory. Falls back to the script's own location.
def _detect_repo_root() -> Path:
    cwd = Path.cwd()
    if (cwd / "papers.yaml").exists():
        return cwd
    return Path(__file__).resolve().parents[1]


REPO_ROOT = _detect_repo_root()
READMEDIR = REPO_ROOT / "readme_template"

# ─── Logging ────────────────────────────────────────────────────────
log_dir = READMEDIR / "logs"
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


# ─── Markdown rendering for the README's recent-papers section ──────

def env_string(envs: list[str]) -> str:
    return ", ".join(f"[{e}]" for e in envs)


def kw_string(keywords: list[str]) -> str:
    return ", ".join(f"[{k}]" for k in keywords)


def md_entry_for_readme(p: dict[str, Any]) -> str:
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


# ─── BibTeX ─────────────────────────────────────────────────────────

def _ascii_token(text: str) -> str:
    """Fold to ASCII and keep only alphanumerics, lowercased."""
    folded = unicodedata.normalize("NFKD", text)
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    return "".join(c for c in folded if c.isalnum()).lower()


def _cite_key(paper: dict[str, Any], taken: set[str]) -> str:
    """Build a cite key of the form ``surnameYEARfirstword``.

    The surname comes from the first author, the year from ``date``, and the
    last part from the title's first whitespace-delimited token stripped of
    punctuation, so "VRL-Bench: Benchmarking ..." contributes "vrlbench". A
    numeric suffix is appended if the key is already taken.
    """
    authors = paper.get("authors") or []
    surname = _ascii_token(str(authors[0]).split()[-1]) if authors else "anon"
    year = str(paper.get("date", ""))[:4] or "0000"
    title = str(paper.get("title", "")).split()
    word = _ascii_token(title[0]) if title else "untitled"
    base = f"{surname}{year}{word}" or "entry"
    key = base
    n = 2
    while key in taken:
        key = f"{base}{n}"
        n += 1
    return key


def _venue_booktitle(publisher: str) -> str | None:
    """Return the booktitle for a venue, or None for preprints.

    A trailing presentation qualifier is dropped, so "ICLR 2025 (Poster)"
    yields "ICLR 2025".
    """
    pub = (publisher or "").strip()
    if not pub or pub.lower() in {"arxiv", "preprint"}:
        return None
    return re.sub(r"\s*\([^)]*\)\s*$", "", pub).strip() or None


def build_bibtex(paper: dict[str, Any], taken: set[str]) -> str:
    """Render a BibTeX entry for a paper that has none.

    Venue papers become ``@inproceedings`` with a ``booktitle``; everything
    else becomes ``@misc``. An arXiv identifier adds ``eprint`` and
    ``archivePrefix`` and supplies the URL; otherwise the entry's ``link`` is
    used.
    """
    key = _cite_key(paper, taken)
    title = str(paper.get("title", "")).strip()
    authors = " and ".join(str(a).strip() for a in (paper.get("authors") or []))
    year = str(paper.get("date", ""))[:4]
    booktitle = _venue_booktitle(str(paper.get("publisher", "")))
    arxiv_id = str(paper.get("arxiv_id", "") or "").strip()

    lines = [f"@{'inproceedings' if booktitle else 'misc'}{{{key},"]
    lines.append(f"  title = {{{title}}},")
    if authors:
        lines.append(f"  author = {{{authors}}},")
    if year:
        lines.append(f"  year = {{{year}}},")
    if booktitle:
        lines.append(f"  booktitle = {{{booktitle}}},")
    if arxiv_id:
        lines.append(f"  eprint = {{{arxiv_id}}},")
        lines.append("  archivePrefix = {arXiv},")
        lines.append(f"  url = {{https://arxiv.org/abs/{arxiv_id}}}")
    else:
        lines.append(f"  url = {{{paper.get('link', '')}}}")
    lines.append("}")
    return "\n".join(lines)


def fill_bibtex(groups: list[list[dict[str, Any]]]) -> int:
    """Populate ``bibtex`` on entries that lack it. Returns how many were added.

    Existing values are never overwritten, so hand-verified entries carrying
    ``bibtex_confirmed: true`` keep their text. Cite keys are made unique
    across every group passed in.
    """
    taken: set[str] = set()
    for papers in groups:
        for p in papers:
            existing = str(p.get("bibtex") or "")
            m = re.match(r"@\w+\{([^,]+),", existing.strip())
            if m:
                taken.add(m.group(1).strip())
    added = 0
    for papers in groups:
        for p in papers:
            if p.get("bibtex"):
                continue
            key_before = len(taken)
            entry = build_bibtex(p, taken)
            taken.add(re.match(r"@\w+\{([^,]+),", entry).group(1))
            p["bibtex"] = entry
            added += 1
            assert len(taken) > key_before
    return added


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


def render_readme(canonical: list[dict[str, Any]]) -> None:
    """Render README.md directly from papers.yaml + readme_template/template.md.

    No intermediate fragment files — the template's placeholders are
    substituted in-memory and the result is written straight to
    README.md.
    """
    SITE_BASE = "https://osu-nlp-group.github.io/GUI-Agents-Paper-List/papers/"
    total = len(canonical)

    # Recent-papers section
    max_readme_papers = 500
    is_truncated = total > max_readme_papers
    recent = canonical[:max_readme_papers] if is_truncated else canonical
    paper_entries = "\n".join(md_entry_for_readme(p) for p in recent)
    if is_truncated:
        heading = "## Recent Papers (from most recent to oldest)"
        note = (
            f"> This README shows the {max_readme_papers} most recent papers. "
            f"See [`papers.yaml`](papers.yaml) for the full structured source — "
            f"including BibTeX, OpenReview / publisher / homepage / code / dataset "
            f"links, and the `bibtex_confirmed` flag. For non-canonical adjacent "
            f"papers see [`adjacent.yaml`](adjacent.yaml)."
        )
    else:
        heading = "## All Papers (from most recent to oldest)"
        note = "> For non-canonical adjacent papers see [`adjacent.yaml`](adjacent.yaml)."
    paper_list_section = f"{heading}\n\n{note}\n\n{paper_entries}"

    # Author / env / keyword groupings — links into the website.
    per_line = 5
    author_counter: Counter[str] = Counter()
    for p in canonical:
        for a in p.get("authors", []) or []:
            author_counter[a.strip()] += 1
    top_authors = sorted(author_counter.items(), key=lambda x: x[1], reverse=True)[:20]
    author_links = [f"[{a} ({c})]({SITE_BASE}?author={quote_plus(a)})" for a, c in top_authors]
    author_lines = [" · ".join(author_links[i:i+per_line]) for i in range(0, len(author_links), per_line)]
    author_groups = "<br>".join(author_lines)

    env_keys = ["Web", "Desktop", "Mobile", "General GUI"]
    env_emoji = {"Web": "🌐", "Desktop": "🖥️", "Mobile": "📱", "General GUI": "🖼️"}
    env_parts: list[str] = []
    for env in env_keys:
        count = sum(1 for p in canonical if env in (p.get("envs") or []))
        env_parts.append(f"{env_emoji[env]} [{env} ({count})]({SITE_BASE}?env={quote_plus(env)})")
    env_groups = " · ".join(env_parts)

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
    kw_groups = "<br>".join(kw_lines)

    template_path = READMEDIR / "template.md"
    template = template_path.read_text(encoding="utf-8")
    rendered = (template
        .replace("{{insert_paper_count_here}}", str(total))
        .replace("{{insert_env_groups_here}}", env_groups)
        .replace("{{insert_keyword_groups_here}}", kw_groups)
        .replace("{{insert_author_groups_here}}", author_groups)
        .replace("{{insert_paper_list_section_here}}", paper_list_section)
    )
    (REPO_ROOT / "README.md").write_text(rendered.rstrip() + "\n", encoding="utf-8")


def emit_keyword_chart(canonical: list[dict[str, Any]]) -> None:
    """Quarterly trend + top-25 keyword PNGs. Best-effort — skipped
    silently when plotly isn't installed. Styling matches the
    pre-YAML version (sharp blue gradient, white background, large
    centered title).
    """
    try:
        import plotly.graph_objects as go
    except ImportError:
        return

    stats_dir = READMEDIR / "statistics"
    stats_dir.mkdir(parents=True, exist_ok=True)

    # ─── Top 25 keywords ───
    kw_counter: Counter[str] = Counter()
    for p in canonical:
        for k in p.get("keywords", []) or []:
            kw_counter[k.strip()] += 1
    top_kw = kw_counter.most_common(25)
    top_kw.reverse()
    kw_labels = [k for k, _ in top_kw]
    kw_values = [v for _, v in top_kw]

    if kw_values:
        fig_kw = go.Figure()
        fig_kw.add_trace(go.Bar(
            y=kw_labels, x=kw_values, orientation="h",
            text=kw_values, textposition="outside",
            textfont=dict(size=12, color="#444"),
            marker=dict(
                color=kw_values,
                colorscale=[[0, "#BFDBFE"], [0.4, "#3B82F6"], [1, "#1E3A8A"]],
                line=dict(width=0), cornerradius=3,
            ),
        ))
        fig_kw.update_layout(
            title=dict(text="Top 25 Research Keywords",
                       font=dict(size=20, color="#1a1a1a"), x=0.5),
            xaxis=dict(
                title=dict(text="Number of papers", font=dict(size=13, color="#666")),
                gridcolor="rgba(0,0,0,0.06)", zeroline=False,
                tickfont=dict(size=11, color="#888"),
                range=[0, max(kw_values) * 1.15],
            ),
            yaxis=dict(tickfont=dict(size=12, color="#444"), showgrid=False),
            plot_bgcolor="white", paper_bgcolor="white", showlegend=False,
            margin=dict(l=160, r=50, t=60, b=50),
            width=900, height=650, bargap=0.25,
        )
        try:
            fig_kw.write_image(stats_dir / "keyword_bar_chart.png", scale=2)
        except Exception:
            pass

    # ─── Quarterly publication trend ───
    rows = []
    for p in canonical:
        ts = parse_date_string(str(p.get("date", "")))
        if pd.isna(ts) or ts < pd.Timestamp("2023-01-01"):
            continue
        rows.append(ts)
    if not rows:
        return
    trend_df = pd.DataFrame({"ts": rows})
    trend_df["quarter"] = trend_df["ts"].dt.to_period("Q")
    quarterly = trend_df.groupby("quarter").size().reset_index(name="count")
    quarterly["mid_date"] = quarterly["quarter"].apply(
        lambda q: q.start_time + pd.Timedelta(days=45))
    quarterly["label"] = quarterly["quarter"].apply(
        lambda q: f"Q{q.quarter} {q.year}")
    counts = quarterly["count"].values

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=quarterly["mid_date"], y=counts,
        text=counts, textposition="outside",
        textfont=dict(size=13, color="#333"),
        width=60 * 86400000,
        marker=dict(
            color=counts,
            colorscale=[[0, "#93C5FD"], [0.5, "#3B82F6"], [1, "#1D4ED8"]],
            line=dict(width=0), cornerradius=4,
        ),
        hovertemplate="<b>%{customdata}</b><br>%{y} papers<extra></extra>",
        customdata=quarterly["label"],
    ))
    fig.update_layout(
        title=dict(
            text="GUI Agent Research: Quarterly Publication Trend",
            font=dict(size=22, color="#1a1a1a"), x=0.5,
        ),
        yaxis=dict(
            title=dict(text="Papers per quarter", font=dict(size=14, color="#666")),
            gridcolor="rgba(0,0,0,0.06)", zeroline=False,
            tickfont=dict(size=11, color="#888"),
            range=[0, max(counts) * 1.22],
        ),
        xaxis=dict(
            tickfont=dict(size=11, color="#666"), showgrid=False,
            tickvals=quarterly["mid_date"], ticktext=quarterly["label"],
            tickangle=0,
        ),
        plot_bgcolor="white", paper_bgcolor="white",
        showlegend=False,
        margin=dict(l=60, r=30, t=70, b=50),
        width=1100, height=480, bargap=0.3,
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
            f"papers.yaml not found at {canonical_path}. Are you running this from a paper_repo checkout?"
        )
    canonical = load_yaml(canonical_path)
    adjacent = load_yaml(adjacent_path)

    canonical = normalize_papers(canonical)
    adjacent = normalize_papers(adjacent)

    added = fill_bibtex([canonical, adjacent])
    print(f"Processed {len(canonical)} canonical and {len(adjacent)} adjacent papers.")
    if added:
        print(f"Generated BibTeX for {added} entr{'y' if added == 1 else 'ies'}.")

    emit_yaml(canonical, adjacent)
    render_readme(canonical)
    emit_keyword_chart(canonical)

    if _warnings:
        print(f"\n{len(_warnings)} warning(s) — see {log_dir / 'error.log'}")


if __name__ == "__main__":
    process()
