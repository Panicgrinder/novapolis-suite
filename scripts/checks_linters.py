#!/usr/bin/env python3
"""
Wrapper: checks_linters.py
Runs ruff and black (checks only), captures output, writes a Postflight receipt.
Usage: python scripts/checks_linters.py
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path.cwd()
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
TMP = ROOT / ".tmp-results" / "reports"
TMP.mkdir(parents=True, exist_ok=True)
LOG = TMP / f"checks_linters_{TS}.log"
RECEIPT = TMP / f"checks_linters_postflight_{TS}.md"

COMMANDS = [
    (["ruff", "check", "."], "ruff"),
    (["python", "-m", "black", "--check", "."], "black"),
]

results = []
with LOG.open("w", encoding="utf8") as lh:
    for cmd, name in COMMANDS:
        lh.write(f"\n== {name} CMD: {' '.join(cmd)} ==\n")
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        lh.write(proc.stdout + "\n")
        results.append({"tool": name, "returncode": proc.returncode})

# write receipt
with RECEIPT.open("w", encoding="utf8") as rf:
    rf.write("---\n")
    rf.write(f"stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    rf.write("update: Ran linter checks (ruff + black --check)\n")
    rf.write("checks: logs created\n")
    rf.write("---\n\n")
    rf.write("# Postflight: checks_linters\n\n")
    rf.write(f"Log: {LOG}\n\n")
    rf.write("Results:\n")
    for r in results:
        rf.write(f"- {r['tool']}: returncode={r['returncode']}\n")

# Exit non-zero if any tool failed
exit_code = 0
for r in results:
    if r["returncode"] != 0:
        exit_code = 1

if __name__ == "__main__":
    sys.exit(exit_code)
