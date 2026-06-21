"""Quick-capture for the Dawson House Wiki Telegram bot.

Lets the user drop raw notes/photos into "Dawson's wiki/inbox/" throughout the
day via /note <text> and photo messages, in the same format as the user's
existing manual inbox notes (one file per day, timestamped entries, Obsidian
image embeds). The Extractor picks these up later via /extract — same as any
other inbox note (system/agents/capture.md, system/constitution/write-safety.md).
"""

from __future__ import annotations

import json
import os
import pathlib
import re
from datetime import date, datetime, timedelta, timezone
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


_HEADING_RE = re.compile(r"^## (\d{2}:\d{2})\b", re.MULTILINE)


def append_context(reply_to_date: datetime, context_text: str) -> pathlib.Path | None:
    """Append > context_text under the ## HH:MM block matching reply_to_date.

    Looks in that day's capture file for a heading whose time is within 5 minutes
    of reply_to_date (converted to WIKI_TZ). Returns the path on success, None
    if no suitable block is found.
    """
    local_dt = reply_to_date.astimezone(WIKI_TZ)
    path = capture_file_path(local_dt.date())
    if not path.exists():
        return None

    content = path.read_text(encoding="utf-8")
    matches = [(m.start(), m.group(1)) for m in _HEADING_RE.finditer(content)
               if not content[m.start():].startswith("## Clarifications")]

    if not matches:
        return None

    def _minutes(t: str) -> int:
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    target_min = _minutes(local_dt.strftime("%H:%M"))
    best_pos, best_time = min(matches, key=lambda x: abs(_minutes(x[1]) - target_min))

    if abs(_minutes(best_time) - target_min) > 5:
        return None

    next_positions = [pos for pos, _ in matches if pos > best_pos]
    context_line = f"> {context_text}"

    if next_positions:
        insert_at = next_positions[0]
        new_content = (
            content[:insert_at].rstrip("\n") + f"\n{context_line}\n\n" + content[insert_at:]
        )
    else:
        # Append before any ## Clarifications block if present
        clarif_match = re.search(r"^## Clarifications", content, re.MULTILINE)
        if clarif_match:
            insert_at = clarif_match.start()
            new_content = (
                content[:insert_at].rstrip("\n") + f"\n{context_line}\n\n" + content[insert_at:]
            )
        else:
            new_content = content.rstrip("\n") + f"\n{context_line}\n"

    path.write_text(new_content, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Message-ID → capture heading map
# Persisted to system/state/capture-msgmap.json (gitignored, survives restarts).
# Maps str(message_id) → {"date": "YYYY-MM-DD", "heading": "HH:MM"}
# Pruned to entries ≤ MSG_MAP_MAX_AGE_DAYS old on every write.
# ---------------------------------------------------------------------------

_STATE_DIR = REPO_ROOT / "system" / "state"
_MSG_MAP_PATH = _STATE_DIR / "capture-msgmap.json"
MSG_MAP_MAX_AGE_DAYS = 7


def _load_msgmap() -> dict[str, dict]:
    if not _MSG_MAP_PATH.exists():
        return {}
    try:
        return json.loads(_MSG_MAP_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_msgmap(data: dict[str, dict]) -> None:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=MSG_MAP_MAX_AGE_DAYS)).date()
    pruned = {
        k: v for k, v in data.items()
        if datetime.fromisoformat(v["date"]).date() >= cutoff
    }
    _STATE_DIR.mkdir(parents=True, exist_ok=True)
    _MSG_MAP_PATH.write_text(json.dumps(pruned, indent=2), encoding="utf-8")


def record_message(message_id: int, for_date: date, heading: str) -> None:
    """Record message_id → (date, heading) so reply-context can find the block."""
    data = _load_msgmap()
    data[str(message_id)] = {"date": for_date.isoformat(), "heading": heading}
    _save_msgmap(data)


def lookup_message(message_id: int) -> tuple[date, str] | None:
    """Return (date, heading) for a recorded message_id, or None if not found."""
    data = _load_msgmap()
    entry = data.get(str(message_id))
    if not entry:
        return None
    return datetime.fromisoformat(entry["date"]).date(), entry["heading"]


def append_context_by_heading(
    for_date: date, heading: str, context_text: str
) -> pathlib.Path | None:
    """Append > context_text under the exact ## HH:MM block in for_date's capture file."""
    path = capture_file_path(for_date)
    if not path.exists():
        return None

    content = path.read_text(encoding="utf-8")
    target = f"## {heading}"

    matches = [(m.start(), m.group(1)) for m in _HEADING_RE.finditer(content)
               if not content[m.start():].startswith("## Clarifications")]

    # Find the block whose heading exactly matches
    block_pos = next((pos for pos, t in matches if t == heading), None)
    if block_pos is None:
        return None

    context_line = f"> {context_text}"
    next_positions = [pos for pos, _ in matches if pos > block_pos]

    if next_positions:
        insert_at = next_positions[0]
        new_content = (
            content[:insert_at].rstrip("\n") + f"\n{context_line}\n\n" + content[insert_at:]
        )
    else:
        clarif_match = re.search(r"^## Clarifications", content, re.MULTILINE)
        if clarif_match:
            insert_at = clarif_match.start()
            new_content = (
                content[:insert_at].rstrip("\n") + f"\n{context_line}\n\n" + content[insert_at:]
            )
        else:
            new_content = content.rstrip("\n") + f"\n{context_line}\n"

    path.write_text(new_content, encoding="utf-8")
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
