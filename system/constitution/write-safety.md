# Write Safety

## Roles

| Role | Job |
|------|-----|
| **Human** | Capture in `inbox/`, approve review queue, override compiled notes |
| **Harness** | Maintain `system/` harness config only |
| **Ingestion** | Import into `raw/` |
| **Extractor** | Read inputs → structured facts → review queue |
| **Compiler** | Write `Dawson's wiki/wiki/` |
| **Conversation** | Read wiki, propose via review queue |
| **Research** | Write new notes under `Dawson's wiki/wiki/Research/` only |
| **Capture** | Append-only quick-capture to `Dawson's wiki/inbox/` + `zz_images/` |

---

## Ownership

Who is responsible for each area. See **folder access** for read/write rules.

| Folder | Owned by | Responsibility |
|--------|----------|----------------|
| `Dawson's wiki/inbox/` | Human | Quick capture (Capture agent may also append new daily capture files) |
| `Dawson's wiki/zz_images/` | Human | Photos referenced from inbox notes (Capture agent may add new ones) |
| `Dawson's wiki/wiki/` | Compiler | Compiled renovation database |
| `Dawson's wiki/wiki/Research/` | Research | Web-research comparison notes (not renovation facts) |
| `raw/` | Ingestion | Imported Sheets/Drive snapshots |
| `system/review_queue/` | Human | Approve or reject proposed compiles |
| `system/constitution/`, `agents/`, `prompts/`, `schemas/` | Harness | Rules, roles, prompts, schemas |
| `system/state/`, `runs/` | Pipeline agents | Machine logs and sync state |

---

## Folder access

### `Dawson's wiki/inbox/`

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | ✓ |
| Harness | ✓ | ✗ |
| Ingestion | ✓ | ✗ |
| Extractor | ✓ | ✗ |
| Compiler | ✓ | ✗ |
| Conversation | ✓ | ✗ |
| **Capture** | ✓ | **✓ new `{date} telegram capture.md` files only; may append to its own files, never edit/delete other inbox notes** |

### `Dawson's wiki/zz_images/`

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | ✓ |
| Harness | ✓ | ✗ |
| Ingestion | ✓ | ✗ |
| Extractor | ✓ | ✗ |
| Compiler | ✓ | ✗ |
| Conversation | ✓ | ✗ |
| **Capture** | ✓ | **✓ new photo files only, via `/note`/photo messages** |

### `Dawson's wiki/wiki/` (compiled)

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | override only (not default workflow) |
| Harness | ✓ | ✗ |
| Ingestion | ✓ | ✗ |
| Extractor | ✓ | ✗ |
| Compiler | ✓ | ✓ per [note-creation.md](note-creation.md); merge only |
| Conversation | ✓ | ✗ — propose via review queue |

### `Dawson's wiki/wiki/Research/`

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | ✓ |
| Harness | ✓ | ✗ |
| Ingestion | ✓ | ✗ |
| Extractor | ✓ | ✗ |
| Compiler | ✓ | ✗ |
| Conversation | ✓ | ✗ |
| **Research** | ✓ | **✓ new notes only, via `/research`** |

Web-research comparison notes (e.g. "alternatives to the dining table"), not
renovation facts about items already owned/ordered — no review-queue gate
needed since nothing here overrides compiled item data. Organised by room,
mirroring `Rooms/` (see [note-creation.md](note-creation.md)).

### `raw/sheets/`, `raw/drive/`

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | ✓ manual export drops |
| Harness | ✓ | ✗ |
| Ingestion | ✓ | ✓ add/update snapshots |
| Extractor | ✓ | ✗ |
| Compiler | ✓ | ✗ |
| Conversation | ✓ | ✗ |

### `system/constitution/`, `agents/`, `prompts/`, `schemas/`

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | ✓ project design (rare) |
| **Harness** | ✓ | **✓ only agent that may write** |
| Ingestion | ✓ | ✗ |
| Extractor | ✓ | ✗ |
| Compiler | ✓ | ✗ |
| Conversation | ✓ | ✗ |

### `system/review_queue/`

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | ✓ approve, reject, comment |
| Harness | ✓ | ✗ |
| Ingestion | ✓ | ✗ |
| Extractor | ✓ | ✓ add proposals |
| Compiler | ✓ | ✗ until human approves |
| Conversation | ✓ | ✓ add proposals |

### `system/state/`, `system/runs/`

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | ✗ |
| Harness | ✓ | ✗ |
| Ingestion | ✓ | ✓ |
| Extractor | ✓ | ✓ |
| Compiler | ✓ | ✓ |
| Conversation | ✓ | ✓ |

Pipeline agents write logs and machine state here. Not renovation knowledge.

### Project root (`AGENT.md`, `HARNESS_PLAN.md`)

| Role | Read | Write |
|------|------|-------|
| Human | ✓ | ✓ |
| Harness | ✓ | ✓ harness docs only |
| All other agents | ✓ | ✗ |

---

## Review queue before compiler writes

- New room, vendor, or task note
- Price, vendor, or status change
- Task done or cancelled
- New decisions log row
- Low extractor confidence

File: `system/review_queue/{YYYY-MM-DD}-{slug}.md`

---

## Global never (all agents except where allowed above)

- Delete or rewrite `inbox/` or `raw/` without explicit user request
- Commit secrets
- Auto-sync Google APIs (not built)
- Put harness material inside the Obsidian vault
- **Pipeline agents writing `system/constitution/`, `agents/`, `prompts/`, or `schemas/`**
