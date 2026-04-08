---
stand: 2026-04-08 13:40
update: Dev-DONELOG dokumentiert jetzt den nachgezogenen Wochenabschluss mit gruenem Full-Check, Coverage-, Sim- und KPI-Block.
checks: Wochenabschluss via scripts/run_checks_and_report.py overall=PASS; report=.tmp\results\reports\checks_report_20260408_131224.md; scripts\check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency summary=fail:0,warn:0; scripts\run_pytest_coverage.py --fail-under 80 PASS report=.tmp\results\reports\pytest_coverage_postflight_20260408_131356.md coverage=90.14%; npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py WORKSPACE_STATUS.md DONELOG.md todo.root.md novapolis-dev/docs/donelog.md novapolis-dev/docs/todo.index.md novapolis-dev/docs/meta/dev-kpi-trends.md PASS; .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . --write-index-meta PASS; .\.venv\Scripts\python.exe scripts\check_doc_freshness.py --repo-root . PASS; .\.venv\Scripts\python.exe scripts\check_logs_policy.py --repo-root . PASS
---

<!-- markdownlint-disable MD041 -->

Dev-DONELOG (Current Window)
============================

Hinweis
-------

- Aktives Fenster: nur Eintraege der letzten 14 Tage mit operativer Relevanz.
- Historik bleibt vollstaendig in den Archivdateien unter `novapolis-dev/archive/docs/donelogs/` erhalten.
- Technische Laufdetails gehoeren in Reports unter `.tmp/results/reports/` und werden hier nur zusammengefasst.

Current-Window Eintraege
------------------------

Wochenabschluss: Nachgezogenen Abschlusslauf komplett gruen dokumentiert (2026-04-08 13:27)
---------------------------------------------------------------------------------------------

- `scripts/run_checks_and_report.py` liefert erneut `overall=PASS`; der neue Sammelbeleg liegt unter `.tmp/results/reports/checks_report_20260408_131224.md`, alle Pflichtgates einschliesslich `todo-index-sync`, `doc-freshness`, `logs-policy`, `ruff`, `black`, `pyright`, `mypy` und `pytest` sind gruen.
- Der separate Coverage-Lauf `scripts/run_pytest_coverage.py --fail-under 80` ist ebenfalls PASS; `.tmp/results/reports/pytest_coverage_postflight_20260408_131356.md` meldet `Total coverage: 90.14%` bei `518 passed, 1 warning`, damit sind Hard Gate und Qualitaetsziel zugleich gehalten.
- Der Sim-Offline-Check `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` endet weiterhin mit `summary=fail:0,warn:0`; mangels Strukturdelta mussten keine Tree-Artefakte neu erzeugt werden.
- Die Hygiene-Cadence bleibt bei `todo_index_drift=0`, `active_docs_stale=0`, `placeholder_conflicts=0` und `logs_policy_violations=0`; die Ableitung stuetzt sich auf den PASS-Block aus dem Full-Check, den separaten `check_logs_policy.py`-Direktlauf und das Fehlen offener Placeholder-/Truthfulness-Konflikte im aktiven Dev-Bestand. `novapolis-dev/docs/meta/dev-kpi-trends.md` fuehrt dafuer jetzt den Slot `S6`.
- `todo.root.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md`, `novapolis-dev/docs/todo.index.md` und `novapolis-dev/docs/meta/dev-kpi-trends.md` sind im selben Lauf synchronisiert.

Docs/Governance: Root-Steuerdoku gegen April-Iststand synchronisiert (2026-04-08 12:16)
------------------------------------------------------------------------------------------

- `WORKSPACE_STATUS.md` fuehrt jetzt die zuvor fehlenden 06./07.-April-Schritte des Text-RPG-Slice, statt nach dem Sim-Offline-Check direkt in den Maerz-Root-Cleanup zurueckzuspringen.
- `todo.root.md` referenziert jetzt den PASS-Lauf vom 2026-04-07 statt des veralteten Referenzstands vom 2026-03-27.
- `DONELOG.md` bleibt als Root-Summary auf knappe Root-Meilensteine fokussiert; `todo.index.md` fuehrt nur noch den aktuellen Board- und Gate-Stand, waehrend die Zwischenhistorie in diesem Dev-DONELOG verbleibt.
- Gezielte Doku-Pruefung nach dem Sync: markdownlint, Frontmatter-Validator, `check_todo_index_sync.py --write-index-meta` und `check_doc_freshness.py` sind PASS.

Agent/Typing: Kanonischen Typenrest in eval_utils und rag geschlossen (2026-04-07 20:57)
---------------------------------------------------------------------------------------

- `novapolis_agent/utils/eval_utils.py` und `novapolis_agent/utils/rag.py` fuehren die letzten JSON-/Mapping-Pfade jetzt ueber engere Listen- und Mapping-Casts statt ueber implizit unbekannte Objektwerte.
- Der frische Report `.tmp/results/reports/checks_types_20260407_205737.log` liefert fuer `pyright -p pyrightconfig.json` jetzt `0 errors, 0 warnings`; `mypy --config-file mypy.ini app scripts` bleibt ebenfalls gruen.
- `WORKSPACE_STATUS.md`, `todo.index.md`, `todo.agent-board.md`, `novapolis_agent/docs/DONELOG.txt` und `DONELOG.md` sind auf denselben Iststand nachgezogen; der zuvor noch getrennte Typenrest ausserhalb des Produktpfads ist damit ebenfalls geschlossen.

Agent/Typing: Produktpfad-Warnungen aus Pyright eingeengt (2026-04-07 18:35)
-------------------------------------------------------------------------

- `novapolis_agent/app/api/chat.py`, `app/api/sim.py`, `app/main.py` und `app/tts/providers.py` fuehren JSON-/Snapshot- und Cache-Payloads jetzt ueber engere Coercion- bzw. TypedDict-Pfade statt ueber implizit unbekannte Dict-Formen.
- Der erneute Agent-Typenlauf liefert fuer den aktiven Produktpfad keine Pyright-Warnungen mehr; uebrig bleiben nur noch getrennte Warnungen in `novapolis_agent/utils/eval_utils.py` und `novapolis_agent/utils/rag.py`, die bewusst ausserhalb dieses Produktpfad-Punkts liegen.
- `novapolis-dev/docs/todo.agent-board.md` fuehrt den Folgepunkt damit wieder als geschlossen, `novapolis-dev/docs/todo.index.md` setzt Agent auf `offen: 0`, und der gezielte Pytest-Block fuer Chat, Sim und TTS blieb gruen.

Dev/Typing: Kanonischen Typenpfad repariert und Full-Check wieder gruen (2026-04-07 17:20)
-------------------------------------------------------------------------------------------

- `scripts/checks_types.py` bindet Pyright und Mypy jetzt explizit an `novapolis_agent/pyrightconfig.json` und `novapolis_agent/mypy.ini` und fuehrt beide Kommandos mit `cwd=novapolis_agent` aus; `.vscode/tasks.json` startet denselben Wrapper wieder aus dem Repo-Root statt ueber ein implizites Modul-CWD.
- Der neue Postflight `.tmp/results/reports/checks_types_postflight_20260407_170654.md` zeigt `pyright=0` und `mypy=0`; der zuvor geoeffnete Dev-Punkt in `novapolis-dev/docs/todo.dev.md` ist damit wieder geschlossen und `novapolis-dev/docs/todo.index.md` setzt Dev zurueck auf `offen: 0`.
- Fuer den anschliessenden Gesamtbeleg wurden die unmittelbar betroffenen Portabilitaets- sowie Ruff-/Black-Reste nachgezogen; `.tmp/results/reports/checks_report_20260407_171142.md` liefert den kanonischen Full-Check jetzt wieder vollstaendig PASS.

Dev/Typing: Kanonischen Typenpfad als offenen Infrastrukturrest wieder sichtbar gemacht (2026-04-07 16:55)
---------------------------------------------------------------------------------------------------------

- `scripts/checks_types.py` laeuft aktuell nicht auf derselben Konfigurationsbasis wie der Agent-Scoped Typenpfad: Der Wrapper startet von Repo-Root und ruft `pyright -p pyrightconfig.json` sowie `mypy --config-file mypy.ini` auf, obwohl die realen Config-Dateien nur unter `novapolis_agent/` liegen.
- Der Beleg liegt in `.tmp/results/reports/checks_types_20260407_165332.log` und dem zugehoerigen Postflight: Pyright faellt bereits an einer nicht lesbaren Config-Datei am Repo-Root, Mypy mit `Cannot find config file 'mypy.ini'`; der Workspace-Task `Checks: types (pyright+mypy)` ist damit aktuell kein verifizierbarer Gate-Lauf.
- `novapolis-dev/docs/todo.dev.md` fuehrt die Reparatur deshalb wieder als offenen `Jetzt`-Punkt, und `novapolis-dev/docs/todo.index.md` hebt den Dev-Open-Count entsprechend von `0` auf `1`.

Root/Meta: Slice-, Product-Gate- und Beta-Pfad auf den belegten Produkt-Iststand verdichtet (2026-04-07 16:28)
-----------------------------------------------------------------------------------------------------------------

- `todo.root.md` fuehrt den suiteweiten Metablock fuer `Spielstart Novapolis`, `Slice -> MVP -> Beta` und `spielbarer Kern vor Komfort` jetzt als geschlossen. Root verweist dabei nur noch auf die aktiven SSOTs `rp-start-chooser.ssot.md`, `text-rpg-session-contract-v1.md`, `text-rpg-product-gate-v1.ssot.md`, `standalone-beta-gates.ssot.md` sowie `novapolis_agent/docs/runbook.md`.
- `todo.index.md` zeigt dazu alle Modul-Boards `Dev`, `RP`, `Agent` und `Sim` auf `offen: 0`; der Root-Pfad fuehrt damit keine stale Meta-Forderung mehr neben einem bereits belegten Modul-Iststand.
- Die Schliessung bleibt rein synchronisierend: Es wurden keine neuen Runtime-Zusagen erfunden, sondern nur der bestehende Slice-, Gate- und Release-Stand auf Root-Ebene ohne Doppelpflege festgezogen.

RP/Audio: Live-Dialogpfad ueber produktiven Coqui-Runtime-Stand als geschlossen nachgezogen (2026-04-07 16:28)
-----------------------------------------------------------------------------------------------------------

- `novapolis_agent/app/main.py` und `novapolis_agent/app/tts/providers.py` fuehren Live-TTS bereits ueber den produktiven `coqui`-Provider mit Hash-Cache, Session-/Slot-/Kanalrahmen und sessionbezogenem Artefaktpfad `runtime/sessions/<session>/<channel>/...`; `novapolis_agent/docs/runbook.md`, `README.md` und `docs/DONELOG.txt` dokumentieren denselben Iststand.
- `novapolis-sim/scripts/Main.gd` wertet `tts_manifest` aus dem Sessionpfad bereits fuer Live-Audio aus und spielt passende Eintraege kanalbezogen ab; der RP-Punkt bleibt damit keine theoretische Nacharbeit mehr, sondern ist am aktiven Produktpfad belegt.
- `todo.rp.md` fuehrt den Punkt jetzt als geschlossen, `todo.index.md` senkt den RP-Open-Count von `1` auf `0`; offene Board-Reste verbleiben damit nur noch auf Root-Ebene.

RP/Audio: OGG-Summary-Kandidaten ueber slot 00-30 als SSOT markiert (2026-04-07 16:28)
--------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-ogg-summary-kandidaten-slot-00-30.ssot.md` markiert jetzt die ersten belastbaren Build-Time-Kandidaten fuer `world`- und `pc`-Summaries entlang des bestehenden Produktpfads. Priorisiert sind nur Handover-, Kontakt- und Episodenkanten wie `slot 01`, `04`, `08`, `09`, `15`, `20`, `25` und `30`; die restlichen Stunden bleiben bewusst ohne Audio-Pflicht.
- Die Ableitung bleibt strikt an den bestehenden Slot-SSOTs `00-05`, `06-10`, `11-15`, `16-20`, `21-25` und `26-30` sowie am vorhandenen Audio-Namensschema `epoch{dd}_slot{hh}_{channel}.ogg`; Build-Time-Kandidaten und spaetere Live-Dialoge werden bewusst getrennt.
- `todo.rp.md` fuehrt den Kandidatenpunkt jetzt als geschlossen, `todo.index.md` senkt den RP-Open-Count von `2` auf `1`; als letzter RP-Rest bleibt nur noch der spaetere Runtime-Punkt fuer Live-Dialoge mit Cache.

Sim/Runtime: Clean-Checkout-Bootstrap und warnungsfreier Offline-Asset-Check geschlossen (2026-04-07 15:55)
----------------------------------------------------------------------------------------------------------------

- `scripts/check_sim_epoch_assets.py` wertet `--allow-empty` jetzt nicht mehr als Restwarnung, sondern als kanonisches Clean-Checkout-Profil. Fehlende `epochNN`-Ordner und fehlende OGG-Dateien werden in diesem Profil als `INFO` statt `WARN` berichtet; der aktuelle Lauf `--repo-root . --allow-empty --check-slot-consistency` endet damit mit `summary=fail:0,warn:0`.
- `novapolis-sim/README.md` trennt denselben Minimalstand jetzt explizit vom Vollstand-Pfad ohne `--allow-empty` und dokumentiert die Bootstrap-Zielorte `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` fuer spaetere Offline-Artefakte.
- `todo.sim.md`, `todo.index.md`, `todo.root.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` sind im selben Lauf synchronisiert; der Sim-Open-Count sinkt von `2` auf `0`.

Sim/Runtime: Live-Spielclient-Basis im Hub geschlossen (2026-04-07 15:43)
-----------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` nutzt den bestehenden Hub jetzt nicht mehr nur als freien Chat, sondern als minimalen Live-Spielclient: `_on_hub_chat_send_pressed()` sendet Spielereingaben mit Sessionrahmen an `/chat`, `_refresh_hub_chat_ui()` zeigt Session, Slot/Scene, Szene, Konsequenz, Optionen, State-Patches und Protokoll direkt im Panel, und die Response-Callbacks ziehen den sichtbaren Stand anschliessend ueber denselben Sessionvertrag nach.
- Die bereits geschlossene Replay-/Epoch-Bridge bleibt dabei dieselbe Datenbasis: `_on_hub_chat_request_completed()` und `_on_hub_session_request_completed()` halten Chat-Ansicht und Session-Logs zusammen, statt freie Chat-Ausgabe und statische Epoch-Dateien parallel zu fuehren.
- `todo.sim.md`, `todo.index.md` und `DONELOG.md` sind im selben Lauf synchronisiert; der Sim-Open-Count sinkt von `3` auf `2`.

Sim/Runtime: Session-Bridge fuer Replay-/Epoch-Ansicht und Audio-Verfuegbarkeit geschlossen (2026-04-07 15:32)
-----------------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` zieht den aktuellen Sessionstand jetzt ueber `GET /session/{session_id}` vom bestehenden Sim-API-Host nach, mappt `world_log` und `pc_log` direkt in die vorhandene Epochenansicht und uebernimmt `slot_id`, `slot_index`, Resume-Checkpoint und `artifact_paths` aus demselben Sessionvertrag statt nur `res://data/epochs` zu lesen.
- Der Hub-Reload triggert denselben Session-Sync nach erfolgreichen `/chat`-Antworten und per `Neu laden`; `content`-basierte Logeintraege, `slot_id`-Strings und `tts_manifest`-Artefakte werden dabei direkt fuer die Sim-Oberflaeche ausgewertet, sodass Audio-Verfuegbarkeit aus dem Live-Sessionpfad statt nur aus Offline-Assets erkennbar ist.
- `todo.sim.md`, `todo.index.md`, `novapolis-sim/README.md` und `DONELOG.md` sind im selben Lauf synchronisiert; der Sim-Open-Count sinkt von `4` auf `3`.

Agent/Runtime: Session-Roundtrip und Session-TTS im Text-RPG-Slice geschlossen (2026-04-07 13:18)
--------------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/chat.py` zieht bei aktiviertem Orchestrator jetzt den bestehenden Resume-/Replay-Stand als internen Block `[Session-Stand intern]` ein, parst `State_Patches:` aus der Modellantwort und schreibt `pc_log` plus normalisierte `state_patches` ueber `novapolis_agent/app/api/sim.py` in denselben Session-Store zurueck.
- `novapolis_agent/app/api/tts_models.py`, `novapolis_agent/app/main.py` und `novapolis_agent/app/tts/providers.py` heben denselben Session-/Slot-/Kanalrahmen in `/tts/synthesize`, Cache-Key, TTS-Manifest und den sessiongebundenen Coqui-Artefaktpfad `runtime/sessions/<session>/<channel>/...`; `novapolis_agent/tests/test_tts_api_contract.py`, `test_tts_cache_contract.py`, `test_tts_provider_abstraction.py` und `test_openapi_contract.py` sichern den Schnitt ab.
- `novapolis_agent/docs/runbook.md`, `todo.agent-board.md`, `todo.index.md`, `novapolis_agent/docs/DONELOG.txt` und `DONELOG.md` sind im selben Lauf synchronisiert; der Agent-Open-Count sinkt von `2` auf `0`.

Agent/Eval: Dedizierte GM-Session-Suite mit Severity-Report eingefuehrt (2026-04-07 12:44)
--------------------------------------------------------------------------------------------

- `novapolis_agent/eval/config/suites.json` fuehrt jetzt `gm_session` als eigene Spielleiter-Suite; `novapolis_agent/eval/datasets/rpg/rpg_gm_session_core.v1.jsonl` prueft Kontinuitaet, Reveal-Disziplin, Optionsqualitaet und Patch-Lesbarkeit auf demselben Session-/Slot-Pfad.
- `novapolis_agent/scripts/run_eval.py` spiegelt `slug`, `category` und `tags` jetzt in `results_<timestamp>*.jsonl`; `novapolis_agent/scripts/summarize_gm_eval_kpis.py` trennt Blocker-Faelle von Beobachtungen und referenziert dieselben Case-Metadaten fuer Board-Triage.
- `.vscode/tasks.json`, `tests/scripts/test_summarize_gm_eval_kpis.py`, `tests/scripts/test_run_eval_result_metadata.py`, `novapolis_agent/docs/runbook.md`, `todo.agent-board.md` und `todo.index.md` sind im selben Lauf darauf synchronisiert; der Agent-Open-Count sinkt von `3` auf `2`.

Agent/Runtime: Contract-Rahmen fuer Chat-Response, Savegame und Replay angehoben (2026-04-07 10:42)
------------------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/models.py` fuehrt fuer `/chat` jetzt einen expliziten Contract-Block mit `contract_version`, Session-/Slot-Metadaten, `session_status`, `replay_checkpoint_id` und `log_channels`; `novapolis_agent/app/api/chat.py` fuellt denselben Rahmen im bestehenden Produktpfad.
- `novapolis_agent/app/api/sim.py` validiert den kanonischen Vertragswert `text_rpg_session_v1`, persistiert denselben Rahmen in `savegame.json` und `replay_manifest.json` und normalisiert `state_patches` auf Session-/Slot-/Tick-Kontext statt freier Patchanhaenge.
- `novapolis_agent/tests/test_models_chat_options.py`, `test_api_chat_internal_branches.py`, `test_api_sim_state.py`, `tests/tests_sim_api.py` und `test_openapi_contract.py` sichern die API-, Replay- und OpenAPI-Seite; `novapolis_agent/docs/runbook.md`, `todo.agent-board.md` und `todo.index.md` sind im selben Lauf synchronisiert.

RP/Planning: Modularen Folgekorridor `slot 26-30` als Anschluss hinter dem Episodenanker festgezogen (2026-04-07 10:33)
-----------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md` fuehrt jetzt die naechste Kampagnenstufe hinter `slot 25` als resume-faehigen Folgeblock ueber `D5/C6`, `G7` und die duennen Neutralraeume `E2/F1`, ohne freie Tiefennetz- oder Fraktionslogik zu erfinden.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-21-25.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` und `text-rpg-product-gate-v1.ssot.md` verweisen im selben Lauf auf denselben erweiterten Produktpfad bis `slot 30`; `todo.rp.md` fuehrt den Punkt als geschlossen, `todo.index.md` behaelt den RP-Open-Count bei `2`.
- Die verbleibenden RP-Open-Items bleiben bewusst die spaeteren TTS-/OGG-Folgepunkte; der Produktpfad selbst ist damit eine Stufe weiter festgezogen.

Agent/Docs: Session-/Replay-Bruecke und PR-Scope fuer den Text-RPG-Slice nachgezogen (2026-04-07 09:50)
-------------------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/sim.py` schreibt jetzt pro Session einen dateigestuetzten Artefaktkern `savegame.json`, `world_log.jsonl`, `pc_log.jsonl` und `replay_manifest.json` unter `novapolis_agent/tmp/sim_sessions/<session_id>/` und stellt denselben Stand ueber `PUT /session/{session_id}`, `GET /session/{session_id}` und `GET /session/{session_id}/replay` bereit.
- `novapolis_agent/tests/test_api_sim_state.py` und `tests/tests_sim_api.py` sichern Artefaktwrite, Reload, Resume-Checkpoint, Replay-Manifest und 404-Pfade; das Agent-Board schliesst damit den Replay-/Savegame-Punkt und `todo.index.md` reduziert den Agent-Open-Count von `4` auf `3`.
- `novapolis_agent/docs/runbook.md` dokumentiert den neuen Betriebsweg, und `PR_DESCRIPTION.md` spiegelt jetzt den realen Branch-Scope fuer den Text-RPG-Slice statt der veralteten Draft-Beschreibung.

Agent/Sim: Orchestrator-Kontext gebuendelt und Hub zum Live-Spielclient gehoben (2026-04-07 09:14)
-----------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/models.py` fuehrt fuer den Orchestrator jetzt zusaetzlich `retrieval_query`; `novapolis_agent/app/api/chat.py` faltet bei aktiviertem Spielleiter-Pfad Kontextnotizen und RP-/Projekt-Retrieval in denselben Systemblock und vermeidet dort die getrennten `[Kontext-Notizen]`-/`[RAG]`-Bloecke.
- `novapolis_agent/tests/test_api_chat_internal_branches.py` und `test_models_chat_options.py` sichern die gebuendelte Injektion und das erweiterte Optionsschema; der gezielte Pytest-Lauf fuer beide Dateien sowie ein gezielter Ruff-Check auf den geaenderten Python-Dateien liefen gruen.
- `novapolis-sim/scripts/Main.gd` nutzt das bestehende Hub-Panel jetzt als minimalen Live-Spielclient: Session-ID, Slot-/Turn-Rahmen, `public_context`, `state_patch_hints` und `retrieval_query` werden an `/chat` gesendet, und Antworten werden im Panel als `Szene/Konsequenz/Optionen/State-Patches` aufgefaehrt; `todo.agent-board.md`, `todo.sim.md`, `todo.index.md`, `novapolis_agent/docs/runbook.md`, `novapolis_agent/docs/DONELOG.txt` und `DONELOG.md` sind im selben Lauf synchronisiert.

Agent/Runtime: Minimaler Spielleiter-Orchestrator-Hook gestartet (2026-04-06 06:57)
-------------------------------------------------------------------------------

- Die lokale Root-`.env` ist fuer den aktiven Lauf jetzt ebenfalls auf `qwen2.5:7b` nachgezogen.
- `novapolis_agent/app/api/models.py` fuehrt opt-in Felder fuer Sitzungsrahmen, `public_context`, `hidden_context`, Scheduler- und Patch-Hinweise; `novapolis_agent/app/api/chat.py` injiziert daraus einen ersten kontrollierten Systemblock in `/chat` und `/chat/stream`.
- `novapolis_agent/tests/test_models_chat_options.py` und `novapolis_agent/tests/test_api_chat_internal_branches.py` sichern den Hook; `novapolis_agent/docs/runbook.md`, `novapolis-dev/docs/todo.agent-board.md` und `novapolis-dev/docs/todo.index.md` sind im selben Lauf nachgezogen.

Agent/Runtime: Lokale Baseline `Ollama + qwen2.5:7b` festgezogen (2026-04-06 05:42)
------------------------------------------------------------------------------------

- `novapolis_agent/app/core/settings.py` fuehrt `qwen2.5:7b` jetzt als Default- und Fallback-Modell, waehrend `Ollama` die kanonische lokale Runtime bleibt.
- Die Root-`.env.example` sowie `novapolis_agent/README.md` und `novapolis_agent/docs/runbook.md` fuehren denselben 8-GB-VRAM-Betriebsstandard und halten `llama3.1:8b` nur noch als Vergleichs- oder Fallback-Kandidaten lesbar.
- `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.index.md` und `novapolis_agent/docs/DONELOG.txt` sind im selben Lauf synchronisiert.

Docs/Planning: Sessionvertrag v1, Product Gate v1 und Kampagnenkorridor `slot 21-25` festgezogen (2026-04-06 00:46)
--------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` definiert jetzt den kanonischen Session- und Kampagnenvertrag des ersten spielbaren Slice mit `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id`, `state_patches` und den Log-Kanaelen `world|pc|ally|sys`.
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` fuehrt den verbindlichen End-to-End-Gate-Namen `Text-RPG Product Gate v1` samt Gate-Stufen und aktuellem Task-Block `Checks: full` -> `Tests: pytest (api+streaming)` -> `Checks: sim epoch assets`.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-21-25.ssot.md` fuehrt den Produktpfad hinter `slot 20` ueber `E2/F1`, Rueckkopplung und episodischen Uebergabeanker weiter; `todo.agent-board.md`, `todo.dev.md`, `todo.rp.md`, `todo.index.md`, `novapolis_agent/docs/runbook.md`, `novapolis_agent/docs/DONELOG.txt` und das RP-Startpaket sind im selben Lauf synchronisiert.

RP/Planning: Neutralstarts `E2/F1` plus F1-Klarstellung in `C6` geschlossen (2026-04-05 19:33)
-----------------------------------------------------------------------------------------------

- `C6.md` fuehrt `F1` jetzt nicht mehr als stationslosen Codename gegen den aktiven T0-Stand, sondern als realen Knoten mit unbelegtem direktem C6-Pfad.
- `novapolis-rp/database-rp/03-locations/E2.md` und `F1.md` sowie `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-e2.ssot.md` und `rp-startbogen-freie-gruppen-f1.ssot.md` heben beide auf eigenstaendige `full_slice`-Neutralstarts.
- `rp-startgebiete-reveal-matrix.ssot.md`, `rp-start-chooser.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `todo.rp.md` und `todo.index.md` sind im selben Lauf synchronisiert; ein anschliessender Crossref-Fix begrenzt `connections` auf bereits dokumentierte Nachbar-SSOTs; der RP-Open-Count bleibt bei `2`.

RP/Planning: Neutralstartboegen `C1/D1` geschlossen (2026-04-05 19:24)
---------------------------------------------------------------------

- `novapolis-rp/database-rp/03-locations/C1.md` und `D1.md` geben zwei weiteren aktiven Neutralraeumen konservative Orts-SSOTs auf Basis der T0-Topologie `C2-C1-D1-D2`.
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-c1.ssot.md` und `rp-startbogen-freie-gruppen-d1.ssot.md` heben beide Raeume auf eigenstaendige `full_slice`-Neutralstarts, ohne lokale Crews oder implizite Rechte zu erfinden.
- `rp-startgebiete-reveal-matrix.ssot.md`, `rp-start-chooser.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `todo.rp.md` und `todo.index.md` sind im selben Lauf synchronisiert; der RP-Open-Count bleibt bei `2`.

RP/Planning: Neutralstartboegen `B1/C3` und Kampagnen-Folgekorridor `slot 16-20` geschlossen (2026-04-05 19:19)
----------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-b1.ssot.md` und `rp-startbogen-freie-gruppen-c3.ssot.md` geben dem fraktionslosen Pfad jetzt zwei weitere konkrete `full_slice`-Starts auf neutralen Pufferstationen, ohne lokale Crews oder Rechte frei zu erfinden.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-16-20.ssot.md` fuehrt den Produktpfad hinter `slot 15` in eine erste Kampagnenfolge fuer Innen-, Aussen- und Mobilitaetspfad weiter.
- `rp-start-chooser.ssot.md`, `rp-folgekorridor-slot-11-15.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `todo.rp.md` und `todo.index.md` sind im selben Lauf synchronisiert; der RP-Open-Count bleibt bei `2`.

RP/Planning: Langzeit-Folgekorridor `slot 11-15` und neutrale Puffer-SSOTs `A2/B1/C3` geschlossen (2026-04-05 18:49)
-----------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-11-15.ssot.md` fuehrt den Produktpfad hinter `slot 10` auf erste Langzeitfolgen fuer Innenpfad, Aussenkontakt und neutralen Mobilitaetspfad weiter.
- `novapolis-rp/database-rp/03-locations/A2.md`, `B1.md` und `C3.md` geben den ersten neutralen Pufferstationen konservative Orts-SSOTs aus T0-Topologie, Startboegen und den belegten Anschlusskanten `A1-A2-B1-B2-C3-D3`.
- `rp-startbogen-freie-gruppen-a2.ssot.md`, `rp-startgebiete-reveal-matrix.ssot.md`, `rp-folgekorridor-slot-06-10.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `todo.rp.md` und `todo.index.md` sind im selben Lauf synchronisiert; der RP-Open-Count bleibt bei `2`.

RP/Planning: Reveal-Raum weiterer Startgebiete und Folgekorridor `slot 06-10` geschlossen (2026-04-05 11:34)
------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md` zieht die Reveal- und Wissensgrenzen fuer `A1`, `B2`, `H12`, `F9`, `K4`, `G7` und `A2` auf dieselbe SSOT-Ebene wie den Novapolis-Startkorridor; rohe Innenlagen und verdeckte Fraktionsziele bleiben dabei weiter strikt aus dem PC-Text heraus.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-06-10.ssot.md` fuehrt den ersten Produktpfad hinter `slot 05` auf echte Folge-Slots fuer Nordlinie, Materiallauf `D5 -> C6`, C6-Empfang/Verteilung, G7-Aussenkontakt und die anschliessende Schwerpunktwahl weiter.
- `rp-folgekorridor-slot-00-05.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `todo.rp.md` und `todo.index.md` sind im selben Lauf synchronisiert; der RP-Open-Count bleibt bei `2`.

RP/Planning: Slot-00-05 kanonisiert und lokale Tiefenschaerfe der Full-Slice-Kerne angezogen (2026-04-05 10:53)
---------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-00-05.ssot.md` fixiert jetzt den ersten spielbaren Folgekorridor mit primaerer Linse, Konsequenzklassen, Fail-Forward und Persistenzvertrag gegen `Missionslog-Novapolis.md`, `Nordlinie-01.md`, `D5.md`, `C6.md` und die Reveal-Matrix.
- `A1.md`, `H12.md`, `B2.md`, `F9.md` und `K4.md` fuehren jetzt konservative Status-, Infrastruktur- und Tiefenschaerfe-Bloecke statt reiner `tbd`-Huelle; die zugehoerigen Startboegen `A1/H12/B2/F9/K4` sowie `G7` benennen Mind-Cluster-Anbindung, Unterraeume und Nebenstart-Hooks.
- `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `todo.rp.md` und `todo.index.md` sind im selben Lauf synchronisiert; der RP-Open-Count sinkt von `3` auf `2`.

RP/Planning: Erweiterter Mind-Cluster-Rollout fuer Anschlusscast und externe Full-Slice-Kerne geschlossen (2026-04-05 10:32)
------------------------------------------------------------------------------------------------------------------

- Neue Mind-Cluster-SSOTs fuer `Arlen`, `Lumen`, `Marven`, `Marei`, `Lyra` und `Senn` schliessen die bislang verbleibenden beziehungsnahen Luecken im direkten Novapolis-Anschlussraum; die zugehoerigen Charakterdateien verweisen jetzt auf diese Cluster statt auf doppelte Signatur-/Beziehungsbloecke.
- `novapolis-rp/database-rp/01-factions/arkologie-a1/07-mind-clusters/`, `eisenkonklave/07-mind-clusters/`, `schienenbund/07-mind-clusters/`, `schattenbund/07-mind-clusters/` und `fluesterkollektiv/07-mind-clusters/` fuehren jetzt die Kernfiguren der Full-Slice-Starts `A1/B2/H12/F9/K4` als eigene Cluster-SSOTs; die Charakterdateien dieser Kerne tragen jeweils einen expliziten Verweis.
- `rp-startbogen-novapolis-d5.ssot.md`, `rp-startbogen-novapolis-c6.ssot.md`, `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `todo.rp.md` und `todo.index.md` sind im selben Lauf auf den erweiterten Rollout synchronisiert; der RP-Open-Count bleibt bei `3`.

RP/Planning: Startkorridor-Unterbau aus Mind-Clustern, Scheduler-Daten und Reveal-Matrix geschlossen (2026-04-05 08:10)
-----------------------------------------------------------------------------------------------------------------

- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/reflex-mind-cluster.md`, `jonas-merek-mind-cluster.md`, `pahl-brenner-mind-cluster.md`, `kora-malenkov-mind-cluster.md` und `echo-mind-cluster.md` ziehen den fehlenden Mind-Cluster-Rollout fuer den Kerncast nach; die zugehoerigen Charakterdateien verweisen jetzt auf diese Cluster statt auf doppelte Beziehungs-/Verhaltensbloecke.
- `D5.md`, `C6.md`, `Nordlinie-01.md` sowie die Kernfiguren `Ronja`, `Reflex`, `Jonas`, `Pahl`, `Kora` und `Echo` fuehren jetzt startkorridor-taugliche `knowledge`-/`actions`-Bloecke mit Reveal-Kanaelen, Voraussetzungen, Outputs und Risiken.
- `novapolis-dev/docs/process/rp-startkorridor-reveal-matrix.ssot.md` fixiert die Klassen `pc_visible`, `allies_only`, `npc_only`, `world_only`, `rumor` und `log/reflex` samt Reveal-Pfaden und Guardrails fuer `D5/C6/Nordlinie`.
- `rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `todo.rp.md` und `todo.index.md` sind im selben Lauf synchronisiert; der RP-Open-Count sinkt von `6` auf `3`.

RP/Planning: Restliche Fraktionskerne als eigene Minimal-Startboegen festgezogen (2026-04-05 08:03)
----------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-startbogen-arkologie-a1.ssot.md`, `rp-startbogen-schienenbund-b2.ssot.md`, `rp-startbogen-eisenkonklave-h12.ssot.md`, `rp-startbogen-schattenbund-f9.ssot.md` und `rp-startbogen-fluesterkollektiv-k4.ssot.md` definieren jetzt fuer `A1/B2/H12/F9/K4` je einen belastbaren Minimalstart mit Startkern, Stakes, Entscheidungsraum, Fail-Forward und Guardrails.
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md` fuehrt damit alle derzeit freigegebenen Kernstationen als `full_slice`; das fruehere `framing_start` fuer diese fuenf Knoten ist geschlossen.
- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` fuehrt die neuen Boegen jetzt direkt im Startpaket-Kontext mit.
- `todo.rp.md` schliesst den offenen Folgepunkt fuer die restlichen Fraktionskerne; `todo.index.md` zieht den RP-Open-Count auf `6` nach.

RP/Planning: D5-Defaultstart und C6-Parallelslice als eigene SSOTs festgezogen (2026-04-05 07:51)
-----------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md` definiert jetzt den kanonischen Default-Start in D5 mit Ronja, Reflex, Jonas und Pahl.
- `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md` zieht `C6` als eigenstaendigen Novapolis-Start mit Kora, Echo, Sicherungsdruck und gefiltertem Reveal nach.
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md` fuehrt `novapolis_d5` und `novapolis_c6` jetzt beide als `full_slice`; das fruehere offene Startpaket in `todo.rp.md` ist geschlossen.
- Im selben Lauf wurde als sichtbarer Nachfolger ein neuer RP-Punkt fuer die verbleibenden Fraktionskerne `A1/B2/H12/F9/K4` geoeffnet; der RP-Open-Count bleibt dadurch bei `7`.

RP/Planning: Start-Chooser, Neutralstart und erster externer Fraktionsstart festgezogen (2026-04-05 07:09)
----------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-start-chooser.ssot.md` definiert jetzt die aktive Startauswahl mit `novapolis_default`, `faction_start`, `factionless_start`, `neutral_start`, Gebietsklassen, Dichtegraden und Reveal-Guardrails.
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md` liefert den ersten fraktionslosen Neutralstart ueber `Freie Gruppen` in `A2`.
- `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md` hebt `G7` mit `Marven`, `Arlen` und H-47-Kontext auf einen echten externen Fraktionsstart.
- `todo.rp.md` schliesst damit den Folgepunkt fuer mindestens einen externen und einen fraktionslosen Startbogen; `todo.index.md` zieht den RP-Open-Count von `8` auf `7` nach.

RP/Planning: Mehrere Startoptionen, fraktionsloser Pfad und freie Gebietswahl verankert (2026-04-05 07:01)
---------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` fuehrt jetzt neben dem Default-Slice `Ronja/Reflex in D5` auch `Fraktionsstart`, `Fraktionslos / Freie Gruppen` und `Neutralstart` als evidence-first Startklassen.
- Die Erweiterung stuetzt sich direkt auf `Fraktionen-Taxonomie.md`, `Stationskontroll-Matrix.md`, `Metrokarte-T0.md`, `Freie-Gruppen-inventar.md` sowie die belegten Fraktionsknoten `G7`, `H12`, `A1`, `B2`, `F9`, `K4`.
- `todo.rp.md` fuehrt Mehrfachstart, fraktionslosen Start und freie Gebietswahl jetzt als feste Anforderungen des Startpakets; ein neuer Folgepunkt zieht externe Fraktionsstarts und den Neutralstart spaeter von `Rahmenstart` auf echte Startboegen.
- `todo.index.md` zieht den RP-Open-Count dafuer von `7` auf `8` nach.

RP/Planning: Startpaket und Slot-00-05-Korridor als Arbeitsblatt zerlegt (2026-04-05 06:52)
--------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` fuehrt jetzt den ersten spielbaren Novapolis-Slice evidence-first zusammen: Primärlinse `Ronja/Reflex in D5`, Parallelfaden `Kora/Echo in C6`, Reveal-Grenzen, Konsequenzklassen und die Arbeitsfenster `slot 00-05`.
- `todo.rp.md` referenziert dieses Arbeitsblatt direkt in den offenen Punkten fuer Startpaket, Mind-Cluster-Rollout, Knowledge-/Actions-Abdeckung, Reveal-Matrix und Mehrslot-Korridor.
- `todo.index.md` zieht den neuen RP-Statushinweis im selben Lauf nach; der RP-Open-Count bleibt bewusst bei `7`, weil in diesem Lauf Planungstiefe und nicht Umsetzung geschlossen wurde.

Docs/Planning: Produktpfad zum KI-geleiteten Text-RPG ueber die aktiven Boards zerlegt (2026-04-03 10:53)
---------------------------------------------------------------------------------------------------------

- `todo.root.md` fuehrt jetzt einen suiteweiten Produktpfad mit vertikalem Slice, MVP/Beta-/Release-Stufen und der Priorisierung `spielbarer Kern vor Weltbreite/Komfort`.
- `todo.dev.md` fuehrt den fehlenden End-to-End-Produkt-Gate-Pfad vom RP-Kontext ueber Agent-Session und State-Logs bis zur Sim-/Replay-Sicht als neuen offenen Dev-Punkt.
- `todo.agent-board.md`, `todo.rp.md` und `todo.sim.md` fuehren jetzt erstmals die eigentlichen Produktluecken fuer Spielleiter-Orchestrierung, Startpaket/Sphaeren-SSOT sowie Live-Spielclient/Replays statt nur isolierter Rest- oder Hygienepunkte.
- `todo.index.md` zieht Open-Counts, Statushinweise und Board-Metadaten im selben Lauf auf den neuen Produktpfad nach.

RP/Spec: Skill-Mapping-V1 gegen aktive RP-Pfade gegengeprueft (2026-04-02 05:32)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/specs/annotation-spec.md` dokumentiert jetzt den Realabgleich fuer den belegten Missionspfad `D5 -> C6` mit `Ronja`/`Reflex`, fuer `Pahl` als faktisches D5-Interimkommando und fuer `Kora`/`Echo` im C6-Schutz-/Logistikkontext.
- Die konservativen Baselines bleiben bestehen; nur fuer `Pahl` ist jetzt ein szenengebundener Kontext-Lift `funk +1`, `wache +1` dokumentiert, wenn D5 explizit unter seinem Freigabe- und Sicherheitskommando laeuft.
- `todo.rp.md` markiert den Realabgleich damit als abgeschlossen, `todo.index.md` zieht den RP-Open-Count im selben Lauf von `3` auf `2` nach.

RP/Inventory: Fluesterkollektiv mit belegtem Minimalrahmen vertieft (2026-04-01 00:53)
------------------------------------------------------------------------------------

- `Relationslog-Fluesterkollektiv.md` fuehrt jetzt nicht mehr nur `tbd`, sondern den belastbaren Minimalstatus `Novapolis = unbekannt` aus dem aktiven Gegenlog von Novapolis.
- `Handelslog-Fluesterkollektiv.md` und `Missionslog-Fluesterkollektiv.md` dokumentieren jetzt denselben konservativen Rahmen indirekter Tausch- und Informationskanaele ueber `Corin -> Sera -> Iris` statt einer reinen Stub-Huelle.
- `Fluesterkollektiv-inventar.md` uebernimmt denselben Aussen- und Kanalrahmen in die Inventarlage; benannte Gegenparteien, Routen und Mengen bleiben bewusst `tbd`.

RP/Inventory: Schattenbund mit belegtem Relations- und Beschaffungsrahmen vertieft (2026-04-01 00:39)
-----------------------------------------------------------------------------------------------------

- `Relationslog-Schattenbund.md` fuehrt jetzt nicht mehr nur `tbd`, sondern die belegte Aussenlage `Novapolis = unbekannt`, `Eisenkonklave = feindselig`, `Arkologie = verdeckt`.
- `Handelslog-Schattenbund.md` und `Missionslog-Schattenbund.md` dokumentieren jetzt denselben konservativen Rahmen verdeckter Beschaffungsfenster ueber Zwischenhaendler und gestaffelte Uebergaben statt einer reinen Stub-Huelle.
- `Schattenbund-inventar.md` uebernimmt denselben Aussen- und Beschaffungsrahmen in die Inventarlage; die Kette `Jarek -> Sera -> Nyra` ist sichtbar, Mengen, Routen und benannte Gegenparteien bleiben bewusst `tbd`.

RP/Inventory: Arkologie-A1 mit belegtem Haendlergilden- und Konfliktrahmen vertieft (2026-03-31 18:22)
---------------------------------------------------------------------------------------------------

- `Relationslog-Arkologie-A1.md` fuehrt jetzt nicht mehr nur `tbd`, sondern die belegte Aussenlage `Haendlerbund = beschraenkt`, `Eisenkonklave = umkaempft`, `Novapolis = unbekannt`.
- `Handelslog-Arkologie-A1.md` und `Missionslog-Arkologie-A1.md` dokumentieren jetzt denselben konservativen Haendlergilden-Kanal unter Sicherheits- und Biosicherheitsauflagen statt einer reinen Stub-Huelle.
- `Arkologie-inventar.md` uebernimmt denselben Aussenrahmen in die Inventarlage; Handels-, Konflikt- und Sicherheitskette `Nera -> Borin -> Liora` ist sichtbar, Mengen und Routen bleiben bewusst `tbd`.

RP/Inventory: Eisenkonklave mit belegtem Händlerbund-Handelsrahmen vertieft (2026-03-31 18:12)
-----------------------------------------------------------------------------------------------

- `Missionslog-Eisenkonklave.md` fuehrt jetzt mit den gelegentlichen Händlerbund-Handelsfenstern den ersten belegten Missionsanker der Eisenkonklave ausserhalb des reinen T0-Rahmens.
- `Handelslog-Eisenkonklave.md` ist kein Stub mehr, sondern fuehrt jetzt den belegten Rahmen `handel_gelegentlich` sowie die Freigabekette `Kaspar Dorn -> Yara Kest`.
- `Eiserne-Enklave-inventar.md` uebernimmt denselben Handelsanker in die Inventarlage; Eigenklassen bleiben sichtbar, aber Dealmengen, Routen und Tauschlisten bewusst `tbd`.

RP/Inventory: Haendlerbund mit belegtem H-47/C6-Handelsanker vertieft (2026-03-31 17:50)
------------------------------------------------------------------------------------

- `Missionslog-Haendlerbund.md` fuehrt jetzt mit `H-47: Erstkontakt und Integration in C6` den ersten belegten Missionspfad des Haendlerbunds: dauerhafte Kooperation, `C6 als Handelsstuetzpunkt aktiviert`, geregelte Handelszyklen im Aufbau.
- `caravan-moves.md` fuehrt denselben Pfad als aktives Karawanenlog mit `G7 <-> C6`-Kontaktlinie, sekundärem `C6 <-> D5`-Handoff und den ersten belegten Austauschklassen statt einer fast leeren Planhülle.
- `Haendlerbund-inventar.md` übernimmt H-47, C6-Handelsstuetzpunkt, G7-Kontaktpunkt und die Austauschklassen in die Inventarlage; Mengen, Konvoi-Manifeste und Abrechnung bleiben bewusst `tbd`.

RP/Inventory: Externe Fraktionsinventare auf konservative T0-Rahmenwerte gezogen (2026-03-31 17:41)
-----------------------------------------------------------------------------------------------

- `Arkologie-inventar.md`, `Schienenbund-inventar.md`, `Haendlerbund-inventar.md` und `Eiserne-Enklave-inventar.md` fuehren jetzt nicht mehr nur leere `tbd`-Listen, sondern explizite, nicht quantifizierte T0-Rahmen fuer Grundversorgung, Austauschgüter, Reparatur-/Baukontext, Handelsraum oder Werkstoff-/Schutzgüter.
- `Schattenbund-inventar.md` und `Fluesterkollektiv-inventar.md` wurden auf denselben Rahmenstandard nachgezogen und führen jetzt ebenfalls eine explizite `Rahmenlage (T0)` plus `RAHMENWERT`-Logeintrag statt nur Baseline ohne Bezug zur aktuellen Warenmatrix.
- Der Schritt folgt exakt dem Arbeitsledger-Pfad `Externe Fraktionsinventare: nur rahmenwert bestaetigen; keine neue Mengensetzung ohne fraktionsscharfe Evidenz`; `todo.rp.md` und `todo.index.md` dokumentieren den Abschluss, der RP-Open-Count bleibt unverändert bei `3`.

RP/Inventory: Warenlauf D5 -> C6 und Delta-/Bilanzformat fuer Novapolis geschlossen (2026-03-31 08:46)
-------------------------------------------------------------------------------------------------

- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md` fuehrt den Lauf `D5 -> C6` jetzt nicht mehr nur generisch, sondern mit belegtem D5-Pack-/Entnahmeanker, D5-Abmeldung, Transport mit `ReflexAssist`, Eintreffen in C6, Bestandsaufnahme und Empfangsbestaetigung; Mengen, Charge und Lagerziel bleiben bewusst offen.
- `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md` und `C6-inventar.md` ziehen denselben konservativen Prozessanker jetzt standortscharf nach, ohne daraus freie Mengen oder stillschweigende Lagerbuchungen zu machen.
- `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md` fuehrt die Fraktionslage jetzt in den vier Pflichtdeltas `Transfer`, `Verbrauch`, `Bilanz`, `Handel` plus kompaktem Bedarfsblock; `todo.rp.md`, `todo.index.md`, `todo.root.md` und `DONELOG.md` schliessen den Waren-/Bedarfslauf im selben Zug.

RP/Inventory: Operatives Arbeitsledger fuer die finale Metro-Warenzuteilung verankert (2026-03-30 06:17)
------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` ueberfuehrt die vorhandene RP-Zuteilungsmatrix jetzt in drei operative Ledger-Tabellen `fix`, `rahmenwert` und `handentscheidung` statt nur in eine Vorbereitungslogik.
- Jeder Ledger-Eintrag fuehrt Station/Zielraum, Fraktion, sichtbaren Zielpfad und den beabsichtigten Updatepfad; fuer Novapolis sind damit `D5-inventar.md`, `C6-inventar.md`, `Novapolis-inventar.md` und `Missionslog-Novapolis.md` direkt ansteuerbar, fuer externe Fraktionen die jeweiligen Inventarseiten unter `novapolis-rp/database-rp/01-factions/*/04-inventory/`.
- `todo.rp.md`, `todo.index.md` und `todo.root.md` fuehren den Schritt im selben Lauf als geschlossen; offen bleiben jetzt nur noch die belastbare Transferkette `D5 -> C6`, die Delta-/Bilanzstruktur in `Novapolis-inventar.md` und der spaetere Realabgleich der offenen Handentscheidungen.

Dev/Docs: Nicht-kanonische Unterordner-READMEs im Stub-/Runbook-Scope umbenannt (2026-03-30 04:15)
-------------------------------------------------------------------------------------------------

- Umbenannt wurden die aktiven Unterordner-Dokus aus dem dokumentierten Hub-/Stub-/Tool-Scope, darunter `docs/adr/adr-index.md`, `novapolis_agent/scripts/scripts-overview.md`, `novapolis_agent/eval/eval-overview.md`, `novapolis_agent/eval/config/context.notes/context-notes-guide.md`, `novapolis-dev/logs/logs-policy.md`, `novapolis-dev/integrations/mcp-openai-eval/mcp-openai-eval-guide.md`, `novapolis-rp/coding/tools/validators/validator-suite.md`, `novapolis-rp/database-curated/curation-workflow.md` und `novapolis-rp/database-raw/99-exports/raw-export-policy.md`.
- Aktive Querverweise in `WORKSPACE_INDEX.md`, `DONELOG.md`, `todo.root.md`, `novapolis-dev/docs/readme_decisions.md`, `novapolis-dev/docs/readme.hub.md`, `novapolis-dev/docs/todo.dev.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-rp/database-rp/00-admin/Process-Workflow.md`, `novapolis-rp/database-rp/00-admin/Current-State.md`, `novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-history.md` sowie `.vscode/settings.json` zeigen jetzt auf die neuen Dateinamen; interne `checks:`-Selbstreferenzen der umbenannten Stubs wurden ebenfalls nachgezogen. Als Gate-Nachzug erzwingt `scripts/check_logs_policy.py` fuer den aktiven Logpfad jetzt den neuen kanonischen Namen `novapolis-dev/logs/logs-policy.md`.
- Bewusst unveraendert blieben die kanonischen Root-/Modul-Einstiege (`README.md` auf Root- und Modul-Ebene) sowie fachliche RP-Landingpages unter `novapolis-rp/database-rp/01-factions/**`, weil `novapolis-dev/docs/readme_decisions.md` diesen Renaming-Lauf auf Hub-, Stub-, Tool- und Runbook-Dokus begrenzt.

Agent/Data: Export-/Kurationspfad gegen historischen Results-Drift gehaertet (2026-03-30 01:21)
---------------------------------------------------------------------------------------------

- `novapolis_agent/scripts/export_finetune.py` inspiziert Results jetzt vor dem Export, leitet Dataset-Kandidaten aus Result-Metadaten und `source_file` ab, matched Item-IDs/Slugs resilienter und liefert bei `0` exportierbaren Datensaetzen einen expliziten Fehler mit Diagnostik (`successful_rows`, `exportable_count`, `unmapped_item_ids`) statt einer stillen Erfolgsantwort.
- `novapolis_agent/scripts/curate_dataset_from_latest.py` prueft `results_*.jsonl` newest-first auf Exportierbarkeit und nimmt das neueste kuratierbare Set; uebersprungene Drift-Kandidaten erscheinen als `skipped_results` im Bericht.
- Regressionen sind ueber gezielte Pytests fuer Export-/Curate-Edges und Smoke-Pfade abgesichert. Ein temp-basierter Real-Lauf gegen `novapolis_agent/eval/results/` waehlte kontrolliert `results_20260226_0306_quality_de_round7b_repeat3.jsonl` und erzeugte wieder `20` Export-Eintraege plus Pack-Split `train=18`, `val=2`.

Agent/Artifacts: Outputs-Cleanup als No-Op bestaetigt (2026-03-29 07:07)
-----------------------------------------------------------------------

- Der reale Cleanup-Lauf `novapolis_agent/scripts/cleanup_artifacts.py --target outputs --keep-latest 15` hatte unter der runbasierten Retention keine Remove-Kandidaten; Apply-Report `.tmp/results/reports/artifact_lifecycle_report_apply_outputs_20260329_0707.json` mit `keep=68`, `remove=0`, `removed=0`.
- Der direkte Post-Dry-Run auf denselben Zielpfad bestaetigt denselben Sollzustand ohne Restueberhang; Post-Check-Report `.tmp/results/reports/artifact_lifecycle_report_post_outputs_20260329_0707.json` mit `keep=68`, `remove=0`, `removed=0`.
- Damit bleibt `outputs/` nach der runbasierten Retention aktuell vollstaendig bestehen; echte Remove-Kandidaten lagen in diesem Pfad nicht mehr vor.

Agent/Artifacts: echter Eval-Results-Cleanup ausgefuehrt (2026-03-29 06:47)
--------------------------------------------------------------------------

- Der reale Cleanup-Lauf `novapolis_agent/scripts/cleanup_artifacts.py --target novapolis_agent/eval/results --keep-latest 15` hat im Agent-Resultpfad 1813 Dateien entfernt und 60 Artefakte behalten; der Maschinenreport liegt unter `.tmp/results/reports/artifact_lifecycle_report_apply_eval_results_20260329_0647.json`.
- Der direkte Nachlauf per erneutem Dry-Run auf denselben Zielpfad bestaetigt den Zielzustand ohne Restueberhang (`keep=60`, `remove=0`, `removed=0`); der Post-Check-Report liegt unter `.tmp/results/reports/artifact_lifecycle_report_post_eval_results_20260329_0647.json`.
- Der Cleanup wurde bewusst nur auf `novapolis_agent/eval/results` ausgefuehrt; `outputs/` und `novapolis_agent/outputs/` blieben in diesem Lauf unveraendert.

Agent/Artifacts: runbasierte Retention fuer Cleanup gehaertet (2026-03-29 06:45)
-----------------------------------------------------------------------------

- `novapolis_agent/scripts/cleanup_artifacts.py` gruppiert Artefakte jetzt fuer `novapolis_agent/eval/results` ueber Run-Zeitanker und fuer `outputs` ueber Laufordner/Top-Level-Eintraege statt pro Einzeldatei; Name-Pinning greift auf relativen Pfaden und reisst dadurch Baseline- oder Quality-DE-Artefakte nicht mehr auf Dateiebene auseinander.
- Neue Regressionstests in `novapolis_agent/tests/scripts/test_cleanup_artifacts.py` und `novapolis_agent/tests/scripts/test_cleanup_artifacts_edges.py` sichern Eval-Cluster, Output-Laufordner und Baseline-Pfade gegen Split-Retention ab; der erneute Dry-Run-Report unter `.tmp/results/reports/artifact_lifecycle_report.json` haelt `outputs/` jetzt komplett zusammen (`keep=68`, `remove=0`).
- `todo.agent-board.md` fuehrt den Fixpunkt im selben Lauf von offen auf erledigt, und `todo.index.md` bleibt fuer das Agent-Modul wieder bei genau einem offenen Folgepunkt (`Export-/Kurationspfad gegen historische Results-Drift`).

Root-Cleanup: Root-eval-Rest final bereinigt und post-check Stub erneut quarantanisiert (2026-03-28 06:32)
-------------------------------------------------------------------------------------------------------

- `novapolis_agent/app/core/settings.py`, `novapolis_agent/app/api/chat.py`, `novapolis_agent/scripts/open_context_notes.py` und die betroffenen Eval-Helfer fuehren Eval-, RAG- und lokale Kontext-Defaults jetzt konsistent ueber `novapolis_agent/eval/...`; `novapolis_agent/README.md` und die betroffenen Tests wurden im selben Lauf nachgezogen.
- Der urspruengliche Root-Ordner `eval/` liegt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0501-root-eval-rest/eval`; ein nach den Abschluss-Checks erneut entstandener lokaler Stub `eval/config/context.local.md` wurde zusaetzlich unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0632-root-eval-rest-postchecks/eval` abgelegt. Danach wurden `workspace_tree.txt`, `workspace_tree_dirs.txt` und `workspace_tree_full.txt` fuer den final bereinigten Root-Surface erneut neu erzeugt.

Root-Cleanup: lokale Editor-/Host-Snapshots aus dem Main-Root entfernt (2026-03-28 03:30)
----------------------------------------------------------------------------------------

- `extensions.installed.txt`, `extensions.status.txt` und `desktop.ini` liegen jetzt gesammelt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0330-local-snapshots/`; im aktiven Root bleiben damit nur noch die bewusst gehaltenen Governance-, Shim- und Strukturpfade.
- Die Root-Tree-Artefakte wurden nach dem Move direkt per Terminal neu erzeugt, weil die vorhandenen Tasks `Workspace tree:*` lokal weiterhin am bekannten `pwsh /d /c`-Fehlpfad mit Exit `64` scheitern.

Root-Cleanup: sichere Altartefakte aus dem Main-Root in Quarantaene ueberfuehrt (2026-03-28 03:12)
-----------------------------------------------------------------------------------------------

- `combined.json`, `lint.out`, `md003_scan.out`, `.tmp-datasets/` und `reports/` liegen jetzt gesammelt unter `novapolis-dev/archive/quarantine/root-cleanup-20260328_0238/`; die gleichnamigen Root-Pfade sind aus dem aktiven Single-Root-Surface entfernt.
- Bewusst unangetastet blieben die aktiven Kompatibilitaetspfade `app/__init__.py` und `utils/__init__.py` sowie der noch referenzierte Hinweis `eval/config/context.local.md`, damit der Cleanup nur belegte Altartefakte und keine aktiven Einstiegspfade verschiebt.

Governance/Postflight: `Todos.offen` auf TODO-Index umgestellt (2026-03-28 02:02)
--------------------------------------------------------------------------

- `.github/copilot-instructions.md` definiert `Todos.offen` im Postflight-Receipt jetzt als Summe der Modul-Open-Counts aus `novapolis-dev/docs/todo.index.md` statt als offene Agent-Arbeitsschritte des aktuellen Laufs.
- `todo.root.md` bleibt dabei bewusst ausserhalb der Zahl, weil der aktive Index den Root-Backlog nicht in die Modul-Open-Counts einrechnet.

Docs/Consistency Sweep: Board- und Index-Abschluss nachgezogen (2026-03-28 01:39)
-------------------------------------------------------------------------

- `todo.root.md` und `todo.dev.md` markieren den dokumentierten Stil- und Konsistenzlauf jetzt als erledigt; `todo.index.md` fuehrt Dev dazu wieder mit `offen: 0` und aktualisierter Statusnote.
- Der Sweep deckte Hochfrequenz-Dateien, aktive Dev-SSOTs und erste Modul-Runbooks ab; beim Restscan blieben nur ignorierte Drittanbieter-READMEs unter `node_modules` ausserhalb des aktiven Arbeitsbereichs uebrig.

Docs/Consistency Sweep: aktive Dev-Doku und erste Runbooks nachgezogen (2026-03-28 01:31)
-------------------------------------------------------------------------------

- Im aktiven Dev-Scope fuehren `architecture-summary-local-ai.md`, `tests.md`, `dataset-provenance.md`, `readme.hub.md`, `novapolis-dev/logs/logs-policy.md`, `process/abschluss-routine.ssot.md`, `process/standalone-beta-gates.ssot.md` und `specs/tts-exporter-coqui.md` jetzt keinen alten FAIL-Kontext mehr; Root-Wrapper und manuelle Pruefbeispiele sind vereinheitlicht.
- Als erste modulnahe Runbooks sind `novapolis_agent/scripts/scripts-overview.md` und `novapolis-rp/database-rp/06-scenes/scenes-guidelines.md` auf denselben PASS-/PowerShell-/Root-Wrapper-Rahmen gezogen.

Docs/Consistency Sweep: Root-README-Wrapperstil nachgezogen (2026-03-28 01:27)
-------------------------------------------------------------------------

- `README.md` nennt bei der Wrapper-Policy jetzt dieselben Root-`.venv`-Kommandos wie `WORKSPACE_STATUS.md` und die Modul-READMEs statt der alten Kurzform `python ...`.
- Damit ist der erste Hochfrequenz-Block des laufenden Phase-2-Sweeps im aktiven Reader-Surface ohne verbleibende harte Wrapper- oder Portabilitaetsdrift geschlossen.

Docs/Consistency Sweep: erste Hochfrequenz-Dateien nachgezogen (2026-03-28 01:23)
-------------------------------------------------------------------------

- `WORKSPACE_STATUS.md` nutzt jetzt portable Reportpfade und nennt die Root-Wrapper explizit statt alter `python ...`-Kurzformen.
- `WORKSPACE_INDEX.md` fuehrt den aktiven Phase-2-Sweep statt der alten Redirect-Phase; `novapolis-dev/README.md` verwendet in Archiv-/DONELOG-Matrix und Datenpfaden jetzt repo-relative Referenzen.
- `novapolis_agent/README.md` und `novapolis-sim/README.md` ziehen verbleibende Root-Kommandos, PowerShell-Beispiele und portable Godot-Aufrufe nach.

Docs/Plan: Stil- und Konsistenzlauf fuer aktive Doku vorab dokumentiert (2026-03-28 00:43)
----------------------------------------------------------------------------------------

- `todo.root.md` und `todo.dev.md` fuehren den naechsten Doku-Hygienelauf jetzt als expliziten offenen Punkt statt nur als Chat-Abrede.
- `novapolis-dev/docs/process/doku-konsistenzlauf-aktive-surface-2026-03-28.md` haelt Scope, Stilrahmen, Reihenfolge, Nicht-Ziele und DoD fest; `todo.index.md` spiegelt dazu Dev wieder mit `offen: 1`.

Docs/TODO-Index: Root und historische Nebenpfade klar getrennt (2026-03-28 00:36)
-------------------------------------------------------------------------------

- `todo.index.md` fuehrt `todo.root.md` jetzt explizit in der Uebersicht als Root-Backlog statt nur unten bei den Verweisen.
- Gleichzeitig markiert der Index die weiteren `todo*.md` unter `novapolis-dev/archive/**` und `novapolis-dev/archive/quarantine/**` ausdruecklich als historische, quarantänisierte oder Snapshot-Dateien und nicht als aktive Boards.

Docs/Reader-Surface: aktive Lesedokumente auf PASS-/Single-Root-Kontext gezogen (2026-03-28 00:28)
-----------------------------------------------------------------------------------------------

- `README.md`, `WORKSPACE_INDEX.md`, `novapolis-dev/README.md`, `novapolis_agent/README.md`, `novapolis-rp/README.md` und `novapolis-sim/README.md` fuehren jetzt keine veralteten FAIL-Header mehr, sondern den aktuellen PASS-Kontext des Wochenabschlusses vom 2026-03-27.
- Im Agent-README sind lokale `venv`- und Bash-Altpfade auf den Root-`.venv`-Pfad umgestellt; das RP-README nutzt keinen Sibling-Verweis `../novapolis_agent/` mehr, und das Sim-README trennt UI-Start sauber von optionalen Asset-Warnungen auf Clean-Checkout.
- `todo.dev.md` ist damit wieder geschlossen, `todo.root.md` markiert den Reader-Surface-Punkt als erledigt, und `todo.index.md` fuehrt Dev wieder mit `offen: 0`.

Docs/Boards: Folgepfade aus dem Modulreview explizit verankert (2026-03-28 00:22)
-------------------------------------------------------------------------------

- `todo.root.md` fuehrt den Suite-Backlog jetzt explizit fuer Dev-Reader-Surface, Agent-Exportpfad, RP-Zuteilungsledger und Sim-Bootstrap; der veraltete Root-Punkt zum TODO-Index-Drift wurde dadurch auf den aktuellen Iststand ersetzt.
- `todo.dev.md` fuehrt als neuen offenen Punkt die Reader-Surface-Synchronisation fuer Root/Dev und die vier Hauptmodule, weil mehrere aktive Oberflaechen noch Vor-Maerz-Receipts oder Altpfade zeigen.
- `todo.agent-board.md`, `todo.rp.md` und `todo.sim.md` fuehren jetzt je einen direkten Folgepfad aus der Analyse: Export-/Kurationsrobustheit, operatives RP-Zuteilungsledger und Clean-Checkout-Bootstrap fuer Sim-Assets; `todo.index.md` spiegelt die Open-Counts `Dev 1`, `Agent 1`, `RP 7`, `Sim 2`.

RP/Inventory: Fraktionscheck fuer die Zuteilungsmatrix nachgezogen (2026-03-27 16:19)
-------------------------------------------------------------------------------

- Das Arbeitsblatt `novapolis-dev/docs/process/rp-metro-warenzuteilung-matrix-2026-03-27.md` fuehrt jetzt nicht mehr nur `Novapolis` plus Sammelblock, sondern jede aktive Fraktion einzeln ueber ihr T0-Warenbild und den vorhandenen Inventarrahmen.
- Novapolis bleibt darin bewusst gesondert: Die aktive SSOT fuehrt `Novapolis` als lokale Kernfraktion in frueher Aufbauphase, nicht als etablierte Metro-Hauptfraktion mit normalisiertem Handels- oder Lagernetz.
- Fuer Arkologie-A1, Schienenbund, Haendlerbund, Eiserne Enklave/Eisenkonklave, Schattenbund und Fluesterkollektiv markiert die Matrix jetzt einzeln, was nur als Rollen-/Bandbreitenraum lesbar ist und was weiter echte Handentscheidung bleibt.

RP/Inventory: Operative Zuteilungsmatrix fuer die finale Metro-Warenverteilung verankert (2026-03-27 16:12)
-----------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-metro-warenzuteilung-matrix-2026-03-27.md` fuehrt die relevante RP-Datenbasis jetzt als Arbeitsmatrix `hart gesetzt | konservativ geschaetzt | manuell zu entscheiden`; damit ist die Vorarbeit fuer die finale Handverteilung nicht mehr ueber mehrere Inventar-, Admin- und RAW-Dateien verstreut.
- Die Matrix zieht Metro-Rahmen, Novapolis-T0-Lage, D5-/C6-Startanker, Tagesdeltas und den Versorgungslauf `D5 -> C6` zusammen und markiert explizit, welche Punkte weiterhin manuelle Entscheidungen bleiben muessen.
- `todo.rp.md` fuehrt das neue Arbeitsblatt als abgeschlossenen Vorbereitungspunkt, `todo.index.md` spiegelt den neuen RP-Statushinweis ohne Veraenderung des Open-Counts.

Dev/Governance: Snapshot-Gate-Bypass und Hook-Kommentar nach Review bereinigt (2026-03-27 15:52)
-------------------------------------------------------------------------------------------------

- `scripts/snapshot_gate.py` prueft Snapshot-Freshness jetzt fuer alle geaenderten Markdown-Dateien mit `stand:`-Feld und nicht mehr nur dann, wenn `stand:` selbst im Diff auftaucht. Damit stimmt das technische Gate wieder mit der dokumentierten Governance ueberein.
- Die enge Lock-Stand-Toleranz ist im selben Schritt als benannte Konstante gefasst; das reduziert kuenftige Pflege-Drift zwischen Code und Governance-Beschreibung.
- `scripts/pre_commit.py` kommentiert markdownlint nicht mehr als optional, und der neue Regressionstest deckt sowohl den entfernten Bypass als auch die Gate-Reihenfolge des Hooks ab.

Dev/Governance: Snapshot-/Pre-Commit-Retry-Pfad operativ gehaertet (2026-03-27 15:05)
---------------------------------------------------------------------------------------

- `scripts/pre_commit.py` fuehrt das Snapshot-Gate jetzt erst nach markdownlint, Frontmatter-Validator und optionalen RP-Hard-Gates aus. Damit verbrauchen spaete Hook-Abbrueche oder automatische Markdown-Fixes die Snapshot-Freshness nicht mehr vorzeitig.
- Die dokumentierte Regel `R-SNAP` spiegelt die operative Hook-Reihenfolge jetzt explizit; Governance-Text und Hook-Iststand liegen damit wieder auf derselben technischen Achse.
- Mit diesem Schritt ist der letzte offene Governance-Folgepunkt aus `todo.dev.md` geschlossen. Das Dev-Board steht damit wieder bei `offen: 0`.

Dev/Governance: Python-Workspace-Tasks auf `process` vereinheitlicht (2026-03-27 14:51)
--------------------------------------------------------------------------------------

- In `.vscode/tasks.json` laufen die verbliebenen Python-basierten Tasks jetzt durchgaengig als `process` statt als `shell`; damit faellt der lokale `pwsh /d /c`-Fehlpfad auch fuer Eval-, Daten-, Trainings- und Utility-Tasks weg.
- Bewusst unveraendert blieben nur echte Shell-Aufrufe ueber `pwsh`, etwa fuer `tree`-Erzeugung oder HTTP-basierte TTS-Hilfstasks. Die Ausnahme ist damit technisch begruendet statt historisch gewachsen.
- Der dritte offene Governance-Punkt aus `todo.dev.md` ist damit geschlossen; als letzter offener Dev-Punkt bleibt der operative Snapshot-/Pre-Commit-Retry-Pfad.

Dev/Governance: Kern-Governance auf eine eindeutige Normschicht reduziert (2026-03-27 14:51)
---------------------------------------------------------------------------------------------

- Die Kerndatei `.github/copilot-instructions.md` benennt jetzt die `Regel-ID-Landepunkte (Kern)` explizit als einzige bindende Ebene fuer Runtime-Entscheidungen; der `Regel-ID-Index (Kern)` bleibt Navigation und die `Regelmatrix (Kern)` ist nur noch Kurzreferenz.
- Der bisherige TL;DR-Block wurde von parallel gepflegten Regeltexten auf knappe Verweise pro Regel-ID umgestellt. Damit sinkt die Driftflaeche, ohne dass operative Orientierung verloren geht.
- Der Headings-Index spiegelt die neue Normschichtung mit; damit ist der zweite offene Governance-Punkt aus `todo.dev.md` geschlossen und als naechster Dev-Punkt bleibt die systematische Task-Umstellung von `shell` auf `process` offen.

Dev/Governance: Quellenstand von Kern-SSOT und Headings-Index wieder zusammengezogen (2026-03-27 14:41)
-------------------------------------------------------------------------------------------------------

- `.github/copilot-instructions.md` und `.github/copilot-instructions-headings.md` verweisen jetzt wieder auf denselben aktuellen Governance-Zeitanker; der Drift lag nur noch in Kopf-/Quellenmetadaten, nicht in der eigentlichen Abschnittsstruktur.
- Die Abschnittsliste des Headings-Index blieb inhaltlich tragfaehig; nachgezogen wurden daher bewusst nur Quellenstand, Update-/Check-Hinweise und der zugehoerige Dev-Board-/Index-Sync.
- Damit ist der erste offene Governance-Punkt aus `todo.dev.md` geschlossen; der naechste offene Dev-Punkt bleibt die Redundanzreduktion in der Kern-Governance.

Dev/Governance: Review auf Aktualitaet, Redundanz und Verbesserungspotential in Board-Folgearbeit ueberfuehrt (2026-03-27 14:32)
------------------------------------------------------------------------------------------------------------------------

- Der Review bestaetigt keinen akuten Governance-Bruch mehr, aber vier klare Folgeachsen: Die Kern-SSOT und ihr Headings-Index sind metadatenmaessig hinter dem echten Regelstand, zentrale Regeln liegen redundant auf mehreren Ebenen, ein Teil der Python-Workspace-Tasks laeuft weiter als `shell`, und der Snapshot-Retry-Pfad ist zwar jetzt sauber dokumentiert, operativ aber noch nicht robust genug.
- Diese Befunde sind jetzt als konkrete Dev-Punkte im offiziellen Board verankert: Quellenstand/Headings-Index angleichen, Kern-Governance auf eine normative Hauptebene reduzieren, verbleibende Python-Tasks auf `process` pruefen und den Snapshot-/Pre-Commit-Retry-Pfad technisch haerten.
- Der Index wurde im selben Lauf auf den neuen Dev-Open-Count und den aeltesten offenen Governance-Punkt synchronisiert.

Dev/Governance: Finaler Snapshot-Sync fuer den Commitlauf gezogen (2026-03-27 14:22)
------------------------------------------------------------------------------------

- Vor dem Commit wurde der Snapshot-Lock erneut frisch gesetzt und die aktiven `stand`-Felder auf denselben Zeitanker synchronisiert, damit der zuvor dokumentierte Governance-Fix nicht selbst wieder am Freshness-Gate scheitert.
- Der Lauf ist inhaltlich unveraendert gegenueber 10:33; es handelt sich um den technischen Commit-/Push-Sync fuer denselben Governance-Fixblock.

Dev/Governance: Snapshot-Retry-Pfad und Python-Tasks gegen Hook-/Workspace-Iststand gehaertet (2026-03-27 10:33)
--------------------------------------------------------------------------------------------------------------

- `R-SNAP` nennt jetzt explizit das praktische Gate-Verhalten fuer Retry-Faelle: `stand` muss frisch zu `now` bleiben, der Lock ebenfalls, und ein nach Hook-Abbruch wiederholter Commit beginnt wieder bei Snapshot-Lock plus `stand`-Sync statt mit altem Lock weiterzulaufen.
- Die Markdown-Instructions dokumentieren die kanonische Einzelausnahme fuer `.github/copilot-instructions.md` jetzt konsistent, damit die historische Kopfzeilenform `Stand:`/`Checks:` nicht mehr im Konflikt mit der allgemeinen Legacy-Kopfzeilenregel steht.
- Die betroffenen Python-Workspace-Tasks (`coverage`, `todo index sync`, `logs policy` und verwandte Checks) laufen jetzt als `process` statt `shell`; damit faellt der lokale `pwsh /d /c`-Fehlpfad weg, der die eigentlichen Python-Checks zuvor faelschlich rot machte.

RP/Inventory: RAW-Rettungsstand vor Handverteilung und Verbrauchsrechnung festgezogen (2026-03-27 09:46)
------------------------------------------------------------------------------------------------------

- Der offizielle RP-Backlog haelt jetzt explizit fest, was aus RAW vor manueller Fraktionsverteilung noch belastbar gerettet werden kann: quantifizierter C6-Startsnapshot, teilquantifizierter D5-Startanker, generischer Transferpfad `D5 -> C6`, semiformeller C6-Zielanker sowie einzelne Energie- und Materialdeltas.
- Ebenso ist jetzt getrennt dokumentiert, was nur weich rettbar bleibt: Rollen-, Freigabe- und Prozesslogik fuer D5/C6/Novapolis.
- Weiterhin manuell zu setzen bleiben aktuelle Fraktionssummen, standortscharfe Restbestaende, mehrtaegige Verbrauchsreihen und konkrete Transfermengen pro Lauf; genau dafuer wurde ein erneuter Sicherheits-Recheck ueber die RAW-Daten gestartet.

RP/Inventory: C6-Zielanker fuer den D5-Materiallauf auf Logistiksystem-Ebene geschaerft (2026-03-27 08:33)
-------------------------------------------------------------------------------------------------------

- `logistik_novapolis_v2` fuehrt den Lauf `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` jetzt als explizite aktive Fracht; zusammen mit Chat-RAW ist der Materiallauf damit nicht nur erzählerisch, sondern auch systemisch gerahmt.
- `logistik_c6_v2` liefert fuer C6 mit `Primaerlager (Bereich 3)` und `Sekundaerlager (Kontrollraum)` den vorhandenen Lagerrahmen, ohne aber den konkreten Lauf dort als Charge oder Inventarlog-Zeile einzubuchen.
- Als konservative Definition bleibt deshalb nur ein `missionierter Versorgungslauf D5 -> C6 mit bestaetigtem Empfang, Bestandsaufnahme und anschliessender Baustellenverteilung`; Mengen, konkrete Lagerzuordnung und Quittung wurden bewusst nicht promoted.

RP/Inventory: C6-Zielseite fuer den D5-Materiallauf gegen RAW nachgeschaerft (2026-03-27 08:29)
---------------------------------------------------------------------------------------------

- Chat-RAW belegt jetzt auf der C6-Seite nicht nur `Ankunft` und `Bestandsaufnahme`, sondern auch den expliziten Schritt, dass `der Empfang der Ware bestaetigt werden` muss; anschliessend soll die Ware zusammen mit weiterer D5-Fracht an die Baustellen gebracht werden.
- Damit ist die Zielseite des Laufs enger auf `bestaetigter Empfang in C6 mit operativer Weiterverteilung` rahmbar; `C6-Schleuse` und `C6-Lagerhalle` liefern dafuer den passenden Prozessrahmen, aber weiterhin keinen konkreten Logeintrag.
- Weil weiter keine explizite Schleusen-/Lagerbuchung, keine Charge und keine saubere Quittungszeile im Inventarlog vorliegen, wurde bewusst keine neue Inventarmenge promoted.

RP/Inventory: D5-Quellorte fuer den C6-Materiallauf gegen RAW nachgeschaerft (2026-03-27 08:25)
---------------------------------------------------------------------------------------------

- `RAW-canvas-2025-10-20T12-05-00-000Z` belegt in D5 ein Materiallager unter dem Bahnsteig mit Lastenaufzug und Nutzung fuer Schwerlast, Rohstahl, Kabeltrommeln und Energiezellenpaletten; damit ist erstmals ein konkreter physischer Quellort fuer den Materiallauf greifbar.
- `Draisine-Transportmodul.md` plus Chat-RAW belegen parallel Werkstattbestand, Materiallauf-Unterstuetzung und den Fokus von Jonas, Pahl und Lumen auf den Transportpfad; dadurch ist der Ursprung des Laufs enger auf `Materiallager und/oder Werkstattbestand D5` rahmbar.
- Weil weiterhin keine explizite Entnahmebuchung, keine standortscharfe C6-Zielbuchung und keine Quittung/Verantwortlichenzeile vorliegen, wurde bewusst keine neue Inventarmenge promoted.

RP/Inventory: D5->C6-Transferkette erneut gegen Umfeld und RAW geprueft (2026-03-27 08:14)
----------------------------------------------------------------------------------------

- Der Recheck bestaetigt den generischen Transportanker im RAW-Logistikcanvas `RAW-canvas-2025-10-16T13-05-00-000Z`: `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` bei manuellem Transport ohne Bahnverbindung.
- Im Chat-RAW sind fuer denselben Ablauf lediglich `Abmeldung in D5` sowie anschliessend `Ankunft` und `Bestandsaufnahme` in C6 hart sichtbar; das reicht fuer Prozessrahmen, aber nicht fuer Bestandsbuchung.
- Weil weiterhin keine explizite Entnahme, keine Zielbuchung in `C6-Schleuse` oder `C6-Lagerhalle` und keine Quittung/Verantwortlichen belegt sind, bleibt der RP-Punkt offen und es wurde bewusst keine Fraktionssumme oder Item-Menge promoted.

Dev/Backlog: Folgepunkte nach Wochenabschluss konkretisiert (2026-03-27 04:34)
-------------------------------------------------------------------------

- `todo.rp.md` fuehrt den verbleibenden Inventar-Backfill jetzt nicht mehr nur als Sammelpunkt, sondern getrennt nach Transferkette `D5 -> C6`, Delta-Struktur fuer `Novapolis-inventar.md` und Realabgleich fuer das Skill-Mapping-V1.
- `todo.sim.md` enthaelt erstmals einen aktiven Punkt fuer die beiden bekannten Sim-Asset-Warnungen aus dem Wochenabschluss (`summary=fail:0,warn:2`), statt sie nur im Kontexttext zu nennen.
- `todo.dev.md` fuehrt den sichtbaren Drift in den Board-Metadaten von `todo.index.md` als eigenen Hygiene-Punkt; `todo.root.md` und `todo.index.md` sind auf denselben Folgebacklog synchronisiert.

Dev/Process: Wochenabschluss 2026-03-27 komplett abgeschlossen (2026-03-27 01:16)
-------------------------------------------------------------------------------

- `scripts/run_checks_and_report.py` liefert nach dem Doku-Refresh wieder `overall=PASS`; Coverage bleibt bei `93.69%`, alle Governance-Gates sind gruen, und der Reportpfad ist `.tmp/results/reports/checks_report_20260327_011507.md`.
- Die beiden stale ACTIVE-Boards `todo.agent-board.md` und `todo.sim.md` wurden im selben Slot aufgefrischt; damit stehen `todo_index_drift=0`, `active_docs_stale=0`, `placeholder_conflicts=0` und `logs_policy_violations=0` wieder konsistent im KPI-Block.
- Der separate Coverage-Lauf endet mit Exit `0`; `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` bleibt ohne harte Fehler (`summary=fail:0,warn:2`).

RP/Inventory Governance: Ebenenmodell und Pflicht-Deltas fuer Metro-Warenbestand festgezogen (2026-03-20 13:51)
---------------------------------------------------------------------------------------------------------------

- `todo.rp.md` fuehrt jetzt die feste Promotionskette `Charakter -> Team/POI -> Station -> Fraktion -> Metro`, abgeleitet aus den bereits vorhandenen RP-Artefakten statt aus einem neuen Parallelsystem.
- Die Pflichtartefakte je Ebene sind explizit benannt: Charakter-Canvas, POI-/Lokations-Canvas, Stationsinventar, Fraktionsinventar sowie die Admin-Ebene fuer Metro/T0.
- Neue Bestandsfortschreibung soll ab jetzt nur noch ueber die vier Minimal-Deltas `Transfer`, `Verbrauch`, `Handel` und `Bilanz` nach oben promoted werden.

RP/Inventory: Materiallauf in D5 und C6 standortscharf nachgezogen (2026-03-20 11:49)
-------------------------------------------------------------------------------

- D5 und C6 fuehren den missionierten Materiallauf jetzt beide als lokalen Review-Anker, damit die Luecke nicht nur im Fraktionsinventar haengt.
- D5 dokumentiert den fehlenden Quellabgang, C6 die fehlende Zielbuchung in Lagerhalle/Schleuse.
- Mengen, Charges und Quittungen bleiben weiterhin offen; es wurde nichts neu quantifiziert.

RP/Inventory: Guetermission D5 -> C6 als Transferanker verankert (2026-03-20 11:40)
-------------------------------------------------------------------------------

- Das aktive Missionslog fuehrt jetzt einen eigenen Anker fuer den Materiallauf `D5 -> C6`; belegt sind Richtung, Zweck und der fehlende Stuecklistenentscheid vor dem Lauf.
- Im Fraktionsinventar ist damit die Transportrichtung nicht mehr nur implizit aus RAW ableitbar, sondern im aktiven SSOT benannt.
- Offen bleibt weiterhin die Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`; deshalb wurde keine harte Fraktionssumme promoted.

RP/Inventory: Transfer- und Verbrauchskette fuer Novapolis geprueft (2026-03-20 11:33)
--------------------------------------------------------------------------------------

- Belegt sind jetzt drei harte Anker fuer den Backfill: D5-Startsnapshot, quantifizierter C6-Startsnapshot und der Tagesabschluss Tag 12 -> 13 mit Energie- und Materialdelta.
- Ebenfalls belegt ist eine generische Logistikrichtung aus `logistik_novapolis_v2`: `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` sowie `C6 -> D5 (Materialrueckfuehrung)`.
- Nicht belegt ist weiter die vollstaendige Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`; genau diese Luecke verhindert weiterhin eine harte Fraktionssumme in `Novapolis-inventar`.

RP/Inventory: D5-Startsnapshot aus RAW als Stationsanker nachgezogen (2026-03-20 07:22)
-------------------------------------------------------------------------------------

- `RAW-canvas-2025-10-16T12-00-00-000Z` belegt fuer D5 ein fruehes Stationsinventar mit `Union-Kisten (3)`, Ersatzrohren/Ventilkomponenten, defekter Reparaturstation und zu `60 %` lesbaren Schaltplaenen.
- Der Befund ist stark genug fuer einen lokalen D5-Startanker und einen vorsichtigen Hinweis im Fraktionsinventar, aber nicht fuer aktuelle Summen ohne spaetere Transfer-/Verbrauchskette.
- Der bisherige PoD-Mangel bleibt bestehen; missionierte Zustellungen oder spaetere Umbuchungen wurden weiterhin nicht frei erfunden.

RP/Inventory: C6-Startsnapshot mit Stückzahlen aus RAW/Staging nachgezogen (2026-03-20 07:14)
-------------------------------------------------------------------------------------------

- `inventar_c6_v2` und `logistik_c6_v2` liefern fuer C6 erstmals einen harten Bestandssnapshot mit konkreten Stueckzahlen statt nur Bedarfskategorien.
- Nachgezogen wurden nur datierte C6-Startwerte; D5 und `Novapolis-inventar` bleiben unveraendert, weil kein gleich starker D5-/Aggregatbeleg vorliegt.
- Der Deal-Anker `scene-2026-01-14-b` bleibt fuer Inventarbewegungen weiterhin zu weich, solange PoD, Lieferkette und Abholpunkt nicht belegt sind.

RP/Skills: Skill-Mapping-V1 um zweite Referenzreihe erweitert (2026-03-20 07:08)
-----------------------------------------------------------------------------

- `annotation-spec.md` fuehrt jetzt zusaetzliche V1-Beispiele fuer `Pahl`, `Reflex`, `Lumen` und `Echo`, gestuetzt auf Personenindex, Charakterblaetter und Behavior-Register.
- `Pahl` bleibt trotz Sicherheitsfreigaben konservativ im Rollenfit `wartung_technik`; `Reflex` und `Echo` werden als `sicherung_monitoring`, `Lumen` als `wartung_technik` gelesen.
- Der Ausbau verbreitert die Referenzbasis, ohne neue Rollen-Baselines, Modifier-Logik oder persistente Charakter-Skillwerte einzufuehren.

RP/Skills: Skill-Mapping-V1 aus Verhaltensmatrix verankert (2026-03-20 06:59)
--------------------------------------------------------------------------

- `annotation-spec.md` enthaelt jetzt eine konservative Novapolis-V1 fuer `reparieren`, `wache`, `funk` und `wahrnehmung` mit Rollen-Baselines fuer `wartung_technik`, `stationsleitung` und `sicherung_monitoring`.
- Die V1 bleibt absichtlich klein: keine zweite Wahrheit in Charakterdateien, keine direkte Modifier-Verrechnung, keine versteckten Progressionsboni.
- Beispielableitungen fuer Ronja, Jonas und Kora sind im Spec ergänzt und schliessen den offenen RP-TODO-Block zu Skill-Gewichten/Formelbeispielen.

RP/Inventory: Material-Backfill Tag 12->13 fuer Tunnelarbeiten eingetragen (2026-03-20 06:52)
--------------------------------------------------------------------------------------------

- Aus Staging wurde nur der belegte Verbrauch uebernommen: `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten` sowie `2` beschaedigte Werkzeuge.
- Die Tagesabrechnung liefert keine belastbare D5/C6-Aufteilung dieser Entnahmen; deshalb bleibt die Standortzuordnung offen und wird nur als gemeinsames Delta gefuehrt.
- Es wurden keine Restbestände retconnt; Material- und Werkzeugrestmengen bleiben bis zu belegten Vor-/Nachher-Staenden `tbd`.

RP/Inventory: Energie-Backfill Tag 12->13 fuer D5/C6/Novapolis eingetragen (2026-03-20 06:45)
--------------------------------------------------------------------------------------------

- Aus RAW/Staging plus Logistik-Modell wurde nur die belegte Energiebilanz uebernommen: D5 `+10 Produktion / -8 Grundlast / -12 Export`, C6 `+12 Verbrauch / +10 Zufuhr`, Fraktion gesamt `-12 Netto`.
- Absolute Speicher- oder Startmengen wurden bewusst nicht retconnt; diese bleiben bis zu belastbaren Vor-/Nachher-Staenden offen.
- Materialverbrauch und Werkzeugschaden aus demselben Lauf bleiben vorerst im Log-/Backfill-Kontext und werden nicht als absolute Inventarmenge promoted.

RP/Inventory: Erster konservativer D5/C6/Novapolis-Abgleich abgeschlossen (2026-03-20 06:36)
----------------------------------------------------------------------------------------------

- `D5-inventar` fuehrt keine C6-Bestaende mehr als lokale Bestandszeilen; die fruehere Vermischung wurde auf Standortdrift zurueckgebaut.
- `C6-inventar` fuehrt Filter, Energiezellen und Werkzeuge jetzt explizit als lokal belegten Kontext ohne freie Stueckzahlen; `Adapter DN60` und `Schweissausruestung` bleiben Bedarf.
- `Novapolis-inventar` bleibt als konservatives Aggregat offen fuer spaetere Mengen-/Transferzeilen statt unbelegte Summen zu behaupten.

RP/Inventory: Erster echter Abgleichslauf fuer D5/C6/Novapolis gestartet (2026-03-20 06:28)
-------------------------------------------------------------------------------

- Der vorbereitete Pilot wurde in den eigentlichen SSOT-Abgleich ueberfuehrt.
- Erster harter Driftpunkt: `D5-inventar` fuehrte C6-Bestaende, obwohl RAW/Staging und die Szenenanker die strikte Standorttrennung verlangen.
- Die drei Zielinventare `D5-inventar`, `C6-inventar` und `Novapolis-inventar` werden jetzt konservativ auf lokale bzw. aggregierte Beleglage zurueckgefuehrt.

RP/Prep: RAW- und Staging-Lage fuer Inventare/Items nachgezogen (2026-03-20 06:21)
-------------------------------------------------------------------------------

- Die erste Pilotfassung war zu stark SSOT-zentriert; der fehlende Schritt "RAW gezielt durchsuchen" wurde explizit nachgezogen.
- Belegte Suchpfade fuer den heutigen Pilot sind jetzt im Arbeitsblatt verankert, insbesondere `database-raw/99-exports/chat-export*.txt` sowie die kuratierten Staging-Artefakte `chat-export-complete.finalgate.md` und `chat-export (1).review.md`.
- Ergebnis: Der Mengen-Backfill ist jetzt als RAW-abgestuetzter Abgleichslauf dokumentiert, nicht nur als Fortschreibung aus bestehender SSOT.

RP/Prep: Pilotpaket fuer D5/C6/Novapolis-Backfill vorbereitet (2026-03-20 06:12)
-------------------------------------------------------------------------------

- Neues Arbeitsblatt `novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md` angelegt.
- Der heutige Start-Scope ist damit explizit auf `D5-inventar`, `C6-inventar` und `Novapolis-inventar` begrenzt; Guardrails und Belegquellen sind vorab benannt.
- `novapolis-dev/docs/todo.rp.md` und `novapolis-dev/docs/todo.index.md` wurden auf diesen vorbereiteten Pilot-Scope synchronisiert.

Dev/KPI: Trendansicht fuer Hygiene-Cadence verankert (2026-03-19 11:01)
-----------------------------------------------------------------------

- `novapolis-dev/docs/meta/dev-kpi-trends.md` angelegt und die vier Kernmetriken (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`) ueber vier dokumentierte Slots vergleichbar zusammengefuehrt.
- Der aktuelle Slot 2026-03-19 ist direkt ueber `scripts/check_todo_index_sync.py`, `scripts/check_doc_freshness.py` und `scripts/check_logs_policy.py` belegt; offene Placeholder-/Truthfulness-Konflikte im aktiven Dev-Bestand wurden zusaetzlich gegengeprueft.
- `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf `Dev offen: 0` synchronisiert.

Dev/Beta: Externes Installblatt fuer die Standalone-Beta angelegt (2026-03-18 22:47)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/process/standalone-beta-installblatt.md` neu angelegt; der Text richtet sich explizit an Dritte ohne implizites Repo-Wissen.
- Abgedeckt sind Voraussetzungen, Setup, API-/Sim-Start, Verifikation, Go/No-Go und Troubleshooting.
- `README.md`, `todo.root.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf den geschlossenen O11-Stand synchronisiert.

Dev/Community: Maintainer- und Contributor-Paket aufgebaut (2026-03-18 22:40)
-------------------------------------------------------------------------

- Root-Docs `SUPPORT.md`, `RELEASE.md` und `MAINTAINERS.md` als scanbare Einstiegsschicht fuer Support, Release-Rahmen und Verantwortlichkeiten angelegt.
- Root-GitHub-Templates unter `.github/ISSUE_TEMPLATE/` sowie `.github/pull_request_template.md` ergaenzt.
- `README.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf den neuen Iststand synchronisiert; Dev-Open-Count reduziert sich auf `2`.

Dev/Architecture: ADR-Ordner aktiviert (2026-03-18 22:36)
---------------------------------------------------------

- `docs/adr/0001-donelog-ebenen.md` als akzeptierte Entscheidung fuer die normalisierten DONELOG-Ebenen angelegt.
- `docs/adr/0002-quality-gate-sequenz.md` als akzeptierte Entscheidung fuer die verbindliche Reihenfolge `Lint -> Typen -> Tests -> Coverage` und die Coverage-Zweistufenlogik angelegt.
- `docs/adr/adr-index.md` um einen aktiven ADR-Index erweitert; `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf `Dev offen: 3` synchronisiert.

Dev/Governance: Status- und Board-Sync auf PASS-Referenzlauf gezogen (2026-03-18 22:20)
-------------------------------------------------------------------------------

- `WORKSPACE_STATUS.md`, `todo.root.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` vom veralteten 2026-03-10/11-Stand auf den dokumentierten PASS-Lauf `checks_report_20260318_052318.md` gehoben.
- Der Dev-Punkt `Coverage-Sprint Richtung 91%` wurde evidenzbasiert abgeschlossen; der aktuelle Referenzwert liegt bei `93.69%` statt der zuvor noch gefuehrten Zwischenmarke `80.45%`.
- Open-Count im Dev-Board/Index reduziert (`5 -> 4`); naechster offener Dev-Schwerpunkt ist jetzt das Community-/Maintainer-Doku-Paket.

Dev/Docs: RP-Brainstorming archiviert, ACTIVE-Oberflaeche bereinigt (2026-03-18 05:20)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/brainstorming.rp.md` aus dem aktiven Dev-Bestand entfernt und nach `novapolis-dev/archive/docs/others/brainstorming.rp.archive.2026-03-18.md` ueberfuehrt.
- `novapolis-dev/docs/active-surface-index.md` auf den neuen Ist-Stand synchronisiert; der RP-Brainstorming-Eintrag zaehlt nicht mehr zur ACTIVE-Oberflaeche.
- `.github/instructions/mind-cluster.instructions.md` vom toten Aktivpfad bereinigt; Brainstorming-Regel bleibt generisch fuer kuenftige aktive Brainstorming-Dokumente bestehen.

Dev/Quality: Full-Gate wieder gruen + Coverage-Welle 1 gestartet (2026-03-11 07:24)
-------------------------------------------------------------------------------

- `scripts/run_checks_and_report.py` liefert wieder `overall=PASS` (inkl. `ruff`, `black`, `pyright`, `mypy`, `pytest`, Coverage-Gate `>=80%`).
- Coverage-Anstieg fuer den 91%-Pfad gestartet: Baseline `76.24%` auf `80.45%` angehoben.
- Testausbau in `novapolis_agent/tests/scripts/` begonnen (u. a. `test_build_project_context_index.py`, Erweiterungen in `test_summarize_marathon_kpis.py`, `test_build_eval_from_rp.py`, `test_check_dependency_profiles.py`).

Dev/Tests: Punkt 3 aktiviert, 90%-Ziel verankert (2026-03-11 07:07)
--------------------------------------------------------------------

- `novapolis-dev/docs/tests.md` von Alt-Prequel-Notizen auf aktuelle Test-/Coverage-Governance umgestellt (Hard Gate `>=80%`, verbindliches Qualitaetsziel `>=90%`, selektive `100%` nur fuer kleine kritische Module).
- `novapolis-dev/docs/process/abschluss-routine.ssot.md` um verbindliche Coverage-Zweistufenlogik erweitert und Nachweispflicht bei `<90%` fixiert.
- `novapolis-dev/docs/todo.dev.md` um einen abgeschlossenen Punkt-3-Eintrag ergaenzt; `novapolis-dev/docs/todo.index.md` auf den neuen Statushinweis synchronisiert.

Dev/Qualitaet: Folgezyklus gestartet, Punkt 1 begonnen (2026-03-11 06:57)
--------------------------------------------------------------------------

- `novapolis-dev/docs/todo.dev.md` um neue offene Optimierungspunkte erweitert (Gate-Stabilisierung, modernes Doku-Paket, ADR-Aktivierung, O11-Installblatt, KPI-Trendansicht).
- Punkt 1 aktiv gestartet: Ruff/Black-Restbefunde aus dem letzten Sammellauf in `scripts/check_todo_index_sync.py`, `novapolis_agent/scripts/build_eval_from_rp.py`, `novapolis_agent/scripts/summarize_marathon_kpis.py` und `novapolis_agent/tests/scripts/test_prepare_pack_smoke.py` behoben.
- Zwischenstand Coverage: Lint/Format sind fuer den betroffenen Scope gruen, Full-Gate bleibt wegen Coverage-Abstand (`76.24%` bei Ziel `>=80%`) offen.

Dev/Process: Woechentliche Hygiene-Cadence verankert (2026-03-11 06:49)
-----------------------------------------------------------------------

- Offener Dev-Board-Punkt abgeschlossen: 60-Minuten-Wochenslot fuer Drift-Scan, Donelog-Cleanup und TODO/Index-Abgleich verbindlich in `novapolis-dev/docs/process/abschluss-routine.ssot.md` dokumentiert.
- KPI-Protokollschema fixiert (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`) und Nachweisziel auf `novapolis-dev/docs/donelog.md` plus Root-Summary bei Abweichungen festgelegt.
- `novapolis-dev/docs/todo.index.md` auf `Dev offen: 0` und Metadaten (`keiner (offen: 0)`) synchronisiert.

Dev/Tooling: TODO-Index-CLI Rueckwaertskompatibel (2026-03-11 06:43)
---------------------------------------------------------------------

- `scripts/check_todo_index_sync.py` unterstuetzt wieder legacy Aufrufe mit `--root` (Alias auf `--repo-root`) und akzeptiert `--strict` als Deprecated-Noop.
- Ziel: Bestehende Wrapper-/Task-Aufrufe bleiben lauffaehig, waehrend die neue CLI (`--repo-root`, `--write-index-meta`) aktiv bleibt.

Dev/Docs: Receipt-Hygiene fuer Governance-Dokus finalisiert (2026-03-11 04:49)
------------------------------------------------------------------------

- `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `docs/adr/adr-index.md` von temporaeren `checks: pending`-Markern auf echte Receipt-Zeilen umgestellt.
- `novapolis-dev/docs/donelog.md` Frontmatter auf denselben Lauf synchronisiert.
- Ergebnis: aktive Governance-Dokumente sind jetzt konsistent mit den laufenden Markdown-/Frontmatter-Gates.

Dev/Docs: README-Kompaktmodus + TODO-Index-Autowrite (2026-03-11 05:12)
------------------------------------------------------------------------

- `README.md` und `novapolis-dev/README.md` auf aktive Leseoberflaeche gestrafft; historische/temporäre Details explizit auf Archiv-/Statusquellen verwiesen.
- `scripts/check_todo_index_sync.py` um Auto-Write erweitert (`--write-index-meta`): Open-Counts und Board-Metadaten in `novapolis-dev/docs/todo.index.md` werden jetzt automatisch synchronisiert.
- Integration nachgezogen: `scripts/run_checks_and_report.py` und Task `Checks: todo index sync` verwenden den Auto-Write-Flag.
- Ergebnis: weniger manuelle Indexpflege und schnellere Onboarding-Lesbarkeit in den Haupt-READMEs.

Dev/Docs: Optimierungsbatch Aktiv-vs-Archiv + TODO-Konsistenz (2026-03-11 03:58)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: verbleibende offene Referenz-Checkbox (`scheduler-spec`) auf erledigt gesetzt; Sim-Board damit konsistent auf `offen: 0`.
- `novapolis-dev/docs/todo.index.md`: Sim-Open-Count von `1` auf `0` synchronisiert und Statushinweis `Sim v5.0` ergänzt.
- `README.md`: Archivregeln praezisiert (zentrales Dev-Archiv als Doku-SSOT; modulinterne Archive nur fuer technische/operative Artefakte).

Dev/Docs: Informationsarchitektur-Runde v2 (2026-03-11 04:27)
--------------------------------------------------------------

- Aktive Oberflaechen entlastet: `todo.sim.md` auf offene Punkte + Kurzkontext reduziert.
- TODO-Index operativ gestrafft: `todo.index.md` auf Kernstatus reduziert und um Board-Metadaten erweitert.
- `scripts/check_todo_index_sync.py` erweitert: Open-Count-Konsistenz, Widerspruchserkennung (`keine offenen` bei offenen Checkboxen) und Diagnoseausgaben.
- Archiv-/Log-Matrix in Root-`README.md` und `novapolis-dev/README.md` vereinheitlicht.
- Repo-Standards ergaenzt: `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `CHANGELOG.md`, `docs/adr/adr-index.md`.

Dev/Docs: Root-DONELOG auf Summary-Ebene normalisiert (2026-03-11 04:46)
-------------------------------------------------------------------------

- `DONELOG.md` wurde auf einen bewusst kurzen Root-Summary-/Release-Log umgestellt.
- Detailhistorie bleibt im Archivpfad `novapolis-dev/archive/docs/donelogs/donelog_root.md` erhalten.
- Ziel: niedrigere kognitive Last auf Root-Ebene bei unveraenderter Nachvollziehbarkeit.

Dev/Docs: README-Finish fuer aktive Lesbarkeit (2026-03-11 04:46)
------------------------------------------------------------------

- Root-`README.md` um explizite Verweise auf `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `CHANGELOG.md` und `docs/adr/` ergaenzt.
- `novapolis-dev/README.md` von einem veralteten, ausserhalb des Frontmatters stehenden Checks-Receipt bereinigt und den Abschnitt `Checks & Reports` auf einen stabilen Dauertext umgestellt.
- Ergebnis: weniger Betriebsrauschen in aktiven READMEs und klarere Onboarding-Fuehrung fuer Maintainer/Contributors.

Archivhinweis
-------------

- Aeltere Current-Window-Eintraege bleiben unveraendert in Git-Historie und den Donelog-Archiven.
- Dieses aktive Dokument wird bewusst kurz gehalten und dient als menschlich lesbare Entscheidungs- und Fortschrittsansicht.
