# Note Creation

## Default rule

**Do not create compiled `.md` files by default.** No placeholders.

## Create a new compiled note when

| Trigger | Path pattern |
|---------|----------------|
| Real room in source data | `Dawson's wiki/wiki/Rooms/{Room}/{Room}.md` |
| Real item to track | `Dawson's wiki/wiki/Rooms/{Room}/{Item}.md` |
| Real vendor | `Dawson's wiki/wiki/Vendors/{Vendor}.md` |
| Real task or follow-up | `Dawson's wiki/wiki/Tasks/TASK-#### - {title}.md` |
| Important decision | `Dawson's wiki/wiki/04 Decisions.md` (single log first) |

Task IDs: zero-padded four digits (`TASK-0001`).

## Room layout

Items live under room folders, not a global `Items/` folder.

```text
Dawson's wiki/wiki/Rooms/Kitchen/Kitchen.md
Dawson's wiki/wiki/Rooms/Kitchen/Induction Hob.md
```

## Do not create yet

- `Decisions/` folder (use one master log first)
- `Sources/` folder
- `Templates/` in the vault (use `system/prompts/` later)
- Room folders without real room data

## Update vs create

Prefer updating an existing compiled note over creating a duplicate. Search `wiki/` before adding a new file.

## Inbox

Inbox notes stay in `inbox/` after compilation. Link compiled notes back to the source when useful.
