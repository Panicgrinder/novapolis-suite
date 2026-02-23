---
stand: 2026-02-23 12:32
update: Strikte TTS-Compliance eingefuehrt (deny-by-default, lokale Lizenzkopien verpflichtend, unsichere Modelle blockiert).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis_agent/docs/tts-compliance-policy.md' PASS (2026-02-23 12:16); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis_agent/docs/tts-compliance-policy.md' PASS (EXITCODE=0, 2026-02-23 12:16)
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
