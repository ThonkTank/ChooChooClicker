#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_PATH="$SCRIPT_DIR/src/app.py"
if command -v python3 >/dev/null 2>&1; then
    exec python3 "$APP_PATH" "$@"
elif command -v python >/dev/null 2>&1; then
    exec python "$APP_PATH" "$@"
else
    echo "Fehler: Es wird eine Python-Installation (>=3.10) mit Tkinter-Unterstützung benötigt." >&2
    exit 1
fi
