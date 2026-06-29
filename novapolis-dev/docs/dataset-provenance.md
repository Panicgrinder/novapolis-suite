---
stand: 2026-06-29 16:07
update: Die Provenance-SSOT fuehrt jetzt zusaetzlich den gemeinsamen Release-Gate-Pfad vor Export und LoRA mit rp_content- und Freigabeschwellen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260629_155310.md; snapshot-lock PASS (2026-06-29 16:07)
---

Dataset Provenance (SSOT)
========================

Zweck
-----

- Diese Datei ist die zentrale SSOT fuer Herkunft, Lizenzstatus und Nutzungsfreigabe von Eval-Datasets.
- Geltungsbereich: Agent-Eval-Daten unter `novapolis_agent/eval/datasets/**`.

Statusmatrix
------------

| Datensatz | Pfad | Herkunft | Lizenzstatus | Freigabe | Nachweis |
| --- | --- | --- | --- | --- | --- |
| Neutral Generated 101-300 | `novapolis_agent/eval/datasets/neutral/generated/neutral_101_300_generated.v1.jsonl` | script-generiert (intern) | intern | gruen | `novapolis_agent/docs/DONELOG.txt:112` |
| Neutral Core 01-20 | `novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |
| Neutral Tech 81-100 | `novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |
| Neutral Smoke | `novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |
| Neutral Eval Smoke | `novapolis_agent/eval/datasets/eval-smoke.jsonl` | intern erstellt (Smoke-Paket) | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| Quality-DE Core | `novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl` | intern erstellt (quality_de Paketband) | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| Quality-DE Drift | `novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl` | intern erstellt (quality_de Paketband) | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| Quality-DE Canary | `novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl` | intern erstellt (quality_de Paketband) | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| RPG Fantasy 21-40 | `novapolis_agent/eval/datasets/rpg/rpg_21_40_fantasy.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |
| RPG Dialog 41-60 | `novapolis_agent/eval/datasets/rpg/rpg_41_60_dialog.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |
| RPG Szenen 61-80 | `novapolis_agent/eval/datasets/rpg/rpg_61_80_szenen.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |
| RP SSOT Core | `novapolis_agent/eval/datasets/rp/rp_ssot_core.v1.jsonl` | intern script-generiert aus RP-SSOT | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| RP Characters Core | `novapolis_agent/eval/datasets/rp/rp_characters_core.v1.jsonl` | intern script-generiert aus RP-SSOT | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| RP Locations Core | `novapolis_agent/eval/datasets/rp/rp_locations_core.v1.jsonl` | intern script-generiert aus RP-SSOT | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| RP Admin Core | `novapolis_agent/eval/datasets/rp/rp_admin_core.v1.jsonl` | intern script-generiert aus RP-SSOT | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| RP Lore Train | `novapolis_agent/eval/datasets/training/rp_lore_train.v1.jsonl` | intern script-generiert aus RP-SSOT | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| RP Ops Train | `novapolis_agent/eval/datasets/training/rp_ops_train.v1.jsonl` | intern script-generiert aus RP-SSOT | intern | gruen | `novapolis_agent/docs/DONELOG.txt` |
| Session Promotion Pack | `novapolis_agent/eval/datasets/curation/session_promotions.v1.jsonl` | intern script-generiert aus Session-/Replay-Artefakten | intern | gelb | `novapolis_agent/docs/DONELOG.txt` |
| Training Profil: neutral-assistiv | `novapolis_agent/eval/datasets/training/chronistin_neutral_assistiv.v1.jsonl` | intern erstellt (Profilpaket) | intern | gruen | `novapolis-dev/docs/donelog.md` |
| Training Profil: lore-intensiv | `novapolis_agent/eval/datasets/training/chronistin_lore_intensiv.v1.jsonl` | intern erstellt (Profilpaket) | intern | gruen | `novapolis-dev/docs/donelog.md` |
| Training Profil: operativ-kurz | `novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl` | intern erstellt (Profilpaket) | intern | gruen | `novapolis-dev/docs/donelog.md` |

Trainingsprofil-Konvention (verbindlich)
----------------------------------------

- Zielpfad: `novapolis_agent/eval/datasets/training/`.
- Dateinamen: `chronistin_<profil>.v<major>.jsonl` (Beispiele: `chronistin_neutral_assistiv.v1.jsonl`, `chronistin_lore_intensiv.v1.jsonl`, `chronistin_operativ_kurz.v1.jsonl`).
- Pflichtmetadaten pro Record:
  - `id` (eindeutig),
  - `slug` (eindeutig),
  - `tags` (list[str]),
  - Profilkennzeichnung ueber Feld `profile` und redundante Profilmarke in `tags`.
- Strukturminimum pro Record: mindestens `messages` oder `prompt` oder `conversation` (Validator-Vertrag).

RP-Train-Builder-Konvention (verbindlich)
-----------------------------------------

- Zielpfade: `novapolis_agent/eval/datasets/training/rp_lore_train.v1.jsonl` und `novapolis_agent/eval/datasets/training/rp_ops_train.v1.jsonl`.
- Herkunft: nur intern script-generiert aus `novapolis-rp/database-rp/**` ueber `novapolis_agent/scripts/build_training_from_rp.py`.
- Pflichtfelder pro Record:
  - `id` und `slug` (stabil und eindeutig),
  - `messages` als Seed-Prompt,
  - `source_file`,
  - `source_kind`,
  - `promotion_level`,
  - `license_scope`,
  - `source_package`,
  - `tags` inklusive Profilmarke `profile-rp-lore` oder `profile-rp-ops`.
- Zulassungsgrenze: direkte Session-, Replay-, Savegame- oder Raw-Exports aus `novapolis_agent/tmp/sim_sessions/**`, `novapolis-rp/database-raw/**` oder ungeprueften Laufzeitlogs duerfen nicht in diese Pakete einfliessen.
- Promotionsregel: Laufzeitartefakte werden erst nach dokumentierter Promotion in RP-SSOT oder ein freigegebenes Curation-Pack in trainierbare Pakete uebernommen.

Session-Promotion-Pack-Konvention (verbindlich)
-----------------------------------------------

- Zielpfad: `novapolis_agent/eval/datasets/curation/session_promotions.v1.jsonl`.
- Herkunft: intern script-generiert aus `novapolis_agent/tmp/sim_sessions/**` ueber `novapolis_agent/scripts/build_session_promotion_pack.py`.
- Primärquellen: nur das kanonische Artefakt-Quartett `savegame.json`, `replay_manifest.json`, `pc_log.jsonl` und `world_log.jsonl`; andere Nebenartefakte werden nicht in die Promotionsoberflaeche gezogen.
- Pflichtfelder pro Record:
  - `id` und `slug` (stabil und eindeutig),
  - `messages` als reviewpflichtiger Promotionsprompt,
  - `source_file=replay_manifest.json` als Primaeranker,
  - `source_kind=session_replay`,
  - `promotion_level=runtime_session_review_required`,
  - `license_scope=internal`,
  - `source_package=session_promotion_builder.v1`,
  - `meta.artifact_paths`, `meta.resume_checkpoint_id`, `meta.session_status` und Ereigniszaehler als Provenienzrahmen.
- Freigabegrenze: Das Curation-Pack ist bewusst `gelb`, nicht direkt trainierbar und muss vor jedem RP- oder Trainingsimport noch in RP-SSOT oder eine explizit freigegebene Trainingsableitung uebernommen werden.

Freigaberegel
-------------

- `gruen`: Nutzung fuer Eval/Training im Repo freigegeben.
- `gelb`: Nutzung nur intern fuer Eval, bis Quellen- oder Lizenznachweis explizit dokumentiert ist.
- `rot`: Keine Nutzung bis zur Klaerung.

Release-Gate-Konvention
-----------------------

- `novapolis_agent/scripts/training_release_gate.py` ist der kanonische Repo-Guard vor `curate_dataset_from_latest.py` und `fine_tune_pipeline.py`.
- Export-/Pack-Pfade verlangen denselben Mindestpfad: `validate_eval_datasets --strict`, den neuesten grünen `rp_content`-Resultatbeleg und eine Provenienzpruefung der beteiligten Datasets.
- Fuer Export-/Review-Pfade reicht Provenienzstatus mindestens `gelb`, solange der Pfad bewusst reviewpflichtig bleibt; direkte LoRA-Laeufe verlangen fuer den konkreten Trainingsdatensatz weiterhin `gruen`.
- Fehlende oder `rot` markierte Provenienz sowie ein fehlender oder nicht grüner `rp_content`-Beleg blockieren den naechsten Schritt hart statt in Export oder Training durchzufallen.

Offene Punkte
-------------

- Vollstaendigkeit geprueft: Alle aktuell aktiven JSONL-Dateien unter `novapolis_agent/eval/datasets/**` sind in dieser Matrix erfasst.

- Beide zuvor gelben Datensaetze wurden auf User-Anweisung entfernt: `novapolis_agent/eval/datasets/chai-ai_small_v1.jsonl`.
- Beide zuvor gelben Datensaetze wurden auf User-Anweisung entfernt: `novapolis_agent/eval/datasets/neutral/neutral_gpt_samples.de.v1.jsonl`.
