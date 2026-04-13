#!/usr/bin/env python3
"""Normalize institution names in ALL_PAPERS.md.

Applies a canonical mapping so the same institution always appears the same way.
Only modifies lines matching the Institutions field pattern.

Usage:
    python3 scripts/normalize_institutions.py          # dry-run, print changes
    python3 scripts/normalize_institutions.py --write   # apply changes
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILE = REPO_ROOT / "ALL_PAPERS.md"

# ── Canonical mapping ──────────────────────────────────────────────────────
# Each key is a regex pattern (case-sensitive) matched against individual
# institution tokens (comma-separated).  The value is the canonical form.
# Order matters: earlier rules take priority when multiple could match.
#
# Convention:
#   - Use well-known abbreviations when universally recognised in ML/AI.
#   - Keep full names when no widely known abbreviation exists.
#   - Normalise "The X" / "X" inconsistencies to one form.
#   - Fix spelling variants and typos.

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
]

# Compile patterns once
_COMPILED = [(re.compile(pat), repl) for pat, repl in CANONICAL_MAP]

INST_LINE_RE = re.compile(r"^(    - 🏛️ Institutions: )(.+)$")

# Institutions whose names contain commas.  These must be replaced in the raw
# string BEFORE we split on commas, otherwise the split produces wrong tokens.
# Each entry is (pattern applied to the full Institutions value, replacement).
_COMMA_INSTITUTIONS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"University of California,\s*Berkeley"), "UC Berkeley"),
    (re.compile(r"University of California,\s*Los Angeles"), "UCLA"),
    (re.compile(r"University of California,\s*San Diego"), "UC San Diego"),
    (re.compile(r"University of California,\s*Santa Barbara"), "UC Santa Barbara"),
    (re.compile(r"University of California,\s*Santa Cruz"), "UC Santa Cruz"),
    (re.compile(r"University of California,\s*Davis"), "UC Davis"),
    (re.compile(r"University of California,\s*Irvine"), "UC Irvine"),
    (re.compile(r"University of Maryland,\s*College Park"), "UMD"),
    (re.compile(r"The Chinese University of Hong Kong,\s*Shenzhen"), "CUHK-Shenzhen"),
    (re.compile(r"Chinese University of Hong Kong,\s*Shenzhen"), "CUHK-Shenzhen"),
    (re.compile(r"Harbin Institute of Technology,\s*Shenzhen"), "HIT-Shenzhen"),
    (re.compile(r"Harbin Institute of Technology,\s*Weihai"), "HIT-Weihai"),
]


def normalize_institution(name: str) -> str:
    """Apply canonical mapping to a single institution name."""
    stripped = name.strip()
    for pattern, replacement in _COMPILED:
        if pattern.match(stripped):
            return replacement
    return stripped


def normalize_line(line: str) -> str | None:
    """Normalize an Institutions line. Returns None if unchanged."""
    m = INST_LINE_RE.match(line)
    if not m:
        return None
    prefix, institutions_str = m.group(1), m.group(2)

    # Phase 1: replace comma-containing institution names before splitting
    for pattern, replacement in _COMMA_INSTITUTIONS:
        if replacement is not None:
            institutions_str = pattern.sub(replacement, institutions_str)

    # Phase 2: split on commas and normalize individual tokens
    parts = [p.strip() for p in institutions_str.split(",")]
    normalized = [normalize_institution(p) for p in parts if p]
    new_str = ", ".join(normalized)
    new_line = prefix + new_str
    if new_line == line:
        return None
    return new_line


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize institution names in ALL_PAPERS.md."
    )
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE)
    parser.add_argument("--write", action="store_true",
                        help="Apply changes in-place.")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    lines = text.split("\n")
    changes = 0
    new_lines = []
    for i, line in enumerate(lines):
        result = normalize_line(line)
        if result is not None:
            changes += 1
            if not args.write:
                print(f"L{i+1}:")
                print(f"  - {line.strip()}")
                print(f"  + {result.strip()}")
            new_lines.append(result)
        else:
            new_lines.append(line)

    if changes == 0:
        print("No institution issues found.")
        return 0

    if args.write:
        args.file.write_text("\n".join(new_lines), encoding="utf-8")
        print(f"Normalized {changes} institution lines.")
    else:
        print(f"\n{changes} lines would change. Run with --write to apply.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
