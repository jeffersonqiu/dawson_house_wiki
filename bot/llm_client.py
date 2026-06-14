"""Provider-agnostic chat completion for the Conversation agent.

LLM_MODEL is a litellm-style "<provider>/<model>" string, e.g.:
    anthropic/claude-sonnet-4-6
    openai/gpt-4o-mini

litellm picks the right SDK/endpoint from the prefix and reads the matching
*_API_KEY env var (ANTHROPIC_API_KEY, OPENAI_API_KEY, ...) automatically, so
switching models/providers is a config change only — no code changes.

NOTE: the Research agent (research_agent.py) is NOT covered by this module —
/research depends on Claude's server-side web_search tool and always talks to
the Anthropic SDK directly, regardless of LLM_MODEL. See telegram_bot.py.
"""

from __future__ import annotations

import litellm

# Avoid litellm's background telemetry/update-check network calls.
litellm.telemetry = False
litellm.suppress_debug_info = True


def provider_of(model: str) -> str:
    """The provider prefix of a litellm model string (e.g. "anthropic")."""
    provider, _, _ = model.partition("/")
    return provider


def api_key_env_var(provider: str) -> str:
    """The env var name litellm expects for a provider's API key."""
    return f"{provider.upper()}_API_KEY"


def chat_completion(model: str, system: str, messages: list[dict], max_tokens: int) -> str:
    """Send a system prompt + conversation history, return the reply text."""
    response = litellm.completion(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "system", "content": system}, *messages],
    )
    return (response.choices[0].message.content or "").strip()
