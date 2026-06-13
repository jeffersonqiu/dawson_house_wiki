#!/usr/bin/env bash
# Launches the Dawson House Wiki Telegram bot using the project's uv-managed
# Python environment. Intended to be run directly for testing, or invoked by
# the launchd job (com.dawsonhouse.wikibot.plist) for always-on operation.

set -euo pipefail

BOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$BOT_DIR"

if [ ! -d ".venv" ]; then
    echo "Creating virtualenv in bot/.venv ..."
    uv venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

uv pip install -q -r requirements.txt

exec python3 telegram_bot.py
