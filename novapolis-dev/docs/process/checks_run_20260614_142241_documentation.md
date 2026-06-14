---
stand: 2026-06-14 14:25
update: Dokumentation des Wrapper-Checklaufs mit Governance-Optionen
checks: overall=FAIL; ruff=FAIL; black=FAIL; pytest=PASS; report=.tmp/results/reports/checks_report_20260614_142241.md
---

Kurzbeschreibung
-----------------

Dieser Eintrag dokumentiert den konsolidierten Repository-Checklauf, ausgeführt mit den erweiterten Governance-Optionen:

- `--update-workspace-tree` (vor `doc-freshness`)
- `--write-snapshot-lock` (schreibt `.snapshot.now`)
- `--sync-docs-after-checks` (führt `scripts/sync_docs_after_checks.py` nach dem Report aus)

Ergebnis (Kurz)
---------------

- Gesamt-Gate: FAIL
- Fehlende/Problematische Checks: `ruff` (4 findings), `black` (1 finding)
- Alle anderen Pflicht-Checks: PASS
- Pytest: PASS (709 tests)
- Coverage: ~93.8%

Berichte und Logs
-----------------

- Konsolidierter Markdown-Report: .tmp/results/reports/checks_report_20260614_142241.md
- JSON-Summary: .tmp/results/reports/checks_report_20260614_142241.json
- Detaillogs (Auswahl):
  - .tmp/results/reports/checks_run_20260614_142241/ruff.log
  - .tmp/results/reports/checks_run_20260614_142241/black.log
  - .tmp/results/reports/checks_run_20260614_142241/pytest.log

Empfohlene nächste Schritte
--------------------------

1. Öffne `.tmp/results/reports/checks_run_20260614_142241/ruff.log` und `.tmp/results/reports/checks_run_20260614_142241/black.log` und behebe die gemeldeten Stil-/Formatfehler.
2. Optional: `python -m ruff check --fix ...` / `python -m black ...` lokal ausprobieren.
3. Nach Fixes: `.\.venv\Scripts\python.exe scripts\run_checks_and_report.py --update-workspace-tree --write-snapshot-lock --sync-docs-after-checks` erneut laufen lassen, bis `overall=PASS`.

Kontext
-------

Der Lauf wurde automatisiert mit den Governance-Flags gestartet, um die häufig manuell ausgeführten Schritte in einem konsolidierten Ablauf verfügbar zu machen. Das entspricht dem Vorschlag, den Wrapper um optionale Governance-Tools zu erweitern, um Ordnung herzustellen und repetitive Einzelaufrufe zu vermeiden.
