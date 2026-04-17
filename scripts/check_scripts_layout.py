#!/usr/bin/env python
"""Drift-Check: Skript-Layout.

Ziel (Cleanup TODO v2 / Priorität 1): Neue Python-Skripte sollen nicht „wild" im Repo entstehen.
Stattdessen sollen neue CLIs/Wrapper im Root unter `scripts/` (insb. `scripts/agent/`) landen.

Dieser Check betrachtet *nur neu hinzugefügte oder umbenannte* Python-Dateien (`.py`) im Git-Diff
(standardmäßig staged, also pre-commit-freundlich).

Exitcodes:
- 0: OK
- 2: Verletzung gefunden
- 3: Git nicht verfügbar oder Diff nicht lesbar (konservativ: OK)
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ChangedPath:
    status: str
    path: str


def _run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(REPO_ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def _parse_name_status(output: str) -> list[ChangedPath]:
    items: list[ChangedPath] = []
    for raw_line in output.splitlines():
        line = raw_line.strip("\n\r")
        if not line:
            continue

        # Formats:
        #   A\tpath
        #   R100\told\tnew
        parts = line.split("\t")
        if not parts:
            continue

        status = parts[0]
        if status.startswith("R") and len(parts) >= 3:
            items.append(ChangedPath(status="R", path=parts[2]))
        elif status in {"A", "M", "D"} and len(parts) >= 2:
            items.append(ChangedPath(status=status, path=parts[1]))
        elif status and len(parts) >= 2:
            items.append(ChangedPath(status=status, path=parts[-1]))

    return items


def _is_python(path: str) -> bool:
    return path.lower().endswith(".py")


def _is_allowed_new_script(path: str) -> bool:
    # Hauptregel: Neue Skripte nur im Root-`scripts/`.
    if path.startswith("scripts/"):
        return True

    # Übergangsausnahme: Kompatibilitätspaket gegen `scripts`-Namenskollision.
    # Diese Liste ist absichtlich eng, damit hier keine neuen Dateien „einsickern".
    allowed_compat = {
        "novapolis_agent/scripts/agent/__init__.py",
        "novapolis_agent/scripts/agent/_proxy.py",
        "novapolis_agent/scripts/agent/export_finetune.py",
        "novapolis_agent/scripts/agent/fine_tune_pipeline.py",
        "novapolis_agent/scripts/agent/run_eval.py",
        "novapolis_agent/scripts/agent/quick_eval.py",
        "novapolis_agent/scripts/agent/prepare_finetune_pack.py",
        "novapolis_agent/scripts/agent/dependency_check.py",
        "novapolis_agent/scripts/agent/estimate_tokens.py",
        "novapolis_agent/scripts/agent/map_reduce_summary_llm.py",
        "novapolis_agent/scripts/agent/migrate_dataset_schemas.py",
        "novapolis_agent/scripts/agent/rerun_failed.py",
        "novapolis_agent/scripts/agent/rerun_from_results.py",
        "novapolis_agent/scripts/agent/train_lora.py",
    }
    if path in allowed_compat:
        return True

    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check: neue Python-Skripte nur unter scripts/")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--staged",
        action="store_true",
        help="Prüft staged Änderungen (Default; pre-commit).",
    )
    mode.add_argument(
        "--base",
        metavar="REV",
        help="Prüft Added/Renamed zwischen REV...HEAD (CI/PR-Mode).",
    )
    args = parser.parse_args(argv)

    if args.base:
        proc = _run_git(["diff", "--name-status", "--diff-filter=AR", f"{args.base}...HEAD"])
    else:
        proc = _run_git(["diff", "--cached", "--name-status", "--diff-filter=AR"])

    if proc.returncode != 0:
        # Konservativ: nicht blocken, wenn Git nicht verfügbar ist.
        print(proc.stdout)
        return 3

    changed = _parse_name_status(proc.stdout)
    new_py = [c.path for c in changed if c.status in {"A", "R"} and _is_python(c.path)]

    offenders = [p for p in new_py if not _is_allowed_new_script(p)]
    if not offenders:
        return 0

    print("STOP: Neue Python-Skripte außerhalb `scripts/` gefunden:", file=sys.stderr)
    for p in sorted(offenders):
        print(f"- {p}", file=sys.stderr)

    print(
        "\nBitte neue CLIs/Wrapper unter `scripts/` (i.d.R. `scripts/agent/`) anlegen ",
        "oder (falls zwingend) die Ausnahme explizit im Check begründen/erweitern.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
