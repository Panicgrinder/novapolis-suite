#!/usr/bin/env python3
"""Quick wrapper to run pytest -q for Agent tests.

Replaces `scripts/run_pytest_quick.ps1`.
"""
from __future__ import annotations
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
    cwd = root / "novapolis_agent"
    cmd = [python, "-m", "pytest", "-q"]
    print("Running:", " ".join(cmd), "in", cwd)
    rc = subprocess.run(cmd, cwd=cwd).returncode
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
