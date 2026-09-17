import os
from typing import Any, Dict, List, TypedDict

from openai import OpenAI

# ---------------------------------------------------------------- providers
# Two providers, chosen per request from the UI (v1.5 behaviour):
#   litellm  - the company proxy. Listed first, so it is the default.
#   own_api  - OpenAI directly. Only offered when OPENAI_API_KEY is set, so a
#              deployment that leaves that key out can only reach the proxy.
#
# Nothing is validated at import: the container must boot and answer /healthz
# even when credentials are missing or wrong.

def _models(env: str, fallback: str = "") -> List[str]:
    return [m.strip() for m in os.getenv(env, fallback).split(",") if m.strip()]

def _litellm_base_url() -> str | None:
    raw = os.getenv("LLM_BASE_URL") or os.getenv("LITELLM_BASE_URL")
    if not raw:
        return None
    raw = raw.rstrip("/")
    # The SDK appends /chat/completions etc., so the version segment has to be
    # part of base_url. Proxies are usually configured without it.
    return raw if raw.endswith("/v1") else raw + "/v1"

def _litellm_key() -> str | None:
    return os.getenv("LLM_API_KEY") or os.getenv("LITELLM_API_KEY") or None

def _openai_key() -> str | None:
    return os.getenv("OPENAI_API_KEY") or None

PROVIDERS = {
    "litellm": {
        "label": "LiteLLM",
        "models": lambda: _models("LITELLM_MODELS", "gpt-5.5"),
        "configured": lambda: bool(_litellm_key() and _litellm_base_url()),
        "client": lambda: OpenAI(api_key=_litellm_key(), base_url=_litellm_base_url()),
    },
    "own_api": {
        "label": "Own API",
        "models": lambda: _models("OPENAI_MODELS", "gpt-5.5-2026-04-23"),
        "configured": lambda: bool(_openai_key()),
        "client": lambda: OpenAI(api_key=_openai_key(), base_url=os.getenv("OPENAI_BASE_URL") or None),
    },
}

def get_llm_config() -> Dict[str, Any]:
    """Shape consumed by the UI's provider/model picker. Configured providers only."""
    groups = [
        {"id": pid, "label": p["label"], "models": p["models"]()}
        for pid, p in PROVIDERS.items()
        if p["configured"]()
    ]
    return {"groups": groups}

def default_provider() -> str:
    for pid, p in PROVIDERS.items():
        if p["configured"]():
            return pid
    return "litellm"

def default_model(provider: str) -> str:
    models = PROVIDERS.get(provider, PROVIDERS["litellm"])["models"]()
    return models[0] if models else "gpt-5.5"

def get_llm_client(provider: str = "litellm") -> OpenAI:
    p = PROVIDERS.get(provider)
    if p is None:
        raise ValueError(f"Unknown LLM provider '{provider}'. Choose one of: {', '.join(PROVIDERS)}")
    if not p["configured"]():
        if provider == "litellm":
            raise RuntimeError("LiteLLM is not configured: set LITELLM_BASE_URL and LITELLM_API_KEY")
        raise RuntimeError("Own API is not configured: set OPENAI_API_KEY")
    return p["client"]()

def provider_label(provider: str = "litellm") -> str:
    if provider == "litellm":
        return f"litellm:{_litellm_base_url()}"
    return "openai:api.openai.com/v1"

# ---------------------------------------------------------------- metadata
class LLMUsageMeta(TypedDict, total=False):
    id: str | None
    created: int | None
    model: str | None
    provider: str
    tokens: Dict[str, Any]
    response_type: str
    reasoning_effort: str
    verbosity: str
    latency_s: float

def build_llm_metadata(resp: Any, latency_s: float, provider: str = "litellm") -> Dict[str, Any]:
    usage_obj = getattr(resp, "usage", None)

    if usage_obj is None:
        usage: Dict[str, Any] = {}
    elif isinstance(usage_obj, dict):
        usage = usage_obj
    else:
        try:
            usage = usage_obj.model_dump()
        except AttributeError:
            try:
                usage = usage_obj.dict()
            except Exception:
                usage = dict(usage_obj)

    prompt_tokens = usage.get("prompt_tokens") or usage.get("input_tokens")
    completion_tokens = usage.get("completion_tokens") or usage.get("output_tokens")
    total_tokens = usage.get("total_tokens")

    if total_tokens is None and prompt_tokens is not None and completion_tokens is not None:
        try:
            total_tokens = int(prompt_tokens) + int(completion_tokens)
        except Exception:
            total_tokens = None

    return {
        "id": getattr(resp, "id", None),
        "created": getattr(resp, "created", None),
        "model": getattr(resp, "model", None),
        "provider": provider_label(provider),
        "tokens": {
            "prompt": prompt_tokens,
            "completion": completion_tokens,
            "total": total_tokens,
        },
        "response_type": getattr(resp, "response_type", "json_schema"),
        "reasoning_effort": getattr(resp, "reasoning_effort", "none"),
        "verbosity": getattr(resp, "verbosity", "medium"),
        "latency_s": round(latency_s, 4),
    }
