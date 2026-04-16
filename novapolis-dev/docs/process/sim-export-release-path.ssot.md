---
stand: 2026-04-17 01:04
update: Diese SSOT definiert den kanonischen Windows-Export- und Smoke-Pfad fuer den Sim-Client ausserhalb des Godot-Editors.
checks: snapshot-lock PASS (2026-04-17 01:04); markdownlint=PASS; frontmatter=PASS
---

Sim Export- und Release-Pfad (SSOT)
===================================

Zweck
-----

Diese SSOT ersetzt den frueheren losen Hinweis `Project -> Export` durch einen belastbaren Repo-Pfad fuer den produktiven Windows-Desktop-Start des Sim-Clients.

Scope
-----

- kanonischer Exportpfad fuer Windows Desktop
- getrennte Voraussetzungen fuer Clean-Checkout, lokalen Vollstand und exportierte Laufzeit
- lokaler Smoke-Test fuer die exportierte App ohne Editor-Overlay

Nicht-Ziele
-----------

- keine Verpflichtung auf `export_presets.cfg`, solange derselbe Pfad reproduzierbar dokumentiert bleibt
- keine CI-Automatisierung des Godot-Exports in diesem Lauf

Kanonischer Zielpfad
--------------------

- Exportziel: `novapolis-sim/exports/windows/NovapolisSim.exe`
- Begleitdateien liegen im selben Zielordner wie von Godot erzeugt.
- Dieser Pfad ist die kanonische lokale Release-Ablage fuer manuelle Windows-Smokes.

Voraussetzungen nach Profil
---------------------------

### Clean-Checkout

- Godot-Projekt unter `novapolis-sim/` ist oeffenbar und headless pruefbar.
- Offline-Asset-Check darf ueber `--allow-empty` ohne `epochNN`-Ordner oder OGG-Dateien gruen laufen.
- Erwartung: Hub startet, aber es gibt keine Pflicht auf lokale Session- oder Audio-Artefakte.

### Lokaler Vollstand

- Agent-Sim-API laeuft lokal.
- Optionale Session-Artefakte unter `novapolis_agent/tmp/sim_sessions/<session_id>/` koennen fuer Replay, Resume und Audio vorhanden sein.
- Optionale Offline-Artefakte unter `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` koennen zusaetzlich geladen werden.

### Exportierte Laufzeit

- Exportierte App nutzt denselben API-Host/Port-Pfad wie der Editorlauf.
- Persistente Hub-Daten bleiben im Godot-`user://`-Bereich der exportierten App und sind logisch vom Repo getrennt.
- Erwartung: produktiver Start ohne Editorfenster, Debug-Overlay oder Editor-Menueleiste.

Kanonischer Exportablauf (Godot-Editor)
---------------------------------------

Da dieser Schritt nicht direkt in VS Code laeuft, gilt die User-Praeferenz: explizite Klickpfade und erwartete Resultate.

1. Projekt in Godot oeffnen.
   Erwartetes Ergebnis: `novapolis-sim/project.godot` ist geladen und `Main.tscn` bleibt die Main-Scene.
2. In Godot `Project -> Export...` oeffnen.
   Erwartetes Ergebnis: Der Export-Dialog erscheint.
3. Falls noch kein Windows-Desktop-Preset vorhanden ist: `Add... -> Windows Desktop` waehlen.
   Erwartetes Ergebnis: Ein Preset `Windows Desktop` erscheint in der linken Preset-Liste.
4. Im Windows-Preset den Zielpfad auf `novapolis-sim/exports/windows/NovapolisSim.exe` setzen.
   Erwartetes Ergebnis: Die Ausgabe landet reproduzierbar im Repo unter `novapolis-sim/exports/windows/`.
5. Exportmodus auf Release belassen und den Export starten.
   Erwartetes Ergebnis: `NovapolisSim.exe` und die von Godot benoetigten Begleitdateien werden geschrieben.

Lokaler Smoke fuer die exportierte App
--------------------------------------

1. Zuerst die Sim-API lokal starten.
   Erwartetes Ergebnis: `http://127.0.0.1:8765/world/step` und die Session-Endpunkte sind erreichbar.
2. Danach `novapolis-sim/exports/windows/NovapolisSim.exe` starten.
   Erwartetes Ergebnis: Die App oeffnet ohne Editor-Overlay oder `(DEBUG)`-Fenster.
3. Im Hub pruefen.
   Erwartetes Ergebnis: Topband, Stage, Ops-Spalte und Telemetrieband werden sichtbar geladen.
4. Falls bereits eine persistierte Session vorliegt, `Neu laden` nicht zwingend selbst betaetigen.
   Erwartetes Ergebnis: Die App synchronisiert `GET /session/{session_id}` und `GET /session/{session_id}/replay` beim Start automatisch nach.
5. Einen kurzen Bedienpfad pruefen.
   Erwartetes Ergebnis: `Hub-Chat`, Replay-Zusammenfassung und Statuszeilen reagieren ohne Editorpfad oder Menue-Umschaltung.

Verknuepfte Istquellen
----------------------

- `novapolis-sim/README.md`
- `novapolis-dev/docs/todo.sim.md`
- `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md`
- `novapolis-sim/scripts/Main.gd`
- `novapolis-sim/scripts/verify_sim.gd`