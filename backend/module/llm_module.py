import os, random, time
from typing import Callable, TypeVar, Tuple, Any, Dict, TypedDict, List

from dotenv import load_dotenv
import openai
from openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

from decorators import logger, timeit_log
T = TypeVar("T")

# ------------- SETUP LLM -----------------------------------
load_dotenv()

# Own API (OpenAI)
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    logger.warning("OPENAI_API_KEY not found in .env – Own API provider will be unavailable")

_own_api_models_raw = os.getenv("OPENAI_MODELS", "gpt-5.5-2026-04-23")
own_api_models: List[str] = [m.strip() for m in _own_api_models_raw.split(",") if m.strip()]

# LiteLLM proxy
litellm_base_url = os.getenv("LITELLM_BASE_URL", "")
litellm_api_key = os.getenv("LITELLM_API_KEY", "")
_litellm_models_raw = os.getenv("LITELLM_MODELS", "")
litellm_models: List[str] = [m.strip() for m in _litellm_models_raw.split(",") if m.strip()]


@timeit_log
def get_openai_sdk() -> OpenAI:
    return OpenAI()


@timeit_log
def get_litellm_sdk() -> OpenAI:
    if not litellm_base_url or not litellm_api_key:
        raise EnvironmentError("LITELLM_BASE_URL and LITELLM_API_KEY must be set in .env")
    return OpenAI(base_url=litellm_base_url, api_key=litellm_api_key)


def get_llm_client(provider: str = "own_api") -> OpenAI:
    if provider == "litellm":
        return get_litellm_sdk()
    return get_openai_sdk()


def get_llm_config() -> Dict[str, Any]:
    return {
        "groups": [
            {"id": "own_api", "label": "Own API", "models": own_api_models},
            {"id": "litellm", "label": "LiteLLM", "models": litellm_models},
        ]
    }


# ------------- MULTI-PROVIDER MODEL SELECTION ---------------
# Added alongside get_llm_client/get_llm_config, which keep working unchanged for
# /api/modify, /api/llm-config and the existing extract/HAZOP call sites.

openai_base_url = os.getenv("OPENAI_BASE_URL") or os.getenv("OPENAI_API_BASE")
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_base_url = os.getenv("OPENROUTER_BASE_URL") or "https://openrouter.ai/api/v1"
gemini_api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL") or "https://generativelanguage.googleapis.com/v1beta/openai/"
xai_api_key = os.getenv("XAI_API_KEY")
xai_base_url = os.getenv("XAI_BASE_URL") or "https://api.x.ai/v1"

default_chat_model = own_api_models[0] if own_api_models else "gpt-5.5-2026-04-23"


class ModelPreset(TypedDict, total=False):
    id: str
    provider: str
    provider_label: str
    label: str
    model: str
    api_key_env: str
    base_url: str | None
    configured: bool
    note: str


class ResolvedModel(TypedDict):
    provider: str
    provider_label: str
    model: str
    api_key: str
    base_url: str | None
    display_name: str


def _preset(provider, provider_label, label, model, api_key_env, api_key, base_url, note="") -> ModelPreset:
    return {
        "id": f"{provider}:{model}",
        "provider": provider,
        "provider_label": provider_label,
        "label": label,
        "model": model,
        "api_key_env": api_key_env,
        "base_url": base_url,
        "configured": bool(api_key),
        "note": note,
    }


def _build_model_presets() -> List[ModelPreset]:
    presets = [
        _preset("own_api", "Own API", f"Own API - {m}", m, "OPENAI_API_KEY", openai_api_key, openai_base_url)
        for m in own_api_models
    ]
    presets += [
        _preset("litellm", "LiteLLM", f"LiteLLM - {m}", m, "LITELLM_API_KEY", litellm_api_key, litellm_base_url)
        for m in litellm_models
    ]
    presets += [
        _preset("anthropic_openrouter", "Anthropic Claude", "Claude - Sonnet 5", "anthropic/claude-sonnet-5",
                "OPENROUTER_API_KEY", openrouter_api_key, openrouter_base_url, "via OpenRouter"),
        _preset("anthropic_openrouter", "Anthropic Claude", "Claude - Opus 4.8", "anthropic/claude-opus-4.8",
                "OPENROUTER_API_KEY", openrouter_api_key, openrouter_base_url, "via OpenRouter"),
        _preset("google", "Google Gemini", "Gemini - 3.1 Pro", "gemini-3.1-pro-preview",
                "GEMINI_API_KEY", gemini_api_key, gemini_base_url),
        _preset("google", "Google Gemini", "Gemini - 3.5 Flash", "gemini-3.5-flash",
                "GEMINI_API_KEY", gemini_api_key, gemini_base_url),
        _preset("xai", "xAI Grok", "xAI - Grok 4.3", "grok-4.3",
                "XAI_API_KEY", xai_api_key, xai_base_url),
    ]
    return presets


model_presets: List[ModelPreset] = _build_model_presets()


def _provider_api_settings(provider: str):
    if provider == "litellm":
        return litellm_api_key, litellm_base_url, "LITELLM_API_KEY", "LiteLLM"
    if provider == "anthropic_openrouter":
        return openrouter_api_key, openrouter_base_url, "OPENROUTER_API_KEY", "Anthropic Claude"
    if provider == "google":
        return gemini_api_key, gemini_base_url, "GEMINI_API_KEY", "Google Gemini"
    if provider == "xai":
        return xai_api_key, xai_base_url, "XAI_API_KEY", "xAI Grok"
    return openai_api_key, openai_base_url, "OPENAI_API_KEY", "Own API"


def _provider_from_model(model_name: str | None) -> str | None:
    model = str(model_name or "").strip()
    if not model:
        return None
    if model.startswith("anthropic/"):
        return "anthropic_openrouter"
    if model.startswith("gemini-"):
        return "google"
    if model.startswith("grok-"):
        return "xai"
    for preset in model_presets:
        if preset["model"] == model:
            return preset["provider"]
    return None


def resolve_model_selection(model_name: str | None = None, provider: str | None = None) -> ResolvedModel:
    model = str(model_name or "").strip() or default_chat_model
    selected_provider = str(provider or "").strip() or _provider_from_model(model) or "own_api"
    api_key, base_url, api_key_env, provider_label = _provider_api_settings(selected_provider)

    if not api_key:
        raise EnvironmentError(f"{api_key_env} not found in .env for provider {provider_label}.")

    label = next(
        (p["label"] for p in model_presets
         if p["provider"] == selected_provider and p["model"] == model),
        f"{provider_label} - {model}",
    )
    return {
        "provider": selected_provider,
        "provider_label": provider_label,
        "model": model,
        "api_key": api_key,
        "base_url": base_url,
        "display_name": label,
    }


def get_client_for_model(model_name: str | None = None, provider: str | None = None) -> OpenAI:
    """OpenAI-compatible client for any configured provider."""
    selected = resolve_model_selection(model_name=model_name, provider=provider)
    kwargs: Dict[str, Any] = {"api_key": selected["api_key"]}
    if selected["base_url"]:
        kwargs["base_url"] = selected["base_url"]
    return OpenAI(**kwargs)


def model_presets_for_client() -> List[Dict[str, Any]]:
    return [
        {
            "id": p["id"],
            "provider": p["provider"],
            "provider_label": p["provider_label"],
            "label": p["label"],
            "model": p["model"],
            "configured": p["configured"],
            "api_key_env": p["api_key_env"],
            "note": p.get("note", ""),
        }
        for p in model_presets
    ]


def _is_retryable_error(e: Exception) -> bool:
    """
    Decide whether an exception is worth retrying.
    - Timeouts, connection errors, rate limits, 5xx -> retry
    - BadRequestError (invalid request / schema) -> usually NOT retryable
    """
    if isinstance(e, openai.BadRequestError):
        return False

    return isinstance(
        e,
        (
            openai.APITimeoutError,
            openai.APIConnectionError,
            openai.RateLimitError,
            openai.APIError,
        ),
    )


def _call_with_retries(
    fn: Callable[[], T],
    *,
    max_retries: int = 3,
    base_backoff_s: float = 1.0,
    max_backoff_s: float = 10.0,
    jitter_ratio: float = 0.2,
    max_total_s: float = 60.0,
    context: str = "",
) -> T:
    start_all = time.perf_counter()

    for attempt in range(1, max_retries + 1):
        try:
            return fn()
        except Exception as e:
            elapsed = time.perf_counter() - start_all

            logger.warning(
                "[%s] attempt %d/%d failed after %.2fs: %s",
                context or "call",
                attempt,
                max_retries,
                elapsed,
                repr(e),
            )

            if not _is_retryable_error(e):
                logger.warning("[%s] non-retryable error, aborting", context or "call")
                raise

            if attempt >= max_retries:
                logger.error("[%s] reached max_retries=%d, aborting", context or "call", max_retries)
                raise

            if elapsed >= max_total_s:
                logger.error(
                    "[%s] exceeded max_total_s=%.1f, aborting retries", context or "call", max_total_s
                )
                raise

            raw_delay = base_backoff_s * (2 ** (attempt - 1))
            raw_delay = min(raw_delay, max_backoff_s)
            jitter = random.uniform(1.0 - jitter_ratio, 1.0 + jitter_ratio)
            delay = raw_delay * jitter

            logger.info(
                "[%s] retrying in %.2fs (attempt %d/%d)",
                context or "call",
                delay,
                attempt + 1,
                max_retries,
            )
            time.sleep(delay)
    raise RuntimeError(f"{context or 'call'}: retry loop exited unexpectedly")


@timeit_log
def get_chat_model(model_name="gpt-5.5-2026-04-23"):
    return (
        ChatOpenAI(
            model=model_name,
            api_key=openai_api_key,
            verbose=True,
        ),
        model_name,
    )

@timeit_log
def get_embedding_model(model_name="text-embedding-ada-002"):
    return OpenAIEmbeddings(
        model=model_name,
        api_key=openai_api_key
    )

@timeit_log
def build_qa_chain(llm, retriever):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff")

# ------------- META DATA & HANDOFF --------------------------
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

