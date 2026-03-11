---
stand: 2026-03-11 04:45
update: Sim-Index fuer Hub-Chatfenster-Aufnahme und Abschlussstatus synchronisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-sim/README.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-10 17:19); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-sim/README.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-10 17:19)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 5)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 1)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 0)

Statushinweise (aktuell)
------------------------

- Sim v5.0: Sim-Board konsolidiert, verbleibende Mikrodrift geschlossen (`offen: 1 -> 0`).
- Index v2.0: Operative Anzeige erweitert um Board-Metadaten (letzte Aenderung, aeltester offener Punkt, Widerspruchscheck).

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-03-05 | Woechentliche Hygiene-Cadence etablieren | nein |
| RP (`docs/todo.rp.md`) | 2026-03-05 | Canvas-Rettung - Sprint 1 (offene Checklisten) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-03-11 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-03-11 | keiner (offen: 0) | nein |

Hinweise (Index)
----------------

- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.
- Automationscheck: `scripts/check_todo_index_sync.py` liefert zusaetzlich Metadaten zu letzter Board-Aenderung, aeltestem offenen Punkt und Widerspruchen.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





