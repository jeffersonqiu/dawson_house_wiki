"""Research agent — searches the web for product alternatives and writes a
comparison note to "Dawson's wiki/wiki/Research/{Room}/**".

Invoked via the /research command in telegram_bot.py. Unlike the read-only
Conversation agent, this agent writes new files directly to the wiki — but it
only ever creates new notes under Research/. It never touches Rooms/, Vendors/,
Tasks/, or 04 Decisions.md (the Compiler's territory), so it doesn't need the
review-queue gate in write-safety.md.

Design: model-agnostic via litellm. The LLM drives a client-side tool-calling
loop — it calls the `web_search` function (backed by the Tavily Search API,
TAVILY_API_KEY) up to MAX_SEARCH_ITERATIONS times, then writes the full note
(with YAML frontmatter), followed by a delimiter and a short chat-friendly
summary. Because web search is a normal function tool (not a provider-native
server-side tool), this works with any litellm model that supports tool
calling (Claude, GPT, Gemini, ...) — set via RESEARCH_LLM_MODEL/LLM_MODEL.
"""

from __future__ import annotations

import json
import os
import pathlib
import re

import httpx
import litellm

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "Dawson's wiki" / "wiki"
ROOMS_DIR = WIKI_DIR / "Rooms"
RESEARCH_DIR = WIKI_DIR / "Research"

SUMMARY_MARKER = "===SUMMARY==="
MAX_SEARCH_ITERATIONS = 8

TAVILY_API_URL = "https://api.tavily.com/search"

WEB_SEARCH_TOOL = {
    "type": "function",
    "function": {
        "name": "web_search",
        "description": (
            "Search the web for current information. Returns the top results "
            "with titles, URLs, and content snippets."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query.",
                }
            },
            "required": ["query"],
        },
    },
}


def _tavily_search(query: str) -> str:
    """Run a web search via the Tavily Search API, returning a text blob of
    results (title/URL/snippet per result) for the model to read."""
    api_key = os.environ.get("TAVILY_API_KEY")
    try:
        response = httpx.post(
            TAVILY_API_URL,
            json={
                "api_key": api_key,
                "query": query,
                "max_results": 5,
                "search_depth": "basic",
            },
            timeout=30,
        )
        response.raise_for_status()
    except httpx.HTTPError as exc:
        return f"Search failed: {exc}"

    results = response.json().get("results", [])
    if not results:
        return "No results found."

    return "\n\n".join(
        f"Title: {r.get('title', 'N/A')}\n"
        f"URL: {r.get('url', 'N/A')}\n"
        f"Content: {(r.get('content') or '')[:1000]}"
        for r in results
    )


def _existing_rooms() -> list[str]:
    if not ROOMS_DIR.exists():
        return []
    return sorted(p.name for p in ROOMS_DIR.iterdir() if p.is_dir())


def _build_system_prompt() -> str:
    rooms = _existing_rooms()
    rooms_list = "\n".join(f"- {r}" for r in rooms) or "(none yet)"
    return f"""You are the Research agent for the "Dawson House Wiki" renovation
knowledge base. The user describes something they want to buy or compare —
often a piece of furniture or appliance with specific dimensions and/or
functionality — and you research real alternatives currently for sale and
write up a comparison note.

## Task

1. Use the web_search tool (up to {MAX_SEARCH_ITERATIONS} calls total) to find
   3-5 real, currently-available products that match the user's description
   (dimensions, functionality, style, budget). Prefer options available in
   Singapore (SGD pricing) when relevant, but include good international
   options too if useful.
2. Once you have enough information, STOP calling tools and write a single
   self-contained Markdown note in the same style as this project's compiled
   wiki notes: YAML frontmatter, then a body with sections, exactly as
   specified below.

## Output format — respond with EXACTLY two parts and nothing else

Part 1 — the full Markdown note, starting with YAML frontmatter exactly like
this (fill in the values):

---
name: <short descriptive title, Title Case, suitable as a filename>
room: <one of the existing rooms listed below, or "General" if none fit>
type: research
query: "<the user's original request, verbatim>"
---

# <same title as name>

## Request
<restate what the user asked for, in your own words>

## Alternatives
For each of the 3-5 options (always at least 3 unless fewer genuinely exist),
a subsection (### heading, numbered "1. <Name>", "2. <Name>", ...) with these
exact bullet fields, in this order — use "N/A" for any field you could not
confirm, never omit a field:
- **Price:**
- **Dimensions:**
- **Key features:**
- **Meets your spec?:** Yes / Partial / No — compare this option's ACTUAL
  confirmed dimensions/specs (above) against every number the user specified
  (size, capacity, budget, etc.) one by one. If anything differs — even a
  different size variant of the "same" product — say so explicitly here,
  e.g. "No — this model is 120x60cm, you asked for 140x70cm" or
  "Partial — width matches (140cm) but depth is 65cm not 70cm".
- **Where to buy:**
- **Source URL:**

## Comparison
ALWAYS include this section as a Markdown table, even if some cells are
"N/A". Use EXACTLY these columns and one row per alternative (same order and
numbering as the Alternatives section):

| # | Name | Price | Dimensions | Meets Spec? | Source |
|---|------|-------|------------|-------------|--------|
| 1 | ... | ... | ... | ... | ... |

## Recommendation
1-2 sentences on which option(s) best fit the stated requirements and why.

## Sources
Bullet list of the URLs used.

Part 2 — on its own line, exactly `{SUMMARY_MARKER}`, followed by a chat
summary in PLAIN TEXT ONLY — no Markdown at all (no `**`, `#`, `|`, backticks,
or tables). Follow this exact template, one numbered line per alternative
(same order as Part 1):

Found <N> options for: <one-line restatement of the request>

1. <Name> - <Price> - <Meets spec? Yes/Partial/No> - <one-line note: key
   dimension/feature, and if Partial/No, what's actually different>
2. <Name> - <Price> - <Meets spec?> - <one-line note>
...

Recommended: <top pick name> (<price>) - <one sentence why>

IMPORTANT: This final response (Part 1 + Part 2) must NOT include any more
tool calls. Output ONLY these two parts. Do not add any commentary, preamble,
or sign-off before, between, or after them — including before Part 1 or after
Part 2. Do not wrap the note in a code fence (no ``` anywhere) — Part 1 must
start directly with the `---` of the YAML frontmatter as its very first
characters. Do not mention where the note is saved in Part 2 — that's added
separately.

## Existing rooms in the wiki (pick `room:` from this list when it fits)
{rooms_list}

## Rules
- GROUND EVERY FACT in web_search results from THIS conversation. Do not rely
  on prior/training knowledge of a product, brand, or model — product specs,
  prices, and size variants change and your training data is often stale or
  for the wrong region.
- Pay special attention to NUMBERS the user gave (dimensions, capacity,
  budget, quantity). A product is only a real match if a search result you
  read in THIS conversation explicitly confirms it meets that number for the
  SPECIFIC variant/SKU you're citing — not a different size in the same
  product line, and not an assumption that "custom sizes are usually
  available." If a result only confirms a different size, report that size
  and mark "Meets your spec?" Partial/No accordingly — never silently round
  or substitute a different size as if it matches.
- Do not fabricate prices, dimensions, or URLs — only report what the search
  results actually show; use "N/A" rather than guessing.
- If you can't find good matches, say so honestly in the note and summary
  rather than inventing or stretching options to fit.
- Keep the note focused and skimmable — this is research/reference material,
  not a final purchase decision.
- Follow the templates above exactly and consistently, every time — this
  output feeds an automated pipeline that parses it.
"""


def _slugify_filename(name: str) -> str:
    """Mirror existing wiki filenames: keep spaces/parens, strip path-unsafe chars."""
    cleaned = re.sub(r'[\\/:*?"<>|]', "-", name).strip()
    return cleaned or "Untitled"


_FRONTMATTER_START = re.compile(r"^---[ \t]*\nname:", re.MULTILINE)
_FENCE_LINE = re.compile(r"^[ \t]*```\w*[ \t]*$", re.MULTILINE)


def _extract_note(text: str) -> str:
    """Strip any preamble/commentary and stray code-fence markers the model
    adds despite instructions, leaving just the note starting at its YAML
    frontmatter."""
    text = _FENCE_LINE.sub("", text)
    match = _FRONTMATTER_START.search(text)
    if match:
        text = text[match.start() :]
    return text.strip()


_MD_BOLD_ITALIC = re.compile(r"(\*\*|__|\*|_)(.+?)\1")
_MD_INLINE_CODE = re.compile(r"`([^`]*)`")
_MD_HEADING = re.compile(r"^#+\s*", re.MULTILINE)
_TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE)


def _plainify(text: str) -> str:
    """Strip stray Markdown the model adds to the chat summary despite
    instructions, so Telegram (plain text, no parse_mode) renders consistently."""
    text = _MD_BOLD_ITALIC.sub(r"\2", text)
    text = _MD_INLINE_CODE.sub(r"\1", text)
    text = _MD_HEADING.sub("", text)
    text = _TABLE_ROW.sub("", text)
    return text.strip()


def _parse_frontmatter(note_markdown: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", note_markdown, re.DOTALL)
    fields: dict[str, str] = {}
    if not match:
        return fields
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"')
    return fields


def run_research(query: str, model: str) -> dict:
    """Run the research agent for `query` using `model` (a litellm
    "<provider>/<model>" string).

    Returns a dict with keys: note_markdown, title, room, summary.
    """
    system = _build_system_prompt()
    messages: list[dict] = [{"role": "user", "content": query}]

    full_text = ""
    for _ in range(MAX_SEARCH_ITERATIONS + 1):
        response = litellm.completion(
            model=model,
            max_tokens=8000,
            temperature=0.2,  # consistent structure/formatting over creativity
            messages=[{"role": "system", "content": system}, *messages],
            tools=[WEB_SEARCH_TOOL],
        )
        msg = response.choices[0].message
        tool_calls = msg.tool_calls or []

        if not tool_calls:
            full_text = (msg.content or "").strip()
            break

        messages.append(
            {
                "role": "assistant",
                "content": msg.content,
                "tool_calls": [tc.model_dump() for tc in tool_calls],
            }
        )
        for tc in tool_calls:
            try:
                args = json.loads(tc.function.arguments)
            except (json.JSONDecodeError, TypeError):
                args = {}
            result = _tavily_search(args.get("query", query))
            messages.append(
                {"role": "tool", "tool_call_id": tc.id, "content": result}
            )
    else:
        # Hit the iteration cap while the model still wanted to search — force
        # a final answer with no further tool access.
        response = litellm.completion(
            model=model,
            max_tokens=8000,
            temperature=0.2,
            messages=[{"role": "system", "content": system}, *messages],
        )
        full_text = (response.choices[0].message.content or "").strip()

    if SUMMARY_MARKER in full_text:
        note_markdown, _, summary = full_text.partition(SUMMARY_MARKER)
        summary = _plainify(summary)
    else:
        note_markdown = full_text
        summary = "Research complete — see the saved note for details."

    note_markdown = _extract_note(note_markdown)

    fields = _parse_frontmatter(note_markdown)
    title = fields.get("name") or "Untitled Research"
    room = fields.get("room") or "General"

    return {
        "note_markdown": note_markdown,
        "title": title,
        "room": room,
        "summary": summary,
    }


def save_research_note(title: str, room: str, note_markdown: str) -> pathlib.Path:
    """Write the note to Research/{room}/{title}.md, never overwriting."""
    room_dir = RESEARCH_DIR / _slugify_filename(room)
    room_dir.mkdir(parents=True, exist_ok=True)

    base_name = _slugify_filename(title)
    candidate = room_dir / f"{base_name}.md"
    counter = 2
    while candidate.exists():
        candidate = room_dir / f"{base_name} ({counter}).md"
        counter += 1

    candidate.write_text(note_markdown.rstrip() + "\n", encoding="utf-8")
    return candidate
