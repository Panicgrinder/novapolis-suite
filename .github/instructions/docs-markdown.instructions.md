---
description: Regeln für Markdownlint, Frontmatter-Gates, Delimiter-Schutz und Lint-Diagnostik.
name: Docs Markdown Instructions
applyTo: .github/**/*.md,novapolis-dev/docs/**/*.md,novapolis_agent/docs/**/*.md,README.md,DONELOG.md,WORKSPACE_STATUS.md,WORKSPACE_INDEX.md,todo.root.md
---

Docs Markdown
=============

Lint
----
- Markdownlint immer über `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'`.
- Keine globalen Installationen, keine Wrapper für Markdownlint.

Frontmatter
-----------
- Standard-Schlüssel: `stand`, `update`, `checks`.
- Delimiter `---` oben/unten niemals unbeabsichtigt entfernen.
- Validator: `scripts/check_frontmatter.py`.
- Ausnahme GOV-EX-FM-001: `.github/copilot-instructions.md` ohne YAML-Frontmatter.
- Ausnahme GOV-EX-INS-001: `.github/instructions/*.instructions.md` folgen dem Instruction-Frontmatter-Schema (`description`, `name`, `applyTo`).

Kanonisierung & Format
----------------------
- Kodierung: UTF-8 ohne BOM; Zeilenenden: Unix-EOL.
- Genau eine abschließende Newline und kein Trailing-Whitespace.
- Formatnorm ist syntaktisch: Heading-Hierarchie, Delimiter-Integrität, konsistente Leerzeilen.

Diagnose-Playbook
-----------------
- Run: Lint-Ausgabe bei Bedarf nach `lint_fail.out` spiegeln.
- Analyse: PowerShell + Python Here-String (kein Bash, kein Multi-Line `python -c`).
- Fixfokus: MD012, MD047 zuerst, dann erneut prüfen.

Regelmatrix
-----------
- `id: R-LINT, priority: 1, scope: markdown_docs, trigger: markdown_change, action: run_markdownlint_cli2, validation: exitcode_0, exceptions: none, notes: command_must_use_npx_yes`
- `id: R-FM, priority: 1, scope: markdown_docs, trigger: markdown_change, action: validate_frontmatter, validation: required_keys_and_delimiters_ok, exceptions: GOV_EX_FM_001, notes: utf8_no_bom_single_trailing_newline`
- `id: R-WS, priority: 1, scope: markdown_docs, trigger: markdown_change, action: enforce_whitespace_canonization, validation: utf8_no_bom_unix_eol_single_trailing_newline_no_trailing_spaces, exceptions: none, notes: syntax_only_rule`
- `id: R-FMT, priority: 1, scope: markdown_docs, trigger: markdown_change, action: enforce_markdown_format_norm, validation: heading_hierarchy_and_frontmatter_delimiters_stable, exceptions: GOV_EX_FM_001, notes: syntax_only_no_content_policy`
- `id: R-LINT-DIAG, priority: 2, scope: diagnostics, trigger: lint_fail_detected, action: capture_and_analyze_output, validation: issue_clusters_identified, exceptions: none, notes: prioritize_minimal_safe_fixes`
