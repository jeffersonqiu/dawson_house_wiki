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

### 4. Configure

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
```

`bot/.env` is gitignored — never commit it.

### 5. Run it

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

If you ask it to change something ("mark the dining table as delivered", "update the
ironing set price to $599"), it will explain what the change would be and that it needs
to go through `/extract` → review → `/compile` in a Claude Code session — it won't edit
the wiki itself.

---

## How it works

- `wiki_context.py` — on every message, reads every file under `Dawson's wiki/wiki/**`
  plus `system/agents/conversation.md` and `system/constitution/source-of-truth.md`,
  and assembles them into the system prompt. The wiki is small (~70KB as of June 2026)
  so this is simple and always up to date — no caching, no embeddings, no vector DB.
- `telegram_bot.py` — long-polling Telegram bot (`python-telegram-bot`). Checks the
  sender's Telegram user ID against `TELEGRAM_ALLOWED_USER_IDS`, keeps a short
  in-memory conversation history per chat (lost on restart), and calls the Anthropic
  API (`anthropic` SDK) with the system prompt + history.

## Known limitations / future ideas

- No persistence — restart loses conversation history (acceptable for Q&A).
- No write path — by design (see write-safety.md). If/when you want the bot to be able
  to *propose* review-queue entries directly, that would need the bot process to have
  filesystem write access to `system/review_queue/` and careful prompt-injection
  defenses, since Telegram input is less trusted than a Claude Code session.
- If the wiki grows much larger (hundreds of notes), the "load everything every time"
  approach in `wiki_context.py` will need to move to retrieval (embeddings/search)
  rather than full-context loading.
- WhatsApp could be added later via the WhatsApp Cloud API (Meta) if needed — the
  Claude-calling logic in `telegram_bot.py` is mostly platform-agnostic and could be
  adapted, but expect the business-verification overhead described above.
