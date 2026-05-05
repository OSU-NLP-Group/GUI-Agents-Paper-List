#!/usr/bin/env bash
# Build the site locally and push the static output to the gh-pages branch.
# Usage:
#   ./scripts/deploy.sh                      # builds and pushes
#   ./scripts/deploy.sh --build-only         # builds, doesn't push
#   ./scripts/deploy.sh --remote upstream    # push to a non-default remote
#
# Run from anywhere inside the repo. The script chdirs to site/ for the build,
# then to a temp git worktree for the publish.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
SITE_DIR="$REPO_ROOT/site"

if [[ ! -d "$SITE_DIR" ]]; then
  echo "error: $SITE_DIR not found." >&2
  exit 1
fi

REMOTE="origin"
BUILD_ONLY=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --build-only) BUILD_ONLY=1; shift ;;
    --remote)     REMOTE="$2"; shift 2 ;;
    -h|--help)
      sed -n '1,20p' "$0"; exit 0 ;;
    *)
      echo "error: unknown arg: $1" >&2; exit 1 ;;
  esac
done

REPO_OWNER="$(git -C "$REPO_ROOT" remote get-url "$REMOTE" 2>/dev/null \
  | sed -E 's#.*github\.com[:/]([^/]+)/.*#\1#')"
REPO_NAME="$(git -C "$REPO_ROOT" remote get-url "$REMOTE" 2>/dev/null \
  | sed -E 's#.*github\.com[:/][^/]+/([^/.]+).*#\1#')"

if [[ -z "${REPO_OWNER:-}" || -z "${REPO_NAME:-}" ]]; then
  echo "warn: could not derive owner/name from remote '$REMOTE'." >&2
  echo "      will build with default BASE_PATH=/GUI-Agents-Paper-List." >&2
  REPO_NAME="GUI-Agents-Paper-List"
fi

echo "==> Repo: ${REPO_OWNER:-<unknown>}/${REPO_NAME}"
echo "==> Building site (BASE_PATH=/${REPO_NAME})"

cd "$SITE_DIR"

if [[ ! -d node_modules ]]; then
  echo "==> Installing dependencies"
  npm install --no-audit --no-fund
fi

# Pre-fetch star count if gh is available, otherwise let the build fetch from
# the public API (or skip silently if offline).
STAR_COUNT_VAL=""
if command -v gh >/dev/null 2>&1 && [[ -n "${REPO_OWNER:-}" ]]; then
  STAR_COUNT_VAL="$(gh api "repos/${REPO_OWNER}/${REPO_NAME}" --jq '.stargazers_count' 2>/dev/null || true)"
  if [[ -n "$STAR_COUNT_VAL" ]]; then
    echo "==> Star count: $STAR_COUNT_VAL"
  fi
fi

BASE_PATH="/${REPO_NAME}" \
SITE_URL="https://${REPO_OWNER:-OSU-NLP-Group}.github.io" \
STAR_COUNT="$STAR_COUNT_VAL" \
  npm run build

if [[ "$BUILD_ONLY" == "1" ]]; then
  echo "==> Build complete. Output: $SITE_DIR/dist"
  exit 0
fi

DIST_DIR="$SITE_DIR/dist"
if [[ ! -d "$DIST_DIR" ]]; then
  echo "error: build output missing at $DIST_DIR" >&2
  exit 1
fi

# Publish via a temporary worktree on the gh-pages branch.
WORKTREE_DIR="$(mktemp -d)"
trap 'cd "$REPO_ROOT"; git worktree remove --force "$WORKTREE_DIR" >/dev/null 2>&1 || true; rm -rf "$WORKTREE_DIR"' EXIT

cd "$REPO_ROOT"

# Make sure gh-pages branch exists locally; create it as an orphan if not.
if git show-ref --verify --quiet refs/heads/gh-pages; then
  git worktree add "$WORKTREE_DIR" gh-pages
elif git ls-remote --exit-code --heads "$REMOTE" gh-pages >/dev/null 2>&1; then
  git fetch "$REMOTE" gh-pages:gh-pages
  git worktree add "$WORKTREE_DIR" gh-pages
else
  echo "==> Creating orphan gh-pages branch"
  git worktree add --detach "$WORKTREE_DIR"
  cd "$WORKTREE_DIR"
  git checkout --orphan gh-pages
  git rm -rf . >/dev/null 2>&1 || true
  cd "$REPO_ROOT"
fi

cd "$WORKTREE_DIR"

# Wipe everything except .git*
find . -mindepth 1 -maxdepth 1 ! -name '.git' ! -name '.gitignore' -exec rm -rf {} +

cp -R "$DIST_DIR/." .
# Disable Jekyll on Pages so files starting with _ are served.
touch .nojekyll
# CNAME passthrough: if a file exists in site/public/CNAME, dist already has it.

git add -A
if git diff --cached --quiet; then
  echo "==> No changes to publish."
  exit 0
fi

git -c user.name="${GIT_AUTHOR_NAME:-$(git config user.name)}" \
    -c user.email="${GIT_AUTHOR_EMAIL:-$(git config user.email)}" \
    commit -m "site: $(date -u +%Y-%m-%dT%H:%M:%SZ)"

echo "==> Pushing gh-pages to $REMOTE"
git push "$REMOTE" gh-pages

echo "==> Done. Live at: https://${REPO_OWNER:-<owner>}.github.io/${REPO_NAME}/"
