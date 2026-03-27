---
stand: 2026-03-27 09:54
update: Offene Folgearbeit nach dem Wochenabschluss aus den Boards abgeleitet; Root-Backlog fuehrt jetzt RP-, Sim- und Dev-Hygiene-Fortsetzung explizit.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260327_011507.md
---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Der aktuelle Referenzlauf vom 2026-03-27 ist gruen (`overall=PASS`, Coverage `93.69%`); der Wochenabschluss ist komplett nach SSOT dokumentiert, inklusive Coverage-Gate, Hygiene-KPIs und Sim-Asset-Check ohne harte Fehler.
- Vorheriger Vollinhalt wurde archiviert unter `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md`.
- Historische Sammelbasis: `novapolis-dev/archive/todo.root.archive.md`.
- Diese Datei ist jetzt die aktive Arbeitsliste fuer neue Punkte.
- README-Pruefpunkt (73/73) wurde nach finalem Doppelcheck archiviert: `novapolis-dev/archive/todo.root.archive.md` (Abschnitt "README-Gesamtlauf (73/73) - abgeschlossen").

Neue Punkte (Backlog)
---------------------

- [ ] RP-Inventar-Backfill in die belegte Transferkette ueberfuehren (`D5 -> C6` mit Entnahme, Zielbuchung, Quittung) und `Novapolis-inventar.md` auf Delta-Format umstellen.
  - Evidenz: `novapolis-dev/docs/todo.rp.md`, `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`.

- [ ] Sim-Asset-Warnungen aus dem Wochenabschluss entscheiden: entweder beheben oder als bewusste Ausnahme dokumentieren.
  - Evidenz: `novapolis-dev/docs/todo.sim.md`, `WORKSPACE_STATUS.md` (Wochenabschluss 2026-03-27, `summary=fail:0,warn:2`).

- [ ] TODO-Index-Metadaten gegen die aktuellen Boards haerten, damit `letzte Aenderung` und Open-Counts nicht sichtbar hinterherlaufen.
  - Evidenz: `novapolis-dev/docs/todo.dev.md`, `novapolis-dev/docs/todo.index.md`.

- [x] Wochenabschluss 2026-03-27 nach SSOT komplett ausgefuehrt (Full-Gate, Coverage-Gate, Hygiene-KPIs, Abschluss-Sync).
  - Evidenz: `.tmp/results/reports/checks_report_20260327_011507.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`, `novapolis-dev/docs/meta/dev-kpi-trends.md`, `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.sim.md`.

- [x] Wochenabschluss 2026-03-10 nach SSOT ausgefuehrt (Checks, Tree-Artefakte, Abschluss-Sync).
  - Evidenz: `.tmp/results/reports/checks_report_20260310_153947.md`, `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`.

- [x] Tunnel-Check als VS-Code-Task ergänzen (`Checks: sim epoch assets`) und im README kurz dokumentieren.
  - Evidenz: `/.vscode/tasks.json`, `README.md`.
- [x] Aktive TODO-Boards (Agent/Sim/RP) auf Prioritätstags `Jetzt/Als naechstes/Später` harmonisieren.
  - Evidenz: `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.sim.md`, `novapolis-dev/docs/todo.rp.md`.
- [x] Wochenabschluss-Routine standardisieren: Reihenfolge und Artefaktablage für Tests/Checks/Status-Update verbindlich notieren.
  - Evidenz: `README.md` (Abschnitt „Wochenabschluss-Routine“).
- [x] [Jetzt] `TTS/` nur als temporaere Entnahmequelle behandeln: benoetigte Teile nach `novapolis_agent/` ueberfuehren und das Root-Verzeichnis `TTS/` danach entfernen.
  - Akzeptanzkriterien: (1) Entnommene Dateien/Pfade in `novapolis_agent/` dokumentiert, (2) `TTS/` aus Root entfernt, (3) README/Status/DONELOG synchronisiert.
  - Evidenz: `novapolis_agent/scripts/tts_coqui_export.py` (`--help` verifiziert), Root-Pfad `TTS/` entfernt, Sync in `README.md`/`WORKSPACE_STATUS.md`/`DONELOG.md`.

Standalone-Beta Exit-Checkliste (v0, geordnet)
-----------------------------------------------

Ziel: Eine lokal reproduzierbare Standalone-Beta mit stabilen Gates, dokumentierter Bedienung und klaren No-Go-Kriterien.

- [x] [Blocker B1] Root-TTS-Migration abschliessen: benoetigte Inhalte aus `TTS/` in `novapolis_agent/` ueberfuehren und Root-`TTS/` entfernen.
  - Akzeptanz: `todo.root.md`-Punkt erledigt; README/Status/DONELOG synchron; kein Root-`TTS/` mehr im aktiven Baum.
- [x] [Blocker B2] Sim-Restpunkte schliessen: in `novapolis-dev/docs/todo.sim.md` den Platzhalter konkretisieren und den offenen DoD-Punkt evidenzbasiert auf erledigt setzen.
  - Akzeptanz: `offen: 0` fuer Sim im `novapolis-dev/docs/todo.index.md`.
- [x] [Blocker B3] RP-P0-DoD schliessen: T0-Warenueberblick je Fraktion + D5/C6-Aufbauphase konsistent finalisieren.
  - Akzeptanz: offene `[Jetzt]`-Punkte in `novapolis-dev/docs/todo.rp.md` fuer P0 erledigt, Evidenzpfade gesetzt.
- [x] [Blocker B4] Dev-Truthfulness korrigieren: offene Driftpunkte in `novapolis-dev/docs/todo.dev.md` fuer aktive Dokuoberflaeche beheben.
  - Akzeptanz: README/spec claims spiegeln ausschliesslich Iststand.
- [x] [Blocker B5] Stabilen Full-Check als Beta-Gate einfrieren: ein aktueller kompletter Lauf (`Checks: full`) mit gruenem Ergebnisbeleg.
  - Akzeptanz: verlinkter Report in `.tmp/results/reports/` plus Eintrag in `novapolis-dev/docs/donelog.md` und `DONELOG.md`.
- [x] [Blocker B6] Standalone-Startpfad dokumentieren: ein kanonischer Startablauf fuer API + Sim-Hub + Checklauf.
  - Akzeptanz: reproduzierbarer Abschnitt in `README.md` oder Runbook mit 1:1-Kommandos und erwarteten Ergebnissen.
- [x] [Blocker B7] Release-Go/No-Go Kriterien festschreiben: minimale Schwellwerte fuer Tests/Typen/Coverage/Runtime.
  - Akzeptanz: schriftliche Gate-Definition in Dev-Doku; Entscheidung pro Lauf nachvollziehbar protokolliert.
- [x] [Optional O8] TODO-Index-Guard automatisieren: Aenderungen an `todo.*.md` erzwingen Sync von `novapolis-dev/docs/todo.index.md`.
  - Akzeptanz: technischer Check vorhanden und im Standardlauf eingebunden.
  - Evidenz: `scripts/check_todo_index_sync.py`, `scripts/run_checks_and_report.py`, `/.vscode/tasks.json` (`Checks: todo index sync`).
- [x] [Optional O9] Freshness-SLA durchsetzen: aktive Dokus nach Altersgrenze pruefen (`stand`).
  - Akzeptanz: dokumentierter Checklauf ohne ungekennzeichnete Ausnahmen.
  - Evidenz: `scripts/check_doc_freshness.py` (ACTIVE `<=14`, REFERENCE `<=60`), `scripts/run_checks_and_report.py`, `/.vscode/tasks.json` (`Checks: doc freshness`).
- [x] [Optional O10] Logs-Policy haerten: klare Regeln fuer `novapolis-dev/logs/` inkl. `*.tmp.md` konsistent umsetzen.
  - Akzeptanz: keine policy-widrigen Artefakte im aktiven Logpfad.
  - Evidenz: `scripts/check_logs_policy.py`, `novapolis-dev/logs/README.md`, verschobener Rohlog nach `novapolis-dev/archive/quarantine/logs/betriebsmodi-20251103-0341.tmp.md`.
- [x] [Optional O11] Beta-Installblatt fuer Dritte erstellen: minimale Voraussetzungen, Setup, Troubleshooting.
  - Akzeptanz: eine externe Person kann lokal ohne implizites Vorwissen starten.
  - Evidenz: `novapolis-dev/docs/process/standalone-beta-installblatt.md`, Root-README-Verweis im Abschnitt `Standalone-Beta Startpfad (kanonisch)`.
- [x] [Optional O12] Beta-Tagging vorbereiten: einheitliches Namensschema fuer Beta-Builds und Ergebnisreports.
  - Akzeptanz: run-/artefaktnahe Labels sind in Doku und DONELOG konsistent.
  - Evidenz: `novapolis-dev/docs/process/standalone-beta-gates.ssot.md` (Abschnitt `Beta-Tagging-Konvention`), Eintragsformat in `novapolis-dev/docs/donelog.md` und `DONELOG.md`.

Definition of Ready fuer "Standalone Beta"
-------------------------------------------

- [x] Alle Blocker B1-B7 erledigt.
- [x] Ein finaler Referenzlauf (Checks + Startpfad) ist reproduzierbar dokumentiert.
- [x] Offene Punkte sind nur noch als `[Optional]` markiert.

Hinweise
--------

- Abgeschlossene oder historisierte Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei jeder Mutation TODO/DONELOG/WORKSPACE_STATUS synchron halten.






