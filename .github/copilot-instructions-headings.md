---
stand: 2026-02-17 11:10
update: Kern-SSOT um Naming/Whitespace/Format/Quarantäne ergänzt; R-IDX als Mini-Gate verankert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py PASS
---

Hinweis
=======

Diese Datei ist der kompakte Navigationsindex für das aktuelle
Instruction-System:

- Kern-SSOT: `.github/copilot-instructions.md`
- Scoped-Regeln: `.github/instructions/*.instructions.md`

Aktuelle Überschriften (Kern + Scoped)
--------------------------------------

Quelle: Stand `2026-02-17 10:55` der Kern-Datei und der zugehörigen
scoped Instruction-Files.

1) Kern-SSOT
------------

Datei: `.github/copilot-instructions.md`

- LLM-Dokumentenheader (nicht löschen)
- Dateipfad & Geltungsbereich
- Globale Kernregeln
- Regelmatrix (Kern)
- Scoped Instruction-Files
- Postflight-Schema (5 Zeilen)
- Kompakter Meta-Block (rein lesend)

Neue/geschärfte Kernabschnitte:

- Namensgebungskonvention
- Kanonisierung & Formatnorm (syntaktisch)
- Quarantäne & Backup-Ort
- R-IDX Mini-Gate

2) Scoped Instructions
----------------------

Datei: `.github/instructions/python-runtime.instructions.md`

- Python Runtime
- Ziel
- Regeln
- Prüfsequenz
- Regelmatrix

Datei: `.github/instructions/agent-backend.instructions.md`

- Agent Backend
- Ziel
- Gates
- Konventionen
- Regelmatrix

Datei: `.github/instructions/rp-docs.instructions.md`

- RP & Docs
- Ziel
- Regeln
- Doku-Update-Pflicht
- Regelmatrix

Datei: `.github/instructions/docs-markdown.instructions.md`

- Docs Markdown
- Lint
- Frontmatter
- Diagnose-Playbook
- Regelmatrix

Datei: `.github/instructions/ci-release.instructions.md`

- CI & Release
- Ziel
- Regeln
- Regelmatrix

3) Pflege-Regel
---------------

Bei strukturrelevanten Änderungen in Kern oder scoped Instruction-Files
diesen Index im selben Änderungslauf mit aktualisieren.

