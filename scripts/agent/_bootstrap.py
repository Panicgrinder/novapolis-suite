from __future__ import annotations

import os
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def ensure_repo_root_on_syspath() -> None:
    root = str(repo_root())
    if root not in sys.path:
        sys.path.insert(0, root)


def ensure_cwd_repo_root() -> None:
    root = repo_root()
    try:
        cwd = Path.cwd().resolve()
    except Exception:
        return
    if cwd != root:
        os.chdir(root)
