---
stand: 2025-11-06 15:22
update: YAML Frontmatter ergänzt (MD003-konform)
checks: markdownlint-cli2 PASS (single file)
---

Novapolis Sim
=============

Ein minimales Godot-4-Projekt zur Visualisierung des Simulationszustands aus dem Novapolis Agenten.

Aufgaben & Planung
------------------

- Aufgaben für das Simulations‑Modul bitte im Board `novapolis-dev/docs/todo.sim.md` pflegen (der Index `novapolis-dev/docs/todo.index.md` dient nur der Navigation).

How to run
----------

1. Stelle sicher, dass die Python-Seite läuft:
   - In `novapolis_agent` `.env` anlegen (`AGENT_PORT=8765` Standard).
   - VS Code Task `Run Agent Dev` starten **oder**
     `uvicorn app.api.sim:app --host 127.0.0.1 --port 8765 --reload` ausführen.
2. Starte Godot 4 und öffne dieses Verzeichnis (`novapolis-sim`). Die kanonische Projektdatei ist `project.godot` direkt unter `novapolis-sim/` (Option A). Das frühere, verschachtelte Projekt wurde nach `Backups/novapolis-sim-archived-20251104/` verschoben.
3. Lade `Main.tscn` und drücke **Play**.

Während der Agent nicht erreichbar ist, bleibt die Oberfläche responsiv und zeigt unten eine Statusmeldung an. Läuft die API, aktualisieren sich Tick und Zeit etwa fünfmal pro Sekunde.

Weitere Assets oder Artefakte werden nicht benötigt; das Projekt arbeitet ausschließlich mit Bordmitteln von Godot 4.

 
Local Start / Stop / Verify (Developer)
-------------------------------------

Kurze Anweisungen, um lokal die Sim und die Agent‑API zu starten, kurz zu prüfen und sauber zu stoppen.

- Server starten (in der Workspace-Root):

```powershell
Set-Location "F:\VS Code Workspace\Main\novapolis_agent"
& "F:\VS Code Workspace\Main\.venv\Scripts\python.exe" -m uvicorn app.api.sim:app --host 127.0.0.1 --port 8765 --reload
```

- Godot starten (Editor) oder Headless verifier:

```powershell
# optional: $env:AGENT_PORT = 8765
& "F:\VS Code Workspace\Main\novapolis-sim\Godot_v4.5.1-stable_win64.exe" --path "F:\VS Code Workspace\Main\novapolis-sim"
# headless verifier (prints SIM_VERIFY: OK and exits):
& "F:\VS Code Workspace\Main\novapolis-sim\Godot_v4.5.1-stable_win64.exe" --path "F:\VS Code Workspace\Main\novapolis-sim" -s res://scripts/verify_sim.gd --headless
```

- Quick POST check (PowerShell):

```powershell
Invoke-WebRequest -Method POST "http://127.0.0.1:8765/world/step" -ContentType "application/json" -Body '{"dt":0.5}' | Select-Object StatusCode
# Erwartet: StatusCode 200
```

- Lightweight smoke test (startet uvicorn aus .venv, testet POST, stoppt wieder):

```powershell
pwsh -File .\scripts\verify_sim.ps1
```

- Stop (falls nötig):

```powershell
Get-Process -Name "Godot*" -ErrorAction SilentlyContinue | Stop-Process -Force
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -and ($_.CommandLine -match 'uvicorn' -or $_.CommandLine -match 'app.api.sim') } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
```

Hinweis: `SimClient.gd` stellt `step_interval` und `port` als `@export` bereit (Inspector), sodass du Polling‑Intervall und Port bei Bedarf anpassen kannst.

