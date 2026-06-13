#!/usr/bin/env bash
# Run this on your Mac (NOT on the GCP VM), after:
#   gcloud auth login
#   gcloud config set project <PROJECT_ID>
#
# Reads TELEGRAM_BOT_TOKEN and ANTHROPIC_API_KEY from your local bot/.env
# (gitignored, never printed) and:
#   1. Enables the Secret Manager API
#   2. Creates (or adds a new version to) two secrets with those values
#   3. Grants the Compute Engine default service account read access, so the
#      VM can fetch them at runtime via google-cloud-secret-manager
#
# After this, the VM should NOT keep TELEGRAM_BOT_TOKEN / ANTHROPIC_API_KEY in
# its own bot/.env — set GCP_PROJECT_ID in its environment instead (done by
# setup-vm.sh) and the bot fetches both from Secret Manager automatically.

set -euo pipefail

BOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$BOT_DIR/.env"

if [ ! -f "$ENV_FILE" ]; then
  echo "bot/.env not found at $ENV_FILE — create it first (see bot/.env.example)."
  exit 1
fi

PROJECT_ID="$(gcloud config get-value project 2>/dev/null || true)"
if [ -z "$PROJECT_ID" ] || [ "$PROJECT_ID" = "(unset)" ]; then
  echo "No GCP project configured. Run: gcloud config set project <PROJECT_ID>"
  exit 1
fi
echo "Using project: $PROJECT_ID"

echo "==> Enabling Secret Manager API..."
gcloud services enable secretmanager.googleapis.com

# Load TELEGRAM_BOT_TOKEN / ANTHROPIC_API_KEY from bot/.env without echoing them
set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

: "${TELEGRAM_BOT_TOKEN:?TELEGRAM_BOT_TOKEN not set in bot/.env}"
: "${ANTHROPIC_API_KEY:?ANTHROPIC_API_KEY not set in bot/.env}"

create_or_update_secret() {
  local secret_id="$1"
  local secret_value="$2"

  if gcloud secrets describe "$secret_id" >/dev/null 2>&1; then
    echo "    '$secret_id' already exists — adding a new version."
    printf '%s' "$secret_value" | gcloud secrets versions add "$secret_id" --data-file=-
  else
    echo "    Creating secret '$secret_id'..."
    printf '%s' "$secret_value" | gcloud secrets create "$secret_id" --data-file=- --replication-policy=automatic
  fi
}

echo "==> Creating/updating secrets..."
create_or_update_secret "TELEGRAM_BOT_TOKEN" "$TELEGRAM_BOT_TOKEN"
create_or_update_secret "ANTHROPIC_API_KEY" "$ANTHROPIC_API_KEY"

echo "==> Granting the VM's default service account access to both secrets..."
PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"
VM_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
echo "    Service account: $VM_SA"

for secret_id in TELEGRAM_BOT_TOKEN ANTHROPIC_API_KEY; do
  gcloud secrets add-iam-policy-binding "$secret_id" \
    --member="serviceAccount:${VM_SA}" \
    --role="roles/secretmanager.secretAccessor" \
    --condition=None >/dev/null
done

echo ""
echo "==> Done."
echo "Project:         $PROJECT_ID"
echo "VM service acct: $VM_SA (now has secretAccessor on both secrets)"
echo ""
echo "On the VM: do NOT put TELEGRAM_BOT_TOKEN or ANTHROPIC_API_KEY in bot/.env."
echo "setup-vm.sh sets GCP_PROJECT_ID=$PROJECT_ID in the systemd unit, which"
echo "makes the bot fetch both secrets from Secret Manager automatically."
