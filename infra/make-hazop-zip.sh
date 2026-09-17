#!/usr/bin/env bash
#
# Build the ZIP for the HAZOP backend code deploy.
#
# Unlike the extraction service, this one keeps its folder structure: the
# assistant resolves Skill.md and skills/ by walking two levels up from
# backend/module/, so the archive root must hold backend/ and skills/ side by
# side, exactly as the repo does. Startup therefore uses --chdir backend.
#
#   ./infra/make-hazop-zip.sh
#   -> hazop-deploy.zip
set -euo pipefail

OUT="${1:-hazop-deploy.zip}"
[ -f "backend/app.py" ] || { echo "Run this from the repo root."; exit 1; }

python - "$OUT" <<'PY'
import os, sys, zipfile

out = sys.argv[1]
SKIP_DIRS = {"__pycache__", ".pytest_cache", ".venv", "aah01lib"}
# Old run output and scratch uploads are regenerated at runtime; only the seed
# P&ID documents need to ship.
SKIP_STATIC = {"hazop", "output", "uploads", "store", "file"}
SKIP_NAMES = {".env", "test.py"}

written = []
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for src in ("backend", "skills"):
        for root, dirs, files in os.walk(src):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            rel_root = os.path.relpath(root, ".").replace(os.sep, "/")
            if rel_root.startswith("backend/static"):
                parts = rel_root.split("/")
                if len(parts) > 2 and parts[2] in SKIP_STATIC:
                    dirs[:] = []
                    continue
            for f in files:
                if f in SKIP_NAMES or f.endswith((".pyc", ".pyo", ".xlsx", ".csv")):
                    continue
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, ".").replace(os.sep, "/"))
                written.append(os.path.relpath(full, ".").replace(os.sep, "/"))
    z.write("infra/hazop-requirements.txt", "requirements.txt")
    written.append("requirements.txt")

print(f"{out}  ({os.path.getsize(out)/1024/1024:.1f} MB, {len(written)} files)")

need = {"requirements.txt", "backend/app.py", "backend/Skill.md",
        "backend/module/assistant_module.py", "backend/module/llm_module.py"}
missing = need - set(written)
if missing:
    sys.exit(f"ERROR: missing from archive: {missing}")
if not any(a.startswith("skills/") for a in written):
    sys.exit("ERROR: skills/ is empty, the assistant would have no knowledge base")
if any(os.path.basename(a) == ".env" for a in written):
    sys.exit("ERROR: a real .env was about to be uploaded")
print(f"  backend files: {sum(1 for a in written if a.startswith('backend/'))}")
print(f"  skills files : {sum(1 for a in written if a.startswith('skills/'))}")
PY
