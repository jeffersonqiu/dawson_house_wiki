# Extract from inbox

Read `AGENT.md`, `system/constitution/`, and `system/schemas/`.

**Source:** `Dawson's wiki/inbox/{filename}`

**Task:** Extract item, vendor, and task records. Output YAML blocks per schema.

**Rules:**
- Set `confidence: low` when ambiguous
- Set `source` to the inbox file path
- Do not write to `wiki/` — output only
- List low-confidence items for `system/review_queue/`

**Output format:**

```yaml
items: []
vendors: []
tasks: []
review_needed: []
```
