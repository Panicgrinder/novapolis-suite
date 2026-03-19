---
stand: 2026-03-19 11:09
update: Akzeptierte Architekturentscheidung fuer die verbindliche Quality-Gate-Sequenz dokumentiert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

ADR 0002: Quality-Gate-Sequenz verbindlich festlegen
====================================================

- Status: accepted
- Datum: 2026-03-18

Kontext
-------

- Der Workspace fuehrt Qualitaetslaeufe ueber mehrere Tools und Module hinweg aus.
- Fuer reproduzierbare Ergebnisse muessen Reihenfolge, Bewertung und Nachweispflicht der Gates konsistent bleiben.
- Die aktuelle Test-Governance definiert bereits ein Hard Gate fuer Coverage (`>= 80%`), ein verbindliches Qualitaetsziel (`>= 90%`) und den operativen Wochen-/Monatsabschluss.

Entscheidung
------------

- Die verbindliche Quality-Gate-Sequenz fuer den Standardlauf lautet: `Lint -> Typen -> Tests -> Coverage`.
- Der bevorzugte Sammellauf ist `python scripts/run_checks_and_report.py`; fuer Coverage-Detailpruefungen bleibt `python scripts/run_pytest_coverage.py --fail-under 80` der kanonische Zusatzlauf.
- Die Coverage-Bewertung erfolgt in zwei Stufen:
  - Hard Gate: `>= 80%` ist blockierend.
  - Qualitaetsziel: `>= 90%` ist verbindlich fuer Steuerung, Abschlussroutinen und Nachweispflichten.
- Faellt die Coverage unter `90%`, wird dies nicht als stiller Normalzustand behandelt, sondern als offener Qualitaetsrestpunkt in Board und DONELOG gefuehrt.

Konsequenzen
------------

- Einzelne Teilchecks duerfen lokal selektiv laufen, aber der dokumentierte Referenzstatus fuer den Workspace stammt aus der festgelegten Sequenz.
- Abschlussroutinen, Boards und Logs muessen den Ausgang dieses Gate-Laufs im selben Lauf nachziehen.
- Die Sequenz reduziert Interpretationsspielraum bei Reviews und erleichtert die Einordnung von PASS/FAIL-Staenden ueber Root, Dev-Hub und Modulgrenzen hinweg.

Verweise
--------

- `novapolis-dev/docs/tests.md`
- `novapolis-dev/docs/process/abschluss-routine.ssot.md`
- `WORKSPACE_STATUS.md`
- `novapolis_agent/README.md`