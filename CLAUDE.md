# CLAUDE.md - GUI Agents Paper List

## Project Overview

This repository is a curated list of research papers on direct GUI Agent research. It tracks ~600+ papers with structured metadata across web, mobile, desktop, and general-GUI settings.

**The source of truth is [`papers.yaml`](papers.yaml)** (and [`adjacent.yaml`](adjacent.yaml) for non-canonical adjacent entries). All other artifacts — `README.md`, the site, the per-axis statistics images — are auto-generated from these YAML files.

## Canonical Update Workflow

This repository is updated locally. GitHub Actions is no longer part of the official workflow.

After editing `papers.yaml`, regenerate every derived artifact locally with:

```bash
bash scripts/update_repo.sh
```

The pipeline runs `scripts/regen.py`, which:
1. Loads `papers.yaml` and `adjacent.yaml`.
2. Sorts entries newest-first, writes the YAML files back canonicalised (sorted, ISO date format).
3. Renders `README.md` directly from `readme_template/template.md` (no intermediate fragment files).
4. Emits `readme_template/statistics/{quarterly_trend,keyword_bar_chart}.png`.

Then review the diff, push, and deploy the site:

```bash
git status --short
git diff --stat
git add papers.yaml adjacent.yaml README.md readme_template/statistics scripts tests requirements.txt pyproject.toml uv.lock .gitignore CLAUDE.md
git commit -m "..."
git push
bash site/scripts/deploy.sh   # always deploy after any papers.yaml or site/ change
```

Dependencies are in `requirements.txt` and `pyproject.toml`. With `uv`:

```bash
uv sync
```

## Repository Structure

```
paper_repo/
├── papers.yaml                  ← canonical source of truth (canonical entries)
├── adjacent.yaml                ← canonical source of truth (adjacent entries)
├── README.md                    ← auto-generated; do not edit
├── CLAUDE.md                    ← this file
├── scripts/
│   ├── update_repo.sh           ← entrypoint; regenerates everything
│   ├── regen.py                 ← single-pass: sort YAML + render README + emit charts
│   └── sync_dates_from_paper_db.py   ← push verified dates from paper_db into papers.yaml
├── readme_template/
│   ├── template.md              ← README template with {{placeholders}}
│   ├── statistics/*.png         ← auto-generated stats charts
│   └── logs/                    ← regen warnings (.gitignored)
├── tests/
│   └── test_local_update_workflow.py
├── site/                        ← Astro static site → GitHub Pages
└── pyproject.toml / requirements.txt / uv.lock
```

## How to Add a Paper

Edit `papers.yaml` and append a YAML object with this schema. Only `title` and `link` are required; everything else is optional but most should be filled in:

```yaml
- title: "Paper title (preserve official capitalization)"
  link: https://arxiv.org/abs/2404.07972      # primary canonical link
  authors:
    - First Author
    - Second Author
  institutions: [OSU, CMU]
  date: "2024-04-11"                            # ISO YYYY-MM-DD, or YYYY-MM, or YYYY
  publisher: "NeurIPS 2024"                     # or "arXiv", "ICLR 2025 (Spotlight)", "TMLR", …
  envs: [Desktop]                               # one or more of: Web, Mobile, Desktop, General GUI
  keywords: [benchmark, OSWorld]                # comma-free list, no [] brackets
  tldr: |
    1–3 sentence factual summary of the paper.
  arxiv_id: "2404.07972"                        # optional; auto-populated if `link` is an arXiv URL
  sources:                                      # optional — extra discoverable links, all keys optional
    arxiv: https://arxiv.org/abs/2404.07972
    openreview: https://openreview.net/forum?id=…
    publisher_page: https://aclanthology.org/…  # ACL Anthology / NeurIPS Proceedings / etc.
    homepage: https://project-page.io/
    code: https://github.com/org/repo
    dataset: https://huggingface.co/datasets/…
  bibtex: |                                     # auto-generated if absent
    @inproceedings{author2024key,
      title = {{…}},
      …
    }
  bibtex_confirmed: false                       # set true after verifying against the official source
```

For `sources:` use what's available. ICLR / NeurIPS post-2017 papers often have OpenReview *as* the publisher's official page — fill `openreview` and leave `publisher_page` empty. ACL/EMNLP/NAACL papers have ACL Anthology as their `publisher_page`.

After editing, run `bash scripts/update_repo.sh`.

### Field Specifications

**Title.** Use the paper's canonical public title from the linked source. Normalize LaTeX or typography artifacts (e.g. `\textsc{...}`, `$^2$`) into readable plain text. Keep official abbreviations (`WALT`, `OS-ATLAS`, `Agent Q`) but don't invent new ones.

**Link.** Prefer project homepage > arXiv > venue page. Only one. If you have multiple official links, the others go in `sources:`.

**Authors.** Include all of them.

**Institutions.** Common abbreviations preferred (OSU, MIT, CMU). Use `Unknown` only if no source specifies one.

**Date.** Use the **earliest known public release date** (arXiv v1 / first preprint), not the latest revision. ISO format. If only month is known, use `"YYYY-MM"`; if only year, use `"YYYY"`.

**Publisher.** Use the publication venue, not a free-form status description. Format: `Venue Year` (e.g. `ICML 2024`, `NeurIPS 2025`, `CVPR 2026`). Use `arXiv` if only on arXiv. Presentation type (Poster/Oral/Spotlight) may appear in parentheses (e.g. `ICLR 2025 (Oral)`); the website collapses these into the canonical venue.

**Repository scope.**
- `papers.yaml` is for direct GUI papers only — papers whose main contribution directly studies GUI agents, computer-use agents, GUI grounding, GUI benchmarks, GUI safety, GUI reward, GUI RL, or other GUI-native problems.
- Don't keep pure search-API / agentic-search papers in the main list unless the paper also directly studies browser-based web agents.
- Don't keep non-GUI foundation-model papers in the main list just because later GUI work reuses them — curate those in `adjacent.yaml`.

**Adjacent papers (`adjacent.yaml`).**
- Optional supporting context, not part of the canonical main list.
- Use it for non-GUI-but-relevant papers: reused foundation models, general multimodal methods, general agent infrastructure, non-browser search-agent papers that materially inform GUI research.
- Adjacent entries are excluded from the README's main list, the env/keyword/author groupings, and the stats charts. The website exposes them at a separate `/adjacent` route.

**Env.**
- `Web` — Browser-based GUI agents interacting with real web pages
- `Mobile` — Android/iOS GUI agents
- `Desktop` — Computer-use agents on Windows/macOS/Linux
- `General GUI` — General GUI research not best expressed by a single concrete surface

Use multiple concrete envs (`[Desktop, Mobile, Web]`) when a paper genuinely spans them. `General GUI` is not shorthand for "all of the above" — use it only when the work is truly general-GUI research.

**Keywords.** Each keyword is a string in the YAML list (no `[]` wrapping). Include:
- the paper's commonly used abbreviation (`SeeAct`, `OSWorld`)
- one or two artifact types (`benchmark`, `dataset`, `framework`, `model`, `survey`)
- one to three core technical ideas / problem settings (`reward model`, `visual grounding`, `prompt injection`)

Avoid generic / scope-duplicate tags like `web navigation`, `LLM agent`, `GUI agent`, `multimodal`, `web`, `mobile`, `desktop`, `gui`, etc.

Artifact-type guidance:
- `benchmark` and `dataset` can co-occur. Use both when a paper introduces a benchmark *and* releases reusable training data.
- Keep `benchmark` even when more specific technical keys are present, if the benchmark itself is a core artifact.
- Be conservative with `framework`. In this repo it means an agent framework / scaffolding / runtime, not a generic "method framework" claim from the paper text.

Keyword casing should be consistent across the repo:
- General-concept keys are lowercase: `visual grounding`, `reward model`, `prompt injection`
- Official paper / benchmark / model names keep their canonical casing: `OSWorld`, `UI-TARS-2`, `SeeClick`, `Agent Q`

**TLDR.** 1–3 sentences, factual and contribution-first. Should answer:
1. What problem or gap is the paper targeting?
2. What does the paper actually introduce or show?
3. What is the strongest concrete outcome or takeaway?

Avoid generic openers ("This paper introduces …") when a more specific sentence is possible. Don't overstate beyond what the abstract supports.

## How to Verify a Paper's BibTeX

Auto-generated BibTeX may be approximate (especially the cite-key, booktitle/journal phrasing, DOI). To mark a paper's BibTeX as verified:

1. Open the venue's official BibTeX export (e.g. ACL Anthology's `Cite` button, or the OpenReview / venue proceedings page).
2. Replace the entry's `bibtex:` block in `papers.yaml` with the official text.
3. Set `bibtex_confirmed: true`.
4. Run `bash scripts/update_repo.sh`.

The website displays a **verified** badge on the Copy-BibTeX button when `bibtex_confirmed: true`.

## Task: Update the Website (site/)

Any change to files under `site/` (components, pages, styles, templates, issue templates) must be deployed to GitHub Pages after building. The site is **not** automatically deployed — a manual push is required every time.

```bash
cd paper_repo
bash site/scripts/deploy.sh
```

This script builds the Astro site and force-pushes the output to the `gh-pages` branch. It must be run after **every** site change — including UI tweaks, component edits, and `.github/ISSUE_TEMPLATE/` changes — not just after `papers.yaml` updates.

The live site is at https://osu-nlp-group.github.io/GUI-Agents-Paper-List/.

## Other Workflow Notes

- Errors during regen are logged to `readme_template/logs/error.log`.
- The README only renders the 500 most recent papers (GitHub truncates rendering at ~512KB). The full list is `papers.yaml`.
- `paper_db` (a separate workspace) reads `papers.yaml` directly.
