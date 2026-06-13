---
stand: 2026-06-13 09:19
update: Der Dev-DONELOG fuehrt jetzt den Online-Faktencheck zur Mini-first-Regel vor reviewbarem GPT-5.3-Codex-Handoff.
checks: snapshot-lock PASS (2026-06-13 07:10); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc changed-dev-md PASS (2026-06-13 07:08); C:/Users/FloAu/AppData/Local/Programs/Python/Python313/python.exe scripts/check_frontmatter.py changed-dev-md PASS (EXITCODE=0, 2026-06-13 07:08); C:/Users/FloAu/AppData/Local/Programs/Python/Python313/python.exe scripts/check_todo_index_sync.py PASS (2026-06-13 07:08).
---
Dev/Governance: Mini-first-Regel vor GPT-5.3-Codex-Handoff nach Online-Faktencheck geschaerft (2026-06-13 07:08)
-----------------------------------------------------------------------------------------------------------------------------

- Online-Faktencheck 2026-06-13 gegen GitHub-/VS-Code-Doku: Copilot usage-based billing rechnet nach Modell plus Input-/Output-/Cached-Tokens; `GPT-5.3-Codex` liegt in der offiziellen Copilot-Preistabelle je Tokenart rund 7x ueber `GPT-5 mini`, waehrend Legacy-Multiplikatoren dieselbe Richtung bestaetigen, aber nicht die neue Primaerlogik sind.
- [todo.dev.md](todo.dev.md) fuehrt daraus jetzt die operative Mini-first-Regel ab: `GPT-5 mini` muss Befund, Planung, Suche, Diff-Review, Check-Auswertung und Handoff-Vorbereitung maximal leisten; `GPT-5.3-Codex` darf erst nach belegter Mini-Ausschoepfung fuer praezise Umsetzungs-/Abschlusslaeufe angeboten werden.
- Codex-Handoffs bleiben standardmaessig reviewbar (`send:false`/kein Auto-Submit). Zulassige Eskalationsgruende sind jetzt im Board konkret benannt; reine Board-/Index-/DONELOG-Pflege, Lint-Auswertung oder unspezifisches "zur Sicherheit" reichen nicht.

Archiv: 5 Dev‑Einträge verschoben (2026-06-13 07:14)
-------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=5) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: `Schonmodus fuer Test- und Check-Tasks`, `run_sim_export_smoke`, `run_sim_headless_verify`, `check_sim_hub_prefs_contract`, `training_release_gate`.
- Prüfungen: Dateien und zugehoerige Tests existieren im Repo; Test‑Artefakte (`outputs/test-artifacts/junit.xml`, `.pytest_cache`) enthaelt die zugehörigen Testcases; Validatoren sollen anschliessend `markdownlint` + `check_frontmatter.py` bestätigen.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Archiv: weitere 5 Dev‑Einträge verschoben (Batch 8, 2026-06-13 08:10)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=8) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: `Kanonischer Typenlauf (types)`, `End-to-End Product Gate v1`, `Donelog-Hygiene`, `Logs-Policy`, `Stand-Freshness-SLA`.
- Prüfungen: Referenzierte Files und Skripte existieren im Repo; Validatoren (`markdownlint` + `check_frontmatter.py`) deferred per User-Directive.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Archiv: weitere 2 Dev‑Einträge verschoben (Batch 9, 2026-06-13 08:20)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=9) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: `runpy Warnings: Coverage`, `Nicht-kanonische Unterordner-READMEs`.
- Prüfungen: Referenzierte Files und Skripte existieren im Repo; Validatoren (`markdownlint` + `check_frontmatter.py`) deferred per User-Directive.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Archiv: weitere 5 Dev‑Einträge verschoben (Batch 10, 2026-06-13 08:30)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=10) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: `Full-Gate wieder gruen machen`, `Coverage-Sprint Richtung 91%`, `Punkt-3-Strategie aktivieren`, `Active-Surface-Index erstellen`, `Truthfulness-Drift in novapolis-dev/README.md`.
- Prüfungen: Referenzierte Files und Skripte existieren im Repo; Validatoren (`markdownlint` + `scripts/check_frontmatter.py`) deferred per User-Directive.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Archiv: weitere 5 Dev‑Einträge verschoben (Batch 11, 2026-06-13 08:40)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=11) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: `Logsprache, Reader-Surface, Python-Version, Support-A-B Tie-Break`, `Reader-Surface/Runtime-Doku Konsolidierung`, `Ruff-/Black-Drift (Target-Scope)`, `Wochenpruefung Ruff/Black Restdrift`, `Schonmodus fuer Test- und Check-Tasks`.
- Prüfungen: Referenzierte Files existieren im Repo (scripts, tests, reports); Validatoren (`markdownlint` + `scripts/check_frontmatter.py`) deferred per User-Directive.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Archiv: weitere 25 Dev‑Einträge verschoben (Batch 12, 2026-06-13 08:50)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=12) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: mehrere abgeschlossene Dev-Einträge (Logsprache/Reader-Surface, Reader-Surface/Runtime-Doku, Ruff/Black-Drifts, runpy Warnings, Schonmodus, Text-RPG Product Gate, Nicht-kanonische READMEs, Snapshot-Gate, Kern-SSOT/Headings-Index, Redundanzreduktion, Board-Index-Härtung, Coverage-Strategie, Active-Surface-Index, Truthfulness-Drift, tts-exporter-spec, TODO-Index-Guard, Cadence/KPI-Review u.a.).
- Prüfungen: Referenzierte Files existieren im Repo; Validatoren (`markdownlint` + `scripts/check_frontmatter.py`) deferred per User-Directive.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Archiv: weitere 5 Dev‑Einträge verschoben (Batch 4, 2026-06-13 07:35)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=4) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: `Stil- und Konsistenzlauf`, `Python-Workspace-Tasks: shell->process`, `Snapshot-/Pre-Commit-Retry-Pfad`, `Community-/Maintainer-Doku-Paket`, `ADR-Ordner (0001/0002)`.
- Prüfungen: Referenzierte Files und Skripte existieren im Repo (`novapolis-dev/docs/process/...`, `.vscode/tasks.json`, `scripts/pre_commit.py`, `scripts/snapshot_gate.py`, `SUPPORT.md`, `RELEASE.md`, `docs/adr/*`); Test‑Artefakte und Tasks belegen die Implementierung; Validatoren werden nach Abschluss aller Batches ausgeführt.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Archiv: weitere 5 Dev‑Einträge verschoben (Batch 2, 2026-06-13 07:20)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=2) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: `Doc-Freshness-Scope`, `WORKSPACE_INDEX.md` Nachzug, `Docs: sync after checks` Helper, `Workspace Trees` (update_workspace_tree_dirs), `Active Surface Index`.
- Prüfungen: Dateien und zugehoerige Tests existieren im Repo; Test‑Artefakte (`outputs/test-artifacts/junit.xml`, `.pytest_cache`) enthaelt die zugehörigen Testcases; Validatoren sollen anschliessend `markdownlint` + `check_frontmatter.py` bestätigen.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Archiv: weitere 5 Dev‑Einträge verschoben (Batch 3, 2026-06-13 07:26)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=3) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Betroffene Einträge: `Audit‑Rest & Python‑Stil`, `Workspace‑Audit‑Segmente W2 & W5`, `Wochenabschluss‑Schonpfad (run_with_cpu_limit)`, `Logsprache & Support‑A‑B Tie‑Break`, `Reader‑Surface & Runtime‑Doku Konsolidierung`.
- Prüfungen: Dateien und zugehoerige Tests existieren im Repo; Test‑Artefakte (`outputs/test-artifacts/junit.xml`, `.pytest_cache`) enthaelt die zugehörigen Testcases; Validatoren sollen anschliessend `markdownlint` + `check_frontmatter.py` bestätigen.
- Receipt: snapshot-lock PASS (2026-06-13 07:10); post-archive validators: pending (run on request).

Dev/Governance: VS-Code-Governance-Surface und AI-Credits-Fakten als belastbare Umbaugrundlage nachgezogen (2026-06-13 06:23)
----------------------------------------------------------------------------------------------------------------------------

- [process/vscode-agent-governance-surface.ssot.md](process/vscode-agent-governance-surface.ssot.md) fuehrt jetzt als eigener Datensatz, wie VS Code die aktive Governance tatsaechlich verarbeitet: Always-on Instructions, scoped `*.instructions.md`, Custom Agents, Hooks, Prompt Files, MCP-Server, Workspace-/User-/Org-Prioritaeten sowie relevante Settings und Diagnostikpfade.
- [process/model-credits-optimization-plan.ssot.md](process/model-credits-optimization-plan.ssot.md) ist im selben Lauf auf AI-Credits statt Legacy-Request-Primat nachgezogen. Explizit festgehalten sind jetzt der Logging-Waechter als Orchestrierungsinstanz, die VS-Code-Customization-Surface als Vorphase des eigentlichen Policy-Umbauplans und die Regel, dass Deutsch als Repo-Sprache bleiben kann, waehrend Tokenmenge, Kontextgroesse, Reasoning-Level und Modellwahl die eigentlichen Kostentreiber sind.
- [todo.dev.md](todo.dev.md) und [todo.index.md](todo.index.md) fuehren denselben Nachzug im selben Lauf mit, damit die spaetere Umsetzung nicht auf veralteten Annahmen wie `workspaceInstructions` als einzigem Governance-Anker oder `premium requests` als Primaerlogik aufsetzt.

Dev/Governance: Plan fuer credits-optimierte Modellnutzung angelegt und Scope-Dateien erfasst (2026-06-12 22:49)
--------------------------------------------------------------------------------------------------------------

- Startlauf fuer die Umstellung auf credits-effiziente Arbeitsweise ist jetzt in [process/model-credits-optimization-plan.ssot.md](process/model-credits-optimization-plan.ssot.md) dokumentiert.
- Der Lauf hat die initial betroffenen Governance-/Behavior-Dateien explizit erfasst: `.github/agents/novapolis-workspace-navigator.agent.md`, `.github/agents/novapolis-rp-szenenlabor.agent.md`, `.github/copilot-instructions.md` und [copilot-vscode-usage.md](copilot-vscode-usage.md).
- Das Dev-Board fuehrt denselben Startpunkt jetzt offen in [todo.dev.md](todo.dev.md); [todo.index.md](todo.index.md) ist im selben Lauf auf `Dev offen: 1` synchronisiert.

Dev/Governance: Alte Broken-Venv in Quarantaene verschoben und Drift-Guard gesetzt (2026-06-12 22:38)
----------------------------------------------------------------------------------------------------

- Der lokale Altordner `.venv_broken_py312_20260612_221541` wurde aus dem Workspace-Root nach [../archive/quarantine/.venv_broken_py312_20260612_221541-20260612-2238](../archive/quarantine/.venv_broken_py312_20260612_221541-20260612-2238) verschoben, damit Root nicht mehr durch untracked Paketmassen blockiert wird.
- [.gitignore](../../.gitignore) ignoriert jetzt zusaetzlich `/.venv_broken_py*/` sowie `/novapolis-dev/archive/quarantine/.venv_broken_py*/`, damit derselbe Drift kuenftig nicht erneut im aktiven Git-Status auftaucht.
- Scope bewusst minimal: keine inhaltlichen Aenderungen an Sim-/Agent-/RP-Fachdateien; nur Quarantaene-Nachzug plus Doku.

Sim/UI: Topbar-Status entdoppelt und rote Statuszeile dauerhaft entfernt (2026-06-12 13:35)
--------------------------------------------------------------------------------------------

Sim/UI: Auto-Start Server implementiert (2026-06-12 12:00)
-------------------------------------------------------

- `novapolis-sim` - Implementiert: `Auto-Start Server` Einstellung im Hub-Config-Panel, persistente Preference `server_autostart_enabled`, Auto-Start-Trigger nach 2 aufeinanderfolgenden SimClient-Poll-Fehlern sowie Topbar Settings<->Terminal Toggle.
- Geänderte Dateien: [novapolis-sim/scripts/Main.gd](../../novapolis-sim/scripts/Main.gd), [novapolis-sim/scripts/hub_config_controller.gd](../../novapolis-sim/scripts/hub_config_controller.gd), [novapolis-sim/scripts/hub_layout_controller.gd](../../novapolis-sim/scripts/hub_layout_controller.gd), [novapolis-sim/Main.tscn](../../novapolis-sim/Main.tscn)
- Verify: Lokaler Headless-Check `Checks: sim headless verify` (empfohlen) und UI-Quicktest in Godot-Editor.


- `novapolis-sim/scripts/Main.gd` blendet die rote Hub-Statuszeile jetzt dauerhaft aus (`StatusLabel`), sodass Fehler-/Serverzustand nicht mehr ein drittes Mal separat im Hub erscheint.
- Die API-Chip-Zeile in der Topbar wurde auf `API: <state> | last_ok=<age>` reduziert; redundante `reason=`-Wiederholung faellt damit aus dem Hauptblick.
- Im selben Lauf wurden unbeabsichtigte Fremd-Hunks in `Main.gd` (`_apply_agent_restpoint_summary_result`) sauber zur vorherigen Fallback-Logik zurueckgesetzt.
- Verify: `Checks: sim headless verify` PASS mit `SIM_VERIFY: OK`.

Sim/UI: Replay aus Hub entfernt, Topbar-Aktionen hochgezogen, Telemetry freigestellt (2026-06-12 13:20)
------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` blendet `HubReplayPanel` und `HubConfigPanel` im Hauptmenue jetzt konsequent aus; die bisherigen Replay-/Config-Bloecke sind damit nicht mehr Teil der Hub-Startoberflaeche.
- `novapolis-sim/Main.tscn` verschiebt `HubConfigQuitButton` und `HubConfigCloseButton` auf Root-Ebene (Topbar-Aktionen ohne eigenen Config-Rahmen) und setzt zusaetzlich `clip_text=true` fuer lange API-/Eval-Zeilen, damit kein Text mehr ueber Kartenraender laeuft.
- `novapolis-sim/scripts/hub_layout_controller.gd` legt die beiden Topbar-Aktionen responsiv aus und reserviert keine Stack-Flaeche mehr fuer ausgeblendete Replay-/Config-/Chat-Bloecke; Telemetry-Cards starten tiefer, sodass die Ueberschrift nicht mehr halb ueberdeckt wird.
- Verify: `Checks: sim headless verify` PASS mit `SIM_VERIFY: OK`.

Sim/UI: Hub-Spacingschnitt nach Screenshot-Befund (2026-06-12 13:05)
--------------------------------------------------------------------

- `novapolis-sim/scripts/hub_layout_controller.gd` nutzt die Hauptflaeche links jetzt besser: die Ops-Spalte wurde enger geklammert, und bei ausgeblendetem Hub-Chat reserviert das Layout keinen toten Zwischenraum mehr.
- Derselbe Schnitt dockt `HubConfigPanel` unter dem Replay-Block in der rechten Spalte, statt den Bereich wie zuvor als entkoppelte Restflaeche wirken zu lassen.
- `novapolis-sim/Main.tscn` blendet den kleinen Telemetry-Subtext (`HubTelemetrySubLabel`) aus und bereinigt den Ops-Subtext auf `Server, Module und Checks`, damit doppelte bzw. veraltete Lesart wegfaellt.
- Verify: `Checks: sim headless verify` PASS mit `SIM_VERIFY: OK`.

Sim/UI: Telemetry fixiert, Hub-Chat ausgeblendet, Terminal-Autoscroll aktiv (2026-06-12 12:45)
----------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` zeigt Telemetry-Karten im Hub jetzt durchgehend an und blendet das Hub-Chat-Panel im Hauptmenue konsequent aus. Die Card-Sichtbarkeit wird nicht mehr aus alten Pref-Toggles abgeleitet.
- Derselbe Lauf aktiviert Auto-Scroll fuer das Haupt-Terminal (`PcLogLabel`) und fuer die Checks-Ausgabe; neue Eintraege springen damit automatisch ans Ende.
- `novapolis-sim/scripts/hub_config_controller.gd` und `novapolis-sim/Main.tscn` ziehen den UI-Schnitt nach: Telemetry-Toggle-Schaltflaechen bleiben dauerhaft verborgen und tauchen auch beim Panel-Collapse nicht wieder auf.
- Verify: `Checks: sim headless verify` PASS mit `SIM_VERIFY: OK`.

Sim/UI: Hub-Navigation in Main.gd strukturell bereinigt (2026-06-12 12:20)
--------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` fuehrt die Hub-Navigation jetzt ueber eine zentrale Toggle-Route (`_toggle_operator_module`) und eine gemeinsame UI-Synchronisierung (`_sync_hub_module_menu_ui`) statt mehrfach verteilter Einzelpfade.
- Ziel des Laufs ist bewusst Architektur-Bereinigung vor Feature-Ausbau: weniger duplizierte Toggle-/Statuslogik, klarere Modulgrenzen zwischen Hub, Agent, Checks und RP ohne neue Fachfunktionen.
- Der Lauf behaelt den bestehenden Bedienpfad bei (Buttons und Panel-Exklusivitaet unveraendert), reduziert aber Legacy-Verzweigungen als Grundlage fuer den naechsten UI-Neuschnitt.

Sim UI Neustart: Plan angelegt (2026-06-12 12:00)
------------------------------------------------

- [novapolis-dev/docs/process/sim-ui-restart-plan.md](process/sim-ui-restart-plan.md) angelegt als schlanker Fahrplan fuer den Neuanfang der Sim-Oberflaeche. Erste Schritte: Scaffolding in `novapolis-sim/Main.tscn` planen, Headless-Verify als Akzeptanzkriterium.

Nächster Schritt: Umsetzung in kleinem, commitbarem Patch-Set auf Feature-Branch `feature/sim-ui-restart`.

RP-Runtime/SSOT: Reflex-Profilkante und Turn-15-Wahrnehmung festgeschrieben (2026-05-20 17:39)
-----------------------------------------------------------------------------------------------

- [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md) haelt die freigegebene Lesart fest: Bindungs-/Regulationsnaehe glaettet Reflex nicht; Weltendruck, Tunnelgefahr, Mangel und Anomaliekontext halten `CALM/ALERT/CRISIS` kantig.
- [../../novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](../../novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt Turn 15 als reinen Reflex-Wahrnehmungszug. `CRISIS`-Kokon/Vollschutz bleibt als Notfallimpuls lesbar, wird aber nicht ausgeloest; Ronja, Draisine, Schuttkeil und technische Antworten bleiben ohne neues Delta.
- [../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/mind.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/mind.md), [../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/entity.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/entity.md) und [../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/relationships.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/relationships.md) fuehren denselben Runtime-Arbeitsstand ohne Kontrollfreigabe oder neue Symbiose-Stufe.
- [todo.rp.md](todo.rp.md) und [todo.index.md](todo.index.md) markieren Zug A jetzt mit Turn 14/15 als belegt; offen bleiben Zug B, Zug C und Reflex' Herkunftsaudit bei `RP=1`. Der Commit-Lauf synchronisiert zusaetzlich die Frontmatter-Freshness aller zu committenden RP-/Doku-Dateien.

RP-SSOT: Stop-/Freigabe-Kanonisierung chirurgisch entfernt (2026-05-20 13:46)
--------------------------------------------------------------------------------

- [../../novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md](../../novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md) und [../../novapolis-rp/database-rp/00-admin/Curated-Konfliktliste.md](../../novapolis-rp/database-rp/00-admin/Curated-Konfliktliste.md) entkoppeln Reflex-Control und Kontakt-Guard jetzt von unbelegten formalen Stop-/Freigabe-Kommandos.
- [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md), [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md), [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lumen.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lumen.md), [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo.md), [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md) und [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Kora-Malenkov.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Kora-Malenkov.md) fuehren jetzt belegpflichtige Abbruch-, Distanz- und Consent-Logik statt vorausgesetzter Kommandophrasen.
- [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex-Wissensstand-Trainingsstand.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex-Wissensstand-Trainingsstand.md), [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lumen-Wissensstand-Trainingsstand.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lumen-Wissensstand-Trainingsstand.md) und [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo-Wissensstand-Trainingsstand.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo-Wissensstand-Trainingsstand.md) markieren formale Stop-/Request-Kommandos als unbelegt und offen bis zur ausgespielten Szene.
- [todo.rp.md](todo.rp.md) dokumentiert den Einschub im offenen Reflex-/Nordlinie-Punkt; [todo.index.md](todo.index.md) bleibt synchron bei `RP=1`.

RP-Runtime: Turn 14 klaert Ronja/Reflex-Geste als Naehesignal (2026-05-20 07:46)
--------------------------------------------------------------------------------

- [../../novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](../../novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt jetzt Turn 14. Die kurze Ronja/Reflex-Geste ist als bestaetigendes Naehesignal dokumentiert: Ronja zeigt Reflex, dass sie ihn wahrnimmt, nicht vergessen hat und froh ist, dass er da ist.
- [../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/mind.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/mind.md), [../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/mind.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/mind.md), [../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/relationships.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/relationships.md) und [../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/relationships.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/relationships.md) halten das Delta als Runtime-Arbeitsstand ohne technische Freigabe, Kontrollfreigabe oder neue Symbiose-Stufe.
- [todo.rp.md](todo.rp.md) fuehrt Zug A des offenen Drei-Zug-Abschlusskorridors als belegt; [todo.index.md](todo.index.md) bleibt synchron bei `RP=1`.

RP-Board: Drei-Zug-Abschlusskorridor und Reflex-Herkunftsaudit als offener Punkt angelegt (2026-05-20 07:06)
----------------------------------------------------------------------------------------------------------------

- [todo.rp.md](todo.rp.md) fuehrt jetzt wieder einen offenen RP-Punkt. Der naechste saubere Abschlusskorridor fuer `d5-c6-nordlinie-sanierung-01` ist als Drei-Zug-Folge geplant: Ronja/Reflex-Wirkung, konservative Draisine-Entscheidung mit `Jonas/Pahl/Lumen`, danach Koras/Echos Rueckmeldung nach eigener Schuttkeil-Pruefung.
- Derselbe Boardpunkt zieht zugleich ein Herkunftsaudit fuer Reflex offen nach: Aktive SSOT in [../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md) und [../../novapolis-rp/database-rp/01-factions/novapolis/Novapolis.md](../../novapolis-rp/database-rp/01-factions/novapolis/Novapolis.md) fuehren aktuell nur `D5-Reaktor-Stabilisierung`, waehrend die Datenrettungsreview noch Drift `Jonas' Werkstatt (Geburtsort Reflex)` traegt.
- [todo.index.md](todo.index.md) fuehrt denselben Stand jetzt bei `RP=1`; die uebrigen Modul-Boards bleiben unveraendert.

RP-Runtime: Turn 13 mit Koras Eigenpruefung und konservativer Draisine-Debatte nachgezogen (2026-05-20 06:18)
--------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](../../novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt jetzt Turn 13: Kora bestaetigt die Schuttkeil-Frage selbst aus dem C6-Funkraum und geht anschliessend eigenhaendig an die Kante, statt ueber Funk eine freie Materialentscheidung zu treffen.
- [novapolis-rp/database-curated/staging/rp-runtime/entities/locations/c6/state.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/locations/c6/state.md) und [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/kora-malenkov/entity.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/kora-malenkov/entity.md) sowie [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/kora-malenkov/mind.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/kora-malenkov/mind.md) fuehren denselben Zug als enge Eigenpruefung statt als Fernfreigabe.
- [novapolis-rp/database-curated/staging/rp-runtime/entities/assets/draisine-transportmodul/state.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/assets/draisine-transportmodul/state.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/locations/d5/state.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/locations/d5/state.md) sowie die Jonas-/Pahl-Dossiers ziehen die Draisine-Debatte vom unbelegten Motor auf konservative Hand-/Schubvarianten, ohne daraus Testlauf, Freigabe oder Bauentscheid zu machen.
- Ronjas und Reflex' Runtime-Dossiers halten den kurzen koerperlichen Kontakt aus demselben Zug bewusst offen: belegt, aber noch nicht in eine harte Naehe- oder Bedeutungsbehauptung promoted.

Dev/RP-Governance: Explizite PC-Agency-Grenze fuer RP-Agenten verankert (2026-05-19 07:18)
---------------------------------------------------------------------------------------------

- [.github/instructions/rp-docs.instructions.md](../../.github/instructions/rp-docs.instructions.md) fuehrt jetzt eine harte Regel dafuer, dass die KI Spielercharaktere oder aktuell usergesteuerte Figuren nicht eigenmaechtig steuert. Ohne konkrete User-Vorgabe oder turn-spezifische Delegation duerfen Entscheidung, Dialog, innere Reaktion und koerperliche Handlung eines PCs nicht als KI-Zug festgelegt werden.
- Dieselbe Datei fuehrt dazu einen expliziten Matrix-Eintrag `R-RP-PC-AGENCY`, damit dieselbe Grenze nicht nur als Fliesstext, sondern auch als scanbare RP-Governance-Regel lesbar bleibt.
- [.github/agents/novapolis-rp-szenenlabor.agent.md](../../.github/agents/novapolis-rp-szenenlabor.agent.md) zieht die Regel fuer den Ausspielmodus nach: In laufenden PC-Szenen liefert der Agent ohne Delegation nur offene Anschlusslagen, NPC-/Umweltreaktionen auf bereits belegte Spielerhandlungen oder klar getrennte Handlungsoptionen statt eines fortgeschriebenen PC-Zugs.
- Der Lauf bleibt bewusst eng: keine Runtime-Datei und keine aktive Session wurde umgeschrieben; zuerst wurde die fehlende Governance-Luecke geschlossen.

Dev/Guidance: Copilot-Leitfaden und Root-Kontextsprache an den realen Agent-Betrieb angeglichen (2026-05-19 05:09)
----------------------------------------------------------------------------------------------------------------

- [novapolis-dev/docs/copilot-vscode-usage.md](copilot-vscode-usage.md) fuehrt `Plan` jetzt nicht mehr als starre Produktgrenze ohne Edit-Pfad, sondern als planungsorientierten Modus mit versionsabhaengigem Uebergang zu ausfuehrenden Agent-Flows; bindend bleibt dafuer ausdruecklich die SSOT unter [.github/copilot-instructions.md](../../.github/copilot-instructions.md).
- Derselbe Leitfaden benennt fuer mehrschrittige Arbeit nicht mehr das veraltete Werkzeuglabel `manage_todo_list`, sondern die jeweils aktuelle Plan-/Todo-Funktion des Agenten. Damit bleibt die Guidance stabil, auch wenn VS Code oder Copilot interne Toolnamen aendern.
- [README.md](../../README.md) beschreibt `github.copilot.chat.workspaceInstructions` jetzt enger als SSOT-Anker mit optionalen zusaetzlichen Kontextpfaden; die bisherige Formulierung war breiter als die reale Workspace-Einstellung in [.vscode/settings.json](../../.vscode/settings.json).
- Parallel fuehrt [.github/copilot-instructions.md](../../.github/copilot-instructions.md) beim STOP-Gate jetzt explizit, dass eine klare User-Anweisung im aktuellen Chat die Freigabe fuer einen Hard-Trigger selbst darstellen kann, solange Ziel und Scope eindeutig sind; bei Mehrdeutigkeit oder Scope-Drift bleibt STOP unveraendert hart.

Dev/Governance: Wochenabschluss 2026-05-18 nach Tree- und Freshness-Drift wieder auf Gruenstand gezogen (2026-05-18 22:32)
----------------------------------------------------------------------------------------------------------------------

- Seit dem letzten Wochenabschluss kam kein neuer Repo-Commit hinzu; `git log --since="2026-05-11 12:59"` zeigt weiter nur `855a168`. Der Arbeitsstand blieb damit fachlich stabil; der Wochenabschluss war erneut ein reiner Governance- und Hygiene-Lauf.
- Der initiale Vollcheck [.tmp/results/reports/checks_report_20260518_222210.md](../../.tmp/results/reports/checks_report_20260518_222210.md) fiel nur an zwei Hygiene-Resten: `doc-freshness` mit 23 stale aktiven/Referenzdokus sowie dem Pytest-Gate fuer stale Workspace-Trees `workspace_tree.txt` und `workspace_tree_full.txt`.
- `workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt` und `workspace_tree_local.txt` sind im selben Lauf neu erzeugt; der fokussierte Test `novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py` ist danach wieder gruen. Die stale Root-, Dev-, Agent- und RP-Referenzdokus wurden anschliessend gezielt ueber `scripts/sync_docs_after_checks.py` nachgezogen; der Freshness-Recheck endet danach wieder mit `findings=0`.
- Der finale Recheck [.tmp/results/reports/checks_report_20260518_222833.md](../../.tmp/results/reports/checks_report_20260518_222833.md) ist vollstaendig PASS. `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty` bleibt bei `summary=fail:0,warn:0`; der separate Coverage-Gate-Lauf bleibt mit `709 passed` und `92.19%` klar ueber Hard Gate und Qualitaetsziel.
- KPI-Hygiene-Slot: `todo_index_drift=0`, `active_docs_stale=23 -> 0 im selben Lauf`, `placeholder_conflicts=0`, `logs_policy_violations=0`. Die Modul-Boards bleiben unveraendert bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`.
- Mit [novapolis-dev/docs/process/wochenbericht-2026-05-18.md](process/wochenbericht-2026-05-18.md) liegt der konsolidierte Wochenbericht fuer den Zeitraum 2026-05-12 bis 2026-05-18 jetzt im Dev-Modul vor.

Dev/Governance: Wochenabschluss 2026-05-11 auf Gruenstand gehalten (2026-05-11 12:59)
-----------------------------------------------------------------------------------------

- Seit dem letzten Wochenabschluss kam kein neuer Repo-Commit hinzu; `git log --since="2026-05-04 09:36"` zeigt weiter nur `02f2d9d`. Der Arbeitsstand blieb damit fachlich stabil; der Wochenabschluss war ein reiner Governance- und Hygiene-Lauf.
- Der initiale Vollcheck [.tmp/results/reports/checks_report_20260511_125233.md](../../.tmp/results/reports/checks_report_20260511_125233.md) fiel nur am stale Agent-Board [novapolis-dev/docs/todo.agent-board.md](todo.agent-board.md). Nach diesem Freshness-Fix kippte der Zwischenlauf [.tmp/results/reports/checks_report_20260511_125608.md](../../.tmp/results/reports/checks_report_20260511_125608.md) nur noch an der pflichtigen Index-Synchronisierung; [novapolis-dev/docs/todo.index.md](todo.index.md) wurde im selben Lauf nachgezogen.
- Der finale Recheck [.tmp/results/reports/checks_report_20260511_125821.md](../../.tmp/results/reports/checks_report_20260511_125821.md) ist vollstaendig PASS. `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty` bleibt bei `summary=fail:0,warn:0`; der Coverage-Gate-Lauf bleibt mit `709 passed` und `92.19%` klar ueber Hard Gate und Qualitaetsziel.
- KPI-Hygiene-Slot: `todo_index_drift=0`, `active_docs_stale=1 -> 0 im selben Lauf`, `placeholder_conflicts=0`, `logs_policy_violations=0`. Die Modul-Boards bleiben unveraendert bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`.
- Mit [novapolis-dev/docs/process/wochenbericht-2026-05-11.md](process/wochenbericht-2026-05-11.md) liegt der konsolidierte Wochenbericht fuer den Zeitraum 2026-05-05 bis 2026-05-11 jetzt im Dev-Modul vor.

Dev/Governance: Wochenbericht angelegt und belegte Drift aus dem Abschlusslauf nachgezogen (2026-05-04 08:34)
--------------------------------------------------------------------------------------------------------

- Der initiale Vollcheck [.tmp/results/reports/checks_report_20260504_083019.md](../../.tmp/results/reports/checks_report_20260504_083019.md) war eng rot und belegte nur zwei technische Reste: stale Tree-Artefakte (`workspace_tree.txt`, `workspace_tree_full.txt`) sowie drei ueberfaellige Referenzdokus ([novapolis-dev/docs/copilot-vscode-usage.md](copilot-vscode-usage.md), [novapolis-dev/docs/index.md](index.md), [novapolis-dev/docs/naming-policy.md](naming-policy.md)).
- `workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt` und `workspace_tree_local.txt` sind im selben Lauf ueber [scripts/update_workspace_tree_dirs.py](../../scripts/update_workspace_tree_dirs.py) neu erzeugt; der fokussierte Test `novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py` ist danach wieder grün.
- Mit [novapolis-dev/docs/process/wochenbericht-2026-05-04.md](process/wochenbericht-2026-05-04.md) liegt jetzt ein eigener Wochenbericht im Dev-Modul vor. Er buendelt die belastbaren Fortschritte der Woche ueber Dev-/Governance-, RP- und Runtime-Arbeit sowie den offenen fachlichen Naechstanker fuer den Nordlinie-Strang.
- Der anschliessende Recheck [.tmp/results/reports/checks_report_20260504_083908.md](../../.tmp/results/reports/checks_report_20260504_083908.md) ist wieder vollstaendig PASS; `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty` endet mit `summary=fail:0,warn:0`, und der separate Coverage-Lauf bleibt mit `709 passed` sowie `92.19%` klar ueber Gate und Qualitaetsziel.

RP-Runtime: RP-Stand erfasst und naechsten Antwortzug vorbereitet (2026-04-29 10:51)
------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](../../novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt jetzt einen eigenen Vorbereitungsanker fuer den naechsten Zug: Erst die C6-Antwort zur Schuttbruch-Eignung, danach die Jonas-/Pahl-Antwort zu Draisine-Antrieb, Brems-/Stopplogik und Lastgrenze.
- [novapolis-rp/database-curated/staging/rp-runtime/entities/projects/nordlinie-01/state.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/projects/nordlinie-01/state.md) zieht denselben Schnitt in den Projekt-State: T12 bleibt der aktuelle belegte Arbeitsstand, der naechste Zug ist als Antwortpfad vorbereitet und fuehrt noch keine neue Materialbuchung, keine neue Freigabe und keinen Draisine-Testlauf.
- Der Lauf bleibt absichtlich minimal: keine neue Szene, keine neue Kanonbehauptung und keine still aus T12 abgeleitete D5-/C6-Erfolgsmeldung. Ziel ist ein sauberer Startanker fuer den naechsten einzelnen Zug.

RP-Runtime: Turn 12 mit C6-Schuttbruch-Pruefung und Draisine-Antriebsfrage nachgezogen (2026-04-29 06:39)
----------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](../../novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt den korrigierten Runtime-Arbeitsstand: 2026-06-13 09:19
- [novapolis-rp/database-curated/staging/rp-runtime/entities/projects/nordlinie-01/state.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/projects/nordlinie-01/state.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/projects/nordlinie-01/inventory.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/projects/nordlinie-01/inventory.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/locations/c6/state.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/locations/c6/state.md) und [novapolis-rp/database-curated/staging/rp-runtime/entities/locations/d5/state.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/locations/d5/state.md) halten denselben Schnitt: Schuttbruch aus dem C6-Schuttkeil ist nur eine Pruefoption, keine gebuchte Materialbewegung.
- [novapolis-rp/database-curated/staging/rp-runtime/entities/assets/draisine-transportmodul/state.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/assets/draisine-transportmodul/state.md) wurde als fehlender Asset-State angelegt, weil der konkrete Antrieb, Brems-/Stopplogik, Lastgrenze und Testlauf noch offen sind. [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/entity.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/entity.md) und [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/mind.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/mind.md) fuehren T12 als technische Prueffrage ohne neue Mind- oder Relationship-Delta.

RP-Governance: ERP/RP-Ausspielungsregel fuer Praesens, Klartext und Lore-Fit verankert (2026-04-29 05:41)
------------------------------------------------------------------------------------------------------------------

- [.github/instructions/rp-docs.instructions.md](../../.github/instructions/rp-docs.instructions.md) fuehrt jetzt eine harte `R-RP-SCENE-FIT`-Regel fuer ERP/RP-Ausspielung: Gegenwartsform, klare normalverstaendliche In-World-Sprache, getrennte Admin-/OOC-Begriffe, SSOT-treue Ortsbeschreibungen sowie Rollen- und Mechanik-Fit fuer Figuren und Instanzen.
- Der Nachzug ist aus dem Admin-Befund zu Turn 12 abgeleitet: D5 ist laut [D5](../../novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md) ein geordneter, restaurierter Betriebskern mit engem Funk-/Signalplatz am Kontroll-/Terminalkern; Ronja ist laut [Ronja Kerschner](../../novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md) Leitungs-, Diplomatie-/Freigabe- und Technikrolle mit starkem Ordnungs- und Planungsprofil.
- Die Regel verhindert kuenftig, dass ausgespielter RP-Text unklare Technikmetaphern, OOC-Vokabular im Figurendialog, faktisch falsche Raumstimmung oder herabgestufte Rollenhaltung als Atmosphaere ausgibt. Turn 12 bleibt bis zur User-Freigabe pausiert und wird nicht weiter fortgeschrieben.

RP-Runtime: Alter characters-Typordner archiviert (2026-04-29 02:29)
-------------------------------------------------------------------

- Der alte Typordner `novapolis-rp/database-curated/staging/rp-runtime/characters/` ist nach WhatIf-Pruefung archiviert. Alle 14 alten Markdown-Dateien waren `state: migriert` und verwiesen auf existierende aktive Dossierziele.
- Die Archivkopie liegt unter `novapolis-dev/archive/quarantine/rp-runtime-characters-legacy-20260429-0229/characters/`; im aktiven Runtime-Baum bleibt fuer Figuren nur [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/characters/README.md) relevant.
- [novapolis-rp/database-curated/staging/rp-runtime/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/README.md) und [novapolis-rp/database-curated/staging/rp-runtime/entities/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/README.md) benennen den Archivschnitt; die Modul-Boards bleiben bei `RP=0`.

RP-Runtime: Option-1-Migration auf entity-centric Dossiers abgeschlossen (2026-04-29 02:02)
------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/entities/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/README.md) ist jetzt die aktive Runtime-Oberflaeche fuer entitaetsbezogene Arbeitsdaten. `sessions/` bleibt top-level; Figuren, Orte, Projekte, Assets und Fraktionen liegen unter `entities/<type>/<slug>/`.
- 33 aktive Runtime-Artefakte aus `characters/`, `mind/`, `inventories/`, `state/` und `relationships/` wurden in passende Dossiers ueberfuehrt. Die alten Typordner bleiben mit Redirect-Dateien bestehen, enthalten aber keine aktiven Runtime-Traeger mehr.
- [.github/instructions/rp-docs.instructions.md](../../.github/instructions/rp-docs.instructions.md) und [.github/instructions/mind-cluster.instructions.md](../../.github/instructions/mind-cluster.instructions.md) nutzen jetzt Dossierpflicht und gerichtete `relationships.md`-Eintraege pro Observer statt Relationship-Einzelkanten als Standardmodell. [novapolis-dev/docs/todo.rp.md](todo.rp.md) und [novapolis-dev/docs/todo.index.md](todo.index.md) stehen danach wieder bei `RP=0`.

RP-Runtime: Option-1-Migration auf entity-centric Dossiers geplant (2026-04-29 01:55)
--------------------------------------------------------------------------------------

- [novapolis-dev/docs/todo.rp.md](todo.rp.md) fuehrt den offenen RP-Punkt jetzt als geplante Migration von der flachen Runtime-Typordnerstruktur auf `entities/<type>/<slug>/`-Dossiers. `sessions/` bleibt top-level; entitaetsbezogene Arbeitsdaten sollen kuenftig je Entitaet zusammenliegen.
- Der Plan ersetzt den zuvor begonnenen Relationship-Einzelkantenansatz: Beziehungen werden als gerichtete `observer_id -> target_id`-Eintraege in `relationships.md` pro Entitaetsdossier gefuehrt, nicht als Standard mit einer Datei pro Kante.
- [novapolis-dev/docs/todo.index.md](todo.index.md) bleibt bei `RP=1`, benennt den offenen Punkt aber jetzt als entity-centric Runtime-Migration nach Option 1; die eigentliche Strukturmutation folgt im naechsten freigegebenen Umsetzungslauf.

RP-Runtime/Governance: Entitaets-/Mind-Paarlauf verankert und C6-Runtime komplettiert (2026-04-29 01:30)
----------------------------------------------------------------------------------------------------------------

- [.github/instructions/rp-docs.instructions.md](../../.github/instructions/rp-docs.instructions.md), [.github/instructions/mind-cluster.instructions.md](../../.github/instructions/mind-cluster.instructions.md) und [novapolis-rp/database-curated/staging/rp-runtime/README.md](../../novapolis-rp/database-curated/staging/rp-runtime/README.md) fuehren jetzt explizit, dass individuelle Entitaetsaktionen Entitaets- und Mind-/Sphaerenstand vor dem Zug gemeinsam laden und nach dem Zug gemeinsam aktualisieren oder bewusst als `keine neue Mind-Delta` beziehungsweise `carry_forward_confirmed` stabilisieren.
- [novapolis-rp/database-curated/staging/rp-runtime/inventories/c6.md](../../novapolis-rp/database-curated/staging/rp-runtime/inventories/c6.md) ist vom verworfenen H-47-Probeanker zum aktuellen C6-Hauptpfad-Inventartraeger umgestellt; [novapolis-rp/database-curated/staging/rp-runtime/entities/locations/c6/roster.md](../../novapolis-rp/database-curated/staging/rp-runtime/entities/locations/c6/roster.md) fuehrt die 27 humanoiden Personen und Vor-Ort-Entitaeten als Roster-/Schichtoberflaeche.
- Marei Falk, Marven Kael und Arlen Dross liegen jetzt jeweils mit Character- und Mind-Runtime vor; [novapolis-rp/database-curated/staging/rp-runtime/mind/kora-malenkov.md](../../novapolis-rp/database-curated/staging/rp-runtime/mind/kora-malenkov.md), [novapolis-rp/database-curated/staging/rp-runtime/mind/echo.md](../../novapolis-rp/database-curated/staging/rp-runtime/mind/echo.md) und [novapolis-rp/database-curated/staging/rp-runtime/state/c6.md](../../novapolis-rp/database-curated/staging/rp-runtime/state/c6.md) sind auf den Turn-11-C6-Nachzug konsolidiert. [novapolis-dev/docs/todo.rp.md](todo.rp.md) und [novapolis-dev/docs/todo.index.md](todo.index.md) stehen danach wieder bei `RP=0`.

RP-SSOT: Fluesterkollektiv-Handelslog auf Sammelklassen-Kanon nachgezogen (2026-04-29 00:55)
----------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/06-handel-diplomatie/Handelslog-Fluesterkollektiv.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/06-handel-diplomatie/Handelslog-Fluesterkollektiv.md) fuehrt jetzt die bereits inventarseitig belegten Klassen `Informationsgueter`, `Tarn-/Signaltechnik` und `Batterien` explizit auch auf der externen Handelsoberflaeche mit.
- Der Nachzug bleibt bewusst eng: keine neue Gegenpartei, kein neues Lieferfenster und keine Mengenretcon; die Handelsflaeche bleibt weiter ein konservativer Kanalrahmen fuer indirekte Uebergaben.
- [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren den Nachzug im selben Lauf wieder auf `RP=0`.

RP-SSOT: Neue Sammelklassen in Warenueberblick T0 und Novapolis-Handelsdokus nachgezogen (2026-04-29 00:50)
------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) fuehrt jetzt `Rohmaterialien`, `Medizinische Gueter` und `Informationsgueter` explizit als breite, aber belegte Handels- und Bedarfsklassen fuer die aktive Novapolis-/C6-Oberflaeche mit.
- [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md), [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-markets.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-markets.md) und [novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-pricebands.md](novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/novapolis-pricebands.md) fuehren denselben Kanon jetzt ebenfalls, indem `Nahrungsmittel (Grundbedarf)`, `Grundbedarfsgueter`, `Rohmaterialien`, `Medizinische Gueter` und `Informationsgueter` die bisherigen unschaerferen Oberbegriffe ersetzen oder ergaenzen.
- [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren den Nachzug im selben Lauf wieder auf `RP=0`.

RP-SSOT: Waren-Index um belegte Sammelklassen fuer erwartbare Gueterkorridore erweitert (2026-04-29 00:35)
---------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) fuehrt jetzt zusaetzlich die Sammelklassen `Rohmaterialien`, `medizinische Gueter`, `Informationsgueter`, `Tarn-/Signaltechnik` und `Batterien`, weil diese Klassen bereits in aktiven Relations-, Markt- oder Inventar-SSOTs als eigene Gueterkorridore lesbar sind.
- Die Hinweislogik im selben Index ist jetzt enger formuliert: breite Sammelklassen sind erlaubt, wenn aktive Handels-, Markt- oder Fraktionsinventar-SSOTs sie schon explizit fuehren; freie Detailwaren ohne Missions-/Scene- oder SSOT-Anker bleiben weiter ausgeschlossen.
- [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren den Nachzug im selben Lauf wieder auf `RP=0`.

RP-SSOT: Neue Warenklassen in betroffene Inventare und Runtime-Traeger nachgezogen (2026-04-29 00:27)
-----------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md), [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) und [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md) fuehren `Kabelanschnitt`, `Schienenprofil`, `Betonplatte` sowie die Importklassen `Nahrungsmittel (Grundbedarf)` und `Grundbedarfsgueter` jetzt deckungsgleich dort, wo diese Klassen bereits als Verbrauchs-, Bewegungs- oder Handelsanker belegt waren.
- [novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md](novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md) fuehrt denselben Handelswortschatz jetzt ebenfalls kanonisch mit `Nahrungsmittel (Grundbedarf)` statt nur der kuerzeren Sammelbezeichnung.
- [novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md) und [novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md) fuehren denselben Kanon-Wortschatz jetzt auch im Runtime-Slice, ohne `Anschlusssicherung` oder `Verbindungsmaterial` vorschnell als neue SSOT-Warenklasse hochzuziehen; [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) stehen danach wieder bei `RP=0`.

RP-SSOT: Waren-Index und Warenueberblick T0 um aktive RP-Warenklassen erweitert (2026-04-29 00:20)
---------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) fuehrt jetzt die zusaetzlichen RP-passenden Klassen `Kabelanschnitt`, `Schienenprofil`, `Betonplatte`, `Nahrungsmittel (Grundbedarf)` und `Grundbedarfsgueter` samt Kurzübersicht und SSOT-Ankern aus aktiven Inventar-, Projekt- und Handelsdokus.
- [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) spiegelt denselben Nachzug auf T0-Arbeitslageebene: `Schienenprofil` und `Betonplatte` laufen jetzt sichtbar als Nordlinie-Verbrauchsklassen, `Kabelanschnitt` als kleine Werkstatt-/Baustellenklasse und der H-47-/C6-Pfad explizit mit `Nahrungsmittel` und `Grundbedarfsgueter`.
- Bewusst nicht kanonisiert wurden bloße Runtime-Arbeitsworte ohne harten SSOT-/Log-Anker als Warenklasse, insbesondere `Anschlusssicherung` und `Verbindungsmaterial`; [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren den Nachzug im selben Lauf wieder auf `RP=0`.

Governance: Navigator-/Logging-Waechter-Modus darf aktive SSOTs im Laborbetrieb direkt schaerfen (2026-04-29 00:13)
-----------------------------------------------------------------------------------------------------------------

- [.github/copilot-instructions.md](.github/copilot-instructions.md) fuehrt jetzt explizit, dass aktive SSOT-Dateien in der Laborumgebung bearbeitbare Arbeitsflaechen sind, wenn der aktuelle Auftrag gerade das Testen, Schaerfen, Erweitern oder Ergaenzen dieser SSOTs verlangt.
- [.github/agents/novapolis-workspace-navigator.agent.md](.github/agents/novapolis-workspace-navigator.agent.md) fuehrt dieselbe Freigabe jetzt direkt im Navigator-/Logging-Waechter-Modus: aktive SSOTs duerfen im Laborbetrieb evidenzbasiert, minimal und mit vollem Logging-/Checkpfad direkt mutiert werden.
- Die bestehende Schutzlogik bleibt dabei unveraendert eng: keine freie Kanonvermutung, keine Scope-Ausweitung und keine stillen Mutationen ohne Evidenz, Snapshot-Stand und DONELOG-Nachzug.

RP-Runtime: Novapolis und Haendlerbund jetzt mit Fraktionsruntime; Nordlinie fuehrt erste feste Komponentenlisten (2026-04-28 22:52)
---------------------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/state/novapolis.md](novapolis-rp/database-curated/staging/rp-runtime/state/novapolis.md) fuehrt jetzt den aktiven Novapolis-Hauptpfad auf Fraktionsebene mit `D5`, `C6`, `Nordlinie 01` und `Draisine-Transportmodul` als gebuendelten Runtime-Achsen.
- [novapolis-rp/database-curated/staging/rp-runtime/state/haendlerbund.md](novapolis-rp/database-curated/staging/rp-runtime/state/haendlerbund.md) fuehrt jetzt den aktiven Haendlerbund-Slice als geteilten Stand zwischen `G7` als Eigenkern und `H-47/C6` als eingebetteter Niederlassung, ohne freie neue G7-Reaktion zu behaupten.
- [novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md) fuehrt fuer die benannten Reparaturcluster jetzt nicht mehr nur Satzlogik, sondern erste feste Komponentenlisten; [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren den Nachzug im selben Lauf wieder auf `RP=0`.

RP-Runtime: Draisine-Warenscope erweitert und Nordlinie-Reparaturbedarf als eigener Runtime-Traeger nachgezogen (2026-04-28 22:46)
--------------------------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md) fuehrt jetzt neben dem gebundenen Prototypbestand auch die naechsten SSOT-gebundenen Projektklassen `Kabelanschnitt`, `Werkzeugkit`, `Werkzeugsatz (Mechanik)`, `Wartungsschluessel` und `Druckmesser` als noch ungebundene Projektumgebung statt als freie Spaetvermutung.
- [novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/nordlinie-01.md) fuehrt den belegten Reparaturbedarf von Nordlinie 01 jetzt eigenstaendig: harte Blocker `Schweißgeraet` und `Adapter / Fitting (DN60)`, dazu `Anschlusssicherung`, `Verbindungsmaterial`, Nachsicherung, Unterfuetterung, Raeumkapazitaet und Freiraeumung mit Zuordnung auf die benannten Reparaturflaechen.
- [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) und [novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md) fuehren denselben Trennschnitt jetzt deckungsgleich mit; [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren den Lauf erst offen und danach wieder geschlossen auf `RP=0`.

RP-Runtime: Draisine-Transportmodul jetzt mit eigenem Runtime-Traeger und getrenntem Bedarfsschnitt (2026-04-28 22:39)
-----------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/draisine-transportmodul.md) fuehrt jetzt den belegten Prototypbestand der Draisine eigenstaendig nach bestehendem `inventories/`-Muster: `Schmieroel`, `Lagerfett (Technik)`, `Sicherungssatz` und `Dichtungsmanschette` sind mit gebundenem Satz plus D5-Rest getrennt gefuehrt.
- [novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md), [novapolis-rp/database-curated/staging/rp-runtime/state/d5.md](novapolis-rp/database-curated/staging/rp-runtime/state/d5.md) und [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) fuehren denselben Trennschnitt jetzt deckungsgleich: gebundener Draisine-Bestand laeuft separat, waehrend `Schweißgeraet` und `Adapter / Fitting (DN60)` weiter als Nordlinie-/Tunnelblocker und nicht als Draisine-Eigenverbrauch gelesen werden.
- [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren den Nachzug im selben Lauf erst offen und danach wieder geschlossen; das RP-Board steht damit erneut bei `offen: 0`.

RP-Runtime: Turn 11 fuehrt D5-Bahnsteiggleise, Draisine-Status und getrennte C6-Stationsverarbeitung nach (2026-04-28 22:24)
------------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt jetzt Turn 11: Ronja kehrt mit Reflex nach `D5` zurueck, trifft Jonas und Pahl an der Draisine auf den Bahnsteiggleisen, klaert erst Baufortschritt und gebundenes Material und erst danach den Tunnelbedarf.
- [novapolis-rp/database-curated/staging/rp-runtime/state/d5.md](novapolis-rp/database-curated/staging/rp-runtime/state/d5.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/jonas-merek/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/jonas-merek/entity.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/pahl-brenner/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/pahl-brenner/entity.md) und [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/lumen/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/lumen/entity.md) fuehren denselben D5-Schnitt jetzt sichtbar am Bahnsteig-/Gleis-Arbeitsort statt als stillen Werkstattinnenraum.
- [novapolis-rp/database-curated/staging/rp-runtime/state/c6.md](novapolis-rp/database-curated/staging/rp-runtime/state/c6.md), [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) und [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/kora-malenkov/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/kora-malenkov/entity.md) fuehren zugleich die getrennte C6-Ebene weiter: `Kora` verarbeitet den Bericht des `C6-Tunneltrupps` als Stationsaufgabe, ohne Ronjas D5-Perspektive mitzufuehren.

RP-Runtime: Turn 10 per Admin-Nachzug auf getrennte C6-Tunnel- und Stationslesart korrigiert (2026-04-28 22:13)
------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt Turn 10 jetzt nicht mehr so, als brächte nur Ronjas Seite melderelevante Befunde an den Kontaktpunkt. Der `C6-Tunneltrupp` fuehrt jetzt mit `Schuttkeil Kontaktseite`, `Randauflage Suedlauf` und `Leitungsaufnahme C6-Vorlauf` einen eigenen Reparaturbefund seiner Haelfte.
- [novapolis-rp/database-curated/staging/rp-runtime/state/c6.md](novapolis-rp/database-curated/staging/rp-runtime/state/c6.md) trennt jetzt `C6-Tunneltrupp` und `C6-Station` sichtbar: Der Tunneltrupp fuehrt den direkten Arbeitskontakt und die eigene Schadlage, waehrend `Kora` den getrennten Ruecklauf und Innenbetrieb der Station haelt.
- [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) fuehrt den Folgeanker damit nicht mehr als implizit einseitige D5-Befundlage, sondern als gekoppelte D5-/C6-Reparaturflaeche mit beidseitiger Bedarfskalkulation.

RP-Runtime: KB der aktiven Entitaeten auf Turn-9/10-Stand gezogen und Folgezug mit direktem C6-Kontakt fortgesetzt (2026-04-28 21:47)
----------------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/entity.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/entity.md), [novapolis-rp/database-curated/staging/rp-runtime/mind/ronja-kerschner.md](novapolis-rp/database-curated/staging/rp-runtime/mind/ronja-kerschner.md) und [novapolis-rp/database-curated/staging/rp-runtime/mind/reflex.md](novapolis-rp/database-curated/staging/rp-runtime/mind/reflex.md) fuehren die zuvor noch auf Turn 8 stehende D5-Protagonistenkante jetzt sauber bis zum aktuellen Kontaktstand mit `C6`.
- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt jetzt Turn 10: Ronja dokumentiert den Restabschnitt, erreicht den C6-Tunneltrupp an einem schmalen Kontaktpunkt und zieht mit ihm eine gemeinsame Befundliste plus Bedarfskalkulation statt eines freien Durchbruchs.
- [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) und [novapolis-rp/database-curated/staging/rp-runtime/state/c6.md](novapolis-rp/database-curated/staging/rp-runtime/state/c6.md) fuehren denselben neuen Arbeitsstand jetzt projekt- und ortsscharf: beidseitig bestaetigte Problemherde, gemeinsamer Mindestbedarf `Schweißgeraet` plus `DN60`, aber weiterhin kein freier Material- oder Personaldurchgang.

RP-Runtime: Turn 9 per Admin-Auswertung auf den festgeschriebenen Arbeitsstand korrigiert (2026-04-28 21:36)
-----------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt Turn 9 jetzt nicht mehr als freien G7-Weltzug, sondern als Admin-Nachzug mit bilateraler Tunnelarbeit, vorsichtiger gegenseitiger Wahrnehmung der beiden Trupps und weiter offenem technischen Blocker.
- [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) und [novapolis-rp/database-curated/staging/rp-runtime/state/c6.md](novapolis-rp/database-curated/staging/rp-runtime/state/c6.md) fuehren denselben Stand jetzt projekt- und ortsscharf: `Kora` bleibt in der Stationsverwaltung, und die nicht im Tunnel eingesetzten Gefluechteten tragen Wasser-, Lager-, Hygiene-, Kuechen-, Wache- und Entlastungsarbeit des laufenden C6-Innenbetriebs.
- [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/mara-quell/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/mara-quell/entity.md) fuehrt Mara Quell jetzt wieder als Vor-Ort-Akteurin in `C6` beim Aufbau des H-47-Aussenpostens statt als aktive Fernreaktion aus `G7`.
- [novapolis-rp/database-curated/staging/rp-runtime/state/g7.md](novapolis-rp/database-curated/staging/rp-runtime/state/g7.md) fuehrt im selben Lauf ausdruecklich keinen neuen Novapolis-Wissensstand; ohne Meldung aus `C6` bleibt `G7` beim vorherigen Kenntnisstand.

RP-Runtime: Turn 9 als offener Weltzug ueber die direkt belegten Anschlussachsen gezogen (2026-04-28 21:17)
---------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt Turn 9 jetzt als offenen Weltzug ueber `Tunnel`, `D5`, `C6` und `G7/H-47`, ohne neue Lieferungen oder freien Vollerfolg zu behaupten.
- [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md), [novapolis-rp/database-curated/staging/rp-runtime/state/d5.md](novapolis-rp/database-curated/staging/rp-runtime/state/d5.md), [novapolis-rp/database-curated/staging/rp-runtime/state/c6.md](novapolis-rp/database-curated/staging/rp-runtime/state/c6.md) und [novapolis-rp/database-curated/staging/rp-runtime/state/g7.md](novapolis-rp/database-curated/staging/rp-runtime/state/g7.md) fuehren denselben Weltzug jetzt als Projekt-, Werkstatt-, Vorposten- und externe Freigabekante.
- Neu angelegte Runtime-Traeger fuer [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/kora-malenkov/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/kora-malenkov/entity.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/echo/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/echo/entity.md), [novapolis-rp/database-curated/staging/rp-runtime/mind/kora-malenkov.md](novapolis-rp/database-curated/staging/rp-runtime/mind/kora-malenkov.md) und [novapolis-rp/database-curated/staging/rp-runtime/mind/echo.md](novapolis-rp/database-curated/staging/rp-runtime/mind/echo.md) halten die jetzt aktiv mitgezogene C6-Achse sauber im Runtime-Baum.
- [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/mara-quell/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/mara-quell/entity.md) fuehrt Mara Quell jetzt nicht mehr nur als alten C6-H47-Probeanker, sondern auch als aktive G7-/H-47-Reaktionskante des aktuellen Hauptpfads.

RP-Runtime: Turn 8 mit erweitertem Runtime-Slice erneut simuliert (2026-04-28 20:01)
-----------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt Turn 8 jetzt noch einmal auf Basis des inzwischen volleren Runtime-Slices fuer D5, Figuren und Mind-Traeger.
- Der belegte Ausgang bleibt bewusst unveraendert: keine neue D5-Freigabe, kein neues Material, nur der reale Tunnelrest aus `metallprofil-kurz`, `ausgleichsplatte` und `schraubensatz-mittel` an der `Schottertasche Nordkante`.
- Neu enger ausgespielt ist vor allem die Hintergrundkante: Die bekannte D5-Werkstattlage bleibt auch in Turn 8 belastbar knapp, statt still als moeglicher Nachschub mitzuschwingen.

Governance: Kanonischen Vollcheck nach lokalem Tree-Slice-Stilfix wieder komplett gruen gezogen (2026-04-28 17:28)
---------------------------------------------------------------------------------------------------

- [scripts/update_workspace_tree_dirs.py](scripts/update_workspace_tree_dirs.py) enthaelt nach dem letzten Vollcheck nur noch den von Black erwarteten Zeilenumbruch in `_git_visible_paths()`; dadurch schliesst derselbe Tree-Skriptpfad jetzt wieder ohne Formatrest.

Post-Check: Frontmatter Auto-Sync & Stil-Fixes (2026-06-13 09:17)
----------------------------------------------------------------

- Aktion: Automatischer Frontmatter-`stand`/`checks`-Nachzug fuer aktive Dokus (API/README/Workspace-Index/TODO-Boards + aktive RP-Referenzen) zur Behebung von `doc-freshness`-Findings; zusatzlich automatisierte Ruff/Black-Fixes fuer Code-Stil.
- Betroffene Dateien: 76 Markdown-Dateien (Frontmatter aktualisiert), plus formatierte Python-Dateien unter `novapolis_agent/` und `scripts/` (Ruff/Black-Anpassungen).
- Prüfungen: Vorheriger Wrapper-Run identifizierte `doc-freshness` und Style-Reste; nach Auto-Sync und Stil-Fixes wurde `doc-freshness` deutlich reduziert (83 -> 11 Findings); `ruff`/`black` wurden lokal repariert; `mypy` now PASS; `pytest` weiterhin FAIL in Full-Run (Details: .tmp/results/reports/checks_report_20260613_091615.md).
- Receipt: snapshot-lock refreshed before mutation; post-change full wrapper run produced `.tmp/results/reports/checks_report_20260613_091615.md` (overall=FAIL) with remaining gates to address (path-portability, residual doc-freshness, pytest failures).

- [novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py](novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py) endet wieder mit abschliessender Newline, womit der letzte Ruff-Hinweis im zugehoerigen Testpfad ebenfalls wegfaellt.
- Der kanonische Repo-Lauf ueber `scripts/run_checks_and_report.py` ist danach wieder vollstaendig gruen; der aktuelle Report liegt unter [.tmp/results/reports/checks_report_20260428_172700.md](.tmp/results/reports/checks_report_20260428_172700.md), und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehrt den PASS-Stand im selben Lauf nach.

Governance: Expliziten lokalen Workspace-Baum neben den drei überwachten Trees eingeführt (2026-04-28 13:15)
--------------------------------------------------------------------------------------------------------

- [scripts/update_workspace_tree_dirs.py](scripts/update_workspace_tree_dirs.py) erzeugt jetzt zusätzlich [workspace_tree_local.txt](workspace_tree_local.txt) über den neuen Modus `local-full`; der neue Baum bildet den echten lokalen On-Disk-Zustand ab, während [workspace_tree.txt](workspace_tree.txt), [workspace_tree_dirs.txt](workspace_tree_dirs.txt) und [workspace_tree_full.txt](workspace_tree_full.txt) die überwachten kanonischen Trees bleiben.
- [novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py](novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py) prüft jetzt explizit, dass `workspace_tree_local.txt` bewusst nicht Teil von `snapshot_outputs()` und damit nicht Teil des Default-Freshness-Gates ist; zugleich bleibt der vollständige Tree-Testpfad grün.
- [.vscode/tasks.json](.vscode/tasks.json), [README.md](README.md) und [WORKSPACE_INDEX.md](WORKSPACE_INDEX.md) führen denselben Vierer-Split jetzt repo-lesbar; der neue Task `Workspace tree: local` erzeugt den lokalen Maschinenbaum gezielt neben den bestehenden Tree-Tasks.
- Alle vier Tree-Artefakte sind im selben Lauf neu erzeugt; [novapolis-dev/docs/todo.dev.md](novapolis-dev/docs/todo.dev.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) führen den Abschluss im selben Lauf nach.

Governance: Vollbaum wieder im Default-Freshness-Gate, aber ohne Ignore-Drift (2026-04-28 12:53)
----------------------------------------------------------------------------------------------

- [scripts/update_workspace_tree_dirs.py](scripts/update_workspace_tree_dirs.py) rendert [workspace_tree_full.txt](workspace_tree_full.txt) jetzt deterministisch aus repo-sichtbaren Pfaden via `git ls-files --cached --others --exclude-standard`, statt den kompletten lokalen Maschinenbaum direkt zu serialisieren.
- Damit bleibt der Vollbaum wieder im Default-Freshness-Gate von `stale_snapshot_paths()`, ohne an ignore-basierten Laufartefakten wie `.snapshot.now`, `.venv`, `.tmp` oder `coverage.xml` zu kippen.
- [novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py](novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py) deckt jetzt sowohl die Rueckkehr von [workspace_tree_full.txt](workspace_tree_full.txt) in den Default-Gate als auch das Ausfiltern derselben Ignore-Volatilitaet explizit ab.
- [workspace_tree_full.txt](workspace_tree_full.txt) ist mit dem neuen Renderer neu erzeugt; [novapolis-dev/docs/todo.dev.md](novapolis-dev/docs/todo.dev.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren den Abschluss im selben Lauf nach.

Governance: Aktive Root-Trees jetzt tracked-only statt Reader-Surface-Sonderfilter (2026-04-28 12:53)
------------------------------------------------------------------------------------------------

- [scripts/update_workspace_tree_dirs.py](scripts/update_workspace_tree_dirs.py) fuehrt in aktiven Trees keine zusaetzlichen Reader-Surface-Sonderausschluesse fuer getrackte Repo-Pfade mehr; ausgeschlossen bleiben nur noch Ignore-basierte Maschinenartefakte sowie lokale Repo-Metadatenpfade wie `.git` und `.tox`.
- [novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py](novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py) prueft jetzt explizit, dass getrackte Repo-Pfade aus [novapolis-dev/archive](novapolis-dev/archive), [novapolis-rp/database-raw](novapolis-rp/database-raw) und [novapolis-rp/database-curated](novapolis-rp/database-curated) in der aktiven Tree- und Directory-Sicht wieder sichtbar sind, waehrend Ignore-Faelle wie `coverage.xml` weiterhin ausgeschlossen bleiben.
- [workspace_tree.txt](workspace_tree.txt) und [workspace_tree_dirs.txt](workspace_tree_dirs.txt) sind mit derselben vereinfachten Policy neu erzeugt und zeigen damit wieder den vollstaendigen getrackten Repo-Inhalt der aktiven Surface.
- [novapolis-dev/docs/todo.dev.md](novapolis-dev/docs/todo.dev.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) fuehren denselben Abschluss im selben Lauf nach; das Dev-Board steht wieder bei `offen: 0`.

Governance: Tree-Skip-Policy jetzt explizit gegen gitignore gespiegelt (2026-04-28 12:18)
-------------------------------------------------------------------------------------

- [scripts/update_workspace_tree_dirs.py](scripts/update_workspace_tree_dirs.py) trennt die aktive Filterlogik jetzt explizit in `ACTIVE_GITIGNORE_SKIP_*` fuer ignorierte Maschinenartefakte und `ACTIVE_READER_SURFACE_ONLY_*` fuer staerkere Reader-Surface-Ausnahmen.
- Der Nachzug schliesst die belegte Drift, dass ignorierte Artefakte wie `novapolis_agent/coverage.xml` wieder in [workspace_tree.txt](workspace_tree.txt) auftauchten, obwohl Root- und Modul-`.gitignore` sie aus dem Arbeitsstand ausschliessen.
- [novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py](novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py) prueft jetzt Freshness, gitignore-gespiegelte Skip-Klassen, die Trennung der Reader-Surface-Extras und den konkreten Coverage-Driftfall.
- [workspace_tree.txt](workspace_tree.txt) und [workspace_tree_dirs.txt](workspace_tree_dirs.txt) sind mit derselben Policy neu erzeugt; [novapolis-dev/docs/todo.dev.md](novapolis-dev/docs/todo.dev.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) ziehen den Abschluss im selben Lauf nach.

Governance: Root-Trees erneuert und per pytest gegen Drift abgesichert (2026-04-28 11:50)
-----------------------------------------------------------------------------------

- [scripts/update_workspace_tree_dirs.py](scripts/update_workspace_tree_dirs.py) bietet jetzt testbare Render-Helfer plus `stale_snapshot_paths()`, sodass Tree-Drift direkt gegen frisch generierten Output nachweisbar ist.
- [novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py](novapolis_agent/tests/scripts/test_update_workspace_tree_dirs.py) fuehrt genau diesen Freshness-Check als pytest-Slice; vor dem Refresh fiel er fuer alle drei Tree-Artefakte rot, nach dem echten Refresh ist er gruen.
- [workspace_tree.txt](workspace_tree.txt), [workspace_tree_dirs.txt](workspace_tree_dirs.txt) und [workspace_tree_full.txt](workspace_tree_full.txt) sind im selben Lauf neu erzeugt und spiegeln wieder den aktuellen Workspace-Stand.
- [novapolis-dev/docs/todo.dev.md](novapolis-dev/docs/todo.dev.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) ziehen denselben Abschluss nach; das Dev-Board steht wieder bei `offen: 0`.

Governance: README-Minifix fuer Workspace-Index und Decision-Liste abgeschlossen (2026-04-28 08:26)
---------------------------------------------------------------------------------------------------

- [WORKSPACE_INDEX.md](WORKSPACE_INDEX.md) ersetzt den aktiven Phantom-Link `packages/novapolis_common/README.md` jetzt durch den realen Einstieg [packages/README.md](packages/README.md).
- [novapolis-dev/docs/readme_decisions.md](novapolis-dev/docs/readme_decisions.md) fuehrt `WORKSPACE_INDEX.md` nicht mehr als offenen Phase-2-Verkuerzungspunkt, sondern nur noch als punktuelle Driftfix-Flaeche.
- [novapolis-dev/docs/todo.dev.md](novapolis-dev/docs/todo.dev.md) und [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) ziehen denselben Abschluss nach; das Dev-Board steht wieder bei `offen: 0`.
- Ein zusaetzlicher Root-Skripte-Landing-Block in [WORKSPACE_INDEX.md](WORKSPACE_INDEX.md) wurde bewusst nicht aufgenommen, weil der bestehende Root-Steuerpfad bereits den operativen Einstieg abdeckt.

Governance: Architektur-Notiz fixiert jetzt die Systemlesart als kontrollierte Simulation (2026-04-28 06:40)
---------------------------------------------------------------------------------------------------------

- [novapolis-dev/docs/architecture-summary-local-ai.md](novapolis-dev/docs/architecture-summary-local-ai.md) fuehrt jetzt explizit aus, dass Novapolis nicht als freier Chatbot, sondern als kontrolliertes Simulationssystem betrieben wird.
- Die Notiz trennt dabei bewusst zwischen Modellrollen und Fuehrungsstruktur: `llama3.1:8b`, `qwen3.5:4b` und `qwen2.5:7b` bleiben operative Rollen im A/B/Judge-Pfad, waehrend SSOT, DONELOG, STOP-Gates, Runtime-Artefakte, Frontmatter und Validatoren die eigentliche Verbindlichkeit tragen.

RP-Runtime: Expliziten Inventar-Diff fuer den kleinen Nordlinie-Turn-7/8-Satz nachgezogen (2026-04-28 05:09)
------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md) fuehrt den kleinen Behelfssatz jetzt nicht mehr nur als konsolidierten Mengenstand, sondern zusaetzlich als `Turn Delta Ledger` fuer Turn 7 und Turn 8.
- Turn 7 trennt jetzt sichtbar zwischen realer D5-Teilbereitstellung, belegtem Ersteinsatz an markierten Schwachzonen und der offenen Evidenzgrenze, dass noch nicht jede einzelne Komponente einem exakt benannten Punkt zugeordnet werden kann.
- Turn 8 zieht den Restverbrauch ohne neue D5-Lieferung komponentenscharf an der `Schottertasche Nordkante` nach und macht damit klar, warum genau `metallprofil-kurz`, `ausgleichsplatte` und `schraubensatz-mittel` dort auf Null laufen.

Governance: Evidence-Pflicht fuer ERP/RP explizit verankert (2026-04-28 04:56)
---------------------------------------------------------------------------

- [.github/instructions/rp-docs.instructions.md](.github/instructions/rp-docs.instructions.md) fuehrt jetzt agentuebergreifend die Kernregel `keine Aussage ohne Beleg` fuer ERP/RP: belastbar sind nur SSOT, bestehende Runtime-Dateien oder sauber benannte Session-Evidenz; fehlende Runtime-Traeger muessen vor der Nutzung aus SSOT, Governance und laufender Evidenz abgeleitet angelegt werden.
- [.github/agents/novapolis-rp-szenenlabor.agent.md](.github/agents/novapolis-rp-szenenlabor.agent.md) zieht dieselbe Regel fuer ausgespielte Turns, Admin-Bestaetigungen und Pflichtlesephase nach, inklusive `mind/` als regularem Runtime-Pfad.
- [novapolis-rp/database-curated/staging/rp-runtime/README.md](novapolis-rp/database-curated/staging/rp-runtime/README.md) macht den operativen Vertrag jetzt explizit: keine belastbare RP-Aussage ohne SSOT-/Runtime-Beleg, keine freie Zwischenbehauptung als Ersatz fuer fehlende Evidenz.

Archiv: weitere 5 Dev‑Einträge verschoben (Batch 5, 2026-06-13 07:50)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=5) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Zeit: 2026-06-13 07:50
- Snapshot-lock: PASS (2026-06-13 07:10).
- Validators: deferred (global run after all batches as per user directive).
- Archive: `novapolis-dev/archive/todo.dev.archive.md` angehängt (Batch 5 block).
- Note: Einträge wurden auf Existenz der referenzierten Evidenzdateien geprüft; Evidenzen sind vorhanden und im Archivblock referenziert.

Archiv: weitere 3 Dev‑Einträge verschoben (Batch 7, 2026-06-13 08:00)
-----------------------------------------------------------------

- Aktion: Validierung und Archivierung (Batch=7) ausgeführt; Einträge verschoben nach `novapolis-dev/archive/todo.dev.archive.md`.
- Zeit: 2026-06-13 08:00
- Snapshot-lock: PASS (2026-06-13 07:10).
- Validators: deferred (global run after all batches as per user directive).
- Archive: `novapolis-dev/archive/todo.dev.archive.md` angehängt (Batch 7 block).
- Note: Einträge wurden auf Existenz der referenzierten Evidenzdateien geprüft; Evidenzen sind vorhanden und im Archivblock referenziert.

RP-Runtime: Aktiven Nordlinie-Traegersatz fuer Figuren, D5 und Jonas-Lumen geschlossen (2026-04-28 04:50)
---------------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/ronja-kerschner/entity.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/reflex/entity.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/jonas-merek/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/jonas-merek/entity.md), [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/pahl-brenner/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/pahl-brenner/entity.md) und [novapolis-rp/database-curated/staging/rp-runtime/entities/characters/lumen/entity.md](novapolis-rp/database-curated/staging/rp-runtime/entities/characters/lumen/entity.md) fuehren den aktiven Nordlinie-Hauptpfad jetzt auch auf Figurenebene statt nur ueber Projekt-, Inventar- und Mind-Deltas.
- [novapolis-rp/database-curated/staging/rp-runtime/state/d5.md](novapolis-rp/database-curated/staging/rp-runtime/state/d5.md) zieht den aktuellen D5-Werkstatt- und Freigabestand als eigenen Runtime-Ort nach; [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) nennt Lumen in derselben Hauptpfadlage jetzt ausdruecklich mit.
- [novapolis-rp/database-curated/staging/rp-runtime/mind/lumen.md](novapolis-rp/database-curated/staging/rp-runtime/mind/lumen.md) fuehrt die bisher fehlende Jonas-Begleitinstanz als eigenen Runtime-Mind-Arbeitsstand; [novapolis-rp/database-curated/staging/rp-runtime/mind/jonas-merek.md](novapolis-rp/database-curated/staging/rp-runtime/mind/jonas-merek.md) traegt die Jonas-Lumen-Kopplung im aktiven Runtime-Slice jetzt explizit statt nur implizit.
- [novapolis-dev/docs/process/rp-runtime-surface-matrix.ssot.md](novapolis-dev/docs/process/rp-runtime-surface-matrix.ssot.md) fuehrt die aktuelle Mindestmenge jetzt belastbar mit Figuren-, D5- und Lumen-Traegern und haelt zugleich fest, dass fuer den Hauptpfad weiterhin keine pauschale Fraktions-, C6- oder Relationship-Vollspiegelung noetig ist.

RP-Runtime: Mind-Pfad und Surface-Matrix fuer den aktiven Laborbetrieb angelegt (2026-04-28 04:44)
---------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/mind/README.md](novapolis-rp/database-curated/staging/rp-runtime/mind/README.md) und [novapolis-rp/database-curated/staging/rp-runtime/mind/mind-template.md](novapolis-rp/database-curated/staging/rp-runtime/mind/mind-template.md) fuehren jetzt einen eigenen Runtime-Pfad fuer Mind-/Sphaeren-Arbeitsstaende statt diese Delta-Lesarten in `relationships/` oder `state/` zu verstecken.
- [novapolis-rp/database-curated/staging/rp-runtime/mind/ronja-kerschner.md](novapolis-rp/database-curated/staging/rp-runtime/mind/ronja-kerschner.md), [novapolis-rp/database-curated/staging/rp-runtime/mind/reflex.md](novapolis-rp/database-curated/staging/rp-runtime/mind/reflex.md), [novapolis-rp/database-curated/staging/rp-runtime/mind/jonas-merek.md](novapolis-rp/database-curated/staging/rp-runtime/mind/jonas-merek.md) und [novapolis-rp/database-curated/staging/rp-runtime/mind/pahl-brenner.md](novapolis-rp/database-curated/staging/rp-runtime/mind/pahl-brenner.md) ziehen den aktiven Nordlinie-Kerncast erstmals als Runtime-Mind-Arbeitsstand gegen die bestehenden Mind-Cluster-SSOTs nach.
- [novapolis-rp/database-curated/staging/rp-runtime/README.md](novapolis-rp/database-curated/staging/rp-runtime/README.md) fuehrt `mind/` jetzt in Struktur, Routing-Matrix und Vertragsregeln, und [novapolis-dev/docs/process/rp-labor-review-und-promotion-matrix.ssot.md](novapolis-dev/docs/process/rp-labor-review-und-promotion-matrix.ssot.md) behandelt `mind/` ab jetzt als gleichwertige Runtime-Typflaeche vor Promotion.
- [novapolis-dev/docs/process/rp-runtime-surface-matrix.ssot.md](novapolis-dev/docs/process/rp-runtime-surface-matrix.ssot.md) leitet fuer den gesamten RP-Baum her, welche Klassen wirklich runtime-pflichtig sind und welche bewusst SSOT-only bleiben; damit ist explizit geklaert, dass vor dem Weiterspielen nicht der gesamte `database-rp` vorgespiegelt werden muss.

Governance: Allgemeine RP-Terminologie-SSOT angelegt (2026-04-28 04:24)
----------------------------------------------------------------------

- [novapolis-rp/database-rp/00-admin/rp-terminologie.ssot.md](novapolis-rp/database-rp/00-admin/rp-terminologie.ssot.md) fuehrt jetzt einen ersten kontrollierten Begriffsrahmen fuer RP: Raumbegriffe, Schadstellenmuster, Befundstatus und bevorzugte Aufwand-/Kostenbenennung.
- Der Startsatz zieht insbesondere fuer Nordlinie-01 den bevorzugten Oberbegriff `U-Bahn-Tunnel` sowie erste belastbare Problemherd-Bezeichnungen wie `Schottertasche Nordkante` und `Schienenversatz Engbogen` vor.

RP-Runtime: Turn 8 replayt Problemherde jetzt direkt benannt und klassifiziert (2026-04-28 02:49)
----------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt Turn 8 jetzt nicht mehr nur atmosphaerisch, sondern mit direkt benannten Problemherden: `Schottertasche Nordkante`, `Haltepunktpaar Leitungszug` und `Uebergang Engbogen`.
- [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) zieht fuer die hinreichend untersuchten Schadstellen die Reparatur- und Aufwandsklassen nach: `Band M` fuer die lokale Nordkante, `Band H` fuer den Engbogen; die Kostenklasse des Leitungszug-Haltepunktpaars bleibt bis zur Volluntersuchung offen.

Governance: RP-Regel fuer Problemherde und Reparaturklassen verankert (2026-04-28 02:49)
-------------------------------------------------------------------------------------

- [.github/instructions/rp-docs.instructions.md](.github/instructions/rp-docs.instructions.md) fuehrt jetzt agentuebergreifend fuer RP-Runtime-Zuege die Pflicht ein, Problemherde direkt zu benennen und nach hinreichender Untersuchung mit Reparaturfolge, Kernmaterialien und Aufwand- oder Kostenklasse zu versehen.
- [.github/agents/novapolis-rp-szenenlabor.agent.md](.github/agents/novapolis-rp-szenenlabor.agent.md) zieht dieselbe Regel in die Qualitaetskriterien des ausgespielten Turns nach, damit Schadstellen nicht nur atmosphaerisch bleiben, sondern auswertbar benannt werden.

RP-Runtime: Turn 8 zieht den Folgekorridor nur mit realem Tunnelrest weiter (2026-04-28 02:37)
----------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt Turn 8 als engen Folgezug auf den in Turn 7 real gewonnenen Arbeitsraum: Ronja und Reflex erfassen weitere Fehler, aber behaupten keine neue D5-Lieferung.
- [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) zieht den enger gelesenen Fehlerkorridor und den ausgeschopften Tunnelrest auf den Runtime-Zustand nach.
- [novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md) verbucht nur den echten Restverbrauch aus Turn 7 auf Null; weiterer Materialfortschritt bleibt bis zu einer expliziten realen D5-Lieferung gesperrt.

Governance: Hook-Surface im Workspace gegen Ist-Bestand abgeglichen (2026-04-28 02:03)
-------------------------------------------------------------------------------

- [WORKSPACE_INDEX.md](WORKSPACE_INDEX.md) fuehrt den veralteten Verweis auf `novapolis_agent/.githooks/pre-commit` nicht mehr; aktiv dokumentiert bleiben nur [githooks/pre-commit](githooks/pre-commit) und [`.github/hooks/rp-runtime-loop-guard.json`](.github/hooks/rp-runtime-loop-guard.json).
- Der Abgleich bestaetigt fuer den aktiven Workspace: Git nutzt `core.hooksPath=githooks`, der Agent-Hook lebt unter `.github/hooks/`, und weitere Hook-Treffer liegen nur noch in Archiv-, Backup- oder Tooling-Kontexten.

Governance: RP-Runtime-Hook-Guard fuer Freigabe- und Mehrturn-Drift angelegt (2026-04-28 01:55)
-----------------------------------------------------------------------------------------------

- [.github/hooks/rp-runtime-loop-guard.json](.github/hooks/rp-runtime-loop-guard.json) haengt einen Workspace-PreToolUse-Hook ein, der Mutationen im RP-Runtime-Slice gegen den Mindestablauf prueft.
- [scripts/rp_runtime_loop_guard.py](scripts/rp_runtime_loop_guard.py) fragt bei unklarem Workflowanker nach und blockiert insbesondere neue Turn-Heading-Mutationen in `scene-log.md`, wenn der Prompt wie ein Admin-Fix ohne ausdrueckliche Freigabe aussieht.
- [novapolis_agent/tests/scripts/test_rp_runtime_loop_guard.py](novapolis_agent/tests/scripts/test_rp_runtime_loop_guard.py) deckt die kleinen Kernfaelle fuer `allow`, `ask` und `deny` ab.

Governance: Agentuebergreifende RP-Mindestschleife im Testbetrieb verankert (2026-04-28 01:51)
-------------------------------------------------------------------------------------------

- [.github/instructions/rp-docs.instructions.md](.github/instructions/rp-docs.instructions.md) fuehrt jetzt fuer Arbeit in `novapolis-rp/database-curated/staging/rp-runtime/**` einen kleinen, agentuebergreifenden Mindestablauf: Runtime-Dateien vor Folgezug neu lesen, pro Antwort nur einen begrenzten RP-Schritt zulassen und nach Admin-Rueckmeldung keinen neuen Turn ohne ausdrueckliche Freigabe starten.
- Der Nachzug setzt absichtlich nicht den vollen Szenenlabor-Vertrag fuer jeden Agenten global durch, erzwingt aber dieselbe Sicherheitskante dort, wo im RP-Testbetrieb sonst unbemerkt Mehrturn- oder Freigabe-Drift passieren koennte.

RP-Runtime: Turn-7-Handover und Begleitlogik auf Ist-Stand gezogen (2026-04-28 01:39)
--------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt Turn 1-7 jetzt als echten Handover-Stand; veraltete offene Punkte, die die Teilbereitstellung noch wie Turn 6 behandelten, sind gestrichen oder auf die neue Folgelage umgeschrieben.
- [novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md](novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md) fuehrt den kleinen Satz jetzt als reale Teilbereitstellung mit koerpernaher Reflex-Assistenz und korrigierter Blockerformulierung ueber den Turn-7-Satz hinaus.
- [novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md) trennt die Turn-6-Werkstattvorbereitung jetzt sauber vom Turn-7-Ist-Zustand, damit spaetere Datensammlung nicht dieselbe Bewegung gleichzeitig als vorbereitet und als noch nicht geliefert liest.

RP-Runtime: Turn 7 fuehrt Reflex jetzt ausdruecklich als Ronjas Exoskelett (2026-04-28 01:34)
----------------------------------------------------------------------------------------------

- [novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md](novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md) fuehrt den kleinen Stuetzsatz in Turn 7 jetzt nicht mehr so, als trage Reflex getrennt neben Ronja, sondern explizit koerpernah als an Ronja gebundene Exoskelett-Hilfe.
- Der Nachzug bleibt absichtlich klein und aendert weder Materialfluss noch Erfolgslage des Turns; korrigiert wird nur die Bindungslogik, damit sie mit [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md) und dessen Detachment-Regel deckungsgleich bleibt.

Workspace-Doc-Freshness: Scope von Dev-Subset auf workspaceweiten Pruefrahmen gehoben (2026-04-28 01:17)
----------------------------------------------------------------------------------------------------------

- [scripts/check_doc_freshness.py](scripts/check_doc_freshness.py) leitet seinen Scope nicht mehr aus [novapolis-dev/docs/active-surface-index.md](novapolis-dev/docs/active-surface-index.md) ab, sondern aus [novapolis-dev/docs/meta/doc-freshness-scope.md](novapolis-dev/docs/meta/doc-freshness-scope.md).
- Der neue Scope fuehrt Root-, Governance-, Dev-, Agent-, RP- und Sim-Doku sowie [workspace_tree.txt](workspace_tree.txt), [workspace_tree_dirs.txt](workspace_tree_dirs.txt) und [workspace_tree_full.txt](workspace_tree_full.txt) in einer eigenen Tabelle mit den Modi `frontmatter`, `legacy-header` und `mtime`.
- Globs werden jetzt explizit zu konkreten Dateien expandiert; ein gruener Lauf bedeutet damit nicht mehr still nur ein kleines Dev-Subset. Der aktuelle Recheck endet mit `scope_rows=46`, `expanded_glob_rows=12`, `checked_docs=262` und `findings=0`.
- [novapolis-dev/docs/active-surface-index.md](novapolis-dev/docs/active-surface-index.md) bleibt dabei absichtlich die Dev-Hub-Klassifikation und nicht mehr die operative Scope-Quelle des Freshness-Checks.

RP-Commitretry: Snapshot-Sync fuer Commit-Slice nachgezogen (2026-04-27 06:11)
--------------------------------------------------------------------------

- [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md), [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md), [novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md](novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md), [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Lagerhalle.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Lagerhalle.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Schleuse.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Schleuse.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Funkraum.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Funkraum.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Werkstatt.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Werkstatt.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Quarantaenehof.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Quarantaenehof.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/README.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/README.md), [novapolis-rp/database-rp/03-locations/E1.md](novapolis-rp/database-rp/03-locations/E1.md), [novapolis-rp/database-rp/03-locations/E2.md](novapolis-rp/database-rp/03-locations/E2.md) und [novapolis-rp/database-rp/03-locations/F2.md](novapolis-rp/database-rp/03-locations/F2.md) fuehren ihren `stand`-Wert jetzt gemeinsam auf dem frischen Snapshot-Lock `2026-04-27 06:11`.
- Der Retry adressiert ausschliesslich das zuvor vom Hook gemeldete Freshness-Fenster; die inhaltlichen RP-Hard-Gates waren bereits gruen.

RP-Laborpfad: Nordlinie-Runtime-Warenfluss geschlossen, C6-Hauptort als Empfangsanker nachgezogen (2026-04-27 06:06)
-----------------------------------------------------------------------------------------------------------------

- [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) fuehrt den letzten offenen RP-Punkt jetzt als erledigt; der kleine Nordlinie-Turn-7-Satz ist zwischen Runtime-Scene-Log, Runtime-Inventar und RP-SSOT als belastbare Teilbereitstellung mit Transfer, Einsatz und Tunnelrest konsistent geschlossen.
- [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) steht damit wieder bei `RP=0` offenen Punkten.
- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) fuehrt den C6-seitigen Empfangs- und Stagingpfad jetzt ueber den Hauptort [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md); [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Schleuse.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Schleuse.md) und [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Lagerhalle.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Lagerhalle.md) bleiben nur noch rueckwaertskompatible Stub-Ziele.
- [novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md](novapolis-dev/docs/process/rp-inventory-backfill-pilot-2026-03-20.md) dokumentiert dieselbe Autoritaetsverschiebung jetzt explizit im Prozesspfad, damit Inventar-, Pilot- und Ortsdoku denselben Zielanker fuehren.

RP-Ortsstruktur: E1/F2 angelegt, Tunnelknoten-Graph geschärft, D5/C6-Unterorte als Stubs zurückgeführt (2026-04-27 05:52)
---------------------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/03-locations/E1.md](novapolis-rp/database-rp/03-locations/E1.md) und [novapolis-rp/database-rp/03-locations/F2.md](novapolis-rp/database-rp/03-locations/F2.md) fuehren die bisher nur textlich behaupteten Anschlussknoten um `E2` jetzt als echte konservative Orts-SSOTs.
- [novapolis-rp/database-rp/03-locations/E2.md](novapolis-rp/database-rp/03-locations/E2.md) zeigt damit wieder konsistent auf echte Ortsdateien `e1`, `e3` und `f2` statt nur auf eine validatorreduzierte Restverbindung.
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md) und [novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3.md) fuehren ihre Frontmatter-Verbindungen jetzt bevorzugt ueber die eigenstaendigen Tunnel- und Unterortsknoten statt ueber direkte Stationskanten.
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Funkraum.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Funkraum.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Werkstatt.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Werkstatt.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Schleuse.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Schleuse.md) und [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Lagerhalle.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Lagerhalle.md) bleiben nur noch als Kompatibilitaetsstubs erhalten; autoritative Ortsdetails liegen jetzt in den starken Hauptorten `D5` und `C6`.
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Quarantaenehof.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Quarantaenehof.md) fuehrt den Ort nun passend zur aktuellen E3-Lesart als verriegelten Nachlaufraum der Evakuierung.
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/README.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/README.md) ist jetzt ausdruecklich nur noch Graphanker; Details bleiben in den Einzelorten und der Weltkarte.

RP-Commitpfad: Snapshot-Sync fuer den gesamten Orts- und Prozess-Slice nachgezogen (2026-04-27 05:33)
-----------------------------------------------------------------------------------------------

- Die aktuell zu pushenden Markdown-Dateien wurden vor dem Commit gemeinsam auf den frischen Snapshot-Lock `2026-04-27 05:33` synchronisiert, damit das Snapshot-Gate fuer aktive Doku- und RP-Dateien wieder sauber greift.
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md) fuehrt den zuletzt versehentlich in den Body gerutschten Zusatzblock jetzt wieder sauber im Frontmatter und als normale Statussektion.

RP-Ortsmodell: E2-Frontmatter vor Commit auf bestehende Orts-Slugs begrenzt (2026-04-27 05:16)
----------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/03-locations/E2.md](novapolis-rp/database-rp/03-locations/E2.md) behaelt die neue Lichtgarten- und Mehr-Ebenen-Lesart, fuehrt im `connections`-Frontmatter aber wieder nur den aktuell belegten validator-sicheren Orts-Slug `e3`.
- Die textliche Topologie zu `E1` und `F2` bleibt als Ortsbeschreibung erhalten; eigene Frontmatter-Verbindungen fuer diese Knoten folgen erst, wenn dafuer auch echte Ortsdateien existieren.

RP-Ortsmodell: Hauptort als Default, Unterort nur mit Separationsgrund festgezogen (2026-04-27 05:05)
----------------------------------------------------------------------------------------------------

- [novapolis-dev/docs/process/rp-ortsmodell-granularitaet.ssot.md](novapolis-dev/docs/process/rp-ortsmodell-granularitaet.ssot.md) legt jetzt RP-weit fest, dass Orte zuerst als starke Hauptdateien gefuehrt werden und Unterorte nur dann eine eigene Orts-SSOT erhalten, wenn sie einen echten Betriebs-, Risiko- oder Referenzgrund tragen.
- Die Ableitung bleibt bewusst kompatibel mit dem aktuellen Bestand: 2026-06-13 09:19

RP-Ortslesart: E3-Wasseraufbereitung als verriegelte Infrastrukturreserve geschaerft (2026-04-27 04:51)
------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Wasseraufbereitung.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Wasseraufbereitung.md) fuehrt den Ort jetzt nicht mehr nur als abstrakten POI, sondern als kritische, derzeit verriegelte Wasser- und Filterinfrastruktur hinter dem E3-Risikorahmen.
- Der Nachzug bleibt bewusst konservativ: belastbar sind Kritikalitaet, fehlende Freigabe, offener Filter- und Wasserdruck auf C6-Seite sowie der moegliche Zukunftswert fuer eine spaetere Reaktivierung; nicht behauptet werden freie Zugangswege, intakte Produktion oder konkrete Anlagenraeume.

RP-Ortslesart: E3 zieht die C6-E3-Korridorlogik jetzt am Stationsende nach (2026-04-27 04:28)
----------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3.md) fuehrt den Anschluss nach `C6` jetzt nicht mehr nur als pauschal begehbaren Verbindungsweg, sondern als durch Evakuierung belegten, kontrollierten Fuss- und Sicherungsarm mit verriegeltem E3-Ende.
- Damit ist die C6-E3-Kante jetzt auf beiden Seiten gleich gelesen: nutzbar fuer Evakuierung und Kontrolle, aber nicht als freie Rueckkehr- oder Routineverbindung normalisiert.

RP-Korridorlogik: Nordlinie 01 und C6-E3 auf belegten Fussbetrieb geschaerft (2026-04-27 04:18)
---------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md) beschreibt den D5-C6-Korridor jetzt nicht mehr als Projekt zur ersten Begehbarmachung, sondern als Belastbarkeits-, Sicherungs- und Materialfuehrungsprojekt fuer einen bereits genutzten Arbeitsweg.
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md) fuehrt den Tunnel jetzt ausdruecklich als im Fussbetrieb belegten, aber nicht normalisierten Sicherungs- und Evakuierungskorridor; [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md) zieht diese Lesart im Linienstatus nach.

RP-Korridorlesart: D5-C6 als mehrfach begangener U-Bahn-Arbeitsweg geschaerft (2026-04-27 04:13)
--------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md) fuehrt den Korridor jetzt explizit als regulaeren, beschaedigten U-Bahn-Tunnel, der bereits mehrfach zu Fuss passiert wurde und damit kein unpassierbarer Bruchraum ist.
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md) trennt diese belegte D5-Seite jetzt sauberer vom eigentlichen Nord- und E3-Risikodruck, damit die Ortslesart nicht den falschen Tunnel ueberdramatisiert.

RP-Ortslesart: C6 als gedrungener Novapolis-Aussenposten bildlich verdichtet (2026-04-27 04:06)
----------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md) fuehrt C6 jetzt nicht mehr nur als teilaktiven Aussenposten mit Zahlen- und Betriebsdaten, sondern als eng gefuehrten Vorposten mit Schleuse, Stagingraum, geschuetzter Kernzone, Technikzugang, Beobachtungskante und staendigem E3-/Norddruck.
- Die Verdichtung bleibt an vorhandene RP-Belege gebunden: 27 Personen auf kleiner aktiver Kernflaeche, Kora/Echo als lokale Filter- und Rueckmeldeinstanz, H-47 und E3-Evakuierte als Personendruck sowie der C6-seitig gesicherte, aber gefaehrliche Anschluss nach E3.

RP-Ortslesart: D5 als kompakter Novapolis-Kern bildlich verdichtet (2026-04-27 04:02)
---------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md) fuehrt D5 jetzt nicht mehr nur als funktionale Hauptbasis, sondern als engen, von innen reaktivierten Kernstandort mit restauriertem Kontrollraum, Wartungsgang, Schacht-/Unterbereich, Materialsockel am Bahnsteig und D5-seitiger Tunnelkante.
- Die Verdichtung bleibt an vorhandene RP-Belege gebunden: Ronja/Reflex als D5-seitige Korridorarbeiterinnen, Jonas/Pahl als Werkstatt- und Freigabeschiene, sowie der belegte Material- und Wartungspfad aus D5 heraus.

RP-Ortslesart: E2 als Lichtgarten-Hochrisikoknoten kanonisch verdichtet (2026-04-27 03:54)
-----------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/03-locations/E2.md](novapolis-rp/database-rp/03-locations/E2.md) fuehrt `E2` jetzt nicht mehr nur als neutralen Knoten mit Gasunfall-Nachhall, sondern als mehrstufigen Lichtgarten-Komplex mit altem Oberflaechenwahrzeichen, eingestuerzter Glaskuppel, offener Hallenebene, darunterliegendem Verteilergeschoss und weiter betriebsrelevanter Unterebene.
- Der Nachzug bleibt kompatibel mit der bisherigen Evidenz: aktive Hauptnutzung unten, keine feste Kerncrew, echter Transitdruck nach `E1` und `F2`, sowie ein deutlich riskanter, instabiler Bezug Richtung `E3`.

RP-Kartenlesart: Metrogradient und tote Zonen als In-World-Rahmen verankert (2026-04-27 02:53)
-----------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/00-admin/Metrokarte-T0.md](novapolis-rp/database-rp/00-admin/Metrokarte-T0.md) fuehrt jetzt explizit, dass sich die Metro im T0-Rahmen nicht wie ein einzelner Fraktionsklumpen anfuehlen soll, sondern wie ein Netz aus wenigen harten Kernen, neutralen Durchlaufraeumen, Schadenszonen und toten Bereichen mit steigendem Risiko-Loot-Verhaeltnis nach aussen.
- Dieselbe Karten-SSOT erlaubt jetzt ausdruecklich auch eine zentrale tote Zone: eine ehemalige grosse, halb offene oder witterungsexponierte Station darf als gefaehrlicher toter Keil mitten in einer wichtigen Netzachse liegen, ohne dass dafuer schon ein konkreter Stationsretcon behauptet wird.

RP-Kartenregel: neutrale Zwischenstationen im T0-Verteilungsbild wiederhergestellt (2026-04-27 02:42)
------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/00-admin/Metrokarte-T0.md](novapolis-rp/database-rp/00-admin/Metrokarte-T0.md) fuehrt die Verteilungsregel fuer neutrale Zwischenstationen jetzt wieder konsistent aus: die nicht-kernigen Marker `F5`, `F7`, `G1`, `G6`, `H1`, `H2` und `H3` wurden auf neutrale Puffer zurueckgesetzt, damit zwischen verschiedenen Fraktionskernen keine direkte Fraktions-zu-Fraktions-Kopplung mehr im T0-Verteilungsbild steht.
- Der Fix bleibt bewusst auf die Kartenverteilung begrenzt und folgt den bereits nachgezogenen konservativen Kernlesarten: aktive Eigenkerne bleiben `B2`, `D5`, `G7`, `F9`, `H12` und `K4`; nicht-kernige Korridor- oder Randstationen werden dadurch nicht nachtraeglich als Vollkerne gelesen.

RP-Kernmodell: Novapolis mit Kernbasis D5 und Aussenposten C6 nachgezogen (2026-04-27 02:24)
------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-betriebsmodell-t0.md](novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-betriebsmodell-t0.md) fuehrt jetzt den konservativen Arbeitsanker fuer Novapolis: `D5` als aktive Kernbasis, `C6` als teilaktiver Aussenposten und `D5 <-> C6` als primaerer Arbeits-, Versorgungs- und Sicherheitskorridor der Fraktion.
- [novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-nahraum-t0.md](novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-nahraum-t0.md) verdichtet denselben Raum als unmittelbaren Nahraum T0, damit Novapolis nicht nur ueber Einzelorte, sondern ueber Kernbasis, Aussenposten und Korridor als zusammenhaengender Aufbau- und Sicherungsblock lesbar bleibt.
- [novapolis-rp/database-rp/01-factions/novapolis/Novapolis.md](novapolis-rp/database-rp/01-factions/novapolis/Novapolis.md), [novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/README.md](novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/README.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md), [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md), [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md), [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md) und [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) fuehren diesen Anker jetzt deckungsgleich aus Fraktions-, Doctrine-, Orts- und Inventarsicht.

RP-Kernmodell: Haendlerbund mit externer Zentrale G7 und Niederlassungsanker C6 nachgezogen (2026-04-27 02:17)
--------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/haendlerbund-betriebsmodell-t0.md](novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/haendlerbund-betriebsmodell-t0.md) fuehrt jetzt den konservativen Arbeitsanker fuer den Haendlerbund: `G7` als aktive externe Zentrale, `C6` als eingebettete Niederlassung im Novapolis-Raum und `G7 <-> C6` als primaeren Arbeitskorridor zwischen Eigenkern und Partnerfenster.
- [novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/haendlerbund-nahraum-t0.md](novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/haendlerbund-nahraum-t0.md) verdichtet denselben Raum als unmittelbaren Nahraum T0, damit der Haendlerbund nicht nur ueber einen Kontaktpunkt, sondern ueber Zentrale, Niederlassung und Korridor als zusammenhaengender Handelsblock lesbar bleibt.
- [novapolis-rp/database-rp/01-factions/haendlerbund/Haendlerbund.md](novapolis-rp/database-rp/01-factions/haendlerbund/Haendlerbund.md), [novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/README.md](novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/README.md), [novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md](novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md), [novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md](novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md) und [novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md](novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md) fuehren diesen Anker jetzt deckungsgleich aus Fraktions-, Doctrine-, Orts-, Inventar- und Startbogensicht.

RP-Kernmodell: Fluesterkollektiv mit Betriebs- und Nahraumanker fuer K4 nachgezogen (2026-04-27 02:06)
------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-betriebsmodell-t0.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-betriebsmodell-t0.md) fuehrt jetzt den konservativen Arbeitsanker fuer das Fluesterkollektiv: `K4` als aktiver Kern, indirekte Kanalpfade als kontaktarmer Funktionsraum sowie die innere Konfliktlage zwischen Signalgewinn, Kanalhygiene, Abschirmung und Gegenaufklaerung.
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-nahraum-t0.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-nahraum-t0.md) verdichtet denselben Raum als unmittelbaren Nahraum T0, damit das Fluesterkollektiv nicht nur ueber K4 behauptet, sondern ueber Kern und indirekte Pfade als zusammenhaengender Signal- und Einflussblock lesbar bleibt.
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/Fluesterkollektiv.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/Fluesterkollektiv.md), [novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/README.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/README.md), [novapolis-rp/database-rp/01-factions/fluesterkollektiv/03-locations/K4.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/03-locations/K4.md) und [novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md) fuehren diesen Anker jetzt deckungsgleich aus Fraktions-, Doctrine-, Orts- und Inventarsicht.

RP-Kernmodell: Schattenbund mit Betriebs- und Nahraumanker fuer F9 nachgezogen (2026-04-27 02:06)
--------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/schattenbund-betriebsmodell-t0.md](novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/schattenbund-betriebsmodell-t0.md) fuehrt jetzt den konservativen Arbeitsanker fuer den Schattenbund: `F9` als aktiver Kern, `F9 -> G6` als Tarnungs- und Bewegungskorridor sowie die innere Konfliktlage zwischen Beschaffung, Abschirmung, Leak-Druck und Gegenaufklaerung.
- [novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/schattenbund-nahraum-t0.md](novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/schattenbund-nahraum-t0.md) verdichtet denselben Raum als unmittelbaren Nahraum T0, damit der Schattenbund nicht nur ueber F9 behauptet, sondern ueber Kern und aktiven Korridor als zusammenhaengender Schattenblock lesbar bleibt.
- [novapolis-rp/database-rp/01-factions/schattenbund/Schattenbund.md](novapolis-rp/database-rp/01-factions/schattenbund/Schattenbund.md), [novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/README.md](novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/README.md), [novapolis-rp/database-rp/01-factions/schattenbund/03-locations/F9.md](novapolis-rp/database-rp/01-factions/schattenbund/03-locations/F9.md) und [novapolis-rp/database-rp/01-factions/schattenbund/04-inventory/Schattenbund-inventar.md](novapolis-rp/database-rp/01-factions/schattenbund/04-inventory/Schattenbund-inventar.md) fuehren diesen Anker jetzt deckungsgleich aus Fraktions-, Doctrine-, Orts- und Inventarsicht.

RP-Kernmodell: Eisenkonklave mit Betriebs- und Nahraumanker fuer H12 nachgezogen (2026-04-27 02:02)
----------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/eisenkonklave-betriebsmodell-t0.md](novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/eisenkonklave-betriebsmodell-t0.md) fuehrt jetzt den konservativen Arbeitsanker fuer die Eisenkonklave: `H12` als aktiver Kern, der beschaedigte Zulauf `H3 -> H12` als Belastungs- und Sicherheitskorridor sowie die innere Konfliktlage zwischen Kontrolle, Versorgung, Werkstofflogik und selektiver Oeffnung.
- [novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/eisenkonklave-nahraum-t0.md](novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/eisenkonklave-nahraum-t0.md) verdichtet denselben Raum als unmittelbaren Nahraum T0, damit die Eisenkonklave nicht nur ueber H12 behauptet, sondern ueber Kern und Schadenskorridor als zusammenhaengender Kontrollblock lesbar bleibt.
- [novapolis-rp/database-rp/01-factions/eisenkonklave/Eisenkonklave.md](novapolis-rp/database-rp/01-factions/eisenkonklave/Eisenkonklave.md), [novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/README.md](novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/README.md), [novapolis-rp/database-rp/01-factions/eisenkonklave/03-locations/H12.md](novapolis-rp/database-rp/01-factions/eisenkonklave/03-locations/H12.md) und [novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md](novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md) fuehren diesen Anker jetzt deckungsgleich aus Fraktions-, Doctrine-, Orts- und Inventarsicht.

RP-Kernmodell: Schienenbund mit Betriebs- und Nahraumanker fuer B2 nachgezogen (2026-04-27 01:56)
------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/schienenbund-betriebsmodell-t0.md](novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/schienenbund-betriebsmodell-t0.md) fuehrt jetzt den konservativen Arbeitsanker fuer den Schienenbund: `B2` als aktiver Kern, `B1` als vorgeschalteter Vorpuffer, `C3` als verletzlicher Nachlauf sowie die innere Konfliktlage zwischen Netzbetrieb, Reparatur, Freigabe und Sperrlogik.
- [novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/schienenbund-nahraum-t0.md](novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/schienenbund-nahraum-t0.md) verdichtet denselben Korridor als unmittelbaren Nahraum T0, damit der Schienenbund nicht nur ueber `B2` behauptet, sondern ueber Zulauf, Kern und Nachlauf als zusammenhaengender Trassenblock lesbar bleibt.
- [novapolis-rp/database-rp/01-factions/schienenbund/Schienenbund.md](novapolis-rp/database-rp/01-factions/schienenbund/Schienenbund.md), [novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/README.md](novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/README.md), [novapolis-rp/database-rp/01-factions/schienenbund/03-locations/B2.md](novapolis-rp/database-rp/01-factions/schienenbund/03-locations/B2.md) und [novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md](novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md) fuehren diesen Anker jetzt deckungsgleich aus Fraktions-, Doctrine-, Orts- und Inventarsicht.

RP-Sozialmodell: Arkologie-A1 mit konservativem Bevoelkerungsmodell und Alltagsdoktrin nachgezogen (2026-04-27 01:44)
------------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/arkologie-a1-sozialmodell-t0.md](novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/arkologie-a1-sozialmodell-t0.md) fuehrt jetzt den zentralen Arbeitsanker fuer Arkologies Soziallesart: kein harter Zensus, sondern ein konservatives Stationsverhaeltnis `A1 > A5 > A3`, offene Bildung mit leistungsbezogener Zuteilung und spielbare Konfliktlinien zwischen Prestigezentrum und Betriebsarmen.
- [novapolis-rp/database-rp/01-factions/arkologie-a1/Arkologie-A1.md](novapolis-rp/database-rp/01-factions/arkologie-a1/Arkologie-A1.md) sowie [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A1.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A1.md), [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A3.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A3.md) und [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A5.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A5.md) verweisen denselben Sozialanker jetzt direkt aus Fraktions- und Ortssicht.
- [novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/README.md](novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/README.md) fuehrt das neue Sozialmodell im Doctrine-Index mit, damit Bildung, Zuteilung, Bevoelkerungsverteilung und Alltagskonflikt nicht als Streuwissen im Repo verbleiben.

RP-Soziallesart: Arkologie-A1 mit offener Bildung und betrieblicher Rollenverteilung nachgezogen (2026-04-27 01:39)
-----------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/arkologie-a1/Arkologie-A1.md](novapolis-rp/database-rp/01-factions/arkologie-a1/Arkologie-A1.md) fuehrt jetzt explizit, dass Arkologie-A1 Bildung und fachliche Schulung hoch gewichtet, den Zugang formal offen haelt und Zuteilung vor allem ueber Wissen, Leistung, Eignung und Freigabefaehigkeit liest, ohne kleinere Korruptions- und Netzwerkeffekte auszublenden.
- [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A1.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A1.md) fuehrt A1 jetzt als Schwerpunkt von Lehre, Forschung, Archiv und dichter Kernbevoelkerung; [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A3.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A3.md) und [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A5.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A5.md) lesen ihre Bevoelkerung dagegen bewusst als Pruef-, Sicherungs-, Versorgungs- und Wartungsarme fuer den Betrieb von A1.
- Die Arkologie bleibt damit als funktional kontrollierter Dreistationskern lesbar, ohne drei gleich dichte Macht- oder Siedlungszentren behaupten zu muessen; die innere Spannung entsteht jetzt sichtbar aus Bildungs- und Prestigeschwerpunkt in A1 bei realer Betriebslast in A3 und A5.

RP-Umfeld: Arkologie-A1-Nahraum bis Ring 2 und naechstem Fremdkorridor nachgezogen (2026-04-27 01:24)
----------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/arkologie-a1-nahraum-t0.md](novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/arkologie-a1-nahraum-t0.md) fuehrt jetzt den Arkologie-Nahraum konservativ bis zwei Stationsschritte aus: Kerngebiet `A1/A3/A5`, erster Ring `A2/A4/B5`, zweiter Ring `B1/A6/C5` und der naechste belegte Fremdfraktionskorridor Richtung `B2`.
- [novapolis-rp/database-rp/03-locations/A6.md](novapolis-rp/database-rp/03-locations/A6.md) und [novapolis-rp/database-rp/03-locations/C5.md](novapolis-rp/database-rp/03-locations/C5.md) wurden als fehlende Zweitring-Orte angelegt; [novapolis-rp/database-rp/03-locations/A4.md](novapolis-rp/database-rp/03-locations/A4.md) und [novapolis-rp/database-rp/03-locations/B5.md](novapolis-rp/database-rp/03-locations/B5.md) fuehren ihre Anschlusskanten jetzt wieder vollstaendig.
- [novapolis-rp/database-rp/01-factions/arkologie-a1/Arkologie-A1.md](novapolis-rp/database-rp/01-factions/arkologie-a1/Arkologie-A1.md) und [novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/README.md](novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/README.md) verlinken den neuen Nahraumanker direkt aus dem Fraktionskern heraus.

RP-Ledger: Arkologie-A1 mit Kerngebiet A1-A3-A5 nachgezogen (2026-04-27 01:14)
-----------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A3.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A3.md) und [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A5.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A5.md) existieren jetzt als fehlende Orts-SSOTs fuer den belegten Arkologie-Kern; [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A1.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A1.md) fuehrt denselben Dreistationskern jetzt verlinkt mit.
- [novapolis-rp/database-rp/03-locations/A4.md](novapolis-rp/database-rp/03-locations/A4.md) und [novapolis-rp/database-rp/03-locations/B5.md](novapolis-rp/database-rp/03-locations/B5.md) wurden im selben Lauf als fehlende neutrale Pufferorte angelegt, damit die neuen Arkologie-Verbindungen nach `A3 -> A4` und `A5 -> B5` nicht nur behauptet, sondern repo-seitig valide referenzierbar sind.
- [novapolis-rp/database-rp/01-factions/arkologie-a1/Arkologie-A1.md](novapolis-rp/database-rp/01-factions/arkologie-a1/Arkologie-A1.md) und [novapolis-rp/database-rp/01-factions/arkologie-a1/04-inventory/Arkologie-inventar.md](novapolis-rp/database-rp/01-factions/arkologie-a1/04-inventory/Arkologie-inventar.md) fuehren Arkologie-A1 jetzt explizit als Kerngebiet `A1/A3/A5` mit Leit-, Validierungs- und Versorgungsfunktion statt als impliziten Ein-Station-Sockel.
- [novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md](novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md) und [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) aggregieren denselben Dreistationskern jetzt auch auf Arbeits- und T0-Ebene.

RP-Ledger: Schienenbund mit Stationssockel und Instandsetzungsanker nachgezogen (2026-04-27 01:05)
-------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md](novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md) fuehrt jetzt B2 explizit als aktiven Stationssockel mit Betriebslager, kontrolliertem Transit-/Freigabelager und lokaler Instandsetzungsnahe.
- [novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md](novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md) zieht denselben Schienenbund-Pfad im Rahmenwert- und Rollenmatrixblock nach: Lager und kleine Produktionsnahe sind fuer B2 jetzt explizit erlaubt, waehrend freie Fabrik- oder Vollsortimentslogik weiter ausgeschlossen bleibt.

RP-Ledger: Rollenbasierte Promotionsmatrix fuer externe Fraktionen nachgezogen (2026-04-27 01:02)
--------------------------------------------------------------------------------------------------

- [novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md](novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md) fuehrt jetzt eine rollenbasierte Promotionsmatrix fuer Arkologie-A1, Schienenbund, Haendlerbund, Eisenkonklave, Schattenbund und Fluesterkollektiv.
- Der neue Block trennt fuer jede Fraktion zwischen aktuellem Sockel, Rollenanker, passendem naechstem Promotionspfad und explizitem Nicht-Ziel, damit kuenftige Nachzuege nicht aus allen Fraktionen dieselbe Lagerlogik machen.
- Die empfohlene Reihenfolge priorisiert zuerst rollennahe Ausbaupfade: Schienenbund ueber Infrastruktur-/Reparaturkorridor, danach Arkologie-A1 oder Eisenkonklave ueber kontrollierte Freigabefenster; Schattenbund und Fluesterkollektiv bleiben vorerst bewusst auf indirekteren Kontakt- und Signalpfaden.

RP-Inventar: C6-Stagingpfad zwischen Empfang und Baustellenabgang explizit gezogen (2026-04-27 00:51)
----------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) fuehrt jetzt den belegten Zwischenpfad `Eintreffen -> Bestandsaufnahme -> C6-Staging -> spaeterer Baustellenabgang` explizit, ohne freie Itemmengen fuer Schleuse, Lagerhalle oder Zielcharge zu behaupten.
- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md) fuehrt denselben D5->C6-Transfer jetzt deckungsgleich als C6-Stagingprozess statt als direkten Sprung von Empfang zu Baustellenverteilung.

RP-Inventar: Nordlinie-Turn-7-Abgang und Draisine-Werkstattbindung konkret gebucht (2026-04-27 00:44)
-------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md) fuehrt jetzt echte D5-Reststaende nach dem kleinen Nordlinie-Turn-7-Abgang sowie nach der aktuellen Draisine-Werkstattbindung.
- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md), [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md) und [novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md](novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md) fuehren denselben kleinen Turn-7-Stuetzsatz jetzt klassenweise mit Transfer, Einsatz und Tunnelrest statt nur als narrativen Behelfssatz.
- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md) fuehrt jetzt eine konkrete kleine Werkstattbindung aus D5 fuer den Prototyp; derselbe Abgang ist in [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md) als Fraktionsbuchung verdichtet.
- [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) liest damit Nordlinie und Draisine nicht mehr nur als Druckbild, sondern fuer den aktuellen Kleinrahmen auch als konkrete Projektbuchung.

RP-Inventar: Verbrauch fuer beide Stationen und offene Projekte nachgezogen (2026-04-27 00:06)
---------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md) fuehrt jetzt einen konservativen Verbrauchsrahmen fuer D5-Basisbetrieb sowie den kombinierten Werkstattdruck aus Nordlinie und Draisine.
- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) fuehrt jetzt einen konservativen Verbrauchsrahmen fuer den Stationsbetrieb mit `27` Personen sowie den Nordlinie-Druck auf Reserve- und Einsatzgueter.
- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md) buendelt denselben Verbrauch jetzt fraktionsweit ueber beide Stationen plus die offenen Projekte [Nordlinie-01](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md) und [Draisine-Transportmodul](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md).
- [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) spiegelt dieselbe Lage als T0-Operativbild: D5 begrenzt-stabil, C6 knapp, Nordlinie hoher Materialverbrauch, Draisine kleiner technischer Nebenverbrauch.

RP-Inventar: Bestehenden Warenindex erweitert und konservative D5-/C6-Istbestaende nachgezogen (2026-04-26 22:31)
-------------------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/00-admin/Waren-Index.md](novapolis-rp/database-rp/00-admin/Waren-Index.md) war bereits vorhanden und wurde nur um die aktuell fehlenden Klassen erweitert: Nordlinie-Stuetzbaukasten sowie schlanke Evakuierungs-/Stationsgueter fuer C6.
- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md) fuehrt jetzt einen konservativ generierten aktuellen Stationsbestand, der D5 als lange verriegelten Kernstandort mit relativ intaktem Altbestand, aber ohne breite Marktbequemlichkeit liest.
- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) fuehrt jetzt zusaetzlich die definierte Evakuierungsmitnahme aus E3 und einen angespannten aktuellen C6-Arbeitsbestand fuer 27 Personen.
- [novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md](novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md) spiegelt dieselbe Lage als T0-Ueberblick: D5 begrenzt, aber arbeitsfaehig; C6 knapp und priorisierungsbeduerftig.

RP-SSOT: Nordlinie-Stuetzbaukasten vor weiterem Warenfluss explizit festgezogen (2026-04-26 22:07)
------------------------------------------------------------------------------------------------

- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md) definiert `Stuetzelemente` jetzt als komponentenbasierten Baukasten aus Profilen, Formteilen und Verbindungsmitteln statt als pauschalen Lagerposten.
- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md) und [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md) fuehren dieselbe Lesart jetzt mit; offen bleiben weiter die zaehlbaren Klassenmengen und der Restbestand nach Runtime-Teilbereitstellung.
- [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md), [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) und [.github/agents/novapolis-rp-szenenlabor.agent.md](.github/agents/novapolis-rp-szenenlabor.agent.md) ziehen denselben Guard nach: Materialarten zuerst festziehen, dann erst weitere Warenbewegung narrativ oder runtime-seitig vergroessern.

RP-Governance: Mengen- und Restbuchung fuer Runtime-Warenfluss als offener Evidenzpunkt nachgezogen (2026-04-26 22:07)
---------------------------------------------------------------------------------------------------------------

- [novapolis-dev/docs/todo.rp.md](novapolis-dev/docs/todo.rp.md) fuehrt jetzt wieder genau einen offenen RP-Punkt: Die Nordlinie-Teilbereitstellung aus Turn 7 ist als realer Warenfluss belegt, aber noch nicht als belastbare Mengen- und Restbuchung geschlossen.
- [.github/agents/novapolis-rp-szenenlabor.agent.md](.github/agents/novapolis-rp-szenenlabor.agent.md) beschreibt dafuer jetzt explizit, wann die Formulierung `ohne harte Mengen- oder Restbuchung` zu verwenden ist und welche Evidenz mindestens vorliegen muss, bevor ein Transfer als belastbar gebucht gilt.
- [novapolis-dev/docs/todo.index.md](novapolis-dev/docs/todo.index.md) ist im selben Lauf auf `RP=1` synchronisiert, damit Board, Index und Agent denselben offenen Nachzug fuehren.

Workspace-Agenten: RP-Szenenlabor auf Admin-Loop und vollen Runtime-Datenabgleich nachgezogen (2026-04-26 21:54)
---------------------------------------------------------------------------------------------------------

- `.github/agents/novapolis-rp-szenenlabor.agent.md` fuehrt jetzt den festen Ablauf `Turn -> Admin-Auswertung -> Bestaetigung -> Admin-Freigabe` als Standard ein, statt freie Mehrturn-Fortsetzung zu erlauben.
- Derselbe Agent liest bei Admin-Rueckmeldungen kuenftig verpflichtend die betroffenen Runtime-Dateien zu Session, State, Inventar, Beziehungen und Figuren erneut ein; Warenfluss und Beziehungsaenderungen sind damit explizite Pflichtachsen statt impliziter Nebenpfad.
- Die Tool-Freigabe des RP-Agenten ist auf `read`, `search`, `edit` und `execute` gehoben, damit er Rueckmeldungen nicht nur textlich bestaetigt, sondern bei Bedarf auch validieren und Laufzeitdaten belastbar nachziehen kann.

RP-Runtime: Nordlinie Turn 7 mit erster kleiner D5-Teilbereitstellung fortgefuehrt (2026-04-26 21:44)
-----------------------------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` fuehrt jetzt Turn 7: D5 bringt erstmals einen kleinen Behelfssatz fuer markierte Schwachzonen in den Tunnelzug, ohne daraus einen falschen Reparaturdurchbruch zu machen.
- `novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md` und `novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md` spiegeln denselben Stand als Runtime-Typdaten: reale, aber eng begrenzte Teilbereitstellung; Schweißgeraet und `DN60` bleiben die harten Hauptblocker.
- Der Hauptweltpfad gewinnt damit einen belastbaren naechsten Anschluss fuer weiteres Bespielen unter Laborbedingungen, ohne Kanon, Mengenlage oder Fortschrittsgrad unnoetig aufzublaehen.

RP-Runtime: Nordlinie mit enger D5-Werkstattantwort fortgesetzt (2026-04-26 21:24)
-----------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` fuehrt jetzt einen weiteren Folgezug: D5 beantwortet die gegliederte Bedarfsskizze nicht mit einem Vollerfolg, sondern mit einer schmalen Werkstattvorbereitung fuer Stuetzelemente, waehrend Schweißgeraet und Adapter `DN60` weiter die harten Hauptblocker bleiben.
- `novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md` und `novapolis-rp/database-curated/staging/rp-runtime/inventories/d5.md` spiegeln denselben Laborstand jetzt typisiert mit: vorbereitete Stuetzelemente sind als enger Werkstattpfad lesbar, aber noch nicht als echte Teilbereitstellung oder Mengenbuchung promotable.
- Der Hauptweltpfad bleibt damit konsistent auf Nordlinie D5-C6, gewinnt aber einen engeren naechsten Anschluss fuer weitere Laborzuege, ohne den Materialmangel oder die SSOT-Grenzen weichzuzeichnen.

RP-Runtime: Figuren-Guard und Labor-/Review-Matrix fuer weitere Datensammlung eingezogen (2026-04-26 21:17)
-----------------------------------------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/entities/characters/mara-quell/entity.md` markiert die dortige Lesart jetzt ebenfalls explizit als verworfenen Probe-Einstiegspunkt statt als still lesbare Hauptwelt-Figurenfortsetzung.
- `novapolis-rp/database-curated/staging/rp-runtime/README.md` verweist jetzt auf eine kleine operative Matrix fuer Hauptweltpfad, Laborzuege, Review, Promotion und spaetere Trainingsnutzung.
- `novapolis-dev/docs/process/rp-labor-review-und-promotion-matrix.ssot.md` fasst denselben Guard erstmals als eigene SSOT zusammen: Nordlinie D5-C6 bleibt aktueller Hauptweltpfad; weitere RP-Fortsetzung unter Laborbedingungen ist ausdruecklich sinnvoll, aber nur mit sauberer Trennung zwischen Runtime, Hauptwelt und spaeterer Trainingsableitung.

RP-Runtime: Zeitlinien-Guard auch in C6-H47-Inventar und Beziehung nachgezogen (2026-04-26 21:13)
-------------------------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/inventories/c6.md` und `novapolis-rp/database-curated/staging/rp-runtime/relationships/mara-quell-zu-c6.md` markieren den C6-H47-Strang jetzt ebenfalls explizit als verworfenen Probe-Einstiegspunkt statt als still lesbare Hauptwelt-Fortsetzung.
- Damit tragen Szene, State, Inventar, Beziehung und Nordlinie-Index nun denselben Guard: keine Uebernahme aus mehreren Zeitlinien in den laufenden Hauptweltpfad ohne ausdrueckliche Richtungsentscheidung.


Archiv-Note (Batch 6 preparation, 2026-06-13 07:55)
--------------------------------------------------

- Aktion: Entfernung von 5 bereits archivierten Einträgen aus `novapolis-dev/docs/todo.dev.md` (Dedupe nach Archiv-Check).
- Zeit: 2026-06-13 07:55
- Befund: Die betreffenden Einträge waren bereits in `novapolis-dev/archive/todo.dev.archive.md` vorhanden (Batches 2–5), daher wurde nur das Live-Board bereinigt, ohne doppelte Archivierung.
- Snapshot-lock: PASS (2026-06-13 07:10).
- Validators: deferred (global run after all batches as per user directive).


RP-Runtime: Nordlinie als aktueller Weltstand explizit gegen C6-H47 abgegrenzt (2026-04-26 21:09)
-----------------------------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/c6-h47-handelsfenster-01/scene-log.md` und `novapolis-rp/database-curated/staging/rp-runtime/state/c6.md` markieren das fruehe C6-H47-Fenster jetzt explizit als Probe- und Routingversuch, der nicht weiter als laufender Hauptpfad fortgesetzt wird.
- `novapolis-rp/database-rp/01-factions/novapolis/Nordlinie-D5-C6-Index.md` fuehrt den Nordlinie-D5-C6-Strang jetzt genauso explizit als chronologisch aktuellen Welt- und Fortsetzungsstand fuer das laufende Bespielen im Chat.
- Damit ist fuer Review, Lore-Fortschreibung und spaetere Trainingsableitung klarer getrennt, welcher Runtime-Strang nur dokumentierte Probe blieb und welcher Strang aktuell als massgeblicher Fortsetzungsanker gelesen werden muss.

Workspace: Wochenabschluss auf grünem Evidenzstand nachgezogen (2026-04-26 20:40)
-------------------------------------------------------------------------------

- `scripts/run_checks_and_report.py` endet gegen `.tmp/results/reports/checks_report_20260426_203550.md` vollstaendig PASS und zieht den TODO-Index dabei erneut auf den aktuellen Gruenstand.
- `Checks: sim epoch assets` bleibt mit `summary=fail:0,warn:0` ohne Restbefund gruen; `Tests: coverage (fail-under)` endet separat mit `696 passed` und `92.19%` damit klar ueber Hard Gate (`>=80%`) und Qualitaetsziel (`>=90%`).
- `todo.root.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md` und `novapolis-dev/docs/todo.index.md` fuehren jetzt denselben Wochenabschlussstand; die Modul-Boards bleiben bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`.

Workspace: Kleiner Audit-Rest wieder geschlossen (2026-04-23 23:50)
--------------------------------------------------------------

- `todo.root.md` fuehrt wieder den aktuellen Modulstand `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`; der zuvor veraltete Kurzstatus ist damit aus der aktiven Root-Oberflaeche verschwunden.
- `novapolis-dev/docs/todo.sim.md` fuehrt den Resolver-Erfolg fuer den Godot-Headless-Verify jetzt ohne hostgebundenen Pfad; `scripts/check_portable_paths.py --repo-root .` ist damit wieder PASS.
- `novapolis_agent/scripts/training_release_gate.py`, `scripts/check_sim_hub_prefs_contract.py`, `scripts/run_sim_export_smoke.py` und der betroffene Testsatz unter `novapolis_agent/tests/scripts/` sind wieder Ruff-/Black-konform. Der gezielte Script-Testblock und der kanonische Voll-Lauf `scripts/run_checks_and_report.py` gegen `.tmp/results/reports/checks_report_20260423_234820.md` bleiben PASS. Damit stehen die Modul-Boards wieder bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`.

Workspace: Erneuter Auditlauf zeigt kleinen Dev-Rest in Doku-Portabilitaet und Python-Stil (2026-04-23 23:42)
-----------------------------------------------------------------------------------------------------------

- Der kanonische Recheck `scripts/run_checks_and_report.py` gegen `.tmp/results/reports/checks_report_20260423_234016.md` bleibt fuer `markdownlint`, `frontmatter`, `todo-index-sync`, `doc-freshness`, `logs-policy`, `pytest`, `pyright` und `mypy` gruen, faellt aber aktuell an `path-portability`, `ruff` und `black`.
- Der konkrete Portabilitaetsbefund sitzt in `novapolis-dev/docs/todo.sim.md` als hostgebundener Pfad `F:\Downloads\Godot\Godot_v4.6.1-stable_win64.exe`; parallel trug `todo.root.md` noch den veralteten Kurzstatus mit viermal fuenf offenen Boards und ist in diesem Lauf auf `Dev=1`, `RP=0`, `Agent=0`, `Sim=0` nachgezogen.
- Das Dev-Board fuehrt dafuer jetzt wieder genau einen offenen Steuerpunkt. Der Rest bleibt bewusst klein und belegt: aktive Doku-Portabilitaet plus der aktuelle Ruff-/Black-Dateisatz unter `novapolis_agent/` und `scripts/`.

Sim: Headless-Verify ueber laufende Godot-Binary wieder gruen (2026-04-23 18:34)
-----------------------------------------------------------------------------

- `scripts/run_sim_headless_verify.py` erkennt unter Windows jetzt auch den Pfad eines bereits laufenden lokalen Godot-Prozesses ueber `pwsh` oder `powershell` und nutzt ihn als Resolver-Fallback hinter `GODOT_BIN`, `godot4` und `godot`.
- Der kanonische Task `Checks: sim headless verify` loest im aktuellen Workspace-Kontext damit automatisch `F:\Downloads\Godot\Godot_v4.6.1-stable_win64.exe` auf und endet wieder mit `SIM_VERIFY: OK` statt am frueheren Exit `2`.
- `novapolis_agent/tests/scripts/test_run_sim_headless_verify.py` sichert denselben Fallback mit zwei fokussierten Unit-Tests ab. Damit stehen die Modul-Boards wieder bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`.

Workspace: Feste Audit-Segmente fuer den Gesamt-Workspace eingefuehrt (2026-04-23 18:27)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/process/workspace-audit-segmente.ssot.md` teilt den Workspace jetzt erstmals kanonisch in sieben wiederverwendbare Pruefsegmente: Root-Steuerflaeche, Shared Tooling/Pakete, Dev-Hub, Agent, RP, Sim sowie historische/generierte Flaechen.
- `README.md`, `WORKSPACE_INDEX.md` und `novapolis-dev/README.md` fuehren denselben Auditrahmen jetzt direkt in ihrer Navigationsoberflaeche mit, sodass kuenftige Workspace-Pruefungen nicht mehr ad hoc, sondern gegen denselben festen Zuschnitt laufen.
- Erster Iststand: 2026-06-13 09:19

Sim: Agent-Form-Workflow aus Main.gd in eigenen Controller gezogen (2026-04-23 17:39)
------------------------------------------------------------------------------------

- `novapolis-sim/scripts/agent_form_workflow_controller.gd` uebernimmt jetzt das branchige Open/Select/Apply-Routing fuer `datasets`, `synonyms`, `finetune`, `profiles`, `advanced` und `jobs`.
- `novapolis-sim/scripts/Main.gd` reicht fuer denselben Agent-Studio-Formpfad jetzt nur noch Session-, Payload-, Persistence- und Runtime-State in den neuen Controller hinein, nimmt das Pipeline-Ergebnis entgegen und bleibt bei UI-Refresh plus Result-Anwendung.
- `get_errors` bleibt fuer `Main.gd`, `agent_form_workflow_controller.gd` und `agent_form_session_controller.gd` ohne Befund. Der formale Board-Abschluss bleibt dennoch offen, weil `Checks: sim headless verify` weiterhin mit `Could not resolve a Godot executable` auf Exit `2` faellt. Der Modulstand bleibt damit `Dev=0`, `RP=0`, `Agent=0`, `Sim=1`.

Agent: Gemeinsamen Release-Gate-Pfad vor Export und LoRA eingezogen (2026-04-23 16:38)
---------------------------------------------------------------------------------------

- `novapolis_agent/scripts/training_release_gate.py` ist jetzt der kanonische Repo-Guard vor `curate_dataset_from_latest.py` und `fine_tune_pipeline.py`.
- Der Guard erzwingt `validate_eval_datasets --strict`, einen grünen `rp_content`-Beleg und die passende Provenienzschwelle; Exportpfade akzeptieren reviewpflichtige Datasets bis `gelb`, LoRA-Laeufe verlangen fuer den konkreten Trainingsdatensatz `gruen`.
- Der fokussierte Pytest-Block fuer `test_training_release_gate.py`, `test_fine_tune_pipeline_edges.py` und `test_curate_dataset_from_latest_minimal.py` bleibt PASS; der direkte Repo-Lauf blockiert aktuell sauber an `missing rp_content results` statt ungeguardet in LoRA zu springen. Der Modulstand liegt damit jetzt bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=1`.

Sim: Exportanker, Export-Smoke, Minimal-Vollstand und Hub-Prefs-Contract geschlossen (2026-04-23 16:38)
-----------------------------------------------------------------------------------------------------

- `novapolis-sim/export_presets.cfg` fuehrt jetzt den Windows-Desktop-Pfad `exports/windows/NovapolisSim.exe` repo-seitig als Godot-Presetanker.
- `scripts/run_sim_export_smoke.py`, `scripts/check_sim_hub_prefs_contract.py` und die neuen Tasks `Checks: sim export smoke`, `Checks: sim epoch assets (minimal fullstand)` sowie `Checks: sim hub prefs contract` ziehen die vier repo-loesbaren Sim-Reste in eigene Pruefpfade.
- Unter `novapolis-sim/data/epochs/epoch01/` plus `novapolis-sim/assets/audio/` liegt jetzt ein kleiner Vollstand; `scripts/check_sim_epoch_assets.py --repo-root . --check-slot-consistency` endet damit im Repo-Stand mit `summary=fail:0,warn:0`.
- Der neue Pytest-Block fuer `test_run_sim_export_smoke.py`, `test_check_sim_hub_prefs_contract.py` und `test_check_sim_epoch_assets.py` ist PASS. Offen bleibt im Sim-Scope nur noch der Headless-Verify, weil lokal weiterhin keine Godot-Binary aufloesbar ist. Der Modulstand liegt damit jetzt bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=1`.

RP-Runtime: Selektiver Transcript-Backfill fuer Nordlinie-Session nachgezogen (2026-04-23 14:26)
--------------------------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/transcript.jsonl` fuehrt jetzt neben dem Bootstrap-Record auch belegte Originalnachrichten aus dem exportierten VS-Code-Chat mit: Agentwechsel-Erfassung, Story-Fortsetzungsauftrag, die Architekturantwort zum Rohtranskriptpfad und die folgende Auswahl `2. und 1.`.
- Der Ruecktrag bleibt bewusst ehrlich selektiv: Ein `correction`-Record markiert `selective_backfill_applied`, waehrend die bislang im engen Suchlauf nicht wiedergefundene ausloesende Nutzerfrage zur Transcript-Architektur explizit als weiter offen dokumentiert ist.
- Damit ist die Rohspur fuer `d5-c6-nordlinie-sanierung-01` nicht mehr nur vorbereitet, sondern auf belegte Entscheidungs- und Uebergabepunkte aus dem bisherigen Chatverlauf zurueckgezogen, ohne stilles Umschreiben oder erfundene Rueckdatierung. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: RP-Chattranskriptpfad als append-only Rohspur angelegt (2026-04-23 13:26)
------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-chat-transcript-flow.ssot.md` definiert jetzt den kleinen Vertragsrahmen fuer `sessions/<session-id>/transcript.jsonl`: append-only, roh, nachvollziehbar, aber weder RP-SSOT noch direkter Trainingsinput.
- `novapolis-rp/database-curated/staging/rp-runtime/README.md`, `sessions/README.md` und `sessions/session-template.md` fuehren denselben Pfad jetzt direkt in der Runtime-Struktur mit; `sessions/transcript-template.jsonl` liefert ein minimales JSONL-Schema.
- Fuer `d5-c6-nordlinie-sanierung-01` liegt bereits ein Bootstrap-Record in `sessions/d5-c6-nordlinie-sanierung-01/transcript.jsonl`, der den Start der Repo-seitigen Rohspur ehrlich als `backfill_status=not_backfilled` markiert.
- `novapolis_agent/docs/runbook.md`, `novapolis-dev/docs/architecture-summary-local-ai.md`, `novapolis-dev/docs/todo.agent-board.md` und `novapolis-dev/docs/todo.index.md` ziehen denselben Truth-Layer- und Promotionsrahmen nach. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: Gebuendelte Nordlinie-Folge-Szene mit erster Materialerfassung nachgezogen (2026-04-21 07:33)
-------------------------------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` fuehrt jetzt Turn 5: Ronja und Reflex ziehen die Markierungsarbeiten als gebuendelten Arbeitsblock weiter und fassen den Folgeabschnitt erstmals materiell gegliedert.
- `state/nordlinie-01.md` zieht denselben Schritt als lesbarer strukturierten Sanierungsstand nach; `inventories/d5.md` trennt harte Sofortblocker (`Schweißgeraet`, `Adapter DN60`) jetzt sichtbar von markierten Folgebedarfen (`Stuetzelemente` an Schwachzonen), ohne daraus schon eine Lieferung zu machen.
- Damit ist der Nordlinie-Zug fuer die naechste Werkstatt- oder Materialantwort vorbereitet, ohne den vorbereitenden Charakter der Tunnelsanierung oder die offene Beleglage zu beschoenigen. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Index: Nordlinie-D5-C6-Fortsetzungsindex angelegt und verdrahtet (2026-04-21 07:28)
------------------------------------------------------------------------------------

- Unter `novapolis-rp/database-rp/01-factions/novapolis/Nordlinie-D5-C6-Index.md` liegt jetzt ein fokussierter Index fuer den aktiven Tunnel- und Werkstattstrang zwischen `D5` und `C6`.
- Der Index buendelt die relevanten Projekt-, Orts-, Figuren-, Missions- und Inventar-SSOTs und markiert den aktuellen Runtime-Handover sauber als Arbeitsstand ausserhalb des RP-SSOT.
- `novapolis-rp/database-rp/01-factions/novapolis/README.md` sowie die Teilindizes fuer `02-characters`, `03-locations` und `05-projects` verweisen jetzt direkt auf denselben Fortsetzungsindex. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: Agentwechsel in SSOT-/Lore-Modus als vollzogen erfasst (2026-04-21 07:23)
-----------------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` fuehrt jetzt einen expliziten `Admin Handover` mit `agent_switch: vollzogen`, Zielmodus `SSOT, Story, Weltgeschichte, Lore` und derselben Handoverbasis aus dem nicht unterbrochenen Vorspulwurf.
- `state/nordlinie-01.md` zieht dieselbe Admin-Lesart nach: Der Folgeagent startet nicht mehr auf einer vorbereiteten, sondern auf einer bereits uebernommenen Wechselkante.
- Damit ist im Repo nicht nur die Vorbereitung, sondern auch der tatsaechliche Wechselzustand dokumentiert; die Tagespruefung bleibt wie vorgesehen spaeter nachgezogen. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: Nordlinie-Handover fuer Agentwechsel nach nicht unterbrochenem Vorspulwurf nachgezogen (2026-04-21 07:23)
-----------------------------------------------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` fuehrt jetzt Turn 4 mit dem echten Vorspulwurf `1W6 = 4`: kein Ereignis unterbricht die laufenden Markierungsarbeiten.
- `state/nordlinie-01.md` zieht denselben Handover-Zustand nach: beidseitig vorsichtiger Sanierungsmodus, keine neue Gefahr, kein Durchbruch, kein Materialwunder, aber freie Bahn fuer eine gebuendelte Folgeszene zu Markierungsarbeiten und erster Materialerfassung.
- Damit ist der naechste Agentwechsel fachlich vorbereitet: Der Folgeagent kann direkt SSOT-, Story-, Welt- und Lore-Fortschreibung auf dem bestehenden Nordlinie-Stand beginnen, ohne eine fehlende Zwischenszene rekonstruieren zu muessen. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: Nordlinie-Zug um C6-Lageabgleich erweitert (2026-04-21 02:02)
-----------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` fuehrt jetzt Turn 3: Ronja markiert am Problemabschnitt weiter und holt zwischendurch einen knappen Status von C6 ein.
- `state/nordlinie-01.md` verdichtet daraus keinen freien Fortschritt, sondern einen beidseitig vorsichtigen Sanierungsmodus: D5 und C6 arbeiten weiter an derselben Linie, aber ohne Durchbruch, Materialwunder oder freigegebenen Abschnitt.
- Damit bleibt die Runtime-Lesart weiter konsistent mit dem SSOT-Rahmen der Nordlinie: beidseitige Arbeit ja, beschoenigter Fortschritt nein. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: Nordlinie-Zug mit D5-Rueckmeldung fortgefuehrt (2026-04-21 02:02)
-------------------------------------------------------------------------

- `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` fuehrt jetzt auch Turn 2: D5 bestaetigt Ronjas Meldung knapp, verspricht keine Wunderloesung und laesst den Engpass an Schweißgeraet und DN60-Adaptern bewusst offen.
- `state/nordlinie-01.md` zieht denselben Projektstand als laufenden Material- und Werkstattdruck nach; `inventories/d5.md` bleibt eine Bedarfs- statt Transfernotiz, fuehrt nun aber die bestaetigte Priorisierung ohne sofortige Ausgabe mit.
- Damit bleibt die Runtime-Lesart belastbar: D5 reagiert, aber es wird nichts stillschweigend verfuegbar gemacht, was im SSOT weiter fehlt. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: Nordlinie-Sanierungszug mit Status- und Bedarfsrouting angelegt (2026-04-21 02:02)
-------------------------------------------------------------------------------------------------

- Unter `novapolis-rp/database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` liegt jetzt ein erster Runtime-Zug fuer Ronjas laufende Tunnelsanierung zwischen D5 und C6.
- Die belastbaren Nebenfolgen des Zugs sind getrennt in `state/nordlinie-01.md` und `inventories/d5.md` nachgezogen: einmal als knapper Projektstatus fuer Nordlinie 01, einmal als noch nicht erfuellter D5-Materialbedarf fuer Schweißgeraet, DN60-Adapter und Stuetzelemente.
- Alle neuen Artefakte bleiben bewusst `Probe` oder `working`, referenzieren den bestehenden SSOT-Rahmen aus Nordlinie-01, Draisine-Transportmodul und Verbindungstunnel D5-C6 und behaupten keinen bereits erfolgten Materialfluss. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

Agent-Customization: Testwechsel fuer RP-Szenenlabor vorbereitet (2026-04-21 02:02)
-------------------------------------------------------------------------------------

- `.github/agents/novapolis-rp-szenenlabor.agent.md` fuehrt im `argument-hint` jetzt auch Session-ID und Runtime-Verwaltung explizit mit, damit der Wechsel im Agentenwaehler zielgerichteter startet.
- `novapolis-rp/database-curated/staging/rp-runtime/README.md` enthaelt jetzt einen kompakten Teststart mit einem sofort nutzbaren Prompt fuer `c6-h47-handelsfenster-01` und der erwarteten Routing-Spur in `sessions/`, `inventories/`, `relationships/` und `state/`.
- Damit ist der naechste Agentwechsel nicht nur technisch moeglich, sondern fuer einen ersten Turn-2-Probelauf direkt vorbereitet. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: Beispielzug mit kompletter Routing-Spur angelegt (2026-04-21 01:53)
-------------------------------------------------------------------------

- Unter `novapolis-rp/database-curated/staging/rp-runtime/sessions/c6-h47-handelsfenster-01/scene-log.md` liegt jetzt ein konkreter Beispielzug, der das neue Routing nicht nur beschreibt, sondern mit echten Runtime-Artefakten vorfuehrt.
- Die Nebenfolgen des Zugs sind getrennt in `characters/mara-quell.md`, `relationships/mara-quell-zu-c6.md`, `inventories/c6.md` und `state/c6.md` abgelegt. Damit ist das Muster fuer `Session -> Figur -> Beziehung -> Inventar -> Status` direkt im Repo sichtbar.
- Alle neu angelegten Dateien bleiben bewusst `Probe` oder `working`, referenzieren belegte SSOT-Anker aus C6, Mara Quell und dem H-47/C6-Versorgungsrahmen und vermeiden damit freie Kanon-Promotion. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Agent: Automatische Routing-Logik fuer Laufzeitdaten geschaerft (2026-04-21 01:50)
------------------------------------------------------------------------------------

- `.github/agents/novapolis-rp-szenenlabor.agent.md` fuehrt jetzt eine explizite Routing-Logik nach Aenderungsart: Szenenzuege gehen in `sessions/`, Figuren in `characters/`, Beziehungsverschiebungen in `relationships/`, Bestandsaenderungen in `inventories/` und uebergeordnete Weltfolgen in `state/`.
- Fuer Mischfaelle ist jetzt festgezogen, dass der eigentliche RP-Zug immer im Session-Log landet, zusaetzliche belastbare Folgen aber parallel in die passenden Typdateien geschrieben werden statt in einem unscharfen Sammelartefakt zu verschwinden.
- `novapolis-rp/database-curated/staging/rp-runtime/README.md` spiegelt dieselbe Routing-Matrix fuer den Arbeitsbereich, damit Agent-Vertrag und Runtime-Doku wieder denselben Schreibpfad fuehren. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

RP-Runtime: Konkrete Unterstruktur und Vorlagen angelegt (2026-04-21 01:38)
-------------------------------------------------------------------------

- Unter `novapolis-rp/database-curated/staging/rp-runtime/` liegen jetzt die festen Unterordner `sessions/`, `characters/`, `relationships/`, `inventories/` und `state/` jeweils mit eigener Leitdatei und einer einfachen Vorlage. Damit hat der RP-Agent jetzt konkrete Landing-Paths statt nur eines abstrakten Schreibbereichs.
- `sessions/` ist auf laufende Sitzungsordner mit `scene-log.md` ausgerichtet; `characters/`, `relationships/`, `inventories/` und `state/` trennen Figuren-, Beziehungs-, Bestands- und Weltstatusarbeit bewusst auseinander. Alle Pfade bleiben Arbeitsstand und markieren ihre Inhalte weiter explizit als `Probe`, `working`, `review_required` oder `promotion_ready`.
- Der RP-Agent kann damit laufende Verwaltung fuer Inventar, Beziehungen, neue Figuren und Statuswechsel jetzt strukturiert ablegen, ohne direkt RP-SSOT und Runtime-Arbeitsdaten zu vermischen. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

Agent-Customization: RP-Agent auf kontrollierten Laufzeitbereich umgestellt (2026-04-21 01:34)
---------------------------------------------------------------------------------------------

- `.github/agents/novapolis-rp-szenenlabor.agent.md` ist nicht mehr read-only. Der Agent darf jetzt kontrolliert schreiben, aber standardmaessig nur unter `novapolis-rp/database-curated/staging/rp-runtime/**` statt direkt im RP-SSOT.
- Der neue Leitpfad `novapolis-rp/database-curated/staging/rp-runtime/README.md` definiert dafuer die Arbeitsflaeche fuer Szenenlogs, Figuren, Beziehungen, Inventare und Zustandsdateien. Alles dort bleibt bewusst Arbeitsstand und wird erst nach Review oder expliziter User-Freigabe nach `database-rp/**` promoted.
- Damit ist der RP-Agent fuer laufende Verwaltung brauchbar, ohne Kanon und Laufzeitdaten zu vermischen. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

Agent-Customization: Workspace-Agent fuer RP-Szenenlabor angelegt (2026-04-21 01:28)
--------------------------------------------------------------------------------------

- Unter `.github/agents/novapolis-rp-szenenlabor.agent.md` liegt jetzt ein eigener, user-invocable Workspace-Agent fuer RP im Chat. Er trennt Inworld-Szene und OOC-Auswertung, priorisiert Ton-, Stimmungs- und Figurenstimmen-Kalibrierung und markiert Kanonlage sowie Wiederverwendbarkeit jedes Zugs explizit.
- Der Agent bleibt absichtlich read-only auf Repo-Ebene und darf nur lesen und suchen. Damit taugt er fuer belastbare RP-Weiterfuehrung und Stiltests, ohne nebenbei Workspace-Dateien oder Logs zu mutieren.
- Der neue Agent ergaenzt den bestehenden Governance-Agenten unter `.github/agents/novapolis-workspace-navigator.agent.md` um einen klar getrennten Dialog- und Szenenmodus. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

Agent-Implementierung: Rueckkopplung vom Session-Promotionspack in Eval/Export verdrahtet (2026-04-21 01:10)
--------------------------------------------------------------------------------------------------------------

- `.vscode/tasks.json` fuehrt jetzt die beiden Rueckkopplungs-Tasks `Eval: session promotions review (10, asgi)` und `Data: export+pack (session promotions review)`, damit das reviewpflichtige Curation-Pack nicht roh in Trainingsjobs, sondern ueber einen getaggten Results-Lauf in denselben Export-/Pack-Vertrag geht.
- `novapolis_agent/scripts/curate_dataset_from_latest.py` akzeptiert dazu jetzt `--results-glob`, sodass der Export-/Pack-Schritt gezielt `results_*_session_promotions*.jsonl` statt irgendeiner neuesten Results-Datei waehlt.
- `novapolis_agent/tests/scripts/test_curate_dataset_from_latest_minimal.py` und `novapolis_agent/tests/test_export_and_prepare_pipeline.py` sichern denselben Pfad gegen Drift ab: gezielte Results-Auswahl, Rueckaufloesung auf das Curation-Dataset ueber `results._meta.patterns` und anschliessender Prepare-Pack-Lauf bleiben PASS. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

Agent-Implementierung: Zweiter RP->Training-Schnitt mit Session-/Replay-Promotionspack eingezogen (2026-04-21 00:52)
-----------------------------------------------------------------------------------------------------------------

- `novapolis_agent/scripts/build_session_promotion_pack.py` erzeugt jetzt ein getrenntes Curation-Pack unter `novapolis_agent/eval/datasets/curation/session_promotions.v1.jsonl` aus dem kanonischen Session-Artefaktquartett `savegame.json`, `replay_manifest.json`, `pc_log.jsonl` und `world_log.jsonl` statt rohe Laufzeitartefakte direkt in Trainingsjobs zu schieben.
- `scripts/agent/build_session_promotion_pack.py`, `.vscode/tasks.json` und `novapolis_agent/tests/scripts/test_build_session_promotion_pack.py` fuehren denselben Pfad als Root-Wrapper, kanonischen Task `Data: build session promotion pack` und gezielt abgesicherten Script-Scope; der erste belegte Builder-Lauf hat 10 valide reviewpflichtige Promotions-Records geschrieben.
- `novapolis-dev/docs/dataset-provenance.md`, `novapolis-dev/docs/architecture-summary-local-ai.md`, `novapolis_agent/docs/runbook.md`, `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` fuehren denselben getrennten Pfad `Runtime Session -> Session Promotion Pack -> RP-SSOT oder freigegebene Trainingsableitung` jetzt deckungsgleich mit. Der Modulstand bleibt dabei `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

Agent-Implementierung: Erster RP->Training-Schnitt mit Builder, Tasks und Referenzdoku eingezogen (2026-04-20 22:03)
---------------------------------------------------------------------------------------------------------------

- `.vscode/tasks.json` fuehrt jetzt die beiden Root-Tasks `Data: build training from RP (lore)` und `Data: build training from RP (ops)`, damit RP-abgeleitete Trainings-Seed-Pakete nicht ueber freie Terminal-Sonderwege entstehen.
- `novapolis-dev/docs/dataset-provenance.md`, `novapolis-dev/docs/architecture-summary-local-ai.md` und `novapolis_agent/docs/runbook.md` fuehren denselben Truth-Layer-, Promotions- und Gate-Rahmen jetzt explizit mit: RP-SSOT bleibt Quelle, Laufzeitlogs bleiben getrennt, Trainingspakete sind abgeleitete Seeds.
- `novapolis-dev/docs/todo.agent-board.md` fuehrt denselben ersten Umsetzungsschnitt als Arbeitsstand am offenen Agent-Punkt; `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` bleiben auf demselben Modulstand `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

Agent-Plan: RP-SSOT, Spielstand und Trainingsableitung wieder als offener Ausbaupunkt verankert (2026-04-20 21:48)
-------------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.agent-board.md` fuehrt jetzt wieder genau einen offenen Agent-Punkt, der RP-SSOT, Session-/Replay-Artefakte und kuratierte Trainingspakete explizit trennt, statt rohes RP oder Laufzeitlogs direkt in Trainingsjobs laufen zu lassen.
- Der konkrete Plan legt denselben Ausbaupfad auf `Truth-Layer -> RP-Train-Builder -> Promotionspfad -> Gates -> Export/Pack -> LoRA` fest und verankert dazu die Zielpfade `novapolis_agent/scripts/build_training_from_rp.py`, `novapolis_agent/eval/datasets/training/` sowie die Pflichtquellen `dataset-provenance.md`, `architecture-summary-local-ai.md` und `novapolis_agent/docs/runbook.md`.
- `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` fuehren denselben offenen Agent-Stand jetzt wieder deckungsgleich mit `Dev=0`, `RP=0`, `Agent=1`, `Sim=5`.

Wochenabschluss: CPU-Schonpfad konservativer gezogen, Full-Check wieder gruen (2026-04-20 21:07)
---------------------------------------------------------------------------------------------

- `scripts/run_with_cpu_limit.py` nutzt im Auto-Modus jetzt nur noch `2` logische CPUs statt `4`; der Regressionstest `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py` zieht denselben konservativeren Default nach und isoliert den Default-Pfad gegen ein aeusseres `NVP_CPU_LIMIT`.
- Die verbliebenen Ruff-/Black-Reste in `scripts/run_text_rpg_product_gate.py`, `scripts/sync_docs_after_checks.py`, `scripts/update_workspace_tree_dirs.py` sowie den betroffenen Script-Tests sind bereinigt; der kleine Testblock fuer Wrapper, Produkt-Gate und Doku-Sync bleibt PASS.
- Der frische Full-Check `.tmp/results/reports/checks_report_20260420_210436.md` ist im expliziten 1-CPU-Schonmodus wieder vollstaendig PASS. Der separate Coverage-Lauf bleibt mit `672 passed` und `96.16%` PASS, `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty` endet weiter mit `summary=fail:0,warn:0`, und `novapolis-dev/docs/todo.dev.md` steht wieder bei `offen: 0`.

Sim-Arbeitsstand: 2026-06-13 09:19
---------------------------------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/agent_form_session_controller.gd` kapselt jetzt den verbliebenen Agent-Studio-Form-Session-State (`form_kind`, `form_mode_value`, `form_target_value`, `template_signature`, `form_controls`) in einem eigenen Controller statt in `Main.gd`.
- `novapolis-sim/scripts/Main.gd` delegiert fuer denselben Pfad jetzt Form-Oeffnen, Modus-/Zielwahl, Payload-/Persistenz-State und Form-UI-Refresh an diesen Controller; im Main-Script bleiben damit nur noch Orchestrierung, Payload-Dispatch und UI-Folgeaktionen.
- `get_errors` bleibt fuer beide GDScript-Dateien ohne Befund. Der kanonische Task `Checks: sim headless verify` endet im aktuellen Terminalkontext dagegen weiter mit Exitcode `2`, weil kein Godot-Binary aufloesbar ist (`GODOT_BIN` leer, `godot4`/`godot` nicht im PATH, keine lokale `*godot*.exe` gefunden); der Sim-Board-Punkt bleibt deshalb bewusst offen.

RP-Board-Abschluss: Metro-Warenueberblick auf belastbare Aggregationslogik verdichtet (2026-04-18 07:08)
------------------------------------------------------------------------------------------------------

- `novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md` aggregiert jetzt evidence-first nur die belegten D5/C6-Aufbaupfade, den Haendlerbund-Korridor `G7 <-> C6` sowie die T0-Bandbreiten der uebrigen externen Fraktionen. Neutrale Stationslager und Weltsummen bleiben im selben Lauf explizit `tbd`.
- `rp-metro-warenzuteilung-matrix-2026-03-27.md` und `rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` fuehren dieselbe Aggregationslogik fuer `Metro gesamt`; damit verweisen Matrix, Warenueberblick und Inventarpfade wieder auf denselben evidence-first Verdichtungsrahmen.
- `novapolis-dev/docs/todo.rp.md` schliesst damit den letzten offenen RP-Punkt, und `novapolis-dev/docs/todo.index.md` zieht den RP-Stand im selben Lauf auf `offen: 0` nach.

RP-Board-Abschluss: Externer Warenledger nur dort ueber Rahmenwert geschoben, wo echte Belegkette vorliegt (2026-04-18 06:52)
-----------------------------------------------------------------------------------------------------------------------

- `rp-metro-warenzuteilung-matrix-2026-03-27.md` und `rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` fuehren beim Haendlerbund jetzt den konkreten G7-<->-C6-Austauschkorridor mit `H-47`, aktiviertem Handelsstuetzpunkt `C6` und belegten Austauschklassen `Energie`, `technische Reparaturen`, `Kommunikationszugang` gegen `Nahrungsmittel`, `Filter` und `Grundbedarfsgueter` explizit mit.
- Arkologie-A1, Schienenbund, Eisenkonklave, Schattenbund und Fluesterkollektiv bleiben im selben Lauf bewusst auf Rahmenwert, weil weiter keine belastbaren Mengen-, Manifest- oder Stationsketten vorliegen; damit bleibt die externe Warenzuteilung evidence-first statt pauschal aufgeblasen.
- `novapolis-dev/docs/todo.rp.md` schliesst damit den vorletzten offenen RP-Punkt, und `novapolis-dev/docs/todo.index.md` zieht den RP-Stand im selben Lauf von `2` auf `1` offenen Punkt nach.

RP-Board-Abschluss: Verbrauchsdelta Tag 12 -> 13 konservativ zwischen D5-Quellseite und C6-Baustellenverbrauch gezogen (2026-04-18 06:44)
-----------------------------------------------------------------------------------------------------------------------------

- `novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`, `D5-inventar.md` und `C6-inventar.md` fuehren den Materialverbrauch Tag 12 -> 13 jetzt deckungsgleich als `C6-/Nordlinie-Baustellenverbrauch` bei D5-seitiger Quell-/Transferlast. Neue Mengen, Charges oder Restbestaende werden dabei nicht gesetzt; offen bleiben nur konkrete D5-Abbuchungen und C6-Lagerbuchungen.
- `rp-metro-warenzuteilung-matrix-2026-03-27.md` und `rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` ziehen dieselbe konservative Standortlesart fuer den laufenden Produktpfad nach, statt das Delta weiter pauschal als fraktionsweit ungesplittet stehen zu lassen.
- `novapolis-dev/docs/todo.rp.md` schliesst damit den naechsten offenen RP-Punkt, und `novapolis-dev/docs/todo.index.md` zieht den RP-Stand im selben Lauf von `3` auf `2` offene Punkte nach.

RP-Board-Abschluss: D5->C6-Transferkette im Warenledger explizit auf den belegten Prozessrahmen gezogen (2026-04-18 06:37)
-----------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-metro-warenzuteilung-arbeitsledger-2026-03-30.md` fuehrt den D5->C6-Lauf jetzt nicht mehr als offenen `tbd`-Belegpfad, sondern als explizite Prozesskette mit Quelle `D5-Materiallager unter dem Bahnsteig und/oder Werkstattbestand`, D5-seitigem `Entnahme/Packen -> Abmeldung`, `manuellerTransport` mit `Tragegestell(ReflexAssist)` sowie C6-seitigem `Eintreffen -> Bestandsaufnahme -> Empfangsbestaetigung -> Baustellenverteilung`.
- `rp-metro-warenzuteilung-matrix-2026-03-27.md`, `Missionslog-Novapolis.md`, `D5-inventar.md`, `C6-inventar.md` und `Novapolis-inventar.md` fuehren damit denselben konservativen Belegrahmen; offen bleiben weiter nur Mengen, Charge und die genaue Zielbuchung in C6 statt stiller Mengenpromotion.
- `novapolis-dev/docs/todo.rp.md` schliesst damit den aeltesten offenen RP-Punkt, und `novapolis-dev/docs/todo.index.md` zieht den RP-Stand im selben Lauf von `4` auf `3` offene Punkte nach.

RP-Board-Abschluss: Folgekorridor slot 41-45 unter demselben Slice-2-Handover-Vertrag ausgebaut (2026-04-18 06:32)
-----------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-41-45.ssot.md` fuehrt jetzt den sechsten Kampagnenblock hinter `slot 40` evidence-first auf demselben Resume-, Reveal- und Artefaktrahmen fort. Der neue Folgeblock bleibt auf `D5`, `C6`, `G7`, `E2` und `F1` begrenzt und setzt hinter `slot 45` wieder nur einen klaren adapterfaehigen Anschluss statt freier Weltverbreiterung.
- `novapolis-dev/docs/process/rp-folgekorridor-slot-36-40.ssot.md`, `text-rpg-slice-2-handover-v1.ssot.md` und `text-rpg-product-gate-v1.ssot.md` zeigen im selben Lauf auf denselben neuen Folgepfad; damit bleiben RP-, Handover- und Product-Gate-Quellen fuer den Ausbau hinter `slot 40` wieder deckungsgleich.
- `novapolis-dev/docs/todo.rp.md` schliesst damit den aeltesten offenen RP-Punkt; `novapolis-dev/docs/todo.index.md` zieht den RP-Stand im selben Lauf von `5` auf `4` offene Punkte nach.

Commit-Preflight: Root-/Dev-Dokus vor dem Commit erneut auf frisches Snapshot-Fenster gezogen (2026-04-18 02:58)
----------------------------------------------------------------------------------------------------------------

- Vor dem Commit wird nur der bereits belegte Root-/Dev-Dokuscope auf einen frischen Snapshot-Lock nachgezogen; der sachliche Inhalt des geschlossenen Dev-Blocks bleibt unveraendert.
- `scripts/sync_docs_after_checks.py` aktualisiert dazu die `stand`-/`checks`-Frontmatter der bereits geaenderten Root- und Dev-Markdownpfade erneut gegen denselben Gruenlauf `.tmp/results/reports/checks_report_20260417_071110.md`.
- `README.md`, `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/active-surface-index.md`, `novapolis-dev/docs/todo.dev.md`, `novapolis-dev/docs/todo.index.md` und diese Dev-DONELOG-Datei fuehren danach wieder denselben Snapshot-Zeitpunkt im Commit-Pfad.

Doku-Sync-Helfer: Snapshot-, Frontmatter- und TODO-Index-Nachzug nach Gruenlaeufen gebuendelt (2026-04-18 02:09)
---------------------------------------------------------------------------------------------------------------

- `scripts/sync_docs_after_checks.py` fuehrt einen kleinen, separaten Nachzugspfad fuer geaenderte Root-/Dev-Markdowndateien ein: Der Helfer loest `--report latest` oder einen konkreten Reportpfad auf, prueft standardmaessig auf `overall=PASS`, schreibt einen frischen Snapshot-Lock und spiegelt danach denselben `run_checks_and_report.py`-Headline plus `snapshot-lock PASS (...)` in die betroffenen `stand`-/`checks`-Frontmatter.
- Sobald aktive TODO-Boards im Sync-Scope liegen, ruft der Helfer `scripts/check_todo_index_sync.py --write-index-meta` auf und zieht `novapolis-dev/docs/todo.index.md` im selben Lauf nach; damit bleiben Board-Count, aeltester offener Punkt und Frontmatter nicht mehr haeufig als manuelle Restarbeit liegen.
- `.vscode/tasks.json` fuehrt dazu den Task `Docs: sync after checks`, damit derselbe Pfad nach einem belegten Gruenlauf ohne Terminal-Sonderweg erreichbar bleibt.
- `novapolis_agent/tests/scripts/test_sync_docs_after_checks.py` deckt Frontmatter-Sync, Latest-Report-Aufloesung und den TODO-Index-Hook gezielt ab; im Dev-Board bleiben damit keine offenen Steuerpunkte mehr.

Agent-Board-Abschluss: gm_session-Hard-Fail diagnostisch frueher und klarer getrennt (2026-04-18 06:08)
-----------------------------------------------------------------------------------------------------------

- `scripts/run_text_rpg_product_gate.py` fuehrt jetzt einen separaten `--gm-preflight-only`-Pfad und dieselbe explizite `GM Diagnosis` im Produkt-Gate-Report. Damit werden `preflight`, `eval` und `summary` sowie `runtime_unreachable`, `model_missing` und spaetere inhaltliche Blocker nicht mehr nur indirekt ueber Fehlerlisten, sondern als klarer Diagnosepfad mit naechstem Schritt ausgewiesen.
- `.vscode/tasks.json` fuehrt dazu den leichten Task `Checks: gm runtime preflight`; `novapolis_agent/docs/runbook.md` zieht denselben Vorpruefpfad vor dem teuren Gesamtgate und die neue Diagnose-Lesart im Report nach.
- `novapolis_agent/tests/scripts/test_run_text_rpg_product_gate.py` deckt die neue Vorpruefungs- und Diagnose-Aufteilung gezielt ab; der fokussierte Pytest-Lauf bleibt PASS, und im Agent-Board sinkt der offene Stand damit von `1` auf `0`.

Agent-Board-Abschluss: map_reduce_summary-Rest ueber Edge-Tests geschlossen (2026-04-18 04:49)
--------------------------------------------------------------------------------------------------

- `novapolis_agent/tests/scripts/test_map_reduce_summary_edges.py` deckt jetzt gezielt die verbliebenen `safe_read()`- und Python-Parse-Fallbacks, den markdownfreien Rohtext, JSON-/JSONL-Fehler- und Skalarpfade, die Skip-/Exception-Zweige in `walk_scope()` sowie den Fehler- und `__main__`-Pfad von `main()` ab.
- Der fokussierte Testblock `pytest -q novapolis_agent/tests/scripts/test_map_reduce_summary_heuristic_min.py novapolis_agent/tests/scripts/test_map_reduce_summary_json_modes.py novapolis_agent/tests/scripts/test_map_reduce_summary_markdown_and_excludes.py novapolis_agent/tests/scripts/test_map_reduce_summary_python_and_json.py novapolis_agent/tests/scripts/test_map_reduce_summary_edges.py novapolis_agent/tests/test_map_reduce_summary_smoke_minimal.py novapolis_agent/tests/test_map_reduce_summary_scripts_smoke.py` bleibt komplett PASS, und die Nachmessung `--cov=scripts.map_reduce_summary --cov-report=term-missing` zieht den Runner von `89%` auf `100%` Coverage.
- Der bestehende CLI- und Artefaktvertrag des Summary-Runners bleibt dabei unveraendert; im Agent-Board sinkt der offene Stand damit von `2` auf `1`.

Agent-Board-Abschluss: Support-A/B-Smoke auf klare Fehlerklassen und belastbare Tests gezogen (2026-04-18 03:28)
-----------------------------------------------------------------------------------------------------------------

- `novapolis_agent/scripts/support_ab_smoke.py` gibt fuer denselben `/chat`-Smoke jetzt immer einen strukturierten JSON-Block mit `status` aus und trennt Nicht-200-Antworten, Payload-/Contract-Drift und Netzwerkfehler explizit in `http_error`, `payload_error` und `network_error`.
- `novapolis_agent/tests/scripts/test_support_ab_smoke.py` deckt jetzt Happy Path, non-JSON, invalides JSON-Objekt, HTTP-Detailfehler, fehlende Modell-/Content-Felder, Runtime-Parsefehler, Netzwerkfehler, Argumentparser und `main()` gezielt ab; der frische Pytest-Lauf ist PASS, und die fokussierte Nachmessung hebt `scripts.support_ab_smoke` von `47%` auf `91%` Coverage.
- `novapolis_agent/docs/runbook.md` fuehrt dieselbe Erfolgs-/Fehlersprache fuer den Support-A/B-Smoke jetzt explizit mit; im Agent-Board sinkt der offene Stand damit von `5` auf `4`.

Agent-Board-Abschluss: Referenzrunner-Rest ueber Sammelreport- und Multi-Spec-Tests geschlossen (2026-04-18 03:40)
-------------------------------------------------------------------------------------------------------------------

- `novapolis_agent/tests/scripts/test_run_text_rpg_reference_session_edges.py` deckt jetzt gezielt die verbleibenden Sammelreport-Zweige in `_build_markdown()` mit und ohne Fehlerliste, die Fehleraggregation in `run_reference_sessions()` sowie den Multi-Spec-CLI-Pfad in `main()` inklusive `case_count`-Ausgabe und Reportschreiben ab.
- Der fokussierte Testblock `pytest -q novapolis_agent/tests/scripts/test_run_text_rpg_reference_session.py novapolis_agent/tests/scripts/test_run_text_rpg_reference_session_edges.py` bleibt PASS, und die Nachmessung `--cov=scripts.run_text_rpg_reference_session --cov-report=term-missing` zieht den Runner von `90%` auf `100%` Coverage.
- Der bestehende Referenz- und Artefaktvertrag fuer die deterministischen Faelle hinter `slot 05` und `slot 40` bleibt dabei unveraendert; im Agent-Board sinkt der offene Stand damit von `4` auf `3`.

Agent-Board-Arbeitsstand: 2026-06-13 09:19
----------------------------------------------------------------------------------------------------------------

- Der naechste offene Agent-Punkt ist evidence-first auf den heutigen Restzweig von `novapolis_agent/scripts/export_finetune.py` eingegrenzt.
- Der fokussierte Testblock ueber Export-, Fallback- und Prepare-Integration ist derzeit nur an einer fragilen `app.core.settings`-Importannahme in `novapolis_agent/tests/scripts/test_export_finetune_more_edges.py` rot und misst fuer `scripts.export_finetune` aktuell `85%` Coverage.
- Offen bleiben laut Nachmessung vor allem `_load_run_eval_module()`-Fehlerzweig, Guard-/Dedup-Zweige in `_resolve_existing_inputs()` und `_collect_export_pairs()`, der doppelte Settings-/Default-Fallback in `export_from_results()`, der `unknown format`-Guard, der breite Dataset-Fallback in `inspect_results_for_export()` sowie der direkte CLI-Block unter `__main__`.

Agent-Board-Abschluss: export_finetune-Rest ueber Fallback- und CLI-Tests geschlossen (2026-04-18 04:09)
----------------------------------------------------------------------------------------------------------------

- `novapolis_agent/tests/scripts/test_export_finetune_more_edges.py` deckt jetzt die verbleibenden Settings-Fallbacks ueber den zweiten Importpfad und den finalen `run_eval`-Default, Helper-/Dedup-Skip-Pfade, den breiten Dataset-Fallback in `inspect_results_for_export()`, den `unknown format`-Guard sowie den direkten CLI-Block unter `__main__` gezielt ab.
- Der fokussierte Export-Testblock ueber Export-, Fallback- und Prepare-Integration ist jetzt vollstaendig PASS, und die Nachmessung `--cov=scripts.export_finetune --cov-report=term-missing` zieht `scripts.export_finetune` von `85%` auf `100%` Coverage.
- Der bestehende Export- und Prepare-Pack-Vertrag bleibt dabei unveraendert; im Agent-Board sinkt der offene Stand damit von `3` auf `2`.

Agent-Board-Arbeitsstand: 2026-06-13 09:19
--------------------------------------------------------------------------------------------------------------------

- Der naechste offene Agent-Punkt ist evidence-first auf den heutigen Restzweig von `novapolis_agent/scripts/map_reduce_summary.py` eingegrenzt.
- Der fokussierte Testblock fuer Heuristik-, JSON-, Markdown-, Python- und Smoke-Pfade ist grün, misst fuer `scripts.map_reduce_summary` aktuell aber nur `89%` Coverage.
- Offen bleiben laut Nachmessung vor allem `safe_read()`-Fallbacks, der Parse-Fallback in `summarize_python()`, der markdownfreie Textpfad in `summarize_markdown()`, JSON-/JSONL-Fehler- und Simplify-Zweige in `summarize_json()`, die Skip-/Exception-Pfade in `walk_scope()`, der Verzeichnis-Write-Pfad in `write_md()` sowie der Fehler- und `__main__`-Pfad von `main()`.

Workspace-Tree-Split: aktive Reader-Surface gegen forensischen Vollbaum getrennt (2026-04-18 01:45)
-------------------------------------------------------------------------------------------------

- `scripts/update_workspace_tree_dirs.py` erzeugt jetzt drei klar getrennte Artefakte: `workspace_tree.txt` als aktiven Reader-Baum, `workspace_tree_dirs.txt` als aktive Verzeichnis-Summary und `workspace_tree_full.txt` als forensischen Vollbaum.
- Die aktive Filterlogik blendet lokale Artefaktpfade wie `.tmp`, `.venv*`, `eval/results`, `novapolis-dev/logs`, `novapolis-sim/.godot`, `outputs`, `Backups` sowie die grossen Archive-/Raw-/Curated-Surfaces bewusst aus, damit die Reader-Surface nicht weiter von Maschinen- und Auditmassen dominiert wird.
- `.vscode/tasks.json`, `README.md`, `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` fuehren dieselbe Zweiteilung jetzt explizit mit; im Dev-Board bleibt nach diesem Nachzug nur noch der Doku-Sync-Helfer offen.
- Der technische Referenzstand bleibt der letzte kanonische Gruenlauf `.tmp/results/reports/checks_report_20260417_071110.md`.

Active-Surface-Nachzug: Referenzzeilen auf belegten April-Stand und Wildcard-Logik gezogen (2026-04-18 01:21)
-------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/active-surface-index.md` fuehrt die bislang auf `2026-03-04` stehenden Referenzzeilen jetzt mit belegtem April-Pruefstand fuer die weiterhin aktiven Einzelquellen `index.md`, `naming-policy.md`, `tests.md`, `dataset-provenance.md`, `copilot-vscode-usage.md`, `readme_decisions.md`, `readme.hub.md` und `architecture-summary-local-ai.md`.
- Die Gruppenpfade `specs/**` und `meta/**` bleiben REFERENCE, sind aber jetzt als manuell gepruefte Sammelwerte markiert; zusaetzlich benennt der Pflege-Block explizit, dass `scripts/check_doc_freshness.py` nur konkrete Dateizeilen bewertet und Wildcards bewusst ueberspringt.
- `novapolis-dev/docs/todo.dev.md` markiert den offenen Dev-Punkt damit als geschlossen, weil Active-Surface-Index, Freshness-Logik und Reader-Surface fuer diesen Referenzscope nicht mehr gegeneinander laufen.
- Im Dev-Board bleiben nach diesem Nachzug nur noch zwei offene Steuerpunkte; der technische Referenzstand bleibt der letzte kanonische Gruenlauf `.tmp/results/reports/checks_report_20260417_071110.md`.

Workspace-Index-Nachzug: Landing-Surface fuer Root und Hauptmodule vor den Agent-Katalog gezogen (2026-04-18 01:03)
---------------------------------------------------------------------------------------------------------------

- `WORKSPACE_INDEX.md` startet jetzt mit einer echten Workspace-Landing-Surface fuer Root, Dev, Agent, RP und Sim statt direkt mit dem agent-lastigen Tiefenkatalog.
- Der bisherige Detailpfad bleibt im selben Dokument als `Referenzkatalog Agent-Verzeichnis` erhalten; damit bleibt die Agent-Tiefe erreichbar, dominiert aber nicht mehr die erste Orientierung.
- `novapolis-dev/README.md`, `WORKSPACE_STATUS.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` fuehren damit wieder denselben Navigationsrahmen fuer Root plus die vier Hauptmodule.
- Im Dev-Board bleiben nach diesem Reader-Surface-Nachzug nur noch drei offene Steuerpunkte; der technische Referenzstand bleibt der letzte kanonische Gruenlauf `.tmp/results/reports/checks_report_20260417_071110.md`.

Workspace-Tree-Nachzug: Taskpfad und Statusclaim wieder auf denselben Iststand gezogen (2026-04-18 00:59)
-----------------------------------------------------------------------------------------------------------

- Die VS-Code-Tasks `Workspace tree: full`, `Workspace tree: directories` und `Workspace tree: summary (dirs)` laufen lokal wieder belegbar ueber den aktuellen Taskpfad; der kanonische Pfad fuehrt jetzt ueber `scripts/update_workspace_tree_dirs.py` mit den Modi `forensic-full`, `active-tree` und `active-dirs`.
- `novapolis-dev/docs/todo.dev.md` markiert den offenen Dev-Punkt damit als geschlossen, weil `.vscode/tasks.json`, `WORKSPACE_STATUS.md` und diese Dev-DONELOG-Datei fuer den aktuellen Iststand nicht mehr gegeneinander laufen.
- Der fruehere Claim, `Workspace tree:*` haenge lokal weiter am alten `pwsh /d /c`-Launcherfehler, bleibt fuer den aktuellen Taskpfad nicht mehr stehen; historische Altlaeufe behalten ihre damalige Evidenz, werden aber nicht mehr als aktueller Restfortschritt fortgeschrieben.
- `novapolis-dev/docs/todo.index.md` fuehrt Dev damit nur noch mit vier offenen Folgepunkten; der technische Referenzstand bleibt der letzte kanonische Gruenlauf `.tmp/results/reports/checks_report_20260417_071110.md`.


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

Root-Archivschnitt: Abgeschlossenen April-Block ins Root-Archiv uebernommen und Live-Datei zurueckgesetzt (2026-04-18 00:49)
--------------------------------------------------------------------------------------------------------------------------

- `novapolis-dev/archive/todo.root.archive.md` fuehrt jetzt den vollstaendig abgeschlossenen April-Block mit Recovery-, Warnsignal-, Handover-, Release- und Hygiene-Nachzug als eigenen Archivabschnitt.
- `todo.root.md` ist im selben Lauf wieder als schlanke Live-Arbeitsvorlage ohne offene suiteweite Punkte vorbereitet, statt den bereits erledigten Block weiter auf der aktiven Root-Oberflaeche zu tragen.
- `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` spiegeln denselben Archivstand nach; die Modul-Boards bleiben unveraendert bei `Dev=5`, `RP=5`, `Agent=5` und `Sim=5`.
- Der aktuelle Doku-Lauf bleibt auf Snapshot-, Markdownlint-, Frontmatter- und TODO-Index-Gate begrenzt; der Technikreferenzstand bleibt `.tmp/results/reports/checks_report_20260417_071110.md`.

Hygiene-Cadence-Nachzug: April-Root-Takt fuer KPI- und Boardpflege wieder aktiv verankert (2026-04-17 23:59)
----------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/abschluss-routine.ssot.md` bleibt die kanonische Vorlage fuer den 60-Minuten-Hygiene-Slot mit Drift-Scan, Donelog-Cleanup und TODO/Index-Abgleich.
- `todo.root.md` fuehrt nach dem Nachzug keinen offenen suiteweiten Punkt mehr; `novapolis-dev/docs/todo.index.md` spiegelt dazu weiter unveraenderte Modul-Open-Counts `Dev=5`, `RP=5`, `Agent=5` und `Sim=5`, waehrend Root ausserhalb dieser Summe bleibt.
- `WORKSPACE_STATUS.md` und `DONELOG.md` fuehren denselben April-Rahmen jetzt sichtbar mit den KPI-Feldern `todo_index_drift`, `active_docs_stale`, `placeholder_conflicts` und `logs_policy_violations`, statt den letzten grünen Hygiene-Schnitt nur historisch auf 2026-04-08 stehen zu lassen.
- Der sachliche Technikreferenzstand bleibt der letzte kanonische Gruenlauf `.tmp/results/reports/checks_report_20260417_071110.md`; der aktuelle Doku-Nachzug bleibt auf Snapshot-, Markdownlint-, Frontmatter- und TODO-Index-Gate begrenzt.

Handover- und Release-Nachzug: Root-Kurzformel und Freigabeklammer fuer den ersten Vertikalslice geschlossen (2026-04-17 23:22)
--------------------------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/text-rpg-pre-rp-product-model-v1.ssot.md`, `text-rpg-slice-2-handover-v1.ssot.md` und `rp-folgekorridor-slot-31-35.ssot.md` fuehren jetzt dieselbe player-facing Kurzformel `Weiter im selben Lauf: offener Druck, offene Aufgaben, klarer naechster Zug.` fuer den ersten aktiven Anschluss hinter `slot 30`.
- Die neue SSOT `novapolis-dev/docs/process/text-rpg-release-evidence-bundle-v1.ssot.md` bindet `Checks: full`, `Checks: text-rpg product gate`, `Tests: text-rpg reference session`, den Sim-Export-Smoke und die Release-Protokollierung in `WORKSPACE_STATUS.md`, `novapolis-dev/docs/donelog.md` und `DONELOG.md` zu einer aktiven Freigabekette zusammen.
- `README.md`, `novapolis_agent/docs/runbook.md`, `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` und `novapolis-dev/docs/process/sim-export-release-path.ssot.md` zeigen jetzt auf denselben Bundle-Pfad statt nur auf getrennte Teilbelege.
- `todo.root.md` markiert beide suiteweiten Root-Punkte als geschlossen, `novapolis-dev/docs/todo.index.md` fuehrt Root danach nur noch mit einem offenen Querschnittspunkt weiter.

Warnsignal-Nachzug: Root-Produktsprache fuer stille Hintergrundlage, Knappheit, Warnung und Ueberzug geschlossen (2026-04-17 22:51)
------------------------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/text-rpg-pre-rp-product-model-v1.ssot.md` fuehrt jetzt die kanonische Viererlesart `stille Hintergrundlage`, `Knappheit`, `Warnung` und `Ueberzug` als Pflichtmatrix fuer den ersten Vertikalslice.
- `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` zieht dieselbe Matrix auf die Hub-Zonen `Topband`, `Stage`, `Ops-Spalte` und `Telemetrieband`; `novapolis-sim/README.md` fuehrt dieselbe IA-Lesart fuer den produktiven Hub nach.
- `todo.root.md` markiert den suiteweiten Root-Punkt als geschlossen, `novapolis-dev/docs/todo.index.md` fuehrt Root danach mit noch drei offenen Querschnittspunkten weiter.
- Der sachliche Checkreferenzstand bleibt der letzte kanonische Gruenlauf `.tmp/results/reports/checks_report_20260417_071110.md`; der Doku-Nachzug selbst bleibt auf Snapshot-, Markdownlint- und Frontmatter-Gate begrenzt.

Recovery-Nachzug: Root-Produktsprache fuer teilmoeglich, verschoben und blockiert geschlossen (2026-04-17 22:36)
----------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/text-rpg-turn-budget-model-v1.ssot.md` fuehrt jetzt die drei kanonischen Recovery-Klassen `teilmoeglich`, `verschoben` und `blockiert` als player-facing Lesart der Budgetklassen `slightly_over`, `significantly_over` und `blocked`.
- `novapolis-dev/docs/process/text-rpg-pre-rp-product-model-v1.ssot.md`, `text-rpg-product-gate-v1.ssot.md`, `novapolis_agent/docs/runbook.md` und `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` ziehen dieselbe Lesart im selben Lauf nach; damit driftet der erste Vertikalslice nicht mehr zwischen Produktmodell, Gate, Agent und UI.
- `todo.root.md` markiert den suiteweiten Root-Punkt als geschlossen, `novapolis-dev/docs/todo.index.md` fuehrt Root danach mit noch vier offenen Querschnittspunkten weiter.
- Der sachliche Checkreferenzstand bleibt der letzte kanonische Gruenlauf `.tmp/results/reports/checks_report_20260417_071110.md`; der Doku-Nachzug selbst bleibt auf Snapshot-, Markdownlint- und Frontmatter-Gate begrenzt.

Board-Refill: Root und Live-Boards wieder auf je fuenf Punkte gezogen (2026-04-17 06:37)
----------------------------------------------------------------------------------------

- `todo.root.md` sowie `novapolis-dev/docs/todo.dev.md`, `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.rp.md` und `novapolis-dev/docs/todo.sim.md` fuehren nach dem erneuten Workspace-Scan wieder je fuenf aktive Folgepunkte statt leerer Live-Oberflaechen.
- `novapolis-dev/docs/todo.index.md` synchronisiert die Modulzaehlung jetzt auf `Dev=5`, `RP=5`, `Agent=5` und `Sim=5`; Root bleibt bewusst ausserhalb dieser Counts.
- Die neuen Punkte bleiben an aktuelle Evidenz gebunden: Dev fokussiert Workspace-/Reader-Surface-/Sync-Themen, Agent fokussiert Coverage- und Runtime-Reste, RP fokussiert den Korridor hinter `slot 40`, und Sim fokussiert Export-, Persistenz- und Architekturrest.
- Der kanonische Sammellauf `.tmp/results/reports/checks_report_20260417_063849.md` ist dazu vollstaendig PASS; die Board-Dateien sind nach der Tab-Korrektur in `todo.root.md` wieder markdownlint-sauber.

Semantik-Nachzug II: Logsprache, Reader-Surface-Abgrenzung und Tie-Break-Fallback geschlossen (2026-04-17 06:04)
----------------------------------------------------------------------------------------------------------------

- `WORKSPACE_INDEX.md` beschreibt lokale/private Artefaktklassen jetzt nur noch als Klassenhinweise; direkte Reader-Links auf diese Einzelpfade sind aus der aktiven Surface entfernt.
- `novapolis_agent/README.md` fuehrt die Root-`.venv` jetzt robust als Python-3.12.x-Referenz mit zuletzt dokumentiertem Gruenlauf 3.12.10, statt die operative Baseline patch-genau zu verengen.
- `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt jetzt zusaetzlich den Gleichstandsfall gleicher heuristischer Scores plus unbrauchbarer Judge-Antwort ab; der Dauer-Tie-Break bleibt dabei stabil auf dem vorgerankten Gewinner.
- Der kanonische Sammellauf `.tmp/results/reports/checks_report_20260417_060413.md` ist dazu vollstaendig PASS; `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` stehen wieder bei `offen: 0`.

Semantik-Nachzug: Reader-Surface, Runtime-Doku und Support-A-B-Fallback konsistent geschlossen (2026-04-17 05:55)
-------------------------------------------------------------------------------------------------------------

- `novapolis_agent/README.md` fuehrt jetzt den belegten Root-Interpreter als reproduzierbaren Python-3.12.x-Referenzpfad mit zuletzt dokumentiertem Gruenlauf 3.12.10 und trennt Standard-Chat, Support-A-B und Judge in einer operativen Profilmatrix.
- `WORKSPACE_INDEX.md` priorisiert wieder aktive Navigation und kapselt private oder generierte Artefaktklassen hinter einer eigenen Reader-Surface-Grenze, statt sie als gleichrangige Einzelnavigation zu fuehren.
- `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt jetzt den Fallback ab, falls ein gesetzter Support-A-B-Judge keine verwertbare Antwort `A|B` liefert und der heuristische Gewinner bestehen bleiben muss.
- Der kanonische Sammellauf `.tmp/results/reports/checks_report_20260417_055543.md` ist dazu vollstaendig PASS; `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` stehen wieder bei `offen: 0`.

Ruff-/Black-Nachzug: Python-Stildrift in Agent- und Root-Skripten wieder auf PASS gezogen (2026-04-17 05:30)
----------------------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/chat.py`, `novapolis_agent/scripts/run_eval.py`, `novapolis_agent/scripts/support_ab_smoke.py`, mehrere betroffene Agent-Tests sowie `scripts/run_sim_headless_verify.py` fuehren wieder denselben repoweiten Stilrahmen ohne die zuvor gemeldeten E501-, I001- und EOF-Drifts.
- Der gezielte Testscope fuer Chat-, Sim- und Script-Pfade ist PASS; `ruff check novapolis_agent scripts` und `black --check novapolis_agent scripts` sind ebenfalls PASS.
- Der damals gezogene kanonische Sammellauf `.tmp/results/reports/checks_report_20260417_053609.md` endet dadurch wieder vollstaendig mit `overall=PASS`, und `novapolis-dev/docs/todo.dev.md` plus `novapolis-dev/docs/todo.index.md` stehen erneut bei `offen: 0`.

Commit-Preflight: Aktive Reader-Doku vor dem Main-Push auf frischen Snapshot-Stand gezogen (2026-04-17 05:18)
-----------------------------------------------------------------------------------------------------------

- `DONELOG.md`, `WORKSPACE_STATUS.md` und diese Dev-DONELOG-Datei fuehren vor dem Push auf `main` wieder denselben Snapshot-Zeitpunkt wie `.snapshot.now`.
- Die bereits aktualisierten `workspace_tree*.txt`-Artefakte sowie die Wrapper-/Test-Aenderungen bleiben der sachliche Inhalt des Laufs; der Doku-Nachzug zieht nur den Gate-Zeitwert und den belegten Commit-Preflight nach.
- Der vorbereitende Fokus-Testscope fuer die neuen Agent-Wrapper-Checks bleibt vor dem Commit gruen.

Workspace-Trees: Root-Strukturartefakte und aktive Reader-Doku erneut auf Iststand gezogen (2026-04-17 04:44)
----------------------------------------------------------------------------------------------------------

- `workspace_tree.txt`, `workspace_tree_dirs.txt` und `workspace_tree_full.txt` sind erneut direkt aus dem aktuellen Repo-Stand erzeugt und spiegeln jetzt auch die aktuellen `.tmp`-Referenz-/Reportpfade sowie die lokale Venv-/Cache-Oberflaeche.
- Der anschliessende aktive Freshness-Lauf bleibt mit `checked_docs=14` und `findings=0` PASS; es war kein weiterer Stale-Docs-Nachzug noetig.
- Fuer den damaligen Lauf erfolgte der Refresh direkt per Terminal plus `scripts/update_workspace_tree_dirs.py`; der aktuell wieder belegte Taskpfad ist separat im Eintrag vom 2026-04-18 00:59 dokumentiert.

Root-Konsistenznachzug: Aktive TODO-Uebersicht auf den aktuellen Index-Stand gezogen (2026-04-17 04:33)
-----------------------------------------------------------------------------------------------------

- `todo.root.md` fuehrt im Kurzstatus jetzt wieder denselben Modulstand `Dev=0`, `RP=0`, `Agent=0`, `Sim=0` wie `novapolis-dev/docs/todo.index.md`.
- Der Lauf aendert keine offenen Boards und keinen Produktstand, sondern korrigiert nur die veraltete Root-Kurzzeile auf den bereits belegten Iststand.

Board-Archivierung: Letzten Sim-Abschluss in das Modularchiv uebernommen (2026-04-17 04:27)
--------------------------------------------------------------------------------------------

- `novapolis-dev/archive/todo.sim.archive.md` fuehrt jetzt den zuletzt geschlossenen Sim-Abschlussschnitt vom 2026-04-17 als Archivabschnitt mit `archived_at`.
- `novapolis-dev/docs/todo.sim.md` ist im selben Lauf wieder als schlanke Live-Oberflaeche fuer neue Sim-Punkte vorbereitet und fuehrt aktuell keine offenen Sim-Punkte.
- `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` spiegeln denselben Board-Archivstand weiter mit `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`.

Sim Cleanup: Main.gd-Altlasten entfernt und kanonischen Godot-CLI-Smoke geschlossen (2026-04-17 04:24)
-----------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` fuehrt die doppelten lokalen Finetune-Helfer nicht mehr; die Runtime-Verantwortung bleibt im bestehenden `agent_runtime_controller.gd`.
- `scripts/run_sim_headless_verify.py` und der neue Task `Checks: sim headless verify` fuehren jetzt denselben kanonischen Headless-Smoke fuer `res://scripts/verify_sim.gd`; `novapolis-sim/README.md` sowie die Sim-SSOTs sind auf denselben Pfad nachgezogen.
- `novapolis-sim/scripts/verify_sim.gd` gibt die instanzierte Main-Scene nach der Pruefung wieder frei; der echte Lauf gegen Godot 4.6.1 endet damit bei `SIM_VERIFY: OK` und `EXITCODE=0` ohne die zuvor sichtbaren Exit-Leaks.

Board-Archivierung: Letzten Agent-Abschluss in das Modularchiv uebernommen (2026-04-17 04:15)
-----------------------------------------------------------------------------------------------

- `novapolis-dev/archive/todo.agent.archive.md` fuehrt jetzt den zuletzt geschlossenen Agent-Handover-Block vom 2026-04-17 als Archivabschnitt mit `archived_at`.
- `novapolis-dev/docs/todo.agent-board.md` ist im selben Lauf wieder als schlanke Live-Oberflaeche fuer neue Agent-Punkte vorbereitet und fuehrt aktuell keine offenen Agent-Punkte.
- `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` spiegeln denselben Board-Archivstand weiter mit `Agent=0`, `Sim=2`.

Agent Gate: Zweiten Handover-Referenzfall hinter slot 30 im Standardlauf materialisiert (2026-04-17 04:00)
-----------------------------------------------------------------------------------------------------------

- `novapolis_agent/eval/config/text_rpg_reference_session_handover_slot31_40.v1.json` fuehrt jetzt den zweiten deterministischen Folgefall hinter `slot 30` bis `slot 40` auf demselben Session- und Artefaktvertrag.
- `novapolis_agent/scripts/run_text_rpg_reference_session.py`, `scripts/run_text_rpg_product_gate.py` und `.vscode/tasks.json` ziehen Basis- und Handover-Fall jetzt im selben Schritt `Tests: text-rpg reference session` bzw. im selben Gate-Standardlauf.
- `novapolis_agent/docs/runbook.md`, `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`, `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`, `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.index.md`, `todo.root.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` sind im selben Lauf auf denselben Abschlussstand nachgezogen; offen bleibt damit nur noch Sim.

Board-Archivierung: Letzte Dev- und RP-Abschluesse in die Modularchive uebernommen (2026-04-17 02:54)
------------------------------------------------------------------------------------------------------

- `novapolis-dev/archive/todo.dev.archive.md` fuehrt jetzt den zuletzt geschlossenen Dev-Steuerpunkt fuer Active-Surface-Index und Workspace-Reader-Surface als archivierten Abschnitt mit `archived_at`.
- `novapolis-dev/archive/todo.rp.archive.md` fuehrt jetzt den zuletzt geschlossenen RP-Folgeblock `slot 36-40` als archivierten Abschnitt mit `archived_at`.
- `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.rp.md` sind im selben Lauf wieder als schlanke Live-Oberflaechen fuer neue Punkte vorbereitet; `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` spiegeln denselben Stand.

RP Folgeblock: Slot 36-40 unter demselben Slice-2-Handover-Vertrag ausgearbeitet (2026-04-17 02:44)
------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-36-40.ssot.md` fuehrt jetzt die fuenfte Kampagnenstufe hinter `slot 35` aus und haelt `resume_checkpoint_id`, Carry-Over-Arbeiten und offenen Restdruck ueber `D5`, `C6`, `G7`, `E2` und `F1` lesbar.
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` und `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` benennen im selben Lauf denselben neuen Anschluss statt weiter bei `slot 31-35` zu enden.
- `novapolis-dev/docs/todo.rp.md`, `novapolis-dev/docs/todo.index.md`, `todo.root.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` sind im selben Lauf auf denselben RP-Abschlussstand nachgezogen; das RP-Board steht damit wieder bei `offen: 0`.

Dev Reader Surface: Active-Surface-Index und Workspace-Index gegen den April-Iststand gehaertet (2026-04-17 02:44)
--------------------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/active-surface-index.md` fuehrt fuer `donelog.md`, `todo.index.md`, `todo.dev.md`, `todo.rp.md`, `todo.agent-board.md`, `todo.sim.md` sowie `process/**` jetzt belastbare April-Pruefstaende statt des alten Maerz-Drifts.
- `WORKSPACE_INDEX.md` fuehrt den dokumentierten Phase-2-Konsistenzlauf nicht mehr als Dauerclaim `Phase 2 aktiv`, sondern als abgeschlossenen Prozessanker mit inkrementeller Pflege ueber Boards, DONELOG und Status-Sync.
- `novapolis-dev/docs/todo.dev.md`, `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` sind im selben Lauf auf diesen neuen Reader-Surface-Stand nachgezogen; das Dev-Board steht damit wieder bei `offen: 0`.

Root Archive: Abgeschlossenen Root-Backlog archiviert und aktive Root-TODO zurueckgesetzt (2026-04-17 02:39)
-------------------------------------------------------------------------------------------------------------

- `novapolis-dev/archive/todo.root.archive.md` fuehrt jetzt den abgeschlossenen Root-Block vom 2026-04-17 als neuen Archivabschnitt.
- `todo.root.md` ist wieder eine leere Arbeitsvorlage fuer neue suiteweite Punkte; offene Folgearbeit bleibt nur in den Modul-Boards.
- `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md` und `DONELOG.md` sind im selben Lauf auf denselben Root-Zustand nachgezogen.

Root Slice: Pre-RP-Produktrest als ersten suiteweiten Vertikalslice geschlossen (2026-04-17 02:27)
---------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/text-rpg-pre-rp-product-model-v1.ssot.md` fixiert jetzt Kernfantasie, primaeres Spielversprechen, Zielgefuehl der ersten Session sowie den verbindlichen Pfad `Hub -> Spielhauptmenue -> Charakterstart -> erster Vollturn -> turn_resume_ready`.
- `novapolis_agent/docs/runbook.md`, `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` und `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` fuehren im selben Lauf denselben kleinsten stabilen Save-Punkt auf dem ersten `turn_resume_ready` und denselben Replay-Zweck als Nachvollzug und Wiedereinstiegshilfe.
- `todo.root.md` fuehrt den Root-Punkt damit als geschlossen; `novapolis-dev/docs/todo.index.md` und `WORKSPACE_STATUS.md` spiegeln dazu weiter die verbleibenden Modul-Open-Counts `Dev=1`, `Agent=1`, `RP=1`, `Sim=2`.

Workspace Review: Neue Folgepunkte fuer Root, Dev, Agent, RP und Sim erneut auf aktiven Boards angelegt (2026-04-17 02:17)
--------------------------------------------------------------------------------------------------------------------------

- `todo.root.md` fuehrt jetzt wieder einen suiteweiten Folgepunkt fuer den fast komplett offenen Produktrest in `text-rpg-pre-rp-product-model-v1.ssot.md`; `WORKSPACE_STATUS.md` spiegelt denselben Root-Folgepfad als aktiven Workspace-Zuschnitt statt des alten Nullstands aller Modul-Boards.
- `novapolis-dev/docs/todo.dev.md` fuehrt die Drift von `active-surface-index.md` und `WORKSPACE_INDEX.md` als neuen offenen Reader-/Surface-Punkt; `novapolis-dev/docs/todo.agent-board.md` zieht einen zweiten Handover-Referenzfall hinter `slot 30` auf den Product-Gate-Pfad.
- `novapolis-dev/docs/todo.rp.md` fuehrt `slot 36-40` aus `rp-folgekorridor-slot-31-35.ssot.md` wieder als offenen Anschluss; `novapolis-dev/docs/todo.sim.md` trennt den Sim-Rest jetzt in Architektur-Abschluss und reproduzierbaren Godot-CLI-Smoke.
- `novapolis-dev/docs/todo.index.md` und `WORKSPACE_STATUS.md` sind im selben Lauf auf den neuen Open-Count `Dev=1`, `Agent=1`, `RP=1`, `Sim=2` synchronisiert; Root bleibt bewusst ausserhalb dieser Modulsumme.

Sim Cleanup: Letzten Runtime-Telemetrie-/Helper-Block aus Main.gd in RuntimeTelemetryController gezogen (2026-04-17 02:07)
----------------------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/runtime_telemetry_controller.gd` ist neu und kapselt jetzt Eval-Summary-Refresh, Trendbildung, System-Metrik-Refresh, Python-Aufloesung sowie Health-/Reachability-Ableitung des verbliebenen Sim-Rests.
- `novapolis-sim/scripts/Main.gd` fuehrt fuer diesen Block jetzt nur noch dünne Wrapper und Statusanwendung aus; die zuvor lokalen Helfer `_refresh_latest_eval_summary()`, `_build_ai_trend_summary()`, `_refresh_system_metrics()`, `_format_*()`, `_effective_temperature_c()`, `_resolve_python_executable()`, `_sim_runtime_status()`, `_derive_health_state()` und `_is_external_server_reachable()` delegieren jetzt an den neuen Controller.
- `novapolis-dev/docs/todo.sim.md`, `novapolis-dev/docs/todo.index.md` und `novapolis-dev/docs/process/sim-controller-roadmap.ssot.md` spiegeln denselben neuen Stand im selben Lauf nach: direkt offen bleiben jetzt praktisch nur noch kleinere Cleanup-Altlasten statt eines weiteren grossen Controller-Kandidaten.

Sim Refactor: Summary-, Server-Ops- und Runtime-Audit-Block aus Main.gd in eigene Controller gezogen (2026-04-17 02:00)
--------------------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/agent_restpoint_summary_controller.gd`, `hub_server_ops_controller.gd` und `runtime_audit_controller.gd` sind neu und kapseln jetzt Restpoint-Summary-Bildung, lokale Serversteuerung sowie Runtime-Event-/Audit-Trail-Persistenz des verbleibenden Sim-Rests.
- `novapolis-sim/scripts/Main.gd` fuehrt fuer diese drei Bereiche jetzt nur noch Zustandsanwendung, Event-Weitergabe, Health-Ableitung und wenige gemeinsame Runtime-Helfer aus; die zuvor lokalen Blöcke `_refresh_agent_restpoint_summaries()`, `_build_*_summary()`, `_start_local_server()`, `_stop_local_server()`, `_update_server_control_ui()`, `_refresh_server_runtime_state()`, `_append_runtime_event()`, `_append_audit_event()`, `_runtime_event_rate_per_second()`, `_trim_runtime_event_rate_window()` und `_extract_error_code()` delegieren jetzt an die neuen Controller.
- `novapolis-dev/docs/todo.sim.md`, `novapolis-dev/docs/todo.index.md` und `novapolis-dev/docs/process/sim-controller-roadmap.ssot.md` spiegeln denselben neuen Stand im selben Lauf nach: direkt offen bleibt jetzt nur noch ein kleiner gemeinsamer Runtime-Telemetrie-/Helper-Block statt eines weiteren grossen Controller-Kandidaten.

Sim Refactor: Registry-/State-Ladepfade aus Main.gd in AgentRegistryStateController gezogen (2026-04-17 01:32)
----------------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/agent_registry_state_controller.gd` ist neu und kapselt jetzt Dataset-/Synonym-/Profile-/Advanced-State-Lader sowie das Security-Model-Laden mitsamt Default-Persistenz des Agent-Studio-Rests.
- `novapolis-sim/scripts/Main.gd` fuehrt fuer diesen Block jetzt nur noch die State-/Result-Anwendung aus; die zuvor lokalen Helfer `_load_dataset_registry_state()`, `_load_synonym_registry_state()`, `_load_profile_registry_state()`, `_load_advanced_settings_state()`, `_load_security_model_state()` und `_persist_security_model_state()` delegieren nur noch an den neuen Controller.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` spiegeln denselben kleineren Rest im selben Lauf nach: direkt offen bleiben jetzt vor allem Summary-Bildung, Server-Ops und Runtime-Audit.

Sim Refactor: Persistenz-/Registry-Schreibpfade aus Main.gd in AgentAuthoringPersistenceController gezogen (2026-04-17 01:24)
----------------------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/agent_authoring_persistence_controller.gd` ist neu und kapselt jetzt Dataset-/Synonym-/Profile-/Advanced-Persistenz, Synonym-Import/Export, lokale Persistenz-Validation und die zugehoerigen Registry-Schreibpfade des Agent-Studio-Authoring-Pfads.
- `novapolis-sim/scripts/Main.gd` fuehrt fuer diesen Block jetzt nur noch die Persistenz-State-/Result-Bruecke und die Runtime-Event-Weitergabe aus; die zuvor lokalen Helfer `_apply_*_form_payload()`, `_load_synonym_entries_from_path()`, `_build_synonym_delta()`, `_validate_synonym_entries()`, `_write_json_to_path()` und `_update_*_registry()` entfallen dort vollstaendig.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` spiegeln denselben kleineren Rest im selben Lauf nach: direkt offen bleiben jetzt vor allem Registry-State-/Ladepfade, Summary-Bildung, Server-Ops und Runtime-Audit.

Sim Refactor: Form-Payload-Building aus Main.gd in AgentAuthoringPayloadController gezogen (2026-04-17 01:16)
----------------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/agent_authoring_payload_controller.gd` ist neu und kapselt jetzt das Lesen der Form-Controls, lokale Pflichtfeldpruefung und die kanonische Payload-Normalisierung fuer Datasets, Synonyms, Finetune, Profiles, Advanced und Jobs.
- `novapolis-sim/scripts/Main.gd` fuehrt fuer diesen Pfad nur noch den Form-Dispatch weiter und wendet Status-Updates des neuen Controllers auf das bestehende Formular an; die zuvor lokalen Helfer `_build_agent_form_payload_from_controls()` und `_form_control_*()` entfallen dort vollstaendig.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` spiegeln denselben kleineren Rest im selben Lauf nach: direkt offen bleiben jetzt vor allem die Persistenz-/Registry-Schreibpfade des Agent-Studio-Blocks.

Sim Planung: Verbleibende Controller-Schnitte in eigener Roadmap-SSOT vorbereitet (2026-04-17 00:58)
-----------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-controller-roadmap.ssot.md` ist neu und grenzt die verbleibenden sinnvollen Controller-Kandidaten in `novapolis-sim/scripts/Main.gd` nach dem Runtime-Schnitt pragmatisch ab.
- Als direkte Folgecontroller sind dort `AgentAuthoringPayloadController` und `AgentAuthoringPersistenceController` dokumentiert; `AgentRegistryStateController`, `AgentRestpointSummaryController`, `HubServerOpsController` und `RuntimeAuditController` sind als nachgelagerte, aber belastbar abgegrenzte Folgepfade vorbereitet.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` spiegeln dieselbe Roadmap im selben Lauf, damit der offene Sim-Rest jetzt nicht nur technisch, sondern auch dokumentarisch auf Controller-Ebene vorbereitet ist.

Sim Refactor: Runtime-/Prozesssteuerung aus Main.gd in AgentRuntimeController gezogen (2026-04-17 00:50)
------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/agent_runtime_controller.gd` ist neu und kapselt jetzt Eval-Start/Stop, Finetune-Start/Stop, Jobs-Queue-Mutationen, Destructive-Guard sowie die Runtime-Refresh-Pfade fuer Eval und Finetune in einem eigenen Controller.
- `novapolis-sim/scripts/Main.gd` fuehrt fuer diesen Block jetzt eine explizite Runtime-State-/Result-Bruecke (`_agent_runtime_state()`, `_apply_agent_runtime_result()`) und delegiert die zuvor lokalen Handler `_on_agent_eval_run_pressed()`, `_apply_finetune_form_payload()`, `_apply_jobs_form_payload()`, `_load_jobs_state()`, `_confirm_destructive_action()`, `_refresh_eval_runtime_state()` und `_refresh_finetune_runtime_state()` an den neuen Controller.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` ziehen den kleineren Architekturrest im selben Lauf nach: offen bleiben fuer den Agent-Studio-Rest jetzt vor allem Payload-Building/Validation und Persistenz-/Registry-Pfade.

Sim Board: Offenen Agent-Studio-Rest auf konkrete Folgeschnitte geschaerft (2026-04-17 00:33)
----------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` traegt im offenen Architekturrest nicht mehr den Form-UI-Aufbau, sondern noch drei klar abgrenzbare Restgruppen: Payload-Building und lokale Form-Validation, Persistenz-/Registry-Schreibpfade fuer Authoring-Aktionen sowie Runtime-/Prozesssteuerung fuer Eval, Finetune und Jobs.
- `novapolis-dev/docs/todo.sim.md` fuehrt diesen Rest jetzt nicht mehr als unscharfen Runtime-/Apply-Block, sondern als konkreten Folgeschnitt mit drei technischen Teilpfaden plus Zielbild fuer einen kleineren `Main.gd`-Fassadenrest.
- `novapolis-dev/docs/todo.index.md` spiegelt dieselbe Schärfung im aktiven Modulindex, ohne den Open-Count des Sim-Boards kuenstlich aufzublasen.

Sim Debug: Hub-Overlay-Reste und Session-/Replay-Parsefehler bereinigt (2026-04-15 05:02)
-------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` blendet im exklusiven Modulmodus jetzt auch die separaten Hub-Topbar-Labels aus (`hub_title_label`, `hub_api_label`, `hub_polling_label`, `hub_queue_label`, `hub_errors_label`), sodass im Agent-Modul kein Hub-Overlay mehr durchscheint.
- `novapolis-sim/scripts/session_replay_request_controller.gd` ersetzt in `complete_live_session()` und `complete_live_replay()` das direkte `JSON.parse_string(...)` durch robustes Parsing via `JSON.new().parse(...)` und liefert bei leerem/ungueltigem Body kontrollierte `parse_error`-Events statt harter Parserlogs.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` spiegeln denselben Debug-Schnitt im selben Lauf auf den aktiven Board-Stand.

Sim UI: Hub beim exklusiven Modulwechsel ohne Zwischen-Einblendung (2026-04-15 04:56)
-----------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` fuehrt fuer Agent-/Checks-/RP-Modulumschaltung jetzt einen `defer_hub_refresh`-Pfad ein. Beim Wechsel zwischen zwei exklusiven Modulen werden Schliessvorgaenge intern ohne sofortige Hub-Aktualisierung ausgefuehrt.
- Die Hub-Sichtbarkeit wird anschliessend genau einmal zentral ueber `_apply_hub_visibility_for_modules()` gesetzt; damit faellt das kurzzeitige Wieder-Einblenden des Hub-Layouts beim Modulwechsel weg.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` ziehen diesen UI-Fix im selben Lauf auf den aktiven Board-Stand nach.

Sim Refactor: Agent-Form-UI aus Main.gd herausgezogen (2026-04-15 04:39)
-------------------------------------------------------------------------

- `novapolis-sim/scripts/agent_form_controller.gd` ist neu und fuehrt jetzt den Agent-Form-Baukasten fuer das Sim-Hub-Studio: Form-Defaults beim Oeffnen, Dropdown-Normalisierung, Platzhalter, Form-Layout und den dynamischen Feldaufbau fuer Datasets, Synonyms, Finetune, Profiles, Advanced und Jobs.
- `novapolis-sim/scripts/Main.gd` delegiert diese Form-UI-Pfade jetzt an den neuen Controller und verliert damit den lokalen Block `_refresh_agent_form_ui()`, `_rebuild_agent_form_fields()` sowie die ungenutzten `_build_*_form_template()`-Helfer. Im offenen Architekturrest bleiben dort jetzt vor allem Payload-Anwendung und Runtime-Aktionspfade.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` ziehen denselben kleineren Rest im selben Lauf nach: offen bleibt nur noch der Runtime-/Apply-Pfad im Agent-Studio-Block.

Sim Integration: Planungs-SSOT vollstaendig aufgeloest und archiviert (2026-04-15 04:35)
------------------------------------------------------------------------------------------

- Der verbliebene strategische Produktrest des Pre-RP-Sim-Pfads liegt jetzt kompakt in `novapolis-dev/docs/process/text-rpg-pre-rp-product-model-v1.ssot.md` als Entscheidungsraster statt als lange Moderationsfragenliste.
- UI-Hinweise fuer den Zustand ohne aktive RP-Integration liegen in `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md`; der minimale RP-Adapter-Scope fuer den ersten Integrationsschnitt liegt in `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`.
- Die fruehere Datei `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` ist vollstaendig aus der aktiven Dev-Oberflaeche verschwunden und lebt nur noch als historische Evidenz unter `novapolis-dev/archive/docs/others/sim-spielaufbau-vor-rp-integration.archive.2026-04-15.md`.
- Aktive Zielquellen referenzieren den frueheren Zwischenschritt nicht mehr; `novapolis-dev/docs/active-surface-index.md` fuehrt den Zustand auf dem Archivstand `2026-04-15`.

Sim Integration: Pre-RP-Sim-KPI-Matrix im Product Gate konkretisiert (2026-04-15 04:07)
------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` fuehrt jetzt die kanonische KPI-Matrix fuer den Pre-RP-Sim-Pfad ueber denselben `gm_session`- und Summary-Rahmen: `gm.session.continuity.v1` und `gm.session.reveal-discipline.v1` bleiben harte Gate-Blocker, `gm.session.option-quality.v1` und `gm.session.patch-validity.v1` Beobachtungen.
- Die Gate-Lesart der bestehenden Summary ist jetzt explizit: `severity=blocker` ist harter Produkt-Fail, `severity=warnung` bleibt Beobachtungspfad ohne Blockerstatus, `severity=beobachtung` ist der gruene Zielzustand des aktuellen Summary-Skripts.
- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt die Frage nach Sim-seitigen Gate-KPIs damit nicht mehr als offenen Planungsrest, sondern verweist fuer diesen Block auf das Product Gate.

Sim Integration: Detaillierte Turn-Budget-Mechanik in eigene Prozess-SSOT ausgelagert (2026-04-15 03:53)
---------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/text-rpg-turn-budget-model-v1.ssot.md` ist neu und fuehrt die ausdifferenzierte Referenzlogik fuer Zeitwerte, Modifikatoren, Budgetschwellen, Verdichtungswechsel, harte Blockaden und die drei mechanischen Referenzfaelle jetzt als eigene aktive Prozessquelle.
- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt damit keinen Detailblock fuer Zeit-/Budgetmechanik mehr, sondern nur noch den strategischen Planungsrest aus Produktannahmen, Moderationsfragen und Restcheckliste.
- Der kompakte Vertragskern in `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` bleibt bewusst unangetastet; die neue Prozess-SSOT ergaenzt ihn als Detailreferenz statt ihn zu duplizieren.

Sim Integration: Uebernommene Bloecke aus der Sim-Planungs-SSOT entfernt (2026-04-15 03:35)
-------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt nur noch den verbliebenen Planungsrest. Entfernt wurden die inzwischen aktiven Doppelungen fuer Start-/Charakterpfad, Bedienmodi, Turn-Zustandsrahmen, sichtbares Turn-Feedback, Resume-Wiedereinstieg sowie der zuvor dort noch mitgefuehrte UI-/Menueaufbau.
- Als Zielquellen verweist die bereinigte Sim-SSOT jetzt explizit auf `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`, `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`, `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`, `novapolis-dev/docs/process/rp-start-chooser.ssot.md`, `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`, `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` und `novapolis_agent/docs/runbook.md`.
- In der Datei verbleiben bewusst nur noch die nicht kanonisierten Detailmatrizen fuer Zeit/Modifikatoren, mechanische Referenzfaelle, Moderationsfragen und die grosse Planungscheckliste.

Sim Integration: Budgetlogik und RP-Startpfad in Bestandsdaten nachgezogen (2026-04-15 03:27)
-----------------------------------------------------------------------------------------------

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` fuehrt jetzt den kompakten Vertragskern fuer strukturierte Budget- und Zeitlogik: `plan_analysis`, `budget_decision` und `time_state` bleiben optionale Vertragsbloecke mit festen Schritt- und Modifikatorklassen statt frei in der Planungs-SSOT zu bleiben.
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` behandelt dieselbe Budget- und Zeitlogik jetzt als Gate-relevante Driftklasse. Damit ist der kleine Vertragskern produktnah verankert, ohne die gesamte ausdifferenzierte Zeitwert-Matrix sofort als Runtime-Pflicht zu promoten.
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md` und `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` fuehren jetzt den RP-gebundenen Neueinstieg ueber `Hub -> Spielhauptmenue -> Start-Chooser -> slot_00` sowie den minimalen OOC-Charakterstart fuer neue Laeufe. Die Sim-Planungs-SSOT weist denselben Uebernahmestand jetzt explizit aus.

Sim Integration: Spielfluss und Turn-Feedback in Bestandsdaten nachgezogen (2026-04-15 03:16)
----------------------------------------------------------------------------------------------

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` fuehrt jetzt fuer den Sim-vor-RP-Pfad zusaetzlich `player_input.mode`, den sichtbaren `turn_state`-Rahmen und den optionalen Block `turn_feedback`. Damit liegen Bedienmodus, Turn-Lebenszyklus und sichtbare Turn-Rueckmeldung nicht mehr nur in der Planungs-SSOT, sondern auf demselben Vertragsblock wie `resume_checkpoint_id`, `carry_over`, `world_log` und `pc_log`.
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` und `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` ziehen denselben Nachzug nach: Bedienmodi, Turn-Zustaende und sichtbares Turn-Feedback sind jetzt explizite Driftklassen im Product Gate, und der Wiedereinstieg hinter `slot 30` bleibt an `turn_resume_ready` plus denselben Pfad `Hub -> Spielhauptmenue -> Resume/Checkpoint` gebunden.
- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` weist den Uebernahmestand jetzt selbst aus und grenzt die weiter reine Planungsmasse sauber ab: Zeitwert-Matrix, Referenzfaelle, Moderationsfragen und Checkliste bleiben dort vorerst bewusst Ideenraum.

Sim Hub: Fortsetzungspersistenz, Exportpfad und UI-IA kanonisiert (2026-04-15 03:00)
-------------------------------------------------------------------------------------

- `novapolis-sim/scripts/Main.gd` persistiert ueber den bestehenden Hub-Prefs-Pfad jetzt nicht mehr nur Sichtbarkeit und Default-Panel, sondern zusaetzlich `session_id`, `scene_id`, `resume_checkpoint_id` und den zuletzt gewaehlten Replay-Checkpoint. Beim Neustart wird eine vorhandene Session-ID nicht mehr durch einen Zeitstempel ersetzt; stattdessen synchronisiert die Sim `GET /session/{session_id}` und `GET /session/{session_id}/replay` direkt erneut.
- `novapolis-dev/docs/process/sim-export-release-path.ssot.md` ist als kanonische Export-/Release-SSOT neu. Die Datei trennt Clean-Checkout, lokalen Vollstand und exportierte Laufzeit, dokumentiert den Windows-Desktop-Zielpfad `novapolis-sim/exports/windows/NovapolisSim.exe` und fuehrt den lokalen Smoke fuer die exportierte App als expliziten Godot-Klickpfad.
- `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` ist als kanonische IA-SSOT neu. Dort sind jetzt Screen-/Menuebaum, Rueckwege und Zustandsbesitz fuer Hub, eigentlichen Spielpfad, Replay/Resume und operative Module festgehalten; `novapolis-sim/README.md`, `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md` verweisen im selben Lauf auf dieselben Sim-SSOTs.
- Verifikation im selben Lauf: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/hub_preferences_store.gd` und `novapolis-sim/README.md` ohne Befund; markdownlint, Frontmatter-Check und TODO-Index-Sync werden fuer die betroffenen Doku-Dateien im selben Lauf nachgezogen.

Sim Integration: Turn-, Resume- und Startanker in Bestandsdaten uebernommen (2026-04-14 20:42)
-----------------------------------------------------------------------------------------------

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` fuehrt den Sim-vor-RP-Rahmen jetzt explizit ueber denselben Vertrag: aeusserer `30`-Minuten-Turn, eingebettete `1`-Minuten-Verdichtung, verpflichtender `resume_checkpoint_id` und Carry-Over als Teil desselben Session-, Log- und Replay-Blocks.
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` und `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` pruefen bzw. fuehren denselben Turn-, Resume- und Replay-Rahmen jetzt explizit hinter dem bestehenden Slice, statt Sim dafuer einen Parallelpfad zu erlauben.
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md` und `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` binden Neueinstiege jetzt explizit an `slot_00`, belegte Startgebiete und denselben Sessionvertrag; freie Sim-Vorstarts ausserhalb der RP-Produktanker sind damit dokumentarisch ausgeschlossen.
- Verifikation im selben Lauf: markdownlint, Frontmatter-Check und TODO-Index-Sync laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Ideensammlung gegen bestehende Bestandsdaten abgegrenzt (2026-04-14 20:32)
----------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` markiert den aktuellen Stand jetzt explizit als Ideensammlung statt als neue direkte Bestandsdatenquelle. Der naechste Schritt ist dort als Pflicht zur Einbindung in die bereits aktiven Zielquellen `text-rpg-session-contract-v1.md`, `text-rpg-product-gate-v1.ssot.md`, `text-rpg-slice-2-handover-v1.ssot.md`, RP-Start-/Folgekorridor-SSOTs sowie die belegten Runtime-Pfade festgezogen.
- Damit ist klargestellt, dass Turn-, Tick-, Replay- und Startlogik aus der Sim-SSOT erst nach sauberer Uebernahme in bestehende Vertrags-, Gate-, Handover- und RP-Bestandsdokumente als operativer Bestand gelten und nicht als parallele Wahrheit in der Ideensammlung verbleiben sollen.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Mechanik-Gates, Replay-Grenzen und Blockade-Alternativpfad nachgezogen (2026-04-14 20:22)
-------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt eine messbare Pruefmatrix fuer die bestehenden Mechanik-Akzeptanzkriterien, damit Standardturn, Fragmentierung, Bestaetigungspflicht, harte Blockade, Verdichtungswechsel, Carry-Over und Sessionvertragsabbildung nicht nur als Zielbild, sondern als pruefbare Gate-Faelle vorliegen.
- Zusaetzlich sind dort die Replay-/Checkpoint-Grenzen fuer Verdichtungsfenster explizit dokumentiert, die UI-Verankerung des Turn-Feedbacks auf Stage-, Interaktions- und Ops-Flaeche festgezogen und ein dritter Referenzfall fuer `harte Blockade -> vorbereitende Teilhandlung -> aufgeloester Folgeturn-Anker` als kompletter Beleglauf eingefuegt.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Referenzturns fuer Normalmodus und Verdichtung simuliert (2026-04-14 19:45)
-------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt zwei komplette mechanische Beispielturns: einen normalen 30-Minuten-Turn mit fragmentierter Druckprobe und einen Turn, der mitten in einen verdichteten sozialen Konflikt kippt und sauber wieder in den normalen Turn zurueckkehrt.
- Die beiden Referenzfaelle zeigen nicht nur Regeln, sondern den gesamten Ablauf aus Lagebild, Spielerplan, Bewertung, Systemausgabe, Ausspielung, Carry-Over und Mindestfeedback. Damit ist die SSOT jetzt auch als Beleg nutzbar, dass die Mechanik praktisch lesbar bleibt.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Review-Luecken in SSOT geschlossen (2026-04-14 19:41)
-------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt ein explizites Zustandsmodell fuer den Lauf zwischen Briefing, Planung, Budgetpruefung, Bestaetigung, Ausspielung, Verdichtung, Aufloesung und Resume-Bereitschaft. Dadurch ist die Turn-Mechanik nicht mehr nur in Regeln, sondern auch in erlaubten Uebergaengen beschrieben.
- Zusaetzlich sind dort neue Mechanik-Akzeptanzkriterien, ein Turn-Feedback-Mindestset und das Mapping der internen Turn- und Tick-Mechanik auf den bestehenden Sessionvertrag dokumentiert; dabei wurde zugleich die inkonsistente Ueberschrift `Tick-Referenzschema` im Turn-Schema bereinigt.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Spieler-Ausgaberegeln fuer Turn-Mechanik in SSOT verankert (2026-04-14 19:27)
-----------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt eine eigene Regelschicht fuer die Ausgabe an den Spieler: klare Budgethinweise, sichtbare Fragmentierung, konkrete Blockade-Sprache und markierte Verdichtungswechsel.
- Zusaetzlich liegen dort Referenzformulierungen fuer `innerhalb des Rahmens`, `knapp drueber`, `deutlich drueber`, harte Blockade sowie Ein- und Austritt aus dem Verdichtungsmodus, damit die interne Mechanik spaeter nicht beliebig nach aussen formuliert wird.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Prioritaetslogik und Blockade-Regeln in SSOT verankert (2026-04-14 19:21)
-------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` trennt jetzt explizit die Reihenfolge `harte Blockade -> Verdichtungsbedarf -> Minutenmodifikatoren -> Sequenzverlust`, damit die Zeitableitung nicht mit unmittelbarer Reaktionslogik oder Unmoeglichkeitsfaellen vermischt wird.
- Zusaetzlich sind dort feste Eskalationsregeln fuer den Wechsel in den Verdichtungsmodus und konkrete Blockade-Klassen wie koerperlich, werkzeugseitig, zugangsseitig, wissensseitig und sozial unmoeglich dokumentiert.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Modifikator-Matrix und Tick-Schema in SSOT nachgezogen (2026-04-14 19:16)
-----------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt feste Zeitmodifikatoren fuer Zustand der Figur, Umgebung und Druck, Hilfsmittel, Unterstuetzung sowie Vertrautheit und Routine. Die Zeitableitung hat damit erstmals konkrete Zu- und Abschlaege statt nur Kategorien.
- Zusaetzlich liegt dort nun ein technisches Tick-Schema fuer den Verdichtungsmodus mit `tick_context`, `perception`, `decision_window`, `resolution` und `carry_tick_state`; zugleich ist der Tick fest auf `1 Minute` normiert.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Zeitbasis auf 30-Minuten-Turn umgestellt (2026-04-14 19:14)
----------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt den Normalmodus jetzt mit `1 Turn = 30 Minuten` statt `1 Turn = 1 Stunde`; dazu sind Zeitklassen, Referenz-Grundwerte, Budgetschwellen und das technische Antwortschema auf denselben Rahmen nachgezogen.
- Der Verdichtungsmodus bleibt bei `1 Tick = 1 Minute`, arbeitet dadurch jetzt im Regelfall mit bis zu `30 Ticks` pro Turn und fuehrt Restzeit nach dem Ruecksprung in einen 30-Minuten-Kontext zurueck.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Referenz-Grundwerte und Turn-Schema in SSOT nachgezogen (2026-04-14 19:06)
------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt eine erste Referenz-Grundwerttabelle fuer Standardhandlungen, damit die Zeitableitung auf wiederholbaren Minutenwerten statt nur auf Klassen und Modifikatoren aufbaut.
- Zusaetzlich liegt dort nun ein technisches Antwortschema fuer `plan_analysis`, `budget_decision`, `execution_result`, `carry_over` und `time_state`, inklusive Referenz-JSON und festen Semantikregeln fuer Klassifikation, Fragmentierung und Wiederaufnahme.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Stunden-Turn als belastbare Mechanik geschaerft (2026-04-14 18:49)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt den Stunden-Turn jetzt nicht mehr nur als Erzaehlrahmen, sondern als abgeleitete Mechanik: atomare Schrittzerlegung, feste Grundwerte, Pflicht-Modifikatoren und Sequenzverlust mit Uebergangsaufschlag.
- Zusaetzlich sind klare Budgetschwellen dokumentiert (`<= 60`, `60 bis 75`, `75 bis 120`, `> 120` oder logisch unmoeglich), dazu die Persistenzzustaende `begonnen`, `unterbrochen`, `offen` samt konkreter Zustandsfelder fuer Wiederaufnahme und Fragmentierung.
- Die Verdichtungsregel fuehrt jetzt explizite Trigger, Tick-Logik und Ruecksprung in den Stundenkontext; Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Turn-Modell, Zeitmodell und Verdichtungsregel in SSOT konsolidiert (2026-04-14 18:11)
----------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt den bisher besprochenen Spielaufbau als zusammenhaengenden Zwischenstand: 2026-06-13 09:19
- Zusaetzlich ist dort jetzt eine vorlaeufige Verdichtungsregel dokumentiert: Bei direkten NPC-Interaktionen kann der Stunden-Turn in bis zu 60 Ticks zerlegt werden, damit soziale oder konfliktnahe Situationen nicht unplausibel grob aufgeloest werden.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: Erste Festlegungsrunde zum Spielaufbau in SSOT uebernommen (2026-04-14 17:09)
--------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt die erste beantwortete Entscheidungsrunde als feste Vorfestlegung: Charaktererstellung in den ersten 5 bis 10 Minuten, Hauptmenue als heruntergekommener U-Bahn-Ticketschalter, Erzaehler-KI als Eintrittsschwelle, klare Trennung Operator im Hub versus Spieler im eigentlichen Spiel und Turn als kleinste spielbare Einheit.
- Zusaetzlich ist dort jetzt eine sachliche Einordnung des aktuellen Planungsstands dokumentiert, inklusive der offenen Risiken bei Balancing der Eingabemodi und beim Spannungsfeld zwischen realitaetsnahem Fortschritt und kurzfristig sichtbarem Feedback.
- Verifikation im selben Lauf: markdownlint und Frontmatter-Check laufen fuer die betroffenen Doku-Dateien PASS; der anschliessende Projekt-Scan fuer Turn-/Spielzug-Anker wird im Antworttext mit konkreten Evidenzstellen zusammengefasst.

Sim Planung: Fragenkatalog und Spielaufbau-Checkliste vor RP-Integration erweitert (2026-04-14 16:16)
------------------------------------------------------------------------------------------------------

- `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` fuehrt jetzt einen strukturierten Moderationsblock, damit der Spielaufbau nicht nur als Zielbild, sondern als gemeinsam beantwortbarer Fragenpfad weiterentwickelt werden kann.
- Zusaetzlich liegt dort jetzt eine umfangreiche Checkliste vor, die Produktkern, Spielerrolle, Startfluss, Kernloop, Entscheidungen, Ressourcen, Sessionlogik, Save/Resume/Replay, UI-Komposition, Onboarding, Robustheit und die RP-Integrationsnaht systematisch abdeckt.
- Verifikation im selben Lauf: markdownlint, Frontmatter-Check und TODO-Index-Sync laufen fuer die betroffenen Doku-Dateien PASS.

Sim Planung: SSOT fuer Spielaufbau vor RP-Integration angelegt (2026-04-14 16:00)
-------------------------------------------------------------------------------

- Neue Planungsdatei unter `novapolis-dev/docs/process/sim-spielaufbau-vor-rp-integration.ssot.md` angelegt, um den Sim-Spielaufbau vor RP-Integration als Phasenmodell mit klarer Integrationsgrenze festzuziehen.
- Enthalten sind Scope/Nicht-Ziele, Zielbild (Hub, Session-Init, Kernloop, Resume/Replay, RP-Integrationsfenster), vertragliche Uebergabefelder und Akzeptanzkriterien fuer den Start der RP-Kopplung.
- Verifikation im selben Lauf: markdownlint, Frontmatter-Check und TODO-Index-Sync laufen fuer die betroffenen Doku-Dateien PASS.

Sim UI: Labelklaerung fuer Chat-Kontexte (Hub-Chat vs RP-Chat) (2026-04-14 15:54)
-------------------------------------------------------------------------------

- Auf Wunsch ist die sichtbare Benennung der beiden Kontexte im Sim-Hub jetzt eindeutig: Der Chatbereich im Hub heisst `Hub-Chat`, und der RP-Bereich traegt den Titel `RP-Chat`.
- Technisch ist das als minimaler Scene-Textpatch in `novapolis-sim/Main.tscn` umgesetzt (`HubChatTitleLabel`, `RpStudioTitleLabel`), ohne Eingriff in Runtime-Logik oder Modulzustand.
- Verifikation im selben Lauf: `get_errors` bleibt fuer `Main.tscn` und `scripts/Main.gd` ohne Befund; markdownlint, Frontmatter-Check und TODO-Index-Sync laufen PASS.

Sim Hotfix: Chat-Priorisierung bei knapper Ops-Hoehe, Replay kompakter (2026-04-14 15:49)
-------------------------------------------------------------------------------------------

- Der Folgewunsch zum Layout-Hotfix ist umgesetzt: Bei sehr knapper vertikaler Flaeche priorisiert die rechte Ops-Spalte jetzt den Live-Chat, waehrend das Replay-Panel zuerst kompakter wird.
- In `novapolis-sim/scripts/hub_layout_controller.gd` nutzt die Hoehenverteilung nun `chat_pref_height` plus hartes Replay-Minimum statt gleichwertiger Mindestverteilung. Bei Platzmangel wird zunaechst Replay reduziert, bevor Chat unter seine Mindesthoehe faellt.
- Verifikation im selben Lauf: `get_errors` bleibt fuer `hub_layout_controller.gd` und `Main.gd` ohne Befund; markdownlint, Frontmatter-Check und TODO-Index-Sync laufen PASS.

Sim Hotfix: Non-Overlap-Guard fuer rechte Ops-Spalte (Replay, Chat, Hub Config) (2026-04-14 15:44)
------------------------------------------------------------------------------------------------------

- Der gemeldete UI-Befund zeigte Ueberlagerungen in der rechten Hub-Spalte: Replay-/Resume, Live-Chat und Hub-Config konkurrierten um dieselbe vertikale Flaeche. In `novapolis-sim/scripts/hub_layout_controller.gd` laeuft die Stapelung jetzt nicht mehr mit starren Hoehen, sondern ueber einen dynamischen Non-Overlap-Guard.
- Der neue Guard verteilt die verfuegbare Spaltenhoehe zwischen Replay-, Chat- und Config-Panel adaptiv, setzt Mindesthoehen mit kontrolliertem Rueckbau und verhindert negative Zwischenraeume. Zusaetzlich ist fuer die drei Panels `clip_contents` aktiv, damit bei engem Raum keine Inhalte mehr in Nachbarbereiche ueberzeichnen.
- Verifikation im selben Lauf: `get_errors` bleibt fuer `hub_layout_controller.gd` und `Main.gd` ohne Befund; markdownlint, Frontmatter-Check und TODO-Index-Sync laufen PASS.

Sim Hotfix: Typinferenz fuer slot_number in SessionReplayStateController stabilisiert (2026-04-14 15:36)
---------------------------------------------------------------------------------------------------------

- Aus dem laufenden Godot-Befund kam ein neuer Parserfehler: `Cannot infer the type of 'slot_number' variable because the value doesn't have a set type` in `res://scripts/session_replay_state_controller.gd`.
- Die Stelle in `build_selected_replay_checkpoint_state(...)` ist jetzt explizit typisiert: `slot_number` wird als `int` gefuehrt statt als implizit inferierter Lokalwaert.
- Verifikation im selben Lauf: `get_errors` bleibt fuer `novapolis-sim/scripts/session_replay_state_controller.gd` und `novapolis-sim/scripts/Main.gd` ohne Befund.

Sim Hotfix: Typinferenz fuer epoch in SessionReplayHelpers stabilisiert (2026-04-14 15:06)
-------------------------------------------------------------------------------------------

- Aus dem laufenden Godot-Befund kam ein neuer Parserfehler: `Cannot infer the type of 'epoch' variable because the value doesn't have a set type` in `res://scripts/session_replay_helpers.gd`.
- Die Stelle in `find_slot_for_checkpoint(...)` ist jetzt explizit typisiert: statt implizitem `var epoch := loaded_epochs[current_epoch_index]` laeuft dort eine klare Variant-zu-Dictionary-Normalisierung mit Typguard. Damit entfaellt die unsichere Typinferenz fuer den lokalen `epoch`-Wert.
- Verifikation im selben Lauf: `get_errors` bleibt fuer `novapolis-sim/scripts/session_replay_helpers.gd` und `novapolis-sim/scripts/Main.gd` ohne Befund.

Sim Hotfix: Hub-Layout-Controller dedupliziert nach Godot-Preload-Parserfehler (2026-04-14 15:01)
-----------------------------------------------------------------------------------------------

- Aus einem laufenden Godot-Befund kam ein harter Parse-Fehler auf `res://scripts/hub_layout_controller.gd` (`Could not preload resource script`). Die Ursache war kein Pfadproblem, sondern ein Dateidrift: im Script war eine zweite Klassenhaelfte angehaengt, inklusive doppeltem `class_name HubLayoutController`.
- `novapolis-sim/scripts/hub_layout_controller.gd` ist auf eine einzelne, konsistente Klassen-Definition zurueckgefuehrt. Damit ist der Preload in `novapolis-sim/scripts/Main.gd` wieder parsebar und der vom Editor gemeldete Fehlerpfad geschlossen.
- Verifikation im selben Lauf: `get_errors` bleibt fuer `Main.gd` und `hub_layout_controller.gd` ohne Befund; der Klassenbezeichner kommt im Zielscript wieder genau einmal vor.

Sim Refactor: Agent-Studio-UI/Layout aus Main.gd herausgezogen und Controller-Drift bereinigt (2026-04-14 14:49)
--------------------------------------------------------------------------------------------------------------

- Der naechste Architektur-Schnitt verschiebt den zentralen Agent-Studio-UI-Pfad aus `novapolis-sim/scripts/Main.gd` nach `novapolis-sim/scripts/agent_studio_controller.gd`. Der neue Controller kapselt jetzt Agent-Studio-UI-Exklusivschaltung, Agent-Studio-Layout und den zentralen Studio-Refresh, waehrend `Main.gd` fuer diesen Bereich nur noch State-Aufbereitung und Orchestrierung traegt.
- Im selben Lauf wurde ein echter Dateidrift behoben: `novapolis-sim/scripts/hub_config_controller.gd` und `novapolis-sim/scripts/checks_rp_controller.gd` enthielten jeweils eine versehentlich doppelt angehaengte zweite Dateihälfte. Beide Dateien sind jetzt auf einen sauberen, einfachen Controllerstand zurueckgefuehrt.
- Die statische Pruefung ist fuer `Main.gd`, `agent_studio_controller.gd`, `hub_config_controller.gd` und `checks_rp_controller.gd` gruen (`get_errors` ohne Befund). Ein echter Godot-Headless-Lauf bleibt fuer diesen Schnitt weiter nur mit verfuegbarer lokaler Binary moeglich.

Sim Refactor: Layout-, Hub-Config- und Checks/RP-Controller aus Main.gd herausgezogen (2026-04-14 14:36)
------------------------------------------------------------------------------------------------------

- Der breite Sammellauf schneidet die letzten klar abgrenzbaren `Main.gd`-Bereiche aus dem Sim-Hub heraus. `novapolis-sim/scripts/hub_layout_controller.gd`, `hub_config_controller.gd` und `checks_rp_controller.gd` kapseln jetzt den Responsive-/Hub-Layoutpfad, die Hub-Config-/Prefs-Bedienlogik sowie die Checks-/RP-Modul-UI.
- `novapolis-sim/scripts/Main.gd` behaelt fuer diese Pfade nur noch Zustandsfluss, Signal-/Event-Folge und die sichtbare Node-Fassade. Als groesserer Architekturrest bleibt im Wesentlichen nur noch der bewusst nicht im selben Kleinschnitt ausgelagerte Agent-Studio-Block, weil er Form-State, Scriptstarts, Registry-Lader und Runtime-Refreshs noch eng koppelt.
- Die statische Pruefung ist fuer `Main.gd`, `hub_layout_controller.gd`, `hub_config_controller.gd` und `checks_rp_controller.gd` gruen (`get_errors` ohne Befund). Ein echter Godot-Headless-Lauf bleibt fuer diesen Sammelschnitt weiter nur mit verfuegbarer lokaler Binary moeglich.

Sim Refactor: Hub-Chat-Controller aus Main.gd herausgezogen (2026-04-14 14:10)
--------------------------------------------------------------------------------

- Der vierte Entflechtungsschnitt zieht jetzt den Live-Spielclient-Chat aus `novapolis-sim/scripts/Main.gd`. `novapolis-sim/scripts/hub_chat_controller.gd` kapselt Slot-/Context-Aufbau, Retrieval-Query, Request-Start, Response-Auswertung und die Chat-State-Anwendung fuer den Hub-Chat-Pfad.
- `novapolis-sim/scripts/Main.gd` behaelt fuer den Chat nur noch Widget-Status, Protokollzeilen und die Folgeaktionen nach erfolgreicher Antwort, also Session-/Replay-Refreshes und das bestehende UI-Refresh. Damit verliert die Datei erneut einen klar abgegrenzten Runtime-Pfad, ohne ihre sichtbare Hub-Fassade aufzubrechen.
- Die statische Pruefung ist fuer `Main.gd` und `hub_chat_controller.gd` gruen (`get_errors` ohne Befund). Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor weiter nur mit verfuegbarer lokaler Binary moeglich.

Sim Refactor: Session-/Replay-State-Controller aus Main.gd herausgezogen (2026-04-14 14:02)
--------------------------------------------------------------------------------------------

- Der dritte Entflechtungsschnitt verschiebt jetzt nicht mehr nur Hilfs- oder Requestlogik, sondern die eigentlichen Session-/Replay-State-Transitionen aus `novapolis-sim/scripts/Main.gd`. `novapolis-sim/scripts/session_replay_state_controller.gd` baut jetzt die Zustands-Snapshots fuer Live-Session-Anwendung, Replay-Manifest-Uebernahme und Resume-/Checkpoint-Anwendung.
- `novapolis-sim/scripts/Main.gd` spiegelt in diesen Pfaden nur noch die vom Controller gelieferten Snapshot-Updates auf bestehende Member und fuehrt danach UI-Refreshes aus. Damit bleibt die Datei weiter kompatibel zur Szene, verliert aber erneut handgeschriebene Zustandsmutation.
- Die statische Pruefung ist fuer `Main.gd`, `session_replay_state_controller.gd`, `session_replay_request_controller.gd` und `session_replay_helpers.gd` gruen (`get_errors` ohne Befund). Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor nur mit verfuegbarer lokaler Binary moeglich.

Sim Verifier: Headless-Smoke jetzt ueber Projekt, Scene und Kernknoten statt Minimal-Check (2026-04-14 13:57)
-----------------------------------------------------------------------------------------------------------

- `novapolis-sim/scripts/verify_sim.gd` ist kein Minimalcheck mehr auf `application/config/name`, sondern prueft jetzt Projektname, Main-Scene, Autoload `SimClient`, das Root-Script `res://scripts/Main.gd` sowie die zentralen Hub-, Replay-, Chat- und Modul-Knoten direkt an einer instanziierten Main-Scene.
- Das Sim-Board schliesst diesen Verifier-Punkt damit im selben Lauf. Gleichzeitig ist dort der naechste Architektur-Folgeschnitt festgehalten: Nach Helpern und Request-Controller soll als naechstes die Session-/Replay-Zustandsanwendung selbst in einen eigenen State-Controller wandern.
- Die statische Pruefung ist fuer `verify_sim.gd`, `Main.gd`, `project.godot` und `Main.tscn` gruen (`get_errors` ohne Befund). Ein echter Godot-Headless-Lauf war im aktuellen Terminalkontext nicht belegbar, weil weder `GODOT_BIN` gesetzt war noch `godot`/`godot4` im PATH aufloesbar waren.

Sim Refactor: Session-/Replay-Request-Controller aus Main.gd herausgezogen (2026-04-14 13:49)
----------------------------------------------------------------------------------------------

- Der zweite Entflechtungsschnitt zieht jetzt nicht mehr nur Hilfslogik, sondern den eigentlichen Request-Lebenszyklus aus `novapolis-sim/scripts/Main.gd`. `novapolis-sim/scripts/session_replay_request_controller.gd` kapselt jetzt Request-Guards, In-Flight-Status und Response-Auswertung fuer Session- und Replay-HTTP-Laeufe.
- `novapolis-sim/scripts/Main.gd` behaelt fuer diese Pfade nur noch Host/Port-Aufloesung, die Anwendung erfolgreicher Sessiondaten auf Epochen-/Replay-Zustand und die UI-Folgen. Damit verliert die Datei erneut konkrete Verantwortung, ohne Node-Pfade oder Bedienlogik aufzubrechen.
- Die statische Pruefung ist fuer `Main.gd`, `session_replay_request_controller.gd`, `session_replay_helpers.gd` und `hub_preferences_store.gd` gruen (`get_errors` ohne Befund). Der Godot-Headless-Nachweis bleibt als eigener offener Sim-Punkt bestehen, weil im Terminalkontext weiterhin keine lokal aufloesbare Godot-Binary belegbar war.

Sim Refactor: Erster Runtime-Schnitt fuer Main.gd umgesetzt (2026-04-14 13:29)
---------------------------------------------------------------------------

- Die Entflechtung des Sim-Hubs ist nicht bei Planung stehengeblieben: `novapolis-sim/scripts/hub_preferences_store.gd` kapselt jetzt das Laden/Speichern der Hub-Prefs, und `novapolis-sim/scripts/session_replay_helpers.gd` traegt die Session-/Replay-Normalisierung, Endpoint-Bildung sowie Checkpoint-/Slot-Helfer.
- `novapolis-sim/scripts/Main.gd` behaelt vorerst die sichtbare Node- und UI-Orchestrierung, delegiert aber die genannten Runtime-Teile jetzt an die neuen Helfer statt ihre Implementierung weiter inline zu tragen. Das ist bewusst ein kleiner erster Schnitt, damit Szene, Node-Pfade und Bedienlogik kompatibel bleiben.
- Die statische Pruefung ist fuer `Main.gd` plus beide neue Helper-Dateien gruen (`get_errors` ohne Befund). Ein erneuter Godot-Headless-Lauf war in diesem Terminal-Kontext nicht belegbar, weil keine aufloesbare Godot-Binary im PATH zurueckkam; der offene Verifier-Ausbau bleibt daher folgerichtig weiter als eigener Sim-Punkt im Board.

Sim Planung: Folge-Backlog nach Hub-Abschluss auf belegte Nicht-UI-Punkte gesetzt (2026-04-14 13:06)
-------------------------------------------------------------------------------------------------

- Der Sim-Hub ist nach UI-Reset und Replay-/Resume-Abschluss nicht mehr ohne offenen Folgepfad, aber die naechsten Punkte betreffen bewusst nicht die direkte Oberflaechen-Implementierung. `novapolis-dev/docs/todo.sim.md` fuehrt jetzt einen neuen Sim-Backlog fuer Architektur-Schnitt, Verifier-Tiefe, Release-/Exportpfad, Session-Fortsetzung und die fachliche Beschreibung des eigentlichen Spiel-UI-/Menueaufbaus.
- Die Ableitung ist direkt aus dem Iststand belegt: `novapolis-sim/scripts/Main.gd` traegt weiterhin Layout, Session-/Replay-Sync, Audio-Bridge, Hub-Prefs und Modulsteuerung in einem Script; `novapolis-sim/scripts/verify_sim.gd` prueft bislang nur eine Projekteinstellung; `novapolis-sim/README.md` verweist fuer Produktion nur auf `Project -> Export`; und unter `novapolis-dev/docs/process/` existiert derzeit keine eigene aktive Sim-SSOT fuer Menue- oder Informationsarchitektur.
- `novapolis-dev/docs/todo.index.md` zieht den neuen Sim-Open-Count im selben Lauf auf `5` nach. Produktcode bleibt in diesem Planning-Lauf unveraendert; es geht nur um den naechsten belastbaren Arbeitszuschnitt.

Wochenpruefung 2026-04-14: letzter Ruff-/Black-Rest geschlossen, Full-Check wieder vollstaendig PASS (2026-04-14 12:47)
-----------------------------------------------------------------------------------------------------------------

- Der zwischenzeitliche Dev-Rest der Wochenpruefung ist im selben Lauf wieder geschlossen. `novapolis_agent/app/api/tts_models.py` nutzt fuer `TtsOutputFormat` jetzt `StrEnum`, die betroffenen TTS- und CPU-Limit-Tests sind lint-/formatkonform nachgezogen, und der von `black` gemeldete Restdateisatz in `scripts/` ist formatiert.
- Der gezielte Pytest-Scope fuer `tests/scripts/test_run_with_cpu_limit.py`, `tests/test_tts_models_validators.py` und `tests/test_tts_provider_edges.py` ist PASS; `ruff check novapolis_agent scripts`, `black --check novapolis_agent scripts` und der frische Sammellauf `.tmp/results/reports/checks_report_20260414_124519.md` sind ebenfalls PASS.
- `todo.dev.md` und `todo.index.md` fuehren Dev damit wieder auf `offen: 0`; zusammen mit den bereits geschlossenen RP-, Agent- und Sim-Punkten stehen alle aktiven Modul-Boards wieder auf `0`.

Wochenpruefung 2026-04-14: Doku-/Governance-Drift bereinigt, Rest auf Ruff/Black eingegrenzt (2026-04-14 12:37)
------------------------------------------------------------------------------------------------------------------

- Der erste Wochenlauf zeigte noch Nebengeräusche ausserhalb des eigentlichen Produktrests: `markdownlint` griff in eine lokale Backup-Venv, und `path-portability` meldete hostgebundene Godot-Pfade in aktiven Root-/Sim-Dokus.
- Der Same-Run-Fix bleibt bewusst minimal: `.markdownlint-cli2.jsonc` ignoriert jetzt auch `.venv-py313-backup-*/**`, und `DONELOG.md`, `WORKSPACE_STATUS.md`, `novapolis-dev/docs/donelog.md` sowie `novapolis-dev/docs/todo.sim.md` fuehren die erfolgreiche Headless-Verifikation nur noch portabel als lokal gestartete Godot-4.6.1-Binary.
- Der frische Recheck `.tmp/results/reports/checks_report_20260414_123622.md` ist damit fuer `markdownlint`, `frontmatter`, `path-portability`, `namingpolicy`, `todo-index-sync`, `doc-freshness`, `logs-policy`, `pyright`, `mypy` und `pytest` PASS; der separate Coverage-Lauf haelt `94.92%`, und der Sim-Offline-Check bleibt mit `summary=fail:0,warn:0` gruen.
- Offen bleibt nur noch der repo-eigene Python-Baseline-Rest `ruff=FAIL (8)` und `black=FAIL (13)`; `todo.dev.md` fuehrt dafuer wieder genau einen offenen Dev-Punkt, und `todo.index.md` zieht den Dev-Open-Count im selben Lauf auf `1` nach.

Sim Replay/Resume: Hub nutzt jetzt den bestehenden Replay-Vertrag sichtbar und bedienbar (2026-04-14 12:21)
----------------------------------------------------------------------------------------------------

- Der letzte offene Sim-Bedienpfad ist jetzt produktiv im Hub verankert, ohne einen zweiten Replay-Kanal neben dem bestehenden Sessionvertrag einzufuehren.
- `novapolis-sim/Main.tscn` fuehrt dafuer einen eigenen `HubReplayPanel`-Block mit Checkpoint-Auswahl sowie `Replay Sync`- und `Resume-Anker`-Buttons; `novapolis-sim/scripts/Main.gd` laedt neben dem Session-Snapshot jetzt auch explizit `GET /session/{session_id}/replay`, zeigt Manifestzaehler und Pfade an und wendet den ausgewaehlten Resume-Anker auf Slot- und Logansicht an.
- Die statische Pruefung bleibt gruen (`get_errors` fuer `Main.gd` und `Main.tscn` ohne Befund), der kanonische Godot-Verifier endet mit `EXITCODE=0`, und der gezielte Session-/Replay-Testscope `novapolis_agent/tests/test_api_sim_state.py` plus `novapolis_agent/tests/tests_sim_api.py` endet ebenfalls mit `EXITCODE=0`. Das Sim-Board steht damit jetzt bei `offen: 0`.

Sim Replay/Resume: Client-Luecke vor dem Fixlauf konkret eingegrenzt (2026-04-14 12:09)
-------------------------------------------------------------------------------

- Der noch offene Sim-Punkt ist jetzt auf eine konkrete Client-Luecke eingegrenzt statt auf einen diffusen Folgewunsch.
- `novapolis_agent/app/api/sim.py` stellt den benoetigten Vertrag bereits bereit: `GET /session/{session_id}` liefert den aktuellen Sessionstand, `GET /session/{session_id}/replay` den Replay-Manifestpfad inklusive `resume_checkpoint_id`, `checkpoints`, `artifact_paths` und Event-Zaehlern.
- `novapolis-sim/scripts/Main.gd` ruft derzeit nur `_request_live_session_state()` und zeigt `resume_checkpoint_id` lediglich ueber `rp_replay_seed_label`; genau diese fehlende Client-Nutzung des bestehenden Replay-Endpunkts wird im naechsten Schritt geschlossen.

Sim UI: Hub-Reset jetzt lokal mit Godot 4.6.1 verifiziert (2026-04-14 12:03)
-----------------------------------------------------------------------------

- Der Sim-Hub ist auf User-Anforderung sichtbar neu aufgesetzt. `novapolis-sim/Main.tscn` fuehrt eigene Shell-Zonen fuer Top-Band, Live-Stage, Operations-Spalte und Telemetrieband sowie neue Panel-Stile statt der frueheren losen Hintergrundflaechen.
- `novapolis-sim/scripts/Main.gd` schaltet den Hub standardmaessig auf den neuen Responsive-Pfad, fuehrt Hilfsrechtecke fuer Stage und Ops ein und verteilt Topbar, Buttons, Chat, Config und Telemetrie jetzt ueber wenige Hauptbereiche statt ueber die alte Sammellogik aus vielen Einzelkoordinaten.
- Die statische Validierung bleibt gruen (`get_errors` ohne Befund fuer `Main.gd` und `Main.tscn`), und der kanonische Verifier `res://scripts/verify_sim.gd` liefert mit einer lokal laufenden Godot-4.6.1-Binary jetzt `SIM_VERIFY: OK` bei `EXITCODE=0`. `todo.sim.md` schliesst den UI-Reset damit; offen bleibt im Sim-Board nur noch Replay-/Resume.

Agent Coverage: Restwelle fuer chat_helpers, main und providers geschlossen (2026-04-14 11:15)
-------------------------------------------------------------------------------------------

- Die offene Coverage-Welle im Agent-Modul ist jetzt ueber minimale Testergaenzungen geschlossen, ohne Produktcode oder API-Vertraege umzubauen.
- Neue Edge-Tests decken die restlichen Coercion-/Omit-Pfade in `app/api/chat_helpers.py`, die TTS-Cache-Hit-/Snapshot-Helfer in `app/main.py` sowie Platzhalter-Provider und den sanitisierten Sessionpfad in `app/tts/providers.py` ab.
- Der breite Fokuslauf bestaetigt `app/api/chat_helpers.py = 100%`, `app/main.py = 98%`, `app/tts/providers.py = 96%`; der kanonische Wrapper `scripts/run_pytest_coverage.py --fail-under 80` bleibt anschliessend mit `615 passed` und `Total coverage: 94.92%` PASS. `todo.agent-board.md` und `todo.index.md` fuehren Agent damit wieder auf `offen: 0`.

Agent Coverage: Offenen Restpunkt vor dem Fixlauf auf konkrete Zweige eingegrenzt (2026-04-14 11:06)
-----------------------------------------------------------------------------------------------

- Die offene Coverage-Welle im Agent-Board ist vor der eigentlichen Mutation auf konkrete Restpfade eingegrenzt, statt als pauschaler Sammelpunkt offen zu bleiben.
- `app/api/chat_helpers.py` haelt seine Restluecken vor allem in Coercion-/Clamp-Kombinationen von `normalize_ollama_options()`, `app/main.py` in den Cache-/Cleanup-Helfern fuer TTS, und `app/tts/providers.py` in Platzhalter-, Decode- und sessionlosen Artefakt-Fallbacks.
- Das Agent-Board und `todo.index.md` fuehren denselben evidenzbasierten Zuschnitt jetzt vor dem naechsten Testlauf, damit der folgende Fixlauf minimal auf neue Tests statt auf Produktpfad-Umbauten begrenzt bleibt.

Dev UX: Terminal-Heartbeat fuer lange Testlaeufe eingezogen (2026-04-10 13:36)
-------------------------------------------------------------------------

- Lange Testlaeufe ueber `scripts/run_pytest_coverage.py`, `scripts/tests_pytest_root.py` und den Pytest-Schritt in `scripts/run_checks_and_report.py` zeigen jetzt einen sichtbaren Heartbeat im Terminal statt ueber laengere Strecken komplett still zu bleiben.
- Der neue Helfer `scripts/terminal_progress.py` streamt vorhandene Prozessausgabe weiter, puffert sie gleichzeitig fuer Logs/Receipts und schreibt in stillen Phasen periodisch Statuszeilen wie Laufzeit, Ausgabezeilen und Zeit seit der letzten Aktivitaet.
- Der Effekt ist bewusst minimalinvasiv: keine neue TUI, kein Umbau des Pytest-Aufrufs, sondern nur sichtbare Lebenszeichen fuer Menschen, wenn ein Testlauf laenger arbeitet als der letzte sichtbare Output vermuten laesst.

Dev Hygiene: runpy-Warnings im kanonischen Coverage-Pfad an der Ursache beseitigt (2026-04-10 05:16)
-----------------------------------------------------------------------------------------------

- Die vier bekannten `RuntimeWarning: ... found in sys.modules after import of package 'scripts'` kamen aus Edge-Tests, die denselben `scripts.*`-Modulnamen nach einem Vorimport noch einmal per `runpy.run_module(..., run_name="__main__")` starteten. Das war eine echte Importzustands-Kollision zwischen Vorimport und CLI-Simulation, kein Wrapper- oder Coverage-Fehler.
- `novapolis_agent/tests/scripts/test_open_latest_summary_edges.py`, `test_run_text_rpg_reference_session_edges.py`, `test_summarize_gm_eval_kpis_edges.py` und `test_validate_eval_datasets_edges.py` fuehren die betroffenen CLI-Pfade jetzt ueber den realen Skriptpfad per `runpy.run_path(..., run_name="__main__")` aus. Damit bleibt der CLI-Beleg erhalten, ohne dass `runpy` ein bereits geladenes `scripts.*`-Modul erneut als `__main__` re-exekutieren muss.
- Der gezielte Testblock ist gruen, und der kanonische Wrapper-Lauf `.tmp/results/reports/pytest_coverage_postflight_20260410_051125.md` bestaetigt `596 passed`, `returncode=0`, `Total coverage: 93.66%` sowie `warnings=0` fuer diese Klasse; `todo.dev.md` und `todo.index.md` fuehren Dev damit wieder auf `offen: 0`.

RP/Planning: Slice-2-Handover fachlich bis `slot 35` ausgebaut (2026-04-10 00:11)
-------------------------------------------------------------------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md` fuehrt den ersten fachlichen Ausbau hinter `slot 30` jetzt als vierte Kampagnenstufe. Der Pfad bleibt auf `D5`, `C6`, `G7`, `E2` und `F1` begrenzt und nutzt denselben Resume-, Reveal- und Artefaktrahmen wie `Text-RPG Slice 2 Handover v1`.
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` und `text-rpg-product-gate-v1.ssot.md` verweisen im selben Lauf auf die neue RP-SSOT; das RP-Board fuehrt den Handover-Punkt damit als geschlossen und der TODO-Index zieht den RP-Open-Count wieder auf `0`.
- Offen bleiben nach diesem Lauf nur die Dev-, Agent- und Sim-Folgearbeiten; der RP-Pfad selbst benoetigt fuer Slice 2 keinen freien Platzhalter mehr.

Slice 2 Handover: Gemeinsame SSOT hinter `slot 30` eingezogen (2026-04-10 00:11)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` fixiert jetzt den gemeinsamen Namen, den Session-/Artefaktvertrag und die Modulrollen fuer den Folgepfad hinter `slot 30`; Root, Product Gate und Agent-Runbook nutzen damit denselben Handover statt freier Folgebezeichnungen.
- `todo.root.md` fuehrt den Root-Punkt damit als geschlossen, waehrend `todo.rp.md` und `todo.sim.md` ihre offenen Folgearbeiten explizit unter denselben Handover stellen; `todo.index.md` spiegelt den neuen gemeinsamen Anker im Root-/RP-/Sim-Status.
- Der Handover selbst fuehrt bewusst noch keine neue Runtime oder neuen RP-Slot aus; offen bleiben die fachliche Ausarbeitung `slot 31-35`, der Sim-Resume-Bedienpfad und spaetere Agent-Gate-/Referenz-Erweiterungen auf demselben Vertragsrahmen.

Workspace Review: Neue Folgepunkte fuer alle aktiven TODO-Boards angelegt (2026-04-09 23:45)
------------------------------------------------------------------------------------------

- Der aktuelle Workspace-Scan leitet neue offene Punkte jetzt direkt aus der belegten Istlage ab statt aus pauschaler Wunschliste: Dev fuehrt die vier `runpy`-Warnings aus `.tmp/results/reports/pytest_coverage_postflight_20260409_232603.md` als Hygiene-Rest, Agent die naechste Coverage-Welle fuer `app/api/chat_helpers.py` (`89%`), `app/main.py` (`90%`) und `app/tts/providers.py` (`87%`).
- RP fuehrt den naechsten belegten Ausbau hinter `slot 30`, weil `novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md` im Abschnitt `Weiterer Ausbau` explizit `slot 31-35` oder eine modulare Episode fordert; Sim fuehrt einen Replay-/Resume-UI-Punkt, weil `novapolis-sim/scripts/Main.gd` `resume_checkpoint_id` derzeit nur als Label zeigt und keinen sichtbaren Replay-Endpunktpfad nutzt.
- `todo.root.md`, `todo.dev.md`, `todo.agent-board.md`, `todo.rp.md`, `todo.sim.md`, `todo.index.md` und `WORKSPACE_STATUS.md` sind im selben Lauf auf diesen neuen Folgepfad synchronisiert.

Agent Coverage: Letzten Low-Coverage-Rest geschlossen und Wrapper-CWD gehärtet (2026-04-09 23:33)
-----------------------------------------------------------------------------------------------

- `novapolis_agent/tests/test_content_management_edges.py` deckt jetzt den erfolgreichen `_SettingsProxy.__setattr__`-Pfad, den erlaubten `apply_pre()`-No-Op unter aktiven Policies und den `apply_post()`-Bypass fuer `mode="unrestricted"`; damit schliesst `novapolis_agent/app/core/content_management.py` die letzten drei offenen Zeilen.
- `novapolis_agent/scripts/validate_eval_datasets.py` nutzt seine Default-Dataset- und Suite-Config-Pfade jetzt skriptrelativ statt cwd-abhaengig. Ausloeser war der kanonische Coverage-Wrapper im Agent-CWD, der zuvor am Test `test_main_covers_default_patterns_read_fail_duplicate_id_strict_and_missing_id_strict` mit `No dataset files found.` scheiterte.
- Die fokussierte Nachmessung zieht `run_text_rpg_reference_session.py`, `validate_eval_datasets.py`, `summarize_gm_eval_kpis.py`, `content_management.py` und `tts_models.py` jeweils auf `100%`; der anschliessende Wrapper-Lauf `.tmp/results/reports/pytest_coverage_postflight_20260409_232603.md` ist mit `596 passed`, `returncode=0` und `Total coverage: 93.73%` PASS.

CPU Schonmodus: Gemeinsamen Wrapper fuer schwere Tasklaeufe eingezogen (2026-04-09 17:34)
-----------------------------------------------------------------------------------------

- `scripts/run_with_cpu_limit.py` fuehrt schwere Python-Aufrufe jetzt ueber einen kleinen CPU-Slice statt frei ueber alle logischen Prozessoren: Unter Windows setzt der Wrapper CPU-Affinität, `below_normal`-Prioritaet und konservative Thread-Umgebungsvariablen; ohne Override nutzt er auf dem lokalen `AMD Ryzen 5 3600X` mit `12` Threads automatisch `4` logische CPUs.
- `.vscode/tasks.json` haengt Root-Pytest, Coverage, Full-Check, den Text-RPG-Produktlauf sowie die relevanten Eval-/Validierungslaeufe an denselben Schonpfad, damit Taskverhalten und Direktaufruf nicht auseinanderdriften.
- `novapolis_agent/tests/scripts/test_run_with_cpu_limit.py` deckt Default-Sizing, Env-Begrenzung und den echten Child-Spawn-Pfad gegen Regression ab. Die direkte Probe `scripts/run_with_cpu_limit.py -- ... -c "import os; ..."` bestaetigt im Kindprozess `NVP_CPU_LIMIT_ACTIVE=4`, `OMP_NUM_THREADS=4` und `TOKENIZERS_PARALLELISM=false`.

GM Vertrag: Eval-Hinweisturn entkoppelt Strict-RPG-Rebuilder nicht mehr (2026-04-09 12:20)
-------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/chat.py` waehlt fuer Strict-RPG-Hint und Rebuilder jetzt nicht mehr blind den letzten Userturn, sondern den letzten Userturn mit echtem Vertragsmuster `Szene:/Konsequenz:/Optionen:/State_Patches:` und ignoriert den von `novapolis_agent/scripts/run_eval.py` angehaengten Eval-Hinweisturn `Hinweis: Verwende diese Begriffe ...`.
- `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt den Root Cause jetzt mit zwei gezielten Regressionen ab: Hint-Injektion und Rebuilder muessen auch dann greifen, wenn der Eval-Hinweis als zweiter Userturn hinter dem eigentlichen Prompt haengt.
- Der gezielte Suite-Lauf `novapolis_agent/eval/results/results_20260409_1217_gm_session.jsonl` ist jetzt `4/4`, und der kanonische End-to-End-Lauf `.tmp/results/reports/text_rpg_product_gate_20260409_121807.md` ist wieder PASS; die zugehoerige KPI-Summary `.tmp/results/reports/gm_session_kpi_summary_20260409_121807.md` zeigt keine Blocker und keine Beobachtungen mehr.

GM Vertrag: Frischer Product-Gate-Lauf isoliert den Rest auf KPI-Ebene (2026-04-09 09:58)
-----------------------------------------------------------------------------------------

- `.tmp/results/reports/text_rpg_product_gate_20260409_095602.md` ist jetzt der frische End-to-End-Beleg nach dem Vier-Sektions-Rebuilder: `checks_full`, API-/Streaming-Tests, Referenz-Session, Sim-Assets, Runtime-Preflight und `gm_session_eval` laufen alle gruen durch.
- Der verbleibende Product-Fail kommt ausschliesslich aus `.tmp/results/reports/gm_session_kpi_summary_20260409_095602.md` mit `Success: 2/4` und `Severity: blocker`.
- Blocker bleibt `gm.session.reveal-discipline.v1` auf fehlendem `Geraeusch` und `Entscheidung`; `gm.session.option-quality.v1` bleibt Beobachtung auf den fehlenden exakten Labels `vorsichtige`, `riskante` und `soziale`.

GM Vertrag: Finalen Vier-Sektions-Rebuilder fuer Reveal-Anker und Optionen eingezogen (2026-04-09 09:48)
------------------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/chat.py` rekonstruiert fuer strikte Text-RPG-Formatprompts den finalen Antworttext jetzt kanonisch aus `Szene:`, `Konsequenz:`, `Optionen:` und `State_Patches:` statt nur punktuell fehlende Teilstuecke anzuhängen.
- Der neue Rebuilder ersetzt umlautete Aliasformen wieder durch exakte ASCII-Pflichtanker wie `Geraeusch`, normalisiert inline ausgespielte Optionen auf echte `1./2./3.`-Zeilen und setzt fehlende `State_Patches:`-Segmente deterministisch auf `[]`.
- `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt den neuen Pfad jetzt zusaetzlich fuer inline `Optionen:` ohne State-Patches und fuer den Reveal-Fall mit `Geräusch`-Drift ab; der fokussierte Pytest-Lauf ist mit `3 passed` gruen.
- Ein frischer Product-Gate-Lauf wurde in diesem Schritt bewusst noch nicht nachgezogen; der letzte belegte Messstand bleibt deshalb bei `.tmp/results/reports/text_rpg_product_gate_20260409_083707.md` und `.tmp/results/reports/gm_session_kpi_summary_20260409_083707.md` mit `3/4`.

GM Vertrag: Literal-Anker-Fixlauf drueckt den Rest auf einen Reveal-Fall (2026-04-09 08:39)
-------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/chat.py` zieht den strikten Text-RPG-Vertrag jetzt nicht mehr nur ueber Systemhinweise, sondern repariert fehlende Sichtbarkeitsanker und Optionslabels nach der Modellantwort deterministisch an der finalen Ausgabestelle.
- `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt den neuen Reparaturpfad fuer fehlende Slot-/Turn-Anker, Optionslabel und den Reveal-Fall gezielt ab; der fokussierte Pytest-Lauf bleibt gruen, Ruff ebenfalls.
- Der belegte Effekt liegt im aktuellen Produktlauf `.tmp/results/reports/text_rpg_product_gate_20260409_083707.md`: `gm.session.continuity.v1` und `gm.session.option-quality.v1` sind jetzt gruen, die KPI-Summary `.tmp/results/reports/gm_session_kpi_summary_20260409_083707.md` steht bei `Success: 3/4`, und als einziger Blocker bleibt `gm.session.reveal-discipline.v1` mit den fehlenden Literalankern `Geraeusch`, `Druck` und `Entscheidung`.

Product Gate: Wrapper-Haertung und blocker-treuer Gate-Status nachgezogen (2026-04-09 03:29)
----------------------------------------------------------------------------------------------

- `scripts/run_text_rpg_product_gate.py` loest den Runtime-Target-Import jetzt robust ueber Repo-/Modulpfade, setzt fuer Unterprozesse `PYTHONIOENCODING=utf-8` plus `PYTHONUTF8=1` und wertet die GM-KPI-Summary jetzt als harte Gate-Quelle aus.
- Dadurch scheitert das Product Gate nicht mehr an Ruff/Black-Drift, Importfehlern oder `cp1252`-Ausgaben aus `run_eval.py`, sondern am fachlich richtigen Signal `gm_session summary classified: blocker`.
- Die frische Nachmessung `results_20260409_0312_gm_compare_qwen_sweep_n256.jsonl` kommt nur auf `1/4`; der finale Gate-Lauf `.tmp/results/reports/text_rpg_product_gate_20260409_032736.md` endet bei `Success: 2/4` in der KPI-Summary mit Blockern `slot-03`/`turn-0007` sowie `Geraeusch`.

GM Vertrag: Strikten Antwortvertrag im produktiven Chat-Pfad nachgezogen (2026-04-09 03:05)
-------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/chat.py` fuehrt fuer explizite Text-RPG-Formatprompts jetzt einen engeren Systemhinweis: exakt vier Abschnittstitel, genau drei nummerierte Optionen, keine zusaetzlichen sichtbaren Ueberschriften und ein verpflichtendes `State_Patches`-Segment.
- Der Hinweis extrahiert sichtbare Prompt-Anker wie `slot-03`, `turn-0007`, `Scannerkarte`, `Geraeusch`, `Druck` und `Entscheidung` separat und haelt sie sichtbar stabil; verdeckte Begriffe wie `verdeckter Auftrag` werden zugleich explizit als nicht sichtbarer Antwortinhalt markiert.
- `novapolis_agent/tests/test_api_chat_internal_branches.py` deckt denselben Vertrag jetzt sowohl fuer `process_chat_request()` als auch fuer `stream_chat_request()` gezielt ab; der fokussierte Pytest-Lauf ist PASS.

GM Payload: Kontextnotizen im deaktivierten Zustand wirklich abgeschaltet (2026-04-08 23:08)
------------------------------------------------------------------------------------------

- `novapolis_agent/app/api/chat.py` beendet `_resolve_context_notes()` jetzt sofort, wenn `CONTEXT_NOTES_ENABLED` nicht aktiv ist; gefundene lokale Notizdateien duerfen den produktiven `/chat`-Payload damit nicht mehr stillschweigend vergroessern.
- Ausloeser war die Live-Repro fuer `gm.session.continuity.v1`: Der extrahierte Payload enthielt trotz deaktiviertem Flag einen dritten Systemturn `[Kontext-Notizen]`, und genau der volle Payload kippte in der Direktprobe wieder in Timeouts, waehrend der reduzierte `system+user`-Pfad noch antwortete.
- Der neue Regressionstest `test_process_chat_request_skips_context_notes_when_disabled` in `novapolis_agent/tests/test_api_chat_internal_branches.py` ist PASS; die anschliessende Live-Payload-Pruefung zeigt nur noch zwei Nachrichten (`system`, `user`) ohne Kontextturn.

Product Gate: GM-Restpfad im Produktlauf mit Preflight und Fehlklassifikation gehaertet (2026-04-08 22:38)
-----------------------------------------------------------------------------------------------------------

- `scripts/run_text_rpg_product_gate.py` fuehrt vor `gm_session_eval` jetzt einen expliziten Schritt `gm_runtime_preflight` gegen den aktiven Ollama-Host samt `/api/tags`-Pruefung und Modellnachweis aus; fehlende Runtime und fehlendes Modell brechen damit frueh und sichtbar ab.
- Der Produktlauf klassifiziert spaetere GM-Resultate jetzt getrennt als `runtime_unreachable`, `model_missing`, `ollama_http_500` und `gm_timeout_504` statt nur als generisches `step failed: gm_session_eval`.
- Ausloeser war der frische Re-Run `novapolis_agent/eval/results/results_20260408_2150_gm_session.jsonl`: `gm.session.continuity.v1` schlug mit direktem Ollama-500 fehl, zwei weitere Faelle mit `504 Gateway Timeout` im Agent-/ASGI-Pfad, waehrend der lokale Listener selbst auf `127.0.0.1:11434` fuer `qwen2.5:7b` und `llama3.1:8b` erreichbar blieb.
- Der gezielte Unit-Test `novapolis_agent/tests/scripts/test_run_text_rpg_product_gate.py` deckt jetzt sowohl Preflight als auch Klassifikation ab und ist mit vier Tests PASS; Ruff und `black --check` sind fuer die geaenderten Dateien ebenfalls gruen.

Product Gate: Reproduzierbaren Text-RPG-Verbundlauf mit Referenz-Session verankert (2026-04-08 14:22)
-----------------------------------------------------------------------------------------------------

- `scripts/run_text_rpg_product_gate.py` fuehrt `checks_full`, `pytest_api_streaming`, Referenz-Session, Sim-Offline-Check, `gm_session_eval` und die direkte KPI-Summary jetzt in einem kanonischen Root-Lauf aus; `.vscode/tasks.json` fuehrt denselben Verbund ueber `Checks: text-rpg product gate` und `Tests: text-rpg reference session`.
- `novapolis_agent/scripts/run_text_rpg_reference_session.py` und `novapolis_agent/eval/config/text_rpg_reference_session.v1.json` fixieren einen dreistufigen D5/`slot-03..05`-Referenzfall; der Verifikationslauf ist PASS und bestaetigt `savegame.json`, `world_log.jsonl`, `pc_log.jsonl` und `replay_manifest.json` samt Endzustand `scene-d5-nordlinie`, `slot-05`, `turn-0009` unter `.tmp/results/reports/text_rpg_reference_session_verify.md`.
- `novapolis_agent/scripts/summarize_gm_eval_kpis.py` akzeptiert explizite Resultatdateien jetzt sauber ohne Pattern-Fallback; dadurch bindet der Verbundlauf die KPI-Summary an genau `novapolis_agent/eval/results/results_20260408_1422_gm_session.jsonl` statt an historische Altlaeufe.
- Der gezielte Pytest-Block fuer die neuen Scriptpfade ist PASS, der anschliessende Full-Check bleibt komplett gruen (`.tmp/results/reports/checks_report_20260408_141908.md`), und der Gesamtbericht `.tmp/results/reports/text_rpg_product_gate_verify.md` zeigt nur noch `gm_session_eval` als FAIL.
- Der verbleibende Blocker ist kein Gate-Drift mehr, sondern der lokal nicht erreichbare Modellruntime im produktiven Chat-Pfad (`httpx.ConnectError: All connection attempts failed`); `.tmp/results/reports/gm_session_kpi_summary_20260408_142100.md` spiegelt denselben Befund mit `Severity: blocker`, `Records: 4` und `Success: 0`.

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
