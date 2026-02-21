---
description: Regeln für RP-Dokumentation, Redirect-Stubs, RAW/Curation-Flow und Doku-Synchronisation.
name: RP Docs Instructions
applyTo: novapolis-rp/**/*.md,novapolis-dev/docs/**/*.md,WORKSPACE_INDEX.md,WORKSPACE_STATUS.md,todo.root.md,DONELOG.md
---

RP & Docs
=========

Ziel
----
- Konsistente Dokumentpflege mit klarer SSOT-Zuordnung und minimalen Diffs.

Regeln
------
- SSOT für Working Docs: `novapolis-dev/docs/**`.
- Redirect-Stubs unter `novapolis-rp/development/...` nicht inhaltlich ausbauen.
- RAW-Exporte nur unter `novapolis-rp/database-raw/99-exports/`.
- Strukturänderungen in Status-/Index-Artefakten nachziehen.
- Arbeitskopien/Backups nicht lose im Repo-Root ablegen; Quarantänepfad: `novapolis-dev/archive/quarantine/`.
- Bei Neuanlage von `novapolis-rp/database-rp/**/*.md` mit `category: project` Frontmatter direkt RP-validator-konform setzen: `status` nur aus `[planned, active, paused, done, prototyping]` und `last_updated`/`last-updated` verpflichtend.

Doku-Update-Pflicht
------------------
- Bei jeder Dateiänderung im Scope ist ein Eintrag im passenden Modul-DONELOG verpflichtend (im selben Änderungslauf).
- TODO/DONELOG/Index synchron halten.
- Frontmatter (`stand`, `update`, `checks`) pflegen, sofern Datei nicht ausgenommen ist.
- Bei Konflikt/Unklarheit STOP auslösen.

Regelmatrix
-----------
- `id: R-RP-SSOT, priority: 1, scope: rp_docs, trigger: rp_doc_change, action: write_to_devhub_live_sources, validation: no_content_in_redirect_stubs, exceptions: redirect_readme_metadata, notes: keep_single_source_of_truth`
- `id: R-RAW, priority: 1, scope: data_exports, trigger: raw_export_operation, action: store_in_database_raw_exports, validation: no_unfiltered_data_in_database_rp, exceptions: none, notes: privacy_first`
- `id: R-DOCSYNC, priority: 1, scope: documentation, trigger: any_doc_file_mutation_in_scope, action: sync_todo_donelog_index_status, validation: touched_docs_consistent_and_donelog_updated, exceptions: none, notes: log_checks_results`
- `id: R-RP-PROJ-FM, priority: 1, scope: rp_docs, trigger: new_or_updated_project_markdown_in_database_rp, action: enforce_project_frontmatter_contract, validation: status_in_allowed_enum_and_last_updated_present, exceptions: none, notes: align_with_validate_rp_hard_gate`
- `id: R-QUAR, priority: 1, scope: backups_and_copies, trigger: backup_or_copy_operation, action: route_to_quarantine_path, validation: no_loose_root_backups_and_traceable_source, exceptions: archival_migration_with_stop_approval, notes: target_novapolis_dev_archive_quarantine`
