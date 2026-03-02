#!/usr/bin/env python
"""Startet den minimalen Sim-API-Server robust aus dem Workspace heraus."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import uvicorn


def _ensure_app_import_path() -> None:
    """Ensure `app.*` can be imported regardless of current working directory."""
    project_root = Path(__file__).resolve().parents[1]
    root_text = str(project_root)
    if root_text not in sys.path:
        sys.path.insert(0, root_text)


def main() -> None:
    _ensure_app_import_path()
    port = int(os.getenv("AGENT_PORT", "8765"))
    uvicorn.run("app.api.sim:app", host="127.0.0.1", port=port, reload=False)


if __name__ == "__main__":
    main()
