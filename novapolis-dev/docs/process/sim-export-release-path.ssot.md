---
stand: 2026-04-23 16:50
update: Diese SSOT fuehrt jetzt zusaetzlich `export_presets.cfg`, den Repo-Export-Smoke und den minimalen Vollstand als kanonische Sim-Anker.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260423_155606.md; snapshot-lock PASS (2026-04-23 16:50)
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
- kanonischer Headless-Verify-Pfad fuer den lokalen Editor-/Repo-Smoke vor Export oder Release-Smoke

Nicht-Ziele
-----------

- keine CI-Automatisierung des Godot-Exports in diesem Lauf

Kanonischer Zielpfad
--------------------

- Repo-Anker: `novapolis-sim/export_presets.cfg`
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
- Minimaler Repo-Vollstand liegt unter `novapolis-sim/data/epochs/epoch01/` plus benannte OGG-Beispiele unter `novapolis-sim/assets/audio/`.
- Optionale weitere Offline-Artefakte unter `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` koennen zusaetzlich geladen werden.

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
4. Falls der Editor einen bestehenden Presetanker anbietet, `novapolis-sim/export_presets.cfg` laden bzw. bestaetigen.
   Erwartetes Ergebnis: Der Windows-Desktop-Preset fuehrt denselben Repo-Zielpfad bereits vor.
5. Im Windows-Preset den Zielpfad auf `novapolis-sim/exports/windows/NovapolisSim.exe` setzen oder gegen den vorhandenen Wert gegenpruefen.
   Erwartetes Ergebnis: Die Ausgabe landet reproduzierbar im Repo unter `novapolis-sim/exports/windows/`.
6. Exportmodus auf Release belassen und den Export starten.
   Erwartetes Ergebnis: `NovapolisSim.exe` und die von Godot benoetigten Begleitdateien werden geschrieben.

Lokaler Smoke fuer die exportierte App
--------------------------------------

1. Zuerst die Sim-API lokal starten.
   Erwartetes Ergebnis: `http://127.0.0.1:8765/world/step` und die Session-Endpunkte sind erreichbar.
2. Danach `Checks: sim export smoke` oder direkt `scripts/run_sim_export_smoke.py --repo-root . --launch` ausfuehren.
   Erwartetes Ergebnis: Fehlende Exporte werden klar als Vorbedingung `export executable missing` gemeldet; ein vorhandener Export startet zumindest kurz an.
3. Danach `novapolis-sim/exports/windows/NovapolisSim.exe` starten, falls der Wrapper nur den Vorcheck ausfuehrte.
   Erwartetes Ergebnis: Die App oeffnet ohne Editor-Overlay oder `(DEBUG)`-Fenster.
4. Im Hub pruefen.
   Erwartetes Ergebnis: Topband, Stage, Ops-Spalte und Telemetrieband werden sichtbar geladen.
5. Falls bereits eine persistierte Session vorliegt, `Neu laden` nicht zwingend selbst betaetigen.
   Erwartetes Ergebnis: Die App synchronisiert `GET /session/{session_id}` und `GET /session/{session_id}/replay` beim Start automatisch nach.
6. Einen kurzen Bedienpfad pruefen.
   Erwartetes Ergebnis: `Hub-Chat`, Replay-Zusammenfassung und Statuszeilen reagieren ohne Editorpfad oder Menue-Umschaltung.

Rolle im Release-Evidence-Bundle
--------------------------------

- Der Export-Smoke unter `novapolis-sim/exports/windows/NovapolisSim.exe` ist der Sim-seitige Pflichtbeleg des gemeinsamen Pfads `novapolis-dev/docs/process/text-rpg-release-evidence-bundle-v1.ssot.md`.
- `Checks: sim headless verify` bleibt der Vorlauf fuer Editor- und Projektintegritaet, ersetzt aber nicht den produktiven Export-Smoke ausserhalb des Editors.
- Ein Slice gilt daher nicht als release-reif, solange entweder der Headless-Vorlauf oder der exportierte Windows-Smoke fuer denselben Stand fehlt.

Kanonischer Headless-Verify vor Export
--------------------------------------

- VS-Code-Task: `Checks: sim headless verify`
- CLI-Wrapper: `& .\.venv\Scripts\python.exe scripts\run_sim_headless_verify.py`
- Fallback fuer lokale Binaries ausserhalb des PATH: `GODOT_BIN=<Pfad-zur-Godot-Binary>` oder `--godot-bin <Pfad-zur-Godot-Binary>`.
- Erwartetes Ergebnis: `SIM_VERIFY: OK` ohne neue Scene-, Preload- oder Parserfehler fuer `Main.tscn` und den aktuellen Hub-Pfad.

Zusaetzliche Repo-Checks
------------------------

- VS-Code-Task: `Checks: sim epoch assets (minimal fullstand)`
- VS-Code-Task: `Checks: sim hub prefs contract`
- Der erste prueft den kleinen Vollstand unter `novapolis-sim/data/epochs/epoch01/` plus benannte OGG-Beispiele ohne `--allow-empty`.
- Der zweite prueft statisch die Persistenzschluessel fuer `user://hub_prefs.cfg` gegen leere, partielle und aeltere Fixture-Dateien.

Verknuepfte Istquellen
----------------------

- `novapolis-sim/README.md`
- `novapolis-dev/docs/todo.sim.md`
- `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md`
- `novapolis-sim/scripts/Main.gd`
- `novapolis-sim/scripts/verify_sim.gd`
