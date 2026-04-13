#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CACHE_ROOT="${XDG_CACHE_HOME:-$REPO_ROOT/.cache}"
MPL_CACHE_DIR="${MPLCONFIGDIR:-$CACHE_ROOT/matplotlib}"
FONTCONFIG_CACHE_DIR="$CACHE_ROOT/fontconfig"

# Use uv run if available, otherwise fall back to python3
if command -v uv >/dev/null 2>&1 && [ -f "$REPO_ROOT/pyproject.toml" ]; then
  RUN="uv run python3"
else
  RUN="${PYTHON_BIN:-python3}"
  if ! command -v $RUN >/dev/null 2>&1; then
    echo "Error: $RUN is not installed or not on PATH." >&2
    exit 1
  fi
fi

cd "$REPO_ROOT"
mkdir -p "$MPL_CACHE_DIR" "$FONTCONFIG_CACHE_DIR"

export XDG_CACHE_HOME="$CACHE_ROOT"
export MPLCONFIGDIR="$MPL_CACHE_DIR"

echo "Normalizing institutions and keywords..."
$RUN scripts/normalize_institutions.py --write
$RUN scripts/lint_keys.py --write

echo "Updating generated repo artifacts..."
$RUN update_template_or_data/utils/scripts/sort_by_date.py
$RUN scripts/assemble_readme.py --repo-root "$REPO_ROOT"

echo
echo "Generated artifacts are up to date. Review the diff with:"
echo "  git status --short"
echo "  git diff --stat"
