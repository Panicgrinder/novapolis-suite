---
stand: 2025-11-10 06:00
update: Erstfassung bereinigte Aufgabenliste (Root), JSON-Draht für Copilot/GPT
checks: pending
---

Bereinigte Aufgabenliste (Root)
==============================

Hinweis: Temporärer, kuratierter Auszug für operative Arbeit (Copilot/GPT). SSOT bleibt `todo.root.md`. Abweichungen → STOP.

Hoch priorisiert (0–2 Tage)
--------------------------

- [ ] Agent: Tests/Typen/Coverage abschließen (R-COV)
  - Ziel: `pytest -q` PASS, `pyright` PASS, `mypy` PASS, Coverage ≥80% mit Receipt.
  - Schritte: pytest → pyright → mypy → `scripts/run_pytest_coverage.ps1` (Receipt in `DONELOG.md` + `WORKSPACE_STATUS.md`).
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
