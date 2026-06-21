"""Google Cloud Storage helpers for captured images.

Uploads captured photos to a GCS bucket so the git repo stays image-free.
If GCS_IMAGES_BUCKET is unset the module is a no-op, so local dev (without GCS)
still works exactly as before.

Usage (in capture_bot.py photo_handler):
    gcs_images.resize_if_needed(local_path)
    gcs_images.upload_image(local_path, filename)
"""

from __future__ import annotations

import logging
import os
import pathlib

logger = logging.getLogger(__name__)

BUCKET = os.environ.get("GCS_IMAGES_BUCKET", "")
_GCS_PREFIX = "zz_images"
_MAX_LONG_EDGE = 2048  # pixels — safety cap; Telegram photos are already ~200KB


def resize_if_needed(local_path: pathlib.Path) -> None:
    """Downscale image to ≤MAX_LONG_EDGE px (JPEG q85) in-place if oversized.

    Silently skips non-JPEG/PNG files or if Pillow is unavailable.
    Telegram-captured photos are typically 55–200KB and well within the cap;
    this guards against manually-dropped large originals.
    """
    try:
        from PIL import Image  # type: ignore
    except ImportError:
        logger.debug("Pillow not installed — skipping resize check")
        return

    try:
        with Image.open(local_path) as img:
            w, h = img.size
            long_edge = max(w, h)
            if long_edge <= _MAX_LONG_EDGE:
                return  # already small enough

            scale = _MAX_LONG_EDGE / long_edge
            new_size = (int(w * scale), int(h * scale))
            logger.info(
                "resize_if_needed: %s %dx%d -> %dx%d",
                local_path.name, w, h, new_size[0], new_size[1],
            )
            resized = img.resize(new_size, Image.LANCZOS)
            # Convert to RGB first (handles PNG/RGBA transparency)
            if resized.mode not in ("RGB", "L"):
                resized = resized.convert("RGB")
            resized.save(local_path, "JPEG", quality=85, optimize=True)
    except Exception:
        logger.exception("resize_if_needed: failed on %s (continuing)", local_path.name)


def upload_image(local_path: pathlib.Path, dest_name: str) -> str | None:
    """Upload local_path to gs://{BUCKET}/{GCS_PREFIX}/{dest_name}.

    Returns the gs:// URI on success, None if GCS_IMAGES_BUCKET is unset or
    the upload fails (so capture still works without GCS configured).
    """
    if not BUCKET:
        logger.debug("GCS_IMAGES_BUCKET not set — skipping upload of %s", dest_name)
        return None

    try:
        from google.cloud import storage  # type: ignore

        client = storage.Client()
        bucket = client.bucket(BUCKET)
        blob = bucket.blob(f"{_GCS_PREFIX}/{dest_name}")
        blob.upload_from_filename(str(local_path))
        uri = f"gs://{BUCKET}/{_GCS_PREFIX}/{dest_name}"
        logger.info("upload_image: %s -> %s", dest_name, uri)
        return uri
    except Exception:
        logger.exception("upload_image: failed to upload %s (continuing)", dest_name)
        return None
