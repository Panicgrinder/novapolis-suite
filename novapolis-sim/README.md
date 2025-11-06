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

