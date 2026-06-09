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

