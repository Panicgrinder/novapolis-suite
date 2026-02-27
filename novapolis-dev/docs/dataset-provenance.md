---
stand: 2026-02-27 06:06
update: Provenance-Matrix auf den vollstaendigen aktiven Dataset-Bestand erweitert (inkl. quality_de und eval-smoke) und Vollstaendigkeitscheck dokumentiert.
checks: npx --yes markdownlint-cli2 --config f:/VS-Code-Workspace/Main/.markdownlint-cli2.jsonc "f:/VS-Code-Workspace/Main/novapolis_agent/docs/provenance-register.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/vendor_licenses/huggingface/README.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-voice-provenance-log.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/dataset-provenance.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-compliance-policy.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" PASS (2026-02-27 05:00); f:/VS-Code-Workspace/Main/.venv/Scripts/python.exe f:/VS-Code-Workspace/Main/scripts/check_frontmatter.py "f:/VS-Code-Workspace/Main/novapolis_agent/docs/provenance-register.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/vendor_licenses/huggingface/README.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-voice-provenance-log.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/dataset-provenance.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-compliance-policy.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" PASS (EXITCODE=0, 2026-02-27 05:00)
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
