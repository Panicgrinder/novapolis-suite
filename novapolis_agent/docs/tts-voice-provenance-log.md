---
stand: 2026-02-27 06:06
update: Voice-Provenance-Log als Pflichtnachweis fuer produktive Runtime-Stimmen angelegt.
checks: npx --yes markdownlint-cli2 --config f:/VS-Code-Workspace/Main/.markdownlint-cli2.jsonc "f:/VS-Code-Workspace/Main/novapolis_agent/docs/provenance-register.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/vendor_licenses/huggingface/README.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-voice-provenance-log.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/dataset-provenance.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-compliance-policy.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" PASS (2026-02-27 05:00); f:/VS-Code-Workspace/Main/.venv/Scripts/python.exe f:/VS-Code-Workspace/Main/scripts/check_frontmatter.py "f:/VS-Code-Workspace/Main/novapolis_agent/docs/provenance-register.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/vendor_licenses/huggingface/README.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-voice-provenance-log.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/dataset-provenance.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-compliance-policy.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" PASS (EXITCODE=0, 2026-02-27 05:00)
---

TTS Voice Provenance Log
========================

Zweck
-----

- Nachweisakte fuer produktiv genutzte Runtime-Stimmen aus dem Coqui-Provider.
- Erfasst Herkunft, Lizenzbezug und Snapshot-Kontext pro Stimme.

Schema
------

| snapshot_date | provider | voice_id | source_model_id | source_endpoint | license_ref | decision | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |

Regeln
------

- `decision` nur `approved` oder `blocked`.
- `license_ref` verweist auf eine lokale Datei unter `novapolis_agent/docs/vendor_licenses/**`.
- Ohne gepflegten Eintrag gilt eine Runtime-Stimme als nicht freigegeben fuer produktive Nutzung.

Initialer Stand
---------------

- Noch keine produktive Stimme in dieser Akte eingetragen.
- Vor produktivem Betrieb die aktuelle `/tts/voices`-Antwort protokollieren und pro Stimme nachziehen.
