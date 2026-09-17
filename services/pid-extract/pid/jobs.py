import threading, time, uuid
from typing import Any, Callable

from .logging_conf import logger

# In-memory job registry.
#
# Extraction runs for minutes, but Azure App Service closes idle HTTP requests
# after ~230s and that limit cannot be raised. So POST /api/extract returns a
# job id immediately and the client polls.
#
# This registry lives in one process, so gunicorn MUST run --workers 1
# (threads are fine). With more worker processes a poll could land on a worker
# that never saw the job.
_jobs: dict[str, dict[str, Any]] = {}
_lock = threading.Lock()

def submit(name: str, fn: Callable[[], Any]) -> str:
    return submit_with_id(uuid.uuid4().hex, name, fn)

def submit_with_id(job_id: str, name: str, fn: Callable[[], Any]) -> str:
    """Caller supplies the id so uploads can be stored under it before the job starts."""
    with _lock:
        _jobs[job_id] = {
            "status": "queued",
            "name": name,
            "result": None,
            "error": None,
            "started_at": time.time(),
        }

    def run() -> None:
        with _lock:
            _jobs[job_id]["status"] = "running"
        try:
            result = fn()
            with _lock:
                _jobs[job_id]["result"] = result
                _jobs[job_id]["status"] = "done"
            logger.info("Job %s (%s) done", job_id, name)
        except Exception as e:
            logger.exception("Job %s (%s) failed", job_id, name)
            with _lock:
                _jobs[job_id]["error"] = str(e)
                _jobs[job_id]["status"] = "error"

    threading.Thread(target=run, daemon=True, name=f"extract-{job_id[:8]}").start()
    return job_id

def get(job_id: str) -> dict[str, Any] | None:
    with _lock:
        job = _jobs.get(job_id)
        return dict(job) if job else None
