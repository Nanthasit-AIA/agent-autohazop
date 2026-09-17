"""Blob mirror for generated HAZOP workbooks.

App Service wipes wwwroot on every deploy, which would otherwise take the
download links and the assistant's worksheet with it. Runs keep writing to
local disk as before - the agent saves incrementally and reads its own output -
and the finished workbooks are copied to Blob afterwards, then pulled back on
demand when the local copy has gone.

With no connection string configured this is inert and everything stays on
local disk, which is what local development does.
"""
import os
from pathlib import Path

from decorators import logger

PREFIX = "hazop"


def _container():
    conn = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "").strip()
    if not conn:
        return None
    try:
        from azure.storage.blob import BlobServiceClient

        return BlobServiceClient.from_connection_string(conn).get_container_client(
            os.getenv("BLOB_CONTAINER", "pid-results")
        )
    except Exception as exc:
        logger.warning("Blob mirror unavailable: %s", exc)
        return None


def _blob_name(path: Path) -> str:
    """hazop/<output folder>/<file name>, mirroring the on-disk layout."""
    return f"{PREFIX}/{path.parent.name}/{path.name}"


def mirror(paths) -> int:
    """Copy finished run artefacts to Blob. Never raises: a failed mirror must
    not fail the run the user just paid for."""
    container = _container()
    if container is None:
        return 0

    copied = 0
    for raw in paths:
        path = Path(raw)
        if not path.exists():
            continue
        try:
            with open(path, "rb") as fh:
                container.upload_blob(name=_blob_name(path), data=fh, overwrite=True)
            copied += 1
        except Exception as exc:
            logger.warning("Could not mirror %s to Blob: %s", path, exc)

    if copied:
        logger.info("Mirrored %d HAZOP file(s) to Blob", copied)
    return copied


def ensure_local(path) -> bool:
    """True if the file is on disk, pulling it back from Blob if it is not."""
    path = Path(path)
    if path.exists():
        return True

    container = _container()
    if container is None:
        return False

    try:
        data = container.download_blob(_blob_name(path)).readall()
    except Exception:
        return False

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        logger.info("Restored %s from Blob", _blob_name(path))
        return True
    except Exception as exc:
        logger.warning("Could not write restored blob to %s: %s", path, exc)
        return False
