---
stand: 2026-02-25 18:33
update: Beide zuvor gelben Datensaetze entfernt und Statusmatrix auf verbleibende freigegebene Pakete reduziert.
checks: .\.venv\Scripts\python.exe novapolis_agent\scripts\validate_eval_datasets.py --strict --suite-config novapolis_agent\eval\config\suites.json --suite neutral --suite rpg PASS (2026-02-24 16:02); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/dataset-provenance.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-24 16:02); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/dataset-provenance.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-24 16:02)
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
| RPG Fantasy 21-40 | `novapolis_agent/eval/datasets/rpg/rpg_21_40_fantasy.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |
| RPG Dialog 41-60 | `novapolis_agent/eval/datasets/rpg/rpg_41_60_dialog.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |
| RPG Szenen 61-80 | `novapolis_agent/eval/datasets/rpg/rpg_61_80_szenen.v1.jsonl` | intern migriert/normalisiert | intern | gruen | `novapolis_agent/docs/DONELOG.txt:31` |

Freigaberegel
-------------

- `gruen`: Nutzung fuer Eval/Training im Repo freigegeben.
- `gelb`: Nutzung nur intern fuer Eval, bis Quellen- oder Lizenznachweis explizit dokumentiert ist.
- `rot`: Keine Nutzung bis zur Klaerung.

Offene Punkte
-------------

- Beide zuvor gelben Datensaetze wurden auf User-Anweisung entfernt: `novapolis_agent/eval/datasets/chai-ai_small_v1.jsonl`.
- Beide zuvor gelben Datensaetze wurden auf User-Anweisung entfernt: `novapolis_agent/eval/datasets/neutral/neutral_gpt_samples.de.v1.jsonl`.
