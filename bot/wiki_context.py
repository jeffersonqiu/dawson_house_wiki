"""Build the text context the Conversation agent reads from.

Loads all compiled wiki notes (Dawson's wiki/wiki/**) plus the Conversation
agent's rule file, and assembles a single context blob to pass to Claude as
part of the system prompt.

Kept deliberately simple (read everything, no chunking/embeddings) — the wiki
is small enough (tens of short markdown files) to fit comfortably in context.
Revisit with retrieval/embeddings only if the wiki grows much larger.
"""

from __future__ import annotations

import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "Dawson's wiki" / "wiki"
CONVERSATION_AGENT_SPEC = REPO_ROOT / "system" / "agents" / "conversation.md"
SOURCE_OF_TRUTH_DOC = REPO_ROOT / "system" / "constitution" / "source-of-truth.md"


def _read(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"[missing: {path}]"


def load_wiki_notes() -> str:
    """Concatenate every .md file under the compiled wiki, with path headers."""
    chunks: list[str] = []
    if not WIKI_DIR.exists():
        return "[wiki directory not found]"

    for path in sorted(WIKI_DIR.rglob("*.md")):
        rel = path.relative_to(WIKI_DIR)
        content = _read(path)
        chunks.append(f"### File: {rel}\n\n{content.strip()}\n")

    return "\n---\n\n".join(chunks)


def load_agent_rules() -> str:
    """Conversation agent role definition + source-of-truth rules."""
    parts = [
        "## Conversation agent role (system/agents/conversation.md)",
        _read(CONVERSATION_AGENT_SPEC).strip(),
        "",
        "## Source of truth (system/constitution/source-of-truth.md)",
        _read(SOURCE_OF_TRUTH_DOC).strip(),
    ]
    return "\n\n".join(parts)


def build_system_prompt() -> str:
    rules = load_agent_rules()
    wiki = load_wiki_notes()

    return f"""You are the Conversation agent for the "Dawson House Wiki" renovation
knowledge base, accessed via a personal Telegram bot for Jefferson (and Marcella).

{rules}

## How to behave in this chat

- Answer questions about the renovation (rooms, items, vendors, tasks, decisions, budget,
  statuses) using ONLY the compiled wiki content provided below as ground truth.
- Be concise — this is a chat interface, not a document. Use short paragraphs, bullet
  points, and bold for key facts (prices, statuses, dates). Avoid restating large tables
  verbatim; summarize and cite the relevant note name (e.g. "see Working-Vanity Desk").
- If asked something the wiki doesn't cover, say so plainly — do not guess or fabricate
  prices, vendors, or statuses.
- If the user asks you to change/update/correct something in the wiki (a new fact, a price
  change, marking a task done, etc.), do NOT edit the wiki yourself. Instead, draft what the
  proposed change would be and tell the user it needs to go through the review queue +
  Compiler — you can describe what the proposal would contain, but the actual file write
  happens in the main Claude Code session (via `/extract` and `/compile`), not here.
- If asked to trigger a pipeline step ("check for new files", "run extraction", "compile the
  approved items"), explain that this happens via the `/ingest`, `/extract`, `/compile` slash
  commands in the Claude Code session on the project, and offer to summarize what each would
  do — but you cannot run them yourself from this chat.
- Today's date context is not reliable here; if a date matters, prefer dates/statuses as
  recorded in the wiki notes themselves.

## Compiled wiki contents (Dawson's wiki/wiki/**)

{wiki}
"""
