---
stand: 2026-03-28 06:51
update: Snapshot-Retry-Pfad operativ gehaertet; der Headings-Index spiegelt die aktualisierte Hook-Reihenfolge mit.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/copilot-instructions.md' '.github/copilot-instructions-headings.md' '.github/instructions/docs-markdown.instructions.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_frontmatter.py '.github/copilot-instructions-headings.md' '.github/instructions/docs-markdown.instructions.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (EXITCODE=0, 2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_todo_index_sync.py --repo-root . --write-index-meta PASS (2026-03-27 15:47); .\.venv\Scripts\python.exe scripts/check_logs_policy.py --repo-root . PASS (2026-03-27 15:47)
---

Hinweis
=======

Diese Datei ist der kompakte Navigationsindex für das aktuelle
Instruction-System:

- Kern-SSOT: `.github/copilot-instructions.md`
- Scoped-Regeln: `.github/instructions/*.instructions.md`

Aktuelle Überschriften (Kern + Scoped)
--------------------------------------

Quelle: Stand `2026-03-28 02:02` der Kern-Datei und der zugehörigen
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
- Normative Schichtung (Kern)
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

