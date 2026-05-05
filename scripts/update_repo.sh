#!/usr/bin/env bash
set -euo pipefail

# Canonical pipeline: papers.yaml is the source of truth; the README
# and per-axis statistics are regenerated from it.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Use uv run if available, otherwise fall back to python3.
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

if [ ! -f "$REPO_ROOT/papers.yaml" ]; then
  echo "Error: papers.yaml not found in $REPO_ROOT" >&2
  exit 1
fi

echo "Regenerating derived artifacts from papers.yaml ..."
$RUN scripts/regen.py

echo
echo "Generated artifacts are up to date. Review the diff with:"
echo "  git status --short"
echo "  git diff --stat"
