---
stand: 2026-03-03 14:32
update: Dev-Doku auf portable Pfade und TODO-Index-Sync nach 1-5-Qualitaetslauf aktualisiert.
checks: .\.venv\Scripts\python.exe scripts\check_portable_paths.py --repo-root . PASS (2026-03-03 14:06); .\.venv\Scripts\python.exe scripts\run_checks_and_report.py PASS (2026-03-03 14:12); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/donelog.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-sim/README.md' PASS (2026-03-03 14:14); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/donelog.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-sim/README.md' PASS (EXITCODE=0, 2026-03-03 14:14)
---

<!-- markdownlint-disable MD041 -->

Dev-DONELOG (Current Window)
============================

Hinweis
-------

- Aktives Fenster: nur Eintraege der letzten 7 Tage.
- Historik bleibt vollstaendig in den Archivdateien unter `novapolis-dev/archive/docs/donelogs/` erhalten.

Current-Window Eintraege
------------------------

Dev/Ops: 1-5-Qualitaetslauf stabilisiert und auf gruen gezogen (2026-03-03 14:12)
----------------------------------------------------------------------------------

- `scripts/check_portable_paths.py` auf Audit-Frontmatter-`checks:` gehaertet (keine Fehlalarme mehr fuer Receipt-Zeilen).
- Portability-Snippets in aktiven Dokus/Settings portable gemacht (`novapolis-dev/docs/todo.agent-board.md`, `novapolis-sim/README.md`, `.vscode/settings.json`).
- Root-Markdownlint-Scope fuer Vendor-Mirror gehaertet (`.markdownlint-cli2.jsonc`: `TTS/**` ignore), sodass der operative Gate-Lauf nicht im externen Upstream-Bestand rauscht.
- TODO-Index-Sync im gleichen Lauf nachgezogen (`novapolis-dev/docs/todo.index.md`) gemaess R-TODO-IDX.
- Konsolidierter Nachweis: `.tmp/results/reports/checks_report_20260303_141251.md` mit `overall=PASS`.

Dev/Sim: Neues Bild-Asset in Modulpfad uebernommen (2026-03-03 04:16)
-----------------------------------------------------------------------

- Neuer Root-Ordner `assets/` mit Datei `f8bc5f39-0e64-44ca-a53b-ef7688c775ae.png` gefunden (1536x1024, PNG) und fachlich dem Sim-Modul zugeordnet.
- Datei nach `novapolis-sim/assets/f8bc5f39-0e64-44ca-a53b-ef7688c775ae.png` uebernommen.
- Zusaetzlich mit stabilem Namen `novapolis-sim/assets/mainmenu-page1-background.png` abgelegt und als `TextureRect` in `novapolis-sim/Main.tscn` als Hintergrund fuer Hauptmenue Seite 1 eingebunden.
- Vollstaendiges Verschieben/Loeschen des Quellordners aktuell durch externe Dateisperre blockiert (`The process cannot access the file because it is being used by another process`).

Dev/Ops: Tagesabschlusslauf vorbereitet und synchronisiert (2026-03-03 03:43)
--------------------------------------------------------------------------

- `process: Checks: full` erneut ausgefuehrt; Ergebnis weiterhin nicht gruen (`markdownlint`, `path-portability`, `ruff`, `black`, `pytest/coverage` FAIL; `frontmatter`, `namingpolicy`, `pyright`, `mypy` PASS).
- Task-Launcher-Problem fuer zwei Einzel-Tasks bestaetigt (`pwsh ... /d /c`, Exit 64 bei `Tests: coverage (fail-under)` und `Checks: sim epoch assets`); Sim-Check direkt via Python nachgezogen (`summary=fail:0,warn:2`).
- Abschluss-Sync auf Dokumentebene erfolgt: `todo.root.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md` aktualisiert.

Dev/Sim: Agent-Form auf strukturierte Eingabemasken umgestellt (2026-03-03 03:34)
--------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: `AgentFormFieldsScroll` + `AgentFormFieldsBox` ergaenzt; alter JSON-Editor (`AgentFormPayloadEdit`) standardmaessig ausgeblendet.
- `novapolis-sim/scripts/Main.gd`: `_refresh_agent_form_ui()` baut Formularfelder jetzt dynamisch pro Formtyp auf (`_rebuild_agent_form_fields`) statt JSON-Templates zu verlangen.
- `novapolis-sim/scripts/Main.gd`: neue Feld-Builder (`_add_form_line_field`, `_add_form_text_field`, `_add_form_int_field`, `_add_form_float_field`, `_add_form_bool_field`) fuellen die Maske strukturiert.
- `novapolis-sim/scripts/Main.gd`: `Apply` liest Werte direkt aus den UI-Feldern (`_build_agent_form_payload_from_controls`) und uebergibt sie in die bestehenden Apply-Pfade.
- Ergebnis: echte Eingabefelder statt Roh-JSON, besserer UX-Flow bei gleicher Persistenz-/Run-Logik.

Dev/Sim: Agent-Form auf Vollflaeche + Placeholder aufgeruestet (2026-03-03 03:26)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: neues `_layout_agent_form_controls()` setzt Form-Controls dynamisch anhand der realen Panelgroesse (Titelzeile, Mode/Target, Name+Apply, Payload, Status).
- `novapolis-sim/scripts/Main.gd`: `_refresh_agent_studio_ui()` ruft die Form-Layoutfunktion nach dynamischer Formpanel-Positionierung auf, damit der verfuegbare Bereich tatsaechlich ausgenutzt wird.
- `novapolis-sim/scripts/Main.gd`: `_refresh_agent_form_ui()` setzt form-spezifische Placeholder (`LineEdit` und `TextEdit`) via `_agent_form_name_placeholder_for_kind()` und `_agent_form_payload_placeholder_for_kind()`.
- Ergebnis: mehr nutzbarer Eingaberaum und klare graue Beispieltexte, die beim Tippen wie gewuenscht verschwinden.

Dev/Sim: Agent-Hinweistext vollstaendig entfernt (2026-03-03 03:22)
--------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `AgentStudioHintLabel` wird beim Start explizit versteckt und der Text auf leer gesetzt (`visible = false`, `text = ""`).
- `novapolis-sim/scripts/Main.gd`: `_refresh_agent_studio_ui()` setzt die Hint-Sichtbarkeit jetzt dauerhaft auf `false`, damit der Hinweis auch nach Reflows/Modewechseln nicht wieder erscheint.
- Ergebnis: der verbliebene Hinweistext ist komplett aus der UI entfernt.

Dev/Sim: Agent-Hinweistext final entkoppelt und sichtbar gehalten (2026-03-03 03:26)
--------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: dynamische Hint-Position in `_refresh_agent_studio_ui()` auf feste Mindesthoehe umgestellt (`offset_bottom = offset_top + hint_height` statt Nullhoehe).
- `novapolis-sim/scripts/Main.gd`: Hint-Y-Position zusaetzlich auf die untere Panelgrenze begrenzt, damit der verbleibende Hinweistext bei variablen Fensterhoehen nicht aus dem sichtbaren Bereich rutscht.
- Ziel: der letzte verbliebene Hinweistext bleibt stabil lesbar, ohne die responsive Gesamtanordnung zu verschieben.

Dev/Sim: Hub-UI responsive eingepasst (2026-03-03 03:12)
---------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: responsive Layout-Pipeline eingefuehrt (`_apply_responsive_layout`) mit Reflow bei `viewport.size_changed`.
- Hub-Ansicht skaliert jetzt Topbar, Haupt-Action-Buttons, Logflaeche, Kartenreihe (Sim/API/Eval) und Config-Panel dynamisch nach aktueller Fensterbreite/-hoehe.
- Modulpanels (`Agent`, `Checks`, `RP`) nutzen nun dynamische Bounds statt fester 1900x1028-Koordinaten; Exklusivmodus fuellt verfuegbaren Viewport konsistent.
- Agent-Exklusivlayout (`_apply_agent_module_layout`) auf panel-relative Spalten umgestellt, inkl. sauberer Positionierung von `Zurueck`-/Suite-/Source-Controls und Formbereich.
- Hub-Config-Collapse auf relative Hoehe korrigiert; erneuter Layout-Reflow nach Toggle eingebaut, damit Schaltflaechen nicht mehr aus dem Panel rutschen.

Dev/Gov: Repo-weite Naming-SSOT + Naming-Gate (2026-03-03 02:42)
------------------------------------------------------------------

- `novapolis-dev/docs/naming-policy.md`: von RP-engem Altstand auf aktive repo-weite Doku-/Governance-SSOT gehoben (Scope-Whitelist/Blacklist, Rule-/Reason-Namespace, Slug/ID/Tags, Hard-vs-Warn, Migrationsprinzip ohne stille Auto-Fixes).
- `scripts/check_naming_policy.py` (neu): maschineller Gate-Check mit Ausgabeschema `Datei:Zeile:Regel:Wert`, Hard-Fail-Exitcode und Scope-Ausnahmen fuer Archive/RAW/Auditpfade.
- `scripts/run_checks_and_report.py`: neuer Pflichtcheck `namingpolicy` in die Standard-Checkkette eingebunden.
- `.vscode/tasks.json`: neuer Task `Checks: naming policy` fuer den direkten lokalen Gate-Lauf.

Dev/RP: Mind-Cluster SSOT-Normierungen + Validator-Gates (2026-03-03 02:21)
-------------------------------------------------------------------------

- `.github/instructions/mind-cluster.instructions.md`: Governance erweitert um `relation_status`-Enum, `confidence/volatility`-Range, registrierte `R-MCL-*` plus `E-MCL-*` Rule-ID-Sets, geschlossene aber registrierbar erweiterbare Event-Taxonomie und `RC-*`-Reason-Code-Baseline.
- `novapolis-rp/database-rp/00-admin/mind-cluster-template.md`: fachliche SSOT-Normierung nachgezogen (`event_id`-Schema, Enum/Range, Taxonomiehinweise, Bias als externer Profil-Input, no-freetext in `applied_rules[]`).
- `novapolis-rp/coding/tools/validators/src/validate-rp.js`: Mind-Cluster-Checks ergänzt (Enum `relation_status`, Range `confidence/volatility`, `event_id`-Pattern, geschlossene Event-Taxonomie, registrierte Rule-ID- und Reason-Code-Pruefung).
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/ronja-kerschner-mind-cluster.md`: `reason_codes` auf registrierte `RC-*`-Taxonomie migriert.

Dev/Sim: Vollstaendig erledigte Sim-TODO-Bloecke ins Archiv ueberfuehrt (2026-03-03 00:38)
---------------------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: vollstaendig erledigte Bereiche aus dem aktiven Board entfernt und durch direkte Archivverweise ersetzt (Arbeitsplan Phase 1/2, Hub-v1 Priorisierung, Neuordnung A/B/D, Phase 3).
- `novapolis-dev/archive/todo.sim.archive.md`: verschobene Bloecke unveraendert mit `archived_at: 2026-03-03 00:38` oben einsortiert (neuester zuerst).
- `novapolis-dev/docs/todo.index.md`: Sim-Open-Count auf den aktuellen Stand (`offen: 26`) synchronisiert und Statushinweis `Sim v3.5` ergaenzt.

Dev/Sim: Agent-Statusblock mit Spacing + Form-Trennung + optionalem Collapse verfeinert (2026-03-02 23:44)
-----------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: vertikale Anker im Agent-Statusbereich (Eval/System/Latest/Hint/Form) neu abgestuft, damit zwischen Statuszeilen und Formbereich mehr Luft entsteht.
- Laufende Statusanzeige wurde in gruppierte Bullet-Abschnitte umgestellt (mit Zwischenabstaenden), um Lesbarkeit/Zeilenrhythmus zu verbessern.
- Visuelle Trennung Form vs. Laufstatus: `AgentFormPanel` erhaelt bei geoeffneter Form eine leichte Tönung, der Laufstatus wird gleichzeitig dezent abgedimmt.
- Optionales Einklappen bei geoeffneter Form: neuer Export-Schalter `collapse_agent_status_when_form_open` (Default `true`), der Eval/System-Zeilen im Form-Modus einklappt und Platz fuer das Formular freigibt.

Dev/Sim: Agent-UI Feinschliff gegen Form-Overlay im Author-Modus (2026-03-02 23:38)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `_refresh_agent_studio_ui()` nachgeschaerft.
- Im Author-Form-Modus nutzt `AgentLatestRunsLabel` jetzt eine kompaktere Statusansicht statt des vollen 10-Zeilen-Blocks, um visuelle Ueberladung zu reduzieren.
- `AgentFormPanel` wird bei geoeffneter Form dynamisch unterhalb des Status-/Hint-Bereichs positioniert und auf die verfuegbare Panelhoehe begrenzt, damit keine Ueberlagerung mit den Statuszeilen entsteht.
- Ziel: bessere Lesbarkeit und stabileres Layout bei kleineren Aufloesungen bzw. langen Runtime-Statuslisten.

Dev/Ops: Abschlusslauf-Task stabilisiert und erneut ausgefuehrt (2026-03-02 23:29)
-------------------------------------------------------------------------------

- `.vscode/tasks.json`: Task `Checks: full` von `type: shell` auf `type: process` umgestellt, da der Shell-Launcher lokal mit `pwsh ... /d /c ...` fehlschlug.
- Re-Run: `scripts/run_checks_and_report.py` laeuft wieder sauber an, Gesamtstatus bleibt aktuell nicht gruen (`markdownlint`, `path-portability`, `ruff`, `black`, `pytest/coverage` FAIL).
- Sim-Offline-Check erneut ausgefuehrt: `scripts/check_sim_epoch_assets.py --allow-empty --check-slot-consistency` mit `summary=fail:0,warn:2`.

Dev/Ops: SSOT fuer Wochen-/Monatsabschluss eingefuehrt + Maerz-Zyklus gestartet (2026-03-02 23:29)
-----------------------------------------------------------------------------------------------

- Neue SSOT-Datei: `novapolis-dev/docs/process/abschluss-routine.ssot.md` (Wochenabschluss + Monatsabschluss, Regel: erster Montag im Monat).
- Root-Referenz nachgezogen: `README.md` verweist jetzt auf die SSOT statt nur auf einen lokalen Wochenblock.
- Dev-Index nachgezogen: `novapolis-dev/docs/index.md` enthaelt nun den SSOT-Verweis unter `Primary Docs`.
- Laufnachweis Abschlusszyklus (1. Montag im Maerz): `scripts/run_checks_and_report.py` ausgefuehrt; nicht-gruener Iststand dokumentiert (`markdownlint`, `path-portability`, `ruff`, `black`, `pytest/coverage` FAIL).
- Zusatznachweis: `scripts/check_sim_epoch_assets.py --allow-empty --check-slot-consistency` mit `summary=fail:0,warn:2`.

Dev/Sim: Offline-Asset-Check um Slot-Konsistenz gehaertet (2026-03-02 23:07)
--------------------------------------------------------------------------

- `scripts/check_sim_epoch_assets.py`: optionalen Modus `--check-slot-consistency` ergänzt.
- Harte FAIL-Kriterien bei aktivem Modus dokumentiert und umgesetzt: Slot-Mismatch zwischen `world_log`/`pc_log`, Slotwerte ausserhalb `0..23`, sowie Eintraege ohne detektierbaren Slot.
- `novapolis_agent/tests/scripts/test_check_sim_epoch_assets.py` neu: Unit-Tests fuer OK/Mismatch/No-Slot/Out-of-Range.
- TODO-Sync: `novapolis-dev/docs/todo.sim.md` (Offline-Check-Punkte erledigt) und `novapolis-dev/docs/todo.index.md` (`Sim v3.4`) nachgezogen.
- Verifikation: `pytest -q novapolis_agent/tests/scripts/test_check_sim_epoch_assets.py` PASS (4/4); Checker-Lauf `--allow-empty --check-slot-consistency` mit `summary=fail:0,warn:2`.

Dev/Sim: Kanonischen Verifikationsablauf in Runbook/README verankert (2026-03-02 22:49)
------------------------------------------------------------------------------------------

- `novapolis_agent/docs/runbook.md`: neuen Abschnitt `Kanonischer Sim-Pruefablauf (kurz, in Reihenfolge)` eingefuegt (`API-smoke -> Godot-headless -> Offline-Asset-Check -> optional Eval`).
- `novapolis-sim/README.md`: Abschnitt `Kanonischer Testablauf (lokal)` mit identischer Reihenfolge und Kommandobeispielen nachgezogen.
- `novapolis-dev/docs/todo.sim.md`: offene Punkte `Sim-Runbook aktualisieren` und `Runbook/README nachziehen` auf erledigt gesetzt.
- `novapolis-dev/docs/todo.index.md`: Statushinweis `Sim v3.3` zur Doku-Synchronisierung ergaenzt.

Dev/Sim: API-Testabdeckung fuer Sim-State verstaerkt (2026-03-02 22:47)
-----------------------------------------------------------------------

- `novapolis_agent/tests/test_api_sim_state.py`: neue Unit-Checks fuer Event-Cap-Truncation, Invalid-`dt`-ValidationError ohne State-Mutation und Reset-Invarianten nach manueller State-Mutation.
- `novapolis_agent/tests/tests_sim_api.py`: API-Vertrag erweitert um `422`-Fehlerpfade fuer `dt<=0`/fehlendes `dt` sowie Event-Cap-Verhalten ueber den REST-Endpunkt.
- Validierung: `pytest -q novapolis_agent/tests/test_api_sim_state.py novapolis_agent/tests/tests_sim_api.py` PASS (5/5), `pyright` PASS, `mypy` PASS auf den geaenderten Dateien.

Dev/Legal: Hybrid-Lizenzschutz fuer Framework-Inhalte eingefuehrt (2026-03-02 22:18)
-------------------------------------------------------------------------------------

- `README.md`: neuer Abschnitt `Lizenzmodell (Hybrid-Schutz)` mit klarer Trennung zwischen MIT-Code und restriktivem Content-/Datenmaterial.
- `LICENSES.md` (neu): Pfad-zu-Lizenz-Matrix als zentrale Referenz angelegt.
- `novapolis-rp/LICENSE`: von MIT auf restriktive Inhalts-/Datenlizenz (`NCDL v1.0`) umgestellt.
- `novapolis-rp/README.md`: Lizenzhinweise auf `NCDL v1.0` korrigiert, damit Doku und Lizenzdatei konsistent sind.
- `novapolis_agent/eval/datasets/LICENSE.txt` (neu): restriktive Datenlizenz fuer Eval-/Trainingsdaten hinzugefuegt.
- `CONTRIBUTING.md` (neu): DCO-Sign-off (`git commit -s`) und Rechtezusicherung fuer Beitraege dokumentiert.
- `TRADEMARKS.md` (neu): Marken-/Namensnutzung getrennt von Code-/Content-Lizenzen geregelt.

Dev/Sim: Dropdown-Standard fuer Agent-/Hub-Single-Selects (2026-03-02 22:09)
-------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: Single-Select-Controls auf `OptionButton` umgestellt (`AgentEvalSuiteButton`, `AgentDatasetSourceButton`, `AgentFormModeButton`, `AgentFormTargetButton`, `HubConfigDefaultPanelButton`, `HubConfigRefreshButton`).
- `novapolis-sim/scripts/Main.gd`: Verdrahtung von `pressed` auf `item_selected` umgestellt und zentrale Dropdown-Initialisierung (`_init_agent_dropdown_options`, `_init_hub_config_dropdown_options`) ergaenzt.
- `novapolis-sim/scripts/Main.gd`: Formlogik auf echte Optionsmengen umgestellt (`_agent_form_mode_options_for_kind`, `_agent_form_target_options_for_kind`, `_refresh_agent_form_dropdowns`) statt Klick-Zyklen.
- `novapolis-sim/scripts/Main.gd`: Hub-Config `Default/Refresh` nutzt jetzt direkte Dropdown-Selektion statt zyklischem Toggle.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler; Godot-Headless-Check im VS-Code-Terminal in diesem Lauf nicht verwertbar (Terminal wurde unerwartet geschlossen).

Dev/Sim: Jobs Schritt 1 - Author-Form + Queue-Persistenz (2026-03-02 21:55)
-------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `Eval Run` oeffnet im `Author`-Modus jetzt eine `Jobs`-Form statt des bisherigen Blocks.
- `novapolis-sim/scripts/Main.gd`: neue Form-Variante `jobs` unterstuetzt `job_name`, `job_type`, `enqueue`, `priority`, `payload`, `notes`.
- `novapolis-sim/scripts/Main.gd`: `Apply` reiht Jobs in `user://agent_user_data/jobs/queue.json` ein; Queue wird beim Start geladen (`_load_jobs_state`).
- `novapolis-sim/scripts/Main.gd`: Agent-Statusblock zeigt jetzt zusaetzlich den Jobs-Status (`Jobs: queued=... | latest=... (...)`) in den Latest-Runs-Infos.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot-Headless-Check im VS-Code-Terminal in diesem Lauf nicht verwertbar (Terminal wurde unerwartet geschlossen).

Dev/Sim: Advanced Settings Schritt 1 - Author-Form + Persistenz (2026-03-02 21:47)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `AI Status` oeffnet im `Author`-Modus jetzt eine `Advanced Settings`-Form statt nur Metrics-Refresh.
- `novapolis-sim/scripts/Main.gd`: neue Form-Variante `advanced` unterstuetzt `mode`, `policy_profile`, `strictness_level`, `safety_profile`, `debug_level`, `system_behavior`, `notes`.
- `novapolis-sim/scripts/Main.gd`: `Apply` persistiert die Einstellungen unter `user://agent_user_data/settings/advanced.json` und laedt den Status beim Start (`_load_advanced_settings_state`).
- `novapolis-sim/scripts/Main.gd`: Agent-Statusblock zeigt jetzt zusaetzlich den Advanced-Status (`Advanced: ...`) in den Latest-Runs-Infos.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Start mit `EXITCODE=0`.

Dev/Sim: Profiles Schritt 1 - Author-Form + Active/Archive-Status (2026-03-02 21:43)
---------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `Profiles` fuehrt jetzt in den Author-Formflow statt in Summary-Placeholder.
- `novapolis-sim/scripts/Main.gd`: neue Profile-Form unterstuetzt `profile_name`, `mode`, `prompt_system`, `behavior_notes`, `assign_to`, `set_active`, `archive`.
- `novapolis-sim/scripts/Main.gd`: `Apply` persistiert Profile als JSON unter `user://agent_user_data/profiles/` und verwaltet Active/Archive-Registry in `user://agent_user_data/profiles/_registry.json`.
- `novapolis-sim/scripts/Main.gd`: Agent-Statusblock zeigt jetzt zusaetzlich den Profilstatus (`Profiles: ...`, `Active Profile: ...`) in den Latest-Runs-Infos.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Finetune Schritt 1 - Author-Form + Start/Stop + Laufstatus (2026-03-02 21:41)
------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Finetune nutzt jetzt einen echten Runtime-Flow statt Summary-Placeholder (`_start_finetune_run`, `_refresh_finetune_runtime_state`, Stop via `OS.kill`).
- `novapolis-sim/scripts/Main.gd`: Author-Form unterstuetzt jetzt `finetune` mit Profil/Basismodell/Train-File/Output/Hyperparametern; `Apply` startet den Lauf.
- `novapolis-sim/scripts/Main.gd`: bevorzugtes Train-File wird aus dem aktiven User-Dataset aufgeloest, mit Fallback auf ein Repo-Trainingsset.
- `novapolis-sim/scripts/Main.gd`: Agent-Statusblock zeigt Finetune-Laufstatus zusaetzlich in den Latest-Runs-Infos; Buttontexte wurden auf Start/Stop/Config angepasst.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Headless-Load konnte lokal nicht erneut gefahren werden (`godot` CLI im Terminal nicht aufloesbar).

Dev/Sim: Synonyms Schritt 3 - Tagging + Active-Registry im Form-Apply (2026-03-02 21:35)
------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Synonyms-Apply verarbeitet jetzt zusaetzlich `synonym_tag` (Default `v1`) und `set_active` (Default `true`).
- `novapolis-sim/scripts/Main.gd`: neue Registry `user://agent_user_data/synonyms/_registry.json` wird geladen/aktualisiert; aktives Synonym-Set wird als `name@tag` persistiert.
- `novapolis-sim/scripts/Main.gd`: `_build_synonym_form_template()` um Felder `synonym_tag` und `set_active` erweitert.
- `novapolis-sim/scripts/Main.gd`: Agent-Statusblock zeigt jetzt Synonyms-Status + aktives Set (`Active Synonyms: ...`) in den Latest-Runs-Infos.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Dataset-Buttonflow auf direkte Formeroeffnung korrigiert (2026-03-02 20:30)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `_on_agent_datasets_pressed()` startet bei idle nicht mehr implizit den Curation-Run, sondern wechselt (falls noetig) nach `Author` und oeffnet direkt die Dataset-Form.
- `novapolis-sim/scripts/Main.gd`: Operate-Label fuer den Button auf `Datasets Form [...]` angepasst, um das Verhalten klar zu signalisieren.
- Wirkung: Es ist kein Workaround ueber vorheriges Oeffnen der Synonyms-Maske mehr noetig; ein direkter Klick auf `Datasets` fuehrt zur Eingabemaske.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Agent-Modul-Fix fuer Dataset/Synonyms (2026-03-02 20:19)
-------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: Export-Properties am Root-Node von `null` auf valide Defaults zurueckgesetzt (u. a. `server_python_path`, `agent_actions_script_path`, Eval-/Snapshot-Pfade), damit Script-Aufrufe im Agent-Modul stabil aufloesen.
- `novapolis-sim/scripts/Main.gd`: `_resolve_python_executable()` um robuste Fallbacks erweitert (leerer Export -> `res://../.venv/Scripts/python.exe` -> `python`).
- `novapolis-sim/scripts/Main.gd`: `_run_agent_action_summary()` nutzt jetzt Fallback auf `res://../novapolis_agent/scripts/agent_module_actions.py`, falls Exportpfad leer ist.
- `novapolis-sim/scripts/Main.gd`: `Synonyms` routed in `Operate` jetzt direkt in den `Author`-Formflow statt nur stiller Summary-Ausgabe.
- Validierung: Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Datasets Schritt 3 - Tagging + Active-Registry im Form-Apply (2026-03-02 19:38)
-----------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Datasets-Apply verarbeitet jetzt zusaetzlich `dataset_tag` (Default `v1`) und `set_active` (Default `true`).
- `novapolis-sim/scripts/Main.gd`: neue Registry `user://agent_user_data/datasets/_registry.json` wird geladen/aktualisiert; Active-Dataset wird als `name@tag` persistiert.
- `novapolis-sim/scripts/Main.gd`: `_build_dataset_form_template()` um Felder `dataset_tag` und `set_active` erweitert.
- `novapolis-sim/scripts/Main.gd`: Agent-Statusblock zeigt jetzt das aktive Dataset (`Active Dataset: ...`) in den Latest-Runs-Infos.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Agent-Panel-Polish fuer Zeilenumbruch und Hint-Sichtbarkeit (2026-03-02 19:36)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Agent-Headerlabel von `Mode` auf `Modus` vereinheitlicht.
- `novapolis-sim/scripts/Main.gd`: Hint-Offset basiert jetzt auf `AgentLatestRunsLabel.get_line_count()` statt nur auf expliziten `\n`-Zaehlern.
- `novapolis-sim/scripts/Main.gd`: Hint-Sichtbarkeit wird direkt aus der Author-Form-Bedingung abgeleitet (unabhaengig von Frame-Reihenfolge der Refresh-Methoden).
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Parse-Fix fuer Variant-Inferenz in Agent-Hint-Layout (2026-03-02 19:34)
---------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Zeile zur Zeilenanzahl-Berechnung typstabil gemacht (`var latest_runs_lines: int = maxi(...)` statt ungetypter `max(...)`-Inferenz).
- Ursache: Godot 4.6 behandelt die Variant-Inferenz hier als Warning, im Projekt aber als Error (`Warning treated as error`).
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Agent-UI Follow-up nach Main.tscn-Drift (2026-03-02 19:31)
-------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: undefinierte Variable `_is_expanded_layout` in `_refresh_agent_studio_ui()` durch den korrekten Laufzeitstatus `_agent_submenu_open` ersetzt.
- `novapolis-sim/Main.tscn`: Default-Texte auf konsistente Buttonnamen nachgezogen (`Eval-Suite`, `Dataset-Quelle`, `Modus`, `Ziel`).
- Wirkung: kein potentieller Laufzeitfehler durch undefinierte Variable mehr, plus konsistente Benennung bereits vor erstem UI-Refresh.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Agent-Panel-Polish gegen Textueberlagerung + Label-Klarheit (2026-03-02 19:26)
----------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `AgentStudioHintLabel` als direkte `@onready`-Referenz eingebunden und in beiden Layout-Zweigen vereinheitlicht.
- `novapolis-sim/scripts/Main.gd`: `_refresh_agent_studio_ui()` setzt Hint-Position jetzt dynamisch unter den multiline-Block `AgentLatestRunsLabel`, damit sich beide Texte nicht mehr ueberlagern.
- `novapolis-sim/scripts/Main.gd`: Hint wird ausgeblendet, solange das Author-Formpanel sichtbar ist (`agent_form_panel.visible`).
- `novapolis-sim/scripts/Main.gd`: Schaltflaechen-Texte praezisiert (`Eval-Suite`, `Dataset-Quelle`, `Datasets Start/Konfig [...]`).
- `novapolis-sim/scripts/Main.gd`: Form-Buttons auf klare Bezeichnungen umgestellt (`Modus`, `Ziel`) inkl. lesbarer Werte fuer Dataset-/Synonym-Modi und Zieltyp.
- Validierung: `Main.gd` Diagnostics ohne Fehler; Sim-Asset-Check lief ohne harte Fehler (`fail:0`, `warn:2` wegen leerer Epochen + fehlendem Audio-Ordner mit `--allow-empty`).

Dev/Sim: Schritt 2 - Form-Apply schreibt echte User-Assets (2026-03-02 19:18)
---------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `_on_agent_form_apply_pressed()` von Entwurfsspeicher auf echte Persistenz umgestellt.
- `novapolis-sim/scripts/Main.gd`: Datasets-Apply schreibt validierte Records in `user://agent_user_data/datasets/<name>.jsonl` mit `new`/`append_user`-Semantik.
- `novapolis-sim/scripts/Main.gd`: Synonyms-Apply schreibt validierte Eintraege in `user://agent_user_data/synonyms/<name>.json` mit `new`/`append_user`-Semantik.
- `novapolis-sim/scripts/Main.gd`: Basiskontrollen fuer JSON-Gueltigkeit, Pflichtfelder und Zielmodus (`new|append_user`) ergänzt.
- `novapolis-dev/docs/todo.sim.md`: Datasets/Synonyms als Schritt-2-Status erweitert (direkte Apply-Persistenz).
- `novapolis-dev/docs/todo.index.md`: Statushinweis `Sim v2.4` ergaenzt.
- Validierung: Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Agent unten mit dynamischen Form-Masken (Datasets/Synonyms) erweitert (2026-03-02 19:15)
-----------------------------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neuer Bereich `AgentFormPanel` im unteren Agent-Modul (Mode/Target/Name, Payload-Editor, Apply, Status).
- `novapolis-sim/scripts/Main.gd`: dynamische Form-Logik ergaenzt (`_open_agent_form`, `_refresh_agent_form_ui`, Mode-/Target-Zyklen, Apply-Handler).
- `novapolis-sim/scripts/Main.gd`: `Datasets` und `Synonyms` oeffnen im `Author`-Mode nun gezielt diese Maske statt nur statischer Aktionen.
- `novapolis-sim/scripts/Main.gd`: Formular liefert editierbare JSON-Vorlagen und speichert Entwuerfe unter `user://agent_forms/`.
- Wirkung: Nutzer koennen den unteren freien Agent-Bereich als guided Input-Maske nutzen und muessen primär nur Felder/Template ausfuellen.
- Validierung: Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Datasets-Regression behoben (Source getrennt, Run/Stop wieder direkt) (2026-03-02 19:09)
----------------------------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neuer Button `AgentDatasetSourceButton` fuer Source-Umschaltung (`clean/with_failures`).
- `novapolis-sim/scripts/Main.gd`: `Datasets` fuehrt wieder konsistent Start/Stop in `Operate` und `Author` aus; Source-Wechsel wurde in `_on_agent_dataset_source_pressed()` ausgelagert.
- `novapolis-sim/scripts/Main.gd`: UI-Labels nachgezogen (`Source: ...`, `Datasets Run [...]`, `Datasets Stop`) und Source-Button waehrend laufendem Job gesperrt.
- Wirkung: Eigene Datasets lassen sich wieder ohne Modus-Falle starten/erweitern; Source bleibt dabei explizit steuerbar.
- Validierung: Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Agent-Datasets mit Source-Modus + Start/Stop erweitert (2026-03-02 19:05)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Datasets von Placeholder auf reale Kurationslogik erweitert (`_start_dataset_curation`, `_refresh_dataset_runtime_state`).
- `novapolis-sim/scripts/Main.gd`: Source-Modus (`clean`/`with_failures`) in Author-Mode per `Datasets`-Button-Zyklus eingefuehrt.
- `novapolis-sim/scripts/Main.gd`: in Operate-Mode startet/stoppt `Datasets` den Hintergrundprozess (`curate_dataset_from_latest.py`), inkl. Laufstatus und Runtime-Events `AGENT_DATASETS`.
- `novapolis-sim/scripts/Main.gd`: Modulanzeige kombiniert jetzt Datasets-Status mit Eval-Summary im Agent-Bereich.
- `novapolis-dev/docs/todo.sim.md`: Datasets-Punkt als offene Aufgabe belassen, aber Vorstufe auf den neuen Implementierungsstand aktualisiert.
- `novapolis-dev/docs/todo.index.md`: Statushinweis `Sim v2.1` hinzugefuegt.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Agent-Eval Suite-Auswahl + Start/Stop im Hub (2026-03-02 19:01)
------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neuer `AgentEvalSuiteButton` im Agent-Modul hinzugefuegt.
- `novapolis-sim/scripts/Main.gd`: Suite-State (`neutral/rpg/quality_de`) und Handler `_on_agent_eval_suite_pressed()` implementiert.
- `novapolis-sim/scripts/Main.gd`: `Eval Run` auf Start/Stop-Logik erweitert; bei aktivem Lauf wird per erneutem Klick ein Stop (`OS.kill`) ausgeloest.
- `novapolis-sim/scripts/Main.gd`: Eval-Starts laufen nun ueber `scripts/agent/run_eval.py` mit suite-spezifischen Argumenten/Paketlisten.
- `novapolis-sim/scripts/Main.gd`: UI-Text/Status nachgezogen (`Suite: ...`, `Eval Start`/`Eval Stop`, Laufstatus inkl. Suite).
- `novapolis-dev/docs/todo.sim.md`: Eval-Run-Suite-Start/Stop-Punkt als erledigt markiert.
- `novapolis-dev/docs/todo.index.md`: Statushinweis `Sim v2.0` aufgenommen.
- Validierung: Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: RP-Panel exklusiv umgesetzt (Hour +1, Auto-Advance, Replay-Seed) (2026-03-02 18:57)
-----------------------------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neues `RpStudioPanel` mit Controls `Hour +1`, `Auto-Advance`, `Replay-Seed`, Status und Rueckweg zum Hub hinzugefuegt.
- `novapolis-sim/scripts/Main.gd`: RP-Panel als exklusiver Submenu-View verdrahtet (`_set_rp_module_exclusive`, Toggle ueber `RP Modul`-Button).
- `novapolis-sim/scripts/Main.gd`: Slot-Navigation und Auto-Advance bei leerem PC-Slot implementiert (`_on_rp_hour_plus_pressed`, `_run_rp_auto_advance`).
- `novapolis-sim/scripts/Main.gd`: Replay-Seed-Anzeige aus `sim_meta.seed` und separate Runtime-Events mit `RP_*`-Tags ergaenzt.
- `novapolis-dev/docs/todo.sim.md`: RP-Panel-Punkte und UI-Controls als erledigt markiert.
- `novapolis-dev/docs/todo.index.md`: neuer Statushinweis `Sim v1.9` fuer RP-Panel-Meilenstein aufgenommen.
- Validierung: Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Systemressourcen-Ueberwachung testweise deaktiviert (2026-03-02 18:51)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: neues Export-Flag `enable_system_resource_monitoring` eingefuehrt (Default: `false`).
- `novapolis-sim/scripts/Main.gd`: `_refresh_system_metrics(...)` fuehrt bei deaktiviertem Flag keine externen Snapshot-Skripte mehr aus (`OS.execute` entfällt).
- `novapolis-sim/scripts/Main.gd`: Agent-UI zeigt bei deaktiviertem Monitoring jetzt klar `System: Monitoring deaktiviert (testweise)`.
- `novapolis-sim/scripts/Main.gd`: auch `AI Status` triggert ohne aktives Flag keinen System-Metrics-Refresh.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Agent-Modul-Refresh und Script-Last entchaerft (2026-03-02 18:47)
-------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Heavy-Refresh im Agent-Modul nun gestaffelt (abwechselnd Metrics/Summary pro `_process()`-Tick statt potentiell gebuendelt).
- `novapolis-sim/scripts/Main.gd`: manueller `AI Status` startet Summary-Refresh verzoegert (`pending + due_ms`), damit kein direktes Doppel-`OS.execute` entsteht.
- `novapolis-sim/scripts/Main.gd`: Busy-Guard fuer Agent-Script-Aktionen (`_agent_action_busy`) verhindert gleichzeitige Action-Summary-Starts.
- `novapolis-sim/scripts/Main.gd`: waehrend Busy-Phase werden relevante Agent-Buttons temporaer deaktiviert und danach automatisch wieder freigegeben.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Hub-Config rechts leicht vergroessert (2026-03-02 18:19)
-----------------------------------------------------------------

- `novapolis-sim/Main.tscn`: `HubConfigPanel` moderat vergroessert (`left 1660 -> 1620`, `bottom 218 -> 264`).
- `novapolis-sim/scripts/Main.gd`: `_HUB_CONFIG_EXPANDED_BOTTOM` auf `264.0` synchronisiert, damit Minimieren/Öffnen mit der neuen Hoehe konsistent bleibt.
- Validierung: Diagnostics fuer `Main.tscn` und `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Karten unten links/mitte/rechts + Hub-Config rechts (2026-03-02 18:09)
-------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: `SimCardPanel`, `ApiCardPanel`, `EvalCardPanel` als untere Dreierreihe positioniert (links/mitte/rechts).
- `novapolis-sim/Main.tscn`: `HubConfigPanel` nach rechts oben verlegt (`left=1660`, `right=1900`).
- Wirkung: rechte Seite oben entlastet und die drei Status-Karten als klare Footer-Reihe gruppiert.
- Validierung: Diagnostics fuer `Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Rechte Hub-Karten nach unten verschoben (2026-03-02 17:56)
------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: `SimCardPanel`, `ApiCardPanel`, `EvalCardPanel` gleichmaessig nach unten versetzt (`+120px`), Abstaende untereinander beibehalten.
- Wirkung: obere Hub-Haelfte wirkt weniger voll; `HubConfigPanel` hat visuell mehr Raum.
- Validierung: Diagnostics fuer `Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Hub-Config kompakt + Beenden-Button + Minimieren/Öffnen (2026-03-02 17:50)
-------------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: `HubConfigPanel` auf dieselbe Hoehe wie `SimCardPanel` gesetzt (`top=44`, `bottom=218`) und Inhalte als kompaktes 2-Spalten-Layout angeordnet.
- `novapolis-sim/Main.tscn`: neuer Button `HubConfigQuitButton` (Text: `Beenden`) hinzugefuegt.
- `novapolis-sim/scripts/Main.gd`: Quit-Handler `_on_hub_config_quit_pressed()` mit `get_tree().quit()` ergänzt.
- `novapolis-sim/scripts/Main.gd`: bisheriger Collapse-Toggle umbenannt auf `Minimieren`/`Öffnen`.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Hub-Config um Schliessen/Oeffnen-Button erweitert (2026-03-02 17:44)
-----------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neuer Button `HubConfigCloseButton` im Header des Config-Panels hinzugefuegt.
- `novapolis-sim/scripts/Main.gd`: Toggle-Logik fuer einklappbares Config-Panel implementiert (`_set_hub_config_collapsed`, `_on_hub_config_close_pressed`).
- Verhalten: Klick auf `Schliessen` blendet den Panel-Inhalt aus und reduziert die Hoehe; derselbe Button wechselt auf `Oeffnen` und stellt den Inhalt wieder her.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Topbar-Textueberlappung im Hub behoben (2026-03-02 17:41)
------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: Topbar-Labels (`HubApiLabel`, `HubPollingLabel`, `HubQueueLabel`, `HubErrorsLabel`) mit festen Breiten versehen und `clip_text=true` gesetzt.
- `novapolis-sim/scripts/Main.gd`: neuer Helper `_compact_reason_text(...)` kuerzt lange API-Reasons fuer die Topbar.
- Wirkung: Lange API-Statuszeilen ueberlagern nicht mehr Polling/Queue/Errors im oberen Headerbereich.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Kurzhaenger vor Ticks reduziert (2026-03-02 17:25)
-----------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `_refresh_system_metrics(false)` wird im `_process()` nur noch ausgefuehrt, wenn das Agent-Modul offen ist.
- Ursache: System-Snapshot nutzt `OS.execute` (PowerShell/Python) synchron und kann im Hub sichtbare Frame-Hitches erzeugen.
- Wirkung: weniger periodische Main-Thread-Blocker im normalen Hub-Betrieb.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: HubConfig-Buttons unten wieder hoverbar/klickbar (2026-03-02 17:08)
-------------------------------------------------------------------------

- Ursache: `HubConfigPanel` lag teilweise im Y-Bereich des `PcLogLabel`; dadurch wurden untere Buttons von dessen Eingabeflaeche ueberdeckt.
- `novapolis-sim/Main.tscn`: `HubConfigPanel` nach oben verlegt (`offset_top: 24`, `offset_bottom: 306`) und damit aus dem Log-Overlay herausgenommen.
- Wirkung: Alle HubConfig-Buttons (inkl. der letzten vier) erhalten wieder Hover-Feedback und Klicks.
- Validierung: Diagnostics fuer `Main.tscn` ohne Fehler.

Dev/Sim: Show-Eval-Toggle robust gemacht und sichtbar rueckgemeldet (2026-03-02 17:04)
-----------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: zentrale Sichtbarkeitsanwendung fuer Modul-Karten in `_apply_card_visibility_now()` gebuendelt.
- `novapolis-sim/scripts/Main.gd`: `Show Eval` setzt jetzt sofort den sichtbaren Zustand und meldet klaren Status im HubConfig-Panel.
- `novapolis-sim/scripts/Main.gd`: bei offenem Agent-/Checks-Subview wird explizit angezeigt, dass die Einstellung gespeichert ist und im Hub sichtbar wird.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Persistente Hub-Konfiguration umgesetzt (2026-03-02 16:59)
-------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neues `HubConfigPanel` hinzugefuegt (Karten-Sichtbarkeit, Refresh-Profil, Default-Panel, Save).
- `novapolis-sim/scripts/Main.gd`: Persistenzfunktionen ergaenzt (`_load_hub_preferences`, `_save_hub_preferences`, `_apply_hub_preferences`, `_set_refresh_profile`, `_open_default_panel_if_configured`).
- `novapolis-sim/scripts/Main.gd`: Hub-Views respektieren jetzt Konfiguration fuer sichtbare Module und starten optional direkt im Default-Panel (`hub|agent|checks`).
- Speicherort: `user://hub_prefs.cfg` via `ConfigFile`.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: Health-Panel auf `local/external/offline/degraded` vereinheitlicht (2026-03-02 16:56)
----------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: neue Ableitungslogik `_derive_health_state(...)` eingefuehrt.
- `novapolis-sim/scripts/Main.gd`: Hub-Topbar (`hub_api_label`) zeigt jetzt Status + Ursache + `last_ok` einheitlich.
- `novapolis-sim/scripts/Main.gd`: API-Card (`api_card_health_label`) und Server-Status (`server_status_label`) auf dieselbe Zustandslogik umgestellt.
- Wirkung: klarer Betriebskontext zwischen lokalem Prozess, externer API, Offline-Zustand und degradiertem Fehlerzustand.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Dev/Sim: GDScript-Shadowing-Warnung in Main.gd gefixt (2026-03-02 16:50)
------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Parameter in `_set_hub_content_visible(...)` von `is_visible` auf `visible_state` umbenannt.
- Wirkung: Warning `SHADOWED_VARIABLE_BASE_CLASS` (Kollision mit `CanvasItem.is_visible`) entfällt.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler.

Dev/Sim: Exklusives Checks-Modul als Baukasten umgesetzt (2026-03-02 16:20)
-------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neues `ChecksStudioPanel` als exklusiver Vollbereich integriert (Back-Button, 2 Spalten fuer Modul/Check-Typ, read-only `ChecksOutputLabel`).
- `novapolis-sim/scripts/Main.gd`: `Run Checks` von Placeholder auf echte UI-/Run-Logik umgestellt (`_set_checks_module_exclusive`, `_refresh_checks_studio_ui`, `_build_check_command`, `_execute_check`).
- `novapolis-sim/scripts/Main.gd`: Baukasten-Prinzip umgesetzt: Spalte 1 waehlt Ziel (`sim|agent|eval|workspace`), Spalte 2 waehlt Check-Art (`smoke|unit|api|lint|full`), optional Modul-Pack-Lauf.
- `novapolis-sim/scripts/Main.gd`: Ausgaben laufen in ein read-only Terminal-Feld (`ChecksOutputLabel`) mit Command- und Exitcode-Nachweis.
- `novapolis-dev/docs/todo.sim.md`: Hub-Core-Punkt `Run Checks` auf erledigt gesetzt und mit Evidenz/Verifikation dokumentiert.
- `novapolis-dev/docs/todo.index.md`: Sim-Statushinweis `v1.6` fuer das neue Checks-Modul ergaenzt.
- Validierung: Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`; Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler.

Dev/Sim: To-do-Fortschritt verifiziert (Headless + Diagnostics) (2026-03-02 16:06)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: Priorisierungspunkt `Hub-Topbar v1` final auf erledigt gesetzt und mit aktueller Revalidierung dokumentiert.
- `novapolis-dev/docs/todo.index.md`: Sim-Statushinweis um Verifikationsstand (`v1.5`) synchronisiert.
- Laufnachweis: Godot Headless-Start `res://Main.tscn` mit `EXITCODE=0`.
- Validierung: Diagnostics fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/Main.tscn` ohne Fehler.

Dev/Sim: Terminologie sinnvoll getrennt (Deutsch + etablierte Tech-Begriffe) (2026-03-02 16:05)
-----------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Agent-UI-Texte auf natuerliche Mischsprache justiert (`Letzte Eval-Runs`, `Success Rate`, `Metrics Setup`).
- `novapolis-sim/scripts/Main.gd`: unnatuerliche Komplett-Eindeutschung reduziert (`keine Laeufe gefunden` -> `keine Runs gefunden`).
- `novapolis-sim/Main.tscn`: Default-Labeltexte entsprechend synchronisiert (`Letzte Eval-Runs`, `Hinweis: Jobs, Artifacts, Experiments, Policy, Release, Audit ...`).
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Agent-Modul-Buttons voll verdrahtet + Umlaut-Texte (2026-03-02 15:57)
---------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: neue Script-Anbindung `agent_actions_script_path` auf `agent_module_actions.py` ergaenzt.
- `novapolis-sim/scripts/Main.gd`: Button-Handler fuer `Datasets`, `Synonyms`, `Finetune`, `Profiles` auf echte Ausfuehrung umgestellt (`_run_agent_action_summary`).
- `novapolis-sim/scripts/Main.gd`: Action-Resultate werden als kompakte Zeilen in `AgentLatestRunsLabel` ausgegeben; Fehlerfaelle sauber abgefangen.
- `novapolis-sim/scripts/Main.gd`: sichtbare UI-Texte auf Umlaute nachgezogen (`Letzte Eval-Läufe`, `nicht verfügbar`, `geöffnet`, `keine Läufe gefunden`).
- `novapolis-sim/Main.tscn`: Agent-UI-Texte mit Umlauten aktualisiert (`Zurueck`/`Laeufe`/Hint-Menueebene).
- `novapolis_agent/scripts/agent_module_actions.py` neu verdrahtet/finalisiert; Timestamp-Formatter fuer Typpruefung korrigiert.
- Validierung: Diagnostics fuer `Main.gd`, `Main.tscn` und `agent_module_actions.py` ohne Fehler.

Dev/Sim: Agent-Modul-Layout fuer bessere Platznutzung optimiert (2026-03-02 15:48)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Exklusivansicht neu ausgerichtet (`_apply_agent_module_layout`) mit deutlich breiteren Action-Buttons und besserer vertikaler Staffelung.
- `novapolis-sim/scripts/Main.gd`: ueberlappende Hub-Elemente in Exklusivansicht entfernt (`PlayPcButton` wird mit Hub-Content ausgeblendet).
- `novapolis-sim/scripts/Main.gd`: `StatusLabel` wird in Agent-Exklusivansicht nicht mehr eingeblendet, um Header-Overlaps zu vermeiden.
- Wirkung: Agent-Modul nutzt den Vollbereich sichtbar besser und bleibt lesbar, ohne Rest-Hub-Ueberlagerungen.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler.

Dev/Sim: Parse-Fix fuer Agent-Modul-Panelvariable (2026-03-02 15:42)
--------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Schreibfehler bei Panel-Referenz korrigiert (`_agent_studio_panel` -> `agent_studio_panel`).
- Wirkung: Parser-Fehler `Identifier "_agent_studio_panel" not declared in the current scope` beseitigt.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler.

Dev/Sim: Agent-Modul exklusiv + letzte Laufprozente integriert (2026-03-02 15:40)
-------------------------------------------------------------------------------

- `novapolis_agent/scripts/latest_eval_summary.py` neu: liest letzte `results_*.jsonl` und liefert pro Run `success_rate_percent`, `items`, `avg_duration_ms` als JSON.
- `novapolis-sim/scripts/Main.gd`: exklusiven Agent-Subview eingefuehrt (`_set_agent_module_exclusive`) mit Rueckweg (`AgentBackButton`) statt kleinem Dock-Panel.
- `novapolis-sim/scripts/Main.gd`: Hub-Inhalte werden beim Agent-Subview gezielt ausgeblendet; Agent-Panel wird auf Vollbereich vergroessert.
- `novapolis-sim/scripts/Main.gd`: Laufauswertung im Agent-Modul verdrahtet (`_refresh_latest_eval_summary`) und als Prozentanzeige in `AgentLatestRunsLabel` dargestellt.
- `novapolis-sim/Main.tscn`: neue Controls `AgentBackButton`, `AgentLatestRunsLabel` im Agent-Modul.
- Validierung: Diagnostics ohne Fehler; `latest_eval_summary.py --count 3` liefert erwartete Run-Prozente.

Dev/Sim: Terminologie auf Agent-Modul vereinheitlicht (2026-03-02 15:18)
-----------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: sichtbare Label konsolidiert (`Agent Studio` -> `Agent-Modul`, `Agent Menu` -> `Agent-Modul`).
- `novapolis-sim/scripts/Main.gd`: Status-/Buttontexte im Togglepfad auf `Agent-Modul` umgestellt (`[offen]`, `geoeffnet/geschlossen`).
- Wirkung: konsistente Benennung im Hub, keine Mischbegriffe zwischen Menu/Studio/Modul mehr.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Agent-Bereich als Untermenue + RP-Einstieg umgesetzt (2026-03-02 15:14)
---------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: Button `PlayPcAudioButton` auf `Agent Menu` umbenannt; `PlayWorldAudioButton` auf `RP Modul` umbenannt.
- `novapolis-sim/scripts/Main.gd`: Agent-Menue-Toggle eingefuehrt (`_agent_submenu_open`, `_update_agent_menu_ui`); der ehemalige PC-Audio-Button blendet jetzt `AgentStudioPanel` ein/aus.
- `novapolis-sim/scripts/Main.gd`: zweiter Schnellbutton als RP-Einstieg verdrahtet (`rp_module_open`, Runtime-Event `RP_MODULE`), statt OGG-Playback.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Agent Studio v1.2 Bedienbarkeit/Telemetry nachgeschaerft (2026-03-02 14:56)
-------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Runtime-Log entflutet, indem `state_update`-Start/End-Eintraege nicht mehr in die Event-Historie geschrieben werden; Historie auf 80 Eintraege vergroessert.
- `novapolis-sim/Main.tscn`: `PcLogLabel` explizit als scrollbar konfiguriert (`scroll_active=true`, `scroll_following=false`).
- `novapolis_agent/scripts/quick_eval.py`: neuer CLI-Parameter `--limit`; Default fuer `QUICK_EVAL_LIMIT` auf 30 angehoben.
- `novapolis-sim/scripts/Main.gd`: Hub uebergibt beim Eval-Start jetzt `--limit` (Export `eval_quick_limit`, Standard 30), damit Quick-Runs nicht zu kurz ausfallen.
- `novapolis_agent/scripts/system_snapshot.py`: GPU-Metrik auf VRAM umgestellt (`gpu_vram_percent`, `gpu_vram_used_mb`, `gpu_vram_total_mb`) statt GPU-Load.
- Validierung: Diagnostics ohne Fehler; `quick_eval.py --help` erfolgreich; `system_snapshot.py` liefert VRAM-Werte im JSON.

Dev/Sim: Agent Studio v1.1 Slice mit Eval-Run und Telemetrie (2026-03-02 14:24)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `Eval Run (quick)` von Placeholder auf echte Prozessausfuehrung (`quick_eval.py`) umgestellt; Laufstatus inkl. Prozentanzeige im Agent-Studio ergaenzt.
- `novapolis-sim/scripts/Main.gd`: Systemmetriken (CPU/RAM/GPU/Temp) als best-effort Polling integriert; `AI Status` erzwingt Sofort-Refresh.
- `novapolis-sim/Main.tscn`: neue Labels `AgentEvalStatusLabel` und `AgentSystemMetricsLabel` fuer Laufstatus/Telemetrie eingefuegt.
- `novapolis_agent/scripts/system_snapshot.py`: neuer Snapshot-Helper fuer leichte Windows-Metriken (CPU/RAM via PowerShell, GPU/Temp via `nvidia-smi` falls vorhanden).
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Agent Studio v1 Slice implementiert (2026-03-02 14:13)
---------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neues `AgentStudioPanel` inkl. `Operate/Author`-Switch und ersten Action-Buttons (`Eval Run`, `Datasets`, `Synonyms`, `Finetune`, `Profiles`, `AI Status`) angelegt.
- `novapolis-sim/scripts/Main.gd`: Operate/Author-Logik verdrahtet (`_on_agent_operate_pressed`, `_on_agent_author_pressed`, `_refresh_agent_studio_ui`) und erste Action-Buttons als Runtime-Events angeschlossen (`AGENT_ACTION ...`, Placeholder-Status).
- Wirkung: Die ersten Agent-Studio-Punkte sind sichtbar und bedienbar, ohne schon die Backend-Jobs fest zu verdrahten.
- `novapolis-dev/docs/todo.sim.md`: erste Punkte unter Agent Studio auf erledigt gesetzt; verbleibende Punkte mit `Vorstufe umgesetzt` konkretisiert.
- `novapolis-dev/docs/todo.index.md`: Statushinweis fuer Agent-Studio-v1 synchronisiert.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Agent-Studio-Menueplan erweitert (2026-03-02 14:04)
-------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: Agent-Modul-Block um expliziten `Operate`/`Author`-Zuschnitt erweitert.
- Ergaenzte Menuepunkte aufgenommen: `Jobs`, `Artifacts`, `Experiments`, `Policy Sandbox`, `Release Gate`, `Audit Trail`.
- Ziel: klare Trennung zwischen Laufbetrieb (Operate) und inhaltlicher Konfiguration (Author) fuer bessere Bedienbarkeit und Governance.
- `novapolis-dev/docs/todo.index.md`: Statushinweis um den erweiterten Agent-Studio-Zuschnitt synchronisiert.

Dev/Sim: Offene Punkte neu sortiert + Agent-Integrationsplan ergaenzt (2026-03-02 13:59)
------------------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: neue kanonische Sektion `Neuordnung offener Punkte nach Zugehoerigkeit` eingefuehrt.
- Sortierung umgesetzt in vier Bloecken: `Hub-Core`, `RP-spezifische Bedienebene`, `Agent-Modul im Hub (Agent Studio)`, `Qualitaet/Governance/Nachweis`.
- Agent-Plan konkretisiert fuer: Eval-Runs, Dataset-Management, Synonym-Management, Finetuning, KI-Entwicklungsstand, Profile, Advanced Settings/Leitplanken.
- `novapolis-dev/docs/todo.index.md`: Sim-Statushinweis und Open-Count auf die neue kanonische Sortierung synchronisiert.
- Validierung: markdownlint + Frontmatter-Check fuer `todo.sim.md`, `todo.index.md`, `donelog.md` erfolgreich.

Dev/Sim: RP-spezifische Slot-/Replay-Controls aus Hub entfernt (2026-03-02 13:29)
-------------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: `HourJumpButton`, `AutoAdvanceCheckBox`, `ReplaySeedLabel` aus der allgemeinen Hub-Ansicht entfernt.
- `novapolis-sim/scripts/Main.gd`: zugehoerige Hub-Verdrahtung und Handler (`_on_hour_jump_pressed`, `_on_auto_advance_toggled`, `_maybe_auto_advance_slot`, `_has_pc_events_for_slot`) entfernt.
- Begruendung: Diese Steuerungen gehoeren in den RP-spezifischen Teil und nicht in den allgemeinen Framework-Hub.
- `novapolis-dev/docs/todo.sim.md`: Punkt als offener RP-Panel-Folgepunkt neu markiert; `novapolis-dev/docs/todo.index.md` Open-Count entsprechend synchronisiert.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: UI-Controls fuer Slotsteuerung und Replay-Seed umgesetzt (2026-03-02 13:24)
-------------------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neue Controls eingefuegt (`HourJumpButton`, `AutoAdvanceCheckBox`, `ReplaySeedLabel`).
- `novapolis-sim/scripts/Main.gd`: Bedienlogik verdrahtet (`_on_hour_jump_pressed`, `_on_auto_advance_toggled`) und Auto-Advance-Mechanik fuer leere Slots implementiert (`_maybe_auto_advance_slot`, `_has_pc_events_for_slot`).
- `novapolis-sim/scripts/Main.gd`: Replay-Seed im linken UI-Bereich sichtbar gemacht (`Replay-Seed: ...`) via `sim_meta.seed`.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Externer Server wird im Hub erkannt (2026-03-02 13:20)
----------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: UI-Statuslogik erweitert, damit bei erreichbarer API ohne lokalen PID (`_server_pid <= 0`) der Zustand als `external detected` angezeigt wird.
- `novapolis-sim/scripts/Main.gd`: Buttontext wird dann auf `Start Local Server` gesetzt, damit klar ist, dass bereits eine externe Instanz verbunden ist.
- `novapolis-sim/scripts/Main.gd`: `_process()` aktualisiert jetzt auch laufend `_update_server_control_ui()`, damit Statuswechsel ohne manuellen Reload sichtbar werden.
- Heuristik: Erkennung basiert auf frischer erfolgreicher Poll-Antwort (`_last_success_ms`) innerhalb eines Intervalls aus `step_interval`.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler.

Dev/Sim: Hub-Schnellaktionen als Platzhalter verdrahtet (2026-03-02 13:14)
-------------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neue Buttons `HubReloadButton` und `HubChecksButton` neben der Serversteuerung ergaenzt.
- `novapolis-sim/scripts/Main.gd`: Quick-Action-Handler umgesetzt (`_on_hub_reload_pressed`, `_on_hub_checks_pressed`) und an Runtime-Event-Log angebunden.
- Verhalten: `Reload Hub` refresht Status-/Topbar-/Kartenanzeige, `Run Checks` schreibt bewusst einen Platzhalter-Event (`CHECKS_PLACEHOLDER`) fuer den spaeteren Task-Orchestrierungsanschluss.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Hub-Serverstart robust gemacht (2026-03-02 13:09)
-----------------------------------------------------------

- `novapolis_agent/scripts/run_sim_server.py` neu angelegt: startet Sim-API via `uvicorn.run("app.api.sim:app", host="127.0.0.1", port=AGENT_PORT|8765, reload=False)` und setzt den Importpfad robust auf `novapolis_agent`.
- `novapolis-sim/scripts/Main.gd`: `server_script_path` auf den neuen Wrapper umgestellt (`res://../novapolis_agent/scripts/run_sim_server.py`).
- `novapolis-sim/scripts/Main.gd`: Laufzeitpruefung `_refresh_server_runtime_state()` ergaenzt, um abgestuerzte/sofort beendete Prozesse als `SERVER_EXITED` sichtbar zu machen statt nur `running (pid=...)`.
- Validierung: Diagnostics fuer `Main.gd` und `run_sim_server.py` ohne Fehler.

Dev/Sim: Hub-Serverstart auf Sim-API korrigiert (2026-03-02 13:04)
---------------------------------------------------------------

- Ursache fuer fehlende Verbindung identifiziert: Hub-Button startete `novapolis_agent/run_server.py` (FastAPI `app.main`, Standardport `8000`), waehrend `SimClient` gegen `127.0.0.1:8765/world/step` pollt.
- `novapolis-sim/scripts/Main.gd`: Default `server_script_path` von `res://../novapolis_agent/run_server.py` auf `res://../novapolis_agent/app/api/sim.py` umgestellt.
- Wirkung: Button startet nun den passenden Sim-API-Server (AGENT_PORT-Default `8765`) und passt damit zum Polling-Endpunkt.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler.

Dev/Sim: Hub-Serversteuerung (Start/Stop) eingebaut (2026-03-02 12:57)
-----------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: neuen Button `ServerToggleButton` sowie Label `ServerStatusLabel` in die Hub-Leiste aufgenommen.
- `novapolis-sim/scripts/Main.gd`: Prozesssteuerung ergaenzt (`_on_server_toggle_pressed`, `_start_local_server`, `_stop_local_server`, `_update_server_control_ui`, `_resolve_python_executable`).
- Startpfad bevorzugt: `res://../.venv/Scripts/python.exe` + `res://../novapolis_agent/run_server.py`; Fallback fuer Python-Binary: `python` im PATH.
- Runtime-Evidenz: Start/Stop-Faelle werden als Events (`SERVER_STARTED`, `SERVER_STOPPED`, `SERVER_*_FAILED`) im Runtime-Log dokumentiert.
- Validierung: Diagnostics fuer `Main.gd` und `Main.tscn` ohne Fehler.

Dev/Sim: Zwei Godot-Warnungen behoben (2026-03-02 12:52)
---------------------------------------------------------

- `novapolis-sim/scripts/scheduler_hook.gd`: Integer-Division-Warnung entfernt, Parent-Index in `_sift_up()` auf bit-shift umgestellt (`(i - 1) >> 1`).
- `novapolis-sim/scripts/Main.gd`: Shadowing-Warnung entfernt, Parametername `is_visible` in Signal/Funktions-Handler auf `visible_state` umbenannt.
- Validierung: Diagnostics fuer `Main.gd` und `scheduler_hook.gd` ohne Fehler.

Dev/Sim: Full-HD gesetzt und Hub-Elemente neu verortet (2026-03-02 12:29)
--------------------------------------------------------------------------

- `novapolis-sim/project.godot`: Viewport-Default auf Full HD gesetzt (`window/size/viewport_width=1920`, `window/size/viewport_height=1080`).
- `novapolis-sim/Main.tscn`: Hub-Topbar horizontal entzerrt (`HubApi/Polling/Queue/Errors`) und Modul-Karten (`Sim/API/Eval`) auf die rechte Spalte mit groesserer Breite/Hoehe verschoben.
- `novapolis-sim/Main.tscn`: linke Inhaltsflaeche (`PcLogLabel`) deutlich vergroessert und Kernlabels/Buttons vertikal neu verteilt, um Ueberlappung bei Full-HD zu vermeiden.
- Validierung: Diagnostics fuer `Main.tscn`, `Main.gd`, `scheduler_hook.gd`, `SimClient.gd` ohne Fehler.

Dev/Sim: Parser-Warnung (Variant-Inferenz) in Main.gd behoben (2026-03-02 12:20)
-------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: `seed`-Wert in `_refresh_module_cards()` nicht mehr per `:=` direkt aus `Dictionary.get(...)` uebernommen.
- Umsetzung: auf typstabile String-Ableitung umgestellt (`seed_text = str(sim_meta.get("seed", "n/a"))`), damit keine implizite Variant-Inferenz mehr auftritt.
- Wirkung: Godot-Hinweis `The variable type is being inferred from a Variant value` (Warning treated as error) fuer diesen Pfad eliminiert.

Dev/Sim: Hub Modul-Karten v1 (read-only) umgesetzt (2026-03-02 12:16)
---------------------------------------------------------------------

- `novapolis-sim/Main.tscn`: drei read-only Hub-Panels angelegt (`SimCardPanel`, `ApiCardPanel`, `EvalCardPanel`) inklusive Status-Labels.
- `novapolis-sim/scripts/Main.gd`: Label-Bindings und `_refresh_module_cards()` ergaenzt; Live-Felder aus vorhandenen Quellen (`get_runtime_status()`, `sim_meta`, Scheduler-Queue, Epoch-/Audio-Praesenz) verdrahtet.
- `novapolis-sim/scripts/Main.gd`: `scan_audio_assets()` eingefuehrt, um Kartenstatus fuer Artefaktpraesenz (OGG vorhanden/nicht vorhanden) read-only darzustellen.
- Validierung: Diagnostics fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/Main.tscn` ohne Fehler.

Dev/Sim: Scheduler-Hook Parse-Fehler behoben (2026-03-02 12:08)
---------------------------------------------------------------

- `novapolis-sim/scripts/scheduler_hook.gd`: problematische `:=`-Zuweisungen auf ungetyptes `=` umgestellt, um `Warning treated as error` bei Variant-Inferenz zu vermeiden.
- Wirkung: Hook kompiliert wieder sauber im Editorbetrieb; Stack-Trace auf `scheduler_hook.gd:30` tritt nicht mehr auf.
- Validierung: Diagnostics fuer `scheduler_hook.gd` und `Main.gd` ohne Fehler; Headless-Start `res://Main.tscn` erfolgreich.

Dev/Sim: Hub-Topbar v1 umgesetzt (2026-03-02 12:02)
---------------------------------------------------

- `novapolis-sim/Main.tscn`: neue Hub-Labels angelegt (`HubTitleLabel`, `HubApiLabel`, `HubPollingLabel`, `HubQueueLabel`, `HubErrorsLabel`).
- `novapolis-sim/scripts/Main.gd`: Topbar-Refresh eingebunden (`_refresh_hub_topbar()` in `_process`) fuer API-/Polling-/Queue-/Fehlerstatus.
- `novapolis-sim/autoload/SimClient.gd`: read-only Snapshot-Methode `get_runtime_status()` bereitgestellt, damit UI-Statusfelder ohne direkte Feldzugriffe gepflegt werden.
- Validierung: Diagnostics fuer `Main.gd`, `SimClient.gd`, `Main.tscn` ohne Fehler; Headless-Start `res://Main.tscn` erfolgreich.

Dev/Sim: Hub-v1 in Sim-Todo festgeschrieben (2026-03-02 11:49)
---------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: neuer Abschnitt `Hub-v1 fuer Framework-Betrieb (konkretisiert 2026-03-02)` ergaenzt.
- Inhaltlich definiert: konkrete Menuepunkte (`Dashboard`, `Sim`, `Agent/API`, `Eval/Training`, `RP/Content`) und zentrale Statusfelder fuer Topbar/Modul-Karten.
- Priorisierung aufgenommen: zuerst Hub-Topbar v1, danach read-only Modul-Karten und Dashboard-Schnellaktionen.

Dev/Sim: Scheduler-Hook als Min-Heap-Schnittstelle vorbereitet (2026-03-02 11:34)
-----------------------------------------------------------------------------------

- Neue Datei `novapolis-sim/scripts/scheduler_hook.gd`: ticklose Queue-API ohne Business-Logik (`enqueue`, `peek_next`, `pop_next`, `pop_due`, `clear`, `size`) inkl. stabiler Ordnungslogik (`t`, `priority`, `seq`).
- `novapolis-sim/scripts/Main.gd`: minimaler Hook-Start (`SchedulerHookRef.new()`), Runtime-Hinweis `SCHEDULER_READY` im Event-Log.
- Ziel gemaess Spec: Schnittstellen/Types vorbereitet, noch keine Scheduling-Entscheidungslogik im Sim-Loop.
- Validierung: Diagnostics fuer `Main.gd` und `scheduler_hook.gd` ohne Fehler; Headless-Start `res://Main.tscn` erfolgreich.

Dev/Sim: Runtime-Event-Duplizierung in Main.gd behoben (2026-03-02 11:30)
--------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: direkte `SimClient`-Signalverbindungen in `_ready()` entfernt, damit State/Status nur noch ueber den Gruppenpfad (`receive_world_state`/`receive_status`) verarbeitet werden.
- Wirkung: `START/END state_update` Eintraege erscheinen nicht mehr mehrfach pro Tick, Runtime-Events bleiben pro Poll-Zyklus eindeutig.
- Validierung: Diagnostics fuer `Main.gd` ohne Fehler und Headless-Start `res://Main.tscn` erfolgreich.

Dev/Sim: Event-Signals in Main.gd umgesetzt und an UI/Log gebunden (2026-03-02 11:22)
---------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Signale `on_action_start`, `on_action_end`, `on_visibility_change`, `on_interrupt` eingefuehrt.
- Signalpfade an bestehende Flows gebunden: State-Update (`START/END state_update`), Statusfehler (`INTERRUPT`), Sichtbarkeitswechsel (`VISIBILITY`) sowie Audio-Aktionen (`play_audio_pc/world`).
- Runtime-Ereignisse in `PcLogLabel` sichtbar gemacht (`Runtime-Events`, begrenzt auf letzte 8 Eintraege), auch im Fallback ohne Epoch-Daten.
- Validierung: Headless-Start `res://Main.tscn` erfolgreich; Diagnostics fuer `Main.gd` ohne Fehler.

Dev/Sim: Phase-1 Punkt 2 umgesetzt - SimClient Polling robuster gemacht (2026-03-02 10:41)
-------------------------------------------------------------------------------------------

- `novapolis-sim/autoload/SimClient.gd`: zentrale Fehlerroutine `_register_failure(...)` eingefuehrt (einheitliche Retry-/Timeout-Statusmeldungen im Format `Retry in ... (Fehler #..., timeout=...)`).
- Neue Exports: `request_timeout` (statt fixem HTTP-Timeout) und `auto_pause_after_failures` (0 = deaktiviert, >0 pausiert Polling nach N Fehlern).
- Auto-Pause implementiert (`_paused_due_to_failures`) mit klarer Statusmeldung und Resume-API (`resume_polling()`) fuer kontrolliertes Fortsetzen.
- Validierung: Headless-Start von `res://Main.tscn` durchgefuehrt; Diagnostics fuer `SimClient.gd` ohne Fehler.

Dev/Sim: Phase-1 gestartet - Verbindungsstatus in Main.gd erweitert (2026-03-02 10:37)
--------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Statusanzeige auf Live-Connection-Monitoring umgestellt (Basisstatus + "letztes OK vor ..." + "Fehlerdauer ...").
- `receive_world_state`/`receive_status` auf einheitliche Handlerpfade (`_on_state_updated`/`_on_status_updated`) umgestellt, damit Status-Tracking konsistent bleibt.
- Validierung: kurzer Godot-Headless-Szenenstart (`res://Main.tscn`) und Diagnostics-Check auf `Main.gd` ohne Fehler.

Dev/Sim: Arbeitsmodus-Hinweis fuer Godot-Schritte in Sim-Todo verankert (2026-03-02 10:33)
-------------------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: am Dokumentanfang unter `Hinweis` eine feste User-Praeferenz ergaenzt.
- Inhalt: Alle Schritte ausserhalb VS Code (insbesondere Godot-Editor) werden kuenftig nur mit expliziter Schritt-fuer-Schritt-Anleitung, Klickpfaden und Erwartungsbild ausgegeben.
- Ziel: Sim-Arbeit fuer Godot-Einstieg reproduzierbar und ohne implizite Annahmen halten.

Dev/Sim: Main.gd Parse-Fix und Godot-API-Loop revalidiert (2026-03-02 10:04)
-------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd`: Variant-Inferenz-Warnungen als Parse-Blocker beseitigt (`var parsed :=`/`var parsed_line :=` auf ungetyptes `=` umgestellt).
- Kommunikationscheck erneut ausgefuehrt: Sim-API lokal gestartet und Godot-Headless-Lauf gegen `res://Main.tscn` durchgefuehrt.
- Nachweis: Sim-State stieg waehrend des kontrollierten Headless-Runs von `tick=8,time=0.8` auf `tick=16,time=1.6` (`tick_delta=8`).
- Extension-Validierung: lokaler Extension-Ordner `C:\Users\FloAu\.vscode\extensions\geequlim.godot-tools-2.5.1` vorhanden; GDScript-Datei ohne aktuelle Diagnostics (`get_errors` auf `Main.gd`: no errors).

Dev/Sim: Sim-Iststand analysiert und Plan im Sim-Board verankert (2026-03-02 09:48)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: neuen Abschnitt `Arbeitsplan Sim-Modul (Analyse 2026-03-02)` ergaenzt (3 Phasen + DoD).
- Analysegrundlage dokumentiert: Godot-Laufzeit (`novapolis-sim/scripts/Main.gd`), API-Client (`novapolis-sim/autoload/SimClient.gd`), Sim-API (`novapolis_agent/app/api/sim.py`), Testbasis (`novapolis_agent/tests/test_api_sim_state.py`, `novapolis_agent/tests/tests_sim_api.py`) und Offline-Checker (`scripts/check_sim_epoch_assets.py`).
- Zielbild priorisiert: erst Laufzeit-Stabilisierung, dann Scheduler/UI-Hooks, dann Qualitaets- und Evidenzpfad.

Dev/Agent: Letzter Agent-Board-Punkt geschlossen (2026-02-27 05:14)
-------------------------------------------------------------------

- `novapolis-dev/docs/todo.agent-board.md`: letzter offener Punkt `VS Code Task-Set fuer Datensatzbau & Training vervollstaendigen` auf erledigt gesetzt.
- `.vscode/tasks.json`: neue Labels hinzugefuegt (`Data: curate from latest (train pack)`, `Data: export+pack (latest results)`, `Train: baseline LoRA (tiny-gpt2, 1-step)`).
- `novapolis_agent/README.md` und `novapolis_agent/docs/runbook.md`: identische Task-Labels aufgenommen, um Doku-Drift zu vermeiden.
- `novapolis-dev/docs/todo.index.md`: Agent-Open-Count synchronisiert (`offen: 1 -> 0`).
- Laufbelege: Curate-CLI `--help` PASS; Export auf historischem quality_de-Resultset ausgefuehrt (`0` Eintraege wegen Source-Path-Drift); Prepare-Pack PASS (`train=90`, `val=10`, `total=100`); Baseline-LoRA-Pipeline PASS (`train_loss=10.4748`, Output `outputs/lora-baseline-vscode`).

Dev/Agent: KI/TTS-Provenance und Nachweisstruktur nachgezogen (2026-02-27 04:57)
-------------------------------------------------------------------------------

- Vollaudit fuer Herkunft/Nachweise erstellt: neue zentrale Datei `novapolis_agent/docs/provenance-register.md` (intern vs. extern, Statusmatrix gruen/gelb/rot).
- Dataset-Herkunft in `novapolis-dev/docs/dataset-provenance.md` auf den kompletten aktiven Bestand erweitert (inkl. `quality_de_*` und `eval-smoke`).
- TTS-Compliance um Runtime-Voice-Nachweispflicht ergaenzt: `novapolis_agent/docs/tts-compliance-policy.md` verlinkt jetzt auf `novapolis_agent/docs/tts-voice-provenance-log.md`.
- Nachweisablage fuer externe Basismodelle vorbereitet: `novapolis_agent/docs/vendor_licenses/huggingface/README.md` (Pflichtkatalog + Zielpfade fuer lokale Lizenzkopien).

Dev/Agent: LoRA-Gates und Baseline-Metriken verbindlich gemacht (2026-02-27 04:45)
------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.agent-board.md`: Punkt `Trainingspaket-Gates und Baseline-Metriken fuer LoRA-Lauf` auf erledigt gesetzt.
- Go/No-Go-Basiswerte dokumentiert (`records>=20`, `filterquote>=0.70`, `dupe_rate<=0.10`) und Pflichtschema fuer Laufprotokolle festgelegt.
- `novapolis_agent/scripts/fine_tune_pipeline.py` robust gemacht (lokale Zeitstempel-Erzeugung statt importfragiler `now_compact`-Imports), damit der Baseline-Entrypoint standalone laeuft.
- Reproduzierbarer Baseline-Run erfolgreich belegt: `fine_tune_pipeline.py` mit `sshleifer/tiny-gpt2`, `batch=1`, `epochs=1`, `max_steps=1`, `lr=0.0002`; Ergebnisartefakte unter `outputs/lora-baseline-20260227_02/`.
- `novapolis-dev/docs/todo.index.md` im selben Lauf synchronisiert (`Agent offen: 2 -> 1`).

Dev/Agent: Monats-Baseline fuer Datensatz-Driftkontrolle umgesetzt (2026-02-27 04:28)
-------------------------------------------------------------------------------

- Neues Skript `novapolis_agent/scripts/eval_drift_report.py` eingefuehrt: KPI-Extraktion (`pass_rate`, `top_failed_checks`, `top_missing_terms`) aus `results_*.jsonl`, Baseline-Vergleich und `ok/warning/blocker`-Status anhand Schwellen.
- Monats-Baseline abgelegt unter `novapolis_agent/eval/results/baselines/training_profiles.2026-02.json`.
- Vergleichsreport reproduzierbar erstellt unter `novapolis_agent/eval/results/drift/training_profiles_drift_2026-02-27.json`.
- Board-Punkt `Datensatz-Driftkontrolle mit Monats-Baseline` auf erledigt gesetzt und Schwellwerte/Rueckkopplung verbindlich im Board dokumentiert.
- `novapolis-dev/docs/todo.index.md` im selben Lauf synchronisiert (`Agent offen: 3 -> 2`).

Dev/Agent: Trainingsprofil-Datensaetze auf je 20 Eintraege erweitert (2026-02-27 02:13)
-----------------------------------------------------------------------------------------

- `novapolis_agent/eval/datasets/training/chronistin_neutral_assistiv.v1.jsonl` von 3 auf 20 Eintraege erweitert.
- `novapolis_agent/eval/datasets/training/chronistin_lore_intensiv.v1.jsonl` von 3 auf 20 Eintraege erweitert.
- `novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl` von 3 auf 20 Eintraege erweitert.
- Schema unveraendert beibehalten (`id`, `slug`, `category`, `profile`, `tags`, `messages`, `source_package`) und ID-Reihen bis `...-020` fortgefuehrt.
- Strict-Validator erfolgreich: `python novapolis_agent/scripts/validate_eval_datasets.py --strict --pattern "novapolis_agent/eval/datasets/training/*.jsonl"` -> `files=3, records=60, ids=60, slugs=60`.

Dev/Agent: Datensatz-Erzeugungspfad verbindlich standardisiert (2026-02-27 02:04)
-------------------------------------------------------------------------------

- In `novapolis-dev/docs/todo.agent-board.md` wurde der naechste offene Punkt abgeschlossen: reproduzierbarer Ablauf `generate_eval_dataset.py -> run_eval.py -> export_finetune.py -> prepare_finetune_pack.py`.
- Optionaler Kurationszweig `curate_dataset_from_latest.py` als integrierter Pfad dokumentiert.
- Mindestfilter verbindlich festgelegt (`include_failures=false`, `min_output_chars>=20`, `dedupe_by_instruction=true`; optionale Schaerfung via `near_dup_threshold>=0.80`).
- E2E-Artefaktkette im Board belegt (Results + Finetune + Train/Val-Dateien unter `novapolis_agent/eval/results/` und `novapolis_agent/eval/results/finetune/`).
- `novapolis-dev/docs/todo.index.md` im selben Lauf synchronisiert (`Agent offen: 4 -> 3`).

Dev/Agent: Kanonische Trainingsprofil-Pakete umgesetzt (2026-02-27 01:50)
-------------------------------------------------------------------------

- Drei Profilpakete fuer die Chronistin angelegt: `chronistin_neutral_assistiv.v1.jsonl`, `chronistin_lore_intensiv.v1.jsonl`, `chronistin_operativ_kurz.v1.jsonl` unter `novapolis_agent/eval/datasets/training/`.
- Strikter Validator-Lauf erfolgreich: `python novapolis_agent/scripts/validate_eval_datasets.py --strict --pattern "novapolis_agent/eval/datasets/training/*.jsonl"` -> `files=3, records=9, ids=9, slugs=9`.
- `novapolis-dev/docs/dataset-provenance.md` um Namensschema/Pflichtmetadaten und Herkunft/Policy der drei Profilpakete erweitert.
- `novapolis-dev/docs/todo.agent-board.md` Punkt abgeschlossen; `novapolis-dev/docs/todo.index.md` synchronisiert (`Agent offen: 5 -> 4`).

Dev/Agent: Eval-Marathon als Qualitaetsanker operationalisiert (2026-02-27 01:11)
-------------------------------------------------------------------------------

- In `novapolis-dev/docs/todo.agent-board.md` wurde der naechste offene Punkt abgeschlossen: verbindliches Betriebsprofil mit KPI-Mindestset, Blocker/Warnung-Triage und reproduzierbarem Receipt-Standard.
- Rueckkopplungsregel verankert: `Blocker -> Jetzt`, `Warnung -> Als naechstes`, `Beobachtung -> Spaeter`.
- `novapolis-dev/docs/todo.index.md` im selben Lauf synchronisiert (`Agent offen: 6 -> 5`).
- Evidenzpfade: `.vscode/tasks.json` (`Eval: suite marathon (~60m, asgi, loud)`), `novapolis_agent/eval/results/`, `novapolis_agent/docs/DONELOG.txt`.

Dev: Archivfenster kanonisiert ohne Datenverlust (2026-02-27 00:18)
--------------------------------------------------------------------

- Kanonisches Archivfenster bleibt `novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md` und `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md`.
- Die vorherigen Dubletten (`pre-2026-02-19`) wurden verlustfrei verschoben nach `novapolis-dev/archive/quarantine/archive-window-dedupe-20260227_0018/`.
- Ziel: ein eindeutiges aktives Archivfenster bei gleichzeitig vollstaendig erhaltener Historie.

Dev: Wochenarchivierung fuer Status/Donelog eingefuehrt (2026-02-27 00:04)
--------------------------------------------------------------------------

- Historische Inhalte aus den aktiven Dateien wurden wochenweise in die vorgesehenen Dev-Archive ueberfuehrt:
  - `novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md`
  - `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md`
- `WORKSPACE_STATUS.md` wurde auf ein aktuelles, scanbares Wochenfenster reduziert.
- `novapolis-dev/docs/donelog.md` wurde auf ein operatives Current-Window reduziert; Historik bleibt in Archivdateien verlinkt.

Dev/Root: Doku-Drift-Audit und Obsoleszenz-Fix (2026-02-26 21:59)
-----------------------------------------------------------------

- Nachweisbare Driftstellen behoben:
  - `WORKSPACE_INDEX.md`: obsolete Eval-Dataset-Verweise entfernt und auf aktuellen `neutral/`, `rpg/`, `quality_de_*`-Bestand umgestellt.
  - `novapolis-dev/docs/tests.md`: obsolete `cvn-agent`-Referenz entfernt; Task-/Testbezug auf Single-Root-Iststand korrigiert.

Dev/Agent: Snapshot-Resync vor Commit (2026-02-26 05:17)
---------------------------------------------------------

- Commit-Hook (`snapshot_gate`) blockierte aufgrund veralteter `stand`-Werte in gestagten Markdown-Dateien.
- Frischer Lock gesetzt und `stand` in den betroffenen Dateien auf den Lock-Zeitwert synchronisiert.

Archivverweise
--------------

- Dev-Historikfenster (neu): `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md`
- Vorheriges Dublettenfenster (verlustfrei verschoben): `novapolis-dev/archive/quarantine/archive-window-dedupe-20260227_0018/donelog_dev.window-archive.pre-2026-02-19.md`
- Konsolidierter historischer Ziellog: `novapolis-dev/archive/docs/donelogs/donelog_dev.md`

