"""Shared config/secret-loading helpers for the Dawson House Wiki Telegram bots.

Used by both telegram_bot.py (Conversation agent + /research) and
capture_bot.py (quick-capture + daily review) — see bot/README.md for the
two-bot architecture.

GCP Secret Manager (optional, used for deployment — see bot/gcp/):
    If GCP_PROJECT_ID is set and a requested env var is NOT present in the
    environment, it's fetched from Secret Manager (secret ID == variable
    name, "latest" version) using the host's Application Default Credentials.
    Locally this is never triggered — bot/.env supplies values directly.
    See bot/gcp/setup-secrets.sh.
"""

from __future__ import annotations

import logging
import os

import llm_client

logger = logging.getLogger("dawson-wiki-bot")


def secret_from_manager(project_id: str, secret_id: str) -> str | None:
    """Fetch the latest version of `secret_id` from GCP Secret Manager.

    Lazily imports google-cloud-secret-manager so local runs (which never set
    GCP_PROJECT_ID) don't require the dependency to be installed.
    """
    try:
        from google.cloud import secretmanager
    except ImportError:
        logger.error(
            "GCP_PROJECT_ID is set but google-cloud-secret-manager isn't installed "
            "(it's in requirements.txt — re-run bot/run.sh)."
        )
        return None

    try:
        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
        response = client.access_secret_version(name=name)
        return response.payload.data.decode("utf-8").strip()
    except Exception:
        logger.exception("Failed to fetch secret '%s' from Secret Manager", secret_id)
        return None


def config_value(name: str, project_id: str | None) -> str | None:
    """Env var (incl. bot/.env) first; GCP Secret Manager fallback if configured."""
    value = os.environ.get(name)
    if value:
        return value
    if project_id:
        return secret_from_manager(project_id, name)
    return None


def ensure_model_api_key(model: str, project_id: str | None) -> str | None:
    """Best-effort: ensure the *_API_KEY needed by `model` is in os.environ
    (incl. Secret Manager fallback).

    Soft-required: returns the missing env var name if it couldn't be found
    (so the bot still starts and chat/research/daily-review can reply "not
    configured yet" at runtime), or None if the key is present.
    """
    provider = llm_client.provider_of(model)
    key_env_var = llm_client.api_key_env_var(provider)
    api_key = config_value(key_env_var, project_id)
    if api_key:
        os.environ[key_env_var] = api_key  # ensure litellm sees it (e.g. when from Secret Manager)
        return None
    logger.warning(
        "%s is not set — model '%s' is unavailable until it's configured "
        "(see bot/.env.example or bot/gcp/setup-secrets.sh).",
        key_env_var,
        model,
    )
    return key_env_var


def load_allowed_user_ids() -> set[int]:
    allowed_raw = os.environ.get("TELEGRAM_ALLOWED_USER_IDS", "")
    allowed_ids = {
        int(x.strip()) for x in allowed_raw.split(",") if x.strip().isdigit()
    }
    if not allowed_ids:
        logger.warning(
            "TELEGRAM_ALLOWED_USER_IDS is empty — the bot will refuse ALL users. "
            "Set it to your Telegram numeric user ID (get it from @userinfobot)."
        )
    return allowed_ids


def resolve_llm_model(default: str) -> str:
    """LLM_MODEL, or anthropic/<CLAUDE_MODEL> (legacy), or `default`."""
    if os.environ.get("LLM_MODEL"):
        return os.environ["LLM_MODEL"]
    if os.environ.get("CLAUDE_MODEL"):
        return f"anthropic/{os.environ['CLAUDE_MODEL']}"
    return default
