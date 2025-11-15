#!/usr/bin/env python3
"""
Wrapper: tests_pytest_root.py
Runs `pytest -q` at repo root, writes log + receipt. Use for quick smoke tests.
Usage: python scripts/tests_pytest_root.py
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path.cwd()
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
TMP = ROOT / ".tmp-results" / "reports"
TMP.mkdir(parents=True, exist_ok=True)
LOG = TMP / f"pytest_root_{TS}.log"
RECEIPT = TMP / f"pytest_root_postflight_{TS}.md"

cmd = ["pytest", "-q"]
proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
with LOG.open("w", encoding="utf8") as lh:
    lh.write(proc.stdout)

with RECEIPT.open("w", encoding="utf8") as rf:
    rf.write("---\n")
    rf.write(f"stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    rf.write("update: Ran pytest -q at repo root\n")
    rf.write(f"checks: returncode={proc.returncode}\n")
    rf.write("---\n\n")
    rf.write("# Postflight: pytest root\n\n")
    rf.write(f"Log: {LOG}\n\n")
    rf.write("Output (truncated):\n\n")
    rf.write(proc.stdout[:10000])

if __name__ == "__main__":
    sys.exit(proc.returncode)
