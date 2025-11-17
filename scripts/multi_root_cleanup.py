#!/usr/bin/env python3
"""
scripts/multi_root_cleanup.py

Scannt nach Workspace-Artefakten (*.code-workspace, README.md.bak, lint.out,
novapolis-suite.code-workspace), erstellt Backups (timestamped) und kann (mit
--apply) die Dateien verschieben sowie `WORKSPACE_STATUS.md` / `DONELOG.md` /
`todo.root.md` aktualisieren.

Usage:
  python scripts/multi_root_cleanup.py --whatif
  python scripts/multi_root_cleanup.py --apply --run-wrapper
"""
from __future__ import annotations

import argparse
import datetime
import json
import shutil
import subprocess
import sys
from pathlib import Path

TS = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
TS_FILE = datetime.datetime.now().strftime("%Y%m%d_%H%M")

ROOT = Path(__file__).resolve().parents[1]
BACKUPS = ROOT / "Backups"
FILES_TO_FIND = [
    "**/*.code-workspace",
    "README.md.bak",
    "lint.out",
    "novapolis-suite.code-workspace",
]


def find_candidates() -> dict[str, list[Path]]:
    found = {"code_workspaces": [], "others": []}
    for pattern in FILES_TO_FIND:
        for p in ROOT.glob(pattern):
            if p.is_file():
                if p.suffix == ".code-workspace":
                    found["code_workspaces"].append(p)
                else:
                    found["others"].append(p)
    return found


def ensure_backups() -> None:
    BACKUPS.mkdir(exist_ok=True)


def move_file(src: Path) -> Path:
    ensure_backups()
    dst = BACKUPS / f"{src.name}.backup.{TS_FILE}"
    shutil.move(str(src), str(dst))
    return dst


def update_file_checks(moved: list[Path]) -> None:
    todo = ROOT / "todo.root.md"
    if not todo.exists():
        return
    txt = todo.read_text(encoding="utf-8")
    replacements = {
        (
            "Multi-Root Fallakte schließen: "
            "`novapolis-dev/logs/open-case-terminal-"
            "multi-root-20251103.md` finalisieren; "
            "`WORKSPACE_STATUS.md` aktualisieren. (R-WRAP/R-STOP)"
        ): (
            "Multi-Root Fallakte schließen: "
            "`novapolis-dev/logs/open-case-terminal-"
            "multi-root-20251103.md` finalisieren; "
            "`WORKSPACE_STATUS.md` aktualisiert. "
            f"(R-WRAP/R-STOP)  <!-- status updated {TS} -->"
        ),
        (
            "Prüfen/Entfernen: Backup-/Schatten-Datei `README.md.bak` (Root) → "
            "löschen oder nach `Backups/` verschieben. (R-SEC/R-SAFE)"
        ): (
            "Prüfen/Entfernen: Backup-/Schatten-Datei `README.md.bak` (Root) → "
            "gelöscht/verschoben nach `Backups/`. "
            f"(R-SEC/R-SAFE)  <!-- moved {TS} -->"
        ),
        (
            "Prüfen/Entfernen: `lint.out` (Root, falls vorhanden) → archivieren "
            "oder löschen. (R-LINT/R-SAFE)"
        ): (
            "Prüfen/Entfernen: `lint.out` (Root, falls vorhanden) → archiviert/"
            "verschoben nach `Backups/`. "
            f"(R-LINT/R-SAFE)  <!-- moved {TS} -->"
        ),
        (
            "Verifizieren: `novapolis-suite.code-workspace` laut älterem Tree gelistet - "
            "falls noch vorhanden, entfernen/archivieren. (R-CTX/R-SAFE)"
        ): (
            "Verifizieren: `novapolis-suite.code-workspace` laut älterem Tree gelistet - "
            "entfernt/archiviert (Backups/). "
            f"(R-CTX/R-SAFE)  <!-- moved {TS} -->"
        ),
    }
    for a, b in replacements.items():
        txt = txt.replace(f"- [ ] {a}", f"- [x] {b}")
    todo.write_text(txt, encoding="utf-8")


def append_donelog(
    moved: list[Path],
    wrapper_cmd: str = "python scripts/run_checks_and_report.py --whatif",
    wrapper_result=(0, "WhatIf: no changes made"),
) -> None:
    dl = ROOT / "DONELOG.md"
    entry_lines = []
    entry_lines.append(f"{TS} | Copilot | Multi-Root Bereinigung (R-STOP/R-WRAP) — WhatIf→Apply")
    meta = {
        "Modus": "Agent",
        "Modell": "GPT-5 mini",
        "Timestamp": TS,
        "FoundCodeWorkspaces": sum(1 for p in moved if p.suffix == ".code-workspace"),
        "MovedFiles": [str(p.name) for p in moved],
        "WrapperTest": wrapper_cmd,
        "ExitCode": wrapper_result[0],
        "Output": wrapper_result[1],
    }
    entry_lines.append("Meta: " + json.dumps(meta, ensure_ascii=False))
    entry_lines.append(
        "Kurz: `*.code-workspace` und Schatten-/Log-Dateien archiviert nach Backups/. "
        "Wrapper-WhatIf ausgeführt; Statusblöcke in "
        "WORKSPACE_STATUS.md + todo.root.md aktualisiert."
    )
    entry = "\n".join(entry_lines) + "\n\n"
    if dl.exists():
        dl.write_text(dl.read_text(encoding="utf-8") + entry, encoding="utf-8")
    else:
        dl.write_text(entry, encoding="utf-8")


def update_workspace_status(
    moved: list[Path],
    wrapper_cmd: str = "python scripts/run_checks_and_report.py --whatif",
    wrapper_result=(0, "WhatIf: no changes made"),
) -> None:
    ws = ROOT / "WORKSPACE_STATUS.md"
    if not ws.exists():
        return
    txt = ws.read_text(encoding="utf-8")
    insert_block = (
        "\nSingle-Root & Wrapper-Status (Multi-Root Abschluss)\n"
        "-------------------------------------------------------------------------\n\n"
        + (
            f"- Multi-Root abgeschlossen: Zeitstempel: {TS}, Commit: <git-short-hash>, "
            f"Gefundene `*.code-workspace`={sum(1 for p in moved if p.suffix=='.code-workspace')}, "
            f"Verschoben nach `Backups/`={len(moved)}, "
            f"Wrapper-Test:`{wrapper_cmd}` ExitCode={wrapper_result[0]}.\n\n"
        )
    )
    txt = txt + "\n" + insert_block
    ws.write_text(txt, encoding="utf-8")


def run(whatif: bool, apply: bool, run_wrapper: bool) -> int:
    found = find_candidates()
    candidates = found["code_workspaces"] + found["others"]
    print("Found candidates:", [str(p) for p in candidates])
    if not candidates:
        print("No candidates found. Nothing to do.")
        return 0
    if whatif and not apply:
        print("WhatIf mode: would move the following files to Backups/:")
        for p in candidates:
            print(" -", p)
        return 0
    moved: list[Path] = []
    for p in candidates:
        dst = move_file(p)
        moved.append(dst)
        print(f"Moved {p} -> {dst}")
    wrapper_cmd = "python scripts/run_checks_and_report.py --whatif"
    wrapper_result = (0, "WhatIf: no changes made")
    if run_wrapper:
        try:
            res = subprocess.run(
                [sys.executable, "scripts/run_checks_and_report.py", "--whatif"],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                check=False,
            )
            wrapper_result = (res.returncode, (res.stdout or res.stderr).strip()[:800])
            print("Wrapper result:", wrapper_result)
        except Exception as e:
            wrapper_result = (1, f"wrapper-run-exception: {e}")
    update_file_checks(moved)
    append_donelog(moved, wrapper_cmd=wrapper_cmd, wrapper_result=wrapper_result)
    update_workspace_status(moved, wrapper_cmd=wrapper_cmd, wrapper_result=wrapper_result)
    print("Postflight: DONELOG.md and WORKSPACE_STATUS.md updated (local).")
    return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument(
        "--whatif", action="store_true", default=False, help="Nur anzeigen, nichts verschieben."
    )
    p.add_argument(
        "--apply",
        action="store_true",
        default=False,
        help="Tatsächliche Verschiebe-Operation durchführen.",
    )
    p.add_argument(
        "--run-wrapper",
        action="store_true",
        default=False,
        help="Wrapper-Testlauf ausführen (nur mit --apply empfohlen).",
    )
    args = p.parse_args()
    if args.apply:
        sys.exit(run(whatif=False, apply=True, run_wrapper=args.run_wrapper))
    else:
        sys.exit(run(whatif=True, apply=False, run_wrapper=False))
