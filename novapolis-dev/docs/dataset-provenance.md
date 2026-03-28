---
stand: 2026-03-28 06:51
update: Phase-2-Konsistenzlauf aktualisiert den Provenance-Header auf den aktuellen PASS-Kontext, ohne die Matrixinhalte zu aendern.
checks: markdownlint PASS; frontmatter PASS; path-portability PASS; logs-policy PASS (2026-03-28 01:31)
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

Freigaberegel
-------------

- `gruen`: Nutzung fuer Eval/Training im Repo freigegeben.
- `gelb`: Nutzung nur intern fuer Eval, bis Quellen- oder Lizenznachweis explizit dokumentiert ist.
- `rot`: Keine Nutzung bis zur Klaerung.

Offene Punkte
-------------

- Vollstaendigkeit geprueft: Alle aktuell aktiven JSONL-Dateien unter `novapolis_agent/eval/datasets/**` sind in dieser Matrix erfasst.

- Beide zuvor gelben Datensaetze wurden auf User-Anweisung entfernt: `novapolis_agent/eval/datasets/chai-ai_small_v1.jsonl`.
- Beide zuvor gelben Datensaetze wurden auf User-Anweisung entfernt: `novapolis_agent/eval/datasets/neutral/neutral_gpt_samples.de.v1.jsonl`.
