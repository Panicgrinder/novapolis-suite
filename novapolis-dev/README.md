---
stand: 2025-11-12 03:37
update: Abschnitt Checks: full (PSScriptAnalyzer + Sammellauf) ergänzt
checks: pending (nach Lint/Validator)
---

Novapolis Dev Hub
==================

Dieser Arbeitsbereich bündelt teamübergreifende Dokumentation, ToDos, DoneLogs und Migrationsnotizen für alle Novapolis-Projekte.
Der Dev Hub fungiert als gemeinsame Schaltstelle für Agent-, Sim- und RP-Teams und ersetzt die früheren verteilten „development“-Bereiche.

Zweck
-----

- Zentraler Anlaufpunkt für Entwicklungsunterlagen (Agent, Sim, RP)
- Gemeinsame Policies, Roadmaps, Integrationen
- Verweise auf produktive Repositories:
  - `novapolis_agent/`
  - `novapolis-sim/`
  - `novapolis-rp/`

Scope & Repos
-------------

Der Dev Hub verknüpft die Arbeitsstände aus `novapolis_agent/`, `novapolis-sim/` und `novapolis-rp/`. Alle teamweiten Policies, Planungen und Integrationen landen zentral hier und werden von dort aus in die Produktiv-Repositories gespiegelt.

Primary Docs
------------

- `docs/donelog.md` – tägliche Fortschritte und Beschlüsse
- `docs/todo.index.md` – TODO-Index (Navigation zu Modul-Boards)
  - Module: Dev `docs/todo.dev.md`, RP `docs/todo.rp.md`, Agent `docs/todo.agent.md`, Sim `docs/todo.sim.md`
- `.github/copilot-instructions.md` – Arbeitsweise, Stil, Sicherheitsleitplanken (SSOT)
- `docs/naming-policy.md` – verbindliche Dateibenennung im Verbund
- `docs/tests.md` – Testabdeckung und Sim-/Client-Checkliste

Contributor Workflow
--------------------

- Änderungen zuerst hier dokumentieren, anschließend in den Ziel-Repos umsetzen.
- Fortschritt stets in `docs/donelog.md` loggen; Aufgaben in den jeweiligen Modul-Boards pflegen (Dev `docs/todo.dev.md`, RP `docs/todo.rp.md`, Agent `docs/todo.agent.md`, Sim `docs/todo.sim.md`).
- Vor Commits die Leitlinien aus `.github/copilot-instructions.md` gegenprüfen.

Struktur
--------

- `docs/` – Arbeitsdokumente (ToDos, DoneLogs, Policies, Testpläne)
- `docs/meta/` – Metadaten zu den Arbeitsdokumenten
- `migrations/` – Änderungs- und Umzugshistorie
- `roadmaps/` – Langfristige Planungen (Platzhalter)
- `integrations/` – Schnittstellen- und Abstimmungsdokumente (Platzhalter)
- `raw/`, `curated/` – optionale lokale Skizzen; produktive Datenpools liegen unter `../novapolis-rp/database-*`

Archiv
------

- Zentrales Archiv für historisierte Dokumente: `archive/`
- Bitte keine separaten Archive in Unterprojekten anlegen; verlinkt stattdessen nach `novapolis-dev/archive/`.

Copilot Instructions
--------------------

- Kanonisches Richtlinien-Dokument liegt im Repo-Root unter `.github/copilot-instructions.md` (SSOT).

Bitte dokumentiert neue Arbeitsstände ausschließlich hier und verweist in den Produktiv-Repositories auf dieses Hub.


Temporäre Bereiche
------------------

- Link-Scanner: `scripts/scan_links.ps1`
  - Reports: `.tmp-results/reports/scan_links_reports/`
  - Kandidaten (Dry-Run JSON): `.tmp-results/reports/links/*.json`
  - Status: 0 defekte Verweise (Rescan abgeschlossen)

Checks: full
------------

- Sammellauf-Skript: `scripts/run_checks_and_report.ps1` (Lint: ruff/black, Docs-Lint markdownlint, Frontmatter-Validator, Typen: pyright/mypy, Tests + Coverage ≥80%, PSScriptAnalyzer)
- Report-Ausgabe: `.tmp-results/reports/checks_report_*.md` inkl. JSON-Blöcken & Postflight-Vorlage
- Nutzung: Wrapper-Aufruf `pwsh -File scripts/run_checks_and_report.ps1` (keine Inline-Ketten). Exitcode aggregiert ersten Fehler.

