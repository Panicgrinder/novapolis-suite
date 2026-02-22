---
stand: 2026-02-22 17:31
update: Portabilitätscheck eingerichtet (`scripts/check_portable_paths.py`) und initiale Findings im aktiven Scope bereinigt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/architecture-summary-local-ai.md' 'novapolis-dev/docs/process/rp-canvas-rescue/dedupe-chat-export.md' 'novapolis-dev/docs/process/rp-canvas-rescue/generated-artifacts.md' 'todo.root.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 17:10); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/architecture-summary-local-ai.md' 'novapolis-dev/docs/process/rp-canvas-rescue/dedupe-chat-export.md' 'novapolis-dev/docs/process/rp-canvas-rescue/generated-artifacts.md' 'todo.root.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 17:10); .\.venv\Scripts\python.exe scripts\check_portable_paths.py --repo-root . PASS (2026-02-22 17:10)
---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Vorheriger Vollinhalt wurde archiviert unter `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md`.
- Historische Sammelbasis: `novapolis-dev/archive/todo.root.archive.md`.
- Diese Datei ist jetzt die aktive Arbeitsliste fuer neue Punkte.
- README-Pruefpunkt (73/73) wurde nach finalem Doppelcheck archiviert: `novapolis-dev/archive/todo.root.archive.md` (Abschnitt "README-Gesamtlauf (73/73) - abgeschlossen").

Neue Punkte (Backlog)
---------------------

- [ ] Leere Dateien/Ordner im Root-Bereich inventarisieren und nach Freigabe in `novapolis-dev/archive/quarantine/` archivieren (erst `--whatif`/Dry-Run, dann Apply).
- [ ] Woechentlichen Root-Qualitaetslauf fest einplanen und dokumentieren (`Checks: full` + Coverage + Markdownlint + Frontmatter).
- [ ] Root-Backlog auf Top-3 aktive Querschnittspunkte konkretisieren (je 1 Fokus fuer Agent/RP/Dev mit klarer Abschlussbedingung).
- [ ] CI-Doku-Gates im Root pruefen und entscheiden, ob Markdownlint/Frontmatter auch fuer Branch-Pushes ohne PR laufen sollen.

Hinweise
--------

- Abgeschlossene oder historisierte Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei jeder Mutation TODO/DONELOG/WORKSPACE_STATUS synchron halten.



