---
stand: 2026-02-20 00:57
update: Inhalt aus .tmp-results/sorted_DONELOG.txt (Postflight-Block) einsortiert.
checks: source_split_by_marker DONELOG-Abschnitt
---

---
stand: 2025-11-12 01:38
update: Postflight (Checks-Report 20251112_013920 protokolliert)
checks: markdownlint-cli2 PASS (scoped)


Postflight
----------
Meta: Modus=Postflight, Modell=GPT-5, Arbeitsverzeichnis=F:\VS Code Workspace\Main, RepoRoot=F:\VS Code Workspace\Main, PSScriptRoot=F:\VS Code Workspace\Main\scripts, PSVersion=7.5.4, Aufruf=python F:\VS Code Workspace\Main\scripts\run_checks_and_report.py, SHA256=65570151AA983A6A3784D89B589486A214B8A171D1BA22766C1BF17C49F54E30, STOP-Gate=aktiv, Wrapper-Policy=erfüllt, Quellen=F:\VS Code Workspace\Main\.github\copilot-instructions.md;F:\VS Code Workspace\Main\novapolis_agent\docs\DONELOG.txt;F:\VS Code Workspace\Main\scripts\run_checks_and_report.py, Aktion=Automatisierter Checklauf Backend-relevant (PowerShell-Variante archiviert)
Prüfung: ruff=FAIL, black=FAIL, markdownlint=FAIL, frontmatter=FAIL, pyright=FAIL, mypy=FAIL, pytest=STOP (>40 Testdateien), coverage=SKIP (STOP), PSScriptAnalyzerExit=1
Regeln: IDs=R-WRAP,R-STOP,R-FM,R-LINT,R-CTX,R-SEC,R-LOG,R-COV,R-TIME,R-SAFE
Todos: offen=n/a, BeispielFix=Baseline-Report erfasst, ReRun=geplant nach Lint/Typ-Fixes, Fällig=2025-11-12 01:45
- Pfad-Updates Scanner
  - Reports: `.tmp-results/reports/scan_links_reports` (vorher `.../reports/links`)
  - Backups: `.tmp-datasets/lscan_links_backups` (zentral, timestamped Dateien)
- Test: `scripts/scan_links.ps1` ohne AutoFix ausgeführt → Report `link_report_novapolis_agent_YYYYMMDD_HHMMSS.md` erstellt.
- Nächste Schritte: die 1 verbleibende Referenz „mehrere Versionen. (Prüfen“ im `WORKSPACE_INDEX.md` auflösen; danach Rescan + Receipt.

<!-- frühere Frontmatter (2025-11-10 11:35) inhaltlich erhalten, nur nicht mehr als YAML-Block -->

