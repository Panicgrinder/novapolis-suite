#!/usr/bin/env python3
"""
Wrapper: checks_types.py
Runs pyright and mypy (targets: app, scripts), writes logs and receipt.
Usage: python scripts/checks_types.py
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path.cwd()
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
TMP = ROOT / ".tmp-results" / "reports"
TMP.mkdir(parents=True, exist_ok=True)
LOG = TMP / f"checks_types_{TS}.log"
RECEIPT = TMP / f"checks_types_postflight_{TS}.md"

COMMANDS = [
    (["pyright", "-p", "pyrightconfig.json"], "pyright"),
    (["python", "-m", "mypy", "--config-file", "mypy.ini", "app", "scripts"], "mypy"),
]

results = []
with LOG.open("w", encoding="utf8") as lh:
    for cmd, name in COMMANDS:
        lh.write(f"\n== {name} CMD: {' '.join(cmd)} ==\n")
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        lh.write(proc.stdout + "\n")
        results.append({"tool": name, "returncode": proc.returncode})

with RECEIPT.open("w", encoding="utf8") as rf:
    rf.write("---\n")
    rf.write(f"stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    rf.write("update: Ran type checks (pyright + mypy)\n")
    rf.write("checks: logs created\n")
    rf.write("---\n\n")
    rf.write("# Postflight: checks_types\n\n")
    rf.write(f"Log: {LOG}\n\n")
    rf.write("Results:\n")
    for r in results:
        rf.write(f"- {r['tool']}: returncode={r['returncode']}\n")

exit_code = 0
for r in results:
    if r["returncode"] != 0:
        exit_code = 1

if __name__ == "__main__":
    sys.exit(exit_code)
