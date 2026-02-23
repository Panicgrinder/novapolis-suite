---
stand: 2026-02-23 15:52
update: Kern-SSOT um Snapshot-Gates (Write-Lock/Freshness) erweitert und Regelmatrix um R-SNAP ergänzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/copilot-instructions-headings.md' 'DONELOG.md' 'novapolis_agent/README.md' 'novapolis_agent/docs/DONELOG.txt' PASS (2026-02-23 12:39); .\.venv\Scripts\python.exe scripts\check_frontmatter.py '.github/copilot-instructions-headings.md' 'DONELOG.md' 'novapolis_agent/README.md' 'novapolis_agent/docs/DONELOG.txt' PASS (2026-02-23 12:39)
---

Hinweis
=======

Diese Datei ist der kompakte Navigationsindex für das aktuelle
Instruction-System:

- Kern-SSOT: `.github/copilot-instructions.md`
- Scoped-Regeln: `.github/instructions/*.instructions.md`

Aktuelle Überschriften (Kern + Scoped)
--------------------------------------

Quelle: Stand `2026-02-23 12:39` der Kern-Datei und der zugehörigen
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
- Modul-DONELOG-Pflicht
- Snapshot-Gates (Write-Lock & Freshness)

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

