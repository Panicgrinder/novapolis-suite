#!/usr/bin/env python3
"""Wrapper for link-scan functionality.

This replaces the archived PowerShell `scripts/scan_links.ps1`. Where possible
it will invoke the repository Python utilities; if PowerShell-only logic is
required, it falls back to calling the archived PS1 via `pwsh -File` (if pwsh
is present). The archived original is available under
`novapolis-dev/archive/ps1_archives_20251114_2240/scripts/scan_links.ps1`.
"""
from __future__ import annotations
import shutil
import subprocess
import sys
from pathlib import Path


def pwsh_available() -> bool:
    return shutil.which("pwsh") is not None or shutil.which("powershell") is not None


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent
    archived = root / "novapolis-dev" / "archive" / "ps1_archives_20251114_2240" / "scripts" / "scan_links.ps1"
    if pwsh_available() and archived.exists():
        shell = shutil.which("pwsh") or shutil.which("powershell")
        cmd = [shell, "-NoProfile", "-File", str(archived)] + argv
        print("Delegating to archived PowerShell script:", cmd)
        return subprocess.run(cmd).returncode

    print("NOTICE: Full Python port of scan_links not implemented.")
    print("Archived PowerShell script saved at:", archived)
    print("To run link-scan, ensure pwsh is installed or port the PS1 to Python.")
    return 2


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
