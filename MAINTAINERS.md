---
stand: 2026-03-19 11:09
update: Maintainer-Rahmen und Verantwortungszuschnitt fuer das Root-Repository dokumentiert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

Maintainers
===========

Aktueller Owner
---------------

- Primaerer Maintainer und Default-Owner: `@Panicgrinder`

Verantwortungszuschnitt
-----------------------

- Root-Governance und Workflows: `/.github/`, `README.md`, `DONELOG.md`
- Dev-Hub: `novapolis-dev/`
- Agent-Backend: `novapolis_agent/`
- RP-Modul: `novapolis-rp/`
- Sim-Modul: `novapolis-sim/`

Die verbindliche Review-Zuordnung liegt in `.github/CODEOWNERS`.

Maintainer-Aufgaben
-------------------

- Review und Priorisierung von Issues und Pull Requests
- Sicherstellen, dass Pflichtchecks, TODO-/DONELOG-Sync und Governance-Regeln eingehalten werden
- Pflege der aktiven Dokuoberflaeche und der Release-/Status-Summaries
- Entscheidung bei Konflikten ueber Scope, Archivierung und Freigabepfade

Erwartungen an PRs
------------------

- Scope klar begrenzen
- relevante Checks angeben
- bei Doku- oder Policy-Aenderungen die betroffenen Status-/DONELOG-Pfade mitziehen
- sicherheitsrelevante Funde nicht ueber oeffentliche Issues offenlegen

Verwandte Dokumente
-------------------

- `.github/CODEOWNERS`
- `CONTRIBUTING.md`
- `SUPPORT.md`
- `RELEASE.md`