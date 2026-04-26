---
stand: 2026-04-26 20:40
update: Der TODO-Index steht weiter bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`; der Wochenabschluss ist mit Vollcheck, Sim-Asset-Check und Coverage-Ziellauf gruen belegt.
checks: scripts/run_checks_and_report.py overall=PASS; tests_coverage=PASS (92.19%, 696 passed); sim_epoch_assets=PASS (summary=fail:0,warn:0); report=.tmp\results\reports\checks_report_20260426_203550.md
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

- Dev: `novapolis-dev/docs/todo.dev.md` fuehrt aktuell wieder keine offenen Steuerpunkte mehr. Der kleine Audit-Rest ist geschlossen: `todo.root.md` fuehrt wieder den aktuellen Modulstand, `novapolis-dev/docs/todo.sim.md` ist portabel formuliert, und `ruff` plus `black` sind fuer `novapolis_agent` und `scripts` wieder gruen.

- Agent: `novapolis-dev/docs/todo.agent-board.md` fuehrt aktuell keine offenen Punkte mehr. Der gemeinsame Release-Gate-Pfad `novapolis_agent/scripts/training_release_gate.py` blockiert `export+pack` und LoRA jetzt vor dem naechsten Schritt, wenn `validate_eval_datasets --strict`, ein grüner `rp_content`-Beleg oder die notwendige Provenienz fehlen; im aktuellen Repo-Stand scheitert derselbe Direktlauf erwartungsgemaess an `missing rp_content results` statt ungeguardet in Training zu laufen.

- RP: `novapolis-dev/docs/todo.rp.md` fuehrt nach der Metro-Verdichtung aktuell keine offenen Punkte mehr. `Warenueberblick-T0.md`, das Arbeitsledger und die Matrix aggregieren jetzt evidence-first nur noch die belegten D5/C6-Aufbaupfade, den Haendlerbund-Korridor `G7 <-> C6` und die T0-Bandbreiten der uebrigen externen Fraktionen; neutrale Stationslager und Weltsummen bleiben explizit offen.

- Sim: `novapolis-dev/docs/todo.sim.md` fuehrt aktuell keine offenen Punkte mehr. `scripts/run_sim_headless_verify.py` loest im aktuellen Windows-Kontext jetzt auch den Pfad eines laufenden lokalen Godot-Prozesses auf; `Checks: sim headless verify` endet damit wieder mit `SIM_VERIFY: OK` statt am frueheren Exit `2`.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-26 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-20 | keiner (offen: 0) | nein |
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





