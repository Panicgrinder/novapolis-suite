---
stand: 2026-03-28 06:51
update: Phase-2-Konsistenzlauf zieht die Abschluss-SSOT auf den aktuellen PASS-Kontext und explizite Root-Wrapper fuer die Hygiene-Cadence.
checks: markdownlint PASS; frontmatter PASS; path-portability PASS; logs-policy PASS (2026-03-28 01:31)
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
   - Coverage-Bewertung verbindlich in zwei Stufen:
     - Hard Gate: `>=80%` (blockierend)
     - Qualitaetsziel: `>=90%` (verbindlicher Restpunkt bei Unterschreitung)
2. Bei Strukturänderungen Tree-Artefakte aktualisieren (`Workspace tree:*`).
3. Abschluss-Sync im selben Lauf:
   - `todo.root.md`
   - `WORKSPACE_STATUS.md`
   - `DONELOG.md`
   - `novapolis-dev/docs/donelog.md`

Woechentliche Hygiene-Cadence (60 Minuten)
------------------------------------------

- Termin: jede Woche ein fester 60-Minuten-Slot direkt nach dem Wochenabschluss.
- Reihenfolge (verbindlich):
   1. Drift-Scan: `& .\.venv\Scripts\python.exe scripts/check_todo_index_sync.py --repo-root . --write-index-meta`, `& .\.venv\Scripts\python.exe scripts/check_doc_freshness.py`, `& .\.venv\Scripts\python.exe scripts/check_logs_policy.py --repo-root .`.
   2. Donelog-Cleanup: aktive Eintraege auf operative Relevanz kuerzen, Historik in `novapolis-dev/archive/docs/donelogs/` belassen.
   3. TODO/Index-Abgleich: offene Punkte in Modul-Boards gegen `novapolis-dev/docs/todo.index.md` verifizieren.
- KPI-Protokoll (Pflichtfelder je Slot):
   - `todo_index_drift`: Anzahl erkannter Count-/Board-Widersprueche.
   - `active_docs_stale`: Anzahl aktiver Dokumente mit SLA-Ueberschreitung.
   - `placeholder_conflicts`: Anzahl erkannter Platzhalter-/Iststand-Widersprueche.
   - `logs_policy_violations`: Anzahl policy-widriger Logdateien im aktiven Pfad.
- Nachweis: KPI-Werte und Kurzfazit in `novapolis-dev/docs/donelog.md` dokumentieren; bei Abweichungen zusaetzlich Root-Summary in `DONELOG.md` aktualisieren.

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
5. Coverage-Qualitaetsstatus explizit festhalten:
   - Bei `<90%` muss ein offener Restpunkt im Dev-Board bestehen (`novapolis-dev/docs/todo.dev.md`) und ein kurzer Nachholplan im Dev-DONELOG notiert sein.

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

