"""Quick-capture for the Dawson House Wiki Telegram bot.

Lets the user drop raw notes/photos into "Dawson's wiki/inbox/" throughout the
day via /note <text> and photo messages, in the same format as the user's
existing manual inbox notes (one file per day, timestamped entries, Obsidian
image embeds). The Extractor picks these up later via /extract — same as any
other inbox note (system/agents/capture.md, system/constitution/write-safety.md).
"""

from __future__ import annotations

import os
import pathlib
from datetime import date, datetime
from zoneinfo import ZoneInfo

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
INBOX_DIR = REPO_ROOT / "Dawson's wiki" / "inbox"
IMAGES_DIR = REPO_ROOT / "Dawson's wiki" / "zz_images"

WIKI_TZ = ZoneInfo(os.environ.get("WIKI_TZ", "Asia/Singapore"))


def now() -> datetime:
    return datetime.now(WIKI_TZ)


def capture_file_path(for_date: date) -> pathlib.Path:
    return INBOX_DIR / f"{for_date.isoformat()} telegram capture.md"


def _ensure_capture_file(path: pathlib.Path, for_date: date) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\nsource: telegram-capture\ndate: {for_date.isoformat()}\n---\n",
        encoding="utf-8",
    )


def append_entry(text: str, image_filename: str | None = None) -> pathlib.Path:
    """Append a timestamped entry to today's capture file, creating it if needed."""
    when = now()
    path = capture_file_path(when.date())
    _ensure_capture_file(path, when.date())

    lines = [f"\n## {when.strftime('%H:%M')}"]
    if text:
        lines.append(text)
    if image_filename:
        lines.append(f"![[{image_filename}]]")

    with path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return path


def save_photo_filename() -> str:
    """A collision-safe filename for a newly captured Telegram photo."""
    base = now().strftime("%Y%m%d-%H%M%S")
    candidate = IMAGES_DIR / f"tg-{base}.jpg"
    n = 2
    while candidate.exists():
        candidate = IMAGES_DIR / f"tg-{base}-{n}.jpg"
        n += 1
    return candidate.name
