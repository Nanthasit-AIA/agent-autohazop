import os
from typing import Any, Dict, TypedDict

from openai import OpenAI

# Extraction model, as named by the LiteLLM proxy's /v1/models listing.
EXTRACT_MODEL = os.getenv("EXTRACT_MODEL", "gpt-5.5")

def _base_url() -> str | None:
    """
    LiteLLM proxy endpoint. LLM_BASE_URL wins so a deployment can override the
    value inherited from the project's LITELLM_BASE_URL. Returns None to fall
    back to api.openai.com.
    """
    raw = os.getenv("LLM_BASE_URL") or os.getenv("LITELLM_BASE_URL")
    if not raw:
        return None
    raw = raw.rstrip("/")
    # The SDK appends /chat/completions etc. directly, so the version segment
    # has to be part of base_url. Proxies are usually configured without it.
    return raw if raw.endswith("/v1") else raw + "/v1"

def _api_key() -> str:
    key = (
        os.getenv("LLM_API_KEY")
        or os.getenv("LITELLM_API_KEY")
        or os.getenv("OPENAI_API_KEY")
    )
    if not key:
        raise RuntimeError(
            "No LLM credential set. Provide LITELLM_API_KEY (with LITELLM_BASE_URL) "
            "or OPENAI_API_KEY."
        )
    return key

def get_client() -> OpenAI:
    """
    Checked lazily rather than at import so the container still boots - and
    still answers /healthz - when credentials are missing or wrong.
    """
    return OpenAI(api_key=_api_key(), base_url=_base_url())

def provider_label() -> str:
    base = _base_url()
    return f"litellm:{base}" if base else "openai:api.openai.com/v1"

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

def build_llm_metadata(resp: Any, latency_s: float) -> Dict[str, Any]:
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

    prompt_tokens = (
        usage.get("prompt_tokens")
        or usage.get("input_tokens")
    )
    completion_tokens = (
        usage.get("completion_tokens")
        or usage.get("output_tokens")
    )
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
        "provider": provider_label(),
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
