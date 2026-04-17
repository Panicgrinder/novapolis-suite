---
stand: 2026-04-17 05:25
update: Der TODO-Index spiegelt jetzt auch die Archivierung des letzten Sim-Abschlussschnitts; alle Live-Boards stehen weiter bei offen: 0.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260417_052246.md
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 0)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 0)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` ist nach vollstaendiger Erledigung und Validierung des letzten Root-Blocks wieder auf eine leere Arbeitsvorlage fuer neue suiteweite Punkte zurueckgesetzt. Der abgeschlossene Inhalt liegt jetzt unter `novapolis-dev/archive/todo.root.archive.md`; offene Folgearbeit liegt ausschliesslich in den Modul-Boards.

- Dev: Der zuletzt geschlossene Reader-/Surface-Nachzug liegt jetzt zusaetzlich unter `novapolis-dev/archive/todo.dev.archive.md`; `novapolis-dev/docs/todo.dev.md` ist wieder als schlanke Live-Oberflaeche fuer neue Dev-Punkte vorbereitet und steht weiter bei `offen: 0`.

- Agent: Der zuletzt geschlossene Handover-Block liegt jetzt zusaetzlich unter `novapolis-dev/archive/todo.agent.archive.md`; `novapolis-dev/docs/todo.agent-board.md` ist wieder als schlanke Live-Oberflaeche fuer neue Agent-Punkte vorbereitet und steht weiter bei `offen: 0`.

- RP: Der zuletzt geschlossene Folgepfad `slot 36-40` liegt jetzt zusaetzlich unter `novapolis-dev/archive/todo.rp.archive.md`; `novapolis-dev/docs/todo.rp.md` ist wieder als schlanke Live-Oberflaeche fuer neue RP-Punkte vorbereitet und steht weiter bei `offen: 0`.

- Sim: Der zuletzt geschlossene Sim-Abschlussschnitt liegt jetzt zusaetzlich unter `novapolis-dev/archive/todo.sim.archive.md`; `novapolis-dev/docs/todo.sim.md` ist wieder als schlanke Live-Oberflaeche fuer neue Sim-Punkte vorbereitet und steht weiter bei `offen: 0`.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-17 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-17 | keiner (offen: 0) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-04-17 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-17 | keiner (offen: 0) | nein |


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





