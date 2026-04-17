---
stand: 2026-04-17 02:07
update: Der TODO-Index spiegelt jetzt auch den umgesetzten RuntimeTelemetryController; direkt offen bleiben im Sim-Rest praktisch nur noch kleinere Cleanup-Altlasten.
checks: snapshot-lock PASS (2026-04-17 02:07); get_errors=PASS (Main.gd, runtime_telemetry_controller.gd); markdownlint=PASS; frontmatter=PASS; todo-index-sync=PASS
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 0)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 1)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` fuehrt den Folgepfad hinter `slot 30` jetzt ueber `Text-RPG Slice 2 Handover v1`. Root, Product Gate und Runbook nutzen damit denselben Namen und denselben Session-/Artefaktvertrag; die Root-seitige SSOT-Arbeit ist geschlossen.

- Dev: Der kurz geoeffnete Wochenrest fuer `ruff` und `black` ist im selben Lauf wieder geschlossen. `novapolis_agent/app/api/tts_models.py` nutzt fuer `TtsOutputFormat` jetzt `StrEnum`, die betroffenen TTS- und CPU-Limit-Tests sind lint-/formatkonform nachgezogen, und der von `black` gemeldete Restdateisatz in `scripts/` ist formatiert. `.tmp/results/reports/checks_report_20260414_124519.md` ist jetzt vollstaendig PASS; das Dev-Board steht damit wieder bei `offen: 0`.

- Agent: Sessionvertrag, Replay-/Savegame-Pfad, `gm_session`-Eval, Session-TTS, der warnungsfreie Produktpfad und die Coverage-Welle fuer `app/api/chat_helpers.py`, `app/main.py` und `app/tts/providers.py` sind jetzt geschlossen. Der breite Fokuslauf bestaetigt `100%/98%/96%` fuer die drei Zielmodule, und der kanonische Wrapper `scripts/run_pytest_coverage.py --fail-under 80` bleibt mit `615 passed` und `Total coverage: 94.92%` PASS. Das Agent-Board steht damit wieder bei `offen: 0`.

- RP: Start-Chooser, Reveal-Matrizen und Folgekorridore reichen jetzt bis `slot 35`. `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md` fuehrt den ersten fachlichen Ausbau des `Text-RPG Slice 2 Handover v1` auf demselben Resume-, Reveal- und Artefaktrahmen; das RP-Board steht damit wieder bei `offen: 0`.

- Sim: Der offene Sim-Block ist weiter geschrumpft. `novapolis-sim/scripts/runtime_telemetry_controller.gd` kapselt jetzt auch Eval-Summary-Refresh, Trendbildung, System-Metrik-Refresh, Python-Aufloesung sowie Health-/Reachability-Ableitung; direkt naechstliegend bleiben im Sim-Rest praktisch nur noch kleinere Cleanup-Altlasten statt eines weiteren grossen Architekturblocks.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-14 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-10 | keiner (offen: 0) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-04-14 | keiner (offen: 0) | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-17 | - [ ] [Jetzt] Sim-Hub nach dem Layout-Reset in modulare Controller und Runtime-Dienste zerlegen. | nein |


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





