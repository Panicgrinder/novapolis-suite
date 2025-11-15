#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[2]
venv_py = root / '.venv' / 'Scripts' / 'python.exe'
python = str(venv_py) if venv_py.exists() else sys.executable

cwd = root / 'novapolis_agent'
cmd = [python, '-m', 'pytest', '-q', '-m', '"api or streaming"']
# Use shell=False but pass marker as single argument; pytest accepts the -m expression
cmd = [python, '-m', 'pytest', '-q', '-m', 'api or streaming']
rc = subprocess.call(cmd, cwd=str(cwd))
sys.exit(rc)
