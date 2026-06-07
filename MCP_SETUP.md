# Google Workspace MCP Setup

Project-scoped MCP for **Drive + Sheets** → future ingestion into `raw/`.

Config: `.cursor/mcp.json`  
Package: `google-workspace-mcp-advanced` (via `uvx` — already verified installable on this machine)

## 1. Google Cloud

1. [Google Cloud Console](https://console.cloud.google.com/) → create or pick a project
2. **APIs & Services → Library** → enable:
   - Google Drive API
   - Google Sheets API
3. **OAuth consent screen** → configure (External is fine for personal use)
4. **Credentials → Create OAuth client ID → Desktop app** → download JSON (optional) or copy Client ID + Secret

## 2. Local env

```bash
cp .env.example .env
# Edit .env — set USER_GOOGLE_EMAIL, GOOGLE_OAUTH_CLIENT_ID, GOOGLE_OAUTH_CLIENT_SECRET
```

## 3. Restart Cursor

Open this repo folder. Cursor loads `.cursor/mcp.json` from the project.

**Settings → MCP** should show `google-workspace` with Drive + Sheets tools.

## 4. First auth (one-time)

In **Agent** mode, ask e.g.:

> Search my Google Drive for spreadsheets with "dawson" or "renov"

On first call the server returns a **device auth** URL + code:

1. Open the URL in a browser
2. Enter the code, sign in, approve scopes
3. Retry the same request

Tokens persist in `~/.config/google-workspace-mcp-advanced/credentials/`.

## 5. Verify it works

Try these in Agent mode:

| Test | What success looks like |
|------|-------------------------|
| Drive search | Returns your renovation spreadsheets/docs |
| Sheets metadata | Reads a known spreadsheet ID or name |
| Sheets range | Returns cell values from a tab |

If tools don't appear: check `.env` values, restart Cursor, confirm MCP server shows green in settings.

## 6. Ingestion workflow (next)

Once MCP works, Ingestion agent should:

1. **Sheets** → export range or full sheet → `raw/sheets/{name}-{date}.csv`
2. **Drive** → export Google Docs as text/markdown → `raw/drive/{name}-{date}.md`
3. Log run in `system/runs/`
4. Update manifest in `system/state/`

Do not compile to `Dawson's wiki/wiki/` until Extractor + review queue.

## Safety

- Mutating MCP tools default to `dry_run=True` — ingestion should be **read-only** exports to `raw/`
- `.env` and OAuth tokens are gitignored

## Troubleshooting

| Problem | Fix |
|---------|-----|
| MCP server won't start | Run `uvx google-workspace-mcp-advanced==1.0.10 --help` in terminal |
| Auth loop | Delete `~/.config/google-workspace-mcp-advanced/credentials/` and re-auth |
| Wrong Google account | Re-auth with `USER_GOOGLE_EMAIL` account |
| `uvx` not found | `brew install uv` |
