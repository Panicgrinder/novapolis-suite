---
stand: 2026-04-23 16:50
update: Die Sim-README fuehrt jetzt zusaetzlich den Export-Presetanker, den minimalen Vollstand und den statischen Hub-Prefs-Contract-Check als kanonische Repo-Pfade.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260423_155606.md; snapshot-lock PASS (2026-04-23 16:50)
---

Novapolis Sim
=============

Ein minimales Godot-4-Projekt zur Visualisierung des Simulationszustands aus dem Novapolis Agenten.

Verbindungstest
---------------

2025-11-10 12:12 — Verbindung zwischen Godot und dem Agent-API (`POST /world/step`) erfolgreich verifiziert. Der Headless-Verifier `res://scripts/verify_sim.gd` sowie ein lokaler Smoke-Check (`POST /world/step`) liefen durch und lieferten erwartete Antworten (z. B. `tick` und `time`). Ein Screenshot der laufenden Szene wurde als Audit-Beleg erstellt.


Aufgaben & Planung
------------------

- Aufgaben für das Simulations-Modul bitte im Board `novapolis-dev/docs/todo.sim.md` pflegen (der Index `novapolis-dev/docs/todo.index.md` dient nur der Navigation).

How to run
----------

1. Stelle sicher, dass die Python-Seite läuft:
   - In `novapolis_agent/.env` den Port setzen (`AGENT_PORT=8765` Standard).
   - Root-Task `Integration: MCP OpenAI Eval (run)` ist **nicht** für die Sim-API gedacht; starte stattdessen direkt:
     `& .\.venv\Scripts\python.exe -m uvicorn novapolis_agent.app.api.sim:app --host 127.0.0.1 --port 8765 --reload`.
2. Starte Godot 4 und öffne dieses Verzeichnis (`novapolis-sim`). Die kanonische Projektdatei ist `project.godot` direkt unter `novapolis-sim/` (Option A). Das frühere, verschachtelte Projekt wurde nach `Backups/novapolis-sim-archived-20251104/` verschoben.
3. Lade `Main.tscn` und drücke **Play**.

Während der Agent nicht erreichbar ist, bleibt die Oberfläche responsiv und zeigt unten eine Statusmeldung an. Läuft die API, aktualisieren sich Tick und Zeit etwa fünfmal pro Sekunde.

Für den UI-Start werden keine zusätzlichen Pflicht-Assets benötigt. Der separate Offline-Asset-Check unterscheidet jetzt zwei Profile: `Clean-Checkout` mit `--allow-empty` endet ohne Warnungen auch ohne `epochNN`-Ordner oder OGG-Dateien, waehrend der Vollstand-Pfad ohne dieses Flag echte Offline-Artefakte unter `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` erwartet.

Hub-Chatfenster (Hauptmenue)
---------------------------

Im Hub-Hauptmenue ist ein kleines Chatfenster integriert (`Chat mit Projektkontext`).

- Eingabe in das Feld schreiben und `Senden` klicken (oder Enter).
- Der Hub sendet an denselben Agent-Host/Port wie `SimClient` mit Endpoint `POST /chat`.
- Antworten und Fehler werden direkt im Panelverlauf angezeigt.

Hinweis:

- Ohne erreichbare Agent-API bleibt die Sim stabil; das Chatpanel zeigt den HTTP-/Request-Fehler nur als Status/Verlaufseintrag an.
- `Neu laden` zieht zusaetzlich den aktuellen Sessionstand ueber `GET /session/{session_id}` vom Sim-API-Host nach und spiegelt `world_log`, `pc_log`, Resume-Checkpoint und verfuegbare Session-Artefakte in derselben Ansicht wie die lokalen Epoch-Daten.
- Wenn im Session-Artefaktpfad ein `tts_manifest` vorliegt, markiert die Sim Audio als live verfuegbar und kann spaetere Kanaldateien aus demselben Sessionlauf statt nur aus `res://assets/audio` aufloesen.
- Offline-Bootstrap-Zielorte: `novapolis-sim/data/epochs/` fuer spaetere `epochNN`-Fixtures und `novapolis-sim/assets/audio/` fuer optionale OGG-Dateien nach dem Schema `epoch{dd}_slot{hh}_{pc|world}.ogg`.

Local Start / Stop / Verify (Developer)
-------------------------------------

Kurze Anweisungen, um lokal die Sim und die Agent-API zu starten, kurz zu prüfen und sauber zu stoppen.

- Server starten (in der Workspace-Root):

```powershell
Set-Location "${workspaceFolder}/novapolis_agent"
& "${workspaceFolder}/.venv/Scripts/python.exe" -m uvicorn app.api.sim:app --host 127.0.0.1 --port 8765 --reload
```

- Godot starten (Editor) oder Headless verifier:

```powershell
# optional: $env:AGENT_PORT = 8765
$godot = if ($env:GODOT_BIN) { $env:GODOT_BIN } elseif (Get-Command godot4 -ErrorAction SilentlyContinue) { 'godot4' } else { 'godot' }
# optional, falls Godot nicht in PATH liegt: $env:GODOT_BIN = '<Pfad-zur-Godot-Binary>'
& $godot --path "${workspaceFolder}/novapolis-sim"
# kanonischer Headless-Verifier (prints SIM_VERIFY: OK and exits):
& .\.venv\Scripts\python.exe scripts\run_sim_headless_verify.py
```

Alternativ in VS Code direkt den Task `Checks: sim headless verify` ausfuehren. Der Wrapper nutzt zuerst `--godot-bin`, dann `GODOT_BIN` und danach `godot4`/`godot` aus dem PATH.

Exportanker und Export-Smoke
----------------------------

- Der repo-seitige Windows-Presetanker liegt jetzt unter `novapolis-sim/export_presets.cfg` und fuehrt denselben Zielpfad `novapolis-sim/exports/windows/NovapolisSim.exe`.
- Der neue Task `Checks: sim export smoke` ruft `scripts/run_sim_export_smoke.py --launch` auf. Solange kein Export vorliegt, liefert derselbe Pfad bewusst die klare Vorbedingung `export executable missing`.
- Der Headless-Verify bleibt davon getrennt: `Checks: sim headless verify` prueft Projektintegritaet, `Checks: sim export smoke` den produktiven Windows-Export.

- Quick POST check (PowerShell):

```powershell
Invoke-WebRequest -Method POST "http://127.0.0.1:8765/world/step" -ContentType "application/json" -Body '{"dt":0.5}' | Select-Object StatusCode
# Erwartet: StatusCode 200
```

- Lightweight smoke test (ohne Wrapper):

```powershell
Invoke-WebRequest -Method POST "http://127.0.0.1:8765/world/step" -ContentType "application/json" -Body '{"dt":0.5}' | Select-Object StatusCode
# Erwartet: StatusCode 200
```

- Stop (falls nötig):

```powershell
Get-Process -Name "Godot*" -ErrorAction SilentlyContinue | Stop-Process -Force
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -and ($_.CommandLine -match 'uvicorn' -or $_.CommandLine -match 'app.api.sim') } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
```

Hinweis: `SimClient.gd` stellt `step_interval` und `port` als `@export` bereit (Inspector), sodass du Polling-Intervall und Port bei Bedarf anpassen kannst.

Avoiding the Editor / (DEBUG) window
-----------------------------------

Wenn du vermeiden willst, dass Godot das Editorfenster mit „(DEBUG)“ öffnet, starte die Simulation headless oder führe eine exportierte Release-Build aus. Zwei einfache Optionen:

- Vorher bei Bedarf einmalig setzen: `$env:GODOT_BIN = '<Pfad-zur-Godot-Binary>'`.
- Headless verifier (schnell, fuer CI / Smoke): `& .\.venv\Scripts\python.exe scripts\run_sim_headless_verify.py` oder bei Bedarf explizit `& .\.venv\Scripts\python.exe scripts\run_sim_headless_verify.py --godot-bin '<Pfad-zur-Godot-Binary>'` starten.
- Release/Export (empfohlen für Produktion): Exportiere das Projekt (`Project -> Export`) als Windows Desktop und starte die erzeugte `.exe` — das läuft ohne Editor-Overlay und ohne Debug-Label.

Fortsetzung und Persistenz
--------------------------

- Der Hub persistiert stabile Fortsetzungsdaten jetzt in `user://hub_prefs.cfg`: sichtbare Hub-Prefs, `session_id`, `scene_id`, `resume_checkpoint_id` und den zuletzt gewaehlten Replay-Checkpoint.
- Beim naechsten Start erzeugt die Sim keine neue Hub-Session, wenn bereits eine persistierte Session-ID vorliegt. Stattdessen werden `GET /session/{session_id}` und `GET /session/{session_id}/replay` direkt erneut geladen.
- Der Persistenzpfad speichert bewusst keine fluechtigen Runtime-Metriken wie Polling-Zeiten, Queue-Zwischenstaende oder temporaere Fehlerraten.
- Das kanonische Neustartverhalten fuer Hub, Replay und Live-Session ist in `novapolis-dev/docs/process/sim-export-release-path.ssot.md` beschrieben.
- Der neue Task `Checks: sim hub prefs contract` ruft `scripts/check_sim_hub_prefs_contract.py` auf und prueft denselben Key-Satz jetzt repo-seitig gegen leere, partielle und aeltere Fixture-Dateien unter `novapolis-sim/tests/fixtures/hub_prefs/`.

Kanonische Release-/Export-Doku
-------------------------------

- Der verbindliche Release-/Export-Pfad fuer Windows Desktop liegt unter `novapolis-dev/docs/process/sim-export-release-path.ssot.md`.
- Diese SSOT trennt Clean-Checkout, minimalen Vollstand und exportierte Laufzeit, dokumentiert die Godot-Klickpfade fuer den Export, verweist auf `novapolis-sim/export_presets.cfg` und beschreibt den lokalen Smoke-Test fuer die exportierte `.exe` ohne Editor-Overlay.

Kanonische UI-/Menue-IA
-----------------------

- Die fachliche Informationsarchitektur fuer Hub, Hauptmenue, eigentlichen Spielpfad, Replay/Resume und Modulwechsel liegt unter `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md`.
- README, Board und die Prozess-SSOTs verweisen damit fuer den eigentlichen Spielaufbau auf dieselbe Quelle statt nur auf einzelne Hub-Beschreibungen.

Kanonische Warnsignal-Lesart im Hub
----------------------------------

- Der produktive Hub folgt derselben Viererlesart wie die UI-IA: `stille Hintergrundlage`, `Knappheit`, `Warnung`, `Ueberzug`.
- `stille Hintergrundlage` bleibt in Topband und Telemetrie die ruhige Lesart fuer laufende Wirtschafts-, System- oder Weltlage ohne akuten Eingriffsdruck.
- `Knappheit` wird im aktiven Hub sichtbar, sobald Mittel, Reichweite oder Spielraum knapp werden, aber noch stabilisierbar sind.
- `Warnung` wird in Spielsicht und Ops-Kontext prominent, sobald eine unmittelbare negative Folge fuer Sicherheit, Lage oder Anschluss droht.
- `Ueberzug` bleibt an den turnbezogenen Antwortpfad gebunden und zeigt an, dass ein Plan nicht sauber in den Turn passt, statt eine zweite allgemeine Gefahrenskala zu eroeffnen.
- Fuer den ersten Vertikalslice fuehrt der Hub diese Signale knapp und handlungsnah; Komfort- oder Atmosphaerehinweise bleiben bewusst ausserhalb dieser Pflichtmatrix.

Verification Record
-------------------

- 2026-04-17 04:24 — Der kanonische Wrapper `scripts/run_sim_headless_verify.py` lief gegen Godot `v4.6.1.stable.official.14d19694e` mit explizitem `--godot-bin` erfolgreich durch. `res://scripts/verify_sim.gd` meldete `SIM_VERIFY: OK`, und nach der Cleanup-Korrektur endet derselbe Lauf jetzt ohne RID-/Resource-Leaks bei `EXITCODE=0`.
- 2025-11-16 04:54 — Headless verification executed: Godot Engine `v4.5.1.stable.official.f62fdbde1` loaded `novapolis-sim/project.godot` in headless mode and exited cleanly. Log file: `.tmp/results/logs/godot_headless_20251116_045407.log`. Quick scan found no ERROR/WARNING/Traceback lines. See `novapolis-dev/docs/donelog.md` for the postflight entry.

Kanonischer Testablauf (lokal)
------------------------------

Die Sim-Verifikation laeuft in fester Reihenfolge:

1. API-smoke
2. Godot-headless verify
3. Offline-Asset-Check
4. optionaler Eval-Fokuslauf

Beispielkommandos (Workspace-Root):

```powershell
# 1) API-smoke
.\.venv\Scripts\python.exe -m pytest -q novapolis_agent/tests/tests_sim_api.py::test_get_world_state_initial_values

# 2) Godot-headless verify
.\.venv\Scripts\python.exe scripts\run_sim_headless_verify.py

# 3) Offline-Asset-Check (+ optionale Slot-Konsistenz)
.\.venv\Scripts\python.exe scripts/check_sim_epoch_assets.py --allow-empty --check-slot-consistency

# 3b) Minimaler Vollstand ohne --allow-empty
.\.venv\Scripts\python.exe scripts/check_sim_epoch_assets.py --check-slot-consistency

# 3c) Statischer Hub-Prefs-Contract
.\.venv\Scripts\python.exe scripts/check_sim_hub_prefs_contract.py --repo-root .

# 4) optional: quality_de Eval-Fokus
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --tag quality_de --checks must_include,keywords_any,keywords_at_least,not_include,regex,quality_de --packages novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl
```

Hinweis: Stufe 1 bis 3 muessen gruen sein, bevor ein Sim-Lauf als lokal verifiziert gilt. Mit `--allow-empty` pruefst du das warnungsfreie Clean-Checkout-Profil; ohne dieses Flag pruefst du den kleinen Repo-Vollstand unter `novapolis-sim/data/epochs/epoch01/` und `novapolis-sim/assets/audio/`. Mit `--check-slot-consistency` gilt der Lauf als fehlgeschlagen bei Slot-Mismatch (`world_log` vs. `pc_log`) oder ungueltigen Slotwerten ausserhalb `0..23`. Fuer den Headless-Verifier bleibt `Checks: sim headless verify` der kanonische VS-Code-Einstieg; `Checks: sim hub prefs contract` deckt die persistente Resume-Logik statisch ohne Godot-Binary ab.

Hinweis: Wenn deine lokale Godot-Binary eine Debug-Build ist, zeigt das exportierte Editor-Playfenster weiterhin Debug-Markierungen. Lade im Zweifelsfall die offizielle Release-Binary von `https://godotengine.org` oder nutze einen Export (Release) für produktives Ausführen.



