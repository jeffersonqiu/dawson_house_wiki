#!/usr/bin/env bash
# Pull captured images from GCS to the local zz_images folder.
#
# Run this on your Mac before /extract so the extractor can read the images
# that the capture bot uploaded from the VM. The folder is gitignored — images
# never touch the git repo.
#
# Usage:
#   bash bot/gcp/sync-images.sh
#
# Or from anywhere in the repo:
#   bash "$(git rev-parse --show-toplevel)/bot/gcp/sync-images.sh"
#
# Requires:
#   gcloud CLI authenticated (gcloud auth login / application-default login)
#   GCS_IMAGES_BUCKET set, OR falls back to "dawson-wiki-images"

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BUCKET="${GCS_IMAGES_BUCKET:-dawson-wiki-images}"
DEST="$REPO_DIR/Dawson's wiki/zz_images"

mkdir -p "$DEST"

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] sync-images: syncing gs://${BUCKET}/zz_images -> $DEST"
gcloud storage rsync -r "gs://${BUCKET}/zz_images" "$DEST"
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] sync-images: done."
