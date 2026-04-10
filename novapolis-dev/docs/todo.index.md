---
stand: 2026-04-10 13:22
update: Der TODO-Index fuehrt den Coverage-Warning-Fix jetzt als abgeschlossen; Dev ist damit wieder geschlossen.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=FAIL; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260410_131501.md
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 0)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 0)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 1)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 1)
- Root-Backlog: `todo.root.md` — suiteweiter Querschnitts-Backlog und Meta-Aufgaben (nicht Teil der Modul-Open-Counts oben)

Statushinweise (aktuell)
------------------------

- Root/Meta: `todo.root.md` fuehrt den Folgepfad hinter `slot 30` jetzt ueber `Text-RPG Slice 2 Handover v1`. Root, Product Gate und Runbook nutzen damit denselben Namen und denselben Session-/Artefaktvertrag; die Root-seitige SSOT-Arbeit ist geschlossen.

- Dev: Der kanonische Typenpfad und der CPU-Schonmodus bleiben belastbar, und der Coverage-Hygiene-Rest ist jetzt geschlossen. Die vier `runpy`-Warnings aus `.tmp/results/reports/pytest_coverage_postflight_20260409_232603.md` kamen aus Edge-Tests, die `runpy.run_module()` auf bereits vorimportierten `scripts.*`-Modulen ausfuehrten; nach der Umstellung auf echte Skriptpfade via `runpy.run_path(..., run_name="__main__")` ist `.tmp/results/reports/pytest_coverage_postflight_20260410_051125.md` mit `596 passed`, `Total coverage: 93.66%` und ohne Warnings derselben Klasse PASS. Das Dev-Board steht damit wieder bei `offen: 0`.

- Agent: Sessionvertrag, Replay-/Savegame-Pfad, `gm_session`-Eval, Session-TTS, der warnungsfreie Produktpfad und der letzte Coverage-Rest bleiben geschlossen. Neu offen ist die naechste Coverage-Welle fuer `app/api/chat_helpers.py` (`89%`), `app/main.py` (`90%`) und `app/tts/providers.py` (`87%`) aus `.tmp/results/reports/pytest_coverage_postflight_20260409_232603.md`; das Agent-Board steht damit bei `offen: 1`.

- RP: Start-Chooser, Reveal-Matrizen und Folgekorridore reichen jetzt bis `slot 35`. `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md` fuehrt den ersten fachlichen Ausbau des `Text-RPG Slice 2 Handover v1` auf demselben Resume-, Reveal- und Artefaktrahmen; das RP-Board steht damit wieder bei `offen: 0`.

- Sim: Live-Spielclient, Audio-Wiedergabe und das Clean-Checkout-Profil fuer Epoch-/Audio-Assets bleiben geschlossen, aber der Hub nutzt den Replay-/Resume-Vertrag fuer `Text-RPG Slice 2 Handover v1` noch nicht als eigenen Bedienpfad. `novapolis-sim/scripts/Main.gd` zeigt `resume_checkpoint_id` derzeit nur als Label und synchronisiert sonst nur den aktuellen Session-Snapshot; das Sim-Board steht damit bei `offen: 1`.

- Historische Zwischenstaende und offene Uebergangsphasen bleiben im Dev-DONELOG dokumentiert; der TODO-Index fuehrt absichtlich nur noch den aktuellen Board- und Gate-Stand.

Board-Metadaten (automationsrelevant)
-------------------------------------

| Board | letzte Aenderung | aeltester offener Punkt | Widerspruch "keine offenen" |
| --- | --- | --- | --- |
| Dev (`docs/todo.dev.md`) | 2026-04-09 | keiner (offen: 0) | nein |
| RP (`docs/todo.rp.md`) | 2026-04-07 | keiner (offen: 0) | nein |
| Agent (`docs/todo.agent-board.md`) | 2026-04-09 | - [ ] [Als naechstes] Naechste Coverage-Welle fuer den aktiven Produktpfad auf `chat_helpers`, `main` und `tts/providers` ziehen. | nein |
| Sim (`docs/todo.sim.md`) | 2026-04-07 | - [ ] [Als naechstes] Replay-/Resume-Steuerung fuer `Text-RPG Slice 2 Handover v1` im Hub auf den bestehenden Session-Vertrag heben. | nein |


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





