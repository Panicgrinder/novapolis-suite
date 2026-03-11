---
stand: 2026-03-11 07:07
update: Coverage-Policy modernisiert und Punkt-3-Strategie mit verbindlichem 90%-Qualitaetsziel verankert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/tests.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/process/abschluss-routine.ssot.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-03-11 07:07); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-dev/docs/tests.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/process/abschluss-routine.ssot.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (EXITCODE=0, 2026-03-11 07:07)
---

Tests, Gates und Coverage-Policy
================================

Zweck
-----

Dieses Dokument definiert den verbindlichen Test- und Coverage-Rahmen fuer den Workspace.
Fokus ist reproduzierbare Qualitaet mit klaren Schwellwerten statt kurzfristiger "100%-Kosmetik".

Gate-Logik (verbindlich)
------------------------

- Hard Gate (blockierend): Gesamt-Coverage muss `>= 80%` sein.
- Qualitaetsziel (verbindlich fuer Steuerung): Gesamt-Coverage soll nachhaltig `>= 90%` erreichen und halten.
- Release-/Monatsabschluss-Regel: Ist die Coverage `< 90%`, gilt der Lauf als Qualitaets-Restpunkt und muss in TODO/DONELOG explizit nachverfolgt werden.
- 100%-Ziel nur fuer kleine, kritische Module mit klarer Logik und stabiler Testbarkeit (z. B. Parser/Validatoren/Normalizer), nicht als pauschale Repo-Vorgabe.

Coverage-Strategie (Punkt 3)
----------------------------

- Grosse Orchestrierungsdateien erhalten realistische Zielkorridore (`85-90%`) mit Schwerpunkt auf risikoreichen Branches.
- Kleine Kernmodule werden selektiv auf `100%` gebracht, wenn der Wartungsaufwand niedrig bleibt.
- Verboten: Coverage kuenstlich durch breite `omit`-Ausnahmen oder reine "Line-Hit"-Tests ohne Assertions schoenrechnen.

Messung und Nachweis
--------------------

- Standardlauf: `python scripts/run_checks_and_report.py`.
- Modullauf (Agent): `Set-Location novapolis_agent; ..\\.venv\\Scripts\\python.exe -m pytest --cov --cov-branch --cov-report=term-missing --cov-config .coveragerc --cov-fail-under=80`.
- Nachweisartefakte:
   - `.tmp/results/reports/checks_report_<timestamp>.md`
   - `outputs/test-artifacts/coverage.xml`
- Jeder Lauf mit Coverage `< 90%` wird als offener Qualitaetsrestpunkt in `novapolis-dev/docs/todo.dev.md` gefuehrt und in `novapolis-dev/docs/donelog.md` dokumentiert.

Priorisierte Hebel fuer den 90%-Pfad
------------------------------------

- Branch-Coverage in grossen Kernpfaden gezielt erhoehen, insbesondere:
   - `novapolis_agent/app/api/chat.py`
   - `novapolis_agent/app/tts/providers.py`
   - skriptnahe Kernpfade mit hoher Wirkung auf Eval/Runtime.
- Testdesign priorisiert Fehlermodi, Timeouts, Guardrails und Fallbacks (nicht nur Happy Path).

Verweise
--------

- Wochen-/Monatsrhythmus: `novapolis-dev/docs/process/abschluss-routine.ssot.md`
- Dev-Board: `novapolis-dev/docs/todo.dev.md`
- Dev-Index: `novapolis-dev/docs/todo.index.md`
- Dev-Log: `novapolis-dev/docs/donelog.md`


