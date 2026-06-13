#!/usr/bin/env bash
# One-time setup script for a fresh Debian/Ubuntu GCP Compute Engine VM
# (e.g. e2-micro on the Always Free tier).
#
# Run this AFTER SSHing into the VM, as a normal (non-root) user with sudo:
#   chmod +x setup-vm.sh
#   ./setup-vm.sh
#
# What it does:
#   1. Installs git, python3, python3-venv, curl
#   2. Installs `uv` (fast Python package manager used by bot/run.sh)
#   3. Clones this repo (if not already present) to ~/dawson_house_wiki
#   4. Creates bot/.env from bot/.env.example (you must fill in real values
#      afterwards — this script will NOT do that for you, and the file is
#      gitignored so it stays local to the VM)
#   5. Installs and enables the systemd service so the bot starts on boot
#      and restarts on crash
#   6. Installs a cron job that runs sync-wiki.sh every 15 minutes to keep
#      the VM's repo copy up to date with origin/main
#
# Secrets (TELEGRAM_BOT_TOKEN, ANTHROPIC_API_KEY): fetched from GCP Secret
# Manager at runtime (see bot/gcp/setup-secrets.sh, run on your Mac first) —
# this script wires up GCP_PROJECT_ID in the systemd unit so that works.
#
# After running this script, you still need to:
#   - Edit ~/dawson_house_wiki/bot/.env and set TELEGRAM_ALLOWED_USER_IDS
#     (and CLAUDE_MODEL if you want a non-default model). Leave
#     TELEGRAM_BOT_TOKEN / ANTHROPIC_API_KEY blank — they come from Secret
#     Manager, assuming setup-secrets.sh has been run.
#   - Run: sudo systemctl start dawsonhouse-wikibot
#   - Test the bot on Telegram

set -euo pipefail

REPO_URL="https://github.com/jeffersonqiu/dawson_house_wiki.git"
REPO_DIR="$HOME/dawson_house_wiki"
SERVICE_NAME="dawsonhouse-wikibot"

echo "==> Installing system packages..."
sudo apt-get update -y
sudo apt-get install -y git python3 python3-venv python3-pip curl

echo "==> Installing uv (Python package manager)..."
if ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
  # uv installs to ~/.local/bin — make sure this shell + future ones can find it
  export PATH="$HOME/.local/bin:$PATH"
  if ! grep -q '.local/bin' "$HOME/.bashrc" 2>/dev/null; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
  fi
fi

echo "==> Cloning repo..."
if [ ! -d "$REPO_DIR" ]; then
  git clone "$REPO_URL" "$REPO_DIR"
else
  echo "    $REPO_DIR already exists, skipping clone."
fi

cd "$REPO_DIR"

echo "==> Setting up bot/.env..."
if [ ! -f bot/.env ]; then
  cp bot/.env.example bot/.env
  echo "    Created bot/.env from template. Set TELEGRAM_ALLOWED_USER_IDS"
  echo "    (TELEGRAM_BOT_TOKEN / ANTHROPIC_API_KEY come from Secret Manager — leave blank):"
  echo "    nano $REPO_DIR/bot/.env"
else
  echo "    bot/.env already exists, leaving it alone."
fi

echo "==> Detecting GCP project ID from VM metadata..."
PROJECT_ID="$(curl -s -H 'Metadata-Flavor: Google' \
  'http://metadata.google.internal/computeMetadata/v1/project/project-id')"
echo "    Project: ${PROJECT_ID}"

echo "==> Installing systemd service..."
SERVICE_SRC="bot/gcp/dawsonhouse-wikibot.service.example"
SERVICE_DST="/etc/systemd/system/${SERVICE_NAME}.service"
sed -e "s#REPLACE_WITH_ABSOLUTE_PATH_TO_PROJECT#${REPO_DIR}#g" \
    -e "s#REPLACE_WITH_GCP_PROJECT_ID#${PROJECT_ID}#g" \
    "$SERVICE_SRC" | sudo tee "$SERVICE_DST" > /dev/null
sudo systemctl daemon-reload
sudo systemctl enable "$SERVICE_NAME"
echo "    Service installed and enabled (will start on boot)."
echo "    NOT starting it yet — fill in bot/.env first, then run:"
echo "      sudo systemctl start ${SERVICE_NAME}"

echo "==> Installing cron job for repo sync (every 15 minutes)..."
chmod +x bot/gcp/sync-wiki.sh
CRON_LINE="*/15 * * * * ${REPO_DIR}/bot/gcp/sync-wiki.sh >> ${REPO_DIR}/bot/logs/sync.log 2>&1"
mkdir -p bot/logs
EXISTING_CRON="$(crontab -l 2>/dev/null | grep -vF "sync-wiki.sh" || true)"
printf '%s\n%s\n' "$EXISTING_CRON" "$CRON_LINE" | grep -v '^$' | crontab -
echo "    Cron job installed."

# sync-wiki.sh calls `sudo systemctl restart`, so allow this user to run that
# one command without a password prompt (limits sudo scope to just this).
SUDOERS_LINE="$(whoami) ALL=(ALL) NOPASSWD: /bin/systemctl restart ${SERVICE_NAME}"
SUDOERS_FILE="/etc/sudoers.d/${SERVICE_NAME}-restart"
if [ ! -f "$SUDOERS_FILE" ]; then
  echo "$SUDOERS_LINE" | sudo tee "$SUDOERS_FILE" > /dev/null
  sudo chmod 440 "$SUDOERS_FILE"
  echo "    Granted passwordless 'systemctl restart ${SERVICE_NAME}' for cron sync."
fi

echo ""
echo "==> Setup complete."
echo ""
echo "Next steps:"
echo "  1. Edit bot/.env with real credentials:"
echo "       nano $REPO_DIR/bot/.env"
echo "  2. Start the bot:"
echo "       sudo systemctl start ${SERVICE_NAME}"
echo "  3. Check it's running:"
echo "       sudo systemctl status ${SERVICE_NAME}"
echo "       journalctl -u ${SERVICE_NAME} -f"
echo "  4. Message your bot on Telegram to confirm it responds."
