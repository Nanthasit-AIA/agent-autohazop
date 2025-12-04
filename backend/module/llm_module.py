import os, random, time
from typing import Callable, TypeVar, Tuple, Any, Dict, TypedDict

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
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY not found in .env , please set in .env")

@timeit_log
def get_openai_sdk():
    return OpenAI()

@timeit_log
def get_chat_model(model_name="gpt-4.1-2025-04-14", temperature=1):
    return ChatOpenAI(model=model_name, 
                      temperature=temperature, 
                      api_key=openai_api_key,
                      verbose=True), model_name

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
    func: Callable[[], T],
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
            return func()
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
