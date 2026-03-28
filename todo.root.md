---
stand: 2026-03-28 06:51
update: Root-eval-Rest final bereinigt; nach den Abschluss-Checks neu entstandener Stub separat quarantanisiert und Tree-Artefakte erneut nachgezogen.
checks: snapshot-lock PASS; pytest PASS; markdownlint PASS; frontmatter PASS; todo-index PASS; logs-policy PASS; doc-freshness PASS (2026-03-28 06:32)
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

- [x] Verbleibenden Root-eval-Rest auf den Modulpfad umziehen und danach aus dem aktiven Root-Surface entfernen.
  - Ziel: Der letzte noch aktive Root-Verweis `eval/config/context.local.md` soll auf den kanonischen Modulpfad unter `novapolis_agent/eval/config/` umgestellt werden, damit der verbliebene Root-eval-Rest nicht weiter technisch live bleibt.
  - Akzeptanzkriterien:
    1) Runtime-Defaults und Hilfsskripte nutzen fuer lokale Kontext-Notizen den Modulpfad statt `eval/config/...`,
    2) aktive Doku verweist auf `novapolis_agent/eval/config/context.local.sample.md` und den Modulpfad in `CONTEXT_NOTES_PATHS`,
    3) der verbliebene Root-eval-Rest wird nachvollziehbar nach Quarantaene ueberfuehrt statt still geloescht,
    4) Root-/Agent-DONELOG, Status und TODO-Index dokumentieren den Schritt im selben Lauf.
  - Evidenz: `novapolis_agent/app/core/settings.py` fuehrt `CONTEXT_NOTES_PATHS` noch mit `eval/config/context.local.md`, `novapolis_agent/scripts/open_context_notes.py` faellt ebenfalls auf den Root-Pfad zurueck, und `eval/results/tmp_summaries/` hat im aktiven Scope keine belegten Referenzen mehr.
  - Abschluss 2026-03-28: `app/core/settings.py`, `app/api/chat.py`, `scripts/open_context_notes.py` und die Agent-README nutzen jetzt durchgaengig `novapolis_agent/eval/...`; der urspruengliche Root-Ordner `eval/` liegt nachvollziehbar unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0501-root-eval-rest/eval`, ein nach den Nachweisen erneut entstandener lokaler Stub `eval/config/context.local.md` wurde zusaetzlich nach `novapolis-dev/archive/quarantine/root-cleanup-20260328_0632-root-eval-rest-postchecks/eval` ueberfuehrt, und die Root-Tree-Artefakte wurden danach erneut neu erzeugt.

- [x] Lokale Editor-/Host-Snapshots aus dem Main-Root in Quarantaene ueberfuehren.
  - Ziel: Root-Dateien ohne aktive Repo-Funktion, die nur den lokalen VS-Code-/Host-Stand spiegeln, sollen nicht im produktiven Single-Root-Surface liegen.
  - Akzeptanzkriterien:
    1) `extensions.installed.txt`, `extensions.status.txt` und `desktop.ini` liegen nicht mehr im Root,
    2) die Dateien sind in einem nachvollziehbaren Quarantaenepfad abgelegt statt still geloescht,
    3) aktive Root-Pfade wie Shims, Tree-Artefakte und Governance-Dokumente bleiben unangetastet,
    4) Root-Backlog, DONELOGs und Workspace-Status dokumentieren den Schritt im selben Lauf.
  - Evidenz: `extensions.installed.txt` listet lokale VS-Code-Erweiterungen, `extensions.status.txt` ist ein lokaler `code --status`-Snapshot, und `desktop.ini` taucht nur noch im alten Tree-Artefakt auf, nicht als aktive Repo-Referenz.
  - Abschluss 2026-03-28: Die drei Dateien liegen jetzt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0330-local-snapshots/`; die Root-Tree-Artefakte wurden danach direkt per Terminal neu erzeugt, weil die vorhandenen Shell-Tasks lokal weiter am bekannten `pwsh /d /c`-Fehlpfad scheitern.

- [x] Sichere Root-Altartefakte aus dem aktiven Single-Root-Surface in Quarantaene ueberfuehren.
  - Evidenz: `combined.json`, `lint.out`, `md003_scan.out`, `.tmp-datasets/` und `reports/` lagen als historische oder temporare Restartefakte direkt im Repo-Root, obwohl der aktive Betriebsrahmen diese Inhalte heute unter `.tmp/`, Modulpfaden oder Archiv-/Quarantaenepfaden fuehrt.
  - Abschluss 2026-03-28: Die Kandidaten liegen gesammelt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0238/`; die gleichnamigen Root-Pfade sind entfernt und tauchen im aktiven Root nicht mehr auf.
  - Bewusste Nicht-Ziele: Die aktiven Kompatibilitaetsshims `app/__init__.py` und `utils/__init__.py` sowie der noch referenzierte Hinweis `eval/config/context.local.md` blieben unveraendert.

- [x] Einheitlichen Stil- und Konsistenzlauf fuer Hochfrequenz-Dateien und aktive Doku nach dokumentiertem Phasenplan durchziehen.
  - Evidenz: `README.md`, `WORKSPACE_INDEX.md`, `novapolis-dev/README.md`, die Modul-READMEs und `novapolis-dev/docs/todo.index.md` mussten gerade erst sichtbare Drift bei Status-Headern, Pfaden, Kommandos und aktiven Verweisen nachgezogen bekommen.
  - Arbeitsplan: `novapolis-dev/docs/process/doku-konsistenzlauf-aktive-surface-2026-03-28.md`.
  - Abschluss 2026-03-28: Hochfrequenz-Dateien, aktive Dev-SSOTs und die ersten Modul-Runbooks fuehren jetzt durchgaengig den PASS-/Root-Wrapper-Stil; im aktiven Scope blieb beim Restscan nur noch ignorierte Drittanbieter-Doku unter `node_modules` ausserhalb des Arbeitsbereichs uebrig.

- [x] Aktive Reader-Surface fuer Root/Dev und die vier Hauptmodule auf den aktuellen Single-Root-/PASS-Iststand ziehen.
  - Evidenz: `novapolis-dev/README.md`, `WORKSPACE_INDEX.md`, `novapolis_agent/README.md`, `novapolis-rp/README.md`, `novapolis-sim/README.md` fuehren teils noch Vor-Maerz-Receipts, Altpfade oder lokale `venv`-/Sibling-Hinweise statt des aktuellen Root-`.venv`- und PASS-Kontexts.
  - Abschluss 2026-03-28: Die aktiven Lesedokumente fuehren jetzt keinen veralteten FAIL-Header mehr, nutzen den Single-Root-/`.venv`-Pfad konsistent und trennen im Sim-Modul UI-Start sauber von optionalen Asset-Warnungen.

- [ ] Agent-Export-/Pack-Pfad gegen Null-Exports aus historischem Results-Drift haerten.
  - Evidenz: `novapolis-dev/docs/todo.agent-board.md`, `novapolis_agent/docs/DONELOG.txt` (Laufbeleg 2026-02-27: `export_finetune.py` lieferte fuer ein historisches Resultset `0` Eintraege wegen Source-Path-Drift).

- [ ] RP-Inventar-Backfill in die belegte Transferkette ueberfuehren (`D5 -> C6` mit Entnahme, Zielbuchung, Quittung) und `Novapolis-inventar.md` auf Delta-Format umstellen.
  - Evidenz: `novapolis-dev/docs/todo.rp.md`, `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md`, `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`.

- [ ] RP-Finalzuteilung aus der fraktionsscharfen Matrix in ein operatives Arbeitsledger ueberfuehren.
  - Evidenz: `novapolis-dev/docs/process/rp-metro-warenzuteilung-matrix-2026-03-27.md`, `novapolis-dev/docs/todo.rp.md`.

- [ ] Sim-Asset-Warnungen aus dem Wochenabschluss entscheiden: entweder beheben oder als bewusste Ausnahme dokumentieren.
  - Evidenz: `novapolis-dev/docs/todo.sim.md`, `WORKSPACE_STATUS.md` (Wochenabschluss 2026-03-27, `summary=fail:0,warn:2`).

- [ ] Sim-Minimalprofil fuer Epoch-/Audio-Assets festlegen, damit Clean-Checkout und Vollstand getrennte Erwartungswerte haben.
  - Evidenz: `novapolis-dev/docs/todo.sim.md`, `novapolis-sim/README.md`, `WORKSPACE_STATUS.md` (weiter `warn:2` trotz sonst gruener Sim-Verifikation).

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






