---
stand: 2026-03-17 16:58
update: Wochenabschluss-Nachholung dokumentiert; KPI-Protokoll der Hygiene-Cadence nachgezogen.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260317_064114.md; .\.venv\Scripts\python.exe scripts\check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency summary=fail:0,warn:2; .\.venv\Scripts\python.exe scripts\run_pytest_coverage.py --fail-under 80 PASS (coverage=91.23%; log=.tmp\results\reports\pytest_coverage_20260317_064421.log)
---

<!-- markdownlint-disable MD041 -->

Dev-DONELOG (Current Window)
============================

Hinweis
-------

- Aktives Fenster: nur Eintraege der letzten 14 Tage mit operativer Relevanz.
- Historik bleibt vollstaendig in den Archivdateien unter `novapolis-dev/archive/docs/donelogs/` erhalten.
- Technische Laufdetails gehoeren in Reports unter `.tmp/results/reports/` und werden hier nur zusammengefasst.

Current-Window Eintraege
------------------------

Dev/Process: Wochenabschluss-Nachholung dokumentiert (2026-03-17 06:45)
----------------------------------------------------------------------

- Nachhol-Lauf fuer den ausgefallenen Wochenabschluss gemaess `novapolis-dev/docs/process/abschluss-routine.ssot.md` ausgefuehrt und in Root-/Dev-Doku synchronisiert.
- `scripts/run_checks_and_report.py` liefert `overall=FAIL` wegen `doc-freshness`, `ruff` und `black`; `pytest`, `pyright`, `mypy` sowie alle Governance-Gates ausser Freshness PASS. Frisches Report-Artefakt: `.tmp/results/reports/checks_report_20260317_064114.md`.
- Separater Coverage-Lauf PASS (`91.23%` bei Hard Gate `>=80%`), separater Sim-Check ohne harte Fehler (`fail:0,warn:2`).
- KPI-Protokoll: `todo_index_drift=0`, `active_docs_stale=1` (`novapolis-dev/docs/brainstorming.rp.md`), `placeholder_conflicts=1` (offener Placeholder-Punkt bei `novapolis_agent/scripts/reports/generate_coverage_report.py`), `logs_policy_violations=0`.

Sim/Docs: Restverzeichnis des alten Nested-Aufbaus als Folgepunkt aufgenommen (2026-03-13 07:02)
-------------------------------------------------------------------------------------------

- Der Sim-Modulscan hat einen dritten offenen Punkt in `novapolis-dev/docs/todo.sim.md` angelegt.
- Das leere Restverzeichnis `novapolis-sim/novapolis-sim/` soll entfernt, klar markiert oder technisch begruendet werden, weil die aktive README den alten verschachtelten Aufbau bereits als nach `Backups/novapolis-sim-archived-20251104/` archiviert beschreibt.
- `novapolis-dev/docs/todo.index.md` wurde im selben Lauf fuer Sim auf `offen: 3` nachgezogen.

Dev/Docs: Historische Migrationsdoku als neuer Folgepunkt aufgenommen (2026-03-13 06:58)
-------------------------------------------------------------------------------

- Der D5-Scan des Dev-Hub hat einen weiteren bislang nicht erfassten Folgepunkt in `novapolis-dev/docs/todo.dev.md` angelegt.
- `novapolis-dev/migrations/docs-migration-2025-10-29.md` soll gegen die aktuelle Board-SSOT abgegrenzt oder nachgezogen werden, weil die Datei weiter `novapolis-dev/docs/todo.md` als Migrationsziel fuehrt, obwohl die aktive TODO-Struktur inzwischen ueber `todo.dev.md`, `todo.rp.md`, `todo.agent-board.md` und `todo.sim.md` laeuft.
- `novapolis-dev/docs/todo.index.md` wurde im selben Lauf fuer Dev auf `offen: 10` nachgezogen.

RP/Docs: README-Portabilitaet als neuer Folgepunkt aufgenommen (2026-03-13 04:04)
------------------------------------------------------------------------

- Der modulweise RP-Scan hat einen neuen Folgepunkt in `novapolis-dev/docs/todo.rp.md` angelegt.
- `novapolis-rp/README.md` soll auf portable aktive Einstiegsdoku nachgezogen werden, weil der Titel noch `Workspace (F:)` traegt und der Visualisierungsabschnitt einen lokalen Direktstart `uvicorn app.api.sim:app --host 127.0.0.1 --port 8765 --reload` dokumentiert.
- `novapolis-dev/docs/todo.index.md` wurde im selben Lauf fuer RP auf `offen: 6` nachgezogen.

Dev/Docs: Governance-Metadaten-Drift als neue Folgepunkte aufgenommen (2026-03-13 04:04)
-----------------------------------------------------------------------------

- Der Dev-Hub-Scan hat zwei weitere bislang ungetrackte Governance-Baustellen in `novapolis-dev/docs/todo.dev.md` aufgenommen.
- Neuer Folgepunkt 1: `novapolis-dev/docs/active-surface-index.md` auf reale `last_check`-Stande nachziehen, weil die aktiven Boards/Logs dort weiter auf `2026-03-04` stehen, obwohl sie im aktuellen Arbeitsfenster mehrfach geaendert wurden.
- Neuer Folgepunkt 2: `novapolis-dev/docs/meta/todo.json` auf aktive TODO-SSOT umstellen oder ausmustern, weil die Datei weiter auf das alte Sammelboard `novapolis-dev/docs/todo.md` und eine RP-Altzuordnung verweist.
- `novapolis-dev/docs/todo.index.md` wurde im selben Lauf fuer Dev auf `offen: 9` nachgezogen.

Sim/Docs: Modulscan oeffnet README- und Check-Drift im Sim-Modul (2026-03-13 04:04)
------------------------------------------------------------------------

- Der Sim-Scan hat zwei bislang nicht erfasste Folgepunkte in `novapolis-dev/docs/todo.sim.md` angelegt.
- Neuer Folgepunkt 1: `novapolis-sim/README.md` auf einen portablen Start-/Verify-Pfad umstellen, weil die Datei weiter eine lokal eingebettete Godot-Binary (`Godot_v4.5.1-stable_win64.exe`) und separate manuelle Startpfade dokumentiert.
- Neuer Folgepunkt 2: die von `novapolis-sim/scripts/Main.gd` erzeugten Sim-Checks auf den kanonischen Asset-Check mit `--allow-empty --check-slot-consistency` angleichen.
- `novapolis-dev/docs/todo.index.md` wurde im selben Lauf fuer Sim auf `offen: 2` nachgezogen.

Agent/Docs: Feinscan deckt Script-Doku- und Report-Drift auf (2026-03-13 04:02)
------------------------------------------------------------------------

- Zweite Tiefenwelle im Modul `novapolis_agent` hat zwei weitere bisher ungetrackte Folgepunkte belegt und in `novapolis-dev/docs/todo.agent-board.md` aufgenommen.
- Neuer Folgepunkt 1: `novapolis_agent/scripts/README.md` auf den realen Script-Bestand und den aktiven Root-`.venv`-/Wrapper-Flow nachziehen, weil die Datei weiter auf einem alten Minimalstand mit `run_eval.py` und freier `pip install`-Anleitung steht.
- Neuer Folgepunkt 2: historisches Placeholder-Verhalten der Report-Skripte explizit aufloesen oder stilllegen; belastbare Evidenz ist `novapolis_agent/scripts/reports/generate_coverage_report.py`, das bei fehlender `coverage.xml` weiterhin nur `Coverage-Report (placeholder)` erzeugt.
- `novapolis-dev/docs/todo.index.md` wurde fuer das Agent-Modul im selben Lauf auf `offen: 6` nachgezogen.

Agent/Docs: Modultiefenscan auf weitere Folgepunkte verdichtet (2026-03-13 03:53)
-------------------------------------------------------------------------

- Vertiefter Scan des Agent-Moduls hat drei weitere bislang ungetrackte Baustellen belegt und in `novapolis-dev/docs/todo.agent-board.md` aufgenommen.
- Neuer `Jetzt`-Punkt: `novapolis_agent/README.md` auf den aktuellen `.venv`-/Runbook-Betriebsweg synchronisieren, weil README noch `venv` und direkten `uvicorn app.main:app --reload` dokumentiert.
- Neue Folgepunkte: (1) `novapolis_agent/docs/DONELOG.txt` von einem widerspruechlichen alten FAIL-Postflight am Dokumentanfang bereinigen, (2) Legacy-Shim-Abbau nach abgeschlossener Inventarphase in eine explizite Exit-Stufe ueberfuehren.
- `novapolis-dev/docs/todo.index.md` wurde im selben Lauf fuer Agent auf `offen: 4` vorbereitet.

Dev/Docs: Workspace-Scan in neue offene Backlogpunkte ueberfuehrt (2026-03-13 03:45)
---------------------------------------------------------------------------

- Evidenzbasierter Drift-Scan ueber aktive Boards, Root-/Statusdokus und Agent-Skripte hat drei bisher nicht erfasste Baustellen sichtbar gemacht.
- `novapolis-dev/docs/todo.dev.md` enthaelt jetzt zwei neue offene Punkte: (1) aktive Root-/Dev-Dokuoberflaechen auf den letzten grünen Sammellauf synchronisieren, (2) VS-Code-Task-Launcher-Drift (`pwsh ... /d /c`, Exit 64) reproduzierbar pruefen und absichern.
- `novapolis-dev/docs/todo.agent-board.md` enthaelt jetzt einen neuen offenen Punkt fuer `novapolis_agent/scripts/todo_gather.py`, weil das Skript weiterhin auf das nicht mehr aktive Ziel `docs/TODO.md` verweist.
- `novapolis-dev/docs/todo.index.md` wurde im selben Lauf auf Dev `offen: 7` und Agent `offen: 1` synchronisiert.

Dev/Quality: Full-Gate wieder gruen + Coverage-Welle 1 gestartet (2026-03-11 07:24)
-------------------------------------------------------------------------------

- `scripts/run_checks_and_report.py` liefert wieder `overall=PASS` (inkl. `ruff`, `black`, `pyright`, `mypy`, `pytest`, Coverage-Gate `>=80%`).
- Coverage-Anstieg fuer den 91%-Pfad gestartet: Baseline `76.24%` auf `80.45%` angehoben.
- Testausbau in `novapolis_agent/tests/scripts/` begonnen (u. a. `test_build_project_context_index.py`, Erweiterungen in `test_summarize_marathon_kpis.py`, `test_build_eval_from_rp.py`, `test_check_dependency_profiles.py`).

Dev/Tests: Punkt 3 aktiviert, 90%-Ziel verankert (2026-03-11 07:07)
--------------------------------------------------------------------

- `novapolis-dev/docs/tests.md` von Alt-Prequel-Notizen auf aktuelle Test-/Coverage-Governance umgestellt (Hard Gate `>=80%`, verbindliches Qualitaetsziel `>=90%`, selektive `100%` nur fuer kleine kritische Module).
- `novapolis-dev/docs/process/abschluss-routine.ssot.md` um verbindliche Coverage-Zweistufenlogik erweitert und Nachweispflicht bei `<90%` fixiert.
- `novapolis-dev/docs/todo.dev.md` um einen abgeschlossenen Punkt-3-Eintrag ergaenzt; `novapolis-dev/docs/todo.index.md` auf den neuen Statushinweis synchronisiert.

Dev/Qualitaet: Folgezyklus gestartet, Punkt 1 begonnen (2026-03-11 06:57)
--------------------------------------------------------------------------

- `novapolis-dev/docs/todo.dev.md` um neue offene Optimierungspunkte erweitert (Gate-Stabilisierung, modernes Doku-Paket, ADR-Aktivierung, O11-Installblatt, KPI-Trendansicht).
- Punkt 1 aktiv gestartet: Ruff/Black-Restbefunde aus dem letzten Sammellauf in `scripts/check_todo_index_sync.py`, `novapolis_agent/scripts/build_eval_from_rp.py`, `novapolis_agent/scripts/summarize_marathon_kpis.py` und `novapolis_agent/tests/scripts/test_prepare_pack_smoke.py` behoben.
- Zwischenstand Coverage: Lint/Format sind fuer den betroffenen Scope gruen, Full-Gate bleibt wegen Coverage-Abstand (`76.24%` bei Ziel `>=80%`) offen.

Dev/Process: Woechentliche Hygiene-Cadence verankert (2026-03-11 06:49)
-----------------------------------------------------------------------

- Offener Dev-Board-Punkt abgeschlossen: 60-Minuten-Wochenslot fuer Drift-Scan, Donelog-Cleanup und TODO/Index-Abgleich verbindlich in `novapolis-dev/docs/process/abschluss-routine.ssot.md` dokumentiert.
- KPI-Protokollschema fixiert (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`) und Nachweisziel auf `novapolis-dev/docs/donelog.md` plus Root-Summary bei Abweichungen festgelegt.
- `novapolis-dev/docs/todo.index.md` auf `Dev offen: 0` und Metadaten (`keiner (offen: 0)`) synchronisiert.

Dev/Tooling: TODO-Index-CLI Rueckwaertskompatibel (2026-03-11 06:43)
---------------------------------------------------------------------

- `scripts/check_todo_index_sync.py` unterstuetzt wieder legacy Aufrufe mit `--root` (Alias auf `--repo-root`) und akzeptiert `--strict` als Deprecated-Noop.
- Ziel: Bestehende Wrapper-/Task-Aufrufe bleiben lauffaehig, waehrend die neue CLI (`--repo-root`, `--write-index-meta`) aktiv bleibt.

Dev/Docs: Receipt-Hygiene fuer Governance-Dokus finalisiert (2026-03-11 04:49)
------------------------------------------------------------------------

- `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `docs/adr/README.md` von temporaeren `checks: pending`-Markern auf echte Receipt-Zeilen umgestellt.
- `novapolis-dev/docs/donelog.md` Frontmatter auf denselben Lauf synchronisiert.
- Ergebnis: aktive Governance-Dokumente sind jetzt konsistent mit den laufenden Markdown-/Frontmatter-Gates.

Dev/Docs: README-Kompaktmodus + TODO-Index-Autowrite (2026-03-11 05:12)
------------------------------------------------------------------------

- `README.md` und `novapolis-dev/README.md` auf aktive Leseoberflaeche gestrafft; historische/temporäre Details explizit auf Archiv-/Statusquellen verwiesen.
- `scripts/check_todo_index_sync.py` um Auto-Write erweitert (`--write-index-meta`): Open-Counts und Board-Metadaten in `novapolis-dev/docs/todo.index.md` werden jetzt automatisch synchronisiert.
- Integration nachgezogen: `scripts/run_checks_and_report.py` und Task `Checks: todo index sync` verwenden den Auto-Write-Flag.
- Ergebnis: weniger manuelle Indexpflege und schnellere Onboarding-Lesbarkeit in den Haupt-READMEs.

Dev/Docs: Optimierungsbatch Aktiv-vs-Archiv + TODO-Konsistenz (2026-03-11 03:58)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.sim.md`: verbleibende offene Referenz-Checkbox (`scheduler-spec`) auf erledigt gesetzt; Sim-Board damit konsistent auf `offen: 0`.
- `novapolis-dev/docs/todo.index.md`: Sim-Open-Count von `1` auf `0` synchronisiert und Statushinweis `Sim v5.0` ergänzt.
- `README.md`: Archivregeln praezisiert (zentrales Dev-Archiv als Doku-SSOT; modulinterne Archive nur fuer technische/operative Artefakte).

Dev/Docs: Informationsarchitektur-Runde v2 (2026-03-11 04:27)
--------------------------------------------------------------

- Aktive Oberflaechen entlastet: `todo.sim.md` auf offene Punkte + Kurzkontext reduziert.
- TODO-Index operativ gestrafft: `todo.index.md` auf Kernstatus reduziert und um Board-Metadaten erweitert.
- `scripts/check_todo_index_sync.py` erweitert: Open-Count-Konsistenz, Widerspruchserkennung (`keine offenen` bei offenen Checkboxen) und Diagnoseausgaben.
- Archiv-/Log-Matrix in Root-`README.md` und `novapolis-dev/README.md` vereinheitlicht.
- Repo-Standards ergaenzt: `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `CHANGELOG.md`, `docs/adr/README.md`.

Dev/Docs: Root-DONELOG auf Summary-Ebene normalisiert (2026-03-11 04:46)
-------------------------------------------------------------------------

- `DONELOG.md` wurde auf einen bewusst kurzen Root-Summary-/Release-Log umgestellt.
- Detailhistorie bleibt im Archivpfad `novapolis-dev/archive/docs/donelogs/donelog_root.md` erhalten.
- Ziel: niedrigere kognitive Last auf Root-Ebene bei unveraenderter Nachvollziehbarkeit.

Dev/Docs: README-Finish fuer aktive Lesbarkeit (2026-03-11 04:46)
------------------------------------------------------------------

- Root-`README.md` um explizite Verweise auf `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `CHANGELOG.md` und `docs/adr/` ergaenzt.
- `novapolis-dev/README.md` von einem veralteten, ausserhalb des Frontmatters stehenden Checks-Receipt bereinigt und den Abschnitt `Checks & Reports` auf einen stabilen Dauertext umgestellt.
- Ergebnis: weniger Betriebsrauschen in aktiven READMEs und klarere Onboarding-Fuehrung fuer Maintainer/Contributors.

Archivhinweis
-------------

- Aeltere Current-Window-Eintraege bleiben unveraendert in Git-Historie und den Donelog-Archiven.
- Dieses aktive Dokument wird bewusst kurz gehalten und dient als menschlich lesbare Entscheidungs- und Fortschrittsansicht.
