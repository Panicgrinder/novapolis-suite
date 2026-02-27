---
stand: 2026-02-27 06:06
update: Runtime-Voice-Provenance als Pflichtnachweis ergaenzt und auf zentrale Provenance-Artefakte verlinkt.
checks: npx --yes markdownlint-cli2 --config f:/VS-Code-Workspace/Main/.markdownlint-cli2.jsonc "f:/VS-Code-Workspace/Main/novapolis_agent/docs/provenance-register.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/vendor_licenses/huggingface/README.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-voice-provenance-log.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/dataset-provenance.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-compliance-policy.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" PASS (2026-02-27 05:00); f:/VS-Code-Workspace/Main/.venv/Scripts/python.exe f:/VS-Code-Workspace/Main/scripts/check_frontmatter.py "f:/VS-Code-Workspace/Main/novapolis_agent/docs/provenance-register.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/vendor_licenses/huggingface/README.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-voice-provenance-log.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/dataset-provenance.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/tts-compliance-policy.md" "f:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "f:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" PASS (EXITCODE=0, 2026-02-27 05:00)
---

TTS Compliance Policy (Strict)
==============================

Ziel
----

- In diesem Repository sind nur TTS-Modelle erlaubt, die nahezu rechtssicher und technisch nachvollziehbar freigegeben sind.
- Alles Unklare oder risikobehaftete bleibt blockiert.

Harte Regeln
------------

- Default ist `deny`.
- Ein Modell darf nur genutzt werden, wenn es in `novapolis_agent/config/tts_model_allowlist.json` als `approved` steht.
- Fuer jedes freigegebene Modell muss eine lokale Lizenzkopie im Repo vorhanden sein.
- Modelle mit unklaren Bedingungen oder Zusatzpflichten (z. B. TOS-Zwang) bleiben gesperrt, bis eine dokumentierte Freigabe vorliegt.
- Modelle mit `non-commercial` oder `no-derivatives` sind in diesem Projekt standardmaessig gesperrt.

Pflichtnachweise pro Modell
---------------------------

- Modell-ID
- Version/Commit/Quelle
- Exakte Lizenzbezeichnung
- Lokaler Lizenzdateipfad
- Entscheidung: `approved` oder `blocked`
- Begruendung der Entscheidung

Ablage fuer Lizenzkopien
------------------------

- Ordner: `novapolis_agent/docs/vendor_licenses/coqui/`
- Beispiel: `novapolis_agent/docs/vendor_licenses/coqui/LICENSE-coqui-TTS.txt`

Freigabeprozess (Kurz)
----------------------

1. Modell und Bedingungen pruefen.
2. Lizenztext lokal ablegen.
3. Allowlist-Eintrag erstellen.
4. Erst dann technischen Export freigeben.

Technische Durchsetzung
-----------------------

- Script: `novapolis_agent/scripts/tts_coqui_export.py`
- Das Script blockiert Ausfuehrung, wenn Modell nicht freigegeben ist oder Lizenzkopie fehlt.
- Kompatibilitaets-Entry: `novapolis_agent/scripts/tts_export_coqui.py`

Runtime-Stimmen (zusaetzliche Pflicht)
--------------------------------------

- Fuer produktive Runtime-Nutzung von Coqui-Stimmen muss ein Voice-Provenance-Eintrag vorhanden sein.
- Pflichtakte: `novapolis_agent/docs/tts-voice-provenance-log.md`.
- Ohne Eintrag gilt eine Stimme als nicht freigegeben fuer produktive Nutzung.

Zentrale Nachweisquellen
------------------------

- Gesamtregister: `novapolis_agent/docs/provenance-register.md`
- Vendor-Lizenzen: `novapolis_agent/docs/vendor_licenses/`
