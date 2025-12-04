import openai, time
from pathlib import Path
from typing import Dict, List

from module.llm_module import get_openai_sdk, build_llm_metadata, LLMUsageMeta
from module.schema_json import PIDResponse
from module.prompt.ext_prompt import PID_SYSTEM_PROMPT, build_pid_input
from decorators import logger, timeit_log
from utils import save_pid_json

@timeit_log
def _upload_vision_file(path: str | Path) -> str:
    client = get_openai_sdk()
    path = Path(path)

    with path.open("rb") as f:
        file_obj = client.files.create(
            file=f,
            purpose="user_data",  
        )
    logger.info("Uploaded file '%s' as id=%s", path, file_obj.id)
    return file_obj.id

# single file (PDF or image) using Responses API.
def extract_pid(
    file_path: str,
    *,
    process_description: str,
    model: str = "gpt-5.1-2025-11-13",
    max_retries: int = 3,
    backoff_s: float = 2.0,
) -> tuple[PIDResponse, LLMUsageMeta]:
    client = get_openai_sdk()

    file_id = _upload_vision_file(file_path)
    input_messages = build_pid_input(process_description, [file_id])

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
        f"Failed to obtain valid P&ID JSON for {file_path} after {max_retries} attempts."
    )

# multiple files (e.g. several PDFs + images) in ONE API call.
# NOTE:
# The model will automatically interpret ANY file types:
# P&ID, PFD, symbol sheets, spec sheets, etc.
# File order does NOT matter; all context is used together.
@timeit_log
def extract_pid_multi_files_single_call(
    file_paths: List[str],
    *,
    process_description: str,
    model: str = "gpt-5.1-2025-11-13",
    max_retries: int = 3,
    backoff_s: float = 2.0,
) -> tuple[PIDResponse, LLMUsageMeta]:
    client = get_openai_sdk()

    file_ids: List[str] = []
    for p in file_paths:
        try:
            fid = _upload_vision_file(p)
            file_ids.append(fid)
        except Exception as e:
            logger.error("Failed to upload file '%s': %s", p, e)
            raise

    input_messages = build_pid_input(process_description, file_ids)

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
        f"Failed to obtain valid P&ID JSON for files {file_paths} after {max_retries} attempts."
    )

# Run P&ID extraction for multiple files, but with ONE call per file.
@timeit_log
def extract_pid_batch(
    file_paths: List[str],
    *,
    process_description: str,
    model: str = "gpt-5.1-2025-11-13",
    max_retries: int = 3,
    backoff_s: float = 2.0,
) -> Dict[str, Dict[str, object]]:
    results: Dict[str, Dict[str, object]] = {}

    for p in file_paths:
        try:
            logger.info("Starting P&ID extraction for: %s", p)
            pid_result, meta = extract_pid(
                p,
                process_description=process_description,
                model=model,
                max_retries=max_retries,
                backoff_s=backoff_s,
            )
            results[p] = {
                "pid": pid_result,
                "metadata": meta,
            }
        except Exception as e:
            logger.error("Failed to extract P&ID from %s: %s", p, e)

    return results
