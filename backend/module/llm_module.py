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


def _call_with_retries(
    fn: Callable[[], T],
    *,
    max_retries: int = 3,
    backoff_s: float = 2.0,
    context: str = "",
) -> T:
    for attempt in range(1, max_retries + 1):
        try:
            return fn()
        except Exception as exc:
            if attempt == max_retries:
                raise
            logger.warning("[%s] attempt %d/%d failed: %s", context, attempt, max_retries, exc)
            time.sleep(backoff_s * attempt)


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

