#!/usr/bin/env bash
# Run this on your Mac (NOT on the GCP VM), after:
#   gcloud auth login
#   gcloud config set project <PROJECT_ID>
#
# Reads credentials from your local bot/.env (gitignored, never printed) and,
# for each one that's set:
#   1. Enables the Secret Manager API
#   2. Creates (or adds a new version to) a secret with that value
#   3. Grants the Compute Engine default service account read access, so the
#      VM can fetch it at runtime via google-cloud-secret-manager
#
# After this, the VM should NOT keep these values in its own bot/.env — set
# GCP_PROJECT_ID in its environment instead (done by setup-vm.sh) and both
# bots fetch them from Secret Manager automatically (see config_value in
# botconfig.py).

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

# Load credentials from bot/.env without echoing them
set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

: "${TELEGRAM_BOT_TOKEN:?TELEGRAM_BOT_TOKEN not set in bot/.env}"

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

# Credentials that may appear in bot/.env, each pushed as its own secret
# (secret ID == env var name) if non-empty. Add new *_API_KEY vars here as
# new providers/tools are supported.
CANDIDATE_VARS=(TELEGRAM_BOT_TOKEN CAPTURE_BOT_TOKEN ANTHROPIC_API_KEY OPENAI_API_KEY TAVILY_API_KEY)

echo "==> Creating/updating secrets..."
SECRETS_PUSHED=()
for var in "${CANDIDATE_VARS[@]}"; do
  value="${!var:-}"
  if [ -n "$value" ]; then
    create_or_update_secret "$var" "$value"
    SECRETS_PUSHED+=("$var")
  else
    echo "    '$var' not set in bot/.env — skipping."
  fi
done

echo "==> Granting the VM's default service account access to pushed secrets..."
PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"
VM_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
echo "    Service account: $VM_SA"

for secret_id in "${SECRETS_PUSHED[@]}"; do
  gcloud secrets add-iam-policy-binding "$secret_id" \
    --member="serviceAccount:${VM_SA}" \
    --role="roles/secretmanager.secretAccessor" \
    --condition=None >/dev/null
done

echo ""
echo "==> Done."
echo "Project:         $PROJECT_ID"
echo "VM service acct: $VM_SA (now has secretAccessor on: ${SECRETS_PUSHED[*]})"
echo ""
echo "On the VM: do NOT put these values in bot/.env."
echo "setup-vm.sh sets GCP_PROJECT_ID=$PROJECT_ID in the systemd unit, which"
echo "makes the bot fetch them from Secret Manager automatically."
