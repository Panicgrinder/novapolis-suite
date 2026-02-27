---
stand: 2026-02-27 06:06
update: HF-Lizenztexte lokal abgelegt und Modellstatus im Register auf gruen gesetzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "novapolis_agent/docs/vendor_licenses/huggingface/README.md" "novapolis_agent/docs/provenance-register.md" "novapolis_agent/docs/DONELOG.txt" PASS (2026-02-27 05:11); ./.venv/Scripts/python.exe scripts/check_frontmatter.py "novapolis_agent/docs/vendor_licenses/huggingface/README.md" "novapolis_agent/docs/provenance-register.md" "novapolis_agent/docs/DONELOG.txt" PASS (2026-02-27 05:11)
---

Provenance Register (KI und TTS)
================================

Zweck
-----

- Zentraler Nachweis, welche Bausteine intern erstellt wurden und welche externen Ursprung haben.
- Rechts-/Compliance-Status wird pro Artefakt klar markiert: `gruen`, `gelb`, `rot`.

Legende
-------

- `gruen`: Herkunft klar, Nachweise lokal vorhanden, Nutzung im aktuellen Scope freigegeben.
- `gelb`: Herkunft klar benannt, aber Nachweisakte lokal noch unvollstaendig.
- `rot`: Herkunft/Lizenz unklar oder Nutzung nicht freigegeben.

A) Interne Eigenentwicklungen
-----------------------------

| Artefaktklasse | Scope | Herkunft | Nachweis | Status |
| --- | --- | --- | --- | --- |
| Agent-Backend-Code | `novapolis_agent/app/**`, `novapolis_agent/scripts/**` | intern entwickelt | Git-Historie + `novapolis_agent/docs/DONELOG.txt` | gruen |
| Training-Profile | `novapolis_agent/eval/datasets/training/*.jsonl` | intern erstellt | `novapolis-dev/docs/dataset-provenance.md` | gruen |
| Eval-Pakete neutral/rpg/quality | `novapolis_agent/eval/datasets/{neutral,rpg}/**` | intern migriert/normalisiert bzw. intern generiert | `novapolis-dev/docs/dataset-provenance.md` | gruen |
| LoRA-Artefakte | `outputs/lora-*` | intern erzeugt aus dokumentierten Runs | Run-CLI + Run-Metriken in `novapolis_agent/docs/DONELOG.txt` | gruen |

B) Externe Basismodelle (Training)
----------------------------------

| Modell-ID | Verwendungsstelle | Herkunft klar benannt | Lokale Lizenzkopie | Status |
| --- | --- | --- | --- | --- |
| `sshleifer/tiny-gpt2` | `fine_tune_pipeline.py`, LoRA-Baselines | ja (HF-ID) | `docs/vendor_licenses/huggingface/LICENSE-sshleifer-tiny-gpt2.txt` | gruen |
| `TinyLlama/TinyLlama-1.1B-Chat-v1.0` | `train_lora.py` Default, historische LoRA-Runs | ja (HF-ID) | `docs/vendor_licenses/huggingface/LICENSE-TinyLlama-1.1B-Chat-v1.0.txt` | gruen |
| `Qwen/Qwen2.5-0.5B-Instruct` | Free-Allowlist | ja (HF-ID) | `docs/vendor_licenses/huggingface/LICENSE-Qwen2.5-0.5B-Instruct.txt` | gruen |
| `Qwen/Qwen2.5-1.5B-Instruct` | Free-Allowlist | ja (HF-ID) | `docs/vendor_licenses/huggingface/LICENSE-Qwen2.5-1.5B-Instruct.txt` | gruen |

C) TTS (Coqui)
--------------

| Komponente | Herkunft | Nachweis | Status |
| --- | --- | --- | --- |
| Coqui-Export-Policy | intern implementiert, deny-by-default | `novapolis_agent/scripts/tts_coqui_export.py`, `novapolis_agent/config/tts_model_allowlist.json` | gruen |
| Coqui-Model-Lizenzablage | externer Vendor | `novapolis_agent/docs/vendor_licenses/coqui/LICENSE-coqui-TTS.txt` | gruen |
| Runtime-Stimmenliste (`/tts/voices`) | extern vom Coqui-Endpoint geliefert | Voice-Provenance-Log (siehe Datei `novapolis_agent/docs/tts-voice-provenance-log.md`) | gelb |

D) Harte Guardrails
-------------------

- Build-Time-TTS ist ohne explizite Allowlist-Freigabe blockiert (`default_action=deny`).
- Lokale Lizenzkopie ist fuer Build-Time-TTS-Modelle verpflichtend (`require_local_license_copy=true`).
- Fuer Runtime-Stimmen darf produktive Nutzung nur mit ausgefuellter Voice-Provenance-Akte erfolgen.

E) Offene Nachweise (konkret)
-----------------------------

1. Voice-Provenance-Log je produktiv genutzter Runtime-Stimme ausfuellen (Quelle, Modell-ID, Lizenz, Snapshot-Datum).
