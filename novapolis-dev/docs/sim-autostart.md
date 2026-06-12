---
stand: 2026-06-12 08:32
update: Added doc for Auto-Start Server preference and behavior
checks: frontmatter=manual
---

Sim: Auto-Start Server (Kurzreferenz)
====================================

Kurz: Die Sim bietet eine Developer-Preference `server_autostart_enabled`, die lokal gespeicherte Hub-Preferences (`user://hub_prefs.cfg`) nutzt, um nach wiederholten Poll-Fehlern automatisch den lokalen Agent-Python-Server zu starten.

Details
-------
- Preference-Key: `server_autostart_enabled` (Boolean)
- Persistenz: `user://hub_prefs.cfg` (via `HubPreferencesStore`)
- Auslösebedingung: `SimClient` erkennt >=2 aufeinanderfolgende Poll-Fehler und `server_autostart_enabled` ist aktiv; keine lokale Server-PID vorhanden.
- Rate-Limit: Startversuche werden intern zeitlich begrenzt (z.B. 4000ms Mindestabstand zwischen Attempts).
- UI: `Auto-Start Server` `CheckBox` in Hub-Config (`novapolis-sim/Main.tscn` → `HubConfigAutoStartCheckBox`).
- Dateien (Änderung): `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/hub_config_controller.gd`, `novapolis-sim/scripts/hub_layout_controller.gd`, `novapolis-sim/Main.tscn`.

Sicherheit & Hinweise
---------------------
- Autostart ist nur eine Developer-Hilfe. Es startet lokal nur den bereits vorhandenen lokalen Serverstart-Pfad (`_start_local_server()`), schreibt keine Secrets und nutzt keine externen Netzwerkdienste.
- Visuelle Politur (Position, Labeltext, Topbar-Indikator) ist optional und kann separat umgesetzt werden.

Wie testen
----------
1. Setze `server_autostart_enabled` in der UI (Hub → Settings → Auto-Start Server).
2. Stoppe lokalen Agent-Server (falls laufend).
3. Starte Godot, lasse Sim starten; beobachte Terminal/Log: nach ~2 Poll-Fehlern sollte ein Startversuch erfolgen.

Weitere Schritte
----------------
- Optional: Topbar-Indikator "Autostart: an/aus" hinzufügen.
- Optional: Unit-/Integrationstest für `_maybe_autostart_server()` in Godot-Headless-Verify-Umgebung.
