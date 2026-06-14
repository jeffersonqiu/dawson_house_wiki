#!/usr/bin/env bash
# Launches one of the Dawson House Wiki Telegram bots using the project's
# uv-managed Python environment. Intended to be run directly for testing, or
# invoked by a systemd unit (see bot/gcp/) for always-on operation.
#
# Usage:
#   run.sh                 # telegram_bot.py — Conversation agent + /research (default)
#   run.sh telegram_bot.py
#   run.sh capture_bot.py  # Capture agent — /note, photos, daily review

set -euo pipefail

BOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$BOT_DIR"

SCRIPT="${1:-telegram_bot.py}"

# uv installs to ~/.local/bin, which isn't on PATH for systemd services
# (they don't source .bashrc). Harmless no-op if it's already on PATH.
export PATH="$HOME/.local/bin:$PATH"

if [ ! -d ".venv" ]; then
    echo "Creating virtualenv in bot/.venv ..."
    uv venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

uv pip install -q -r requirements.txt

exec python3 "$SCRIPT"
