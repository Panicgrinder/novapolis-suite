stand: 2026-06-13 13:25
Checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'README.md' 'novapolis-dev/docs/copilot-vscode-usage.md' 'WORKSPACE_STATUS.md' 'DONELOG.md' 'novapolis-dev/docs/donelog.md' PASS (2026-05-19 05:10); .\.venv\Scripts\python.exe scripts\check_frontmatter.py README.md WORKSPACE_STATUS.md DONELOG.md novapolis-dev/docs/copilot-vscode-usage.md novapolis-dev/docs/donelog.md PASS (EXITCODE=0, 2026-05-19 05:10); GOV-EX-FM-001 fuer '.github/copilot-instructions.md' beachtet; snapshot-lock PASS (2026-05-19 05:14)


LLM-Dokumentenheader (nicht löschen)
====================================
- Type: Copilot Instruction Set / Project Governance
- Scope: Novapolis-Suite (VS Code Workspace Main)
- Language: Deutsch
- Encoding: UTF-8 / Unix-EOL
- Purpose: Verbindlicher Kern für globale Regeln; Details leben in scoped Instruction-Files.
- Priority: Diese Datei bleibt SSOT für globale Governance.
- Audit: Jede mutationale Aktion endet mit genau einem Postflight-Block.

TL;DR / Runtime Essentials
==========================
- Dieser Block ist nur Schnellorientierung; bindend fuer Runtime-Entscheidungen sind die `Regel-ID-Landepunkte (Kern)` plus passende scoped Instruction-Files.
- Aktive Governance-/Runtime-/SSOT-/Board-/Agent-Dateien sind primaer KI-operative Steuertexte; menschliche Lesbarkeit ist nachrangig.
- Snapshot-/Freshness-Pfad: siehe `R-SNAP`.
- STOP-/Freigabelogik: siehe `R-STOP`.
- Phase-2-Status: Agent-Policy-Haertung ist als normative Agent-Body-Schicht aktiv; automatische VS-Code-Frontmatter-Enforcement und Runtime-Hook-Enforcement sind davon getrennt.
- Wrapper-Policy: siehe `R-WRAP`.
- Markdown-/Frontmatter-Gates: siehe `R-LINT` und `R-FM`.
- DONELOG- und Receipt-Pflicht: siehe `R-DONELOG` und `R-LOG`.
- Portabilitaet aktiver Dokus: siehe `R-PATH`.
- Headings-Index-Nachzug: siehe `R-IDX`.

Dateipfad & Geltungsbereich
---------------------------
### Kanonischer Speicherort
- `.github/copilot-instructions.md` im Repo-Root.

### SSOT-Definition (Kern + Scoped)
- Diese Datei ist SSOT für globale Regeln und Prioritäten.
- Scoped Instruction-Files unter `.github/instructions/*.instructions.md` sind ausdrücklich erlaubt.
- Scoped Files ergänzen oder präzisieren nur innerhalb ihres `applyTo`-Scopes.
- Scoped Files dürfen globale Kernregeln dieser Datei nicht aufheben.
- In der Laborumgebung sind aktive SSOT-Dateien ausdruecklich bearbeitbare Arbeitsflaechen, wenn der aktuelle User-Auftrag gerade das Testen, Schaerfen, Erweitern oder Ergaenzen dieser SSOTs verlangt.
- Der Navigator-/Logging-Waechter-Modus darf in diesem Fall auch direkt in aktive SSOTs schreiben; das ist keine Regelverletzung, solange Evidenz-, Scope-, Snapshot-, Board-/DONELOG- und Minimaldiff-Regeln eingehalten werden.

### Konfliktpriorität (Leitlinie)
- 1. Höchste Priorität: System-/Plattformvorgaben und explizite User-Anweisung im aktuellen Chat.
- 2. Diese Kerndatei (`.github/copilot-instructions.md`) für globale Governance.
- 3. Scoped `.instructions.md` mit passendem `applyTo`.
- 4. Bei Konflikt soll das Modell spezifischere Regeln bevorzugen; widersprüchliche Regeln sind zu vermeiden.
- 5. Bei unklarer Lage: STOP-Gate auslösen, keine Mutation vor Klärung.

### Aktive vs. sekundäre Quellen
- Aktiv bindend sind nur `.github/copilot-instructions.md` und `.github/instructions/*.instructions.md`.
- `README.md` ist Einstieg und Kontextoberflaeche, aber keine aktive Runtime-Regelbasis.
- Ergänzend, aber nicht bindend für Runtime-Governance, sind Leitfäden wie `novapolis-dev/docs/copilot-vscode-usage.md`.
- Archivpfade unter `novapolis-dev/archive/**` sind historische Evidenz und nie als aktive Regelbasis zu behandeln.
- Bei Suchtreffern mit Mischlage (aktiv + archiviert) muss aktiv bindende Quelle explizit priorisiert und genannt werden.

Globale Kernregeln
------------------
### Normative Schichtung (Kern)
- Bindend fuer Runtime-Entscheidungen sind in dieser Datei nur die `Regel-ID-Landepunkte (Kern)`.
- Der `Regel-ID-Index (Kern)` ist reine Navigation.
- Die `Regelmatrix (Kern)` ist eine abgeleitete Kurzreferenz fuer Scanbarkeit und darf keine zusaetzlichen Normen gegenueber den Landepunkten einfuehren.
- Normtexte in aktiven Steuerdateien muessen KI-operativ eindeutig sein (Rollen, Scope, Load-Order, SSOT/Runtime-Grenzen, Gate-Status, erlaubte Aktionen) und duerfen nicht in menschenberatende Fliesstexte driften.
- Bei Abweichungen oder Pflegekonflikten gewinnen die `Regel-ID-Landepunkte (Kern)`; danach folgen scoped Instruction-Files gemaess `applyTo`.

### Regel-ID-Index (Kern)

| ID | Kurzname | Abschnittsueberschrift |
| --- | --- | --- |
| `R-STOP` | STOP-Gate | `#### R-STOP STOP-Gate (aktiv, scharf)` |
| `R-WRAP` | Wrapper-Policy | `#### R-WRAP Wrapper-Policy und Guards` |
| `R-CTX` | Kontextquellen | `#### R-CTX Kontextquellen (Mindestset)` |
| `R-LOG` | Receipt-Pflicht | `#### R-LOG Logging- und Receipt-Pflicht` |
| `R-DONELOG` | Modul-DONELOG | `#### R-DONELOG Modul-DONELOG-Pflicht` |
| `R-SEC` | Sicherheitsprinzip | `#### R-SEC Sicherheitsprinzip` |
| `R-PATH` | Pfadportabilitaet | `#### R-PATH Pfadportabilitaet in aktiven Dokus` |
| `R-LINT` | Markdownlint-Gate | `#### R-LINT Markdownlint-Gate` |
| `R-FM` | Frontmatter-Gate | `#### R-FM Frontmatter-Gate` |
| `R-SNAP` | Snapshot-Gate | `#### R-SNAP Snapshot-Gates (Write-Lock und Freshness)` |
| `R-NAME` | Namenskonvention | `#### R-NAME Namensgebungskonvention` |
| `R-WS` | Whitespace-Norm | `#### R-WS Kanonisierung und Whitespace-Norm` |
| `R-FMT` | Markdown-Formatnorm | `#### R-FMT Markdown-Formatnorm (syntaktisch)` |
| `R-QUAR` | Quarantaene-Ort | `#### R-QUAR Quarantaene- und Backup-Ort` |
| `R-IDX` | Headings-Index-Gate | `#### R-IDX Mini-Gate fuer Headings-Index` |
| `R-TIME` | Zeitkonvention | `#### R-TIME Zeitkonvention` |

### Regel-ID-Landepunkte (Kern)
#### R-STOP STOP-Gate (aktiv, scharf)
- Hard-Trigger: Code-/Doc-Mutationen, skriptgestützte Änderungen, Policy-Änderungen.
- Soft-Trigger: Mehrdeutigkeit, Konflikt, fehlender Kontext.
- Ohne Freigabe bei Hard-Trigger keine Ausführung.
- Stop-, Rueckfrage- und Scope-Checks sind explizite Semantik-Alignment-Mechanismen gegen KI-Default-Drift und kein Stoerfaktor.
- Eine explizite User-Anweisung im aktuellen Chat kann diese Freigabe selbst darstellen, wenn Ziel und Scope klar sind; bei Mehrdeutigkeit, Konflikt oder verdeckter Scope-Ausweitung bleibt STOP verpflichtend.

#### R-WRAP Wrapper-Policy und Guards
- Mehrschritt-/Artefaktbefehle über Python-Wrapper (`.venv` bevorzugt, Fallback `python`).
- Inline `pwsh -Command` nur echte Einzeiler.
- Ausnahme: Markdownlint ausschließlich via `npx --yes markdownlint-cli2 ...`.
- Vor Ausführung Guards prüfen: Pfad, Kontextquellen, STOP-Status.

#### R-CTX Kontextquellen (Mindestset)
- `.github/copilot-instructions.md`
- betroffene Arbeitsdateien
- bei Doku-/Planungsthemen zusätzlich `todo.root.md`, `DONELOG.md`, `WORKSPACE_STATUS.md`

#### R-LOG Logging- und Receipt-Pflicht
- Nach jeder Dateimutation oder Skript-/Testausführung genau ein Postflight-Receipt am Ende der Antwort.
- Kein Zwischen-Receipt für Teilaktionen.

#### R-DONELOG Modul-DONELOG-Pflicht
- Bei jeder Dateimutation (Code, Doku, Config, Workflow, Skript) ist im selben Änderungslauf ein Eintrag im passenden Modul-DONELOG verpflichtend.
- Zuordnung: bevorzugt Modul-DONELOG (z. B. `novapolis-dev/docs/donelog.md` für Dev/RP-Doku, `novapolis_agent/docs/DONELOG.txt` für Agent-Modul); falls kein Modul-DONELOG existiert, in `DONELOG.md` auf Root-Ebene dokumentieren.
- Kein Interpretationsspielraum über „Relevanz“: Mutation erkannt => DONELOG-Eintrag verpflichtend.

#### R-SEC Sicherheitsprinzip
- Minimalinvasive Diffs.
- Keine destruktiven Änderungen ohne vorgeschaltete WhatIf-/Prüfphase.
- Keine Secrets/PII in Logs/Receipts.
- In langlebigen SSOT-/Policy-/README-Dokumenten keine hostgebundenen absoluten Pfade (`F:/`, `C:/`); stattdessen repo-relative Pfade oder `${workspaceFolder}` nutzen.
- Ausnahme: reine Audit-/Forensik-/Artefaktprotokolle (z. B. Postflight-Logs, generierte Reports, Archiv-Metadaten) dürfen absolute Pfade enthalten, wenn dies für Nachvollziehbarkeit notwendig ist.

#### R-PATH Pfadportabilitaet in aktiven Dokus
- In aktiven SSOT-/Policy-/README-Dokumenten sind hostgebundene absolute Pfade untersagt.
- Erlaubt sind repo-relative Pfade oder `${workspaceFolder}`.
- Ausnahme nur fuer reine Audit-/Forensik-/Artefaktprotokolle.

#### R-LINT Markdownlint-Gate
- Markdownlint verpflichtend: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'`.

#### R-FM Frontmatter-Gate
- Frontmatter-Validator verpflichtend: `scripts/check_frontmatter.py`.
- Ausnahme GOV-EX-FM-001: Diese Datei bleibt ohne YAML-Frontmatter.
- Ausnahme GOV-EX-INS-001: `.github/instructions/*.instructions.md` nutzen nur instruction-spezifische Frontmatter-Felder (`description`, `name`, `applyTo`).

#### R-SNAP Snapshot-Gates (Write-Lock und Freshness)
- Vor mutationalen Läufen Write-Lock frisch setzen: `& .\.venv\Scripts\python.exe scripts/snapshot_write_lock.py`.
- Für alle betroffenen Markdown-Dateien muss `stand` auf den frischen Lock-Zeitwert (oder innerhalb des zulässigen Fensters) synchronisiert sein.
- Praktisch bindend ist dabei das aktuelle Gate-Verhalten: `stand` muss innerhalb von `±5 min` zur aktuellen Zeit liegen; der Lock selbst muss ebenfalls frisch sein und `stand` im Commit-Pfad eng folgen (derzeit `<= 2 min` Abstand im Gate).
- Reihenfolge verpflichtend: Snapshot-Lock -> `stand`-Sync -> markdownlint (betroffene Dateien) -> Frontmatter-Validator (betroffene Dateien) -> Commit/Push.
- Operativer Hook-Pfad: Im Pre-Commit-Hook laeuft die Snapshot-Pruefung erst nach markdownlint, Frontmatter-Validator und eventuellen RP-Hard-Gates, damit spaete Abbrueche oder Auto-Fixes keinen unnoetigen Freshness-Verbrauch ausloesen.
- Wenn ein Hook- oder Lint-Fix den Commit abbricht oder gestagte Markdown-Dateien veraendert, beginnt die Reihenfolge erneut bei Snapshot-Lock -> `stand`-Sync; ein Retry ohne frischen Lock gilt nicht als sauberer Standardpfad.
- Wenn Snapshot-Gate blockiert, kein Bypass als Standardpfad; zuerst Lock/`stand` korrekt nachziehen.

#### R-NAME Namensgebungskonvention
- Regel-IDs im Format `R-<BEREICH>-<THEMA>` (Großbuchstaben, Bindestrich-separiert).
- Instruction-Dateien unter `.github/instructions/` enden auf `.instructions.md`.
- Bezeichner in Frontmatter-Feldern (`name`, `description`) bleiben stabil und eindeutig.

#### R-WS Kanonisierung und Whitespace-Norm
- Markdown-Dateien in UTF-8 ohne BOM, Unix-EOL, genau eine abschließende Newline.
- Kein Trailing-Whitespace; Leerzeilen konsistent und minimal.

#### R-FMT Markdown-Formatnorm (syntaktisch)
- Überschriften-Hierarchie strikt einhalten.
- Delimiter `---` nicht unbeabsichtigt verändern.

#### R-QUAR Quarantaene- und Backup-Ort
- Arbeitskopien/Backups nicht lose im Repo-Root ablegen.
- Quarantänepfad für temporäre Kopien: `novapolis-dev/archive/quarantine/`.
- Backups nur mit nachvollziehbarer Quelle und alternativesicherer Zielablage erstellen.

#### R-IDX Mini-Gate fuer Headings-Index
- Bei strukturrelevanten Änderungen an Kern- oder Scoped-Instructions ist `.github/copilot-instructions-headings.md` im selben Änderungslauf zu aktualisieren.

#### R-TIME Zeitkonvention
- Zeitquelle immer frisch via `Get-Date`.
- Format: `YYYY-MM-DD HH:mm` (lokal).

### Kommunikationsmodus
- Standard-Antwortsprache: Deutsch.
- Prägnant, skimmbar, minimalinvasiv.

Regelmatrix (Kern)
------------------
### Feldset
- `id, priority, scope, trigger, action, validation, exceptions, notes`

### Matrix
Ableitungsstatus: Diese Matrix fasst die bindenden `Regel-ID-Landepunkte (Kern)` kompakt zusammen und ersetzt keine Normtexte.

- `id: R-STOP, priority: 1, scope: repo, trigger: hard_or_soft_conflict, action: stop_and_request_confirmation, validation: no_mutation_before_confirm, exceptions: none, notes: hard_has_precedence`
- `id: R-WRAP, priority: 1, scope: repo, trigger: multistep_or_artifacts, action: use_python_wrapper, validation: wrapper_policy=erfüllt, exceptions: markdownlint_npx_yes, notes: inline_pwsh_only_oneliner`
- `id: R-CTX, priority: 1, scope: repo, trigger: before_action, action: load_minimum_context_sources, validation: sources_listed_in_receipt, exceptions: trivial_readonly_smalltalk, notes: include_affected_files`
- `id: R-LOG, priority: 1, scope: repo, trigger: file_mutation_or_script_run, action: emit_single_postflight_receipt, validation: receipt_has_5_lines, exceptions: readonly_general_mode, notes: receipt_is_last_block`
- `id: R-DONELOG, priority: 1, scope: repo, trigger: any_file_mutation, action: append_module_donelog_entry_same_change_set, validation: donelog_entry_present_and_scoped, exceptions: none, notes: if_no_module_log_then_root_donelog`
- `id: R-SEC, priority: 1, scope: repo, trigger: risky_or_destructive_change, action: apply_minimal_diff_and_precheck, validation: whatif_or_equivalent_done, exceptions: none, notes: no_secret_output`
- `id: R-PATH, priority: 1, scope: docs, trigger: markdown_change_in_active_docs, action: enforce_portable_paths, validation: no_host_bound_absolute_paths_in_active_docs, exceptions: audit_forensics_artifacts_allowed, notes: prefer_repo_relative_or_workspaceFolder`
- `id: R-LINT, priority: 1, scope: docs, trigger: markdown_change, action: run_markdownlint_cli2, validation: exitcode_0, exceptions: none, notes: use_npx_yes_only`
- `id: R-FM, priority: 1, scope: docs, trigger: markdown_change, action: run_frontmatter_validator, validation: required_keys_present, exceptions: GOV_EX_FM_001, notes: stand_update_checks_required`
- `id: R-SNAP, priority: 1, scope: docs_and_commits, trigger: markdown_or_commit_intent, action: refresh_snapshot_lock_and_sync_stand, validation: snapshot_gate_pass, exceptions: explicit_stop_approved_override, notes: commit_hook_runs_snapshot_after_doc_and_rp_gates`
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
- `.github/instructions/mind-cluster.instructions.md`

Postflight-Schema (5 Zeilen)
----------------------------
### Format
- Zeile 1 (`Meta`): `Modus, Modell, Arbeitsverzeichnis, RepoRoot, PSScriptRoot, PSVersion, Aufruf, SHA256, STOP-Gate, Wrapper-Policy, Wrapper-Guards, Quellen, Aktion`
- Zeile 2 (`Prüfung`): `markdownlint, ExitcodeLint, behobenLint, Frontmatter-Validator, ExitcodeFM, behobenFM, Cleanup-WhatIf-Exit, behobenWhatIf, Cleanup-Real-Exit, behobenReal, WorkspaceScanRoot, WorkspaceScanRecurse`
- Zeile 3 (`Regeln`): `IDs, Details`
- Zeile 4 (`Todos`): `offen, BeispielFix, ReRun, Fällig`
- Zeile 5 (`Ende`): `Timestamp`

### Semantik `Todos` (verbindlich)
- `Todos.offen` im Postflight-Receipt bezeichnet den offenen Stand aus `novapolis-dev/docs/todo.index.md` und wird als Summe der dort gefuehrten Modul-Open-Counts (`Dev`, `RP`, `Agent`, `Sim`) berichtet.
- `todo.root.md` bleibt dabei bewusst ausserhalb dieser Zahl, weil der Index den Root-Backlog nicht in die Modul-Open-Counts einrechnet.
- Wenn der TODO-Index fuer den aktuellen Lauf nicht belastbar verfuegbar ist, muss der Receipt das explizit benennen statt einen Agent-Laufstand als Ersatz zu verwenden.

Kompakter Meta-Block (rein lesend)
----------------------------------
- `Meta: Modus=General, Modell=<...>, Aktion=<...>, Timestamp=<yyyy-MM-dd HH:mm>[, Arbeitsverzeichnis=<...>]`
