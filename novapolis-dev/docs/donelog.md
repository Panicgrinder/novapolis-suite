---
stand: 2026-03-19 11:09
update: KPI-Trendansicht fuer die Hygiene-Cadence angelegt und das Dev-Board damit geschlossen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
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

Dev/KPI: Trendansicht fuer Hygiene-Cadence verankert (2026-03-19 11:01)
-----------------------------------------------------------------------

- `novapolis-dev/docs/meta/dev-kpi-trends.md` angelegt und die vier Kernmetriken (`todo_index_drift`, `active_docs_stale`, `placeholder_conflicts`, `logs_policy_violations`) ueber vier dokumentierte Slots vergleichbar zusammengefuehrt.
- Der aktuelle Slot 2026-03-19 ist direkt ueber `scripts/check_todo_index_sync.py`, `scripts/check_doc_freshness.py` und `scripts/check_logs_policy.py` belegt; offene Placeholder-/Truthfulness-Konflikte im aktiven Dev-Bestand wurden zusaetzlich gegengeprueft.
- `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf `Dev offen: 0` synchronisiert.

Dev/Beta: Externes Installblatt fuer die Standalone-Beta angelegt (2026-03-18 22:47)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/process/standalone-beta-installblatt.md` neu angelegt; der Text richtet sich explizit an Dritte ohne implizites Repo-Wissen.
- Abgedeckt sind Voraussetzungen, Setup, API-/Sim-Start, Verifikation, Go/No-Go und Troubleshooting.
- `README.md`, `todo.root.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf den geschlossenen O11-Stand synchronisiert.

Dev/Community: Maintainer- und Contributor-Paket aufgebaut (2026-03-18 22:40)
-------------------------------------------------------------------------

- Root-Docs `SUPPORT.md`, `RELEASE.md` und `MAINTAINERS.md` als scanbare Einstiegsschicht fuer Support, Release-Rahmen und Verantwortlichkeiten angelegt.
- Root-GitHub-Templates unter `.github/ISSUE_TEMPLATE/` sowie `.github/pull_request_template.md` ergaenzt.
- `README.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf den neuen Iststand synchronisiert; Dev-Open-Count reduziert sich auf `2`.

Dev/Architecture: ADR-Ordner aktiviert (2026-03-18 22:36)
---------------------------------------------------------

- `docs/adr/0001-donelog-ebenen.md` als akzeptierte Entscheidung fuer die normalisierten DONELOG-Ebenen angelegt.
- `docs/adr/0002-quality-gate-sequenz.md` als akzeptierte Entscheidung fuer die verbindliche Reihenfolge `Lint -> Typen -> Tests -> Coverage` und die Coverage-Zweistufenlogik angelegt.
- `docs/adr/README.md` um einen aktiven ADR-Index erweitert; `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` auf `Dev offen: 3` synchronisiert.

Dev/Governance: Status- und Board-Sync auf PASS-Referenzlauf gezogen (2026-03-18 22:20)
-------------------------------------------------------------------------------

- `WORKSPACE_STATUS.md`, `todo.root.md`, `novapolis-dev/docs/todo.dev.md` und `novapolis-dev/docs/todo.index.md` vom veralteten 2026-03-10/11-Stand auf den dokumentierten PASS-Lauf `checks_report_20260318_052318.md` gehoben.
- Der Dev-Punkt `Coverage-Sprint Richtung 91%` wurde evidenzbasiert abgeschlossen; der aktuelle Referenzwert liegt bei `93.69%` statt der zuvor noch gefuehrten Zwischenmarke `80.45%`.
- Open-Count im Dev-Board/Index reduziert (`5 -> 4`); naechster offener Dev-Schwerpunkt ist jetzt das Community-/Maintainer-Doku-Paket.

Dev/Docs: RP-Brainstorming archiviert, ACTIVE-Oberflaeche bereinigt (2026-03-18 05:20)
-------------------------------------------------------------------------------

- `novapolis-dev/docs/brainstorming.rp.md` aus dem aktiven Dev-Bestand entfernt und nach `novapolis-dev/archive/docs/others/brainstorming.rp.archive.2026-03-18.md` ueberfuehrt.
- `novapolis-dev/docs/active-surface-index.md` auf den neuen Ist-Stand synchronisiert; der RP-Brainstorming-Eintrag zaehlt nicht mehr zur ACTIVE-Oberflaeche.
- `.github/instructions/mind-cluster.instructions.md` vom toten Aktivpfad bereinigt; Brainstorming-Regel bleibt generisch fuer kuenftige aktive Brainstorming-Dokumente bestehen.

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
