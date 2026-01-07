from __future__ import annotations

import importlib
import runpy
import sys

from ._bootstrap import ensure_cwd_repo_root, ensure_repo_root_on_syspath


def import_module(module: str):
    ensure_repo_root_on_syspath()
    ensure_cwd_repo_root()
    return importlib.import_module(module)


def run_module(module: str, argv: list[str] | None = None) -> int:
    ensure_repo_root_on_syspath()
    ensure_cwd_repo_root()

    if argv is None:
        argv = sys.argv[1:]
    sys.argv = [module, *argv]

    runpy.run_module(module, run_name="__main__")
    return 0
