import json, os, re
from pathlib import Path
from typing import Any, Protocol

from .logging_conf import logger

# Both stores use the same two prefixes so local and Azure layouts match:
#   inputs/<job_id>/<filename>   uploaded drawings
#   results/<name>.json          extraction output
INPUT_PREFIX = "inputs"
RESULT_PREFIX = "results"

def slugify_filename(raw: str) -> str:
    """
    Turn an arbitrary name into a safe result key:
    - lowercases
    - replaces spaces with '_'
    - strips non-alphanumeric/_/-
    - ensures not empty
    """
    s = raw.strip().lower()
    s = s.replace(" ", "_")
    s = re.sub(r"[^a-z0-9_\-]+", "", s)
    return s or "pid_result"

class Store(Protocol):
    def put_input(self, job_id: str, filename: str, data: bytes) -> str: ...
    def get_input(self, key: str) -> bytes: ...
    def save_result(self, name: str, payload: dict) -> str: ...
    def load_result(self, name: str) -> dict | None: ...

class LocalStore:
    """Filesystem store. Used for local dev and docker compose."""

    def __init__(self, root: Path):
        self.root = Path(root)

    def put_input(self, job_id: str, filename: str, data: bytes) -> str:
        key = f"{INPUT_PREFIX}/{job_id}/{filename}"
        path = self.root / key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        logger.info("Stored input %s (%d bytes)", key, len(data))
        return key

    def get_input(self, key: str) -> bytes:
        return (self.root / key).read_bytes()

    def save_result(self, name: str, payload: dict) -> str:
        key = f"{RESULT_PREFIX}/{slugify_filename(name)}.json"
        path = self.root / key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        logger.info("Saved result %s", key)
        return key

    def load_result(self, name: str) -> dict | None:
        path = self.root / RESULT_PREFIX / f"{slugify_filename(name)}.json"
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

class BlobStore:
    """Azure Blob Storage. Inputs and outputs both live here."""

    def __init__(self, container: str):
        from azure.storage.blob import BlobServiceClient

        conn = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        if conn:
            service = BlobServiceClient.from_connection_string(conn)
        else:
            # Managed identity path - no code change needed to switch to it.
            from azure.identity import DefaultAzureCredential

            account = os.environ["AZURE_STORAGE_ACCOUNT"]
            service = BlobServiceClient(
                account_url=f"https://{account}.blob.core.windows.net",
                credential=DefaultAzureCredential(),
            )

        self.container = service.get_container_client(container)
        try:
            self.container.create_container()
        except Exception:
            pass  # already exists

    def put_input(self, job_id: str, filename: str, data: bytes) -> str:
        key = f"{INPUT_PREFIX}/{job_id}/{filename}"
        self.container.upload_blob(name=key, data=data, overwrite=True)
        logger.info("Stored input blob %s (%d bytes)", key, len(data))
        return key

    def get_input(self, key: str) -> bytes:
        return self.container.download_blob(key).readall()

    def save_result(self, name: str, payload: dict) -> str:
        key = f"{RESULT_PREFIX}/{slugify_filename(name)}.json"
        self.container.upload_blob(
            name=key,
            data=json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"),
            overwrite=True,
        )
        logger.info("Saved result blob %s", key)
        return key

    def load_result(self, name: str) -> dict | None:
        from azure.core.exceptions import ResourceNotFoundError

        key = f"{RESULT_PREFIX}/{slugify_filename(name)}.json"
        try:
            blob = self.container.download_blob(key).readall()
        except ResourceNotFoundError:
            return None
        return json.loads(blob.decode("utf-8"))

_store: Any = None

def get_store() -> Store:
    global _store
    if _store is None:
        backend = os.getenv("STORAGE_BACKEND", "local").lower()
        if backend == "blob":
            _store = BlobStore(os.getenv("BLOB_CONTAINER", "pid-results"))
        else:
            _store = LocalStore(Path(os.getenv("LOCAL_STORE_DIR", "data")))
        logger.info("Store backend: %s", backend)
    return _store
