#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def python_exe(root: Path) -> str:
    candidates = [
        root / ".venv" / "Scripts" / "python.exe",
        root / ".venv" / "bin" / "python",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return sys.executable


def npm_exe() -> str:
    candidates = ["npm", "npm.cmd", "npm.exe"] if sys.platform.startswith("win") else ["npm"]
    for candidate in candidates:
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    return "npm"


def run_step(root: Path, command: list[str], label: str) -> int:
    print(f"[rp-hard-gates] -> {label}: {' '.join(command)}")
    proc = subprocess.run(command, cwd=str(root))
    code = int(proc.returncode)
    if code == 0:
        print(f"[rp-hard-gates] <- {label}: PASS")
    else:
        print(f"[rp-hard-gates] <- {label}: FAIL (exit={code})")
    return code


def main() -> int:
    root = repo_root()
    py = python_exe(root)
    npm = npm_exe()

    steps: list[tuple[str, list[str]]] = [
        (
            "validate:rp",
            [
                npm,
                "--prefix",
                "novapolis-rp/coding/tools/validators",
                "run",
                "validate:rp",
            ],
        ),
        (
            "validate:crossrefs",
            [
                npm,
                "--prefix",
                "novapolis-rp/coding/tools/validators",
                "run",
                "validate:crossrefs",
            ],
        ),
        (
            "checks_rp_consistency --strict",
            [py, "scripts/checks_rp_consistency.py", "--strict"],
        ),
    ]

    for label, command in steps:
        code = run_step(root, command, label)
        if code != 0:
            return code

    print("[rp-hard-gates] PASS: Alle RP-Hard-Gates erfolgreich.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
