# Extract from raw

Read `AGENT.md`, `system/constitution/`, and `system/schemas/`.

**Source:** `raw/sheets/{file}` or `raw/drive/{file}`

**Task:** Extract item, vendor, and task records. Output YAML blocks per schema.

**Rules:**
- Set `confidence: low` when ambiguous
- Set `source` to the raw file path (and row/section if applicable)
- Do not write to `wiki/` — output only
- List low-confidence items for `system/review_queue/`

**Output format:**

```yaml
items: []
vendors: []
tasks: []
review_needed: []
```
