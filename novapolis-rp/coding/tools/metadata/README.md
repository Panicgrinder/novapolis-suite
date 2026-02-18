---
stand: 2026-02-18 04:05
update: Metadata-Init konsolidiert; Python-Skript ist kanonisch.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc DONELOG.md WORKSPACE_STATUS.md todo.root.md novapolis-rp/coding/tools/metadata/README.md novapolis-dev/docs/donelog.md PASS (2026-02-18 04:05); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe scripts/check_frontmatter.py DONELOG.md WORKSPACE_STATUS.md todo.root.md novapolis-rp/coding/tools/metadata/README.md novapolis-dev/docs/donelog.md PASS (2026-02-18 04:05)
---

Metadata Tool (Stub)
====================
Details & JSON-Shape jetzt im Hub: `novapolis-dev/docs/readme.hub.md` → "Metadata Layer".

Kurz:
- Erzeugt Companion JSON neben Markdown (Struktur/Tags, kein Text-Eingriff).
- Dry-Run / Overwrite Flags.
- Kanonischer Einstieg: `python novapolis-rp/coding/tools/metadata/init_metadata.py --dry-run --root novapolis-rp`.
- Konsolidierungsstand (2026-02-18): `init_metadata.py` ist die einzige aktive Init-Implementierung; die frühere JS-Variante `init-metadata.js` wurde entfernt.
- Siehe Hub für Beispiele & Integrationshinweise.


