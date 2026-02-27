---
stand: 2026-02-27 06:06
update: Obsolete Referenzen auf `cvn-agent` bereinigt und Test-/Task-Verweise auf den aktuellen Single-Root-Iststand nachgezogen.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'WORKSPACE_INDEX.md' 'DONELOG.md' 'novapolis-dev/docs/tests.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-26 22:02); f:/VS-Code-Workspace/Main/.venv/Scripts/python.exe scripts/check_frontmatter.py 'WORKSPACE_INDEX.md' 'DONELOG.md' 'novapolis-dev/docs/tests.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-02-26 22:02)
---

Tests & Prequel
===============

<!-- Dokument angelegt am 2025-10-29, basierend auf Anforderungen zur Konsolidierung -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/tests.md` am 2025-10-29 -->

Bestehende Testabdeckung
------------------------

- `novapolis_agent/tests/` (pytest): deckt die Simulations-API (`novapolis_agent/app/api/sim.py`) inklusive `GET /world/state` und `POST /world/step` ab; Kernabdeckung liefern u. a. `novapolis_agent/tests/tests_sim_api.py` und `novapolis_agent/tests/test_api_sim_state.py`.
- `novapolis_agent/coverage.xml`: erzeugt durch pytest, dient als Referenz für API-Abdeckung.
- Root-Tasking: VS-Code-Tasks in `.vscode/tasks.json` ermöglichen reproduzierbare Läufe (u. a. `Tests: pytest (-q) [root]`, `Tests: pytest (unit)`, `Tests: pytest (api+streaming)`).
- `novapolis-sim/`: keine automatisierten Tests; manuelle Prüfung via Godot-Editor.

Mini-Prequel-Testplan (novapolis-sim)
-------------------------------------

Ziel: Beim Client-Start einen kurzen "Prequel"-Ablauf testen, der den aktuellen Weltzustand visualisiert und einen deutschen Intro-Text abspielt, ohne neue Funktionen zu implementieren.

1. **Startzustand abrufen**
   - Godot-Client lädt Szene `Main.tscn` und nutzt den bestehenden Autoload `SimClient`.
   - Sofortiger `GET /world/state`-Request: Erwartet Payload mit `tick`, `time`/`timestamp` und optionalen Statusfeldern.
2. **Intro-Overlay rendern**
   - Neuen UI-Knoten (z. B. `CanvasLayer`) vorbereiten, der den Tick (`Tick: <n>`) und die aktuelle Sim-Zeit (`Zeit: <hh:mm:ss>`) als Text anzeigt.
   - Intro-Text (Deutsch, aus finalem RP-Inhalt) als mehrzeiligen Label/TextBox anzeigen; Inhalte aus freigegebenem Kanon (z. B. Kurzfassung Memory-Bundle) wählen.
3. **Sequenz abspielen**
   - Nach dem ersten erfolgreichen State-Poll erscheint der Intro-Text für ca. 5 Sekunden, danach ausblenden und zur regulären Visualisierung übergehen.
   - Während der Intro-Phase bereits Poll-Loop aktiv lassen (bestehender 0,2 s Step).
4. **Statusanzeige**
   - Ergänze ein kleines Statuspanel mit Feldern `Verbindung` (siehe Offline-Verhalten) und `Letztes Update` (timestamp aus Response, fallback "-").

Offline-Verhalten
-----------------

- Wenn `POST /world/step` oder `GET /world/state` fehlschlägt (Timeout, ConnectionRefused, HTTP ≥500):
  - Setze Statusanzeige auf `Verbindung: Offline` in roter Schrift.
  - Stoppe Step-Requests temporär (z. B. Retry nach 3 Sekunden mit Backoff) und behalte letzten bekannten Tick/Zeit eingefroren.
  - Zeige Hinweistext: "Agent nicht erreichbar - Anzeige pausiert".
- Bei erfolgreichem Reconnect:
  - Status zurück auf `Verbindung: Verbunden` in neutraler/grüner Farbe.
  - Intro-Overlay bleibt deaktiviert; nur Statuspanel aktualisieren.

Testprotokolle
--------------

- 2025-10-29: `python -m pytest tests\tests_sim_api.py` (ausgeführt im Verzeichnis `novapolis_agent`) - **Bestanden**.

Abstimmung & Folgearbeiten
--------------------------

- Intro-Text aus finalen Inhalten auswählen und im Dev-Board `novapolis-dev/docs/todo.dev.md` als Aufgabe notieren (z. B. unter "Visualisierung"), bevor Umsetzung startet.
- Keine Änderungen an API-Endpunkten notwendig; bestehende Polling-Logik wird nur um UI-Ausgaben ergänzt.
- Manuelle Tests künftig in `novapolis-dev/docs/donelog.md` dokumentieren (Datum, Kurzresultat).


