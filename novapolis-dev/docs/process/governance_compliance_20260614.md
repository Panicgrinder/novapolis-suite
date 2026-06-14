---
stand: 2026-06-14 14:37
update: Governance-Compliance-Notiz zum Wrapper-Checklauf und Doku-Mutationen
checks: overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260614_143533.md
---

Kurz: Was wir gemacht haben
-------------------------

- Erstellung: `novapolis-dev/docs/process/mini-lamas-architecture.ssot.md` (Dev/Process SSOT)
- Dokumentation: `novapolis-dev/docs/process/checks_run_20260614_142241_documentation.md` (Wrapper-Lauf Zusammenfassung)
- DONELOG: `novapolis-dev/docs/donelog.md` wurde während des Laufs aktualisiert (Frontmatter `stand` auf Snapshot synchronisiert).
- Governance-Run: `scripts/run_checks_and_report.py --update-workspace-tree --write-snapshot-lock --sync-docs-after-checks` ausgeführt; Snapshot geschrieben und `stand:`-Timestamps synchronisiert.
- Lint/Format: `ruff`- und `black`-Funde automatisch behoben; Wrapper erneut ausgeführt; Endstatus: PASS.
- Commits: Dokumente + Fixes committed und zu `origin/main` gepusht (commit: 8211bad8f..., 9d3d593e3...).

Governance-Checks (erledigt)
----------------------------

- R-CTX: Relevante Kontext-Quellen geprüft (`.github/copilot-instructions.md`, `.github/instructions/docs-markdown.instructions.md`, `novapolis-dev/docs/process/**`).
- R-SNAP: Snapshot-Lock geschrieben via `scripts/snapshot_write_lock.py` und `stand:`-Felder der betroffenen MD-Dateien synchronisiert (Timestamp: 2026-06-14 14:37).
- R-FM: Frontmatter-Validator `scripts/check_frontmatter.py` ausgeführt — keine Befunde.
- R-LINT: `npx --yes markdownlint-cli2` lief erfolgreich — keine MD-Fehler.
- R-DONELOG: `novapolis-dev/docs/donelog.md` aktualisiert (Eintrag zu SSOT + Checklauf).
- R-WRAP: Wrapper-Policy eingehalten — Wrapper erweitert und mit Governance-Flags ausgeführt.
- R-LOG: Postflight-Receipt (Reports) generiert: `.tmp/results/reports/checks_report_20260614_143533.md`.

Wohin zugreifen
----------------

- Konsolidierter Report: .tmp/results/reports/checks_report_20260614_143533.md
- Lauf-Dokumentation: novapolis-dev/docs/process/checks_run_20260614_142241_documentation.md
- SSOT: novapolis-dev/docs/process/mini-lamas-architecture.ssot.md
- DONELOG: novapolis-dev/docs/donelog.md

Nächste Schritte (empfohlen)
---------------------------

1. Review: Kurzer Review der SSOT `mini-lamas-architecture.ssot.md` durch Stakeholder.
2. Persistenz: Falls gewünscht, Report in `novapolis-dev/docs/reports/` archivieren (neuer Ordner).
3. Policy-Entscheidung: Entscheiden, ob Wrapper-Flags (`--update-workspace-tree`, `--write-snapshot-lock`, `--sync-docs-after-checks`) dauerhaft Standard werden sollen.

Evidenz
-------

- Snapshot: .snapshot.now = 2026-06-14 14:37
- Commits: 8211bad8f1d0 (doc), 9d3d593e336c (fixes)
