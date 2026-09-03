#!/usr/bin/env bash
#
# Build the ZIP that Azure App Service expects for a code (non-container) deploy.
#
# App Service unpacks the archive straight into /home/site/wwwroot, so app.py,
# requirements.txt and pid/ must sit at the ZIP root - not inside a folder.
#
#   ./infra/make-zip.sh
#   -> pid-extract-deploy.zip
set -euo pipefail

SRC="services/pid-extract"
OUT="${1:-pid-extract-deploy.zip}"

[ -f "$SRC/app.py" ] || { echo "Run this from the repo root."; exit 1; }

python - "$SRC" "$OUT" <<'PY'
import os, sys, zipfile

src, out = sys.argv[1], sys.argv[2]
SKIP_DIRS = {"__pycache__", ".pytest_cache", "data"}
SKIP_NAMES = {".env", ".dockerignore", "Dockerfile", "README.md"}

written = []
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f in SKIP_NAMES or f.endswith((".pyc", ".pyo")):
                continue
            full = os.path.join(root, f)
            arc = os.path.relpath(full, src).replace(os.sep, "/")
            z.write(full, arc)
            written.append(arc)

print(f"{out}  ({os.path.getsize(out)/1024:.1f} KB)")
for a in sorted(written):
    print("  " + a)

missing = {"app.py", "requirements.txt"} - set(written)
if missing:
    sys.exit(f"ERROR: missing from archive root: {missing}")
if any(a.startswith(".env") and a != ".env.example" for a in written):
    sys.exit("ERROR: a real .env was about to be uploaded")
PY
