"""End-of-day clarification review for the Dawson House Wiki Telegram bot.

Once a day (DAILY_REVIEW_HOUR, default 21:00 WIKI_TZ / Asia/Singapore), checks
today's quick-capture file (see capture.py) and — if it exists and hasn't been
reviewed yet — asks the model to find up to DAILY_REVIEW_MAX_QUESTIONS points
that are ambiguous or missing context (which room/vendor a price or photo
belongs to, whether a price is a quote or final, etc.).

Each question is sent as a Telegram message with inline-keyboard buttons
(tabular multiple-choice, like Claude's app-side Q&A), plus an "Other" button
that switches to a free-text reply. Answers are appended to the capture file
under a "## Clarifications" section, and the file is marked `reviewed: true`
in its frontmatter so it's not processed again. The Extractor later picks up
the whole file (original entries + clarifications) via /extract.

Assumption: this is a personal bot used in 1:1 private chats only, where
Telegram's chat_id == the user's numeric user_id — so the scheduled job can
message each TELEGRAM_ALLOWED_USER_IDS entry directly by chat_id without an
incoming update to read it from.
"""

from __future__ import annotations

import base64
import json
import logging
import pathlib
import re

import litellm
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

import capture

logger = logging.getLogger("dawson-wiki-bot.daily_review")

WIKI_DIR = capture.REPO_ROOT / "Dawson's wiki" / "wiki"
ROOMS_DIR = WIKI_DIR / "Rooms"
VENDORS_DIR = WIKI_DIR / "Vendors"

CALLBACK_PREFIX = "dr"

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_IMAGE_EMBED_RE = re.compile(r"!\[\[([^\]]+)\]\]")
_FENCE_RE = re.compile(r"^```\w*\n?|```$", re.MULTILINE)

# chat_id -> {"path": Path, "questions": [...], "index": int,
#             "answers": [...], "awaiting_free_text": bool}
pending_reviews: dict[int, dict] = {}


def _existing_rooms() -> list[str]:
    if not ROOMS_DIR.exists():
        return []
    return sorted(p.name for p in ROOMS_DIR.iterdir() if p.is_dir())


def _existing_vendors() -> list[str]:
    if not VENDORS_DIR.exists():
        return []
    return sorted(p.stem for p in VENDORS_DIR.glob("*.md"))


def _is_reviewed(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return False
    return any(
        line.strip() == "reviewed: true" for line in match.group(1).splitlines()
    )


def _mark_reviewed(path: pathlib.Path) -> None:
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return
    body = match.group(1)
    if any(line.strip().startswith("reviewed:") for line in body.splitlines()):
        return
    new_frontmatter = f"---\n{body}\nreviewed: true\n---\n"
    path.write_text(new_frontmatter + text[match.end() :], encoding="utf-8")


def append_clarifications(path: pathlib.Path, qa_pairs: list[dict]) -> None:
    when = capture.now()
    lines = [f"\n## Clarifications ({when.strftime('%Y-%m-%d %H:%M')})"]
    for qa in qa_pairs:
        lines.append(f"- Q: {qa['question']}")
        lines.append(f"  A: {qa['answer']}")
    with path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def _extract_image_filenames(text: str) -> list[str]:
    return _IMAGE_EMBED_RE.findall(text)


def _build_system_prompt(max_questions: int) -> str:
    rooms = "\n".join(f"- {r}" for r in _existing_rooms()) or "(none yet)"
    vendors = "\n".join(f"- {v}" for v in _existing_vendors()) or "(none yet)"
    return f"""You are the end-of-day review step for the "Dawson House Wiki"
renovation knowledge base. The user has quickly jotted down notes and/or
attached photos during the day via a Telegram bot. Your job is to spot up to
{max_questions} points where important context is AMBIGUOUS OR MISSING — the
kind of thing that would make it hard to file this note into the wiki later
(which room or vendor something relates to, whether a price is a quote vs.
final, what an item in a photo actually is, etc.).

For each point, write ONE short clarifying question and 2-4 short
multiple-choice answer options (a few words each). Ground room/vendor options
in the lists below when relevant — don't invent new room or vendor names as
options unless the note itself suggests one.

If the notes are already clear and self-contained, return an empty list — do
NOT invent questions just to fill the quota.

Respond with ONLY a JSON object, no markdown, no commentary, no code fences:
{{"questions": [{{"question": "...", "options": ["...", "..."]}}]}}

## Existing rooms
{rooms}

## Existing vendors
{vendors}
"""


def _build_messages(capture_text: str, image_filenames: list[str]) -> list[dict]:
    content: list[dict] = [
        {"type": "text", "text": f"Today's quick-capture notes:\n\n{capture_text}"}
    ]
    for filename in image_filenames:
        image_path = capture.IMAGES_DIR / filename
        if not image_path.exists():
            continue
        try:
            b64 = base64.b64encode(image_path.read_bytes()).decode("ascii")
        except OSError:
            continue
        ext = image_path.suffix.lstrip(".").lower() or "jpeg"
        content.append(
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/{ext};base64,{b64}"},
            }
        )
    return [{"role": "user", "content": content}]


def _parse_questions(raw: str, max_questions: int) -> list[dict]:
    cleaned = _FENCE_RE.sub("", raw).strip()
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        logger.warning("Could not parse daily review questions JSON: %r", raw[:200])
        return []

    result = []
    for q in data.get("questions", [])[:max_questions]:
        question = str(q.get("question") or "").strip()
        options = [str(o).strip() for o in q.get("options", []) if str(o).strip()]
        if question and options:
            result.append({"question": question, "options": options[:4]})
    return result


def generate_questions(
    capture_text: str, image_filenames: list[str], model: str, max_questions: int
) -> list[dict]:
    system = _build_system_prompt(max_questions)
    messages = _build_messages(capture_text, image_filenames)
    response = litellm.completion(
        model=model,
        max_tokens=1500,
        temperature=0.2,
        messages=[{"role": "system", "content": system}, *messages],
    )
    raw = (response.choices[0].message.content or "").strip()
    return _parse_questions(raw, max_questions)


def _question_keyboard(idx: int, options: list[str]) -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(opt, callback_data=f"{CALLBACK_PREFIX}|{idx}|{i}")]
        for i, opt in enumerate(options)
    ]
    rows.append(
        [InlineKeyboardButton("Other (type below)", callback_data=f"{CALLBACK_PREFIX}|{idx}|other")]
    )
    rows.append([InlineKeyboardButton("Skip", callback_data=f"{CALLBACK_PREFIX}|{idx}|skip")])
    return InlineKeyboardMarkup(rows)


async def _send_question(context: ContextTypes.DEFAULT_TYPE, chat_id: int) -> None:
    session = pending_reviews[chat_id]
    idx = session["index"]
    q = session["questions"][idx]
    await context.bot.send_message(
        chat_id=chat_id,
        text=q["question"],
        reply_markup=_question_keyboard(idx, q["options"]),
    )


async def _continue_or_finish(context: ContextTypes.DEFAULT_TYPE, chat_id: int) -> None:
    session = pending_reviews[chat_id]
    if session["index"] >= len(session["questions"]):
        if session["answers"]:
            append_clarifications(session["path"], session["answers"])
        _mark_reviewed(session["path"])
        del pending_reviews[chat_id]
        await context.bot.send_message(
            chat_id=chat_id, text="Thanks — added your answers to today's notes."
        )
    else:
        await _send_question(context, chat_id)


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if not query or not query.data:
        return
    await query.answer()

    chat_id = query.message.chat_id
    session = pending_reviews.get(chat_id)
    if not session:
        return

    _, idx_str, choice = query.data.split("|")
    idx = int(idx_str)
    if idx != session["index"]:
        return  # stale buttons from an earlier question

    q = session["questions"][idx]

    if choice == "skip":
        await query.edit_message_text(f"{q['question']}\n\n(skipped)")
        session["index"] += 1
    elif choice == "other":
        session["awaiting_free_text"] = True
        await query.edit_message_reply_markup(reply_markup=None)
        await context.bot.send_message(chat_id=chat_id, text="Okay, type your answer:")
        return
    else:
        answer = q["options"][int(choice)]
        session["answers"].append({"question": q["question"], "answer": answer})
        await query.edit_message_text(f"{q['question']}\n\nYou answered: {answer}")
        session["index"] += 1

    await _continue_or_finish(context, chat_id)


async def handle_free_text_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """If `chat_id` has a pending "Other" answer, consume this message as that
    answer and return True. Otherwise return False (caller should handle the
    message normally)."""
    chat_id = update.effective_chat.id
    session = pending_reviews.get(chat_id)
    if not session or not session.get("awaiting_free_text"):
        return False

    idx = session["index"]
    q = session["questions"][idx]
    answer = (update.message.text or "").strip()
    session["answers"].append({"question": q["question"], "answer": answer})
    session["awaiting_free_text"] = False
    session["index"] += 1

    await update.message.reply_text(f"Got it: {answer}")
    await _continue_or_finish(context, chat_id)
    return True


async def daily_review_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    data = context.job.data or {}

    if data.get("missing_llm_key"):
        logger.info(
            "Daily review skipped — %s is not configured", data["missing_llm_key"]
        )
        return

    today = capture.now().date()
    path = capture.capture_file_path(today)
    if not path.exists() or _is_reviewed(path):
        return

    text = path.read_text(encoding="utf-8")
    image_filenames = _extract_image_filenames(text)
    max_questions = data.get("max_questions", 3)

    try:
        questions = generate_questions(text, image_filenames, data["llm_model"], max_questions)
    except Exception:
        logger.exception("Daily review: question generation failed")
        return

    if not questions:
        _mark_reviewed(path)
        return

    for user_id in data.get("allowed_user_ids", set()):
        if user_id in pending_reviews:
            continue  # a review is already in progress for this chat
        pending_reviews[user_id] = {
            "path": path,
            "questions": questions,
            "index": 0,
            "answers": [],
            "awaiting_free_text": False,
        }
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text="A few quick questions about today's notes before I file them:",
            )
            await _send_question(context, user_id)
        except Exception:
            logger.exception("Daily review: failed to message user_id=%s", user_id)
            pending_reviews.pop(user_id, None)
