---
stand: 2026-03-19 11:09
update: Schlanken Release-Rahmen fuer Root-Checks, Doku-Sync und Changelog festgelegt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

Release-Prozess
===============

Zweck
-----

Dieses Dokument beschreibt den minimalen Release-Rahmen fuer nachvollziehbare, reproduzierbare Veroeffentlichungen im Root-Repository.

Freigabekriterien
-----------------

- Der aktuelle Referenzlauf ist gruen:
  - `scripts/run_checks_and_report.py` liefert `overall=PASS`.
- Betroffene TODO-/Status-/DONELOG-Dateien sind im selben Lauf synchronisiert.
- Release-notable Aenderungen sind in `CHANGELOG.md` erfasst.
- Fuer Standalone-Beta-Entscheidungen gelten zusaetzlich die Gates aus `README.md` und `novapolis-dev/docs/process/standalone-beta-gates.ssot.md`.

Empfohlene Reihenfolge
----------------------

1. Arbeitsstand bereinigen und Scope scharf ziehen.
2. Vollcheck ausfuehren:
   - `& .\.venv\Scripts\python.exe scripts\run_checks_and_report.py`
3. Bei Strukturdelta optional Tree-Artefakte aktualisieren.
4. Doku-Sync im selben Lauf:
   - `todo.root.md`
   - `WORKSPACE_STATUS.md`
   - `DONELOG.md`
   - `novapolis-dev/docs/donelog.md`
5. `CHANGELOG.md` fuer release-notable Punkte nachziehen.

Release-Artefakte
-----------------

- Root-Summary: `DONELOG.md`
- technische Laufbelege: `.tmp/results/reports/**`
- aenderungsbezogene Historie: `CHANGELOG.md`

Nicht-Ziele
-----------

- Dieses Dokument ersetzt keine modulinternen Release- oder Exportprozesse.
- Es definiert bewusst keinen semantischen Versionierungszwang fuer das Gesamt-Repo.

Verwandte Dokumente
-------------------

- `CHANGELOG.md`
- `README.md`
- `novapolis-dev/docs/process/abschluss-routine.ssot.md`
- `novapolis-dev/docs/donelog.md`