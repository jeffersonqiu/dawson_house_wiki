#!/usr/bin/env bash
# Commits and pushes any new capture files (inbox + zz_images) from the VM
# back to origin/main so the local Mac can pull them and run /extract.
#
# Intended to run on a schedule via cron, e.g. every 30 minutes:
#   */30 * * * * /home/YOUR_USER/dawson_house_wiki/bot/gcp/push-wiki.sh >> /home/YOUR_USER/dawson_house_wiki/bot/logs/push.log 2>&1
#
# Requires GCP_PROJECT_ID to be set (done by setup-vm.sh via the systemd unit
# environment, or export it manually for testing). Fetches GITHUB_TOKEN from
# Secret Manager at runtime — never stored on disk.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] push-wiki: checking for new capture files in $REPO_DIR"

cd "$REPO_DIR"

# Only stage files the capture bot writes — never touch wiki/, system/, or bot/
CAPTURE_PATHS=("Dawson's wiki/inbox/" "Dawson's wiki/zz_images/")

# Check if there's anything new to commit in those paths
DIRTY=false
for path in "${CAPTURE_PATHS[@]}"; do
  if [ -n "$(git status --porcelain -- "$path")" ]; then
    DIRTY=true
    break
  fi
done

if [ "$DIRTY" = false ]; then
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] push-wiki: nothing new to push."
  exit 0
fi

# Fetch GITHUB_TOKEN from Secret Manager
PROJECT_ID="${GCP_PROJECT_ID:-}"
if [ -z "$PROJECT_ID" ]; then
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] push-wiki: GCP_PROJECT_ID not set — cannot fetch GITHUB_TOKEN." >&2
  exit 1
fi

GITHUB_TOKEN="$(gcloud secrets versions access latest --secret=GITHUB_TOKEN --project="$PROJECT_ID" 2>/dev/null)"

if [ -z "$GITHUB_TOKEN" ]; then
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] push-wiki: GITHUB_TOKEN empty — aborting." >&2
  exit 1
fi

# Configure git to use the token for this push (not stored in config)
REPO_URL="$(git remote get-url origin)"
# Strip any existing credentials from URL, then inject token
AUTHED_URL="$(echo "$REPO_URL" | sed 's|https://\(.*\)|https://x-access-token:'"$GITHUB_TOKEN"'@\1|')"

git config user.email "dawsonhouse-wikibot@vm.local"
git config user.name "Dawson Wiki Bot"

# Stage only capture paths
for path in "${CAPTURE_PATHS[@]}"; do
  git add -- "$path" 2>/dev/null || true
done

# Commit
DATESTAMP="$(date -u +%Y-%m-%d)"
git commit -m "chore: capture files from VM [$DATESTAMP]

Auto-committed by push-wiki.sh on the GCE VM.
New inbox notes and photos from the Capture bot."

# Pull latest first (fast-forward only) to avoid conflicts, then push
git fetch origin main
git merge --ff-only origin/main

git push "$AUTHED_URL" HEAD:main

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] push-wiki: pushed capture files to origin/main."
