---
stand: 2026-03-11 07:02
update: Neuer Dev-Optimierungszyklus gestartet; Punkt 1 (Gate-Stabilisierung) begonnen.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc README.md novapolis-dev/README.md DONELOG.md novapolis-dev/docs/donelog.md SECURITY.md CODE_OF_CONDUCT.md CHANGELOG.md docs/adr/README.md PASS (2026-03-11 04:49); .\.venv\Scripts\python.exe scripts/check_frontmatter.py README.md novapolis-dev/README.md DONELOG.md novapolis-dev/docs/donelog.md SECURITY.md CODE_OF_CONDUCT.md CHANGELOG.md docs/adr/README.md PASS (EXITCODE=0, 2026-03-11 04:49)
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
