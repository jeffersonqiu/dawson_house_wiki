# Conversation Agent

**Status:** not implemented

## Purpose

Answer renovation questions from the compiled wiki; trigger pipeline steps on request.

## Inputs

- `Dawson's wiki/wiki/**`
- `system/constitution/*`
- Optional: `raw/`, `inbox/` for context

## Outputs

- Chat responses (read-only by default)
- Pipeline triggers → Ingestion / Extractor / Compiler
- Write proposals → `system/review_queue/`

## May write

- `system/review_queue/**`
- `system/runs/**`

## Must not

- Write compiled wiki without user approval
- Auto-run ingestion against Google APIs (not built)
- Write `system/constitution/`, `agents/`, `prompts/`, `schemas/` (Harness only)
