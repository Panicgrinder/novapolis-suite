---
stand: 2026-03-27 09:54
update: Dev-KPI-Trendansicht um den Wochenabschluss-Slot vom 2026-03-27 erweitert; die vier Hygiene-Kernmetriken stehen wieder auf Null.
checks: scripts/run_checks_and_report.py overall=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; grep open placeholder/truthfulness conflicts in active dev docs PASS
---

Dev KPI Trends
==============

Zweck
-----

Diese Uebersicht macht die vier Hygiene-Kernmetriken der woechentlichen Dev-Cadence ueber mehrere dokumentierte Slots vergleichbar sichtbar.

KPI-Definitionen
----------------

- `todo_index_drift`: erkannte Count- oder Board-Widersprueche aus `scripts/check_todo_index_sync.py`.
- `active_docs_stale`: Anzahl stale aktiver Dev-Dokumente aus `scripts/check_doc_freshness.py`.
- `placeholder_conflicts`: explizit offene Placeholder-/Truthfulness-Konflikte im aktiven Dev-Bestand.
- `logs_policy_violations`: policy-widrige aktive Log-Artefakte aus `scripts/check_logs_policy.py`.

Ableitungsregel
---------------

- Wenn fuer einen Slot ein direkter Scriptlauf dokumentiert ist, gilt dessen Ergebnis.
- Wenn ein Slot nur ueber einen konsolidierten PASS-Status dokumentiert ist, werden `todo_index_drift`, `active_docs_stale` und `logs_policy_violations` aus den gemeldeten PASS-Gates abgeleitet.
- `placeholder_conflicts` wird aus offenen, explizit dokumentierten Placeholder-/Truthfulness-Punkten im aktiven Dev-Bestand abgeleitet. Fuer die unten aufgefuehrten Slots ist kein offener Konflikt dokumentiert; relevante Driftpunkte sind jeweils als erledigt markiert.

Trend-Slots
-----------

| Slot | Zeitpunkt | todo_index_drift | active_docs_stale | placeholder_conflicts | logs_policy_violations | Basis |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| S1 | 2026-03-10 15:40 | 0 | 0 | 0 | 0 | `WORKSPACE_STATUS.md`: Governance-Gates `todo-index-sync`, `doc-freshness`, `logs-policy` PASS; keine offene Truthfulness-/Placeholder-Aufgabe im aktiven Dev-Board |
| S2 | 2026-03-18 05:24 | 0 | 0 | 0 | 0 | `.tmp/results/reports/checks_report_20260318_052318.md`: PASS fuer `todo-index-sync`, `doc-freshness`, `logs-policy`; aktive Driftpunkte bereits geschlossen |
| S3 | 2026-03-18 22:47 | 0 | 0 | 0 | 0 | O11-Sync auf gruenem Referenzlauf; aktiver Dev-Bestand zeigt keinen offenen Placeholder-/Truthfulness-Konflikt und keinen offenen Hygiene-Blocker mehr |
| S4 | 2026-03-19 11:01 | 0 | 0 | 0 | 0 | Direktlauf `scripts/check_todo_index_sync.py`, `scripts/check_doc_freshness.py`, `scripts/check_logs_policy.py`; Grep auf offene Placeholder-/Truthfulness-Konflikte im aktiven Dev-Bestand ohne Treffer |
| S5 | 2026-03-27 01:16 | 0 | 0 | 0 | 0 | `.tmp/results/reports/checks_report_20260327_011507.md`: PASS fuer `todo-index-sync`, `doc-freshness`, `logs-policy`; Grep auf offene Placeholder-/Truthfulness-Konflikte im aktiven Dev-Bestand ohne Treffer |

Kurzfazit
---------

- Die vier Kernmetriken liegen ueber alle fuenf dokumentierten Slots stabil bei `0`.
- Der verbleibende Dev-Backlog ist damit kein Hygiene- oder Governance-Blocker mehr, sondern nur noch normale Ausbauarbeit ausserhalb der Cadence-KPIs.

Quellen
-------

- `novapolis-dev/docs/process/abschluss-routine.ssot.md`
- `WORKSPACE_STATUS.md`
- `.tmp/results/reports/checks_report_20260318_052318.md`
- `.tmp/results/reports/checks_report_20260327_011507.md`
- `novapolis-dev/docs/todo.dev.md`
- `novapolis-dev/docs/donelog.md`