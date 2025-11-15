#!/usr/bin/env python3
"""Run ruff checks and black --check as a combined wrapper.
Creates exit code 0 on success, 1 on failure.
"""
import sys
import subprocess


def run(cmd):
    proc = subprocess.run(cmd)
    return proc.returncode


def main():
    python = sys.executable
    # ruff check .
    rc1 = run([python, "-m", "ruff", "check", "."])
    # black --check .
    rc2 = run([python, "-m", "black", "--check", "."]) 
    if rc1 != 0 or rc2 != 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
