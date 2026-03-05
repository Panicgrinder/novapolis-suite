---
stand: 2026-03-05 01:00
update: Strukturabschnitt auf Iststand korrigiert und Active-Surface-Index als Primärdokument verankert.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260305_005843.md
---

Novapolis Dev Hub
==================

Dieser Arbeitsbereich bündelt teamübergreifende Dokumentation, ToDos, DoneLogs und Migrationsnotizen für alle Novapolis-Projekte.
Der Dev Hub fungiert als gemeinsame Schaltstelle für Agent-, Sim- und RP-Teams und ersetzt die früheren verteilten „development“-Bereiche.

Zweck
-----

- Zentraler Anlaufpunkt für Entwicklungsunterlagen (Agent, Sim, RP)
- Gemeinsame Policies, Roadmaps, Integrationen
- Namenskonvention: Der Agent wird als "Chronistin von Novapolis" gefuehrt.
- Verweise auf produktive Repositories:
  - `novapolis_agent/`
  - `novapolis-sim/`
  - `novapolis-rp/`

Scope & Repos
-------------

Der Dev Hub verknüpft die Arbeitsstände aus `novapolis_agent/`, `novapolis-sim/` und `novapolis-rp/`. Alle teamweiten Policies, Planungen und Integrationen landen zentral hier und werden von dort aus in die Produktiv-Repositories gespiegelt.

Primary Docs
------------

- `docs/donelog.md` - tägliche Fortschritte und Beschlüsse
- `docs/todo.index.md` - TODO-Index (Navigation zu Modul-Boards)
  - Module: Dev `docs/todo.dev.md`, RP `docs/todo.rp.md`, Agent `docs/todo.agent-board.md`, Sim `docs/todo.sim.md`
- `.github/copilot-instructions.md` - Arbeitsweise, Stil, Sicherheitsleitplanken (SSOT)
- `docs/naming-policy.md` - verbindliche Dateibenennung im Verbund
- `docs/tests.md` - Testabdeckung und Sim-/Client-Checkliste
- `docs/active-surface-index.md` - Klassifikation ACTIVE/REFERENCE/HISTORICAL inkl. Owner/last_check

Contributor Workflow
--------------------

- Änderungen zuerst hier dokumentieren, anschließend in den Ziel-Repos umsetzen.
- Fortschritt stets in `docs/donelog.md` loggen; Aufgaben in den jeweiligen Modul-Boards pflegen (Dev `docs/todo.dev.md`, RP `docs/todo.rp.md`, Agent `docs/todo.agent-board.md`, Sim `docs/todo.sim.md`).
- Vor Commits die Leitlinien aus `.github/copilot-instructions.md` gegenprüfen.

Struktur
--------

- `docs/` - Arbeitsdokumente (ToDos, DoneLogs, Policies, Testpläne)
- `docs/meta/` - Metadaten zu den Arbeitsdokumenten
- `migrations/` - Änderungs- und Umzugshistorie
- `integrations/` - Schnittstellen- und Abstimmungsartefakte
- Produktive Datenpools liegen unter `../novapolis-rp/database-raw/` und `../novapolis-rp/database-curated/`; im Dev-Hub existieren dafuer keine gleichnamigen Top-Level-Verzeichnisse.

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

- Link-Scanner: `python scripts/scan_links.py`
  - Reports: `.tmp/results/reports/scan_links_*.log` und `.tmp/results/reports/scan_links_*.csv`
  - Status: 0 defekte Verweise (Rescan abgeschlossen)

checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'DONELOG.md' 'README.md' 'WORKSPACE_INDEX.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/README.md' 'novapolis-dev/docs/active-surface-index.md' 'novapolis-dev/docs/process/standalone-beta-gates.ssot.md' 'novapolis-dev/docs/donelog.md' 'novapolis-dev/docs/specs/tts-exporter-coqui.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md' 'todo.root.md' PASS (2026-03-04 00:47); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'DONELOG.md' 'README.md' 'WORKSPACE_INDEX.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/README.md' 'novapolis-dev/docs/active-surface-index.md' 'novapolis-dev/docs/process/standalone-beta-gates.ssot.md' 'novapolis-dev/docs/donelog.md' 'novapolis-dev/docs/specs/tts-exporter-coqui.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md' 'todo.root.md' PASS (EXITCODE=0, 2026-03-04 00:47)
------------

- Sammellauf-Skript: `python scripts/run_checks_and_report.py` (Lint: ruff/black, Docs-Lint markdownlint, Frontmatter-Validator, Typen: pyright/mypy, Tests + Coverage ≥80%; optionale Zusatz-Lints werden als SKIP protokolliert, falls nicht installiert)
- Report-Ausgabe: `.tmp/results/reports/checks_run_<timestamp>/` mit konsolidiertem Markdown- und JSON-Report pro Lauf
- Nutzung: Direktaufruf `python scripts/run_checks_and_report.py` (Wrapper-Policy bleibt aktiv). Exitcode aggregiert den ersten Pflicht-Check, der fehlschlägt.




