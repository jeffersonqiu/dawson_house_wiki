# Compiler Agent

**Status:** not implemented

## Purpose

Turn approved extracted facts into Obsidian markdown in `Dawson's wiki/wiki/`.

## Inputs

- Approved facts (from extractor or cleared review queue)
- `system/constitution/note-creation.md`
- `system/schemas/*.yaml`

## Outputs

- New or updated compiled notes under `Dawson's wiki/wiki/`
- Run log → `system/runs/`

## May write

- `Dawson's wiki/wiki/**` (when justified and approved)
- `system/runs/**`
- `system/state/**` (entity registry)

## Must not

- Create placeholder notes
- Overwrite human sections without merge
- Delete `inbox/` or `raw/` files
- Write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)
