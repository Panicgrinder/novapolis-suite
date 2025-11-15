#!/usr/bin/env python3
"""
Lightweight Markdown link scanner.

Scans Markdown files (excludes `.tmp-results` and `Backups`) for HTTP/HTTPS
links and writes a simple report. The tool does not resolve links and
complements the archived PowerShell scanner.
"""

import csv
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(".")
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT_DIR = ROOT / ".tmp-results" / "reports"
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = OUT_DIR / f"scan_links_{TS}.log"
CSV = OUT_DIR / f"scan_links_{TS}.csv"

link_re = re.compile(r"\bhttps?://[^)\s]+", re.IGNORECASE)

md_files = [
    p for p in ROOT.rglob("*.md") if ".tmp-results" not in str(p) and "Backups" not in str(p)
]
entries = []
with LOG.open("w", encoding="utf8") as lh:
    lh.write(f"SCAN {datetime.now().isoformat()} FILES={len(md_files)}\n")
    for f in md_files:
        text = f.read_text(encoding="utf8", errors="ignore")
        for m in link_re.finditer(text):
            url = m.group(0)
            entries.append({"file": str(f), "url": url})
            lh.write(f"{f}\t{url}\n")

# write CSV
with CSV.open("w", encoding="utf8", newline="") as cf:
    if entries:
        writer = csv.DictWriter(cf, fieldnames=["file", "url"])
        writer.writeheader()
        for e in entries:
            writer.writerow(e)

# write a short receipt
REC = Path("novapolis-dev") / "archive" / "docs" / "donelogs" / f"scan_links_postflight_{TS}.md"
REC.parent.mkdir(parents=True, exist_ok=True)
with REC.open("w", encoding="utf8") as rf:
    rf.write("---\n")
    rf.write(f"stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    rf.write("update: Link scan run (quick, pattern-based)\n")
    rf.write("checks: log and csv created\n")
    rf.write("---\n\n")
    rf.write("# Postflight: scan_links\n\n")
    rf.write(f"Log: {LOG}\n")
    rf.write(f"CSV: {CSV}\n")
    rf.write(f"Found: {len(entries)} links\n")

print(f"WROTE {LOG} {CSV} {REC} FOUND={len(entries)}")
