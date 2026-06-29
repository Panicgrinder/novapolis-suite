---
stand: 2026-06-29 16:07
update: Wochenabschluss 2026-06-29 ist im TODO-Index synchronisiert; Open-Counts bleiben stabil und der Freshness-Repair ist dokumentiert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260629_155310.md; snapshot-lock PASS (2026-06-29 16:07)

---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 2)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 6)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 1)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 1)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` fuehrt aktuell zwei offene Querschnittspunkte fuer den Korrektur-Planlauf des Governance-Umbaus und bleibt bewusst ausserhalb der Modul-Open-Counts.

- Wochenabschluss 2026-06-29: Der initiale Full-Check fiel nur an `doc-freshness` (`74` stale Dokus); der Recheck nach Freshness-Repair ist wieder vollstaendig PASS (`.tmp/results/reports/checks_report_20260629_155005.md`).

- Dev: `novapolis-dev/docs/todo.dev.md` fuehrt jetzt sechs offene Korrekturpunkte fuer Kettenregel, Bootstrap, Berichtsvertraege, Scope-/Wiring-Audit, semantische Autoritaetsverdrahtung und nachgelagertes Hook-Logging.

- Agent: `novapolis-dev/docs/todo.agent-board.md` fuehrt einen offenen Governance-Umbaupunkt fuer die operative Agent-Runtime-Projektion inklusive mini-first/Handoff/Gate-Nachweis.

- RP: `novapolis-dev/docs/todo.rp.md` fuehrt zwei offene Punkte: den laufenden Nordlinie-Fachpunkt plus den Governance-Umbaupunkt fuer die RP-SSOT-to-Runtime-Projektion.

- Sim: `novapolis-dev/docs/todo.sim.md` fuehrt einen offenen Governance-Umbaupunkt als Sim-Bruecke in die Root-/Dev-Planlandschaft.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-06-19 | - [ ] [Jetzt] Kettenregel verbindlich machen: Plantraeger vor Analyse und Mutation. | nein |
| RP (`docs/todo.rp.md`) | 2026-06-19 | - [ ] [Jetzt] Nordlinie-Folgepaket in drei Zuegen schliessen und Reflex-Herkunft gegen Datenrettung pruefen. | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-06-19 | - [ ] [Als naechstes] Agent-Runtime-Projektion fuer den Governance-Umbau als belegten Umsetzungsstrang fuehren. | nein |
| Sim (`docs/todo.sim.md`) | 2026-06-19 | - [ ] [Als naechstes] Sim-Governance-Bruecke fuer den Umbau als explizite Planarbeit fuehren. | nein |


Hinweise (Index)
----------------

- Aktive TODO-Quellen sind `todo.root.md` plus die vier Modul-Boards in `novapolis-dev/docs/`; gleichnamige Dateien unter `novapolis-dev/archive/**` oder `novapolis-dev/archive/quarantine/**` sind Historie, Snapshots oder Arbeitsquarantäne.
- Detaillierte Zwischenhistorie und Board-Uebergangsphasen bleiben in `novapolis-dev/docs/donelog.md`; dieser Index spiegelt nur den aktuellen Board- und Gate-Stand.
- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.
- Automationscheck: `scripts/check_todo_index_sync.py` liefert zusaetzlich Metadaten zu letzter Board-Aenderung, aeltestem offenen Punkt und Widerspruchen.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





