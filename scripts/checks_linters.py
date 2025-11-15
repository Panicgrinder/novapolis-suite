#!/usr/bin/env python3
"""Run linters check (ruff + black), delegating to `run_linters.py` if present.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    delegate = root / 'run_linters.py'
    python = str(root / '.venv' / 'Scripts' / 'python.exe')
    if not Path(python).exists():
        python = sys.executable

    if delegate.exists():
        return subprocess.run([python, str(delegate)]).returncode

    # Fallback: run ruff + black directly
    rc = subprocess.run([python, '-m', 'ruff', 'check', '.']).returncode
    if rc != 0:
        return rc
    return subprocess.run([python, '-m', 'black', '--check', '.']).returncode


if __name__ == '__main__':
    raise SystemExit(main())
