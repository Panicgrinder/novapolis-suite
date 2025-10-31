# Novapolis Sim

Ein minimales Godot-4-Projekt zur Visualisierung des Simulationszustands aus dem Novapolis-Agenten.

## How to run

1. Stelle sicher, dass die Python-Seite läuft:
   - In `novapolis_agent` `.env` anlegen (`AGENT_PORT=8765` Standard).
   - VS Code Task `Run Agent Dev` starten **oder**
     `uvicorn app.api.sim:app --host 127.0.0.1 --port 8765 --reload` ausführen.
2. Starte Godot 4 und öffne dieses Verzeichnis (`novapolis-sim`).
3. Lade `Main.tscn` und drücke **Play**.

Während der Agent nicht erreichbar ist, bleibt die Oberfläche responsiv und zeigt unten eine Statusmeldung an. Läuft die API, aktualisieren sich Tick und Zeit etwa fünfmal pro Sekunde.

Weitere Assets oder Artefakte werden nicht benötigt; das Projekt arbeitet ausschließlich mit Bordmitteln von Godot 4.
