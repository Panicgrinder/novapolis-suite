---
stand: 2026-03-02 22:24
update: Quellenklarheit ergaenzt: aktive vs. sekundaere Instruction-Quellen in Kern-SSOT verankert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/copilot-instructions.md' '.github/copilot-instructions-headings.md' '.github/agents/novapolis-workspace-navigator.agent.md' 'novapolis-dev/docs/copilot-vscode-usage.md' 'novapolis-dev/archive/docs/others/copilot-instructions.2025-11-15 23-48.md' 'novapolis-dev/archive/docs/others/copilot-instructions-headings.archive.md' 'DONELOG.md' PASS (2026-02-27 10:57); .\.venv\Scripts\python.exe scripts/check_frontmatter.py '.github/agents/novapolis-workspace-navigator.agent.md' '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/copilot-vscode-usage.md' 'novapolis-dev/archive/docs/others/copilot-instructions.2025-11-15 23-48.md' 'novapolis-dev/archive/docs/others/copilot-instructions-headings.archive.md' 'DONELOG.md' PASS (EXITCODE=0, 2026-02-27 10:57)
---

Hinweis
=======

Diese Datei ist der kompakte Navigationsindex für das aktuelle
Instruction-System:

- Kern-SSOT: `.github/copilot-instructions.md`
- Scoped-Regeln: `.github/instructions/*.instructions.md`

Aktuelle Überschriften (Kern + Scoped)
--------------------------------------

Quelle: Stand `2026-02-27 10:57` der Kern-Datei und der zugehörigen
scoped Instruction-Files.

1) Kern-SSOT
------------

Datei: `.github/copilot-instructions.md`

- LLM-Dokumentenheader (nicht löschen)
- TL;DR / Runtime Essentials
- Dateipfad & Geltungsbereich
- Globale Kernregeln
- Regelmatrix (Kern)
- Scoped Instruction-Files
- Postflight-Schema (5 Zeilen)
- Kompakter Meta-Block (rein lesend)

Neue/geschärfte Kernabschnitte:

- Aktive vs. sekundäre Quellen
- Regel-ID-Index (Kern)
- Regel-ID-Landepunkte (Kern)
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

Datei: `.github/instructions/mind-cluster.instructions.md`

- Mind Cluster Governance
- Ziel
- Begriffsregeln
- Brainstorming-Modus
- Sphaerenmodell-Regeln
- Pflichtdaten
- Update-Disziplin
- Validierung
- Aenderungspflichten
- Regelmatrix

3) Pflege-Regel
---------------

Bei strukturrelevanten Änderungen in Kern oder scoped Instruction-Files
diesen Index im selben Änderungslauf mit aktualisieren.

