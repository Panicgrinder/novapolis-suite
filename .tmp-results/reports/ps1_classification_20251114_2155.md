---
stand: 2025-11-14 21:55
update: Repo-wide inventory and prioritization of `*.ps1` scripts for planned migration to Python wrappers. This is an analytic report and plan seed.
checks: n/a
---

PS1 Inventory & Conversion Plan (Übersicht)
===========================================

Kurz: Diese Datei listet gefundene `*.ps1`-Skripte, gruppiert sie nach Wichtigkeit (High/Medium/Low/Special), und beschreibt einen sicheren, schrittweisen Plan zur Migration zu Python-Wrappern sowie zur „Verkabelung" (Tasks, Hooks, CI). Alle Änderungen erfolgen nur nach expliziter Bestätigung (STOP-Gate).

Datum: 2025-11-14 21:55

High Priority (Aktiv, produktive Wrapper / Tasks / Hooks)
---------------------------------------------------------
Diese Dateien werden aktiv in Tasks/CI/Workflows oder als Git-Hooks genutzt. Ziel: zuerst diese zu migriren, weil sie das größte Risiko für Quoting/Platform-Probleme bergen.

- `scripts/run_pytest_coverage.ps1`  
- `scripts/run_pytest_quick.ps1`  
- `scripts/setup_root_venv.ps1`  
- `scripts/install_hooks.ps1`  
- `scripts/git_commit_push.ps1`  
- `githooks/pre-commit` (calls `scripts/snapshot_gate.ps1`)  

Empfehlung: 1) Implementiere Python-equivalente wrappers unter `scripts/task_wrappers/` (z. B. `run_pytest_coverage.py`) die dieselbe CLI (args) und Exitcodes liefern; 2) Aktualisiere Tasks / Hooks so dass sie `python .venv\Scripts\python.exe scripts/task_wrappers/<name>.py` aufrufen; 3) Stelle receipts/sha256 und Postflight-Block pro Run sicher.

Medium Priority (Hilfs-/Diagnose-/Maintenance-Skripte)
------------------------------------------------------
Diese werden gelegentlich manuell oder in Archiv-/CI‑Jobs ausgeführt.

- `scripts/scan_links.ps1`  
- `scripts/update_workspace_tree_dirs.ps1`  
- `scripts/update_backups_manifest.ps1`  
- `scripts/rotate_backups.ps1`  
- `scripts/collect_commit_times_batch1.ps1`  
- `scripts/diagnostics.ps1`  
- `scripts/cleanup_workspace_files.ps1`  
- `scripts/run_linters.ps1`  
- `scripts/run_frontmatter_validator.ps1`  
- `scripts/tests_pytest_root.ps1`  

Empfehlung: Priorisiere `run_frontmatter_validator` und `run_linters` direkt nach High. Manche Utilities (update_backups_manifest, diagnostics) können sinnvoll in Python neuimplementiert werden oder zu small shim-wrappers reduziert werden.

Low Priority (Archiv / Legacy / Backups)
---------------------------------------
Viele `*.ps1`-Matches kommen aus Backups, `novapolis-dev/archive/` oder sind historisch dokumentiert.

- `novapolis-dev/archive/scripts/snapshot_write_lock.ps1`  
- `novapolis-dev/archive/scripts/snapshot_gate.ps1`  
- `Backups/tasks.json.bak` (historische `-Command` entries)  
- `novapolis_agent/scripts/cleanup_phase3.ps1` (legacy; note: some were marked removed in DONELOG)  
- `novapolis_agent/scripts/cleanup_phase4.ps1` (legacy)  
- `novapolis_agent/scripts/history_purge_plan.ps1` (legacy)  

Empfehlung: Diese behalten wir als Archiv. Bei Bedarf: 1) dokumentieren, 2) verschieben nach `novapolis-dev/archive/` falls nicht schon dort, 3) keine automatische Konvertierung ohne Review.

Special / Proxy / Wrapper-like (Audit required)
------------------------------------------------
- `novapolis-rp/coding/tools/diagnostics/with_lock.ps1` — Proxy that runs `-Command` or `-ScriptFile` arguments. Vorerst behalten, ggf. ersetzen durch a) small Python proxy that safely shells or b) explicit whitelisting.
- `scripts/snapshot_write_lock.ps1` + `scripts/snapshot_gate.ps1` — small helpers writing timestamps; could be ported to Python easily.

Strategie & Safety Rules (Regelwerk-konform)
--------------------------------------------
- STOP-Gate: Keine produktiven Änderungen (ersetzende Commits) ohne deine Bestätigung. Diese Datei ist lediglich der Plan/Inventory.
- Wrapper-Policy: Mehrschrittige Abläufe implementieren als eigenständige Skripte und aufrufbar via `pwsh -File` oder `python -m scripts.task_wrappers.<name>`; wir bevorzugen Python-only wrappers per Anforderung.
- Receipts: Jeder konvertierte Skript-Run benötigt eine `.tmp-results/reports/<name>_receipt_<YYYYMMDD_HHMM>.md` mit SHA256 (neue Python file), Aufruf, Exitcodes und Postflight-Meta (R-WRAP,R-STOP etc.).
- Tests: Nach Migration: Lint (ruff), Typen (pyright/mypy), Tests (pytest) runnen; Coverage-Gate berücksichtigen.
- Backups & Audit: Vor Löschen/Entfernen: Archiv-Receipt anlegen (novapolis-dev/archive/...) mit SHA256 und Verweis.

Conversion Template (Python wrapper minimal pattern)
---------------------------------------------------
Empfehlung: `scripts/task_wrappers/<name>.py`

- Nutzung: `.\.venv\Scripts\python.exe scripts\task_wrappers\run_pytest_coverage.py --dry-run` oder `-m` style.
- Exitcodes: 0 success, non-zero propagate underlying tool exitcode.
- Logging: write to stdout + `logging` module; write receipt to `.tmp-results/reports/` on completion.

Minimalbeispiel (concept):

```python
#!/usr/bin/env python3
import sys, subprocess, hashlib, pathlib, datetime

def main(argv):
    # map args, set cwd, run underlying commands
    code = subprocess.call([sys.executable, "-m", "pytest", "--cov", "--cov-fail-under=80"]) 
    # write simple receipt
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    receipt = pathlib.Path('.tmp-results/reports') / f'receipt_run_pytest_coverage_{now.replace(':','')}.md'
    receipt.write_text(f"stand: {now}\nexit: {code}\n")
    return code

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
```

Workplan (Sequenziell, sichere Schritte)
---------------------------------------
1) Review & Inventory (done): erzeugte diese Datei.
2) Priorisierungs-Review mit dir (hier kurz bestätigen High/Medium/Low lists).
3) For each High-priority script: create a Python wrapper prototype under `scripts/task_wrappers/` and a unit smoke-run locally (no commit) — produce receipt.
4) Update callsites: `.vscode/tasks.json`, `githooks/pre-commit`, CI workflows to call the Python wrapper via the workspace venv python. Use absolute venv path in docs and tasks templates.
5) Run checks (lint/pyright/pytest) and iterate fixes.
6) Once validated, commit each script migration as a small PR with receipts and DONELOG entry; move original `.ps1` to `novapolis-dev/archive/scripts/` (with archive receipt) rather than immediate deletion.
7) After all callsites updated and PR merged, optionally remove `.ps1` files from repo (final archival step, separate PR).

Deliverables I will produce if du zustimmst
------------------------------------------
- A concrete PR-ready patch for `githooks/pre-commit` extraction → `scripts/hooks/pre-commit.py` (or `.ps1`->`.py` wrapper) including smoke test commands and receipt templates.
- A set of Python wrapper prototypes for the 2–3 top priority scripts (e.g. `run_pytest_coverage`, `setup_root_venv`, `git_commit_push`) plus sample `.vscode/tasks.json` snippets.
- Receipts and WORKSPACE_STATUS / TODO updates per conversion.

Nächste Schritte (Vorschlag)
---------------------------
- Bitte bestätige: Ich starte mit der Migration der High-Priority-Skripte (konkret starten mit `scripts/run_pytest_coverage.ps1` → `scripts/task_wrappers/run_pytest_coverage.py`) und erstelle eine PR-ready Änderung (STOP vor dem Commit).  
- Oder: Ich erzeuge zuerst alle Python-Prototypen lokal und führe smoke-runs ohne Commit, sammle Receipts und bringe die Änderungen in einem einzelnen PR-Batch.

---
Report Ende.
