---
stand: 2025-11-14 22:09
update: Inline `-Command` scan performed; Candidate report: `.tmp-results/reports/inline_command_candidates_20251114_2148.md`. Python wrapper prototype `scripts/task_wrappers/run_pytest_coverage.py` added; smoke-run receipt: `.tmp-results/reports/run_pytest_coverage_wrapper_receipt_20251114_2209.md`. Original PS1 archived to `novapolis-dev/archive/scripts_archives_20251114_2155/run_pytest_coverage.ps1` with archive receipt `.tmp-results/reports/run_pytest_coverage_ps1_archive_receipt_20251114_2209.md`.
checks: PASS
---

Bereinigte Aufgabenliste (Root)
==============================

Hinweis: Temporärer, kuratierter Auszug für operative Arbeit (Copilot/GPT). SSOT bleibt `todo.root.md`. Abweichungen → STOP.

Hoch priorisiert (0-2 Tage)
--------------------------

- Ziel: `pytest -q` PASS, `pyright` PASS, `mypy` PASS, Coverage ≥80% mit Receipt.
- Schritte: pytest → pyright → mypy → `scripts/run_pytest_coverage.ps1` (Receipt in `DONELOG.md` + `WORKSPACE_STATUS.md`).
- [x] Agent: Integration `PSScriptAnalyzer` in der damaligen PowerShell-Variante (jetzt durch `python scripts/run_checks_and_report.py` ersetzt) (2025-11-11 11:00)
- [x] `*.code-workspace` suchen und entfernen/verschieben (report counts)
- [x] `tasks.json` Inline-Ketten geprüft → auf Python-Wrapper umgestellt
- [x] Wrapper-Probelauf `scripts/run_pytest_coverage.ps1` + Receipt `.tmp-results/reports/checks_report_20251114_2112.md` (2025-11-14 21:12)
- [x] Wrapper-Probelauf `python scripts/run_checks_and_report.py` + Receipt (`.tmp-results/reports/checks_report_20251114_203601.md`) (2025-11-14 20:36)
- [x] Statusblock „Multi-Root abgeschlossen“ in `WORKSPACE_STATUS.md`
- [x] Dev: Tree-Artefakte regenerieren (R-IDX)
  - Ziel: `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt` neu erzeugen; Status/Datum in `WORKSPACE_STATUS.md` + `novapolis-dev/docs/donelog.md`.
- [x] RP: Frontmatter/Lint Sweep (R-FM/R-LINT)
  - Reihenfolge: Frontmatter → MD003 Setext. Zählwerte vor/nach dokumentieren; PASS loggen.

- [x] Docs/READMEs: Konsolidierung & Leitlinien (Monorepo)
  - [x] Kandidatenliste erstellt: `.tmp-results/reports/links/candidates_app-routers-README.md_20251111_2340.md` (22 reale README.md-Dateien)
  - [x] Ein-Satz-Summaries für 22 README.md erzeugen (`.tmp-results/reports/links/readme_summaries.md`)
  - [x] Stubs vs. zentrale Doku definieren (Hub erstellt, Stubs Phase 1 umgesetzt)
  - [x] Redirect-/Index-Strategie festlegen (`WORKSPACE_INDEX.md` vereinheitlichen / ggf. ersetzen durch Hub-Verweis)
  - [x] Entscheidungsliste: Welche Kern-READMEs verschlankt werden (PR-Plan)
  - [x] Hub-README erweitert (TL;DR, Links, Beispiele, Governance-Querverweise)

- [x] Link-Scanner (`scripts/scan_links.ps1`) - Nacharbeiten
  - [x] AutoFix + Backups implementiert; defekte Links 10 → 3 reduziert (Reports unter `.tmp-results/reports/scan_links_reports/`)
  - [x] Report-Verzeichnis umbenannt → `.tmp-results/reports/scan_links_reports`
  - [x] Backup-Pfad zentralisiert → `.tmp-datasets/lscan_links_backups`
  - [x] Bei Mehrdeutigkeit Kandidatenliste im Dry-Run mitschreiben (JSON erzeugt)
  - [x] Rescan nach Fix (0 broken) Receipt vorhanden `link_report_novapolis_agent_20251112_033438.md`
  - [x] Backups (*.bak.linkscan) geprüft (`.tmp-datasets/lscan_links_backups/`)
  - [x] Automatisches Schreiben der Kandidaten-JSON im Dry-Run (Implementierung)
  - [x] Report-Summary in Hub unter "Temporäre Bereiche" verlinken (nach Automation)

- [x] Checks-Wrapper (`python scripts/run_checks_and_report.py`) - Review/Nachzug
  - [x] Kurzreview der neuen PSScriptAnalyzer-Phase (Installationspfad, Exit-Codes, Receipt-Felder)
  - [x] Einbindung in „Checks: full“ Dokumentation (README/Status) (2025-11-14 16:55) — siehe `novapolis-dev/docs/checks_full.md`
  - [x] Einmaliger Gesamtlauf inkl. Receipt unter `.tmp-results/reports/checks_report_*.md`

Kurzfristig (3-7 Tage)
----------------------

- [ ] RP: Export `99-exports/chat-export-complete.txt` konsolidieren (Scope/Schema definieren)
- [ ] RP: Tagging-Pipeline 015-010 von Dry-Run auf Write heben (STOP vor Write)
- [ ] Dev/RP: Staging-Reports migrieren oder Frontmatter/Setext nachziehen (einen Task führen; Doppelungen vermeiden)
- [ ] Dev: `README.md.bak` behandeln (verschieben nach `Backups/` oder löschen)
- [ ] Dev: Abschnitt „Editor-Setup“ im Root-`README.md`
- [ ] Sim: Godot headless Lade-Check (`novapolis-sim/project.godot`) und Kurzprotokoll

Sofort-Themen (READMEs/Links/Index)
-----------------------------------

- [x] Entfernte Index-Datei: Links-Anpassungen nun direkt in verbleibenden READMEs geprüft (Agent WORKSPACE_INDEX entfernt)
- [x] Ambiguität „matches=53“: Kandidatenliste JSON erzeugt
  - Datei: `.tmp-results/reports/links/candidates_app-routers-README.json`
  - Nächster Schritt: Scanner erweitern (Auto-Ausgabe JSON bei Dry-Run)
- [x] Doppelte/parallel existierende Index-Dateien entfernt (`novapolis_agent/WORKSPACE_INDEX.md`, Backup `.bak.linkscan`)

Lokale AI - Startpfad (organisch)
---------------------------------

- [ ] Schattenmodus-Logging mit Redaction aktivieren (operativ)
- [ ] 10-20 Kern-Dokumente indexieren (RAG-Minimum)
- [ ] Wöchentlichen Review-Slot (30-45 min) einplanen

Hinweise
--------

- STOP-Marker: Tagging-Write, Cleanup Phase 4, Multi-Root-Abschluss.
- SSOT: Detailkontext und Volltextliste in `todo.root.md`; diese Datei dient als Arbeitsfahrplan für Copilot/GPT.
- 2025-11-10 20:17: WORKSPACE_INDEX Header-Duplikate und SimClient Variable gefixt (Commit 5922521). `run_pytest_quick.ps1` PASS.
- Wrapper-Aufgaben: `python scripts/run_checks_and_report.py` (Lint/Typen/Tests + Report) finalisieren; Link-Scanner `scripts/scan_links.ps1` implementieren und Reports unter `.tmp-results/scan/` ablegen.
  - Hub-README: Erweiterung abgeschlossen (01:12); nächste Phase Index/Redirect-Strategie.

PowerShell-Skripte im Workspace
-------------------------------

Die folgenden PowerShell-Skripte wurden im Workspace rekursiv gefunden. Pfade relativ zum Repo-Root:

- `scripts/verify_sim.ps1`
- `scripts/update_workspace_tree_dirs.ps1`
- `scripts/update_backups_manifest.ps1`
- `scripts/tests_pytest_root.ps1`
- `scripts/snapshot_write_lock.ps1`
- `scripts/snapshot_gate.ps1`
- `scripts/setup_root_venv.ps1`
- `scripts/scan_links.ps1`
- `scripts/run_sim_headless.ps1`
- `scripts/run_pytest_quick.ps1`
- `scripts/run_pytest_coverage.ps1`
- `scripts/run_linters.ps1`
- `scripts/run_frontmatter_validator.ps1`
- `scripts/rotate_backups.ps1`
- `scripts/install_hooks.ps1`
- `scripts/git_commit_push.ps1`
- `scripts/diagnostics.ps1`
- `scripts/collect_commit_times_batch1.ps1`
- `scripts/cleanup_workspace_files.ps1`
- `scripts/checks_types.ps1`
- `scripts/checks_linters.ps1`
- `scripts/append_done_and_push.ps1`
- `novapolis-dev/archive/scripts/snapshot_write_lock.ps1`
- `novapolis-dev/archive/scripts/snapshot_gate.ps1`
- `novapolis_agent/scripts/cleanup_phase4.ps1`
- `novapolis_agent/scripts/cleanup_phase3.ps1`
- `novapolis_agent/scripts/history_purge_plan.ps1`
- `novapolis-rp/coding/tools/validators/run_check_names.ps1`
- `novapolis-rp/coding/tools/diagnostics/systemcheck.ps1`
- `novapolis-rp/coding/tools/validators/run_validate_all.ps1`
- `novapolis-rp/coding/tools/diagnostics/with_lock.ps1`
- `novapolis-rp/coding/tools/curation/build-staging-reports.ps1`

Hinweis: Einige Skripte sind Archiv-Kopien unter `novapolis-dev/archive/` oder legacy-Skripte in `novapolis_agent/scripts/` — bitte bei Cleanup-Aktionen die Archiv-Policy beachten (keine Löschungen ohne Archiv-Receipt & Freigabe).

Archivierte `checks_run_*`-Ordner
-------------------------------

Die im Verzeichnis `.tmp-results/reports/` gefundenen `checks_run_*`-Ordner wurden in das Archiv `novapolis-dev/archive/docs_archives_20251114_202548/old_tmp_reports/` verschoben (inkl. `checks_run_20251114_203601`).

Audit-Receipt: `novapolis-dev/archive/docs_archives_20251114_202548/archived_checks_before_20251114_162424.md` sowie `.tmp-results/reports/checks_wrapper_run_receipt.txt` und die generierten Reports `.tmp-results/reports/checks_report_20251114_203601.*` behalten die vollständigen Laufdetails.
  