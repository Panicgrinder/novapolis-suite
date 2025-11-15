#!/usr/bin/env python3
"""Run type checks: pyright (if present) and mypy.

Replaces `scripts/checks_types.ps1`.
"""
from __future__ import annotations
import shutil
import subprocess
import sys
from pathlib import Path


def find_exe(name: str) -> str | None:
    return shutil.which(name)


def main() -> int:
    root = Path(__file__).resolve().parent
    agent = root / 'novapolis_agent'

    pyright = find_exe('pyright')
    if pyright:
        rc = subprocess.run([pyright, '-p', 'pyrightconfig.json'], cwd=root).returncode
        if rc != 0:
            return rc

    venv_py = root / '.venv' / 'Scripts' / 'python.exe'
    if not venv_py.exists():
        venv_py = Path(sys.executable)

    rc = subprocess.run([str(venv_py), '-m', 'mypy', '--config-file', 'mypy.ini', 'app', 'scripts'], cwd=agent).returncode
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
