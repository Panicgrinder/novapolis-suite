#!/usr/bin/env python3
"""Wrapper to run `scripts/check_frontmatter.py` using the venv python if available.

Replaces `scripts/run_frontmatter_validator.ps1`.
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


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent
    python = find_venv_python(root)
    script = root / "scripts" / "check_frontmatter.py"
    cmd = [python, str(script)] + argv
    print("Running:", " ".join(cmd))
    return subprocess.run(cmd).returncode


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
