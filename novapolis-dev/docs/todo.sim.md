---
stand: 2026-06-19 15:17
update: Das Sim-Board steht jetzt wieder bei `offen: 0`; der letzte Headless-Verify-Rest ist ueber den Resolver-Fallback auf die lokal laufende Godot-Binary geschlossen.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md

---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Sim)
====================

Hinweis
-------

- Arbeitsmodus (User-Praeferenz): Alles, was nicht direkt in VS Code ausgefuehrt wird (insbesondere Godot-Editor-Schritte), immer als explizite Schritt-fuer-Schritt-Anleitung mit klaren Klickpfaden und erwarteten Ergebnissen liefern.
- Dieses Dokument bündelt Aufgaben für das Simulations-Modul (Godot-Projekt `novapolis-sim`, Visualisierung, API-Integration, Build/Export).
- Dev-Aufgaben liegen in `docs/todo.dev.md`. RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Aktive Oberflaeche bleibt absichtlich kurz: nur offene Punkte plus max. 14 Tage Kontext.
- Vollstaendig erledigte und aeltere Bloecke liegen in `novapolis-dev/archive/todo.sim.archive.md`.

Prioritaetstags (aktiv)
-----------------------

- `Jetzt`: Architektur-Entflechtung und belastbare Sim-Verifikation hinter dem neuen Hub.
- `Als naechstes`: Export-/Release-Pfad, Spiel-IA und Fortsetzungslogik auf denselben Produktpfad heben.
- `Spaeter`: Komfort- und Atmosphaere-Ausbau erst nach stabilem Produktloop.

Offene Aufgaben (Sim)
---------------------

- [ ] [Als naechstes] GOV-STRANG-02: Sim-Governance-Bruecke fuer den Umbau als explizite Planarbeit fuehren.
  - Ziel: Sim-seitige Checks/Gates bleiben im Governance-Umbau sichtbar repraesentiert, ohne Sim-Fachroadmap zu uebersteuern.
  - Akzeptanzkriterien:
    1) Sim-relevante Governance-Bezuege sind auf Root-/Dev-Planlandschaft verlinkt,
    2) Sim-Board fuehrt einen klaren Umbaupunkt mit Evidenz,
    3) keine unnoetige Mutation in `.godot/` oder Sim-Exportartefakten.
  - Evidenz: `.github/copilot-instructions.md` (Workspace-Atlas/Sim-Hinweise), `novapolis-dev/docs/todo.index.md`.

Abgeschlossene Eintraege (Bestand)
----------------------------------

- [x] [Jetzt] Den Godot-Resolver des kanonischen Headless-Verify auf den lokal vorhandenen Editor-/Binary-Pfad heben.
  - Ergebnis 2026-04-23 18:34: `scripts/run_sim_headless_verify.py` erkennt unter Windows jetzt neben `GODOT_BIN`, `godot4` und `godot` auch den Pfad eines bereits laufenden lokalen Godot-Prozesses ueber `pwsh` oder `powershell`. Im aktuellen Workspace-Kontext wird damit die lokal laufende Godot-4.6.1-Windows-Binary automatisch aufgeloest, ohne den bestehenden Fehlerpfad fuer wirklich fehlende Binaries zu verschleifen.
  - Verifikation 2026-04-23 18:34: Der kanonische Task `Checks: sim headless verify` endet jetzt mit `SIM_VERIFY: OK`. Der neue fokussierte Pytest-Scope `novapolis_agent/tests/scripts/test_run_sim_headless_verify.py` ist ebenfalls PASS; das Sim-Board steht damit wieder bei `offen: 0`.

- [x] [Jetzt] Den kanonischen Windows-Exportpfad von reinem Klickpfad auf einen belastbaren Preset-/Konfigurationsanker heben.
  - Ergebnis 2026-04-23 16:38: `novapolis-sim/export_presets.cfg` fuehrt jetzt denselben Windows-Desktop-Pfad `exports/windows/NovapolisSim.exe` repo-seitig als Godot-Presetanker. README, Export-SSOT und Tasking referenzieren damit nicht mehr nur einen Editor-Klickpfad, sondern denselben technischen Zielanker im Projektbaum.

- [x] [Als naechstes] Einen lokalen Post-Export-Smoke fuer die erzeugte `NovapolisSim.exe` als eigenen Wrapper-/Checkpfad nachziehen.
  - Ergebnis 2026-04-23 16:38: `scripts/run_sim_export_smoke.py` plus Task `Checks: sim export smoke` pruefen den exportierten Windows-Pfad jetzt repo-seitig. Fehlt die EXE, liefert derselbe Wrapper bewusst `export executable missing` statt diffuser Sim-Fehlersprache; liegt ein Export vor, kann derselbe Pfad die App optional kurz starten.
  - Verifikation 2026-04-23 16:38: Die fokussierten Tests fuer `test_run_sim_export_smoke.py` sind PASS; der direkte Repo-Lauf meldet aktuell erwartungsgemaess die Vorbedingung `novapolis-sim/exports/windows/NovapolisSim.exe` als fehlend.

- [x] [Als naechstes] Fuer den Offline-Asset-Check neben `Clean-Checkout` einen kleinen, reproduzierbaren Vollstand-Fixture-Pfad aufbauen.
  - Ergebnis 2026-04-23 16:38: Unter `novapolis-sim/data/epochs/epoch01/` liegt jetzt ein minimaler Vollstand mit `world_log.jsonl` und `pc_log.jsonl`; `novapolis-sim/assets/audio/` fuehrt dazu benannte OGG-Beispiele. Der neue Task `Checks: sim epoch assets (minimal fullstand)` laeuft ohne `--allow-empty` gegen genau diesen kleinen Repo-Vollstand.
  - Verifikation 2026-04-23 16:38: `scripts/check_sim_epoch_assets.py --repo-root . --check-slot-consistency` endet mit `summary=fail:0,warn:0` und bestaetigt Slot-Konsistenz fuer `epoch01` plus gueltige Audionamen.

- [x] [Als naechstes] Persistenz und Replay-Resume fuer `user://hub_prefs.cfg` ueber gezielte Regressions- oder Verifikationspfade absichern.
  - Ergebnis 2026-04-23 16:38: `scripts/check_sim_hub_prefs_contract.py` prueft jetzt repo-seitig die in `Main.gd` verwendeten Load-/Save-Schluessel gegen leere, partielle und aeltere Fixture-Dateien unter `novapolis-sim/tests/fixtures/hub_prefs/`. Dazu kommt der neue Task `Checks: sim hub prefs contract` als statischer Drift- und Neustartpfad ohne Godot-Runtime.
  - Verifikation 2026-04-23 16:38: Der neue Pytest-Block `test_check_sim_hub_prefs_contract.py` ist PASS, und der direkte Repo-Lauf bestaetigt denselben Key-Satz fuer `session_id`, `scene_id`, `resume_checkpoint_id` und `selected_replay_checkpoint_id` plus die Default-/Fallback-Lesart der Fixtures.

- Der zuletzt geschlossene Sim-Abschlussschnitt liegt jetzt zusaetzlich unter `novapolis-dev/archive/todo.sim.archive.md`; das Live-Board ist fuer neue Sim-Punkte vorbereitet.

- [x] [Jetzt] Den Godot-Headless-Verifier von einem Projekt-Ladecheck auf einen echten Sim-Smokepfad heben.
  - Ziel: Der kanonische Verifier soll kuenftig mehr absichern als nur, dass das Projekt irgendeine `application/config/name`-Einstellung besitzt.
  - Akzeptanzkriterien:
    1) `res://scripts/verify_sim.gd` prueft mindestens Main-Scene, Autoload `SimClient` und die fuer Hub-/Replay-/Chat-Bedienung benoetigten Kernknoten,
    2) der Lauf scheitert mit klarer Fehlermeldung, wenn zentrale Sim-Knoten oder Projektverknuepfungen fehlen,
    3) der Verifier bleibt headless und lokal reproduzierbar,
    4) README und Board nennen denselben Verifier als kanonischen Smoke-Pfad.
  - Evidenz: `novapolis-sim/scripts/verify_sim.gd` prueft derzeit nur `ProjectSettings.has_setting("application/config/name")` und endet anschliessend pauschal mit `SIM_VERIFY: OK`.
  - Arbeitsstand 2026-04-14 13:57: Der Ausbau laeuft jetzt gegen den echten Startpfad. `project.godot` fuehrt `application/run/main_scene="res://Main.tscn"` und `autoload/SimClient`, waehrend `Main.tscn` die relevanten Hub-, Replay-, Chat- und Modulpanels bereits eindeutig traegt. Der neue Verifier soll diese Projektverknuepfung und die Kernknoten direkt headless pruefen.
  - Ergebnis 2026-04-14 13:57: `novapolis-sim/scripts/verify_sim.gd` prueft jetzt Projektname, Main-Scene, Autoload `SimClient`, das Root-Script `res://scripts/Main.gd` sowie die zentralen Hub-, Replay-, Chat- und Modul-Knoten direkt an einer instanziierten Main-Scene. Fehler werden als `SIM_VERIFY: FAIL` mit konkreten Einzelursachen ausgegeben und beenden den Lauf mit Exitcode `1` statt als pauschales OK/WARN durchzulaufen.
  - Verifikation 2026-04-14 13:57: `get_errors` bleibt fuer `novapolis-sim/scripts/verify_sim.gd`, `novapolis-sim/scripts/Main.gd`, `novapolis-sim/project.godot` und `novapolis-sim/Main.tscn` ohne Befund. `novapolis-sim/README.md` verweist bereits auf denselben Verifier-Pfad `res://scripts/verify_sim.gd` als Headless-Smoke-Lauf. Ein echter Godot-Prozesslauf war in diesem Terminalkontext nicht belegbar, weil weder `GODOT_BIN` gesetzt war noch `godot`/`godot4` im PATH aufloesbar waren.

- [x] [Als naechstes] Den Release-/Exportpfad fuer das eigentliche Spiel kanonisch und reproduzierbar machen.
  - Ziel: Der produktive Start ausserhalb des Godot-Editors soll nicht nur als Handhinweis `Project -> Export` existieren, sondern als belastbarer Repo-Pfad.
  - Akzeptanzkriterien:
    1) das Repo fuehrt Export-Voreinstellungen oder eine gleichwertig verbindliche Export-Dokumentation fuer den produktiven Windows-Desktop-Pfad,
    2) Asset- und Datenvoraussetzungen fuer Clean-Checkout, lokalen Vollstand und exportierte Laufzeit sind getrennt beschrieben,
    3) ein lokaler Smoke-Test fuer die exportierte App ist beschrieben und ohne Editor-Overlay nachvollziehbar,
    4) README, Board und Folge-Doku zeigen denselben Release-Pfad.
  - Evidenz: `novapolis-sim/README.md` empfiehlt derzeit nur `Project -> Export` fuer Windows Desktop; im Sim-Baum liegt zugleich keine `export_presets.cfg`, und unter `novapolis-dev/docs/process/` gibt es keinen eigenen aktiven Sim-Export-/Release-Leitfaden.
  - Ergebnis 2026-04-15 03:00: `novapolis-dev/docs/process/sim-export-release-path.ssot.md` ist neu und definiert jetzt den kanonischen Windows-Desktop-Pfad ueber `novapolis-sim/exports/windows/NovapolisSim.exe`, getrennte Voraussetzungen fuer Clean-Checkout, lokalen Vollstand und exportierte Laufzeit sowie einen lokalen Smoke fuer die exportierte App ohne Editor-Overlay. `novapolis-sim/README.md` verweist im selben Lauf auf dieselbe SSOT statt nur auf den losen Menuehinweis `Project -> Export`.
  - Verifikation 2026-04-15 03:00: Die Doku verweist jetzt konsistent auf denselben Exportpfad; ein echter Godot-Exportlauf bleibt in diesem VS-Code-Terminalkontext weiterhin manuell, weil die Exportaktion bewusst als Editor-Schritt mit Klickpfad dokumentiert ist.

- [x] [Als naechstes] Informationen zum UI- und Menueaufbau des eigentlichen Spiels als Sim-SSOT dokumentieren.
  - Ziel: Vor weiterer Oberflaechenarbeit braucht der Workspace eine klare Beschreibung, wie Hub, eigentliches Spiel, Menues, Rueckspruenge und Modulwechsel fachlich zusammenhaengen.
  - Akzeptanzkriterien:
    1) die Doku trennt klar zwischen Sim-Hub, eigentlichem Spielablauf, Replay-/Resume-Pfad und operativen Modulen,
    2) Startscreen, Hauptmenue, Ingame-Menues, Pause/Optionen, Rueckwege und Modulwechsel sind als Screen-/Menuebaum oder Informationsarchitektur beschrieben,
    3) die Beschreibung nennt Zustandsbesitz fuer Session, Slot, Replay-Anker und aktive Ansicht statt nur Layoutnamen,
    4) README und Board verweisen auf dieselbe kanonische IA-/Menue-Doku.
  - Evidenz: `novapolis-sim/Main.tscn` und `novapolis-sim/scripts/Main.gd` zeigen Hub-Zonen, Replay-Panel, Chat-Panel und Modulpfade, waehrend `novapolis-sim/README.md` nur das Hub-Hauptmenue und Laufzeitverhalten beschreibt; ein eigener aktiver Sim-Prozesspfad fuer IA oder Menueaufbau ist unter `novapolis-dev/docs/process/` derzeit nicht vorhanden.
  - Ergebnis 2026-04-15 03:00: `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` ist neu und beschreibt jetzt den Screen-/Menuebaum fuer Sim-Hub, Hauptmenue, laufende Spielsicht, Ingame-Menues und operative Module sowie den Zustandsbesitz fuer Hub-Prefs, Live-Session, Replay/Resume und aktive Ansicht. `novapolis-sim/README.md` und dieses Board verweisen im selben Lauf auf dieselbe IA-SSOT.
  - Verifikation 2026-04-15 03:00: Die bisher nur in `Main.tscn` und `Main.gd` impliziten Zonen-, Modul- und Rueckwegbeziehungen sind jetzt als aktive Prozess-SSOT dokumentiert; ein separater Godot-Lauf war fuer diese Dokuarbeit nicht erforderlich.

- [x] [Spaeter] Session- und Hub-Persistenz fuer echte Fortsetzungslaufe haerten.
  - Ziel: Eine laufende Spielsession soll nach Neustarts nicht nur ueber Zufalls-Session-IDs oder manuelles Neuanknuepfen weiterleben.
  - Akzeptanzkriterien:
    1) die Persistenz speichert nur stabile Fortsetzungsdaten wie Session-ID, Resume-Anker und relevante Hub-Voreinstellungen, nicht fluechtige Runtime-Metriken,
    2) Neustartverhalten fuer Hub, Replay und Live-Session ist bewusst dokumentiert,
    3) bestehende lokale Prefs bleiben lesbar oder sauber migrierbar,
    4) der Fortsetzungspfad bleibt mit denselben Session-Endpunkten kompatibel.
  - Evidenz: `Main.gd` setzt `_hub_chat_session_id` beim Start jedes Mal aus dem aktuellen Zeitstempel neu; `_load_hub_preferences()` und `_save_hub_preferences()` persistieren bislang nur Karten-Sichtbarkeit, Default-Panel und Refresh-Profil.
  - Ergebnis 2026-04-15 03:00: `novapolis-sim/scripts/Main.gd` persistiert ueber den bestehenden Hub-Prefs-Pfad jetzt zusaetzlich `session_id`, `scene_id`, `resume_checkpoint_id` und den zuletzt gewaehlten Replay-Checkpoint. Beim Neustart wird eine vorhandene Session-ID nicht mehr ueberschrieben; stattdessen synchronisiert die Sim direkt `GET /session/{session_id}` und `GET /session/{session_id}/replay`, waehrend fluechtige Runtime-Metriken weiterhin bewusst unpersistiert bleiben.
  - Verifikation 2026-04-15 03:00: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/hub_preferences_store.gd` und `novapolis-sim/README.md` ohne Befund. Das Neustartverhalten fuer Hub, Replay und Live-Session ist im selben Lauf in `novapolis-sim/README.md` dokumentiert.

- [x] [Jetzt] Sim-Hub UI von Grund auf als klaren Spiel-/Operations-Hub neu aufsetzen.
  - Ziel: Die aktuelle Godot-Oberflaeche soll nicht weiter als gewachsene Offset-Sammlung gepflegt werden, sondern einen klaren Hub mit Statusband, Live-Spiel-Flaeche, Operations-Spalte und belastbarer Modulzone erhalten.
  - Akzeptanzkriterien:
    1) der Hub trennt Live-Spiel, Steueraktionen, Telemetrie und Modulzugaenge sichtbar statt mehrere Statusinseln lose uebereinander zu legen,
    2) die bestehenden Bedienpfade fuer Live-Chat, Serversteuerung, Checks, RP und Agent bleiben auf denselben Funktionspfaden benutzbar,
    3) der responsive Layoutpfad in `novapolis-sim/scripts/Main.gd` beschreibt den neuen Hub bewusst als wenige Hauptzonen statt als fortgesetzte Einzelrect-Sammlung,
    4) der neue Aufbau bleibt per Godot-Headless-Ladung ohne Scene-Fehler verifizierbar.
  - Evidenz: `novapolis-sim/Main.tscn` fuehrt den Hub derzeit als breite Menge frei platzierter Labels, Panels und Buttons; `novapolis-sim/scripts/Main.gd` verteilt dieselben Knoten in `_apply_editor_hub_layout()`, `_layout_hub_topbar()`, `_layout_hub_actions()` und `_layout_hub_log_and_cards()` weiterhin ueber viele feste Einzelkoordinaten.
  - Ergebnis 2026-04-14 12:03: Der Hub ist visuell und layoutseitig neu aufgebaut. `Main.tscn` fuehrt jetzt eigene Shell-Zonen (`HubTopBandPanel`, `HubStagePanel`, `HubOpsPanel`, `HubTelemetryPanel`) plus neue Panel-Stile; `scripts/Main.gd` schaltet standardmaessig auf den neuen Responsive-Pfad und layoutet den Hub ueber wenige Hauptrechtecke (`_hub_stage_rect()`, `_hub_ops_rect()`, `_layout_hub_shells()`) statt ueber die alte Freihand-Anordnung.
  - Verifikation 2026-04-14 12:03: Die statische Validierung ist gruen (`get_errors` fuer `Main.gd` und `Main.tscn` ohne Befund). Der kanonische Headless-Verifier `res://scripts/verify_sim.gd` laeuft mit einer lokal gestarteten Godot-4.6.1-Binary ebenfalls gruen und liefert `SIM_VERIFY: OK` bei `EXITCODE=0`.

- [x] [Als naechstes] Replay-/Resume-Steuerung fuer `Text-RPG Slice 2 Handover v1` im Hub auf den bestehenden Session-Vertrag heben.
  - Ziel: Der Live-Spielclient soll den bereits vorhandenen Session-/Replay-Vertrag operativ nutzbar machen, statt `resume_checkpoint_id` nur als Label zu zeigen.
  - Akzeptanzkriterien:
    1) der Hub nutzt einen klaren Replay-/Resume-Pfad auf Basis des bestehenden Sessionvertrags statt nur `_request_live_session_state()` auf den aktuellen Snapshot,
    2) Resume-Checkpoint oder Replay-Manifest sind im Client sichtbar waehl- oder abrufbar,
    3) die bestehende Epoch-/Audio-Ansicht bleibt an dieselben Session-Artefakte gebunden,
    4) der neue Pfad bleibt fuer Godot-Bedienung und erwartete Resultate dokumentierbar.
  - Evidenz: `novapolis-sim/scripts/Main.gd` liest aktuell `resume_checkpoint_id` in `_apply_live_session_state()` ein und zeigt ihn nur ueber `rp_replay_seed_label` an; derselbe Client nutzt fuer Live-Sync `_request_live_session_state()` auf dem Session-Snapshot, fuehrt aber keinen sichtbaren Replay-/Checkpoint-Requestpfad. `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` fixiert diesen Resume-Anker jetzt als gemeinsamen Folgevertrag hinter `slot 30`.
  - Arbeitsstand 2026-04-14 12:09: Der Backend-Vertrag ist bereits da. `novapolis_agent/app/api/sim.py` liefert `GET /session/{session_id}` und `GET /session/{session_id}/replay`, inklusive `resume_checkpoint_id`, `checkpoints`, `artifact_paths` und Replay-Zaehlern. Im Sim-Client fehlt aktuell nur der operative Pfad: `scripts/Main.gd` ruft weiterhin lediglich `_request_live_session_state()` und nutzt den Replay-Endpunkt noch nirgends.
  - Ergebnis 2026-04-14 12:21: Der Hub fuehrt jetzt einen eigenen Replay-/Resume-Block. `novapolis-sim/Main.tscn` enthaelt `HubReplayPanel` mit Checkpoint-Auswahl sowie `Replay Sync`- und `Resume-Anker`-Buttons; `novapolis-sim/scripts/Main.gd` ruft den bestehenden Endpunkt `GET /session/{session_id}/replay` jetzt explizit auf, synchronisiert Manifestdaten in denselben Session-/Artefaktpfad und wendet den gewaehlten Resume-Anker ohne Parallelformat auf Slot- und Logansicht an.
  - Verifikation 2026-04-14 12:21: Die statische Pruefung bleibt gruen (`get_errors` fuer `Main.gd` und `Main.tscn` ohne Befund), der kanonische Headless-Verifier `res://scripts/verify_sim.gd` endet mit `EXITCODE=0`, und der gezielte Session-/Replay-Vertragspfad `python -m pytest -q novapolis_agent/tests/test_api_sim_state.py novapolis_agent/tests/tests_sim_api.py` endet ebenfalls mit `EXITCODE=0`.

- [x] [Jetzt] Live-Spielclient fuer den ersten Text-RPG-Slice statt nur Hub-Chat und statischer Epoch-Logs bauen.
  - Akzeptanzkriterium: Die Sim kann eine laufende Spielsession mit aktueller Szene, angebotenen Optionen, Spielereingabe und Rueckmeldung anzeigen, statt nur freie Chat-Nachrichten und vorab gespeicherte Logs zu rendern.
  - Arbeitsstand 2026-04-07: Der bestehende Hub-Chat bleibt bewusst die UI-Basis, wird aber auf den Text-RPG-Pfad gehoben: Der Client sendet Sitzungsrahmen und Orchestrator-Hinweise mit, haelt eine laufende Session-ID und zeigt Szene, Konsequenz, Optionen und Patch-Vorschau als sichtbaren Sessionstand an.
  - Ergebnis 2026-04-07: `novapolis-sim/scripts/Main.gd` sendet den Hub-Chat jetzt mit `orchestrator_enabled`, `campaign_id`, `scene_id`, `slot_id`, `turn_id`, `public_context`, `state_patch_hints` und `retrieval_query` an denselben `/chat`-Pfad; eingehende Antworten werden fuer Szene/Konsequenz/Optionen/State-Patches geparst, im bestehenden Panel als Live-Spielclient gerendert und anschliessend ueber `GET /session/{session_id}` mit dem kanonischen Sessionstand nachgezogen.
  - Evidenz: `_refresh_hub_chat_ui()` in `novapolis-sim/scripts/Main.gd` zeigt Session, Slot/Scene, Szene, Konsequenz, Optionen, State-Patches und das Chat-Protokoll direkt im Hub; `_on_hub_chat_send_pressed()` sendet die laufende Spielereingabe an `/chat`; `_on_hub_chat_request_completed()` und `_on_hub_session_request_completed()` aktualisieren danach denselben sichtbaren Sessionstand.

- [x] [Als naechstes] Replay-/Epoch-Bridge an denselben Agent-Session-Vertrag koppeln.
  - Akzeptanzkriterium: Live-Lauf, gespeicherter Run und Replay nutzen dasselbe Session-/Slot-Modell; `world_log`, `pc_log` und spaetere Audioartefakte lassen sich im Sim-Client ohne Parallelformat laden oder abspielen.
  - Ergebnis 2026-04-07: `novapolis-sim/scripts/Main.gd` zieht den aktuellen Sessionstand jetzt ueber `GET /session/{session_id}` vom Sim-API-Host nach, mappt `world_log`/`pc_log` direkt in dieselbe Epochenansicht, uebernimmt `slot_id`/`slot_index` aus dem Sessionvertrag und markiert `tts_manifest` als live verfuegbaren Audiopfad statt nur `res://data/epochs` zu scannen.
  - Evidenz: `_load_epochs()` in `novapolis-sim/scripts/Main.gd` erwartete zuvor nur lokale Dateien unter `res://data/epochs/<epoch>/world_log.jsonl` und `pc_log.jsonl`, waehrend `novapolis_agent/app/api/sim.py` den kanonischen Session-/Replay-Stand bereits ueber `GET /session/{session_id}` bereitstellt.

- [x] [Als naechstes] Sim-Asset-Warnungen aus `scripts/check_sim_epoch_assets.py` aufloesen oder bewusst kanonisch ausnehmen.
  - Akzeptanzkriterium: Der Check liefert entweder `warn:0` oder die verbleibenden Warnungen sind als absichtliche Ausnahme im Sim-Runbook/Board mit Ursache, Scope und Wiedervorlage dokumentiert.
  - Ergebnis 2026-04-07: `scripts/check_sim_epoch_assets.py` behandelt `--allow-empty` jetzt als kanonisches Clean-Checkout-Profil statt als Warnpfad; fehlende `epochNN`-Ordner und fehlende `.ogg`-Dateien werden in diesem Profil als `INFO` statt `WARN` gewertet, und der Lauf `--repo-root . --allow-empty --check-slot-consistency` endet im aktuellen Repo-Stand mit `summary=fail:0,warn:0`.
  - Evidenz: Derselbe Checker-Lauf meldete zuvor `WARN|no epochNN folders found` und `WARN|audio directory missing`; nach dem Profil-Fix liefert er nur noch `INFO`-Zeilen und `warn:0`.

- [x] [Als naechstes] Minimalen Offline-Bootstrap fuer Epoch- und Audio-Assets definieren, damit der Asset-Check auf Clean-Checkout nicht zwischen Pflicht- und Optionaldaten verschwimmt.
  - Akzeptanzkriterium: Es gibt entweder ein kleines kanonisches Fixture-Set fuer `warn:0` oder eine explizite Profiltrennung `Clean-Checkout` vs. `Vollstand` mit unterschiedlicher Check-Erwartung und dokumentiertem Bootstrap-Pfad.
  - Ergebnis 2026-04-07: Der Offline-Asset-Check kennt jetzt zwei Profile: `Clean-Checkout` mit `--allow-empty` fuer einen warnungsfreien Minimalstand ohne `epochNN`-Ordner oder OGG-Dateien, und `Vollstand` ohne dieses Flag fuer echte Offline-Artefakte. Die Bootstrap-Pfade `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` sind als kanonische Zielorte angelegt und in der Sim-README beschrieben.
  - Evidenz: `scripts/check_sim_epoch_assets.py` dokumentiert `--allow-empty` jetzt explizit als Clean-Checkout-Bootstrap; `novapolis-sim/README.md` trennt denselben Minimalstand vom Vollstand-Pfad.

- [x] [Spaeter] Platzhalterblock aufgeloest: das Sim-Board nutzt keine pauschale Sammelrubrik mehr; Restarbeit wird nur noch als konkrete Einzelpunkte gefuehrt.
  - [x] Headless-Lade-Check `novapolis-sim/project.godot` durchführen; Kurzprotokoll in `novapolis-dev/docs/donelog.md`.
    - Evidenz: `WORKSPACE_STATUS.md` (2025-11-16 04:54, Headless PASS) und `novapolis-dev/docs/donelog.md` (Abschnitt "Godot Headless - Quick Verification").
- [x] [Als naechstes] Hub-Hauptmenue: kleines Chatfenster integriert (Prompt + Antwort + `/chat`-Roundtrip) fuer lokalen Gespraechsmodus direkt im Sim-Hub.
  - Evidenz: `novapolis-sim/Main.tscn` (`HubChatPanel` + Input/Output/Status + `HubChatRequest`) und `novapolis-sim/scripts/Main.gd` (Senden, Endpoint-Aufbau, Response-Handling, Fehlerfall/Status).

Aktiver Kontext (max. 14 Tage)
------------------------------

- 2026-04-18: Der verbliebene Agent-Studio-/Form-State-Rest ist code-seitig weiter geschrumpft. `novapolis-sim/scripts/agent_form_session_controller.gd` kapselt jetzt den Form-Session-State, waehrend `Main.gd` fuer diesen Pfad nur noch Orchestrierung und Folgeaktionen behaelt; offen bleibt fuer den Board-Punkt derzeit nur noch ein belegbarer Headless-Verify gegen eine lokal verfuegbare Godot-Binary.

- 2026-04-14: Der gemeldete Godot-Preload-Fehler auf `hub_layout_controller.gd` war ein Drift-Artefakt aus einer angehaengten zweiten Klassenhaelfte. Nach Deduplizierung ist der Scriptkopf wieder eindeutig und der Preload-Pfad parsebar.

- 2026-04-14: Der vierte Refactor-Schnitt der Sim-Entflechtung ist umgesetzt. Der Live-Spielclient-Chat liegt jetzt ebenfalls in einem eigenen Controller; in `Main.gd` verbleiben in diesem Pfad nur noch Widget-Status, Logzeilen und UI-Folgeaktionen.

- 2026-04-14: Der Agent-Studio-Pfad ist im Architekturpunkt weiter geschrumpft. `Main.gd` delegiert Agent-Studio-UI-Exklusivschaltung, Layout und Studio-Refresh jetzt an `agent_studio_controller.gd`; offen bleiben dort vor allem Form-State-Aufbereitung und Runtime-Aktionspfade.

- 2026-04-14: Der Sammellauf fuer die letzten klaren Main.gd-Controller ist umgesetzt. Layout, Hub-Config und Checks/RP liegen jetzt ebenfalls in eigenen Controllern; in `Main.gd` verbleibt als groesserer Architekturrest im Wesentlichen nur noch der bewusst noch nicht geschnittene Agent-Studio-Block.

- 2026-04-14: Der dritte Refactor-Schnitt der Sim-Entflechtung ist umgesetzt. Nach Helpern und Request-Controller liegt jetzt auch die Session-/Replay-Zustandsanwendung in einem eigenen State-Controller; in `Main.gd` bleibt fuer diese Pfade nur noch Snapshot-Anwendung plus UI-Komposition.

- 2026-04-14: Der Headless-Verifier prueft nicht mehr nur eine Projekteinstellung, sondern jetzt Main-Scene, Autoload und zentrale Hub-Knoten. Die Session-/Replay-Zustandsanwendung ist inzwischen ebenfalls ausgelagert; offen bleibt fuer die Architektur damit nur noch weitere Entflechtung ausserhalb dieses bereits migrierten Pfads.

- 2026-04-14: Nach Abschluss von Hub-Reset und Replay-/Resume-Pfad ist das Sim-Board wieder offen. Die naechsten Folgepunkte betreffen jetzt nicht neue Oberflaechen-Implementierung, sondern Architektur-Schnitt, Verifier-Tiefe, Export-/Release-Pfad, Session-Fortsetzung und eine kanonische Beschreibung des eigentlichen Spiel-UI-/Menueaufbaus.

- 2026-04-14: Der Sim-Hub ist in diesem Lauf layoutseitig neu aufgesetzt und inzwischen auch mit lokaler Godot-4.6.1-Binary headless verifiziert. Der bestehende Live-Spielclient, die Modulpfade und der offene Resume-/Replay-Punkt bleiben funktional erhalten, waehrend der Hub jetzt ueber Top-Band, Stage, Operations-Spalte und Telemetrieband organisiert wird.

- 2026-04-14: Der letzte offene Bedienpfad ist jetzt ebenfalls geschlossen. Der Hub hat einen sichtbaren Replay-/Resume-Block, nutzt `GET /session/{session_id}/replay` explizit neben dem Session-Snapshot und spiegelt den aktiven Resume-Anker in Hub-, Stage- und RP-Ansicht.

- 2026-04-07: Der Sim-Offline-Check kennt jetzt ein kanonisches Clean-Checkout-Profil. `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` liefert im aktuellen Repo-Stand `summary=fail:0,warn:0`; Vollstand-Laeufe ohne `--allow-empty` pruefen weiter echte Offline-Artefakte.
- 2026-03-27: Wochenabschluss-Refresh. `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` blieb damals ohne harte Fehler (`summary=fail:0,warn:2`); die Restwarnungen zu fehlenden Epoch-Ordnern und Audio-Assets sind seit 2026-04-07 ueber das Clean-Checkout-Profil geschlossen.
- 2026-03-11: Mikrodrift bereinigt (`offen: 1 -> 0`) und Referenz-Checkbox fuer Scheduler-Spec auf erledigt gesetzt.
- 2026-03-10: Hub-Hauptmenue-Chatfenster abgeschlossen (UI + `/chat`-Roundtrip + robustes Fehlerhandling).

Archivhinweis
-------------

- Aeltere und vollstaendig erledigte Sim-Bloecke liegen in `novapolis-dev/archive/todo.sim.archive.md`.
- Technische Nachweise liegen in `novapolis-dev/docs/donelog.md` (Current-Window) und `DONELOG.md` (Root-Summary).





