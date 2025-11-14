---
stand: 2025-11-14 20:25
update: Docs sweep: timestamps synchronized; link-scan receipts kept; Checks: full run PASS — receipts: `.tmp-results/reports/checks_report_20251114_162424.md`; Archiv-Integration: `novapolis-dev/docs/archives` → `novapolis-dev/archive/docs_archives_20251114_202548/` (selected items marked done)
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
  - [ ] `tasks.json` Inline-Ketten prüfen → Wrapper-Aufrufe
  - [ ] Wrapper-Probelauf `scripts/run_pytest_coverage.ps1` + Receipt
  - [x] Statusblock „Multi-Root abgeschlossen“ in `WORKSPACE_STATUS.md`
- [x] Dev: Tree-Artefakte regenerieren (R-IDX)
  - Ziel: `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt` neu erzeugen; Status/Datum in `WORKSPACE_STATUS.md` + `novapolis-dev/docs/donelog.md`.
- [x] RP: Frontmatter/Lint Sweep (R-FM/R-LINT)
  - Reihenfolge: Frontmatter → MD003 Setext. Zählwerte vor/nach dokumentieren; PASS loggen.

- [ ] Docs/READMEs: Konsolidierung & Leitlinien (Monorepo)
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

- [ ] Checks-Wrapper (`python scripts/run_checks_and_report.py`) - Review/Nachzug
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
  