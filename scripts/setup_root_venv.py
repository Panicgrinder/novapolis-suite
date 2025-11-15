#!/usr/bin/env python3
"""Create/ensure root .venv and install dependencies (idempotent).

Replaces `scripts/setup_root_venv.ps1` with a cross-platform Python wrapper.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path


def main(recreate: bool = False) -> int:
    root = Path(__file__).resolve().parent
    venv_path = root / '.venv'
    py = sys.executable

    if recreate and venv_path.exists():
        import shutil
        shutil.rmtree(venv_path)

    if not venv_path.exists():
        print('Creating virtual environment at', venv_path)
        subprocess.check_call([py, '-m', 'venv', str(venv_path)])

    venv_python = venv_path / 'Scripts' / 'python.exe'
    if not venv_python.exists():
        venv_python = venv_path / 'bin' / 'python'
    if not venv_python.exists():
        print('ERROR: python not found in created venv', file=sys.stderr)
        return 1

    print('Upgrading pip')
    subprocess.check_call([str(venv_python), '-m', 'pip', 'install', '--upgrade', 'pip'])

    # Install requirements if present
    req_base = root / 'requirements.txt'
    req_dev = root / 'requirements-dev.txt'
    if req_base.exists():
        print('Installing requirements.txt')
        subprocess.check_call([str(venv_python), '-m', 'pip', 'install', '-r', str(req_base)])
    if req_dev.exists():
        print('Installing requirements-dev.txt')
        subprocess.check_call([str(venv_python), '-m', 'pip', 'install', '-r', str(req_dev)])

    print('Done. Virtual environment ready at', venv_path)
    return 0


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--recreate', action='store_true')
    args = p.parse_args()
    raise SystemExit(main(args.recreate))
