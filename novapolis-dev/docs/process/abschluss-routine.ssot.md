---
stand: 2026-03-05 01:00
update: SSOT fuer Wochen- und Monatsabschluss eingefuehrt (Monatsabschluss am 1. Montag).
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260305_005843.md
---
Wochen- und Monatsabschluss (SSOT)
=================================

Zweck
-----

Dieses Dokument ist die verbindliche Referenz fuer den operativen Abschlussrhythmus im Novapolis-Workspace.

Geltung
-------

- Scope: gesamter Workspace (`Main/`), inklusive Root- und Modul-Dokumentation.
- Rhythmus:
  - Wochenabschluss: jede Arbeitswoche, standardmaessig montags.
  - Monatsabschluss: zusaetzlich am ersten Montag eines Monats (inkl. Wochenabschluss).

Triggerregeln
-------------

- Wochenabschluss wird durchgefuehrt, wenn seit dem letzten Abschluss neue relevante Aenderungen vorliegen (Code, Doku, Tests, Policies).
- Monatsabschluss wird am ersten Montag des Monats durchgefuehrt; faellt der Termin aus, erfolgt Nachholung am naechsten Werktag.

Ablauf Wochenabschluss (verbindlich)
------------------------------------

1. Qualitaetslauf in Reihenfolge:
   - `Checks: full`
   - optional `Checks: sim epoch assets`
   - `Tests: coverage (fail-under)`
2. Bei Strukturänderungen Tree-Artefakte aktualisieren (`Workspace tree:*`).
3. Abschluss-Sync im selben Lauf:
   - `todo.root.md`
   - `WORKSPACE_STATUS.md`
   - `DONELOG.md`
   - `novapolis-dev/docs/donelog.md`

Ablauf Monatsabschluss (zusaetzlich zum Wochenabschluss)
--------------------------------------------------------

1. Alle Schritte aus dem Wochenabschluss ausfuehren.
2. Monatsbezogene Drift-/Qualitaetsartefakte pruefen bzw. aktualisieren:
   - Agent-Baseline/Drift-Nachweise gem. `novapolis-dev/docs/todo.agent-board.md`
   - relevante Eval- und Trainingsartefakte auf Vollstaendigkeit pruefen.
3. Dokument-Hygiene pruefen:
   - offene und erledigte TODO-Bloecke auf Archivierungsreife pruefen
   - Statushinweise in `novapolis-dev/docs/todo.index.md` auf Konsistenz pruefen.
4. Monatsnotiz in den Logs dokumentieren:
   - Root: `DONELOG.md`
   - Dev-Hub: `novapolis-dev/docs/donelog.md`

Nachweisformat
--------------

- Jeder Abschlusslauf enthaelt mindestens:
  - Zeitpunkt (`YYYY-MM-DD HH:mm`)
  - ausgefuehrte Checks inkl. Ergebnis (PASS/FAIL)
  - benannte Sync-Zieldateien
  - offene Restpunkte (falls vorhanden)

Referenzen
----------

- Root-Einstieg: `README.md` (Kurzverweis auf diese SSOT)
- Arbeitsstatus: `WORKSPACE_STATUS.md`
- Root-Backlog: `todo.root.md`
- Dev-Logs: `novapolis-dev/docs/donelog.md`
- Root-Log: `DONELOG.md`

