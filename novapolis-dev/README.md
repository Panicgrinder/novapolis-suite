---
stand: 2026-03-28 06:51
update: Phase-2-Konsistenzlauf zieht den Dev-Hub auf repo-relative Referenzen und einen einheitlichen Root-Wrapper-Rahmen nach.
checks: markdownlint PASS; frontmatter PASS; path-portability PASS; logs-policy PASS (2026-03-28 01:23)
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
- Aktive Oberflaeche bewusst kurz halten: nur operative Doku, keine langen historischen Laufprotokolle.

Struktur
--------

- `docs/` - Arbeitsdokumente (ToDos, DoneLogs, Policies, Testpläne)
- `docs/meta/` - Metadaten zu den Arbeitsdokumenten
- `migrations/` - Änderungs- und Umzugshistorie
- `integrations/` - Schnittstellen- und Abstimmungsartefakte
- Produktive Datenpools liegen unter `novapolis-rp/database-raw/` und `novapolis-rp/database-curated/`; im Dev-Hub existieren dafuer keine gleichnamigen Top-Level-Verzeichnisse.

Archiv
------

- Zentrales Archiv für historisierte Dokumente: `archive/`
- Modulinterne Archive bleiben fuer technische/operative Artefakte zulaessig (`novapolis_agent/archive/`, `Backups/`), sind aber keine aktive Governance-Quelle.

Archiv-Matrix (verbindlich)
---------------------------

| Ablageort | Zweck | Zaehlt als aktive Regelquelle |
| --- | --- | --- |
| `novapolis-dev/docs/**` | Aktive Dev-Hub-Dokumentation | ja |
| `novapolis-dev/archive/**` | Historisierte Dev-Dokumentation | nein |
| `novapolis_agent/archive/**` | Modulintern technische/operative Artefakte | nein |
| `Backups/**` | Forensische Backup-/Restore-Artefakte | nein |

DONELOG-Ebenen
--------------

| Ebene | Datei/Pfad | Zweck |
| --- | --- | --- |
| A | `docs/donelog.md` | Operativer Kurzlog (entscheidungsrelevante Zusammenfassung) |
| B | `.tmp/results/reports/**` | Laufbelege/Diagnosedetails |
| C | `DONELOG.md` | Root-Summary fuer globale Releases/Governance |

Copilot Instructions
--------------------

- Kanonisches Richtlinien-Dokument liegt im Repo-Root unter `.github/copilot-instructions.md` (SSOT).

Bitte dokumentiert neue Arbeitsstände ausschließlich hier und verweist in den Produktiv-Repositories auf dieses Hub.

Historie & Detailprotokolle
---------------------------

- Historisierte Dev-Doku liegt unter `novapolis-dev/archive/`.
- Root-Detailhistorie liegt unter `novapolis-dev/archive/docs/donelogs/donelog_root.md`.
- Maschinenlesbare Laufdetails liegen unter `.tmp/results/reports/`.

Checks & Reports
----------------

- Sammellauf-Skript: `& .\.venv\Scripts\python.exe scripts/run_checks_and_report.py` (Lint: ruff/black, Docs-Lint markdownlint, Frontmatter-Validator, Typen: pyright/mypy, Tests + Coverage >=80%; optionale Zusatz-Lints werden als SKIP protokolliert, falls nicht installiert).
- Report-Ausgabe: `.tmp/results/reports/checks_run_<timestamp>/` mit konsolidiertem Markdown- und JSON-Report pro Lauf.
- Nutzung: Direktaufruf aus dem Repo-Root; der aktuelle Referenzstand ist `overall=PASS` aus `WORKSPACE_STATUS.md` (Wochenabschluss 2026-03-27). Exitcode aggregiert den ersten Pflicht-Check, der fehlschlaegt.




