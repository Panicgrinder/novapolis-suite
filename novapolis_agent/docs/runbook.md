---
stand: 2026-04-10 13:22
update: Runbook fuehrt jetzt auch den gemeinsamen Folgeanker `Text-RPG Slice 2 Handover v1` hinter slot 30.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=FAIL; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260410_131501.md
---

Novapolis Agent Runbook (Ist-Stand)
===================================

Ziel
----

- Betriebsanleitung fuer lokalen Betrieb und Qualitaetsgates auf Basis des aktuell umgesetzten Stands.
- Keine Produktivzusagen ohne Evidenz; alle Aussagen orientieren sich an verifizierbaren Laufartefakten.

Runtime-Start
-------------

1. Python-Umgebung aktivieren:

```powershell
.\.venv\Scripts\activate
```

2. API starten (Agent-Modul-CWD):

```powershell
Set-Location .\novapolis_agent
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

3. Health/Docs pruefen:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

Project Context Bridge (Phase 1 / MVP-Start)
--------------------------------------------

Ziel:

- Bestehenden Chat-Flow um einen reproduzierbaren, kanonischen Projektkontext erweitern.
- Keine neue Parallelarchitektur; Nutzung der vorhandenen RAG-/Kontextpfade.

1. Kontextindex aus kanonischer Quellenliste bauen (Repo-Root):

```powershell
Set-Location ..
.\.venv\Scripts\python.exe novapolis_agent\scripts\build_project_context_index.py
```

2. API mit aktiviertem Kontextmodus starten:

```powershell
Set-Location .\novapolis_agent
$env:RAG_ON = "true"
$env:RAG_INDEX_PATH = "novapolis_agent/eval/results/rag/context_bridge.index.json"
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

3. Chat-Aufruf bleibt unveraendert ueber `/chat` (optional mit `profile_id=context_bridge`):

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/chat" -Method Post -ContentType "application/json" -Body '{"messages":[{"role":"user","content":"Gib mir einen kompakten Projektstatus fuer Novapolis mit Quellenbezug."}],"profile_id":"context_bridge"}'
```

Hinweise:

- Quellenmanifest: `novapolis_agent/eval/config/context.bridge.sources.json`
- Build-Skript: `novapolis_agent/scripts/build_project_context_index.py`
- SSOT zur Planung/Phasen: `novapolis-dev/docs/process/project-context-bridge.ssot.md`

Text-RPG Sessionvertrag v1
-------------------------

Der kanonische Vertragsanker fuer den ersten spielbaren Slice liegt in `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`.

Verbindliche Kernobjekte:

- `campaign_id`
- `session_id`
- `scene_id`
- `slot_id`
- `turn_id`
- `state_patches`
- Log-Kanaele `world|pc|ally|sys`

Aktueller Wahrheitsrahmen:

- Der bestehende Runtime-Pfad bleibt vorerst der vorhandene `/chat`-Flow mit optionaler `session_id`.
- Der Vollvertrag ist bereits festgezogen; `/chat` fuehrt jetzt denselben Contract-Block fuer Session, Slot, Status und Replay-Checkpoint wie der Replay-Pfad, auch wenn der Szenetext weiter in `content` bleibt.
- Neue Session- oder Replay-Artefakte muessen sich an diese SSOT haengen, nicht an freie Nebenformate.

Text-RPG Product Gate v1
------------------------

Der kanonische Gate-Rahmen liegt in `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`.

Aktueller operativer Wrapper-Task:

1. `Checks: text-rpg product gate`

Der Wrapper fuehrt intern denselben Gate-Block aus:

1. `Checks: full`
2. `Tests: pytest (api+streaming)`
3. `Tests: text-rpg reference session`
4. `Checks: sim epoch assets`
5. `Eval: suite gm_session (12, asgi)`
6. `Eval: summarize gm session KPIs`

Die Diagnose-Tasks bleiben zusaetzlich einzeln verfuegbar; der verbindliche Produktpfad laeuft aber ueber denselben Wrapper.

Hard-Fail-Klassen laut SSOT:

- OpenAPI-/Schema-Drift gegen den Sessionvertrag
- fehlende oder spaeter widerspruechliche `world_log`-/`pc_log`-/`state_patches`-Artefakte in der festen Referenz-Session
- Slot- oder Replay-Widersprueche zwischen Agent- und Sim-Pfad
- nicht erreichbare lokale Modellruntime fuer den `gm_session`-Eval-Teil

Text-RPG Slice 2 Handover v1
----------------------------

Der gemeinsame Folgeanker hinter `slot 30` liegt in `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`.

Operative Lesart:

- Der erste Slice bleibt produktiv bis `slot 30` geschlossen; der naechste Ausbau hinter diesem Punkt darf im Agent-Scope keinen freien Zweitnamen bekommen.
- Neue Referenzfaelle, Gate-Erweiterungen oder Resume-Checks hinter `slot 30` muessen denselben Session- und Artefaktvertrag (`savegame.json`, `world_log`, `pc_log`, `replay_manifest.json`, `resume_checkpoint_id`) weiterverwenden.
- Die offene Sim-Folgearbeit haengt explizit an diesem Handover: `resume_checkpoint_id` und `replay_manifest` bleiben damit nicht nur Runtime-Daten, sondern der operative Wiederanlaufanker fuer denselben Folgepfad.

Feste Referenz-Session
----------------------

Der deterministische Artefaktbeleg fuer den Slice liegt unter `novapolis_agent/eval/config/text_rpg_reference_session.v1.json`.

Direkter Einzelaufruf:

```powershell
Set-Location ..
.\.venv\Scripts\python.exe novapolis_agent\scripts\run_text_rpg_reference_session.py --repo-root .
```

Der Lauf schreibt einen JSON- und Markdown-Report unter `.tmp/results/reports/`, erzeugt denselben Session-Artefaktkern (`savegame.json`, `world_log.jsonl`, `pc_log.jsonl`, `replay_manifest.json`) in einem temporaeren Store unter `.tmp/results/reference_sessions/` und validiert die erwarteten Slot-/Turn-/Artefaktzaehler gegen die Referenzdatei.

Operative Lesart:

- Die Referenz-Session ist kein Ersatz fuer den produktiven Chat-Lauf, sondern ein deterministischer Vertragsanker fuer Replay- und Artefaktpruefung.
- Der `gm_session`-Eval-Teil prueft zusaetzlich den produktiven Modellpfad; ohne erreichbare lokale Modellruntime bleibt dieser Teil weiterhin ein Hard-Fail des Gesamt-Gates.

Lokale Runtime-Baseline
-----------------------

Der kanonische lokale Runtime-Pfad bleibt `Ollama`.

Bevorzugtes Baseline-Modell fuer den aktuellen Slice auf 8-GB-VRAM-Systemen:

- `qwen2.5:7b`

Vergleichs- oder Fallback-Kandidaten:

- `llama3.1:8b`

Operative Konsequenz:

- neue lokale Setups, Beispiel-Umgebungen und Default-Fallbacks sollen `qwen2.5:7b` verwenden,
- spaetere Modellvergleiche duerfen davon abweichen, aber nur bewusst und nicht still ueber historische Defaults.

Minimaler Spielleiter-Orchestrator-Hook
---------------------------------------

Der erste Runtime-Schritt fuer den offenen Spielleiter-Orchestrator bleibt auf den vorhandenen Endpunkten `/chat` und `/chat/stream`.

Aktive opt-in Felder in `ChatRequest.options`:

- `orchestrator_enabled`
- `campaign_id`
- `scene_id`
- `slot_id`
- `turn_id`
- `retrieval_query`
- `public_context`
- `hidden_context`
- `scheduler_hints`
- `state_patch_hints`

Aktiver Contract-Block in `ChatResponse`:

- `contract_version`
- `session_id`
- `campaign_id`
- `scene_id`
- `slot_id`
- `turn_id`
- `session_status`
- `replay_checkpoint_id`
- `log_channels`

Operatives Verhalten des Hooks:

- der bestehende Chat-Pfad bleibt erhalten,
- der Hook injiziert einen kontrollierten Systemblock fuer Sitzungsrahmen, PC-Sicht, Hidden-Context, Scheduler-Hinweise und Patch-Ziele,
- bei vorhandenem Session-Store fuehrt derselbe Systemblock jetzt zusaetzlich einen internen Abschnitt `[Session-Stand intern]` mit Resume-Checkpoint, recent `pc_log` und recent `state_patches`,
- bei aktivem Orchestrator werden Kontextnotizen, ein optionaler `retrieval_query` und RP-/Projekt-Retrieval in denselben Spielleiter-Block gefaltet statt als lose Zusatzbloecke daneben zu stehen,
- `hidden_context` bleibt explizit nur interner Steuerkontext und ist nicht fuer direkte PC-Ausgabe gedacht,
- Antworten mit Abschnitt `State_Patches:` werden auf dem Rueckweg geparst und zusammen mit dem erzeugten Folgezug als `pc_log` plus normalisierte `state_patches` in denselben Session-Store geschrieben,
- Projektkontext-Bruecke, Kontextnotizen und RAG bleiben derselbe bestehende Unterbau; getrennte `[Kontext-Notizen]`-/`[RAG]`-Bloecke laufen weiter nur fuer den nicht orchestrierten Standardpfad.

Minimaler Sim-Live-Client (Hub)
-------------------------------

- `novapolis-sim/scripts/Main.gd` nutzt das bestehende Hub-Chat-Panel jetzt als minimalen Live-Spielclient fuer denselben Text-RPG-Pfad,
- der Client sendet `session_id`, `campaign_id`, `scene_id`, `slot_id`, `turn_id`, `public_context`, `state_patch_hints` und `retrieval_query` an `/chat`,
- eingehende Antworten werden heuristisch in `Szene`, `Konsequenz`, `Optionen` und `State_Patches` zerlegt und als laufender Sessionstand im Panel gehalten,
- der Produktpfad bleibt bewusst minimal: die Session-/Replay-Bridge lebt jetzt separat in der Sim-API, waehrend Chat-Orchestrierung und Scheduler-Rueckkopplung weiter locker gekoppelt bleiben.

Session- und Replay-Bruecke
---------------------------

Die minimal belastbare Persistenz fuer den ersten Slice liegt jetzt in `novapolis_agent/app/api/sim.py`.

Artefaktkern pro Session:

- `novapolis_agent/tmp/sim_sessions/<session_id>/savegame.json`
- `novapolis_agent/tmp/sim_sessions/<session_id>/world_log.jsonl`
- `novapolis_agent/tmp/sim_sessions/<session_id>/pc_log.jsonl`
- `novapolis_agent/tmp/sim_sessions/<session_id>/replay_manifest.json`

Aktive Endpunkte:

- `PUT /session/{session_id}`
  - schreibt oder erweitert den Sessionstand,
  - nimmt `contract_version`, `session_status`, `campaign_id`, `scene_id`, `slot_id`, `slot_index`, `turn_id`, `seed`, `world_state`, `state_patches`, `world_log` und `pc_log` an,
  - validiert den kanonischen Vertragswert `text_rpg_session_v1` und den Sessionstatus,
  - normalisiert Logeintraege und `state_patches` auf denselben Session-/Slot-/Tick-Kontext.
- `GET /session/{session_id}`
  - liefert den aktuellen Resume-Stand inklusive `contract_version`, `session_status`, `resume_checkpoint_id`, Checkpoint-Liste, `world_state`, `state_patches`, `world_log` und `pc_log`.
- `GET /session/{session_id}/replay`
  - liefert den Replay-Manifestkern mit demselben `contract_version`-/`session_status`-Block, Artefaktpfaden und Event-/Patch-Zaehlern fuer spaetere Hub- oder Epoch-Exporte.

Operative Lesart:

- Die Bruecke ersetzt noch nicht den Produktpfad ueber `/chat`, sondern stabilisiert den Artefaktkern darunter.
- `/chat` und die Session-API fuehren jetzt denselben Contract-Rahmen fuer Session, Slot, Status und Replay-Checkpoint; der Orchestrator zieht den Session-Snapshot intern ein und schreibt den Folgezug wieder in denselben Store zurueck.
- `world_log` und `pc_log` bleiben bewusst Sim-kompatible JSONL-Dateien statt eines neuen Nebenformats.
- Resume-Punkte laufen zunaechst ueber `turn_id`, sonst ueber einen Tick-basierten Fallback `tick-XXXX`.

Noch offen:

- keine echte Scheduler-Engine,
- keine automatische Ableitung aus RP-SSOTs.

Qualitaetsgates (verbindliche Reihenfolge)
------------------------------------------

Im CWD `novapolis_agent`:

1. Lint:

```powershell
..\.venv\Scripts\python.exe -m ruff check .
..\.venv\Scripts\python.exe -m black --check .
```

2. Typen:

```powershell
..\.venv\Scripts\python.exe -m pyright -p pyrightconfig.json
..\.venv\Scripts\python.exe -m mypy --config-file mypy.ini app scripts
```

3. Tests:

```powershell
..\.venv\Scripts\python.exe -m pytest -q
```

4. Coverage (Repo-Root):

```powershell
Set-Location ..
.\.venv\Scripts\python.exe scripts/run_pytest_coverage.py --fail-under 80
```

Optional-Dependency-Profil (Spezial-CLIs)
-----------------------------------------

Leichter Konsistenzcheck fuer optionale Tool-Abhaengigkeiten (`openai`, `rich`, `pypdf`):

```powershell
Set-Location ..
.\.venv\Scripts\python.exe novapolis_agent/scripts/check_dependency_profiles.py
```

Legacy-Shim-Guard (optional)
----------------------------

Prueft, ob archivierte Legacy-Module ungewollt in produktiven Pfaden importiert werden:

```powershell
Set-Location ..
.\.venv\Scripts\python.exe novapolis_agent/scripts/check_legacy_shim_imports.py --strict
```

Artefakt-Lifecycle-Cleanup (optional)
-------------------------------------

Dry-Run fuer Eval-/Training-Artefakte mit maschinenlesbarem Report:

```powershell
Set-Location ..
.\.venv\Scripts\python.exe novapolis_agent/scripts/cleanup_artifacts.py --dry-run --keep-latest 15 --report .tmp/results/reports/artifact_lifecycle_report.json
```

RP->Eval-Datensatz bauen (optional)
-----------------------------------

Erzeugt ein RP-basiertes Eval-Paket aus `novapolis-rp/database-rp/**`:

```powershell
Set-Location ..
.\.venv\Scripts\python.exe novapolis_agent/scripts/build_eval_from_rp.py --rp-root novapolis-rp/database-rp --out novapolis_agent/eval/datasets/rp/rp_ssot_core.v1.jsonl --limit 120
```

Marathon-KPI zusammenfassen (optional)
--------------------------------------

Erzeugt board-ready KPI-Reports aus Marathon-Result-JSONL (Severity + Top-Fails + Paketverteilung):

```powershell
Set-Location ..
.\.venv\Scripts\python.exe novapolis_agent/scripts/summarize_marathon_kpis.py --pattern novapolis_agent/eval/results/results_*_marathon*.jsonl --report-json .tmp/results/reports/marathon_kpi_summary.json --report-md .tmp/results/reports/marathon_kpi_summary.md
```

Kanonischer Sim-Pruefablauf (kurz, in Reihenfolge)
--------------------------------------------------

Ziel: ein reproduzierbarer Local-Loop fuer Sim-Integritaet.

1. API-smoke (schneller Vertragscheck):

```powershell
Set-Location ..
.\.venv\Scripts\python.exe -m pytest -q novapolis_agent/tests/tests_sim_api.py::test_get_world_state_initial_values
```

2. Godot-headless Scene-Load:

```powershell
$godot = if ($env:GODOT_BIN) { $env:GODOT_BIN } else { 'godot4' }
& $godot --headless --path '.\novapolis-sim' --quit --scene res://Main.tscn
```

Hinweis (Windows):

- Wenn `godot4` nicht im PATH liegt, vor dem Aufruf einmalig setzen:

```powershell
$env:GODOT_BIN = 'C:/Tools/Godot/Godot_v4.6.1-stable_win64.exe'
```

3. Offline-Asset-Check (Epoch/Audio + Slot-Konsistenz):

```powershell
.\.venv\Scripts\python.exe scripts/check_sim_epoch_assets.py --allow-empty --check-slot-consistency
```

4. Optional: Eval-Fokuslauf (nur bei Bedarf):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --tag quality_de --checks must_include,keywords_any,keywords_at_least,not_include,regex,quality_de --packages novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl
```

Abbruchkriterium:

- Stufe 1 bis 3 muessen gruen sein, bevor weitergehende Sim-/Hub-Changes als verifiziert gelten.
- Bei aktivem `--check-slot-consistency` ist der Lauf ein HARTES FAIL bei Slot-Mismatch zwischen `world_log`/`pc_log`, bei ungueltigen Slotwerten ausserhalb `0..23` oder wenn Eintraege ohne detektierbaren Slot vorliegen.

VS Code Task-Labels (Datensatz & Training)
------------------------------------------

- `Data: curate from latest (train pack)`
- `Data: export+pack (latest results)`
- `Train: baseline LoRA (tiny-gpt2, 1-step)`

TTS Runtime-Status (wahrheitsgetreu)
------------------------------------

- Endpunkte vorhanden: `/tts/health`, `/tts/voices`, `/tts/synthesize`, `/tts/cache/stats`, `/tts/cache/cleanup`.
- Produktiver Runtime-Provider aktiv: `coqui` (HTTP-Endpunktaufruf + lokaler Artefaktpfad bei erfolgreicher Synthese).
- Weitere Provider verbleiben als Adapter-Scaffolds: `ollama`, `openai`; Testanker: `dummy`, `null`.
- Fallback-Verhalten: bei nicht verfuegbarem Runtime-Provider liefert `/tts/synthesize` kontrolliert `503` (kein Silent-Fail).
- Sicherheit und Stabilitaet aktiv: TTS-Auth, TTS-Rate-Limit, TTS-Cache (TTL/Size/Cleanup/Telemetry).
- Sessionvertrag aktiv: `/tts/synthesize` fuehrt jetzt optional `contract_version`, `session_id`, `campaign_id`, `scene_id`, `slot_id`, `turn_id` und `channel` (`world|pc|ally|sys`) auf demselben Text-RPG-Schnitt.
- Session-Anbindung aktiv: der Cache-Key enthaelt denselben Rahmen, erfolgreiche und gecachte Antworten schreiben einen sessionbezogenen TTS-Manifest-Eintrag, und Coqui-Artefakte liegen unter `novapolis_agent/outputs/tts/runtime/sessions/<session>/<channel>/...`.

TTS Build-Time-Exporter
-----------------------

- Entrypoint: `novapolis_agent/scripts/tts_export_coqui.py` (Wrapper auf `tts_coqui_export.py`).
- Beispielaufruf (`--dry-run`):

```powershell
.\.venv\Scripts\python.exe novapolis_agent\scripts\tts_export_coqui.py --input <pfad> --voice-map <pfad> --model-id <id> --dry-run
```

- Compliance-Gate aktiv: Model-Allowlist und lokale Lizenzkopie werden geprüft.

Eval-Betrieb (Suite-Trennung)
-----------------------------

Ziel: neutrale Assistenz-Evaluation und RPG-Evaluation getrennt fahren, damit Metriken nicht durch Moduskonflikte verfälscht werden.

Suite-Definition:

- `novapolis_agent/eval/config/suites.json`

Tasks:

- `Eval: suite neutral (20, asgi)`
- `Eval: suite rpg (20, asgi)`
- `Eval: suite rp_content (20, asgi)`
- `Eval: suite gm_session (12, asgi)`
- `Eval: summarize gm session KPIs`

Direkte CLI-Variante (neutral):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --packages novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/generated/neutral_101_300_generated.v1.jsonl
```

Direkte CLI-Variante (rpg):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile unrestricted --limit 20 --quiet --packages novapolis_agent/eval/datasets/rpg/rpg_21_40_fantasy.v1.jsonl --packages novapolis_agent/eval/datasets/rpg/rpg_41_60_dialog.v1.jsonl --packages novapolis_agent/eval/datasets/rpg/rpg_61_80_szenen.v1.jsonl
```

Direkte CLI-Variante (rp_content):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile unrestricted --limit 20 --quiet --packages novapolis_agent/eval/datasets/rp/rp_characters_core.v1.jsonl --packages novapolis_agent/eval/datasets/rp/rp_locations_core.v1.jsonl --packages novapolis_agent/eval/datasets/rp/rp_admin_core.v1.jsonl
```

Direkte CLI-Variante (gm_session):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile unrestricted --limit 12 --quiet --tag gm_session --checks must_include,keywords_any,keywords_at_least,not_include,regex,rpg_style --packages novapolis_agent/eval/datasets/rpg/rpg_gm_session_core.v1.jsonl
.\.venv\Scripts\python.exe novapolis_agent/scripts/summarize_gm_eval_kpis.py --pattern novapolis_agent/eval/results/results_*_gm_session*.jsonl --report-json .tmp/results/reports/gm_session_kpi_summary.json --report-md .tmp/results/reports/gm_session_kpi_summary.md
```

Interpretation:

- `neutral` bewertet primär neutrale Hilfsantworten (rpg_style sollte niedrig sein).
- `rpg` bewertet rollenspielnahe/szenische Antworten; der Lauf ist nicht direkt mit neutralen Keyword-Anforderungen vergleichbar.
- `rp_content` bewertet RP-SSOT-nahe Inhalte (Charaktere, Orte, Admin-/Lagekontexte) auf den RP-Datasetpaketen.
- `gm_session` bewertet denselben Produktpfad als Spielleiterlauf mit Session-/Slot-Fortsetzung, Reveal-Disziplin, dreifacher Optionsflaeche und lesbaren `State_Patches`.
- Fuer die RPG-Suite ist `rpg_style` bewusst aus den Checks entfernt, damit kein neutraler Stil-Malus den RPG-Lauf verfälscht.
- Die GM-Summary trennt Blocker-Faelle (`tags` enthalten `blocker`) von Beobachtungen und verweist je Fail weiter auf `item_id`, `slug`, `source_package` und `failed_checks`.

Quality-Track `quality_de` (operativ)
-------------------------------------

Ziel:

- Deutsches Antwortniveau als reproduzierbaren Zusatz-Gate im neutralen Eval-Betrieb fahren.
- `quality_de` ist ein Check-Alias und expandiert in `languagetool_quality` + `sts_relevance`.

Verpflichtung (Suite-Zuordnung):

- Suite `neutral`: enthält `quality_de` als verpflichtenden Check.
- Suite `quality_de`: dedizierte Qualitäts-Suite für fokussierte Läufe und Triage.

Schwellwerte und Begründung:

- `languagetool_quality`: PASS bei `issue_count <= 2` und `score >= 0.65`.
- `sts_relevance`: PASS bei `score >= 0.09`.
- Begründung: Die Schwellen sind absichtlich moderat gewählt, damit fachlich korrekte Kurzantworten nicht übermäßig blockiert werden, gleichzeitig aber klare Qualitäts-/Relevanz-Ausreißer zuverlässig sichtbar werden.

Tasks:

- `Eval: suite neutral (20, asgi)` (inkl. `quality_de`).
- `Eval: suite quality_de (20, asgi)` (fokussierter Qualitätslauf).

CLI-Beispiel (`quality_de`):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --tag quality_de --checks must_include,keywords_any,keywords_at_least,not_include,regex,quality_de --packages novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --tag quality_de --checks must_include,keywords_any,keywords_at_least,not_include,regex,quality_de --packages novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl
```

Laufartefakte:

- Ergebnisse landen unter `novapolis_agent/eval/results/results_<timestamp>_quality_de*.jsonl`.
- Die erste Zeile (`_meta`) dokumentiert aktive Checks (`enabled_checks`) und Overrides als technische SSOT.
- Aktueller verifizierter Stand: `quality_de_round7b` mit `20/20` sowie drei Wiederholungsläufe (`quality_de_round7b_repeat1..3`) ebenfalls `20/20`.

Dataset-Metadaten (slug/tags, YAML)
-----------------------------------

- Eval-Datasets koennen jetzt neben JSON/JSONL auch YAML (`.yaml`, `.yml`) nutzen.
- Feld `slug` wird als stabiler Identifier unterstuetzt; fehlt `id`, wird `id` aus `slug` abgeleitet (`eval-<slug>`).
- Feld `tags` (Liste von Strings) wird fuer Routing-/Heuristik-Logik verwendet.
- Eval-Resultate spiegeln `slug`, `category` und `tags` jetzt ebenfalls in `results_<timestamp>*.jsonl`, damit KPI-Reports denselben Session-Fall reproduzierbar referenzieren koennen.

Validator-Gate:

- Task: `Eval: validate datasets (slug+tags)`
- Strikter Suite-Lauf (nur Pakete aus `suites.json`): `Eval: validate suite datasets (strict)`
- CLI:

```powershell
.\.venv\Scripts\python.exe novapolis_agent\scripts\validate_eval_datasets.py
```

Strict nur auf Suiten:

```powershell
.\.venv\Scripts\python.exe novapolis_agent\scripts\validate_eval_datasets.py --strict --suite-config novapolis_agent/eval/config/suites.json --suite neutral --suite rpg --suite quality_de --suite rp_content
```

Hinweis:

- Aggregierte Dateien wie `combined_*` sind im Validator als Duplicate-Allowlist hinterlegt und blockieren damit den allgemeinen Lauf nicht.
