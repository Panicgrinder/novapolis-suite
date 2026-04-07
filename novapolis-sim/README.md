stand: 2026-04-07 16:11
update: Die Sim-README trennt jetzt den warnungsfreien Clean-Checkout-Bootstrap vom artefaktbasierten Vollstand-Pfad und dokumentiert die Bootstrap-Zielorte.
checks: snapshot-lock PASS (2026-04-07 16:11); markdownlint PASS; frontmatter PASS; todo-index-sync PASS
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
$godot = if ($env:GODOT_BIN) { $env:GODOT_BIN } else { 'godot4' }
# optional: $env:AGENT_PORT = 8765
& $godot --path "${workspaceFolder}/novapolis-sim"
# headless verifier (prints SIM_VERIFY: OK and exits):
& $godot --path "${workspaceFolder}/novapolis-sim" -s res://scripts/verify_sim.gd --headless
```

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
- Headless verifier (schnell, für CI / Smoke): `& $env:GODOT_BIN --path "${workspaceFolder}/novapolis-sim" -s res://scripts/verify_sim.gd --headless` oder ohne gesetzte Variable mit `godot4 --path "${workspaceFolder}/novapolis-sim" -s res://scripts/verify_sim.gd --headless` starten.
- Release/Export (empfohlen für Produktion): Exportiere das Projekt (`Project -> Export`) als Windows Desktop und starte die erzeugte `.exe` — das läuft ohne Editor-Overlay und ohne Debug-Label.

Verification Record
-------------------

- 2025-11-16 04:54 — Headless verification executed: Godot Engine `v4.5.1.stable.official.f62fdbde1` loaded `novapolis-sim/project.godot` in headless mode and exited cleanly. Log file: `.tmp/results/logs/godot_headless_20251116_045407.log`. Quick scan found no ERROR/WARNING/Traceback lines. See `novapolis-dev/docs/donelog.md` for the postflight entry.

Kanonischer Testablauf (lokal)
------------------------------

Die Sim-Verifikation laeuft in fester Reihenfolge:

1. API-smoke
2. Godot-headless scene load
3. Offline-Asset-Check
4. optionaler Eval-Fokuslauf

Beispielkommandos (Workspace-Root):

```powershell
# 1) API-smoke
.\.venv\Scripts\python.exe -m pytest -q novapolis_agent/tests/tests_sim_api.py::test_get_world_state_initial_values

# 2) Godot-headless
godot --headless --path '.\novapolis-sim' --quit --scene res://Main.tscn

# 3) Offline-Asset-Check (+ optionale Slot-Konsistenz)
.\.venv\Scripts\python.exe scripts/check_sim_epoch_assets.py --allow-empty --check-slot-consistency

# 4) optional: quality_de Eval-Fokus
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --tag quality_de --checks must_include,keywords_any,keywords_at_least,not_include,regex,quality_de --packages novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl
```

Hinweis: Stufe 1 bis 3 muessen gruen sein, bevor ein Sim-Lauf als lokal verifiziert gilt. Mit `--allow-empty` pruefst du das warnungsfreie Clean-Checkout-Profil; ohne dieses Flag pruefst du den Vollstand mit echten Offline-Artefakten. Mit `--check-slot-consistency` gilt der Lauf als fehlgeschlagen bei Slot-Mismatch (`world_log` vs. `pc_log`) oder ungueltigen Slotwerten ausserhalb `0..23`.

Hinweis: Wenn deine lokale Godot-Binary eine Debug-Build ist, zeigt das exportierte Editor-Playfenster weiterhin Debug-Markierungen. Lade im Zweifelsfall die offizielle Release-Binary von `https://godotengine.org` oder nutze einen Export (Release) für produktives Ausführen.



