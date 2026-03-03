---
stand: 2026-03-03 14:32
update: Tagesabschluss vorbereitet; heutiger Abschlusslauf dokumentiert und Root-Backlog auf offenen Kernpunkt fokussiert belassen.
checks: .\.venv\Scripts\python.exe scripts\snapshot_write_lock.py PASS (2026-03-03 03:43); process: Checks: full FAIL (2026-03-03 03:39); .\.venv\Scripts\python.exe scripts\run_pytest_coverage.py FAIL (EXITCODE=1, 2026-03-03 03:40); .\.venv\Scripts\python.exe scripts\check_sim_epoch_assets.py --repo-root . --allow-empty PASS (summary=fail:0,warn:2, 2026-03-03 03:40); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'todo.root.md' 'WORKSPACE_STATUS.md' 'DONELOG.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-03 03:45); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'todo.root.md' 'WORKSPACE_STATUS.md' 'DONELOG.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-03 03:45)
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
- [ ] [Jetzt] `TTS/` nur als temporaere Entnahmequelle behandeln: benoetigte Teile nach `novapolis_agent/` ueberfuehren und das Root-Verzeichnis `TTS/` danach entfernen.
  - Akzeptanzkriterien: (1) Entnommene Dateien/Pfade in `novapolis_agent/` dokumentiert, (2) `TTS/` aus Root entfernt, (3) README/Status/DONELOG synchronisiert.
  - Evidenz: `README.md` (TTS-Vormerkung), Root-`.gitignore` (`/TTS/`).
  - Status 2026-03-03 03:43: Abschlusslauf erneut bestaetigt, Punkt bleibt offen und priorisiert bis zur tatsaechlichen Entnahme/Entfernung.

Hinweise
--------

- Abgeschlossene oder historisierte Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei jeder Mutation TODO/DONELOG/WORKSPACE_STATUS synchron halten.




