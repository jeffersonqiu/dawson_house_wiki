#!/usr/bin/env bash
# Keeps the VM's clone of this repo in sync with origin/main, then restarts
# both bot services (Conversation + Capture) if (and only if) anything
# actually changed.
#
# Intended to run on a schedule via cron, e.g. every 15 minutes:
#   */15 * * * * /home/YOUR_USER/dawson_house_wiki/bot/gcp/sync-wiki.sh >> /home/YOUR_USER/dawson_house_wiki/bot/logs/sync.log 2>&1
#
# Why this is needed:
#   - The Compiler agent runs on your local Mac and pushes wiki updates to
#     GitHub (origin/main).
#   - The VM has its own independent clone of the repo (it does NOT share a
#     filesystem with your Mac), so that clone only updates when *it* runs
#     `git pull`.
#   - The bot reads wiki content from disk at startup (see bot/wiki_context.py),
#     so after a pull the service must be restarted to pick up new content.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SERVICE_NAMES=("dawsonhouse-wikibot" "dawsonhouse-capturebot")

cd "$REPO_DIR"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Checking for updates in $REPO_DIR"

BEFORE="$(git rev-parse HEAD)"

# Fetch + fast-forward only. If the VM has any local changes (it shouldn't —
# the bot is read-only), this will fail loudly rather than silently discard them.
git fetch origin main
git merge --ff-only origin/main

AFTER="$(git rev-parse HEAD)"

if [ "$BEFORE" != "$AFTER" ]; then
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Updated $BEFORE -> $AFTER, restarting ${SERVICE_NAMES[*]}"
  sudo systemctl restart "${SERVICE_NAMES[@]}"
else
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] No changes."
fi
