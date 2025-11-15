#!/usr/bin/env python3
"""Run `pytest -q` using venv python if available."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    venv_py = root / '.venv' / 'Scripts' / 'python.exe'
    python = str(venv_py) if venv_py.exists() else sys.executable
    return subprocess.run([python, '-m', 'pytest', '-q']).returncode


if __name__ == '__main__':
    raise SystemExit(main())
