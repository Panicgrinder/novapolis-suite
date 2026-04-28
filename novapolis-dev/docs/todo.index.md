---
stand: 2026-04-28 13:05
update: Der TODO-Index fuehrt nach dem Vollbaum-Nachzug wieder keine offenen Modul-Boards; Dev, RP, Agent und Sim stehen bei offen: 0.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260428_052348.md; snapshot-lock PASS (2026-04-28 13:05)
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

- Root/Meta: `todo.root.md` ist nach der Archivierung des abgeschlossenen April-Blocks wieder als schlanke Live-Oberflaeche vorbereitet und fuehrt aktuell keine offenen suiteweiten Querschnittspunkte. Der Wochenabschluss vom 2026-04-26 20:40 ist gruen belegt (`Checks: full` PASS, `Checks: sim epoch assets` PASS, Coverage `92.19%`), und der naechste Hygiene-Takt bleibt ueber `novapolis-dev/docs/process/abschluss-routine.ssot.md` sowie die aktuellen Root-Protokolle verankert, waehrend Root bewusst ausserhalb der Modul-Open-Counts bleibt.

- Dev: `novapolis-dev/docs/todo.dev.md` fuehrt aktuell wieder keine offenen Punkte mehr. Alle drei Workspace-Trees liegen wieder im Default-Freshness-Gate; `workspace_tree_full.txt` wird dabei deterministisch aus repo-sichtbaren Pfaden erzeugt und nicht mehr von ignore-basierten Laufartefakten gekippt.

- Agent: `novapolis-dev/docs/todo.agent-board.md` fuehrt aktuell keine offenen Punkte mehr. Der gemeinsame Release-Gate-Pfad `novapolis_agent/scripts/training_release_gate.py` blockiert `export+pack` und LoRA jetzt vor dem naechsten Schritt, wenn `validate_eval_datasets --strict`, ein grüner `rp_content`-Beleg oder die notwendige Provenienz fehlen; im aktuellen Repo-Stand scheitert derselbe Direktlauf erwartungsgemaess an `missing rp_content results` statt ungeguardet in Training zu laufen.

- RP: `novapolis-dev/docs/todo.rp.md` fuehrt aktuell wieder keine offenen Punkte mehr. Die D5-Inventarspur trennt den kleinen Nordlinie-Turn-7/8-Satz jetzt nicht nur als Mengenstand, sondern zusaetzlich als ausdruecklichen Delta-Block fuer Lieferung, Einsatz und offene Evidenzgrenze.

- Sim: `novapolis-dev/docs/todo.sim.md` fuehrt aktuell keine offenen Punkte mehr. `scripts/run_sim_headless_verify.py` loest im aktuellen Windows-Kontext jetzt auch den Pfad eines laufenden lokalen Godot-Prozesses auf; `Checks: sim headless verify` endet damit wieder mit `SIM_VERIFY: OK` statt am frueheren Exit `2`.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-28 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-27 | keiner (offen: 0) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-04-23 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-26 | keiner (offen: 0) | nein |


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





