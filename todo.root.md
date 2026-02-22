---
stand: 2026-02-22 16:51
update: Governance fuer portable Pfade verbindlich ergänzt und aktive Kerndokus von hostgebundenen Absolutpfaden bereinigt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/copilot-instructions.md' 'README.md' 'WORKSPACE_INDEX.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/copilot-vscode-usage.md' 'novapolis-dev/docs/readme_decisions.md' 'todo.root.md' 'DONELOG.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 16:40); .\.venv\Scripts\python.exe scripts\check_frontmatter.py '.github/copilot-instructions.md' 'README.md' 'WORKSPACE_INDEX.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/copilot-vscode-usage.md' 'novapolis-dev/docs/readme_decisions.md' 'todo.root.md' 'DONELOG.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 16:40)
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



