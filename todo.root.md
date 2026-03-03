---
stand: 2026-03-04 00:28
update: Standalone-Beta-Exit-Checkliste (priorisiert, Blocker/Optional, Reihenfolge) als operativen Root-Plan aufgenommen.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'todo.root.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-03-04 00:30); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'todo.root.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (EXITCODE=0, 2026-03-04 00:30)
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

Standalone-Beta Exit-Checkliste (v0, geordnet)
-----------------------------------------------

Ziel: Eine lokal reproduzierbare Standalone-Beta mit stabilen Gates, dokumentierter Bedienung und klaren No-Go-Kriterien.

- [ ] [Blocker B1] Root-TTS-Migration abschliessen: benoetigte Inhalte aus `TTS/` in `novapolis_agent/` ueberfuehren und Root-`TTS/` entfernen.
  - Akzeptanz: `todo.root.md`-Punkt erledigt; README/Status/DONELOG synchron; kein Root-`TTS/` mehr im aktiven Baum.
- [ ] [Blocker B2] Sim-Restpunkte schliessen: in `novapolis-dev/docs/todo.sim.md` den Platzhalter konkretisieren und den offenen DoD-Punkt evidenzbasiert auf erledigt setzen.
  - Akzeptanz: `offen: 0` fuer Sim im `novapolis-dev/docs/todo.index.md`.
- [ ] [Blocker B3] RP-P0-DoD schliessen: T0-Warenueberblick je Fraktion + D5/C6-Aufbauphase konsistent finalisieren.
  - Akzeptanz: offene `[Jetzt]`-Punkte in `novapolis-dev/docs/todo.rp.md` fuer P0 erledigt, Evidenzpfade gesetzt.
- [ ] [Blocker B4] Dev-Truthfulness korrigieren: offene Driftpunkte in `novapolis-dev/docs/todo.dev.md` fuer aktive Dokuoberflaeche beheben.
  - Akzeptanz: README/spec claims spiegeln ausschliesslich Iststand.
- [ ] [Blocker B5] Stabilen Full-Check als Beta-Gate einfrieren: ein aktueller kompletter Lauf (`Checks: full`) mit gruenem Ergebnisbeleg.
  - Akzeptanz: verlinkter Report in `.tmp/results/reports/` plus Eintrag in `novapolis-dev/docs/donelog.md` und `DONELOG.md`.
- [ ] [Blocker B6] Standalone-Startpfad dokumentieren: ein kanonischer Startablauf fuer API + Sim-Hub + Checklauf.
  - Akzeptanz: reproduzierbarer Abschnitt in `README.md` oder Runbook mit 1:1-Kommandos und erwarteten Ergebnissen.
- [ ] [Blocker B7] Release-Go/No-Go Kriterien festschreiben: minimale Schwellwerte fuer Tests/Typen/Coverage/Runtime.
  - Akzeptanz: schriftliche Gate-Definition in Dev-Doku; Entscheidung pro Lauf nachvollziehbar protokolliert.
- [ ] [Optional O8] TODO-Index-Guard automatisieren: Aenderungen an `todo.*.md` erzwingen Sync von `novapolis-dev/docs/todo.index.md`.
  - Akzeptanz: technischer Check vorhanden und im Standardlauf eingebunden.
- [ ] [Optional O9] Freshness-SLA durchsetzen: aktive Dokus nach Altersgrenze pruefen (`stand`).
  - Akzeptanz: dokumentierter Checklauf ohne ungekennzeichnete Ausnahmen.
- [ ] [Optional O10] Logs-Policy haerten: klare Regeln fuer `novapolis-dev/logs/` inkl. `*.tmp.md` konsistent umsetzen.
  - Akzeptanz: keine policy-widrigen Artefakte im aktiven Logpfad.
- [ ] [Optional O11] Beta-Installblatt fuer Dritte erstellen: minimale Voraussetzungen, Setup, Troubleshooting.
  - Akzeptanz: eine externe Person kann lokal ohne implizites Vorwissen starten.
- [ ] [Optional O12] Beta-Tagging vorbereiten: einheitliches Namensschema fuer Beta-Builds und Ergebnisreports.
  - Akzeptanz: run-/artefaktnahe Labels sind in Doku und DONELOG konsistent.

Definition of Ready fuer "Standalone Beta"
-------------------------------------------

- [ ] Alle Blocker B1-B7 erledigt.
- [ ] Ein finaler Referenzlauf (Checks + Startpfad) ist reproduzierbar dokumentiert.
- [ ] Offene Punkte sind nur noch als `[Optional]` markiert.

Hinweise
--------

- Abgeschlossene oder historisierte Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei jeder Mutation TODO/DONELOG/WORKSPACE_STATUS synchron halten.




