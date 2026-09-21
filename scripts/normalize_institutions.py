#!/usr/bin/env python3
"""Canonicalise institution names in papers.yaml and adjacent.yaml.

One institution should appear under exactly one name, so that the site's
institution facet and the statistics charts group its papers together
instead of splitting them across spellings.

The mapping is a strict allow-list: a name is rewritten only when it
matches a rule exactly, and any name without a matching rule is left
untouched. That makes the pass safe to run over the whole corpus without
review -- it can normalise known institutions but can never mangle an
unfamiliar one.

Two details the rules depend on:

- Institution names containing a comma (``University of California,
  Berkeley``) are replaced in the raw string before any comma-splitting,
  because splitting first would produce two meaningless tokens.
- A leading ``The`` is dropped only when the remainder matches a rule, so
  ``The University of Tokyo`` survives while ``The Ohio State University``
  becomes ``OSU``.

Usage:
    uv run scripts/normalize_institutions.py            # dry run, print changes
    uv run scripts/normalize_institutions.py --write    # apply changes
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import regen  # noqa: E402  (needs REPO_ROOT on sys.path)

# ── Canonical mapping ──────────────────────────────────────────────────────
# Each key is a regex matched against a single institution name. The value is
# the canonical form. Order matters: the first matching rule wins.
#
# Convention:
#   - Use well-known abbreviations when universally recognised in ML/AI.
#   - Keep full names when no widely known abbreviation exists.
#   - Normalise "The X" / "X" inconsistencies to one form.
#   - Fix spelling variants and typos.
#   - A company and its research division are distinct entities; do not merge
#     them (Google vs Google Research, IBM vs IBM Research).

CANONICAL_MAP: list[tuple[str, str]] = [
    # ── Well-known abbreviations ──
    (r"^The Ohio State University$", "OSU"),
    (r"^Ohio State University$", "OSU"),
    (r"^Carnegie Mellon University$", "CMU"),
    (r"^School of Computer Science,?\s*Carnegie Mellon University$", "CMU"),
    (r"^Massachusetts Institute of Technology$", "MIT"),
    (r"^Georgia Institute of Technology$", "Georgia Tech"),
    (r"^Georgia Tech$", "Georgia Tech"),
    (r"^National University of Singapore$", "NUS"),
    (r"^Nanyang Technological University$", "NTU"),
    (r"^Seoul National University$", "SNU"),

    # UC system
    (r"^University of California,?\s*Berkeley$", "UC Berkeley"),
    (r"^UC Berkeley$", "UC Berkeley"),
    (r"^University of California,?\s*Los Angeles$", "UCLA"),
    (r"^UC Los Angeles$", "UCLA"),
    (r"^University of California,?\s*San Diego$", "UC San Diego"),
    (r"^UC San Diego$", "UC San Diego"),
    (r"^University of California,?\s*Santa Barbara$", "UC Santa Barbara"),
    (r"^University of California,?\s*Santa Cruz$", "UC Santa Cruz"),
    (r"^University of California,?\s*Davis$", "UC Davis"),
    (r"^University of California,?\s*Irvine$", "UC Irvine"),

    # UIUC
    (r"^University of Illinois Urbana-Champaign$", "UIUC"),
    (r"^University of Illinois at Urbana-Champaign$", "UIUC"),

    # UNC
    (r"^University of North Carolina at Chapel Hill$", "UNC"),
    (r"^UNC-Chapel Hill$", "UNC"),
    (r"^UNC Chapel Hill$", "UNC"),

    # UMich. "Michigan State University" is a different school and has no
    # rule here, so it passes through under its full name.
    (r"^The University of Michigan,?\s*Ann Arbor$", "UMich"),
    (r"^University of Michigan,?\s*Ann Arbor$", "UMich"),
    (r"^The University of Michigan$", "UMich"),
    (r"^University of Michigan$", "UMich"),
    (r"^UMich$", "UMich"),

    # UMass / UMD
    (r"^University of Massachusetts Amherst$", "UMass Amherst"),
    (r"^University of Maryland,?\s*College Park$", "UMD"),
    (r"^University of Maryland$", "UMD"),

    # Hong Kong universities
    (r"^The Hong Kong University of Science and Technology \(Guangzhou\)$", "HKUST(GZ)"),
    (r"^Hong Kong University of Science and Technology \(Guangzhou\)$", "HKUST(GZ)"),
    (r"^The Hong Kong University of Science and Technology$", "HKUST"),
    (r"^Hong Kong University of Science and Technology$", "HKUST"),
    (r"^The Chinese University of Hong Kong,?\s*Shenzhen$", "CUHK-Shenzhen"),
    (r"^Chinese University of Hong Kong,?\s*Shenzhen$", "CUHK-Shenzhen"),
    (r"^The Chinese University of Hong Kong \(Shenzhen\)$", "CUHK-Shenzhen"),
    (r"^Chinese University of Hong Kong \(Shenzhen\)$", "CUHK-Shenzhen"),
    (r"^The Chinese University of Hong Kong \(MMLab @ CUHK\)$", "CUHK MMLab"),
    (r"^The Chinese University of Hong Kong$", "CUHK"),
    (r"^Chinese University of Hong Kong$", "CUHK"),
    (r"^The University of Hong Kong$", "HKU"),
    (r"^University of Hong Kong$", "HKU"),
    (r"^The Hong Kong Polytechnic University$", "PolyU"),
    (r"^Hong Kong Polytechnic University$", "PolyU"),
    (r"^City University of Hong Kong$", "CityU"),

    # Drop "University" for globally unambiguous names
    (r"^Tsinghua University$", "Tsinghua"),
    (r"^Stanford University$", "Stanford"),
    (r"^Princeton University$", "Princeton"),
    (r"^Harvard University$", "Harvard"),
    (r"^Columbia University$", "Columbia"),
    (r"^Cornell University$", "Cornell"),
    (r"^University of Oxford$", "Oxford"),
    (r"^Zhejiang University$", "ZJU"),
    (r"^Peking University$", "PKU"),
    (r"^Fudan University$", "Fudan"),
    (r"^Nanjing University$", "NJU"),
    (r"^University College London$", "UCL"),
    (r"^Johns Hopkins University$", "JHU"),
    (r"^University of Science and Technology of China$", "USTC"),
    (r"^Chinese Academy of Sciences$", "CAS"),
    (r"^University of Southern California$", "USC"),
    (r"^Microsoft Research$", "MSR"),
    (r"^Microsoft Research Asia$", "MSR Asia"),
    (r"^The University of Texas at Austin$", "UT Austin"),
    (r"^University of Texas at Austin$", "UT Austin"),
    (r"^Technical University of Munich$", "TUM"),
    (r"^ETH Zurich$", "ETH"),

    (r"^Xi'an Jiaotong University$", "XJTU"),
    (r"^Xi'an Jiaotong University$", "XJTU"),
    (r"^Shanghai Jiao Tong University$", "SJTU"),
    (r"^Shanghai Jiaotong University$", "SJTU"),
    (r"^Shanghai Artificial Intelligence Laboratory$", "Shanghai AI Laboratory"),
    (r"^Shanghai AI Lab$", "Shanghai AI Laboratory"),

    # Companies / labs
    (r"^Zhipu AI$", "Zhipu"),
    (r"^Z\.AI$", "Zhipu"),

    # Montréal
    (r"^Universit[eé] de Montr[eé]al$", "Université de Montréal"),
    (r"^University of Montreal$", "Université de Montréal"),
    (r"^[EÉ]cole Polytechnique de Montr[eé]al$", "Polytechnique Montréal"),
    (r"^Mila - Quebec AI Research Institute$", "Mila"),
    (r"^Mila - Quebec AI Institute$", "Mila"),
    (r"^Mila Quebec AI Institute$", "Mila"),

    # Other "The" inconsistencies
    (r"^The George Washington University$", "George Washington University"),

    # Pengcheng
    (r"^Peng Cheng Laboratory$", "Pengcheng Laboratory"),

    # Typos
    (r"^University of Chinese Academy of Science$", "University of Chinese Academy of Sciences"),

    # Companies
    (r"^AntGroup$", "Ant Group"),
    (r"^Google Inc\.$", "Google"),
    (r"^Salesforce Research$", "Salesforce AI Research"),
    (r"^DeepMind$", "Google DeepMind"),

    # Xiaomi
    (r"^Xiaomi Inc\.?$", "Xiaomi"),
    (r"^Xiaomi Corporation$", "Xiaomi"),

    # State key labs normalization
    (r"^State Key Laboratory for General Artificial Intelligence$",
     "State Key Laboratory of General Artificial Intelligence"),
    (r"^State Key Laboratory for Novel Software Technology$",
     "National Key Laboratory for Novel Software Technology"),

    # ── Spelling and typography variants ──
    (r"^HKUST \(GZ\)$", "HKUST(GZ)"),
    (r"^Huawei Noah\u2019s Ark Lab$", "Huawei Noah's Ark Lab"),
    (r"^University of Wisconsin\u2013Madison$", "University of Wisconsin-Madison"),
    (r"^GraySwan AI$", "Gray Swan AI"),
    (r"^HiThink Research$", "Hithink Research"),
    (r"^IMean AI$", "iMean AI"),
    (r"^imean\.ai$", "iMean AI"),
    (r"^Shenzhen Institute of Advanced Technology$", "Shenzhen Institutes of Advanced Technology"),
    (r"^Tencent Inc\.?$", "Tencent"),
    (r"^Tencent AI Lab \(Seattle\)$", "Tencent AI Seattle Lab"),
    (r"^ZJU-UIUC Institute$", "ZJU-UIUC"),
    (r"^Aether AI Lab$", "Aether AI"),
    (r"^The Pennsylvania State University$", "Pennsylvania State University"),

    # ── Bare names expanded to the corpus-dominant full form ──
    (r"^McGill$", "McGill University"),
    (r"^Purdue$", "Purdue University"),
    (r"^Beihang$", "Beihang University"),
    (r"^ShanghaiTech$", "ShanghaiTech University"),
    (r"^Waseda$", "Waseda University"),
]

# Compile patterns once.
_COMPILED = [(re.compile(pat), repl) for pat, repl in CANONICAL_MAP]

# Institutions whose names contain a comma. These are replaced in the raw
# string BEFORE any comma-splitting, otherwise the split yields wrong tokens.
_COMMA_INSTITUTIONS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"University of California,\s*Berkeley"), "UC Berkeley"),
    (re.compile(r"University of California,\s*Los Angeles"), "UCLA"),
    (re.compile(r"University of California,\s*San Diego"), "UC San Diego"),
    (re.compile(r"University of California,\s*Santa Barbara"), "UC Santa Barbara"),
    (re.compile(r"University of California,\s*Santa Cruz"), "UC Santa Cruz"),
    (re.compile(r"University of California,\s*Davis"), "UC Davis"),
    (re.compile(r"University of California,\s*Irvine"), "UC Irvine"),
    (re.compile(r"University of Maryland,\s*College Park"), "UMD"),
    (re.compile(r"University of Michigan,\s*Ann Arbor"), "UMich"),
    (re.compile(r"The Chinese University of Hong Kong,\s*Shenzhen"), "CUHK-Shenzhen"),
    (re.compile(r"Chinese University of Hong Kong,\s*Shenzhen"), "CUHK-Shenzhen"),
    (re.compile(r"Harbin Institute of Technology,\s*Shenzhen"), "HIT-Shenzhen"),
    (re.compile(r"Harbin Institute of Technology,\s*Weihai"), "HIT-Weihai"),
    (re.compile(r"Baidu,\s*Inc\."), "Baidu Inc."),
]


def normalize_institution(name: str) -> str:
    """Return the canonical form of one institution name.

    Names that match no rule are returned unchanged apart from surrounding
    whitespace. A leading "The " is retried against the rules only if the
    stripped form matches one, so unknown "The ..." names keep their article.
    """
    stripped = name.strip()
    for pattern, replacement in _COMPILED:
        if pattern.match(stripped):
            return replacement
    if stripped.startswith("The "):
        without_the = stripped[4:]
        for pattern, replacement in _COMPILED:
            if pattern.match(without_the):
                return replacement
    return stripped


def normalize_entry(institutions: list[str]) -> list[str]:
    """Canonicalise one entry's institution list, preserving order and length.

    Each list item is mapped independently, so an institution name that
    legitimately contains a comma ("DAMO Academy, Alibaba Group") stays one
    entry. The single exception is a repair pass: two adjacent items whose
    concatenation exactly names one comma-containing institution
    (["University of California", "Berkeley"]) are merged into it.

    Duplicates are collapsed only when the mapping itself created them, so a
    list that already repeated a name keeps its original shape.
    """
    items = [str(i).strip() for i in institutions if str(i).strip()]

    # Repair pass: merge an adjacent pair that together names one institution.
    merged: list[str] = []
    i = 0
    while i < len(items):
        if i + 1 < len(items):
            combined = f"{items[i]}, {items[i + 1]}"
            hit = next(
                (repl for pat, repl in _COMMA_INSTITUTIONS if pat.fullmatch(combined)),
                None,
            )
            if hit is not None:
                merged.append(hit)
                i += 2
                continue
        merged.append(items[i])
        i += 1

    # Map each item: resolve a comma-containing name inside it, then apply rules.
    out: list[str] = []
    for item in merged:
        for pattern, replacement in _COMMA_INSTITUTIONS:
            item = pattern.sub(replacement, item)
        out.append(normalize_institution(item))

    # Collapse duplicates only if the mapping introduced them.
    if len(set(out)) < len(out) and len(set(items)) == len(items):
        deduped: list[str] = []
        for name in out:
            if name not in deduped:
                deduped.append(name)
        out = deduped
    return out


def normalize_papers(papers: list[dict]) -> int:
    """Rewrite every entry's institutions in place. Returns the change count."""
    changes = 0
    for p in papers:
        before = [str(i).strip() for i in (p.get("institutions") or [])]
        if not before:
            continue
        after = normalize_entry(before)
        if after != before:
            changes += 1
            print(f"  {p.get('title', '')[:70]}")
            print(f"    - {before}")
            print(f"    + {after}")
            p["institutions"] = after
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Canonicalise institution names in papers.yaml and adjacent.yaml."
    )
    parser.add_argument("--write", action="store_true", help="Apply changes in place.")
    args = parser.parse_args()

    canonical = regen.load_yaml(REPO_ROOT / "papers.yaml")
    adjacent = regen.load_yaml(REPO_ROOT / "adjacent.yaml")

    print("papers.yaml:")
    n1 = normalize_papers(canonical)
    print("adjacent.yaml:")
    n2 = normalize_papers(adjacent)
    total = n1 + n2

    if total == 0:
        print("\nNo institution changes needed.")
        return 0

    if args.write:
        regen.emit_yaml(canonical, adjacent)
        print(f"\nNormalized institutions in {total} entries.")
        return 0

    print(f"\n{total} entries would change. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
