# Agents

| Agent | File | Writes |
|-------|------|--------|
| Harness | [harness.md](harness.md) | `system/constitution/`, `agents/`, `prompts/`, `schemas/` only |
| Ingestion | [ingestion.md](ingestion.md) | `raw/`, `system/state/`, `system/runs/` |
| Extractor | [extractor.md](extractor.md) | `system/review_queue/`, `system/runs/`, `system/state/` |
| Compiler | [compiler.md](compiler.md) | `Dawson's wiki/wiki/`, `system/runs/`, `system/state/` |
| Conversation | [conversation.md](conversation.md) | `system/review_queue/`, `system/runs/` |
| Research | [research.md](research.md) | `Dawson's wiki/wiki/Research/` only |

Pipeline order: Ingestion → Extractor → (review) → Compiler.

Harness is separate — maintains the harness, does not process renovation data.
