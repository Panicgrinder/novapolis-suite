#!/usr/bin/env python3
"""Run pytest with coverage using the workspace venv or an existing Python wrapper.

This file replaces `scripts/run_pytest_coverage.ps1` by delegating to
`scripts/task_wrappers/run_pytest_coverage.py` if present, otherwise
attempting a direct pytest invocation similar to the archived PS1.
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
    wrapper = root / "scripts" / "task_wrappers" / "run_pytest_coverage.py"
    python = find_venv_python(root)
    if wrapper.exists():
        cmd = [python, str(wrapper)]
        print("Delegating to:", cmd)
        return subprocess.run(cmd).returncode

    # Fallback: simple pytest invocation
    agent_dir = root / "novapolis_agent"
    cmd = [python, "-m", "pytest", "-q", "--cov", "--cov-report=term-missing"]
    print("Fallback run:", cmd, "in", agent_dir)
    return subprocess.run(cmd, cwd=agent_dir).returncode


if __name__ == '__main__':
    raise SystemExit(main())
