---
stand: 2026-02-23 00:04
update: Vollständig erledigten Root-Block archiviert und aktive Root-TODO auf neue Folgeaufgaben vorbereitet.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'todo.root.md' 'novapolis-dev/archive/todo.root.archive.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/archive/todo.dev.archive.md' 'novapolis-dev/docs/todo.index.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 00:00); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'todo.root.md' 'novapolis-dev/archive/todo.root.archive.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/archive/todo.dev.archive.md' 'novapolis-dev/docs/todo.index.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 00:00)
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

- [ ] Tunnel-Check als VS-Code-Task ergänzen (`Checks: sim epoch assets`) und im README kurz dokumentieren.
- [ ] Aktive TODO-Boards (Agent/Sim/RP) auf Prioritätstags `Jetzt/Als naechstes/Später` harmonisieren.
- [ ] Wochenabschluss-Routine standardisieren: Reihenfolge und Artefaktablage für Tests/Checks/Status-Update verbindlich notieren.

Hinweise
--------

- Abgeschlossene oder historisierte Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei jeder Mutation TODO/DONELOG/WORKSPACE_STATUS synchron halten.



