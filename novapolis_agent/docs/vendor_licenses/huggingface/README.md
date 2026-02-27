---
stand: 2026-02-27 06:06
update: Lokale Lizenztexte fuer vier HF-Basismodelle abgelegt und Status auf vorhanden gesetzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "novapolis_agent/docs/vendor_licenses/huggingface/README.md" "novapolis_agent/docs/provenance-register.md" "novapolis_agent/docs/DONELOG.txt" PASS (2026-02-27 05:11); ./.venv/Scripts/python.exe scripts/check_frontmatter.py "novapolis_agent/docs/vendor_licenses/huggingface/README.md" "novapolis_agent/docs/provenance-register.md" "novapolis_agent/docs/DONELOG.txt" PASS (2026-02-27 05:11)
---

HuggingFace License Evidence
============================

Zweck
-----

- Lokale Lizenzkopien fuer externe Basismodelle, die im Training/Fine-Tuning genutzt werden.
- Diese Ablage dient als Compliance-Beleg fuer die Modellherkunft.

Pflichtfelder pro Modellnachweis
--------------------------------

- Modell-ID
- Upstream-URL
- Lizenzname laut Upstream
- Datum des Snapshots
- Dateiname der lokalen Lizenzkopie

Aktueller Zielkatalog
---------------------

| Modell-ID | Upstream | Lokale Lizenzkopie | Status |
| --- | --- | --- | --- |
| `sshleifer/tiny-gpt2` | `https://huggingface.co/sshleifer/tiny-gpt2` | `LICENSE-sshleifer-tiny-gpt2.txt` | vorhanden |
| `TinyLlama/TinyLlama-1.1B-Chat-v1.0` | `https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0` | `LICENSE-TinyLlama-1.1B-Chat-v1.0.txt` | vorhanden |
| `Qwen/Qwen2.5-0.5B-Instruct` | `https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct` | `LICENSE-Qwen2.5-0.5B-Instruct.txt` | vorhanden |
| `Qwen/Qwen2.5-1.5B-Instruct` | `https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct` | `LICENSE-Qwen2.5-1.5B-Instruct.txt` | vorhanden |

Hinweis
-------

- Keine Lizenztexte aus Drittquellen paraphrasieren; immer den offiziellen Lizenztext als Kopie ablegen.
- Fuer `sshleifer/tiny-gpt2` liegt im Upstream keine explizite Lizenzdatei vor; die lokale Lizenzkopie basiert daher auf dem Basismodell `openai-community/gpt2` (Lizenzkennung `mit`).
