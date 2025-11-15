#!/usr/bin/env python3
"""
Wrapper to run ruff + black checks using the repository .venv when available.
This replaces the archived PowerShell `scripts/run_linters.ps1`.
"""
from __future__ import annotations
import shutil
import subprocess
import sys
from pathlib import Path


def find_venv_python(root: Path) -> str:
    cand = root / ".venv" / "Scripts" / "python.exe"
    if cand.exists():
        return str(cand)
    return sys.executable


def main() -> int:
    root = Path(__file__).resolve().parent
    python = find_venv_python(root)

    cmds = [
        [python, "-m", "ruff", "check", "."],
        [python, "-m", "black", "--check", "."]
    ]

    rc = 0
    for cmd in cmds:
        print("Running:", " ".join(cmd))
        completed = subprocess.run(cmd)
        if completed.returncode != 0:
            rc = completed.returncode

    if rc == 0:
        print("Ruff and Black checks PASS")
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
