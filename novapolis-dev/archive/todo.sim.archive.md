---
stand: 2026-03-03 00:56
update: Vollstaendig erledigte Sim-Bloecke aus dem aktiven Board archiviert (neueste oben).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis-dev/archive/todo.sim.archive.md' PASS (2026-03-03 00:56); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis-dev/archive/todo.sim.archive.md' PASS (EXITCODE=0, 2026-03-03 00:56)
---

TODO-Archiv - Sim
=================

Zweck: Vollständig abgeschlossene TODO-Abschnitte aus `novapolis-sim/**` Aufgaben aufnehmen.

Regeln (kurz)
- Nur vollständig abgehakte Abschnitte ([x] überall) verschieben.
- Inhalt unverändert übernehmen; unter der Abschnitts-Überschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen.
- Headings in diesem Archiv: Setext (MD003 konform, H1/H2).
- Präsentation: Lint-Läufe mit PRESENTATION=SHARED.

Ablage
- Neueste Einträge oben einfügen.

<!-- Hier unterhalb neue, vollständig erledigte Blöcke einfügen (neu zuerst). -->

Arbeitsplan Sim-Modul: Phase 1 - Stabilisierung der Laufzeitkopplung (Jetzt)
--------------------------------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Arbeitsplan Sim-Modul (Analyse 2026-03-02)`).

- [x] Verbindungszustand im UI klarer machen (`novapolis-sim/scripts/Main.gd`): letzte erfolgreiche Aktualisierung + Fehlerdauer anzeigen.
- [x] Polling robuster machen (`novapolis-sim/autoload/SimClient.gd`): explizite Request-Timeout/Retry-Status im Label und optionale Pause bei Dauerfehlern.
- [x] Sim-API-Payload minimal erweitern (`novapolis_agent/app/api/sim.py`): neben `tick/time/events` optionalen `sim_meta`-Block (z. B. `seed`, `mode`) vorbereiten.

Arbeitsplan Sim-Modul: Phase 2 - Interaktions- und Scheduler-Vorbereitung (Als naechstes)
-------------------------------------------------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Arbeitsplan Sim-Modul (Analyse 2026-03-02)`).

- [x] Event-Signals in Godot konkretisieren (`on_action_start/end`, `on_visibility_change`, `on_interrupt`) und in `Main.gd` an UI/Log binden.
- [x] Scheduler-Hook als reine Schnittstelle anlegen (ohne Business-Logik), referenziert von `novapolis-dev/docs/specs/scheduler-spec.md`.
- [x] UI-Controls erweitern: Stundensprung, Auto-Advance bei leerem PC-Slot, sichtbarer Replay-Seed.

Hub-v1: Priorisierung fuer Umsetzung
------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Hub-v1 fuer Framework-Betrieb (konkretisiert 2026-03-02)`).

- [x] [Jetzt] Hub-Topbar v1 (Verbindung + Laufzeit + Fehlerbild) in `Main.tscn/Main.gd` einziehen.
  - [x] Umsetzung erfolgt: Labels `HubTitle/Api/Polling/Queue/Errors` in `Main.tscn`; Live-Refresh in `Main.gd` mit SimClient-Runtime-Snapshot.
  - [x] Revalidiert am 2026-03-02 16:06: Godot Headless-Load (`res://Main.tscn`, Exitcode 0) und Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler.
- [x] [Als naechstes] Modul-Karten v1 fuer `Sim`, `Agent/API`, `Eval/Training` (zunaechst read-only).
  - Evidenz: `novapolis-sim/Main.tscn` (Panels + Label-Struktur) und `novapolis-sim/scripts/Main.gd` (`_refresh_module_cards()` mit Runtime-Snapshot, sim_meta, Queue-/Artefaktstatus).
- [x] [Als naechstes] Dashboard-Schnellaktionen als Platzhalter-Buttons mit Runtime-Events verdrahten.
  - Evidenz: `novapolis-sim/Main.tscn` (`ServerToggleButton`, `HubReloadButton`, `HubChecksButton`) und `novapolis-sim/scripts/Main.gd` (`_on_server_toggle_pressed`, `_on_hub_reload_pressed`, `_on_hub_checks_pressed`).
- [x] [Spaeter] Persistente Hub-Konfiguration (sichtbare Module, Refresh-Raten, Default-Panel).
  - Evidenz: `novapolis-sim/Main.tscn` (`HubConfigPanel`) und `novapolis-sim/scripts/Main.gd` (`_load_hub_preferences`, `_save_hub_preferences`, `_apply_hub_preferences`, `_open_default_panel_if_configured`).
  - Persistenz: `user://hub_prefs.cfg` (ConfigFile) fuer sichtbare Cards, Refresh-Profil, Default-Panel.
  - Verifikation: Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Neuordnung: A) Hub-Core (frameworkweit, allgemein)
---------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Neuordnung offener Punkte nach Zugehoerigkeit (Stand 2026-03-02)`).

- [x] Persistente Hub-Konfiguration umsetzen (sichtbare Module, Refresh-Rate, Default-Panel je Nutzerprofil).
  - Umsetzung in `HubConfigPanel`: Karten-Sichtbarkeit (Sim/API/Eval), Refresh-Profile (`fast/normal/slow`), Default-Panel (`hub/agent/checks`) und Save.
- [x] Dashboard-Punkt `Run Checks` von Placeholder auf echte Task-Ausfuehrung mit Ergebnisstatus umstellen.
  - Evidenz: `novapolis-sim/Main.tscn` (`ChecksStudioPanel` mit 2-Spalten-Baukasten + read-only Output) und `novapolis-sim/scripts/Main.gd` (exklusiver Checks-Subview, Command-Builder, Ausfuehrung via PowerShell, Modul-/Typ-Selektion).
  - Verifikation: Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`; Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler.
- [x] Health-Panel standardisieren: klarer Status fuer `local`, `external`, `offline`, `degraded` inkl. letzter Ursache.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_derive_health_state`) und Einbindung in `hub_api_label`, `api_card_health_label`, `server_status_label`.
  - Verifikation: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Neuordnung: B) RP-spezifische Bedienebene (nicht allgemeiner Hub)
------------------------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Neuordnung offener Punkte nach Zugehoerigkeit (Stand 2026-03-02)`).

- [x] RP-Panel einfuehren: `Hour +1`, `Auto-Advance`, `Replay-Seed` ausschließlich dort darstellen.
- [x] RP-Panel mit Slot-/Epoch-Navigation koppeln, ohne Hub-Core zu vermischen.
- [x] RP-Panel-Ereignisse separat im Runtime-Log taggen (z. B. `RP_*`) fuer bessere Nachvollziehbarkeit.
- [x] RP-Einstieg am ehemaligen zweiten Audio-Slot vorbereitet: Buttontext auf `RP Modul` gesetzt und Runtime-Event `RP_MODULE` angebunden.

Neuordnung: D) Qualitaet, Governance, Nachweis
----------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Neuordnung offener Punkte nach Zugehoerigkeit (Stand 2026-03-02)`).

- [x] API-Tests erweitern (ungueltiges `dt`, Event-Cap, Reset-Invarianten, Fehlerpfad-Resilienz).
  - Evidenz: `novapolis_agent/tests/test_api_sim_state.py` und `novapolis_agent/tests/tests_sim_api.py` decken jetzt Invalid-`dt`-Faelle (`422`/ValidationError), Event-Cap-Truncation und Reset-Invarianten explizit ab.
- [x] Offline-Asset-Check vertiefen (Slot-Konsistenz world_log vs. pc_log, klare Abbruchkriterien).
  - Evidenz: `scripts/check_sim_epoch_assets.py` um `--check-slot-consistency` erweitert (FAIL bei Slot-Mismatch, Slotwerten ausserhalb `0..23`, oder nicht detektierbaren Slots bei vorhandenen Eintraegen).
- [x] Sim-Runbook aktualisieren (kanonischer Ablauf: API-smoke -> Godot-headless -> Asset-check -> optionale Eval-Checks).
  - Evidenz: `novapolis_agent/docs/runbook.md` enthaelt jetzt den Abschnitt `Kanonischer Sim-Pruefablauf (kurz, in Reihenfolge)` mit festen Kommandos.

Phase 3 - Qualitaet und Nachweisfuehrung (Als naechstes)
---------------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md`.

- [x] API-Tests ausbauen (`novapolis_agent/tests/test_api_sim_state.py`, `novapolis_agent/tests/tests_sim_api.py`): Fehlerpfade fuer ungueltiges `dt`, Event-Cap und Reset-Invarianten absichern.
  - Verifikation: `pytest -q novapolis_agent/tests/test_api_sim_state.py novapolis_agent/tests/tests_sim_api.py` PASS (5/5), `pyright` PASS, `mypy` PASS.
- [x] Sim-Offline-Check staerken (`scripts/check_sim_epoch_assets.py`): optional Slot-Konsistenz zwischen `world_log` und `pc_log` validieren.
  - Verifikation: `pytest -q novapolis_agent/tests/scripts/test_check_sim_epoch_assets.py` PASS (4/4), Checker-Lauf `--allow-empty --check-slot-consistency` mit `fail:0`.
- [x] Runbook/README nachziehen (`novapolis-sim/README.md`): neuer Testablauf (headless + API-smoke + epoch-assets-check) als kanonischer Kurzablauf.
  - Evidenz: `novapolis-sim/README.md` Abschnitt `Kanonischer Testablauf (lokal)` hinzugefuegt und mit identischer Reihenfolge dokumentiert.

Root-Uebernahme: novapolis-sim Block aus todo.root
-------------------------------------------------

archived_at: 2026-02-21 04:52

Quelle: `todo.root.md` (Abschnitt `novapolis-sim`).

- [x] Headless-Lade-Check als abgeschlossen archiviert.
- [x] Sim-Detailhistorie aus Root entfernt; aktiver Sim-Backlog bleibt in Sim-/Dev-Boards.


