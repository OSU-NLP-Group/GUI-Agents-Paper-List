#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
CACHE_ROOT="${XDG_CACHE_HOME:-$REPO_ROOT/.cache}"
MPL_CACHE_DIR="${MPLCONFIGDIR:-$CACHE_ROOT/matplotlib}"
FONTCONFIG_CACHE_DIR="$CACHE_ROOT/fontconfig"

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "Error: $PYTHON_BIN is not installed or not on PATH." >&2
  exit 1
fi

if ! "$PYTHON_BIN" - <<'PY' >/dev/null 2>&1
import pandas  # noqa: F401
import matplotlib  # noqa: F401
import wordcloud  # noqa: F401
PY
then
  echo "Error: missing Python dependencies for repo generation." >&2
  echo "Install them with:" >&2
  echo "  $PYTHON_BIN -m pip install -r \"$REPO_ROOT/requirements.txt\"" >&2
  exit 1
fi

cd "$REPO_ROOT"
mkdir -p "$MPL_CACHE_DIR" "$FONTCONFIG_CACHE_DIR"

export XDG_CACHE_HOME="$CACHE_ROOT"
export MPLCONFIGDIR="$MPL_CACHE_DIR"

echo "Updating generated repo artifacts..."
"$PYTHON_BIN" update_template_or_data/utils/scripts/sort_by_date.py
"$PYTHON_BIN" scripts/assemble_readme.py --repo-root "$REPO_ROOT"

echo
echo "Generated artifacts are up to date. Review the diff with:"
echo "  git status --short"
echo "  git diff --stat"
