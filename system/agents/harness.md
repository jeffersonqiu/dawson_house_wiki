# Harness Agent

**Status:** active for repo setup; not automated

## Purpose

Maintain the harness itself — rules, roles, prompts, schemas under `system/`. Does not compile renovation notes or import sources.

## Inputs

- User requests to change project rules or harness design
- `HARNESS_PLAN.md`, `AGENT.md`

## Outputs

- Updates to `system/constitution/`, `system/agents/`, `system/prompts/`, `system/schemas/`
- Project docs at repo root when harness-related

## May write

- `system/constitution/**`
- `system/agents/**`
- `system/prompts/**`
- `system/schemas/**`
- `AGENT.md`, `HARNESS_PLAN.md` (harness docs only)

## May read

- Entire repo

## Must not

- Write `Dawson's wiki/inbox/` or `Dawson's wiki/wiki/`
- Write `raw/` import files
- Write `system/state/`, `system/runs/`, `system/review_queue/` (pipeline agents only)
- Run ingestion, extraction, or compilation on renovation data

Only this agent may change harness config in `system/`.
