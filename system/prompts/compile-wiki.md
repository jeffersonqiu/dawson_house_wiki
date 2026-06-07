# Compile to wiki

Read `system/constitution/note-creation.md` and `system/constitution/write-safety.md`.

**Input:** Approved YAML records (items, vendors, tasks) from extraction or cleared review queue.

**Task:** Create or update compiled notes under `Dawson's wiki/wiki/`.

**Rules:**
- Create a file only when [note-creation rules](../constitution/note-creation.md) justify it
- Merge into existing notes; do not overwrite human sections
- Link back to `source` in note frontmatter or a Sources section
- Log the run in `system/runs/{date}-compile.md`
- Uncertain changes → `system/review_queue/` first, not the wiki

**Room items path:** `Dawson's wiki/wiki/Rooms/{Room}/{Item}.md`
