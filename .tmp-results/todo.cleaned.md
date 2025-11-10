---
stand: 2025-11-10 22:01
update: Status nach Workspace-Audit & Tests ergänzt; Wrapper/Scanner-Aufgaben verlinkt
checks: markdownlint pending, Tests run_pytest_quick.ps1 PASS (2025-11-10)
---

Bereinigte Aufgabenliste (Root)
==============================

Hinweis: Temporärer, kuratierter Auszug für operative Arbeit (Copilot/GPT). SSOT bleibt `todo.root.md`. Abweichungen → STOP.

Hoch priorisiert (0–2 Tage)
--------------------------

- [ ] Agent: Tests/Typen/Coverage abschließen (R-COV)
  - Ziel: `pytest -q` PASS, `pyright` PASS, `mypy` PASS, Coverage ≥80% mit Receipt.
  - Schritte: pytest → pyright → mypy → `scripts/run_pytest_coverage.ps1` (Receipt in `DONELOG.md` + `WORKSPACE_STATUS.md`).
 - [x] Agent: Korrektur `scripts/run_checks_and_report.ps1` - STOP-Fall bei zu vielen Testdateien muss als FAIL ausgewiesen werden. (2025-11-11 00:23)
- [ ] Dev: Multi-Root bereinigen (R-STOP/R-WRAP)
  - [ ] `*.code-workspace` suchen und entfernen/verschieben (report counts)
  - [ ] `tasks.json` Inline-Ketten prüfen → Wrapper-Aufrufe
  - [ ] Wrapper-Probelauf `scripts/run_pytest_coverage.ps1` + Receipt
  - [ ] Statusblock „Multi-Root abgeschlossen“ in `WORKSPACE_STATUS.md`
- [ ] Dev: Tree-Artefakte regenerieren (R-IDX)
  - Ziel: `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt` neu erzeugen; Status/Datum in `WORKSPACE_STATUS.md` + `novapolis-dev/docs/donelog.md`.
- [ ] RP: Frontmatter/Lint Sweep (R-FM/R-LINT)
  - Reihenfolge: Frontmatter → MD003 Setext. Zählwerte vor/nach dokumentieren; PASS loggen.

Kurzfristig (3–7 Tage)
----------------------

- [ ] RP: Export `99-exports/chat-export-complete.txt` konsolidieren (Scope/Schema definieren)
- [ ] RP: Tagging-Pipeline 015–010 von Dry-Run auf Write heben (STOP vor Write)
- [ ] Dev/RP: Staging-Reports migrieren oder Frontmatter/Setext nachziehen (einen Task führen; Doppelungen vermeiden)
- [ ] Dev: `README.md.bak` behandeln (verschieben nach `Backups/` oder löschen)
- [ ] Dev: Abschnitt „Editor-Setup“ im Root-`README.md`
- [ ] Sim: Godot headless Lade-Check (`novapolis-sim/project.godot`) und Kurzprotokoll

Lokale AI – Startpfad (organisch)
---------------------------------

- [ ] Schattenmodus-Logging mit Redaction aktivieren (operativ)
- [ ] 10–20 Kern-Dokumente indexieren (RAG-Minimum)
- [ ] Wöchentlichen Review-Slot (30–45 min) einplanen

Hinweise
--------

- STOP-Marker: Tagging-Write, Cleanup Phase 4, Multi-Root-Abschluss.
- SSOT: Detailkontext und Volltextliste in `todo.root.md`; diese Datei dient als Arbeitsfahrplan für Copilot/GPT.
- 2025-11-10 20:17: WORKSPACE_INDEX Header-Duplikate und SimClient Variable gefixt (Commit 5922521). `run_pytest_quick.ps1` PASS.
- Wrapper-Aufgaben: `scripts/run_checks_and_report.ps1` (Lint/Typen/Tests + Report) finalisieren; Link-Scanner `scripts/scan_links.ps1` implementieren und Reports unter `.tmp-results/scan/` ablegen.
