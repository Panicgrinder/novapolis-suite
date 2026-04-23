---
stand: 2026-04-23 16:00
update: Der TODO-Index fuehrt jetzt zusaetzlich den neuen RP-Chattranskriptpfad als Rohsignal innerhalb des offenen Agent-Punkts.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260423_155606.md; snapshot-lock PASS (2026-04-23 16:00)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 0)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 1)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 5)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` ist nach der Archivierung des abgeschlossenen April-Blocks wieder als schlanke Live-Oberflaeche vorbereitet und fuehrt aktuell keine offenen suiteweiten Querschnittspunkte. Der zuletzt abgeschlossene Root-Block liegt unter `novapolis-dev/archive/todo.root.archive.md`; der naechste Hygiene-Takt fuer KPI-/Boardpflege bleibt ueber `novapolis-dev/docs/process/abschluss-routine.ssot.md` und die aktuellen Root-Protokolle verankert, waehrend Root bewusst ausserhalb der Modul-Open-Counts bleibt.

- Dev: `novapolis-dev/docs/todo.dev.md` fuehrt nach dem konservativeren CPU-Schonpfad und dem gezielten Stilnachzug aktuell wieder keine offenen Steuerpunkte mehr. Der Auto-Modus von `scripts/run_with_cpu_limit.py` nutzt lokal jetzt standardmaessig nur noch `2` logische CPUs; der frische Full-Check bleibt im expliziten 1-CPU-Schonmodus vollstaendig PASS, und der separate Coverage-Lauf liegt weiter bei `96.16%`.

- Agent: `novapolis-dev/docs/todo.agent-board.md` fuehrt weiter genau einen offenen Ausbaupunkt. Neben dem RP-Train-Builder fuer `lore` und `ops` liegt jetzt auch ein getrennter Session-/Replay-Promotionsbuilder samt Root-Wrapper, Task und Script-Tests vor; der erste belegte Lauf hat 10 reviewpflichtige Records unter `novapolis_agent/eval/datasets/curation/session_promotions.v1.jsonl` erzeugt. Neu hinzu kommt jetzt ein append-only RP-Chattranskriptpfad unter `novapolis-rp/database-curated/staging/rp-runtime/sessions/<session-id>/transcript.jsonl`, der lueckenlose Rohspur und spaetere Review ermoeglicht, aber bewusst ausserhalb des Builder-Inputs bleibt. Offen bleibt damit nur noch der spaetere harte Gate-Block gegen rote Provenienz- oder `rp_content`-Signale vor LoRA.

- RP: `novapolis-dev/docs/todo.rp.md` fuehrt nach der Metro-Verdichtung aktuell keine offenen Punkte mehr. `Warenueberblick-T0.md`, das Arbeitsledger und die Matrix aggregieren jetzt evidence-first nur noch die belegten D5/C6-Aufbaupfade, den Haendlerbund-Korridor `G7 <-> C6` und die T0-Bandbreiten der uebrigen externen Fraktionen; neutrale Stationslager und Weltsummen bleiben explizit offen.

- Sim: `novapolis-dev/docs/todo.sim.md` fuehrt weiter fuenf offene Punkte. Der aelteste Architekturpunkt ist code-seitig bis `agent_form_session_controller.gd` gezogen, bleibt aber formal offen, bis `Checks: sim headless verify` gegen eine lokal aufloesbare Godot-Binary wieder belegbar gruen laeuft; der zuletzt geschlossene Sim-Abschlussschnitt bleibt zusaetzlich unter `novapolis-dev/archive/todo.sim.archive.md` archiviert.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-20 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-20 | keiner (offen: 0) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-04-21 | - [ ] [Als naechstes] RP-SSOT, Spielstand und Trainingspipeline sauber trennen und koppeln. | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-20 | - [ ] [Jetzt] Den verbliebenen Agent-Studio-/Form-State-Rest aus `Main.gd` in denselben Controller-Schnitt ziehen wie die uebrigen Hub-Pfade. | nein |


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





