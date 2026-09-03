import os
from typing import Any, Dict, TypedDict

from openai import OpenAI

# Default extraction model. Overridable so a redeploy can change models without a code change.
EXTRACT_MODEL = os.getenv("EXTRACT_MODEL", "gpt-5.1-2025-11-13")

def get_client() -> OpenAI:
    """
    Provider seam. LLM_BASE_URL unset -> api.openai.com.
    Point it at a LiteLLM / OpenRouter proxy to switch providers.

    The key is checked here rather than at import time so the container can
    boot and answer /healthz even when it is misconfigured.
    """
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=key, base_url=os.getenv("LLM_BASE_URL") or None)

class LLMUsageMeta(TypedDict, total=False):
    id: str | None
    created: int | None
    model: str | None
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
