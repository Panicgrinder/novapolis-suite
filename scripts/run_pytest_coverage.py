#!/usr/bin/env python3
"""
Wrapper: run_pytest_coverage.py
Runs pytest with coverage and fail-under threshold (default 80%). Writes CSV/log/receipt.
Usage: python scripts/run_pytest_coverage.py [--fail-under 80]
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--fail-under", type=int, default=80)
args = parser.parse_args()

ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / "novapolis_agent"
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
# Konsolidierte Temp-Pfade unter .tmp
TMP = ROOT / ".tmp" / "results" / "reports"
TMP.mkdir(parents=True, exist_ok=True)
LOG = TMP / f"pytest_coverage_{TS}.log"
RECEIPT = TMP / f"pytest_coverage_postflight_{TS}.md"

cmd = [
    sys.executable,
    "-m",
    "pytest",
    "-c",
    str(AGENT_DIR / "pytest.ini"),
    "--cov",
    "--cov-report=term-missing",
    "--cov-branch",
    "--cov-config",
    str(AGENT_DIR / ".coveragerc"),
    f"--cov-fail-under={args.fail_under}",
]
proc = subprocess.run(
    cmd,
    cwd=str(AGENT_DIR),
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
)
with LOG.open("w", encoding="utf8") as lh:
    lh.write(proc.stdout)

with RECEIPT.open("w", encoding="utf8") as rf:
    rf.write("---\n")
    rf.write(f"stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    rf.write("update: Ran pytest with coverage\n")
    rf.write(f"checks: returncode={proc.returncode}\n")
    rf.write("---\n\n")
    rf.write("# Postflight: pytest coverage\n\n")
    rf.write(f"Log: {LOG}\n\n")
    rf.write("Output (truncated):\n\n")
    rf.write(proc.stdout[:20000])

if __name__ == "__main__":
    sys.exit(proc.returncode)
