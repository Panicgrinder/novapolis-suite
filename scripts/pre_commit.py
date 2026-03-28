#!/usr/bin/env python3
"""Composite pre-commit hook (Python).

Replaces the PowerShell-in-sh implementation in githooks/pre-commit.

Behavior:
- If changes touch novapolis_agent/{app,scripts,utils}/..., enforce DONELOG yearly entry
- For staged Markdown files:
    - Run markdownlint-cli2 (npx) with repo config
    - If lint fails: attempt markdownlint-cli2-fix, stage fixed files, then abort
    - Run frontmatter validator (scripts/check_frontmatter.py)
- Run RP hard gates if needed
- Run snapshot gate (scripts/snapshot_gate.py) last, so downstream aborts do not
    consume snapshot freshness unnecessarily

Exit codes:
- 0: allow commit
- 1+: block commit (git will abort)
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def repo_root() -> Path:
    proc = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    if proc.returncode == 0:
        root = proc.stdout.strip()
        if root:
            return Path(root)
    return Path.cwd()


def run(argv: list[str], *, cwd: Path, check: bool = False) -> int:
    proc = subprocess.run(argv, cwd=str(cwd))
    if check and proc.returncode != 0:
        raise SystemExit(proc.returncode)
    return int(proc.returncode)


def capture_lines(argv: list[str], *, cwd: Path) -> list[str]:
    proc = subprocess.run(argv, cwd=str(cwd), capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def python_exe(root: Path) -> str:
    candidates = [
        root / ".venv" / "Scripts" / "python.exe",
        root / ".venv" / "bin" / "python",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return sys.executable


def run_snapshot_gate(root: Path) -> None:
    py = python_exe(root)
    script = root / "scripts" / "snapshot_gate.py"
    if not script.exists():
        print(f"[pre-commit] WARN: snapshot gate fehlt: {script}")
        return
    code = run([py, str(script)], cwd=root)
    if code != 0:
        raise SystemExit(code)


def enforce_agent_donelog_if_needed(root: Path, staged_all: list[str]) -> None:
    needs_donelog = any(
        p.startswith("novapolis_agent/app/")
        or p.startswith("novapolis_agent/scripts/")
        or p.startswith("novapolis_agent/utils/")
        for p in staged_all
    )
    if not needs_donelog:
        return

    done_log_path = root / "novapolis_agent" / "docs" / "DONELOG.txt"
    if not done_log_path.exists():
        print(f"[pre-commit] Erwartete Datei fehlt: {done_log_path}", file=sys.stderr)
        raise SystemExit(1)

    year = datetime.now().strftime("%Y")
    try:
        text = done_log_path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        print(f"[pre-commit] DONELOG nicht lesbar: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    if year not in text:
        print(
            "[pre-commit] DONELOG-Eintrag für dieses Jahr fehlt. Bitte aktualisieren.",
            file=sys.stderr,
        )
        raise SystemExit(1)


def markdownlint(root: Path, staged_md: list[str]) -> None:
    if not staged_md:
        return

    npx = shutil.which("npx")
    if not npx:
        print("[pre-commit] WARN: npx nicht gefunden. Überspringe markdownlint-cli2.")
        return

    config = root / ".markdownlint-cli2.jsonc"
    args = [npx, "--yes", "markdownlint-cli2", "--config", str(config), *staged_md]
    code = run(args, cwd=root)
    if code == 0:
        return

    print(
        "[pre-commit] markdownlint-cli2 meldet Probleme. Versuche automatische Korrektur.",
        file=sys.stderr,
    )

    fix_args = [
        npx,
        "--yes",
        "markdownlint-cli2-fix",
        "--config",
        str(config),
        *staged_md,
    ]
    fix_code = run(fix_args, cwd=root)

    if fix_code == 0:
        run(["git", "add", *staged_md], cwd=root)
        print(
            "[pre-commit] Markdownlint-Fix angewendet. Bitte Änderungen prüfen "
            "und erneut committen.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    print(
        "[pre-commit] markdownlint-cli2 konnte nicht automatisch reparieren. "
        "Bitte manuell beheben.",
        file=sys.stderr,
    )
    raise SystemExit(1)


def frontmatter_check(root: Path, staged_md: list[str]) -> None:
    if not staged_md:
        print("[pre-commit] Keine Markdown-Dateien im Commit. Frontmatter-Check übersprungen.")
        return

    script = root / "scripts" / "check_frontmatter.py"
    if not script.exists():
        print(f"[pre-commit] WARN: Frontmatter-Validator fehlt: {script}")
        return

    py = python_exe(root)
    code = run([py, str(script), *staged_md], cwd=root)
    if code != 0:
        raise SystemExit(code)


def run_rp_hard_gates_if_needed(root: Path, staged_all: list[str]) -> None:
    needs_rp_gate = any(
        p.startswith("novapolis-rp/database-rp/")
        or p.startswith("novapolis-rp/coding/tools/validators/")
        or p == "scripts/checks_rp_consistency.py"
        for p in staged_all
    )
    if not needs_rp_gate:
        return

    py = python_exe(root)
    script = root / "scripts" / "check_rp_hard_gates.py"
    if not script.exists():
        print(f"[pre-commit] WARN: RP-Hard-Gate fehlt: {script}")
        return

    code = run([py, str(script)], cwd=root)
    if code != 0:
        raise SystemExit(code)


def main() -> int:
    root = repo_root()

    staged_all = capture_lines(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMRT"],
        cwd=root,
    )
    if not staged_all:
        return 0

    enforce_agent_donelog_if_needed(root, staged_all)

    staged_md = [p for p in staged_all if p.lower().endswith(".md")]

    # markdownlint gate on staged markdown
    markdownlint(root, staged_md)

    # frontmatter validator (only if markdown files are present)
    frontmatter_check(root, staged_md)

    # RP hard gates for database-rp / validator changes
    run_rp_hard_gates_if_needed(root, staged_all)

    # Snapshot gate last, to avoid freshness churn after downstream aborts/fixes.
    run_snapshot_gate(root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
