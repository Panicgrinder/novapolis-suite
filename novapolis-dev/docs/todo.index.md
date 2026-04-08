---
stand: 2026-04-08 13:40
update: Der TODO-Index fuehrt den nachgezogenen Wochenabschluss als aktuellen gruenen Board- und Gate-Stand; Zwischenhistorie bleibt im Dev-DONELOG.
checks: Wochenabschluss via scripts/run_checks_and_report.py overall=PASS; report=.tmp\results\reports\checks_report_20260408_131224.md; scripts\check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency summary=fail:0,warn:0; scripts\run_pytest_coverage.py --fail-under 80 PASS report=.tmp\results\reports\pytest_coverage_postflight_20260408_131356.md coverage=90.14%; npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py WORKSPACE_STATUS.md DONELOG.md todo.root.md novapolis-dev/docs/donelog.md novapolis-dev/docs/todo.index.md novapolis-dev/docs/meta/dev-kpi-trends.md PASS; .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . --write-index-meta PASS; .\.venv\Scripts\python.exe scripts\check_doc_freshness.py --repo-root . PASS; .\.venv\Scripts\python.exe scripts\check_logs_policy.py --repo-root . PASS
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

- Root/Meta: `todo.root.md` fuehrt den nachgezogenen Wochenabschluss vom 2026-04-08 als aktuellen Referenzlauf; Full-Check, separater Coverage-Lauf, Sim-Clean-Checkout und Hygiene-Cadence sind gruen, der Root-Metablock `Slice -> MVP -> Beta` bleibt gegen den belegten Modul-Iststand geschlossen.

- Dev: Der kanonische Typenpfad ist belastbar, der produktive Text-RPG-Gate-Pfad ist als SSOT dokumentiert, und der nachgezogene Wochenabschluss vom 2026-04-08 liefert wieder Full-Check PASS bei Hygiene-KPIs `0/0/0/0`. Das Dev-Board steht damit auf `offen: 0`.

- Agent: Sessionvertrag, Replay-/Savegame-Pfad, `gm_session`-Eval, Session-TTS und der warnungsfreie Produktpfad sind auf demselben Text-RPG-Slice geschlossen. Das Agent-Board steht auf `offen: 0`.

- RP: Start-Chooser, Reveal-Matrizen und Folgekorridore reichen jetzt bis `slot 30`; OGG-Kandidaten und der Live-Dialogpfad sind gegen den aktiven Produktstand nachgezogen. Das RP-Board steht auf `offen: 0`.

- Sim: Live-Spielclient, Session-/Replay-Bridge und das Clean-Checkout-Profil fuer Epoch-/Audio-Assets sind geschlossen. Das Sim-Board steht auf `offen: 0`.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-07 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-07 | keiner (offen: 0) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-04-07 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-07 | keiner (offen: 0) | nein |


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





