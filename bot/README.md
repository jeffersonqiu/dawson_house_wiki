# Dawson House Wiki — Telegram Bot (Conversation agent)

A personal Telegram bot that answers renovation questions from the compiled wiki
(`Dawson's wiki/wiki/**`), acting as the **Conversation agent**
(`system/agents/conversation.md`). Read-only — it cannot edit the wiki; for changes,
use the `/extract` and `/compile` slash commands in a Claude Code session.

**Why Telegram, not WhatsApp:** Telegram bots are free and set up in ~2 minutes with no
business verification (just message @BotFather). WhatsApp Business API requires Meta
business verification (2-14 days), template approval, and per-message costs — not worth
it for a personal assistant. See `system/agents/conversation.md` for more detail.

---

## One-time setup

### 1. Create the Telegram bot

1. Open Telegram, search for **@BotFather**, start a chat.
2. Send `/newbot`, follow the prompts (choose a name and a username ending in `bot`,
   e.g. `DawsonHouseWikiBot`).
3. BotFather replies with a token like `123456789:AAExampleTokenFromBotFather`. Copy it.

### 2. Get your Telegram user ID

1. Search for **@userinfobot**, start a chat, it replies with your numeric user ID.
2. If Marcella should also have access, get her ID the same way.

### 3. Get an Anthropic API key

1. Go to https://console.anthropic.com/settings/keys
2. Create a key (this is separate from a Claude.ai / Claude Code subscription — it's
   billed per API usage; the wiki is small so costs per query should be a few cents at
   most with Sonnet).

### 4. Get a Tavily API key

1. Go to https://tavily.com and sign up (free tier available).
2. Copy your API key from the dashboard.

This powers `/research`'s `web_search` tool — required regardless of which LLM(s) you
configure below (see "Model-agnostic agents" below).

### 5. Configure

```bash
cd "dawson_house_wiki/bot"
cp .env.example .env
```

Edit `bot/.env`:

```env
TELEGRAM_BOT_TOKEN=123456789:AAExampleTokenFromBotFather
TELEGRAM_ALLOWED_USER_IDS=111111111,222222222   # your ID, and Marcella's if desired
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-sonnet-4-6                  # optional, this is the default
TAVILY_API_KEY=tvly-...
```

`bot/.env` is gitignored — never commit it.

#### Optional: use ChatGPT (or another provider) for everyday chat and/or /research

Both everyday chat and `/research` are routed through [litellm](https://docs.litellm.ai/),
so the model/provider is a config change — no code changes. Set `LLM_MODEL` to a
litellm `"<provider>/<model>"` string plus that provider's API key, e.g.:

```env
LLM_MODEL=openai/gpt-4o-mini
OPENAI_API_KEY=sk-...
```

This changes the model for both everyday chat and `/research`. To use a different model
for `/research` only (e.g. a stronger model for research, cheaper for chat), set
`RESEARCH_LLM_MODEL` separately:

```env
LLM_MODEL=openai/gpt-4o-mini
RESEARCH_LLM_MODEL=anthropic/claude-sonnet-4-6
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

`/research`'s `web_search` tool is backed by Tavily (`TAVILY_API_KEY`) either way — that's
independent of `LLM_MODEL`/`RESEARCH_LLM_MODEL`. If `LLM_MODEL` is unset, both default to
`anthropic/<CLAUDE_MODEL>`, same as before.

### 6. Run it

```bash
cd "dawson_house_wiki/bot"
./run.sh
```

First run creates a virtualenv (`bot/.venv`) and installs dependencies (takes ~30s),
then starts long-polling. Leave this running, open Telegram, find your bot by its
username, and send `/start`.

Stop with Ctrl-C.

---

## Running it permanently (macOS, launchd)

So the bot keeps running in the background (including after reboot/login), without
keeping a terminal open:

```bash
cd "dawson_house_wiki/bot"
cp com.dawsonhouse.wikibot.plist.example ~/Library/LaunchAgents/com.dawsonhouse.wikibot.plist
```

Edit `~/Library/LaunchAgents/com.dawsonhouse.wikibot.plist` and replace every
`REPLACE_WITH_ABSOLUTE_PATH_TO_PROJECT` with the absolute path to this repo, e.g.
`/Users/jeffersonqiu/Desktop/projects/dawson_house_wiki`.

Then:

```bash
launchctl load ~/Library/LaunchAgents/com.dawsonhouse.wikibot.plist
launchctl list | grep dawsonhouse   # should show it running
```

Logs: `bot/logs/stdout.log` and `bot/logs/stderr.log`.

To stop/disable:

```bash
launchctl unload ~/Library/LaunchAgents/com.dawsonhouse.wikibot.plist
```

To restart after editing `telegram_bot.py` or `wiki_context.py`:

```bash
launchctl unload ~/Library/LaunchAgents/com.dawsonhouse.wikibot.plist
launchctl load ~/Library/LaunchAgents/com.dawsonhouse.wikibot.plist
```

---

## Running it permanently on GCP (Compute Engine, Always Free tier)

This avoids needing your Mac to be on. A small `e2-micro` VM in one of the Always Free
regions runs the bot 24/7 for **$0/month** (within free-tier limits — see "Costs" below).

Deployment files for this live in `bot/gcp/`:
- `setup-secrets.sh` — run on your Mac first (see Step 0.5); creates
  `TELEGRAM_BOT_TOKEN` and `ANTHROPIC_API_KEY` as GCP Secret Manager secrets and
  grants the VM's service account read access
- `dawsonhouse-wikibot.service.example` — systemd unit (Linux equivalent of the launchd
  plist above)
- `setup-vm.sh` — one-time provisioning script you run on the VM
- `sync-wiki.sh` — keeps the VM's copy of the repo in sync with GitHub (see "Keeping the
  VM in sync" below)

**Secrets**: `TELEGRAM_BOT_TOKEN` and `ANTHROPIC_API_KEY` are stored in **GCP Secret
Manager**, not in a plaintext `bot/.env` on the VM. The bot fetches them at startup via
the VM's default service account (see `_secret_from_manager` in `telegram_bot.py`).
`TELEGRAM_ALLOWED_USER_IDS` (not a credential) still lives in `bot/.env` on the VM.

### Quick answers first

- **Does the VM need its own `git pull`?** Yes. The VM has its own independent clone of
  this repo — it does not share a filesystem with your Mac. `bot/gcp/sync-wiki.sh`,
  installed via cron by `setup-vm.sh`, runs `git pull` (fast-forward only) every 15
  minutes and restarts the bot service if anything changed, so wiki updates you `/compile`
  and push from your Mac show up on the bot within ~15 minutes automatically.
- **Does all the wiki content live there?** Yes — it's a normal clone of
  `github.com/jeffersonqiu/dawson_house_wiki` (public repo), nothing is excluded. The bot
  reads `Dawson's wiki/wiki/**` from that local clone exactly as it does on your Mac.
- **Any size concerns?** No. The whole git-tracked repo is well under 1MB (the wiki itself
  is ~200KB). The free-tier VM has 30GB of disk. This is a non-issue even if the wiki
  grows 100x.

### Step 0 — Re-authenticate gcloud (you need to do this — interactive)

The gcloud CLI on this Mac (`/Users/jeffersonqiu/google-cloud-sdk/bin/gcloud`, v475.0.0,
project `citric-inkwell-308409`) currently has an expired/invalid auth token. Before
creating anything, run:

```bash
gcloud auth login
```

This opens a browser for you to sign in with `jeffersonqiu1@gmail.com`. Then confirm the
right project is selected:

```bash
gcloud config set project citric-inkwell-308409
gcloud config get-value project
```

### Step 0.5 — Create the secrets in Secret Manager (run on your Mac)

After `gcloud auth login` and `gcloud config set project citric-inkwell-308409`, with
your local `bot/.env` already filled in (Step 4 above):

```bash
cd "dawson_house_wiki/bot/gcp"
./setup-secrets.sh
```

This enables the Secret Manager API, creates `TELEGRAM_BOT_TOKEN` and `ANTHROPIC_API_KEY`
as secrets from your local `bot/.env` values (without printing them), and grants the
Compute Engine default service account `roles/secretmanager.secretAccessor` on both —
so the VM can read them once it exists. Safe to re-run later (e.g. to rotate a key — it
adds a new secret version).

### Step 1 — Create the VM

Always Free e2-micro is available only in these regions: `us-west1` (Oregon),
`us-central1` (Iowa), `us-east1` (South Carolina). Pick whichever is closest/fine for you
(`us-west1` is closest to Singapore-ish latency-wise but it won't matter much for a
Telegram bot).

```bash
gcloud compute instances create dawsonhouse-wikibot \
  --zone=us-west1-b \
  --machine-type=e2-micro \
  --image-family=debian-12 \
  --image-project=debian-cloud \
  --boot-disk-size=30GB \
  --boot-disk-type=pd-standard \
  --tags=dawsonhouse-wikibot \
  --scopes=cloud-platform
```

Notes:
- `pd-standard` (not SSD) and `30GB` are both required to stay within the free tier.
- `--scopes=cloud-platform` is required for the Secret Manager fallback — without it,
  the VM's service account gets a metadata token that's valid for IAM purposes but
  rejected by the Secret Manager API with `403 ACCESS_TOKEN_SCOPE_INSUFFICIENT`, even
  though `setup-secrets.sh` granted the right IAM role. If you forgot this flag on an
  existing VM, fix it with (stop → update → start):
  ```bash
  gcloud compute instances stop dawsonhouse-wikibot --zone=us-west1-b
  gcloud compute instances set-service-account dawsonhouse-wikibot --zone=us-west1-b --scopes=cloud-platform
  gcloud compute instances start dawsonhouse-wikibot --zone=us-west1-b
  ```
- No firewall rules needed — the bot uses long-polling (outbound connections only to
  Telegram + Anthropic APIs), so nothing needs to accept inbound traffic besides the
  default SSH (which `gcloud compute ssh` handles automatically).

### Step 2 — SSH in and run the setup script

```bash
gcloud compute ssh dawsonhouse-wikibot --zone=us-west1-b
```

(First time: gcloud will offer to generate an SSH key for you — accept.)

Once connected, download and run the setup script (it's checked into the public repo, so
you can fetch it directly):

```bash
curl -fsSL https://raw.githubusercontent.com/jeffersonqiu/dawson_house_wiki/main/bot/gcp/setup-vm.sh -o setup-vm.sh
chmod +x setup-vm.sh
./setup-vm.sh
```

This installs git/python3/uv, clones the repo to `~/dawson_house_wiki`, creates
`bot/.env` from the template, detects the GCP project ID and bakes it into the systemd
unit as `GCP_PROJECT_ID` (so the Secret Manager fallback works), and installs+enables the
service (but doesn't start it yet), plus the cron sync job.

### Step 3 — Configure `bot/.env` on the VM

```bash
nano ~/dawson_house_wiki/bot/.env
```

Set `TELEGRAM_ALLOWED_USER_IDS` to the same value as your local `bot/.env`. **Leave
`TELEGRAM_BOT_TOKEN` and `ANTHROPIC_API_KEY` blank** — they're fetched from Secret Manager
(Step 0.5) via the VM's service account.

**Use the same Telegram bot token as your Mac, or a different one — just don't run both
your Mac's bot and the VM's bot with the same token at the same time** (Telegram's
long-polling API only allows one consumer per token; running two will cause "Conflict:
terminated by other getUpdates request" errors). Once the VM version is working, stop the
one on your Mac (`launchctl unload ...`).

### Step 4 — Start and verify

```bash
sudo systemctl start dawsonhouse-wikibot
sudo systemctl status dawsonhouse-wikibot
journalctl -u dawsonhouse-wikibot -f
```

Message your bot on Telegram — it should respond. Ctrl-C out of `journalctl -f` once
confirmed (the service keeps running).

### Keeping the VM in sync with wiki updates

After you run `/compile` locally and push to GitHub, the VM's cron job
(`bot/gcp/sync-wiki.sh`, runs every 15 min) will:
1. `git fetch` + fast-forward merge `origin/main`
2. If the repo actually changed, `sudo systemctl restart dawsonhouse-wikibot` so the bot
   reloads the updated wiki content

Check sync logs: `tail -f ~/dawson_house_wiki/bot/logs/sync.log`

To force an immediate sync without waiting for cron:
```bash
~/dawson_house_wiki/bot/gcp/sync-wiki.sh
```

### Costs

`e2-micro` + 30GB standard persistent disk in `us-west1`/`us-central1`/`us-east1` is
covered by GCP's [Always Free tier](https://cloud.google.com/free/docs/free-cloud-features#compute)
— **$0/month** as long as you stay within one free instance and don't add extra disks,
static IPs left unattached, etc. Outbound network usage from a Telegram bot is minimal
(text messages only) and well within the 1GB/month free egress to most destinations.

To stop incurring any possibility of charges later, you can always:
```bash
gcloud compute instances delete dawsonhouse-wikibot --zone=us-west1-b
```

---

## Usage

In Telegram, message your bot directly (or in a group it's been added to, if you want
shared access with Marcella):

- "What's the status of the kitchen appliances?"
- "How much have we spent so far vs budget?"
- "What did we decide about the TV size?"
- "What's still pending in the Master Bedroom?"
- "List open tasks"

Commands:
- `/start` or `/help` — intro message
- `/reset` — clear this chat's conversation memory (useful if it gets confused or you
  want to start a fresh topic)
- `/research <description>` — search the web for real alternatives matching your
  description (dimensions, functionality, style, budget) and save a comparison note to
  `Dawson's wiki/wiki/Research/{Room}/`. Example:
  `/research extendable dining table, ~180x90cm, dark wood, under $1500 SGD, for the
  Living-Dining room`. Takes ~30-60s (it runs several web searches). Unlike normal chat,
  this *does* write a new file to the wiki — but only a new note under `Research/`,
  never to `Rooms/`, `Vendors/`, `Tasks/`, or `04 Decisions.md`. See
  `system/agents/research.md`.
- `/note <text>` — quick-capture something you noticed during the day (a price, a
  vendor quote, an idea). Example: `/note Senso Studio quoted $4200 for kitchen
  cabinets`. Appended to `Dawson's wiki/inbox/{date} telegram capture.md`.
- Send a **photo** (with an optional caption) — also quick-captured: saved under
  `Dawson's wiki/zz_images/` and linked from today's capture file via the caption (or
  blank if none).

If you ask it to change something ("mark the dining table as delivered", "update the
ironing set price to $599"), it will explain what the change would be and that it needs
to go through `/extract` → review → `/compile` in a Claude Code session — it won't edit
the wiki itself.

### End-of-day clarification review

Once a day (`DAILY_REVIEW_HOUR`, default 21:00 in `WIKI_TZ`, default
`Asia/Singapore`), if you captured anything via `/note` or a photo that day, the bot
asks the configured LLM to find up to `DAILY_REVIEW_MAX_QUESTIONS` (default 3) points
that are ambiguous — which room/vendor something relates to, whether a price is a quote
or final, what's in a photo, etc. — including looking at any photos you sent.

Each question arrives as a Telegram message with inline buttons: pick one, tap "Other"
to type a free-text answer, or "Skip". Your answers are appended to that day's capture
file under a `## Clarifications` section for `/extract` to pick up later. If you didn't
capture anything that day, or the notes are already clear, nothing is sent — it's
silent. See `system/agents/capture.md`.

---

## How it works

- `wiki_context.py` — on every message, reads every file under `Dawson's wiki/wiki/**`
  plus `system/agents/conversation.md` and `system/constitution/source-of-truth.md`,
  and assembles them into the system prompt. The wiki is small (~70KB as of June 2026)
  so this is simple and always up to date — no caching, no embeddings, no vector DB.
- `telegram_bot.py` — long-polling Telegram bot (`python-telegram-bot`). Checks the
  sender's Telegram user ID against `TELEGRAM_ALLOWED_USER_IDS`, keeps a short
  in-memory conversation history per chat (lost on restart), and calls the
  Conversation agent's model via `llm_client.py` with the system prompt + history.
- `llm_client.py` — thin [litellm](https://docs.litellm.ai/) wrapper used by the
  Conversation agent (everyday chat). `LLM_MODEL` (`"<provider>/<model>"`, default
  `anthropic/<CLAUDE_MODEL>`) selects the model/provider; litellm reads the matching
  `*_API_KEY` from the environment.
- `research_agent.py` — backs `/research`. Also model-agnostic via litellm
  (`RESEARCH_LLM_MODEL`, default same as `LLM_MODEL`): the model drives a client-side
  tool-calling loop, calling a `web_search` function tool (backed by the Tavily Search
  API, `TAVILY_API_KEY`) up to 8 times, then writes a full Markdown note + chat summary
  in its final response; `telegram_bot.py` saves the note under
  `Dawson's wiki/wiki/Research/{Room}/`. See `system/agents/research.md`.
- `capture.py` — backs `/note` and photo messages: appends timestamped entries to
  `Dawson's wiki/inbox/{date} telegram capture.md` (Obsidian `![[filename]]` embeds for
  photos saved under `Dawson's wiki/zz_images/`).
- `daily_review.py` — the end-of-day clarification review, registered as a
  `JobQueue.run_daily()` job. Sends the day's capture file (text + any photos, as
  vision content) to `LLM_MODEL`, which returns up to `DAILY_REVIEW_MAX_QUESTIONS`
  multiple-choice questions as JSON; presents them via Telegram inline keyboards
  (`CallbackQueryHandler`) and appends answers to the capture file under
  `## Clarifications`. See `system/agents/capture.md`.

## Known limitations / future ideas

- The end-of-day review assumes 1:1 private chats only — it messages each
  `TELEGRAM_ALLOWED_USER_IDS` entry directly, relying on Telegram's `chat_id == user_id`
  for private chats. It won't work correctly in a group chat.
- No persistence — restart loses conversation history (acceptable for Q&A). An
  in-progress end-of-day review is also lost on restart: the capture file is only
  marked `reviewed: true` after the review completes, but a new review for that day
  isn't retried until the next day's job runs (which only looks at *that* day's file) —
  low-impact edge case for personal use.
- No write path for the Conversation agent (normal chat) — by design (see
  write-safety.md). `/research` is the one exception: a separate, narrowly-scoped
  Research agent that writes new notes under `Dawson's wiki/wiki/Research/` only (see
  system/agents/research.md). If/when you want the bot to be able to *propose*
  review-queue entries directly from normal chat, that would need filesystem write
  access to `system/review_queue/` and careful prompt-injection defenses, since
  Telegram input is less trusted than a Claude Code session.
- `/research` notes are not committed/pushed automatically — they show up as new files
  in `git status` on whichever machine runs the bot, for you to review and commit like
  any other change.
- `/research` requires `TAVILY_API_KEY` (its `web_search` tool is always Tavily-backed,
  regardless of `LLM_MODEL`/`RESEARCH_LLM_MODEL`). If it's missing, `/research` replies
  that it isn't configured yet but the rest of the bot keeps working normally.
- If the wiki grows much larger (hundreds of notes), the "load everything every time"
  approach in `wiki_context.py` will need to move to retrieval (embeddings/search)
  rather than full-context loading.
- WhatsApp could be added later via the WhatsApp Cloud API (Meta) if needed — the
  Claude-calling logic in `telegram_bot.py` is mostly platform-agnostic and could be
  adapted, but expect the business-verification overhead described above.
