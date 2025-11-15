#!/usr/bin/env python3
"""Run `black .` using venv python if available."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    venv_py = root / '.venv' / 'Scripts' / 'python.exe'
    python = str(venv_py) if venv_py.exists() else sys.executable
    return subprocess.run([python, '-m', 'black', '.']).returncode


if __name__ == '__main__':
    raise SystemExit(main())
#!/usr/bin/env python3
"""Run black formatter on workspace (wrapper for VSCode task)
"""
import sys
import subprocess


def main():
    python = sys.executable
    rc = subprocess.run([python, "-m", "black", "."]).returncode
    sys.exit(rc)


if __name__ == "__main__":
    main()
