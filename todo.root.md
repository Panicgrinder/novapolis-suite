---
stand: 2026-03-17 16:58
update: Wochenabschluss-Nachholung gemaess SSOT ausgefuehrt; Root-Sync dokumentiert.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260317_064114.md; .\.venv\Scripts\python.exe scripts\check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency summary=fail:0,warn:2; .\.venv\Scripts\python.exe scripts\run_pytest_coverage.py --fail-under 80 PASS (coverage=91.23%; log=.tmp\results\reports\pytest_coverage_20260317_064421.log)
---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Vorheriger Vollinhalt wurde archiviert unter `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md`.
- Historische Sammelbasis: `novapolis-dev/archive/todo.root.archive.md`.
- Diese Datei ist jetzt die aktive Arbeitsliste fuer neue Punkte.
- README-Pruefpunkt (73/73) wurde nach finalem Doppelcheck archiviert: `novapolis-dev/archive/todo.root.archive.md` (Abschnitt "README-Gesamtlauf (73/73) - abgeschlossen").

Projektweite Analyseabdeckung (laufend)
---------------------------------------

Ziel: Den gesamten aktiven Workspace in explizite Analysebereiche zerlegen, damit der weitere Tiefenscan vollstaendig gegen den realen Projektschnitt laeuft und keine aktive Flaeche stillschweigend ausfaellt.

Statuslegende:

- `[x]` Bereich bereits mindestens einmal analysiert.
- `[ ]` Bereich noch offen fuer den naechsten Tiefenscan.
- `On-demand` Bereich ist bewusst nachrangig und wird nur bei harter Evidenz oder konkretem Auftrag vertieft.

Root-Ebene / Suite-Steuerung
----------------------------

- [x] R1 Root-/Globaloberflaeche: `README.md`, `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, `todo.root.md`, `DONELOG.md`.
- [ ] R2 Root-Governance-/Community-Doku: `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `TRADEMARKS.md`, `LICENSES.md`, `LICENSE`.
- [ ] R3 Root-Konfiguration/Toolchain: `pyproject.toml`, `requirements.txt`, `requirements-dev.txt`, `pytest.ini`, `.editorconfig`, `.gitattributes`, `.gitignore`, `.env.example`.
- [ ] R4 Root-Shared-Code/-Bridges: `app/**`, `utils/**`, `packages/**`.
- [ ] R5 Root-Skripte/Automationskern: `scripts/**`, `githooks/**`.
- [ ] R6 Root-Daten-/Hilfsflaechen mit aktivem Anspruch: `docs/**`, `eval/**`, `reports/**`, `combined.json`, `workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt`, `extensions.installed.txt`, `extensions.status.txt`.

Repo-Steuerung / Editor / CI
----------------------------

- [ ] C1 VS-Code-Steuerung: `.vscode/**` (Tasks, Launch, Settings, Shared-Workspace-Automation).
- [ ] C2 GitHub-Steuerung aktiv: `.github/workflows/**`, `.github/CODEOWNERS`, Issue-/PR-Templates, aktive `.github/*.md` ausser Archiv.
- [ ] C3 Instruction-/Agent-Steuerung: `.github/instructions/**`, `.github/copilot-instructions-headings.md`, `.github/agents/**`.
- [ ] C4 Release-/PR-Steuerung: `PR_DESCRIPTION.md` plus wirksame Release-/CI-Koppelstellen.

Dev-Hub
-------

- [x] D1 Dev-Hub Einstieg: `novapolis-dev/README.md`.
- [x] D2 Dev-Hub Live-Docs: `novapolis-dev/docs/**` aktive Boards, SSOTs, Specs, Prozesse, Register.
- [x] D3 Dev-Hub Metadaten: `novapolis-dev/docs/meta/**`.
- [x] D4 Dev-Hub Logs aktiv: `novapolis-dev/logs/README.md` plus Policy-relevanter aktiver Logpfad.
- [ ] D5 Dev-Hub Integrationen/Migrationen: `novapolis-dev/integrations/**`, `novapolis-dev/migrations/**`, `novapolis-dev/scripts/**`.

Agent-Modul
-----------

- [x] A1 Agent Einstieg/Doku: `novapolis_agent/README.md`, `novapolis_agent/docs/**`, `novapolis_agent/docs/DONELOG.txt`.
- [x] A2 Agent Runtime-Code: `novapolis_agent/app/**`, `novapolis_agent/utils/**`, `novapolis_agent/run_server.py`.
- [x] A3 Agent Tests und Typ-Grenzen: `novapolis_agent/tests/**`, relevante Configs (`mypy.ini`, `pyrightconfig.json`, `pytest.ini`).
- [x] A4 Agent Skripte/CLI: `novapolis_agent/scripts/**`.
- [x] A5 Agent Eval-/Config-Flaechen aktiv: `novapolis_agent/eval/config/**`, `novapolis_agent/eval/datasets/**`, operative Teile von `novapolis_agent/eval/README.md`.
- [ ] A6 Agent Runtime-Daten/Artefakte on-demand: `novapolis_agent/data/**`, `novapolis_agent/outputs/**`, `novapolis_agent/tmp/**`.
- [ ] A7 Agent Paket-/Kompatibilitaetslayer: `novapolis_agent/novapolis_agent/**`, Egg-Info, Shims/Bridges.

RP-Modul
--------

- [x] P1 RP Einstieg/Doku: `novapolis-rp/README.md`.
- [x] P2 RP-SSOT Admin: `novapolis-rp/database-rp/00-admin/**`.
- [x] P3 RP-SSOT Fachflaechen: `novapolis-rp/database-rp/01-factions/**`, `02-characters/**`, `03-locations/**`, `04-inventory/**`, `05-projects/**`, `06-scenes/**`.
- [x] P4 RP-Arbeits-/Workflowdoku aktiv: RP-bezogene aktive Dokumente im Dev-Hub und direkte RP-Markdownpfade.
- [ ] P5 RP-Kurations-/Validatorpfade: `novapolis-rp/coding/**`, `novapolis-rp/database-curated/**`.
- [ ] P6 RP-RAW-/Importpfade on-demand: `novapolis-rp/database-raw/**`.

Sim-Modul
---------

- [x] S1 Sim Einstieg: `novapolis-sim/README.md`.
- [x] S2 Sim Kernprojekt: `novapolis-sim/project.godot`, `novapolis-sim/Main.tscn`.
- [x] S3 Sim Runtime-/UI-Skripte: `novapolis-sim/scripts/**`.
- [ ] S4 Sim Daten-/Asset-Flaechen: `novapolis-sim/assets/**`, `novapolis-sim/autoload/**`, `novapolis-sim/novapolis-sim/**` sofern aktiv genutzt.

Explizit nicht Teil des aktiven Erstscans
-----------------------------------------

- On-demand / historisch / generiert: `novapolis-dev/archive/**`, `Backups/**`, `.tmp/**`, `.tmp-datasets/**`, `outputs/**`, `tmp/**`, `.venv/**`, `node_modules/**`, `.coverage*`, `.ruff_cache/**`, `.pytest_cache/**`, `__pycache__/**`, weitere reine Cache-/Build-Artefakte.

Neue Punkte (Backlog)
---------------------

- [x] Wochenabschluss 2026-03-17 nach SSOT nachgeholt (Checks, Coverage, Sim-Check, Abschluss-Sync; kein Tree-Delta).
  - Evidenz: `.tmp/results/reports/checks_report_20260317_064114.md`, `.tmp/results/reports/pytest_coverage_postflight_20260317_064421.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`.

- [ ] [Als naechstes] Root-Toolchain-Doku und zentrale `.env.example` auf realen Single-Root-Scope synchronisieren.
  - Akzeptanzkriterien: (1) Root-README beschreibt den Umfang von `requirements.txt` und `requirements-dev.txt` ohne Ueberclaim ueber alle Teilprojekte, (2) die zentrale `.env.example` nutzt den aktuellen Produkt-/Projektbezug statt des Alt-Namens `CVN Agent`, (3) Zentralisierung zwischen Root-`.env.example` und `novapolis_agent/.env.example` bleibt konsistent erklaert.
  - Evidenz: `README.md` behauptet aktuell, die Root-Dateien `requirements.txt` und `requirements-dev.txt` sammelten die Pins aller Teilprojekte, waehrend die Dateien faktisch nur `novapolis_agent/requirements/base.txt`, `novapolis_agent/requirements/dev.txt` und `novapolis_agent/requirements/train.txt` aggregieren; zugleich traegt `.env.example` weiterhin `PROJECT_NAME=CVN Agent` und `PROJECT_VERSION=0.1.0`, obwohl `novapolis_agent/.env.example` explizit nur noch auf die Root-Datei als zentrale Quelle verweist.

- [ ] [Als naechstes] Root-Shared-Layer (`app/`, `utils/`, `packages/`) von dauerhaften Shim-/Platzhalterstrukturen auf klaren Ist-Status heben.
  - Akzeptanzkriterien: (1) Root-Bridges in `app/__init__.py` und `utils/__init__.py` sind als bewusst verbleibende Kompatibilitaetslayer oder als Abbaukandidaten klar eingeordnet, (2) `packages/novapolis_common` ist entweder mit echter gemeinsamer Logik befuellt oder als vorbereiteter, noch leerer Migrationsslot explizit dokumentiert, (3) Root-Doku suggeriert keinen weiter entwickelten Shared-Layer als tatsaechlich vorhanden.
  - Evidenz: `app/__init__.py` ist nur ein Test-/Kompatibilitaetsshim auf `novapolis_agent/app`, `utils/__init__.py` nur eine Legacy-Import-Bridge auf `novapolis_agent/utils`, und `packages/novapolis_common/__init__.py` enthaelt aktuell lediglich einen Platzhalterkommentar zur spaeteren Migration gemeinsamer Logik.

- [ ] [Als naechstes] Root-Skripte von Altpfad- und Legacy-Cleanup-Drift bereinigen.
  - Akzeptanzkriterien: (1) `scripts/run_checks_and_report.py` referenziert in seinem Frontmatter-Scope keine nur archiviert existierenden Root-Dateien mehr, (2) Altwerkzeuge wie `scripts/multi_root_cleanup.py` sind entweder klar als historisch/quarantaenepflichtig markiert oder an den heutigen Single-Root-Iststand angepasst, (3) der Root-Skriptbestand ist fuer aktive vs. historische Wrapper besser trennbar.
  - Evidenz: `scripts/run_checks_and_report.py` fuehrt in `FRONTMATTER_PATHS` weiterhin `single-root-todo.md`, das im Workspace nur noch unter `novapolis-dev/archive/quarantine/single-root-todo.md` existiert; zugleich beschreibt `scripts/multi_root_cleanup.py` weiterhin einen Multi-Root-Bereinigungsworkflow mit direkten Mutationen an `WORKSPACE_STATUS.md`, `DONELOG.md` und `todo.root.md` aus einem ueberholten Umstellungskontext.

- [ ] [Als naechstes] Top-Level-Hilfsartefakte auf den aktiven Single-Root-Iststand bereinigen.
  - Akzeptanzkriterien: (1) `combined.json` wird entweder entfernt, archiviert oder als historisches Multi-Root-Artefakt klar markiert, (2) die `workspace_tree*.txt`-Artefakte spiegeln den gewollten aktiven Oberflaechenschnitt statt ausgeschlossener Cache-/Backup-/Tmp-Baeume, (3) Root-Hilfsartefakte widersprechen der dokumentierten Single-Root-Realitaet nicht.
  - Evidenz: `combined.json` definiert weiterhin ein altes Multi-Root-Setup mit den Ordnern `cvn-agent` und `novapolis-rp`; `workspace_tree.txt` und `workspace_tree_dirs.txt` listen zugleich weiterhin klar ausgeschlossene Pfade wie `.tmp/`, `Backups/` und `node_modules/`, obwohl diese laut Root-TODO nicht Teil des aktiven Erstscans sind.

- [ ] [Als naechstes] `PR_DESCRIPTION.md` von historischer Einzel-PR auf aktuelle Release-/PR-Vorlage umstellen.
  - Akzeptanzkriterien: (1) `PR_DESCRIPTION.md` ist als wiederverwendbare aktuelle PR-/Release-Vorlage lesbar oder explizit als Archivartefakt markiert, (2) die Datei transportiert keinen alten abgeschlossenen Arbeitsstand mehr als aktuelle Vorlage, (3) die Release-/Merge-Steuerung verweist auf den heutigen Governance- und Quality-Gate-Zustand.
  - Evidenz: `PR_DESCRIPTION.md` traegt weiterhin den Titel `PR: Stabilization And Governance Hardening (2026-03-03)` und beschreibt einen abgeschlossenen Alt-Run (`finalizes the Novapolis stabilization and governance hardening run`) statt einer aktuellen generischen Vorlage fuer neue PRs oder Releases.

- [ ] [Als naechstes] Root-Summary und Standalone-Beta-Exit-Checkliste gegen den aktuellen Modulbacklog re-baselinen.
  - Akzeptanzkriterien: `todo.root.md`, `WORKSPACE_STATUS.md` und Root-Zusammenfassungen suggerieren nicht mehr, dass ausser `O11` praktisch nur ein sauberer Restzustand offen ist, waehrend die aktiven Modulboards noch offene Driftpunkte tragen; relevante Root-Blocker werden entweder explizit wiedereroeffnet oder als nicht-beta-kritisch abgegrenzt.
  - Evidenz: `todo.root.md` fuehrt in der `Standalone-Beta Exit-Checkliste` nur noch `Optional O11` offen und markiert die `Definition of Ready` vollstaendig als erledigt, waehrend `novapolis-dev/docs/todo.index.md` aktuell offene Punkte in Dev `9`, RP `6`, Agent `6` und Sim `2` ausweist.

- [ ] [Als naechstes] `WORKSPACE_INDEX.md` von agent-zentriertem Altindex auf eine echte Root-/Suite-Navigation umstellen.
  - Akzeptanzkriterien: Titel, Einleitung und oberer Navigationsblock in `WORKSPACE_INDEX.md` beschreiben die Novapolis Suite statt eines alten Agent-Katalogs; redundante Agent-Detailinventare werden gekuerzt, verschoben oder klar als historisch/sekundaer markiert.
  - Evidenz: `WORKSPACE_INDEX.md` traegt weiterhin den Titel `Novapolis Agent - Workspace Datei-Index` und beschreibt sich direkt als `detailreicher Agent-spezifischer Katalog`, obwohl die Datei im Root als globale Workspace-Navigation verlinkt und genutzt wird.

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
- [ ] [Optional O11] Beta-Installblatt fuer Dritte erstellen: minimale Voraussetzungen, Setup, Troubleshooting.
  - Akzeptanz: eine externe Person kann lokal ohne implizites Vorwissen starten.
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






