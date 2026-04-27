---
stand: 2026-04-28 01:22
update: Der TODO-Index fuehrt den neuen workspaceweiten Freshness-Scope jetzt als geschlossenen Dev-Steuerpunkt bei unveraendertem Modulstand `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`.
checks: snapshot-lock PASS (2026-04-28 01:22); doc-freshness PASS (scope_rows=46, checked_docs=262, findings=0, 2026-04-28 01:17)
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

- Dev: `novapolis-dev/docs/todo.dev.md` fuehrt aktuell wieder keine offenen Steuerpunkte mehr. Der dokumentierte Freshness-Scope ist jetzt workspaceweit statt nur dev-lokal: `scripts/check_doc_freshness.py` liest `novapolis-dev/docs/meta/doc-freshness-scope.md`, expandiert Root-, Governance-, Agent-, RP-, Sim- und Tree-Pfade zu `checked_docs=262`, und `novapolis-dev/docs/active-surface-index.md` bleibt wieder reine Dev-Klassifikation statt versteckter Scope-Ersatzquelle.

- Agent: `novapolis-dev/docs/todo.agent-board.md` fuehrt aktuell keine offenen Punkte mehr. Der gemeinsame Release-Gate-Pfad `novapolis_agent/scripts/training_release_gate.py` blockiert `export+pack` und LoRA jetzt vor dem naechsten Schritt, wenn `validate_eval_datasets --strict`, ein grüner `rp_content`-Beleg oder die notwendige Provenienz fehlen; im aktuellen Repo-Stand scheitert derselbe Direktlauf erwartungsgemaess an `missing rp_content results` statt ungeguardet in Training zu laufen.

- RP: `novapolis-dev/docs/todo.rp.md` fuehrt aktuell keine offenen Punkte mehr. Der Nordlinie-Laborpfad ist fuer den kleinen Runtime-Turn-7-Satz jetzt zwischen Waren-Index, Stuetzbaukasten, D5-/C6-Inventaren und Runtime-Artefakten konsistent geschlossen; darueber hinaus offene C6-Lagerdetails bleiben bewusst als Evidenzluecke in den Fachdokumenten stehen statt als Board-Blocker.

- Sim: `novapolis-dev/docs/todo.sim.md` fuehrt aktuell keine offenen Punkte mehr. `scripts/run_sim_headless_verify.py` loest im aktuellen Windows-Kontext jetzt auch den Pfad eines laufenden lokalen Godot-Prozesses auf; `Checks: sim headless verify` endet damit wieder mit `SIM_VERIFY: OK` statt am frueheren Exit `2`.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-26 | keiner (offen: 0) | nein |
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





