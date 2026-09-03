import openai, time
from typing import Sequence

from .llm import get_client, build_llm_metadata, EXTRACT_MODEL, LLMUsageMeta
from .schema import PIDResponse
from .prompt import PID_SYSTEM_PROMPT, build_pid_input
from .logging_conf import logger, timeit_log

# Files are inlined as base64 content parts rather than uploaded first: the
# LiteLLM proxy does not expose the Files API. See pid/prompt.py.

# single file (PDF or image) using Responses API.
def extract_pid(
    file: tuple[str, bytes],
    *,
    process_description: str,
    model: str = EXTRACT_MODEL,
    max_retries: int = 3,
    backoff_s: float = 2.0,
) -> tuple[PIDResponse, LLMUsageMeta]:
    client = get_client()

    input_messages = build_pid_input(process_description, [file])

    for attempt in range(1, max_retries + 1):
        try:
            start_t = time.perf_counter()

            resp = client.responses.parse(
                model=model,
                instructions=PID_SYSTEM_PROMPT,
                input=input_messages,
                text_format=PIDResponse,
            )

            elapsed = time.perf_counter() - start_t

            pid_result: PIDResponse = resp.output_parsed
            meta = build_llm_metadata(resp, elapsed)

            total_tokens = meta.get("tokens", {}).get("total")
            logger.info(
                "LLM single-file usage: model=%s total_tokens=%s latency=%.3fs",
                meta.get("model"),
                total_tokens,
                meta["latency_s"],
            )

            return pid_result, meta

        except openai.BadRequestError as e:
            logger.warning(
                "[attempt %d/%d] JSON validation or request failed: %s",
                attempt,
                max_retries,
                getattr(e, "message", str(e)),
            )
        except openai.APITimeoutError as e:
            logger.warning(
                "[attempt %d/%d] OpenAI timeout: %s",
                attempt,
                max_retries,
                e,
            )
        except openai.APIConnectionError as e:
            logger.warning(
                "[attempt %d/%d] OpenAI connection error: %s",
                attempt,
                max_retries,
                e,
            )

        if attempt < max_retries:
            time.sleep(backoff_s * attempt)

    raise RuntimeError(
        f"Failed to obtain valid P&ID JSON for {file[0]} after {max_retries} attempts."
    )

# multiple files (e.g. several PDFs + images) in ONE API call.
# NOTE:
# The model will automatically interpret ANY file types:
# P&ID, PFD, symbol sheets, spec sheets, etc.
# File order does NOT matter; all context is used together.
@timeit_log
def extract_pid_multi_files_single_call(
    files: Sequence[tuple[str, bytes]],
    *,
    process_description: str,
    model: str = EXTRACT_MODEL,
    max_retries: int = 3,
    backoff_s: float = 2.0,
) -> tuple[PIDResponse, LLMUsageMeta]:
    client = get_client()

    input_messages = build_pid_input(process_description, files)

    for attempt in range(1, max_retries + 1):
        try:
            start_t = time.perf_counter()

            resp = client.responses.parse(
                model=model,
                instructions=PID_SYSTEM_PROMPT,
                input=input_messages,
                text_format=PIDResponse,
            )

            elapsed = time.perf_counter() - start_t

            pid_result: PIDResponse = resp.output_parsed
            meta = build_llm_metadata(resp, elapsed)

            logger.info(
                "LLM multi-files usage: model=%s total_tokens=%s latency=%.3fs",
                meta["model"],
                meta["tokens"]["total"],
                meta["latency_s"],
            )

            return pid_result, meta

        except openai.BadRequestError as e:
            logger.warning(
                "[attempt %d/%d] JSON validation or request failed (multi-files): %s",
                attempt,
                max_retries,
                getattr(e, "message", str(e)),
            )
        except openai.APITimeoutError as e:
            logger.warning(
                "[attempt %d/%d] OpenAI timeout (multi-files): %s",
                attempt,
                max_retries,
                e,
            )
        except openai.APIConnectionError as e:
            logger.warning(
                "[attempt %d/%d] OpenAI connection error (multi-files): %s",
                attempt,
                max_retries,
                e,
            )

        if attempt < max_retries:
            time.sleep(backoff_s * attempt)

    raise RuntimeError(
        f"Failed to obtain valid P&ID JSON for files {[n for n, _ in files]} after {max_retries} attempts."
    )
