---
stand: 2026-02-23 09:19
update: Root-Punkte 1-3 umgesetzt (Sim-Task + Board-Prioritaetstags + Wochenabschluss-Routine).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'README.md' 'todo.root.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' PASS (2026-02-23 08:39); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'README.md' 'todo.root.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' PASS (EXITCODE=0, 2026-02-23 08:40)
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

- [x] Tunnel-Check als VS-Code-Task ergänzen (`Checks: sim epoch assets`) und im README kurz dokumentieren.
  - Evidenz: `/.vscode/tasks.json`, `README.md`.
- [x] Aktive TODO-Boards (Agent/Sim/RP) auf Prioritätstags `Jetzt/Als naechstes/Später` harmonisieren.
  - Evidenz: `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.sim.md`, `novapolis-dev/docs/todo.rp.md`.
- [x] Wochenabschluss-Routine standardisieren: Reihenfolge und Artefaktablage für Tests/Checks/Status-Update verbindlich notieren.
  - Evidenz: `README.md` (Abschnitt „Wochenabschluss-Routine“).

Hinweise
--------

- Abgeschlossene oder historisierte Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei jeder Mutation TODO/DONELOG/WORKSPACE_STATUS synchron halten.



