Stand: 2026-02-21 20:49 – Modul-DONELOG-Pflicht als harte Globalregel ergänzt; R-DONELOG in Kernmatrix aufgenommen.
Checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/copilot-instructions.md' '.github/instructions/rp-docs.instructions.md' '.github/copilot-instructions-headings.md' 'DONELOG.md' PASS (2026-02-21 20:49; .github/copilot-instructions.md durch Config ausgeschlossen); .\.venv\Scripts\python.exe scripts\check_frontmatter.py '.github/instructions/rp-docs.instructions.md' '.github/copilot-instructions-headings.md' 'DONELOG.md' PASS (2026-02-21 20:49)


LLM-Dokumentenheader (nicht löschen)
====================================
- Type: Copilot Instruction Set / Project Governance
- Scope: Novapolis-Suite (VS Code Workspace Main)
- Language: Deutsch
- Encoding: UTF-8 / Unix-EOL
- Purpose: Verbindlicher Kern für globale Regeln; Details leben in scoped Instruction-Files.
- Priority: Diese Datei bleibt SSOT für globale Governance.
- Audit: Jede mutationale Aktion endet mit genau einem Postflight-Block.

Dateipfad & Geltungsbereich
---------------------------
### Kanonischer Speicherort
- `.github/copilot-instructions.md` im Repo-Root.

### SSOT-Definition (Kern + Scoped)
- Diese Datei ist SSOT für globale Regeln und Prioritäten.
- Scoped Instruction-Files unter `.github/instructions/*.instructions.md` sind ausdrücklich erlaubt.
- Scoped Files ergänzen oder präzisieren nur innerhalb ihres `applyTo`-Scopes.
- Scoped Files dürfen globale Kernregeln dieser Datei nicht aufheben.

### Konfliktpriorität (Leitlinie)
- 1. Höchste Priorität: System-/Plattformvorgaben und explizite User-Anweisung im aktuellen Chat.
- 2. Diese Kerndatei (`.github/copilot-instructions.md`) für globale Governance.
- 3. Scoped `.instructions.md` mit passendem `applyTo`.
- 4. Bei Konflikt soll das Modell spezifischere Regeln bevorzugen; widersprüchliche Regeln sind zu vermeiden.
- 5. Bei unklarer Lage: STOP-Gate auslösen, keine Mutation vor Klärung.

Globale Kernregeln
------------------
### Kommunikationsmodus
- Standard-Antwortsprache: Deutsch.
- Prägnant, skimmbar, minimalinvasiv.

### STOP-Gate (aktiv, scharf)
- Hard-Trigger: Code-/Doc-Mutationen, skriptgestützte Änderungen, Policy-Änderungen.
- Soft-Trigger: Mehrdeutigkeit, Konflikt, fehlender Kontext.
- Ohne Freigabe bei Hard-Trigger keine Ausführung.

### Wrapper-Policy & Guards
- Mehrschritt-/Artefaktbefehle über Python-Wrapper (`.venv` bevorzugt, Fallback `python`).
- Inline `pwsh -Command` nur echte Einzeiler.
- Ausnahme: Markdownlint ausschließlich via `npx --yes markdownlint-cli2 ...`.
- Vor Ausführung Guards prüfen: Pfad, Kontextquellen, STOP-Status.

### Kontextquellen (Mindestset)
- `.github/copilot-instructions.md`
- betroffene Arbeitsdateien
- bei Doku-/Planungsthemen zusätzlich `todo.root.md`, `DONELOG.md`, `WORKSPACE_STATUS.md`

### Logging/Receipt-Pflicht
- Nach jeder Dateimutation oder Skript-/Testausführung genau ein Postflight-Receipt am Ende der Antwort.
- Kein Zwischen-Receipt für Teilaktionen.

### Modul-DONELOG-Pflicht
- Bei jeder Dateimutation (Code, Doku, Config, Workflow, Skript) ist im selben Änderungslauf ein Eintrag im passenden Modul-DONELOG verpflichtend.
- Zuordnung: bevorzugt Modul-DONELOG (z. B. `novapolis-dev/docs/donelog.md` für Dev/RP-Doku, `novapolis_agent/docs/DONELOG.txt` für Agent-Modul); falls kein Modul-DONELOG existiert, in `DONELOG.md` auf Root-Ebene dokumentieren.
- Kein Interpretationsspielraum über „Relevanz“: Mutation erkannt ⇒ DONELOG-Eintrag verpflichtend.

### Sicherheitsprinzip
- Minimalinvasive Diffs.
- Keine destruktiven Änderungen ohne vorgeschaltete WhatIf-/Prüfphase.
- Keine Secrets/PII in Logs/Receipts.

### Lint- und Frontmatter-Gates
- Markdownlint verpflichtend: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'`.
- Frontmatter-Validator verpflichtend: `scripts/check_frontmatter.py`.
- Ausnahme GOV-EX-FM-001: Diese Datei bleibt ohne YAML-Frontmatter.
- Ausnahme GOV-EX-INS-001: `.github/instructions/*.instructions.md` nutzen nur instruction-spezifische Frontmatter-Felder (`description`, `name`, `applyTo`).

### Namensgebungskonvention
- Regel-IDs im Format `R-<BEREICH>-<THEMA>` (Großbuchstaben, Bindestrich-separiert).
- Instruction-Dateien unter `.github/instructions/` enden auf `.instructions.md`.
- Bezeichner in Frontmatter-Feldern (`name`, `description`) bleiben stabil und eindeutig.

### Kanonisierung & Formatnorm (syntaktisch)
- Markdown-Dateien in UTF-8 ohne BOM, Unix-EOL, genau eine abschließende Newline.
- Kein Trailing-Whitespace; Leerzeilen konsistent und minimal.
- Überschriften-Hierarchie strikt einhalten; Delimiter `---` nicht unbeabsichtigt verändern.

### Quarantäne & Backup-Ort
- Arbeitskopien/Backups nicht lose im Repo-Root ablegen.
- Quarantänepfad für temporäre Kopien: `novapolis-dev/archive/quarantine/`.
- Backups nur mit nachvollziehbarer Quelle und alternativesicherer Zielablage erstellen.

### R-IDX Mini-Gate
- Bei strukturrelevanten Änderungen an Kern- oder Scoped-Instructions ist `.github/copilot-instructions-headings.md` im selben Änderungslauf zu aktualisieren.

### Zeitkonvention
- Zeitquelle immer frisch via `Get-Date`.
- Format: `YYYY-MM-DD HH:mm` (lokal).

Regelmatrix (Kern)
------------------
### Feldset
- `id, priority, scope, trigger, action, validation, exceptions, notes`

### Matrix
- `id: R-STOP, priority: 1, scope: repo, trigger: hard_or_soft_conflict, action: stop_and_request_confirmation, validation: no_mutation_before_confirm, exceptions: none, notes: hard_has_precedence`
- `id: R-WRAP, priority: 1, scope: repo, trigger: multistep_or_artifacts, action: use_python_wrapper, validation: wrapper_policy=erfüllt, exceptions: markdownlint_npx_yes, notes: inline_pwsh_only_oneliner`
- `id: R-CTX, priority: 1, scope: repo, trigger: before_action, action: load_minimum_context_sources, validation: sources_listed_in_receipt, exceptions: trivial_readonly_smalltalk, notes: include_affected_files`
- `id: R-LOG, priority: 1, scope: repo, trigger: file_mutation_or_script_run, action: emit_single_postflight_receipt, validation: receipt_has_5_lines, exceptions: readonly_general_mode, notes: receipt_is_last_block`
- `id: R-DONELOG, priority: 1, scope: repo, trigger: any_file_mutation, action: append_module_donelog_entry_same_change_set, validation: donelog_entry_present_and_scoped, exceptions: none, notes: if_no_module_log_then_root_donelog`
- `id: R-SEC, priority: 1, scope: repo, trigger: risky_or_destructive_change, action: apply_minimal_diff_and_precheck, validation: whatif_or_equivalent_done, exceptions: none, notes: no_secret_output`
- `id: R-LINT, priority: 1, scope: docs, trigger: markdown_change, action: run_markdownlint_cli2, validation: exitcode_0, exceptions: none, notes: use_npx_yes_only`
- `id: R-FM, priority: 1, scope: docs, trigger: markdown_change, action: run_frontmatter_validator, validation: required_keys_present, exceptions: GOV_EX_FM_001, notes: stand_update_checks_required`
- `id: R-NAME, priority: 1, scope: governance_docs, trigger: rule_or_instruction_change, action: enforce_naming_conventions, validation: ids_and_instruction_filenames_are_canonical, exceptions: none, notes: r_id_and_instruction_suffix_policy`
- `id: R-WS, priority: 1, scope: markdown_docs, trigger: markdown_change, action: enforce_whitespace_canonization, validation: utf8_no_bom_unix_eol_single_trailing_newline_no_trailing_spaces, exceptions: none, notes: syntax_only_rule`
- `id: R-FMT, priority: 1, scope: markdown_docs, trigger: markdown_change, action: enforce_markdown_format_norm, validation: heading_hierarchy_and_frontmatter_delimiters_stable, exceptions: GOV_EX_FM_001, notes: syntax_only_no_content_policy`
- `id: R-QUAR, priority: 1, scope: backups_and_copies, trigger: backup_or_copy_operation, action: route_to_quarantine_path, validation: no_loose_root_backups_and_traceable_source, exceptions: archival_migration_with_stop_approval, notes: target_novapolis_dev_archive_quarantine`
- `id: R-IDX, priority: 1, scope: governance_index, trigger: instruction_structure_change, action: update_headings_index_same_change_set, validation: headings_index_matches_current_sections, exceptions: none, notes: promote_idx_to_mini_gate`
- `id: R-TIME, priority: 2, scope: receipts_and_logs, trigger: timestamp_needed, action: use_fresh_get_date_value, validation: format_yyyy_mm_dd_hh_mm, exceptions: none, notes: no_cached_timestamps`

Scoped Instruction-Files
------------------------
- `.github/instructions/python-runtime.instructions.md`
- `.github/instructions/agent-backend.instructions.md`
- `.github/instructions/rp-docs.instructions.md`
- `.github/instructions/docs-markdown.instructions.md`
- `.github/instructions/ci-release.instructions.md`

Postflight-Schema (5 Zeilen)
----------------------------
### Format
- Zeile 1 (`Meta`): `Modus, Modell, Arbeitsverzeichnis, RepoRoot, PSScriptRoot, PSVersion, Aufruf, SHA256, STOP-Gate, Wrapper-Policy, Wrapper-Guards, Quellen, Aktion`
- Zeile 2 (`Prüfung`): `markdownlint, ExitcodeLint, behobenLint, Frontmatter-Validator, ExitcodeFM, behobenFM, Cleanup-WhatIf-Exit, behobenWhatIf, Cleanup-Real-Exit, behobenReal, WorkspaceScanRoot, WorkspaceScanRecurse`
- Zeile 3 (`Regeln`): `IDs, Details`
- Zeile 4 (`Todos`): `offen, BeispielFix, ReRun, Fällig`
- Zeile 5 (`Ende`): `Timestamp`

Kompakter Meta-Block (rein lesend)
----------------------------------
- `Meta: Modus=General, Modell=<...>, Aktion=<...>, Timestamp=<yyyy-MM-dd HH:mm>[, Arbeitsverzeichnis=<...>]`
