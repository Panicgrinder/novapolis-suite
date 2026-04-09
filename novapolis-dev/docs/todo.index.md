---
stand: 2026-04-09 14:10
update: Der TODO-Index fuehrt im Agent-Modul jetzt einen offenen Coverage-Haertungslauf fuer fuenf Low-Coverage-Dateien.
checks: scripts\run_pytest_coverage.py --fail-under 80 PASS; report=.tmp\results\reports\pytest_coverage_postflight_20260409_123310.md; coverage=88.98%
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 0)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 1)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 0)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` fuehrt den nachgezogenen Wochenabschluss vom 2026-04-08 als aktuellen Referenzlauf; Full-Check, separater Coverage-Lauf, Sim-Clean-Checkout und Hygiene-Cadence sind gruen, der Root-Metablock `Slice -> MVP -> Beta` bleibt gegen den belegten Modul-Iststand geschlossen.

- Dev: Der kanonische Typenpfad ist belastbar, und der produktive Text-RPG-Gate-Pfad trennt den GM-Rest jetzt sauber. Die Live-Ursachenanalyse hat den unbeabsichtigten Kontextnotiz-Turn im GM-Payload geschlossen: `novapolis_agent/app/api/chat.py` injiziert bei `CONTEXT_NOTES_ENABLED=False` keine `[Kontext-Notizen]` mehr, der neue Regressionstest ist gruen, und die Live-Payload-Pruefung fuer `gm.session.continuity.v1` zeigt nur noch den Zweier-Prompt aus `system` und `user`. Das Dev-Board steht damit wieder auf `offen: 0`.

- Agent: Sessionvertrag, Replay-/Savegame-Pfad, `gm_session`-Eval, Session-TTS und der warnungsfreie Produktpfad bleiben geschlossen. Neu offen ist ein gezielter Coverage-Haertungslauf fuer `run_text_rpg_reference_session.py`, `validate_eval_datasets.py`, `summarize_gm_eval_kpis.py`, `content_management.py` und `tts_models.py`; Basis ist der frische Wrapper-Lauf `.tmp/results/reports/pytest_coverage_postflight_20260409_123310.md` mit `88.98%` Gesamtquote. Das Agent-Board steht damit bei `offen: 1`.

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





