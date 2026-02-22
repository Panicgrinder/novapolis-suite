---
stand: 2026-02-20 00:57
update: Konsolidierter Ziellog aus Workspace-Quellen (neuester Eintrag oben).
checks: generated_by_scripts_consolidate_donelogs_py
---

DONELOG DEV
===========

Format: `YYYY-MM-DD HH:mm | author | summary | source=<relative-path>`

2026-01-11 04:09 | Copilot | Basis-Stabilisierung: Root-READMEs `checks:`-Receipt nachgezogen | source=DONELOG.md
2026-01-11 03:51 | Copilot | Basis-Stabilisierung: `checks: pending` in Docs/READMEs bereinigt (20 Dateien) | source=DONELOG.md
2025-11-12 01:38 | Copilot | DONELOG-Sync (Dev-Hub): Frontmatter aktualisiert; zentraler Vorbereitungseintrag vor Repo-weitem Prüfskript (damals PowerShell, inzwischen `python scripts/run_checks_and_report.py`). | source=novapolis-dev/docs/donelog.md
2025-10-25 23:59 | Copilot | LLM-Optionen erweitert: ChatOptions & Normalisierung (top_k, min_p, typical_p, tfs_z, mirostat*, penalize_newline); Settings-Defaults ergänzt; README dokumentiert; Validation-Tests hinzugefügt; Gates PASS. | source=DONELOG.md
2025-10-25 23:58 | Panicgrinder | eval_ui: profiles support top_p/num_predict; added sample profile policies; updated eval README; tests+types PASS | source=DONELOG.md
2025-10-25 22:37 | Panicgrinder | README: kurzer Abschnitt 'Lokales RAG' ergänzt (Flags, Indexer-CLI, Beispiel, Task-Hinweise); keine Codeänderungen; Gates grün. | source=DONELOG.md
2025-10-23 10:50 | Copilot | Lizenz hinzugefügt: MIT-Lizenz-Datei (`LICENSE`) und Hinweis in README. | source=DONELOG.md
2025-10-23 00:22 | Panicgrinder | Context notes: directory order via ORDER file; ignore README/ORDER meta; collapse excessive blank lines in loader; docs+tests updated | source=DONELOG.md
2025-10-21 23:36 | Panicgrinder | Docs: add BEHAVIOR.md (Projektverhalten) und WORKSPACE_INDEX.md aktualisiert. | source=DONELOG.md
2025-10-19 12:28 | Copilot | Backup-Härtung: cvn-root-files ZIP sanitized (ohne .env) und im Release ersetzt; MANIFEST mit SHA-256 für alle Assets aktualisiert; README mit Restore-Anleitung ergänzt. | source=DONELOG.md
2025-10-19 12:12 | Copilot | Backup: Separates Backup-Repo finalisiert (origin auf neues Repo), orphan main mit README+MANIFEST; GitHub Release erstellt und alle Snapshot-Dateien als Assets hochgeladen (um LFS-Grenzen zu vermeiden). | source=DONELOG.md
2025-10-15 16:26 | Copilot | README/TODO/Customization nach markdownlint (MD031/MD032/MD012/MD009/MD007) bereinigt. | source=DONELOG.md
