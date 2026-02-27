---
stand: 2026-02-27 06:06
update: Letzten offenen Agent-Board-Punkt abgeschlossen (Task-Set Datensatz/Training), Index synchronisiert und Label-Drift in README/Runbook geschlossen.
checks: npx --yes markdownlint-cli2 --config F:/VS-Code-Workspace/Main/.markdownlint-cli2.jsonc "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.agent-board.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.index.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" "F:/VS-Code-Workspace/Main/novapolis_agent/README.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/runbook.md" PASS (2026-02-27 05:31); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe F:/VS-Code-Workspace/Main/scripts/check_frontmatter.py "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.agent-board.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.index.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" "F:/VS-Code-Workspace/Main/novapolis_agent/README.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/runbook.md" PASS (EXITCODE=0, 2026-02-27 05:31)
---

<!-- markdownlint-disable MD041 -->

Dev-DONELOG (Current Window)
============================

Hinweis
-------

- Aktives Fenster: nur Eintraege der letzten 7 Tage.
- Historik bleibt vollstaendig in den Archivdateien unter `novapolis-dev/archive/docs/donelogs/` erhalten.

Current-Window Eintraege
------------------------

Dev/Agent: Letzter Agent-Board-Punkt geschlossen (2026-02-27 05:14)
-------------------------------------------------------------------

- `novapolis-dev/docs/todo.agent-board.md`: letzter offener Punkt `VS Code Task-Set fuer Datensatzbau & Training vervollstaendigen` auf erledigt gesetzt.
- `.vscode/tasks.json`: neue Labels hinzugefuegt (`Data: curate from latest (train pack)`, `Data: export+pack (latest results)`, `Train: baseline LoRA (tiny-gpt2, 1-step)`).
- `novapolis_agent/README.md` und `novapolis_agent/docs/runbook.md`: identische Task-Labels aufgenommen, um Doku-Drift zu vermeiden.
- `novapolis-dev/docs/todo.index.md`: Agent-Open-Count synchronisiert (`offen: 1 -> 0`).
- Laufbelege: Curate-CLI `--help` PASS; Export auf historischem quality_de-Resultset ausgefuehrt (`0` Eintraege wegen Source-Path-Drift); Prepare-Pack PASS (`train=90`, `val=10`, `total=100`); Baseline-LoRA-Pipeline PASS (`train_loss=10.4748`, Output `outputs/lora-baseline-vscode`).

Dev/Agent: KI/TTS-Provenance und Nachweisstruktur nachgezogen (2026-02-27 04:57)
-------------------------------------------------------------------------------

- Vollaudit fuer Herkunft/Nachweise erstellt: neue zentrale Datei `novapolis_agent/docs/provenance-register.md` (intern vs. extern, Statusmatrix gruen/gelb/rot).
- Dataset-Herkunft in `novapolis-dev/docs/dataset-provenance.md` auf den kompletten aktiven Bestand erweitert (inkl. `quality_de_*` und `eval-smoke`).
- TTS-Compliance um Runtime-Voice-Nachweispflicht ergaenzt: `novapolis_agent/docs/tts-compliance-policy.md` verlinkt jetzt auf `novapolis_agent/docs/tts-voice-provenance-log.md`.
- Nachweisablage fuer externe Basismodelle vorbereitet: `novapolis_agent/docs/vendor_licenses/huggingface/README.md` (Pflichtkatalog + Zielpfade fuer lokale Lizenzkopien).

Dev/Agent: LoRA-Gates und Baseline-Metriken verbindlich gemacht (2026-02-27 04:45)
------------------------------------------------------------------------------

- `novapolis-dev/docs/todo.agent-board.md`: Punkt `Trainingspaket-Gates und Baseline-Metriken fuer LoRA-Lauf` auf erledigt gesetzt.
- Go/No-Go-Basiswerte dokumentiert (`records>=20`, `filterquote>=0.70`, `dupe_rate<=0.10`) und Pflichtschema fuer Laufprotokolle festgelegt.
- `novapolis_agent/scripts/fine_tune_pipeline.py` robust gemacht (lokale Zeitstempel-Erzeugung statt importfragiler `now_compact`-Imports), damit der Baseline-Entrypoint standalone laeuft.
- Reproduzierbarer Baseline-Run erfolgreich belegt: `fine_tune_pipeline.py` mit `sshleifer/tiny-gpt2`, `batch=1`, `epochs=1`, `max_steps=1`, `lr=0.0002`; Ergebnisartefakte unter `outputs/lora-baseline-20260227_02/`.
- `novapolis-dev/docs/todo.index.md` im selben Lauf synchronisiert (`Agent offen: 2 -> 1`).

Dev/Agent: Monats-Baseline fuer Datensatz-Driftkontrolle umgesetzt (2026-02-27 04:28)
-------------------------------------------------------------------------------

- Neues Skript `novapolis_agent/scripts/eval_drift_report.py` eingefuehrt: KPI-Extraktion (`pass_rate`, `top_failed_checks`, `top_missing_terms`) aus `results_*.jsonl`, Baseline-Vergleich und `ok/warning/blocker`-Status anhand Schwellen.
- Monats-Baseline abgelegt unter `novapolis_agent/eval/results/baselines/training_profiles.2026-02.json`.
- Vergleichsreport reproduzierbar erstellt unter `novapolis_agent/eval/results/drift/training_profiles_drift_2026-02-27.json`.
- Board-Punkt `Datensatz-Driftkontrolle mit Monats-Baseline` auf erledigt gesetzt und Schwellwerte/Rueckkopplung verbindlich im Board dokumentiert.
- `novapolis-dev/docs/todo.index.md` im selben Lauf synchronisiert (`Agent offen: 3 -> 2`).

Dev/Agent: Trainingsprofil-Datensaetze auf je 20 Eintraege erweitert (2026-02-27 02:13)
-----------------------------------------------------------------------------------------

- `novapolis_agent/eval/datasets/training/chronistin_neutral_assistiv.v1.jsonl` von 3 auf 20 Eintraege erweitert.
- `novapolis_agent/eval/datasets/training/chronistin_lore_intensiv.v1.jsonl` von 3 auf 20 Eintraege erweitert.
- `novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl` von 3 auf 20 Eintraege erweitert.
- Schema unveraendert beibehalten (`id`, `slug`, `category`, `profile`, `tags`, `messages`, `source_package`) und ID-Reihen bis `...-020` fortgefuehrt.
- Strict-Validator erfolgreich: `python novapolis_agent/scripts/validate_eval_datasets.py --strict --pattern "novapolis_agent/eval/datasets/training/*.jsonl"` -> `files=3, records=60, ids=60, slugs=60`.

Dev/Agent: Datensatz-Erzeugungspfad verbindlich standardisiert (2026-02-27 02:04)
-------------------------------------------------------------------------------

- In `novapolis-dev/docs/todo.agent-board.md` wurde der naechste offene Punkt abgeschlossen: reproduzierbarer Ablauf `generate_eval_dataset.py -> run_eval.py -> export_finetune.py -> prepare_finetune_pack.py`.
- Optionaler Kurationszweig `curate_dataset_from_latest.py` als integrierter Pfad dokumentiert.
- Mindestfilter verbindlich festgelegt (`include_failures=false`, `min_output_chars>=20`, `dedupe_by_instruction=true`; optionale Schaerfung via `near_dup_threshold>=0.80`).
- E2E-Artefaktkette im Board belegt (Results + Finetune + Train/Val-Dateien unter `novapolis_agent/eval/results/` und `novapolis_agent/eval/results/finetune/`).
- `novapolis-dev/docs/todo.index.md` im selben Lauf synchronisiert (`Agent offen: 4 -> 3`).

Dev/Agent: Kanonische Trainingsprofil-Pakete umgesetzt (2026-02-27 01:50)
-------------------------------------------------------------------------

- Drei Profilpakete fuer die Chronistin angelegt: `chronistin_neutral_assistiv.v1.jsonl`, `chronistin_lore_intensiv.v1.jsonl`, `chronistin_operativ_kurz.v1.jsonl` unter `novapolis_agent/eval/datasets/training/`.
- Strikter Validator-Lauf erfolgreich: `python novapolis_agent/scripts/validate_eval_datasets.py --strict --pattern "novapolis_agent/eval/datasets/training/*.jsonl"` -> `files=3, records=9, ids=9, slugs=9`.
- `novapolis-dev/docs/dataset-provenance.md` um Namensschema/Pflichtmetadaten und Herkunft/Policy der drei Profilpakete erweitert.
- `novapolis-dev/docs/todo.agent-board.md` Punkt abgeschlossen; `novapolis-dev/docs/todo.index.md` synchronisiert (`Agent offen: 5 -> 4`).

Dev/Agent: Eval-Marathon als Qualitaetsanker operationalisiert (2026-02-27 01:11)
-------------------------------------------------------------------------------

- In `novapolis-dev/docs/todo.agent-board.md` wurde der naechste offene Punkt abgeschlossen: verbindliches Betriebsprofil mit KPI-Mindestset, Blocker/Warnung-Triage und reproduzierbarem Receipt-Standard.
- Rueckkopplungsregel verankert: `Blocker -> Jetzt`, `Warnung -> Als naechstes`, `Beobachtung -> Spaeter`.
- `novapolis-dev/docs/todo.index.md` im selben Lauf synchronisiert (`Agent offen: 6 -> 5`).
- Evidenzpfade: `.vscode/tasks.json` (`Eval: suite marathon (~60m, asgi, loud)`), `novapolis_agent/eval/results/`, `novapolis_agent/docs/DONELOG.txt`.

Dev: Archivfenster kanonisiert ohne Datenverlust (2026-02-27 00:18)
--------------------------------------------------------------------

- Kanonisches Archivfenster bleibt `novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md` und `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md`.
- Die vorherigen Dubletten (`pre-2026-02-19`) wurden verlustfrei verschoben nach `novapolis-dev/archive/quarantine/archive-window-dedupe-20260227_0018/`.
- Ziel: ein eindeutiges aktives Archivfenster bei gleichzeitig vollstaendig erhaltener Historie.

Dev: Wochenarchivierung fuer Status/Donelog eingefuehrt (2026-02-27 00:04)
--------------------------------------------------------------------------

- Historische Inhalte aus den aktiven Dateien wurden wochenweise in die vorgesehenen Dev-Archive ueberfuehrt:
  - `novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md`
  - `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md`
- `WORKSPACE_STATUS.md` wurde auf ein aktuelles, scanbares Wochenfenster reduziert.
- `novapolis-dev/docs/donelog.md` wurde auf ein operatives Current-Window reduziert; Historik bleibt in Archivdateien verlinkt.

Dev/Root: Doku-Drift-Audit und Obsoleszenz-Fix (2026-02-26 21:59)
-----------------------------------------------------------------

- Nachweisbare Driftstellen behoben:
  - `WORKSPACE_INDEX.md`: obsolete Eval-Dataset-Verweise entfernt und auf aktuellen `neutral/`, `rpg/`, `quality_de_*`-Bestand umgestellt.
  - `novapolis-dev/docs/tests.md`: obsolete `cvn-agent`-Referenz entfernt; Task-/Testbezug auf Single-Root-Iststand korrigiert.

Dev/Agent: Snapshot-Resync vor Commit (2026-02-26 05:17)
---------------------------------------------------------

- Commit-Hook (`snapshot_gate`) blockierte aufgrund veralteter `stand`-Werte in gestagten Markdown-Dateien.
- Frischer Lock gesetzt und `stand` in den betroffenen Dateien auf den Lock-Zeitwert synchronisiert.

Archivverweise
--------------

- Dev-Historikfenster (neu): `novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md`
- Vorheriges Dublettenfenster (verlustfrei verschoben): `novapolis-dev/archive/quarantine/archive-window-dedupe-20260227_0018/donelog_dev.window-archive.pre-2026-02-19.md`
- Konsolidierter historischer Ziellog: `novapolis-dev/archive/docs/donelogs/donelog_dev.md`
