"""Update frontmatter `stand` and `checks` for files marked ACTIVE in a doc-freshness log.

Usage: python scripts/sync_frontmatter_from_doc_freshness.py \
    .tmp/results/reports/checks_run_*/doc-freshness.log

It will only update files that already contain both `stand:` and `checks:` in their frontmatter.
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: sync_frontmatter_from_doc_freshness.py <doc-freshness.log>")
    sys.exit(2)

log_path = Path(sys.argv[1])
repo_root = Path(__file__).resolve().parent.parent
if not log_path.exists():
    print(f"Log file not found: {log_path}")
    sys.exit(1)

lines = log_path.read_text(encoding="utf-8").splitlines()
active_paths = []
for ln in lines:
    if not ln.startswith("FAIL|"):
        continue
    parts = ln.split("|")
    if len(parts) < 3:
        continue
    rel = parts[1]
    # detect surface=ACTIVE in remainder
    if "surface=ACTIVE" in ln:
        active_paths.append(rel)

if not active_paths:
    print("No ACTIVE paths found in log.")
    sys.exit(0)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
checks_line = "scripts/run_checks_and_report.py auto-sync"

updated = []


def split_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return [], [], lines
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[: idx + 1], lines[idx + 1 :], lines
    return [], [], lines


for rel in active_paths:
    # normalize path
    p = (repo_root / rel).resolve()
    if not p.exists() or not p.is_file():
        print(f"Skip missing: {rel}")
        continue
    raw = p.read_text(encoding="utf-8")
    fm, body, original = split_frontmatter(raw)
    if not fm:
        print(f"Skip (no fm): {rel}")
        continue
    has_stand = any(line.strip().lower().startswith("stand:") for line in fm[1:-1])
    has_checks = any(line.strip().lower().startswith("checks:") for line in fm[1:-1])
    if not (has_stand and has_checks):
        print(f"Skip (fm missing keys): {rel}")
        continue
    new_fm = []
    for line in fm:
        s = line.strip().lower()
        if s.startswith("stand:"):
            new_fm.append(f"stand: {now}")
            continue
        if s.startswith("checks:"):
            new_fm.append(f"checks: {checks_line}")
            continue
        new_fm.append(line)
    new_lines = new_fm + body
    if new_lines == original:
        print(f"Unchanged: {rel}")
        continue
    p.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    updated.append(rel)
    print(f"Updated: {rel}")

print(f"Done. Updated {len(updated)} files.")
