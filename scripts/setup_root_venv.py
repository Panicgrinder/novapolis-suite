"""
Idempotenter Ersatz für `scripts/setup_root_venv.ps1` als Python-Skript.
Zweck: Erstelle/aktualisiere Root-`.venv` und installiere requirements.

Usage:
    python -m scripts.setup_root_venv

Dieses Skript ist bewusst minimal — es prüft, ob `.venv` existiert und
gibt handlungsanweisungen oder führt einfache creation/installation aus,
je nach Umgebung/Policy.
"""
from __future__ import annotations
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / ".venv"
REQS = ["requirements.txt", "requirements-dev.txt"]


def main() -> int:
    print(f"Root: {ROOT}")
    if VENV.exists():
        print(".venv exists — no creation performed.")
        print("If you want to (re)create, run: python -m venv .venv && .venv\\Scripts\\pip install -r requirements.txt")
        return 0

    try:
        import venv
        print("Creating virtual environment at .venv...")
        venv.create(VENV, with_pip=True)
        pip = VENV / "Scripts" / "pip.exe" if sys.platform == "win32" else VENV / "bin" / "pip"
        reqs = [ROOT / r for r in REQS if (ROOT / r).exists()]
        if reqs:
            print("Installing requirements:")
            for r in reqs:
                print("  -", r)
            os.system(f'"{pip}" install ' + " ".join(str(p) for p in reqs))
        else:
            print("No requirements files found to install.")
        return 0
    except Exception as exc:
        print("Failed to create venv:", exc)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
