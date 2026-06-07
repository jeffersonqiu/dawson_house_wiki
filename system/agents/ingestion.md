# Ingestion Agent

**Status:** proven — two runs completed (`system/runs/2026-06-07-ingestion-01.md`, `-02.md`)

## Purpose

Import Google Sheets and Drive into `raw/`.

## Inputs

- Google Sheets via MCP or manual export
- Google Drive docs via MCP or manual export

Setup: `MCP_SETUP.md`

In Claude Code (this session type), the working tools are the `mcp__claude_ai_Google_Drive__*`
connector tools — NOT the `google-workspace-mcp-advanced` config in `.cursor/mcp.json` (that's
for Cursor). Auth is already established; no per-run setup needed.

## Outputs

- Files in `raw/sheets/`, `raw/drive/`
- Updated `system/state/` import manifest
- Run log in `system/runs/`

## May write

- `raw/**`
- `system/state/**`
- `system/runs/**`

## Must not

- Write to `Dawson's wiki/wiki/` or `inbox/`
- Write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)
- Make mutating Drive calls (`create_file`, `copy_file`, `dry_run=False`) — read-only exports only

## How to run a pull (procedure that worked)

1. Read `system/state/manifest.md` first — it tracks known folder/file IDs and pull status so
   you don't re-discover the tree from scratch.
2. List a folder's full contents with `search_files`, query `parentId = '<id>'` and a generous
   `pageSize` (e.g. 100). Every folder in this Drive has had ≤9 items — one call surfaces
   everything; no pagination has been needed yet, but don't rely on the default page size.
3. For each file, pull with `read_file_content` (preferred — full natural-language extraction,
   handles Docs/Sheets/Slides/PDFs/OCR on images). Fall back to `download_file_content` only for
   binary formats `read_file_content` rejects, and even then expect raw bytes back (see gotcha 2).
4. Save as `raw/sheets/{slug}-{date}.md` (spreadsheets) or `raw/drive/{slug}-{date}.md`
   (everything else), with a small header noting source filename, Drive file ID, and folder path.
5. Update `system/state/manifest.md` (folder statuses + a row per pulled file) and write a run
   log `system/runs/{date}-ingestion-NN.md` modeled on the existing ones — including a
   "Learnings / Issues encountered" section for whatever you hit this time.
6. Fully enumerate `Archive`/`Old`/`Backup`-style folders rather than deprioritizing them — they
   have repeatedly held comparison-shopping artifacts (competing vendor quotes) that matter for
   later compilation.

## Known gotchas (from runs 01–02 — read before re-pulling)

1. **`search_files` snippets truncate (~3–5K chars).** Always re-pull with `read_file_content`
   for the full text before writing a snapshot — never write from the snippet alone.
2. **`download_file_content` ignores `exportMimeType` for non-Google-native binaries** (.xlsm,
   .docx, .zip, etc.) — it returns the raw original bytes, base64-encoded, regardless of the
   requested export type. If `read_file_content` errors "unsupported mime type" on a binary
   office file, there is no read-only path to its structured content — record it as a
   metadata-only `raw/` entry (id, name, why it failed) and move on.
3. **Empty `read_file_content` output reliably means "photo, no text."** Sample 1–2 files in an
   image-heavy folder; if empty, record the whole folder as one metadata-only batch file rather
   than pulling each photo individually.
4. **Filenames collide across folders — never key on filename alone.** Two files in this Drive
   share the exact name "WhatsApp Image 2026-02-07 at 3.17.30 PM.jpeg" but are completely
   different (a photo vs. an OCR-readable floor-layout drawing). Always track and verify by
   Drive file ID.
5. **OCR degrades on handwritten/dense-print docs** — expect garbled fragments; transcribe what
   you can, mark degraded sections explicitly, and flag that the source should be checked
   manually if exact figures matter.
6. **Multiple draft revisions can carry different totals/figures.** Don't assume the
   newest-looking draft is authoritative — the *signed/executed* document (e.g. in a "Signed
   Documents" folder) wins; cross-reference drafts back to it rather than discarding them.
7. **Large tool results may be auto-saved to a temp file** (JSON: `{content, id, mimeType,
   title}`) when they exceed the inline budget — inspect with `python3 -c "import json,
   base64; ..."` or `jq`, don't try to read the whole blob inline.
