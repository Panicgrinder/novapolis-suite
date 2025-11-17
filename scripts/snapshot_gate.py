#!/usr/bin/env python3
"""
Snapshot gate (Python port)

Portiert das Verhalten von `scripts/snapshot_gate.ps1`.
Prüft bei gestagten Markdown-Dateien, ob die Frontmatter-`stand:`-Timestamp frisch ist
und ob eine `.snapshot.now` Lock-Datei vorhanden und aktuell ist.

Exit-Code 0 = PASS, 1 = FAIL
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

TOLERANCE_MINUTES = 5


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
    )


def get_repo_root() -> Path:
    try:
        r = run(["git", "rev-parse", "--show-toplevel"])
        if r.returncode == 0 and r.stdout.strip():
            return Path(r.stdout.strip())
    except Exception:
        pass
    return Path.cwd()


def now_ts() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def read_snapshot_lock(root: Path) -> str | None:
    p = root / ".snapshot.now"
    if not p.exists():
        return None
    try:
        return p.read_text(encoding="utf-8").strip()
    except Exception:
        return None


def get_staged_files() -> list[str]:
    r = run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMRT"])
    if r.returncode != 0:
        return []
    return [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]


def get_staged_content(path: str) -> str | None:
    r = run(["git", "show", f":{path}"])
    if r.returncode != 0:
        return None
    return r.stdout


def find_stand_timestamp(content: str) -> str | None:
    lines = content.splitlines()
    limit = min(len(lines), 40)
    for i in range(limit):
        m = re.match(r"^\s*stand:\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\s*$", lines[i])
        if m:
            return m.group(1)
    return None


def is_stand_changed_in_diff(path: str) -> bool:
    r = run(["git", "diff", "--cached", "-U0", "--", path])
    if r.returncode != 0:
        return False
    for ln in r.stdout.splitlines():
        if ln.startswith("+") and re.search(r"\bstand:\s*\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}", ln):
            return True
    return False


def minutes_diff(a: str, b: str) -> float | None:
    fmt = "%Y-%m-%d %H:%M"
    try:
        da = datetime.strptime(a, fmt)
        db = datetime.strptime(b, fmt)
        return abs((da - db).total_seconds()) / 60.0
    except Exception:
        return None


def test_timestamp_fresh(stand: str, now: str, tol_min: int) -> bool:
    d = minutes_diff(stand, now)
    if d is None:
        return False
    return d <= tol_min


def main() -> int:
    # Bypass
    if os.environ.get("SNAPSHOT_GATE_BYPASS") == "1":
        print("[snapshot-gate] BYPASS set. Skipping checks.")
        return 0

    root = get_repo_root()
    os.chdir(root)

    # Only run in git repo
    if run(["git", "rev-parse", "--is-inside-work-tree"]).returncode != 0:
        print("[snapshot-gate] Not a git repo. Skipping.")
        return 0

    current = now_ts()
    lock = read_snapshot_lock(root)

    staged = get_staged_files()
    md_files = [f for f in staged if f.lower().endswith(".md")]
    if not md_files:
        return 0

    failed = []
    for f in md_files:
        content = get_staged_content(f)
        if not content:
            continue
        stand_ts = find_stand_timestamp(content)
        if not stand_ts:
            continue

        if not is_stand_changed_in_diff(f):
            continue

        ok_now = test_timestamp_fresh(stand_ts, current, TOLERANCE_MINUTES)
        ok_lock = False
        if lock:
            ok_lock_now = test_timestamp_fresh(lock, current, TOLERANCE_MINUTES)
            ok_lock_stand = test_timestamp_fresh(lock, stand_ts, 2)
            ok_lock = ok_lock_now and ok_lock_stand

        if not (ok_now and ok_lock):
            failed.append({"file": f, "stand": stand_ts, "now": current, "lock": lock})

    if failed:
        print("[snapshot-gate] FAIL: Snapshot-Anforderung nicht erfüllt in folgenden Dateien:")
        for x in failed:
            lock_val = x.get("lock") or "<none>"
            print(f" - {x['file']}: stand={x['stand']} | now={x['now']} | lock={lock_val}")
        print()
        print("Bitte VOR dem Edit/Commit die Systemzeit abrufen und Lock setzen:")
        print(
            '  cd "F:/VS Code Workspace/Main"; python -c "from datetime import datetime; '
            'print(datetime.now().strftime("%Y-%m-%d %H:%M"))"'
        )
        print(
            '  cd "F:/VS Code Workspace/Main"; python scripts/snapshot_write_lock.py   # wenn verfügbar'
        )
        print("Danach YAML-Frontmatter 'stand:' aktualisieren und erneut committen.")
        print("Bypass (nicht empfohlen): setx SNAPSHOT_GATE_BYPASS 1 (neues Terminal nötig)")
        return 1

    print(f"[snapshot-gate] PASS: Alle 'stand:'-Timestamps frisch (±{TOLERANCE_MINUTES} min).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
