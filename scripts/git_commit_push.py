#!/usr/bin/env python3
"""Git commit+push (non-interactive).

Python replacement for scripts/git_commit_push.ps1.

Behavior:
- Prints plan/status
- Aborts with exit code 1 if there are no changes
- Stages all changes (with a dry-run preview)
- Commits with provided message (default matches legacy script)
- Pushes to upstream if present; otherwise sets upstream to origin/HEAD

Usage:
  python scripts/git_commit_push.py [--message "..."]
"""

from __future__ import annotations

import argparse
import subprocess


def run_git(args: list[str], *, label: str | None = None) -> None:
    prefix = f"[{label}] " if label else ""
    print(f"{prefix}git {' '.join(args)}")
    proc = subprocess.run(["git", *args])
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)


def capture_git(args: list[str]) -> str:
    proc = subprocess.run(["git", *args], capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)
    return proc.stdout


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--message", default="", help="Commit message")
    args = ap.parse_args(argv)

    print("Git commit+push (non-interactive) gestartet.")

    run_git(["status", "--short", "--branch"], label="PLAN")

    status_porcelain = capture_git(["status", "--porcelain"]).strip()
    if not status_porcelain:
        print("Keine Änderungen gefunden. Vorgang beendet.")
        return 1

    print()
    run_git(["add", "--all", "--dry-run"], label="DRY RUN")

    print()
    message = args.message.strip() or "chore(rp): database-rp consistency fixes"
    print(f"Commit-Message: {message}")

    run_git(["add", "--all"], label="APPLY")

    # Commit can fail (e.g., hooks, race) - bubble exit code.
    proc_commit = subprocess.run(["git", "commit", "-m", message])
    if proc_commit.returncode != 0:
        print(f"Commit fehlgeschlagen (Exit {proc_commit.returncode}).")
        return int(proc_commit.returncode)

    # Detect upstream
    proc_up = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    has_upstream = proc_up.returncode == 0

    if has_upstream:
        run_git(["push"], label="APPLY")
    else:
        run_git(["push", "-u", "origin", "HEAD"], label="APPLY")

    run_git(["status", "--short", "--branch"], label="VERIFY")

    print("Git commit+push abgeschlossen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
