---
stand: 2026-02-24 15:35
update: Scoped Instruction und Template von mind-cluster auf den verbindlichen Namensstandard harmonisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/instructions/mind-cluster.instructions.md' 'novapolis-rp/database-rp/00-admin/mind-cluster-template.md' 'novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/ronja-kerschner-mind-cluster.md' 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md' '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/brainstorming.rp.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-02-24 15:10); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/mind-cluster-template.md' 'novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/ronja-kerschner-mind-cluster.md' 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md' '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/brainstorming.rp.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-02-24 15:10)
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

