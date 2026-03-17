---
stand: 2026-03-17 16:58
update: Wochenabschluss-Nachholung im Index-Hinweis nachgezogen; Board-Metadaten auf aktuellen Stand gebracht.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260317_064114.md; .\.venv\Scripts\python.exe scripts\check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency summary=fail:0,warn:2; .\.venv\Scripts\python.exe scripts\run_pytest_coverage.py --fail-under 80 PASS (coverage=91.23%; log=.tmp\results\reports\pytest_coverage_20260317_064421.log)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 6)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 10)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 6)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 3)

Statushinweise (aktuell)
------------------------

- Dev v5.8: Wochenabschluss-Nachholung 2026-03-17 dokumentiert; `overall=FAIL` bleibt wegen `doc-freshness`, `ruff` und `black`, waehrend Coverage separat mit `91.23%` PASS und der Sim-Check mit `fail:0,warn:2` belegt ist.
- Dev v5.7: Historische Migrationsdoku (`docs-migration-2025-10-29.md`) als neuer Folgepunkt aufgenommen (`offen: 9 -> 10`).
- Sim v5.2: Restverzeichnis des alten Nested-Sim-Aufbaus als neuer Folgepunkt aufgenommen (`offen: 2 -> 3`).
- RP v5.1: README-Portabilitaet und Visualisierungsstart als neuer Folgepunkt aufgenommen (`offen: 5 -> 6`).
- Dev v5.6: Governance-Metadaten-Drift (`active-surface-index`, `docs/meta/todo.json`) als neue Folgepunkte aufgenommen (`offen: 7 -> 9`).
- Dev v5.5: Workspace-Doku-Receipt-Drift und VS-Code-Task-Launcher-Drift als neue Folgepunkte aufgenommen (`offen: 5 -> 7`).
- Agent v5.3: Script-Doku-Drift und historisches Placeholder-Reporting als neue Folgepunkte aufgenommen (`offen: 4 -> 6`).
- Agent v5.2: README-Onboarding, DONELOG-Hygiene und Shim-Exit als Folgepunkte aus dem Modultiefenscan aufgenommen (`offen: 1 -> 4`).
- Agent v5.1: Legacy-TODO-Automation (`todo_gather.py`) als neuer offener Driftpunkt aufgenommen (`offen: 0 -> 1`).
- Sim v5.1: README-Portabilitaet und Hub-Check-Drift als neue Folgepunkte aufgenommen (`offen: 0 -> 2`).
- Dev v5.3: Coverage-Punkt 3 gestartet; 90%-Qualitaetsziel jetzt verbindlich in Dev-Tests/Abschlussprozess verankert.
- Dev v5.4: Punkt 1 (Full-Gate) geschlossen; Coverage-Welle 1 Richtung `91%` gestartet (`76.24% -> 80.45%`).
- Dev v5.2: Folgezyklus fuer Gate-Stabilisierung und modernes Doku-Basispaket gestartet (`offen: 0 -> 5`).
- Dev v5.1: Woechentliche Hygiene-Cadence mit KPI-Tracking verbindlich dokumentiert (`offen: 1 -> 0`).
- Sim v5.0: Sim-Board konsolidiert, verbleibende Mikrodrift geschlossen (`offen: 1 -> 0`).
- Index v2.0: Operative Anzeige erweitert um Board-Metadaten (letzte Aenderung, aeltester offener Punkt, Widerspruchscheck).

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-03-11 | - [ ] [Jetzt] Coverage-Sprint Richtung `91%` starten (Welle 1: skriptnahe Low-Coverage-Module). | nein |
| RP (`docs/todo.rp.md`) | 2026-03-05 | - [ ] [Als naechstes] Danach erst Mengen-Backfill in Inventaren (D5/C6/Fraktionen) starten. | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-03-11 | - [ ] [Als naechstes] Legacy-TODO-Automation auf aktuelle SSOT-Pfade und Nutzbarkeit bereinigen oder geordnet stilllegen. | nein |
| Sim (`docs/todo.sim.md`) | 2026-03-11 | - [ ] [Als naechstes] Sim-README auf den portablen Start-/Verify-Pfad ohne lokal eingebettete Godot-Binary synchronisieren. | nein |


Hinweise (Index)
----------------

- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.
- Automationscheck: `scripts/check_todo_index_sync.py` liefert zusaetzlich Metadaten zu letzter Board-Aenderung, aeltestem offenen Punkt und Widerspruchen.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





