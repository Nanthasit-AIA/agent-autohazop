import json, os, re
from pathlib import Path
from typing import Any, Protocol

from .logging_conf import logger

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

class ResultStore(Protocol):
    def save(self, name: str, payload: dict) -> str: ...
    def load(self, name: str) -> dict | None: ...

class LocalStore:
    """Filesystem store. Used for local dev and docker-compose."""

    def __init__(self, root: Path):
        self.root = Path(root)

    def save(self, name: str, payload: dict) -> str:
        self.root.mkdir(parents=True, exist_ok=True)
        path = self.root / f"{slugify_filename(name)}.json"
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        logger.info("Saved result to %s", path)
        return str(path)

    def load(self, name: str) -> dict | None:
        path = self.root / f"{slugify_filename(name)}.json"
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

class BlobStore:
    """Azure Blob Storage store. One JSON blob per extraction result."""

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

    def save(self, name: str, payload: dict) -> str:
        key = f"{slugify_filename(name)}.json"
        self.container.upload_blob(
            name=key,
            data=json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"),
            overwrite=True,
        )
        logger.info("Saved result to blob %s", key)
        return key

    def load(self, name: str) -> dict | None:
        from azure.core.exceptions import ResourceNotFoundError

        key = f"{slugify_filename(name)}.json"
        try:
            blob = self.container.download_blob(key).readall()
        except ResourceNotFoundError:
            return None
        return json.loads(blob.decode("utf-8"))

_store: Any = None

def get_store() -> ResultStore:
    global _store
    if _store is None:
        backend = os.getenv("STORAGE_BACKEND", "local").lower()
        if backend == "blob":
            _store = BlobStore(os.getenv("BLOB_CONTAINER", "pid-results"))
        else:
            _store = LocalStore(Path(os.getenv("LOCAL_STORE_DIR", "data")))
        logger.info("Result store backend: %s", backend)
    return _store
