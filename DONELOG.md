---
stand: 2025-11-09 22:11
update: Receipts ergänzt (Frontmatter-Validator PASS; Tests/Coverage PASS 81.66%)
checks: markdownlint DONELOG PASS
---

DONELOG-Uebersicht (Novapolis Suite)
====================================

Schneller Blick auf alle dokumentierten Abschluesse. Die Projekt-Logbuecher bleiben weiterhin die fuehrenden Quellen; diese Datei spiegelt ihren Inhalt fuer eine zentrale Sicht wider.

Kurzueberblick
--------------

- 2025-11-09 22:11: Frontmatter-Validator PASS (scoped); Fix an `todo.root.md` (fehlender `---` Delimiter ergänzt); Policy R-FM/R-LINT bestätigt.
 - 2025-11-10 00:01: Tests/Coverage: 298 passed, 1 skipped; Total coverage 81.66%; Artifacts: `outputs/test-artifacts/coverage.xml`, `outputs/test-artifacts/junit.xml`.
- 2025-11-09 22:11: Tests/Coverage PASS – 298 passed, 1 skipped; Total coverage 81.66% (coverage.py line-rate 84.07%, branch-rate 74.25%); Artefakt: `outputs/test-artifacts/coverage.xml`.
- 2025-11-09 17:51: Testabdeckung ≥80% erreicht (81.66% via Wrapper); Chat-API interne Zweige getestet (Stream/Non-Stream); Governance-Anweisung aktualisiert; DONELOGs ergänzt.
- 2025-11-08 01:04: Cleanup-Postflight (WhatIf/Real, Root-Scan, Lint, Frontmatter) – PASS/FAIL Details.
- 2025-11-07 11:58: Wrapper-Policy in `.github/copilot-instructions.md` vereinheitlicht (Skript-Wrapper zwingend via `pwsh -NoProfile -File`); `single-root-todo.md` Hinweis angepasst (Wrapper-Pflicht + Etappe 3b); aktueller Coverage-Lauf (~66% < 80%) bleibt unter Fail-Under – Verbesserung eingeplant.
- 2025-11-07 10:53: Moduswechsel dokumentiert (General aktiv); Coverage-Befehl in Copilot-Anweisungen mit Dateizähler + PASS/FAIL-Ausgabe ergänzt; keine Codeänderungen.
- 2025-11-07 09:59: Doku-Sweep – markdownlint-Aufruf (npx, `'**/*.md'`) repo-weit erneut geprüft; 132 Dateien gelinted, 0 Fehler. Keine Codeänderungen.
- 2025-11-07 08:59: Copilot-Anweisung ergänzt – Schnell-Index und pwsh-Cheat-Sheet hinzugefügt; markdownlint repo-weit PASS. Keine Codeänderungen.
- 2025-11-07 08:46: Copilot-Anweisung überarbeitet – Task-Beschreibungen in `.github/copilot-instructions.md` auf konkrete pwsh-Kommandos umgestellt und Widerspruch zu Task-Ausführung entfernt. Keine Tests.
- 2025-11-07 08:34: Legacy-Kompatibilitätsschicht `utils/__init__.py` ergänzt, re-exportiert Module aus `novapolis_agent.utils` für bestehende Importpfade (`from utils.*`). Smoke-Test `tests/test_api_health.py` PASS. Voller Pytest-Coverage-Lauf via pwsh fehlgeschlagen (Coverage 65.64 % < 80 %).
- 2025-11-07 08:24: Copilot-Anweisung präzisiert: Copilot/GPT dürfen keine VS Code Tasks ausführen; alle Tests/Lint/Typechecks sind via PowerShell (pwsh, -NoProfile) direkt auszuführen. Beispiel-Pattern in `.github/copilot-instructions.md` ergänzt. Reine Dokuänderung.
- 2025-11-07 06:27: Behaviour-SSOT konsolidiert: `.github/copilot-instructions.md` ist jetzt alleinige Quelle. Alte Dokumente `novapolis_agent/docs/AGENT_BEHAVIOR.md` und `novapolis-dev/docs/copilot-behavior.md` gelöscht (pwsh), alle zentralen Verweise gedreht (Root/Dev/Agent READMEs, WORKSPACE_STATUS, Agent WORKSPACE_INDEX, training.md, Dev-Index, .vscode/settings.json, RP todo); Kontext‑Notes `.ref` aktualisiert. Keine Codeänderungen.
- 2025-11-07 04:56: Archiv-TODOs (`novapolis-dev/archive/todo.*.archive.md`) auf Setext gebracht, Timestamps/Checks erneuert; `.github/ISSUE_TEMPLATE/feature_request.md` vereinheitlicht; repo-weites `markdownlint-cli2` PASS (132 Dateien).
- 2025-11-07 03:12: `todo.root.md` auf Setext (H1/H2) umgestellt, YAML-Frontmatter korrigiert; Einzel-Lint PASS.
- 2025-11-07 02:29: Tree‑Snapshots aktualisiert; Staging‑Reports (Setext + YAML‑Frontmatter) vereinheitlicht und gelinted (scoped PASS); Status ergänzt.
- 2025-11-07 02:19: DONELOGs/Status-Docs synchronisiert (`todo.root.md`, `WORKSPACE_STATUS.md`, `single-root-todo.md`); Repo-weites markdownlint-Ergebnis (MD003‑Backlog) dokumentiert; VS Code Lint‑Task (Quoting `'**/*.md'`) angeglichen.
- 2025-11-07 01:39: TODO/WORKSPACE_STATUS aktualisiert (Single-Repo-Governance-Reminder, Aufgaben für Lint-Overrides, Staging-Report-Migration, Metadata-Konsolidierung, Archiv-Ablage) – reine Doku-Anpassung.
- 2025-11-07 01:27: Workspace-Konfliktanalyse abgeschlossen (Markdownlint-Overrides in `novapolis-rp/database-curated/staging/**`, Staging-Reports ohne Frontmatter, doppelte Metadata-Skripte `.js/.py`, Alt-Notiz `novapolis_agent/analysis_chat_routers.md`). Ergebnisse in TODO/Status erfasst.
- 2025-11-06 15:58: MD003 Setext + YAML-Frontmatter in `novapolis_agent/cleanup_recommendations.md`, `Backups/novapolis-rp-development-archived-20251105/development/README.md`, `novapolis-dev/logs/betriebsmodi-20251103-0341.tmp.md`, `novapolis-rp/.github/ISSUE_TEMPLATE/bug_report.md`, `novapolis_agent/eval/config/context.local.sample.md`; targeted markdownlint PASS (5 Dateien); Logs aktualisiert.
- 2025-11-06 15:22: MD003-Setext-Korrekturen in `novapolis-rp/coding/tools/chat-exporter/README.md`, `novapolis-rp/coding/tools/metadata/README.md`, `novapolis-rp/coding/devcontainer/README.md`; targeted markdownlint PASS (3 Dateien).
- 2025-11-06 15:22: YAML-Frontmatter (stand/update/checks) in denselben 3 Dateien ergänzt; frontmatter-Validator PASS (targeted).
- 2025-11-06 15:30: YAML-Frontmatter ergänzt und MD003-Konformität bestätigt (Setext bereits vorhanden bzw. H1 ergänzt) in `packages/README.md`, `novapolis-sim/README.md`, `novapolis-rp/README.md`, `novapolis-dev/README.md`, `novapolis-rp/coding/tools/validators/README.md`; targeted markdownlint + frontmatter-Validator PASS (5 Dateien).
- 2025-11-06 15:35: MD003 Setext + YAML‑Updates in `novapolis-dev/logs/README.md`, `novapolis-dev/integrations/mcp-openai-eval/README.md`, `novapolis-rp/database-curated/staging/README.md`, `novapolis-rp/database-rp/06-scenes/README.md`, `.tmp-results/README.md`; targeted markdownlint + frontmatter-Validator PASS (5 Dateien).
- 2025-11-06 15:44: YAML-Frontmatter ergänzt und MD003 (Setext) vereinheitlicht in `novapolis-rp/database-curated/README.md`, `novapolis-rp/database-raw/99-exports/README.md`, `.tmp-datasets/README.md`, `novapolis_agent/eval/config/context.notes/README.md`; targeted markdownlint + frontmatter-Validator PASS (4 Dateien).
- 2025-11-06 15:51: MD003 Setext H1/H2 und YAML-Frontmatter (falls fehlend) in `Backups/README.md`, `Backups/AUDIT.md`, `novapolis-dev/logs/log-template.md`, `novapolis_agent/data/logs/README.md`, `eval/config/context.local.md`; targeted markdownlint PASS (5 Dateien).
- 2025-11-06 04:50: MD003-Setext-Korrekturen in `packages/README.md`, `novapolis_agent/scripts/README.md`, `novapolis_agent/eval/README.md`, `novapolis_agent/eval/DEPRECATIONS.md`; targeted markdownlint PASS (4 Dateien).
- 2025-11-06 04:52: MD003-Setext-Korrektur in `novapolis-rp/database-curated/README.md`; targeted markdownlint PASS.
- 2025-11-06 04:40: Demo-Test entfernt (`tests/test_intentional_failure.py`) und `pytest -q` manuell via pwsh ausgeführt – Suite PASS.
- 2025-11-06 04:15: Frontmatter-Validator mit Demo-Datei geübt; `check_frontmatter.py` PASS nach Korrektur; absichtlicher pytest-Fail dokumentiert.
- 2025-11-06 03:34: Workspace-Tree-Snapshots (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`) via Tasks aktualisiert; Status-/Donelog-Docs nachgezogen.
- 2025-11-06 03:07: `novapolis-dev/docs/prompts/chat-restart.md` entfernt; Index-Verweis bereinigt; Markdownlint (index/donelog) PASS.
- 2025-11-06 03:18: `novapolis-rp/coding/tools/validators/run_lint_markdown.ps1` entfernt; README & Copilot-Anweisungen aktualisiert; Markdownlint (validators/README.md) PASS.
- 2025-11-06 02:57: RP/Sim-Dokumente (`todo.sim.md`, Specs-Batch, Betriebsmodi-Notizen) auf YAML-Frontmatter gebracht und einzeln gelinted – alle Läufe PASS.
- 2025-11-06 02:52: `novapolis-dev/docs/todo.rp.md` auf YAML-Frontmatter umgestellt und einzeln gelinted (`markdownlint todo.rp.md`) – PASS.
- 2025-11-06 02:00: H1/H2 in `README.md`, `WORKSPACE_STATUS.md` auf Setext-Stil umgestellt; Scope-Lint (`markdownlint README.md WORKSPACE_STATUS.md`) PASS; globaler Repo-Lauf weiter MD003-Backlog (Archive/weitere Readmes).
- 2025-11-06 02:42: `novapolis_agent/docs/training.md` sowie `docs/reports/overnight-20251022.md` gelinted; Frontmatter auf aktuellen Stand gebracht.
- 2025-11-06 02:35: Agent-Dokumente (`customization.md`, `ARCHIVE_PLAN.md`, `CONTEXT_ARCH.md`, `REPORTS.md`) gelinted; Frontmatter aktualisiert; Einzelläufe PASS.
- 2025-11-06 02:30: `novapolis_agent/docs/DONELOG.txt` mit YAML-Frontmatter versehen, Pfadangaben in Backticks und H1 auf Setext-Stil gebracht; Lint-Einzellauf (`markdownlint DONELOG.txt`) PASS.
- 2025-11-06 02:23: README (Agent) komplett auf Setext-Stil gebracht, YAML-Frontmatter ergänzt; `docs/AGENT_BEHAVIOR.md` auf YAML-Frontmatter umgestellt. Lint-Einzelläufe (`markdownlint README.md`, `markdownlint AGENT_BEHAVIOR.md`) PASS.
- 2025-11-06 01:54: Testsuite manuell (pytest -q, pyright, mypy) PASS; markdownlint-cli2 FAIL (MD003 – Setext-Konsistenz über Archiv-/README-Bestand prüfen).

- 2025-11-01 23:45: Workspace-Bereinigung – alte `.code-workspace` Dateien entfernt; markdownlint-cli2 PASS (Root-Lauf, keine Fehler). `WORKSPACE_STATUS.md` aktualisiert.
- 2025-11-02 19:11: YAML-Frontmatter auf allen Root-Dokumenten finalisiert; markdownlint-cli2 PASS (Repo-Lauf).
- 2025-11-02 22:31: Shell-Hooks/Tasks auf PowerShell 7 (`pwsh`) umgestellt; `.gitignore` ignoriert lokale Godot-Editor-Binaries (novapolis-sim).
- **novapolis_agent/docs/DONELOG.txt** protokolliert jede nicht-triviale Codeaenderung im Agent-Backend (Pflicht fuer CI).
- **novapolis-dev/docs/donelog.md** haelt migrations-, daten- und policy-bezogene Arbeiten fest.
- 2025-11-01: Markdownlint zentralisiert – Root-Task vereinheitlicht, Agent-Wrapper entfernt, `run_lint_markdown.ps1` als Hinweisstub belassen.
- 2025-11-02: TODO-Übersichten konsolidiert – Root-`TODO.md` auf Link (driftfrei) mit Zeitstempel umgestellt; RP-Mirror `novapolis-rp/Main/novapolis-dev/docs/todo.md` durch Stub ersetzt; Legacy-Stub `novapolis-rp/development/docs/todo.md` entfernt.
- 2025-11-02: Memory-Bundle und Root-Doku auf Evakuierungsstatus Marei/E3/C6 synchronisiert; offene Aufgabenliste angepasst.
- 2025-11-02: Jonas-Merek-Canvas auf Version 1.0 konsolidiert (Werte, Rollen, Sicherheitsprotokolle; Schuldflag normalisiert) und dev TODO/DONELOG nachgezogen.
- 2025-11-02: Kora-Malenkov-Canvas auf Version 1.0 gehoben (Logistikscope, Echo-Protokolle, Händlergilde/Novapolis Zugehörigkeit) und Dokumentation synchronisiert.
- 2025-11-02: Marven-Kael-Canvas angelegt (Konvoiführung, Handelsprotokolle, Händlergilde-Scope) und Quellen/Tasks aktualisiert.
- 2025-11-02: Behavior-Signaturen für Echo/Lumen/Liora/Lyra/Senn/Varek kuratiert; Validator `behavior_matrix_check.py` um Psymatrix-Diff und Dokumentation ergänzt.
 - 2025-11-02: Copilot-Modelle/STOP‑Gate dokumentiert: `.github/copilot-instructions.md` um Moduswechsel/Reminder/STOP‑Gate ergänzt; Spiegelupdate in `novapolis-dev/docs/copilot-behavior.md`; `WORKSPACE_STATUS.md` führt aktuellen Modus/STOP‑Gate.
 - 2025-11-02: RP-Daten konsolidiert – kuratierte Reports, Memory-Bundle und Charakter‑Canvases (Reflex/Ronja/Kora/Jonas) aktualisiert; `[FACT]`/`[FACT?]`-Status vereinheitlicht.
- 2025-11-01: AI Behavior Matrix (Version 1.0) – RAW `ai_behavior_index_v2` promotet, Cluster/Intensität/Modifikatoren, vollst. Anchor-Register (02-characters) + Psymatrix dokumentiert.
- 2025-11-01: Ronja-Canvas (Version 1.0) – RAW char_ronja_v2 integriert, Drift „Vallin“ dokumentiert, TODO-Boards aktualisiert.
- 2025-11-01: Echo-Canvas (Front-Matter/JSON) formal angeglichen, keine inhaltlichen Änderungen.
- 2025-11-01: Canvas-Rettung Sprint 1 – Liora Navesh abgeschlossen (Canvas + JSON, Quellen/TODO/Personenindex aktualisiert).
- 2025-11-01: Root-Dokumentation (`README.md`, `TODO.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`) aktualisiert; Tree-Snapshot-Refresh als Folgeaufgabe markiert.
 - 2025-11-01: YAML-Frontmatter vereinheitlicht (Root `WORKSPACE_STATUS.md`, `novapolis-dev/docs/{index.md,todo.md,copilot-behavior.md}`, RP‑Admin: `C6-Logistik-Policy.md`, `memory-bundle.md`, `Missionslog.md`, `person_index_np.md`, `system-prompt.md`). `markdownlint-cli2` Lauf: FAIL (Exit 1). Haupttreffer in `novapolis_agent/eval/results/summaries/*`, `outputs/lora-*/README.md`, `novapolis-rp/database-curated/staging/*`; neu migrierte Dateien ohne Befund.

Volltexte
---------

Postflight-Bereinigung (2025-11-08T01:04:00+01:00)

Arbeitsverzeichnis: F:\VS Code Workspace\Main (VS Code Workspace-Root geöffnet, kein "No folder opened").

Receipt:
- RepoRoot laut Skript: F:\VS Code Workspace\Main
- PSScriptRoot: F:\VS Code Workspace\Main\scripts
- WhatIf-Lauf (pwsh -NoProfile -File F:/VS Code Workspace/Main/scripts/cleanup_workspace_files.ps1 -VerboseLog -WhatIf): Ziel F:\VS Code Workspace\Main\novapolis-suite.code-workspace; Konsole meldete "Would delete ..."; $?=True; LASTEXITCODE=0.
- Real-Lauf (pwsh -NoProfile -File F:/VS Code Workspace/Main/scripts/cleanup_workspace_files.ps1 -VerboseLog): Ziel F:\VS Code Workspace\Main\novapolis-suite.code-workspace; Konsole meldete "Deleted: ..."; $?=True; LASTEXITCODE=0.
- SHA256 cleanup_workspace_files.ps1: 7E94DACE615BBF7C08E3A355C34BD5F01032639831B8B62A2F2671A85C9E4453.
- Suchstrategie: Root-only by design; zusätzlicher -Recurse-Check dient ausschließlich der Verifikation.

Scans:
- Get-ChildItem -Path "F:/VS Code Workspace/Main" -Filter "*.code-workspace": 0
- Get-ChildItem -Path "F:/VS Code Workspace/Main" -Filter "*.code-workspace" -Recurse: 0

Lint/Validator:
- npx --yes markdownlint-cli2 DONELOG.md: PASS (Exitcode 0)
- scripts/run_frontmatter_validator.ps1: FAIL (Exitcode 1)

Frontmatter fehlend: 55 Dateien in novapolis-rp/database-rp (weitere Abweichungen siehe Validator-Log)

Beispiel: novapolis-rp/database-rp/02-characters/Echo.md fehlt keys: stand, update, checks

Validator rerun geplant nach Fix

Bestätigungen:
- cleanup_workspace_files.ps1 ausschließlich via pwsh -NoProfile -File ausgeführt (keine -Command-Varianten).
- single-root-todo.md blieb unverändert und diente nur als Preflight-Kontext.
- Neuer Helfer scripts/diagnostics.ps1 liefert Root/Recursive-Counts sowie Hash für künftige Receipts.

PowerShell 7 Standard & Gitignore (2025-11-02T22:31:00+01:00)

- `.vscode/settings.json` setzt Terminal-Profile/Automation jetzt auf PowerShell 7 (`pwsh`), Tasks (`.vscode/tasks.json`) nutzen `pwsh -NoProfile` statt Windows PowerShell.
- Git-Hooks und Snapshot-Skripte (`githooks/pre-commit`, `scripts/snapshot_*`, Diagnosetools) erkennen `pwsh` bevorzugt, behalten Fallback auf `powershell.exe`.
- CI-Workflows/Validatoren (`.github/workflows/validate-rp.yml`, `novapolis-rp/.github/workflows/validate.yml`) führen PS1-Wrapper mit `pwsh` aus; Dokumentation (`.github/copilot-instructions.md`, `single-root-todo.md`, `WORKSPACE_STATUS.md`) auf neuen Standard synchronisiert.
- Root-`.gitignore` ergänzt Ausnahmeregel für lokale Godot-Editor-Binaries (`novapolis-sim/Godot_v*.exe`).

Memory-Bundle Refresh (2025-11-02T10:15:00+01:00)

- `novapolis-rp/database-rp/00-admin/memory-bundle.md` vollständig neu strukturiert: Evakuierung E3→C6, Marei-Rolle, Tunnelstatus und Projektlisten aktualisiert; Charaktersektionen gestrafft.
- Root-Dokumentation (`README.md`, `TODO.md`, `WORKSPACE_STATUS.md`, `DONELOG.md`) auf Stand 2025-11-02 gehoben; TODO-Checkboxen für Memory-Bundle-Aufgaben abgeschlossen.
- Folgeaufgabe: Tree-Snapshots (`workspace_tree*.txt`) beim nächsten Struktur-Update regenerieren.

Markdownlint zentralisiert (2025-11-01T15:30:00+01:00)

- VS Code Tasks für Markdownlint entfernt; Lint läuft zentral und wird lokal direkt im bestehenden Terminal via npx ausgeführt.
- `novapolis_agent/.vscode/tasks.json` bereinigt (Markdownlint-Wrapper-Tasks entfernt); Nutzung lokal ausschließlich per direktem `npx`.
- `.github/workflows/markdownlint.yml` führt den Windows-Lauf nur noch via `npx`; der Aufruf von `run_lint_markdown.ps1` entfällt.
- `run_lint_markdown.ps1` liefert nur noch einen Hinweis (Exit 1); Dokumentation in `novapolis-dev/docs/index.md`, `novapolis-dev/docs/donelog.md`, `novapolis-rp/coding/tools/validators/README.md` aktualisiert.

Jonas Merek Canvas (2025-11-02T13:55:00+01:00)

- Charakter-Canvas `novapolis-rp/database-rp/02-characters/Jonas-Merek.md` auf Version 1.0 aktualisiert: Werte/Skills aus RAW `char_jonas_v2` übernommen, Rollen (Werkstatt, Logistik, Terminal) präzisiert und Sicherheit/Proximity-Protokolle ergänzt.
- Korrupten Makel („Schuld am Tod der Schwester“) gemäß FACT `[JONAS-SIS]` bereinigt – Schwesterstatus als „vermisst/unklar“ festgehalten, Schuldgefühle als subjektive Notiz geführt.
- JSON-Sidecar & Dependencies (`missionslog`, `ai_behavior_index_v2`) synchronisiert, `char-block-nord-sources.md` sowie dev TODO/DONELOG aktualisiert.

Kora Malenkov Canvas (2025-11-02T14:20:00+01:00)

- Charakter-Canvas `novapolis-rp/database-rp/02-characters/Kora-Malenkov.md` auf Version 1.0 angehoben: Werte/Skills und Verhaltenssignatur aus RAW `char_kora_malenkov_v2` übernommen, Logistik-/Sicherheitsrollen für C6 ausgearbeitet und Echo-Protokolle dokumentiert.
- FACTs `[CARAVAN-LEADERSHIP]`, `[PROXIMITY]`, `[FR-KNOWLEDGE]` integriert: Abgrenzung zu Marven/Arlen, Händlergilde + Novapolis Zugehörigkeit, Freigabeprozesse (Missionslog/Logistik) festgeschrieben.
- JSON-Sidecar erweitert (Tags `logistik`/`haendlerbund`, Dependencies `logistik`, `missionslog`, `ai_behavior_index_v2`, `caravan_moves`), `char-block-nord-sources.md`, dev TODO/DONELOG aktualisiert und Personenindex-Notiz ergänzt.

Marven Kael Canvas (2025-11-02T14:45:00+01:00)

- Neues Charakter-Canvas `novapolis-rp/database-rp/02-characters/Marven-Kael.md` angelegt: Werte/Skills und Verhaltenssignatur aus RAW `char_marven_v2` übernommen, Konvoi-/Handelsrolle inklusive Sicherheits- und Verhandlungsprotokollen ausgearbeitet.
- FACTs `[CARAVAN-LEADERSHIP]` und `[FR-KNOWLEDGE]` berücksichtigt – klare Abgrenzung zur internen Logistik (Kora) und zu Arlens Vermittlungsrolle, Schutz der Händlergilde-Koordinaten, strukturierte Verhandlungsabläufe dokumentiert.
- JSON-Sidecar ergänzt (Tags `karawane`/`haendlerbund`, Dependencies `caravan_moves`, `ai_behavior_index_v2`, `missionslog`, `logistik`, `c6`), Quellenreport `char-block-nord-sources.md`, dev TODO/DONELOG und Personenindex aktualisiert.

Arlen Dross Canvas (2025-11-02T15:05:00+01:00)

Pahl Canvas (2025-11-02T15:25:00+01:00)

<details>
Pahl Herkunfts-Abgleich (2025-11-02T15:50:00+01:00)

- FACT `[PAHL-RESCUE]` in `database-curated/staging/reports/resolved.md` dokumentiert: C6-Reaktorunfall, Rettung durch Ronja/Reflex, Transfer nach D5 unter Jonas' Obhut.
- Canvas/JSON (`Pahl.{md,json}`) aktualisiert (Herkunft, Dependency `c6`, Quellenblock) sowie Memory-Bundle, Personenindex und `char-block-nord-sources.md` synchronisiert.
- RAW-Flag bleibt als Vorsichtshinweis bestehen, Kanon orientiert sich jetzt an `[PAHL-RESCUE]`.

Reflex Canvas (2025-11-02T16:05:00+01:00)

- Charakter-Canvas `novapolis-rp/database-rp/02-characters/Reflex.{md,json}` auf Version 1.0 aktualisiert: Symbiose-Stufe I (Frequenzband 7.3–8.0 Hz), Detachment-/Stop-Regeln, Instanzleitung und Signalsätze dokumentiert.
- Quellenreport `char-block-nord-sources.md`, Memory-Bundle und TODO/DONELOG-Einträge synchronisiert; `[REFLEX-*]`-FACTs als Referenz verankert.
- JSON-Sidecar um neue Tags/Dependencies (Ronja, Lumen, Echo, Missionslog, Logistik) erweitert; RAW-Entity `ent_d5_reflex_v1` als technische Quelle hinterlegt.

Modell-Modus & STOP‑Gate Doku (2025-11-02T16:55:00+01:00)

- `.github/copilot-instructions.md`: Abschnitt „Modell‑Profile & Moduswechsel (GPT‑5 ↔ GPT‑5 Codex)“ und „STOP‑Gate vor Code‑Aktionen“ hinzugefügt; Reminder‑Policy ohne 1×/Session‑Limit (Opt‑out: „Bitte nicht erinnern“).
- `novapolis-dev/docs/copilot-behavior.md`: Spiegelabschnitt mit denselben Regeln ergänzt.
- `WORKSPACE_STATUS.md`: Abschnitt „Aktueller Arbeitsmodus“ (Modus: General, STOP‑Gate: an, Erinnerungen: aktiv) aufgenommen.

Validator Docker-Pfadfix (2025-11-02T16:30:00+01:00)

- Validator-Skripte (`validate-*.js`, `check-*.js`) auf relative Pfadermittlung via `import.meta.url` umgestellt, damit Docker-Läufe die Repo-Wurzel korrekt finden.
- `validate-all.js` Exitcode-Handling überarbeitet (Status-Logging, Fehlerpropagation), Statusfile-Schreibpfad repariert.
- `run_validate_all.ps1` geprüft – Lauf in node:22-alpine erfolgreich, temporäre `node_modules`/`.last-run` anschließend bereinigt.

<summary>novapolis_agent/docs/DONELOG.txt</summary>

```text
# DONELOG – Abgeschlossene Arbeiten

Hinweis:
- Bitte jede abgeschlossene, nicht-triviale Änderung hier kurz dokumentieren.
- Format: YYYY-MM-DD HH:MM | Author | Kurzbeschreibung
- Keine sensiblen Inhalte eintragen.

Beispiel:
2025-10-15 12:34 | username | Eval-Pipeline stabilisiert; map_reduce_summary_llm typisiert; Doku aktualisiert.
2025-10-15 14:10 | Copilot | CI erweitert: DONELOG-Prüfung auch bei Push auf main; VS Code Task zum schnellen Eintrag hinzugefügt.
2025-10-15 14:22 | Copilot | Optionale Absicherung: lokaler pre-commit Hook (.githooks) + VS Code Tasks zum Installieren/Prüfen; Tasks portabilisiert.
2025-10-15 14:27 | Copilot | Neuer System-Prompt: docs/AGENT_PROMPT.md; VS Code Task zum Kopieren in die Zwischenablage.
2025-10-15 16:05 | Copilot | Pyright auf 1.1.406 aktualisiert; 0 Fehler/0 Warnungen; mypy/pytest grün.
2025-10-15 16:12 | Copilot | VS Code Tasks portabilisiert; ProblemMatcher für pyright/mypy hinzugefügt; schema warnings behoben.
2025-10-15 16:18 | Copilot | Markdownlint eingeführt (.markdownlint.json); Lint/Fix Tasks; Pre-commit Hook um Markdownlint mit Auto-Fix erweitert.
2025-10-15 16:26 | Copilot | README/TODO/Customization nach markdownlint (MD031/MD032/MD012/MD009/MD007) bereinigt.
2025-10-15 16:41 | Copilot | VS Code Tasks: Git-Hook-Verify/Run auf PowerShell umgestellt; doppelte Ad-hoc-Tasks entfernt; JSON-Syntaxfehler behoben.
2025-10-15 16:44 | Copilot | Markdownlint: npx-basierte Tasks ergänzt und PowerShell-Fallback-Task hinzugefügt (npx oder globales markdownlint).
2025-10-15 16:58 | Copilot | mypy: `scripts/run_eval.py` auf check_untyped_defs=True gestellt; ungenutzte ignores entfernt; Typen/Casts ergänzt; Tests grün.
2025-10-15 17:06 | Copilot | mypy: `scripts/eval_ui.py` auf check_untyped_defs=True gestellt; unused ignores entfernt; Variable umbenannt; Tests grün.
2025-10-15 17:34 | Copilot | mypy: Enforcement abgeschlossen für curate_dataset_from_latest.py, openai_finetune.py, train_lora.py; unnötige ignores entfernt; kleinere Typanpassungen; pytest grün.
2025-10-15 17:55 | Copilot | Tests: Marker-Gruppierung (unit/api/streaming/eval/scripts) eingeführt; Streaming-Fehlerpfad, dependency_check und Export→Prepare-Pipeline als offline-Tests ergänzt; Tasks für Marker-Läufe.
2025-10-15 17:48 | Copilot | Tests gruppiert: pytest-Marker (unit, api, streaming, eval, scripts) eingeführt; VS Code Tasks für gruppierte Läufe hinzugefügt; Marker auf repräsentative Tests angewendet.
2025-10-15 17:18 | Copilot | mypy-Enforcement bestätigt: `scripts/eval_ui.py` clean; pytest erneut grün; TODO/DONELOG aktualisiert.
2025-10-15 18:05 | Copilot | Rate-Limit/Timeout-Tests ergänzt; Middleware wandelt HTTPException in JSONResponse um und setzt X-Request-ID auch bei Fehlern; Header dokumentiert.
2025-10-15 18:22 | Copilot | Coverage erweitert: Prompt-/Options-Parsing, Context-Notes-Injektion, Settings-Validatoren, LLM-Service Success/Fail, Summary-Kantenfälle; .coveragerc mit Branch-Coverage; VS Code Coverage-Tasks; kombiniertes Fail-Under auf 80 angehoben.
2025-10-15 18:47 | Copilot | ID-Normalisierung vereinheitlicht ("eval-" Präfix) in export_finetune/rerun_failed/eval_ui; Utils: strip_eval_prefix/ensure_eval_prefix; Test für gemischte IDs; Cross-Drive relpath-Fixes in audit_workspace/rerun_failed/map_reduce_summary.
2025-10-15 19:02 | Copilot | Script-Smokes hinzugefügt (audit_workspace, smoke_asgi, fine_tune_pipeline, openai_ft_status, open_latest_summary, map_reduce_summary); OpenAI-Client im Test stubbed; minimale Script-Abdeckung >5% erreicht; Teil-Suites grün.
2025-10-15 19:18 | Copilot | Datensatzkurierung aus Logs: VS Code Task "Curate dataset (latest)" ergänzt; Smoke-Test für `scripts/curate_dataset_from_latest.py` hinzugefügt (Export/Prepare gepatcht, stdout-Report geprüft).
2025-10-16 09:40 | Copilot | Chai-Datensatz vereinfacht (must_include reduziert), Synonyms-Overlay erweitert (freundlich/empathisch/einfühlsam/zuwenden), Beispiel-Test `tests/test_chai_checks.py` hinzugefügt.
2025-10-16 09:41 | Copilot | Export/Kuratierung robuster: `EVAL_FILE_PATTERN` auf `eval-*.json*` erweitert; `export_finetune` nutzt `source_file` aus Results für zuverlässige Zuordnung; Mini-LoRA-Lauf (10 Schritte) auf chai-Pack durchgeführt.
2025-10-16 09:45 | Copilot | Docs aktualisiert: AGENT_PROMPT.md um Pipeline/PowerShell‑Shortcuts/Artefakte erweitert; ARCHIVE_PLAN.md mit Status & Prüfkommandos ergänzt; TODO.md Fortschritte/Robustheit dokumentiert.
2025-10-17 10:10 | Copilot | Eval: optionaler Response-Cache in `scripts/run_eval.py` (`--cache`), Near-Dedupe in `prepare_finetune_pack.py` (`--near-dup-threshold`), neue Tests hinzugefügt; VS Code Test-Explorer konfiguriert (pytest), Run-&-Debug-Profile für Marker.
2025-10-18 09:15 | Copilot | Reruns: `scripts/rerun_from_results.py` (profile-aware, liest Meta/Overrides/Patterns), Pattern-Normalisierung implementiert; Smoke-Test hinzugefügt.
2025-10-19 12:12 | Copilot | Backup: Separates Backup-Repo finalisiert (origin auf neues Repo), orphan main mit README+MANIFEST; GitHub Release erstellt und alle Snapshot-Dateien als Assets hochgeladen (um LFS-Grenzen zu vermeiden).
2025-10-19 12:14 | Copilot | VS Code: Task "Eval: rerun from results" hinzugefügt; docs/TODO.md und docs/DONELOG.txt aktualisiert.
2025-10-19 12:28 | Copilot | Backup-Härtung: cvn-root-files ZIP sanitized (ohne .env) und im Release ersetzt; MANIFEST mit SHA-256 für alle Assets aktualisiert; README mit Restore-Anleitung ergänzt.
2025-10-19 13:05 | Copilot | Tests: Neue Script-Smokes (todo_gather, customize_prompts, map_reduce_summary_llm, open_latest_summary, fine_tune_pipeline) hinzugefügt; Scripts-Abdeckung auf ~67% erhöht.
2025-10-19 14:25 | Copilot | Tests: Integration "alpaca Export→Prepare" ergänzt; Edge-Tests für export_finetune, open_context_notes, rerun_failed, fine_tune_pipeline und App-Header auf 400; Suite grün, erneute Scripts-Coverage-Messung anstehend.
2025-10-19 15:10 | Copilot | Tests: 3+1-Runde durchgeführt (customize_prompts EOF/KeyboardInterrupt, map_reduce_summary Markdown+Excludes, fine_tune_pipeline Happy-Path, /health Header). Suite grün, Scripts-Coverage ~75%.
2025-10-19 15:30 | Copilot | Tests: 3+1-Runde II (map_reduce_summary Python/JSON-Zweige, rerun_failed JSON-Array, export_finetune Outdir-Fallback, /404 Header). Suite grün, Scripts-Coverage ~78%.
2025-10-19 15:50 | Copilot | Tests: 3+1-Runde III (fine_tune_pipeline fp16 & KeyboardInterrupt, export_finetune openai_chat include_failures, /chat/stream Fehler als SSE). Suite grün, Scripts-Coverage ~78%.
2025-10-19 16:10 | Copilot | Tests: 3+1-Runde IV (migrate_dataset_schemas Happy-Path, openai_ft_status Snapshot & Follow). Suite grün, Scripts-Coverage ~79%.
2025-10-19 16:28 | Copilot | Tests: 3+1-Runde V (audit_workspace Fallback, curate_dataset_from_latest Minimal-Flow, open_context_notes Happy, /chat Fehlerpfad). Suite grün, Scripts-Coverage ~79%.
2025-10-19 17:05 | Copilot | Tests: 3+1-Runde VI (curate_dataset_from_latest Filter-Exit-5; audit_workspace Referenzsuche; / Root Request-ID Header). Suite grün; Scripts-Coverage jetzt 80% (Branch-Coverage aktiv).
2025-10-20 09:10 | Copilot | Tests: 3+1-Runde VII (curate positive Filterpfad, audit Reachability-Graph, open_latest_summary open-Path, App Rate-Limit-Header). Neue Pfade abgedeckt; Schnelllauf grün.
2025-10-20 10:00 | Copilot | TODO/DONELOG aktualisiert; Konsistenzprüfung Runde 1 durchgeführt; Reports-Standard vorgeschlagen (eval/results/reports/<topic>/<ts> mit report.md und params.txt).
2025-10-20 10:20 | Copilot | Re-Check Konsistenz nach Löschungen: cleanup_recommendations.md aktualisiert; cleanup_phase3.ps1 portabel gemacht; REPORTS.md erstellt; Report abgelegt unter eval/results/reports/consistency/20251020_1015/.
2025-10-20 20:45 | Copilot | Demo→Fantasy-Umstellung konsolidiert (Code/Tests/Docs); Reporting-Skripte (Dependencies/Coverage/Consistency) ergänzt; CI-Workflow für Reports hinzugefügt; Legacy-Bereinigung: doppelten Re-Import in app/services/__init__.py entfernt, Rerun-Failed-Status in todo_gather vereinheitlicht, WORKSPACE_INDEX um Top-Level-Duplikat bereinigt.
2025-10-20 21:10 | Copilot | Endpoints final bereinigt (app/api/endpoints/* entfernt), README/WORKSPACE_INDEX aktualisiert, TODO-Drift korrigiert; Reports-Skripte lokal erfolgreich ausgeführt (dependencies/coverage placeholder/consistency).
2025-10-21 09:25 | Copilot | Pyright Linux-Fix: `scripts/open_context_notes.py` und `scripts/open_latest_summary.py` plattformneutral (webbrowser/open/xdg-open), `os.startfile` nur noch guarded; ungenutzte type: ignore entfernt.
2025-10-21 09:28 | Copilot | `scripts/run_eval.py`: `rich` optional gemacht (Console/Table/Progress Fallbacks) und Typen für `progress.update` bereinigt; mypy/pyright grün.
2025-10-21 09:31 | Copilot | `scripts/openai_ft_status.py`: Import von `openai` optional; Fehlerausgabe nur bei tatsächlicher Nutzung, Tests können `OpenAI` stubben.
2025-10-21 09:34 | Copilot | Synonyme erweitert: Eintrag für „empathisch“ (einfühlsam, zugewandt, mitfühlend, verständnisvoll, empathie) ergänzt; `tests/test_chai_checks.py` besteht.
2025-10-21 09:38 | Copilot | CI: `workflow_dispatch` zur CI hinzugefügt (manuelle Runs möglich); alle Checks grün (CI/build-test, Enforce DONELOG, Consistency & Reports).
2025-10-21 12:00 | Copilot | Chat-Options zentral normalisiert (normalize_ollama_options) und in Stream/Non-Stream verdrahtet; Policy-Stream-Tests (Pyright) stabilisiert; Copilot-Anleitung (PR-Checkliste/Marker/Pitfalls) geschärft.
2025-10-21 12:15 | Copilot | .gitignore: Kontext-Notizen konsolidiert (eval/config/context.local.* statt Einzellisten); keine weiteren Änderungen.
2025-10-21 13:29 | Copilot | Zeitstempel vereinheitlicht: utils/time_utils.py eingeführt; convlog nutzt now_iso(); append_done nutzt now_human(); schnelle Tests grün.
2025-10-21 13:35 | Copilot | Kompakte Timestamps zentralisiert: Scripts auf now_compact() umgestellt (export_finetune, map_reduce_summary[_llm], run_eval, rerun_from_results, reports/*, eval_ui, fine_tune_pipeline, todo_gather); Scripts-Tests grün.
2025-10-21 12:47 | Panicgrinder | Reports: Konsistenz/Dependencies/Coverage Generatoren repariert (sys.path + now_compact); Reports erzeugt.
2025-10-21 12:54 | Panicgrinder | TODO: Cleanup-Kandidaten-Sektion basierend auf Konsistenz-Report ergänzt; CLI-Tools markiert.
2025-10-21 20:53 | Panicgrinder | Docs: removed remaining Compose mention in TODO (superproject and submodule). Also restored VS Code settings from backup to undo catch-all auto-approve.
2025-10-21 20:57 | Panicgrinder | Tests: add pytest norecursedirs to ignore nested submodule; fix import mismatch and restore stable test runs (api, streaming, unit passing).
2025-10-21 22:00 | Panicgrinder | Docs: add docs-only history purge plan and helper script; wording cleanup in DONELOG.
2025-10-21 22:50 | Panicgrinder | Types: fix mypy errors in chat.py, content_management.py, and run_eval.py; no runtime behavior change.
2025-10-21 23:36 | Panicgrinder | Docs: add BEHAVIOR.md (Projektverhalten) und WORKSPACE_INDEX.md aktualisiert.
2025-10-22 00:41 | Panicgrinder | Eval: start overnight run (ASGI) tag=overnight-20251022; results will be summarized after completion.
2025-10-22 00:53 | Panicgrinder | Eval: Teilrun 50/136 (ASGI) saved to results_20251022_0042_overnight-20251022.jsonl; report at docs/reports/overnight-20251022.md.
2025-10-22 01:01 | Panicgrinder | Automation: add summarize_eval_results.py and VS Code task for overnight eval + auto report.
2025-10-22 01:11 | Panicgrinder | Add generator script for new eval items and create dataset eval-101-300_generated_v1.0.jsonl (200 items)
2025-10-22 13:54 | Panicgrinder | Docs konsolidiert: AGENT_BEHAVIOR.md erstellt (Merge aus AGENT_PROMPT.md + BEHAVIOR.md); Settings CONTEXT_NOTES_PATHS um AGENT_BEHAVIOR/TODO/DONELOG erweitert; Referenzen & VS Code Task aktualisiert.
2025-10-22 14:17 | Panicgrinder | Kontext: Digest in eval/config/context.local.md; Platzhalter-Logs für heute/gestern (data/logs/YYYY-MM-DD.jsonl) erstellt; Historie in docs/AGENT_BEHAVIOR.md präzisiert; TODO aktualisiert.
2025-10-22 16:50 | Panicgrinder | Docs/Tasks: Referenzen nach Entfernen der verschachtelten Kopie geprueft; keine verbleibenden  enter cvn-agent/-Hinweise; VS Code Task auf AGENT_BEHAVIOR.md umgestellt; Tests gruen; Typechecks: Pyright 1 Fehler (Test named arg), Mypy weist bestehende unused-ignore in Tests aus.
2025-10-22 17:30 | Panicgrinder | Typechecks gruen: Pyright Warnungen nur; Mypy konfiguriert (warn_unused_ignores in tests deaktiviert); Test-Fix: eval_mode aus ChatRequest() entfernt; tzinfo-Typ fix in time_utils.
2025-10-22 18:56 | Panicgrinder | docs/prompts: Sprache dauerhaft auf Deutsch gesetzt (AGENT_BEHAVIOR.md, DEFAULT_SYSTEM_PROMPT, context.local.md). Tests/Typen grün.
2025-10-22 19:19 | Panicgrinder | lint: Pyright-Warnungen reduziert  unbenutzte Imports in Scripts entfernt (curate_dataset_from_latest, eval_ui, export_finetune, fine_tune_pipeline, generate_eval_dataset, map_reduce_summary(_llm), reports/*, rerun_from_results, todo_gather). Tests/Typen grün.
2025-10-22 23:52 | Panicgrinder | Context notes: directory + .ref support; added eval/config/context.notes with 5 pinned refs; updated AGENT_BEHAVIOR.md
2025-10-23 00:22 | Panicgrinder | Context notes: directory order via ORDER file; ignore README/ORDER meta; collapse excessive blank lines in loader; docs+tests updated
2025-10-23 01:13 | Panicgrinder | Tests: docs obsolete absent  AGENT_PROMPT.md darf fehlen; Mypy: unused ignore in app/core/mode.py entfernt
2025-10-23 10:00 | Copilot | Kontext-Notizen Defaults erweitert (eval/config/context.notes in CONTEXT_NOTES_PATHS); eval_loader Diagnostics um schema_issues ergänzt; Tests/Typen unverändert.
2025-10-23 10:00 | Copilot | Kontext-Notizen Budget erhöht (CONTEXT_NOTES_MAX_CHARS=12000); Standard-Pfade für pinned Notes aktiv; schnelle Tests grün.
2025-10-23 10:20 | Copilot | Cleanup: `app/schemas.py` als Deprecation-Weiterleitung auf `app/api/models.py` umgestellt (keine direkten Importe gefunden); sichere Migration ohne Bruch.
2025-10-23 10:35 | Copilot | Cleanup: `app/schemas.py` endgültig entfernt; Modelle liegen zentral in `app/api/models.py`. Kurzer Testlauf grün.
2025-10-23 10:42 | Copilot | Cleanup-Review: `content_management` aktiv genutzt (behalten), `convlog` nur Beispiele (belassen), `summarize` in Tests/Beispielen (belassen), `session_memory` genutzt (belassen); TODO entsprechend aktualisiert.
2025-10-23 10:50 | Copilot | Lizenz hinzugefügt: MIT-Lizenz-Datei (`LICENSE`) und Hinweis in README.
2025-10-23 11:05 | Copilot | Policy-Hooks: Datei-basierte Minimal-Tests für forbidden_terms/rewrite_map hinzugefügt; Nutzung über SETTINGS.POLICY_FILE verifiziert; schneller Teil-Lauf grün.
2025-10-23 11:08 | Copilot | Doku: Abschnitt „Inhalts‑Policy & Hooks (optional)“ in AGENT_BEHAVIOR.md ergänzt (Aktivierung, POLICY_FILE, Struktur, Verweise auf Implementierung/Tests).
2025-10-23 11:30 | Copilot | Policy-Profile: Merge von default + profiles.<id> in content_management implementiert; Tests für Allow/Rewrite/Block/Profile-Merge/Bypass hinzugefügt; policy.sample.json erweitert.
2025-10-23 11:34 | Copilot | Memory: Tests für Fenster/Trunkierung (InMemory/JSONL) ergänzt; Append-Fehler schlagen Stream nicht mehr fehl (WARN statt Crash).
2025-10-23 11:36 | Copilot | LLM-Options: Smoke-Tests für erweiterte Optionen (num_ctx/stop/penalties) hinzugefügt; Pass-Through verifiziert.
2025-10-23 11:38 | Copilot | Doku: Profiles & Merge Order in AGENT_BEHAVIOR.md ergänzt; WORKSPACE_INDEX aktualisiert (LICENSE, policy.sample.json, Beschreibungen).
2025-10-23 11:40 | Copilot | DONELOG: Autorenschafts-Hinweis in AGENT_BEHAVIOR.md ergänzt (Quelle kann Mensch oder Tool sein; Format dokumentiert).
2025-10-23 11:46 | Copilot | ChatOptions: Pydantic-Optionschema eingeführt; ChatRequest.options akzeptiert Dict oder ChatOptions; chat.py passt Mapping/Dump an; Tests hinzugefügt.
2025-10-24 11:20 | Panicgrinder | Cleanup: app/prompt/system.txt (Altlast) entfernt; WORKSPACE_INDEX und README geprüft.
2025-10-24 11:28 | Copilot | Pyright-Warnungen im App-Code bereinigt (casts/Typen in chat_helpers, content_management, mode, main); Pyright-Config auf app+utils fokussiert.
2025-10-25 09:10 | Copilot | Mittelfristig: Tool‑Use Basis angelegt (Settings: TOOLS_ENABLED/WHITELIST; Registry; calc_add Tool; Unit‑Tests). TODO.md aktualisiert.
2025-10-25 14:02 | Panicgrinder | Kontext-Notizen: Priorität auf lokale Dateien (context.local.*) vor angehefteten Refs (context.notes) gesetzt; Pyright-Konfiguration bereinigt (ungueltige Keys entfernt, Tests/Scripts vorerst ausgeschlossen). Tests & Typen grün.
2025-10-25 14:22 | Panicgrinder | Streaming: Initiales Meta-Event (params: mode, request_id, model, options) am Stream-Beginn hinzugefügt; Test ergänzt (tests/test_streaming_initial_meta.py); TODO.md aktualisiert. Suite & Typen grün.
2025-10-25 18:51 | Panicgrinder | API: Einheitliches Message-Schema  ChatRequest.messages akzeptiert ChatMessage oder dict; Validator hinzugefügt; Tests ergänzt (tests/test_messages_schema.py). CI-Gates grün.
2025-10-25 19:52 | Panicgrinder | Typfehler in app/main.py behoben: Messages-Längenprüfung für ChatMessage|dict; request.json typisiert; Pyright/Mypy grün; Tests unverändert grün.
2025-10-25 20:12 | Panicgrinder | Refactor: _get_content_from_message() eingeführt; Union-Attributzugriff eliminiert; Pyright/Mypy/Tests grün.
2025-10-25 21:10 | Copilot | RAG (leichtgewichtig) integriert: TF‑IDF‑Retriever injiziert Top‑K Snippets als System‑Nachricht (optional via SETTINGS.RAG_*); CLI `scripts/rag_indexer.py` hinzugefügt; bestehende Tests unverändert.
2025-10-25 21:18 | Copilot | Bugfix: utils/rag.py save_index Einrückung korrigiert (payload/json.dump innerhalb des with‑Blocks); Tests/Typen erneut grün.
2025-10-25 21:13 | Panicgrinder | Kleine Korrekturen
2025-10-25 22:07 | Panicgrinder | Pyright-Warnungen in utils/rag.py entfernt: explizite Typisierungen in from_dict (Dict[str, object], Mapping-Casts); keine Verhaltensänderung.
2025-10-25 22:16 | Panicgrinder | Tests ergänzt: RAG-Guards (stream/non-stream) sichern None-Index-Pfade ab; chat.py Typisierungen für RAG-Imports/idx präzisiert; Pyright jetzt 0 Warnungen; Verhalten unverändert.
2025-10-25 22:20 | Panicgrinder | Outstanding Änderungen synchronisiert (Tasks, AGENT_BEHAVIOR, Settings, WORKSPACE_INDEX); rag_indexer Script hinzugefügt. Keine Verhaltensänderung.
2025-10-25 22:31 | Panicgrinder | TODO um RAG-Sektion konsolidiert (Fortschritt+Next Steps an passender Stelle); Unit-Tests für TF-IDF (retrieve Ranking, save/load Roundtrip) ergänzt; Gates grün.
2025-10-25 22:37 | Panicgrinder | README: kurzer Abschnitt 'Lokales RAG' ergänzt (Flags, Indexer-CLI, Beispiel, Task-Hinweise); keine Codeänderungen; Gates grün.
2025-10-25 23:20 | Panicgrinder | chat.py: SSE streaming now emits 'event: delta' with JSON {text} per chunk; keeps meta/done and post-policy meta; tests+pyright+mypy PASS.
2025-10-25 23:59 | Copilot | Streaming: SSE-Chunks als Plain "data: <chunk>" + Fallback bei invalid JSON; "event: delta" nur bei Post-Rewrite; Tests/Pyright/Mypy PASS.
2025-10-25 23:59 | Copilot | LLM-Optionen erweitert: ChatOptions & Normalisierung (top_k, min_p, typical_p, tfs_z, mirostat*, penalize_newline); Settings-Defaults ergänzt; README dokumentiert; Validation-Tests hinzugefügt; Gates PASS.
2025-10-26 00:05 | Copilot | Doku: customization.md um Abschnitt zu LLM-Optionen (Defaults via .env, Pro-Request-Overrides, Beispiele curl/PowerShell) erweitert; Gates PASS.
2025-10-25 23:58 | Panicgrinder | eval_ui: profiles support top_p/num_predict; added sample profile policies; updated eval README; tests+types PASS
2025-10-26 00:10 | Panicgrinder | eval_ui: robust multi-select (comma/space/semicolon, ranges); search datasets+eval for packages; gates PASS
2025-10-31 13:22 | Panicgrinder | Markdownlint-Workflow geprüft; offene Funde aus novapolis-rp erfasst
2025-10-31 14:05 | Copilot | Dokumentation auf Novapolis Agent umgestellt (AGENT_BEHAVIOR, README, TODO, customization, Index, Eval-Doku, Kontextsample aktualisiert).
2025-10-31 15:10 | Copilot | Root-Dokumente (Copilot-Anleitung, README, TODO, DONELOG) an Novapolis Agent Branding angepasst.
2025-10-31 23:40 | Copilot | Agent-Workspace in `novapolis_agent` umbenannt, Mypy-Flow angepasst und Statusdateien bereinigt.
```

</details>

<details>
<summary>novapolis-dev/docs/donelog.md</summary>

```markdown
<!-- markdownlint-disable MD005 MD007 MD032 MD041 -->
<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/donelog.md` am 2025-10-29 -->

Canvas-Rettung Sprint 1 – AI Behavior Matrix (2025-11-01T17:55:00+01:00)

- RAW-Canvas `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.txt` promotet: `database-rp/00-admin/AI-Behavior-Mapping.md` auf Version 1.0 erweitert (Cluster-Tabelle, Intensitätsskala, Modifikatoren, Pflege-Routine, Einsatzrichtlinien).
- Anchor-Register um alle aktuellen Charaktere in `02-characters/` ergänzt (inkl. Echo/Lumen/Liora/Lyra/Senn/Varek; `n/a` markiert fehlende Signaturen); Psymatrix-Abgleich-Routine mit Schwellen (`PsySignatur_Dissonanz`, Kohäsion) dokumentiert.
- Sidecar `AI-Behavior-Mapping.json` synchronisiert (Version 1.0, last_updated, dependencies `ai_behavior_index_v2`/`ai_psymatrix_index_v1`, Tag-Set ergänzt).
- TODO aktualisiert (AI-Behavior-Index erledigt, Validator-Follow-up) und Arbeitsablauf um Anchor-Check erweitert; Quellen/Flag-Hinweise verankert.

Canvas-Rettung Sprint 1 – Ronja Kerschner (2025-11-01T17:12:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Ronja-Kerschner.md` auf Version 1.0 aktualisiert; Status-/Systemabschnitte aus RAW `char_ronja_v2` übernommen und Drift („Vallin“) gemäß `resolved.md #[NAME-RONJA]` dokumentiert.
- JSON-Sidecar (`Ronja-Kerschner.json`) synchronisiert; Routine- und Systemverknüpfungen mit Review-Hinweis auf logistik-/inventar-v1 markiert.
- TODO-Boards (`novapolis-dev/docs/todo.md`, Root `TODO.md`) aktualisiert; Aufgabe „Ronja Kerschner“ auf erledigt gesetzt.
- Quellenhinweise erweitert (Canvas-Quellenblock + `char-block-nord-sources.md` Ronja-Abschnitt aktualisiert); Metadaten-Zeitstempel angepasst.

Canvas-Rettung Sprint 1 – Echo Metadatenabgleich (2025-11-01T16:35:00+01:00)

- Canvas `database-rp/02-characters/Echo.md` um Front-Matter ergänzt (Titel, Version, Zugehörigkeit, Standort, Dependencies) und Markdown-Formatierung mit Leerzeichen/Abständen an Vorlagen angepasst.
- JSON-Sidecar `database-rp/02-characters/Echo.json` auf dieselben Metafelder synchronisiert (last_updated, tags, affiliations, primary_location, dependencies).
- Keine Inhaltsänderungen; Fokus auf formale Angleichung für Lint/Validator-Kompatibilität.

Canvas-Rettung Sprint 1 – Liora Navesh (2025-11-01T16:25:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Liora-Navesh.md` + JSON-Sidecar erstellt; Arkologie-A1-Taxonomie und Validierungsintervall übernommen, Novapolis/D5 weiterhin als unbekannt markiert, SÜDFRAGMENT-Signale und A9-Protokolle hervorgehoben.
- Quellenreport `char-block-nord-sources.md` aktualisiert; Flag-Hinweise (Secrecy, Taxonomie) als abgearbeitet vermerkt und Curated-Verweis ergänzt.
- `novapolis-dev/docs/todo.md` → Liora-Aufgabe als erledigt mit Zeitstempel 2025-11-01T16:20+01:00 markiert; last-updated synchronisiert.
- Personenindex `database-rp/00-admin/person_index_np.md` um Liora ergänzt (Rolle, Zugehörigkeit Arkologie A1, Fokus auf SÜDFRAGMENT, keine Novapolis-Kenntnisse).
- JSON-Sidecar verweist auf Canvas und Abhängigkeiten (`ai_behavior_index_v2`, `relationslog_arkologie_v1`, `ereignislog_weltgeschehen_v1`, `cluster_index_v1`).

Canvas-Rettung Sprint 1 – Varek Solun (2025-11-01T15:55:00+01:00)

- Charakter-Canvas `database-rp/02-characters/Varek-Solun.md` + JSON-Sidecar erstellt; Standortcode H12 (Alias „Sektor_H3“) harmonisiert, Wissensstand gemäß FACT SECRECY auf Gerüchte begrenzt.
- Quellen/Drift-Notizen in `char-block-nord-sources.md` aktualisiert; Flag-Hinweise (Novapolis-Außenwissen, Standortcodierung) als erledigt markiert.
- `novapolis-dev/docs/todo.md` und Root-`TODO.md` → Varek-Aufgabe als erledigt vermerkt (Zeitstempel 2025-11-01T15:45:00+01:00).
- Personenindex `database-rp/00-admin/person_index_np.md` um Varek ergänzt (Rolle, Zugehörigkeit, Verlinkung).
- JSON-Sidecar referenziert Metadaten + Quelle; Routine- und Systemverknüpfungen dokumentiert.

Canvas-Rettung Vorbereitungsrunde (2025-11-01T14:30:00+01:00)

- Canvas-Rettungsplan in `database-curated/staging/reports/canvas-rescue-plan.md` ausgearbeitet (Prioritäten A–C, Workflow, Sprint-Checkpoints, Prüfpfade).
- Quellenaggregation `char-block-nord-sources.md` erstellt (RAW-Referenzen, Drift-Overrides für Ronja/Jonas, Flag-Hinweise gebündelt).
- TODO-Board `novapolis-dev/docs/todo.md` auf Canvas-Rettung Sprint 1 fokussiert, Altbacklog in Archiv-Section überführt.
- Hinweis gesetzt: Jede Canvas-Migration → JSON-Sidecar + DONELOG-Eintrag obligatorisch.

Root-Dokumentation (2025-11-01T00:00:00Z)

- Root-Übersichten `WORKSPACE_STATUS.md`, `TODO.md`, `README.md`, `DONELOG.md` auf Stand 2025-11-01 gebracht (Health-Checks, Aufgaben, Querlinks).
- Tree-Snapshots (`workspace_tree*.txt`) als fällige Folgeaufgabe markiert.

Dev-Hub QA (2025-11-01)

- Modul `novapolis-dev` vollständig geprüft: Primärdokumente, Meta-Sidecars und Platzhalterverzeichnisse vorhanden; keine offenen Drift-Punkte.
- Rolle des Dev-Hubs bestätigt – Dokumentations-/Planungsdrehscheibe, Datenströme verbleiben in `novapolis-rp` (`database-raw`, `database-curated`, `database-rp`).

Agent-Runtime entkoppelt (2025-10-31)

- `novapolis-rp/agents/cvn_agent/` vollständig entfernt; Root-README, RP-README und Ignore-Regeln auf das eigenständige `novapolis_agent`-Repository umgestellt.
- Verweise auf das gebündelte Runtime-Paket bereinigt (`requirements.txt`, `.github/copilot-instructions.md`).
- Obsoletes Patch `_cvn_agent_removal.patch` gelöscht; RP-Workspace enthält nur noch Daten/Docs.
- Leeres Paketverzeichnis `novapolis-rp/agents/` entfernt; keine Agent-Stubs mehr im RP-Repo.

Workspace-Status Snapshot (2025-10-31)

- Gesamtübersicht `WORKSPACE_STATUS.md` auf Root-Ebene angelegt (Stand 2025-10-31) inkl. Health-Checks, Risiken, Empfehlungen.
- Vollständigen Verzeichnisbaum via `tree /A /F` erzeugt und als `workspace_tree.txt` im Root abgelegt.
- Root-`TODO.md` um Verweis auf Statusbericht ergänzt (Pflegezyklus vermerkt).
- Redundante Snapshot-Datei `workspace_tree_full.txt` als Backup abgelegt; zusätzlich kompaktes Verzeichnis-Listing `workspace_tree_dirs.txt` erzeugt.
- README-Hinweise für `.tmp-datasets/` und `.tmp-results/` ergänzt, Zweck der temporären Artefakte dokumentiert.
- Archivierungsplan in `TODO.md` konkretisiert (ZIP-Rotation, Manifest/Script-Aufgaben); Status-Doku verweist jetzt auf koordinierte Snapshot-Aktualisierung.
- Redundanten Snapshot `workspace_tree_compact.txt` entfernt, da `workspace_tree_dirs.txt` die kompakte Ansicht abdeckt.

Relocation Follow-up (2025-10-31)

- Datenpools `database-curated`, `database-raw`, `database-rp` wieder unter `novapolis-rp/` verankert; Dev Hub verweist nur noch auf diese Quelle (`README.md`, `docs/todo.md`).
- `novapolis_agent/docs/TODO.md` um aktuellen RAG-Status aktualisiert (Tests & Doku als erledigt markiert).
- Zentrale Markdown-Lint-Checks via `.github/workflows/markdownlint.yml` reaktiviert; rp-spezifische Duplikat-Workflows entfernt (`docs-lint.yml`, redundante Schritte in `validate.yml`).

Dev Hub Konsolidierung (2025-10-29)

- Dev Hub vom ehemaligen RP-Development-Hub nach `novapolis-dev/docs` verlegt; Referenzen aktualisiert und Meta-Sidecars harmonisiert.
- Legacy `development/docs` bereinigt; Meta-Sidecars geprüft; `.github/copilot-instructions.md` im RP-Repo ergänzt.
- 2025-10-29: Meta sidecars normalized: origin → full legacy path; migrated_at added.
- 2025-10-29: Dev Hub polish (README/index), VS Code Copilot instructions verlinkt; Residual-Sweep ohne Treffer.

VS Code Launch-Konfigurationen (2025-10-28)

- `.vscode/launch.json` hinzugefügt:
  - PowerShell-Runner: `validate:data (ps1)`, `lint:names (ps1)`, `system:check (windows)` (Markdownlint direkt via `npx` oder Root-Task).
  - Node-Varianten: `validate:data (node/npm)`, `lint:names (node)`, `lint:markdown (npx)`, `validate:data (status)`.
  - Ziel: Checks direkt per Startmenü (Run and Debug) nutzbar; identische Pfade wie Tasks/Wrapper.

Dokumentation/Tasks aktualisiert (2025-10-27T20:06:30+01:00)

- `novapolis-dev/docs/index.md` (vormals Coding-Index): Abschnitt "Validierung & Tasks" ergänzt (Validatoren, Lint, Systemcheck); Verweise auf `tools/validators/` und Devcontainer; `last-updated` angepasst.
- `novapolis-dev/docs/copilot-behavior.md` (vormals Coding-Copilot-Policy): Prozessregeln präzisiert – vor Push lokale Tasks ausführen (validate/data, lint/markdown, optional lint/names); Szenen‑Front‑Matter und Co‑Occurrence beachten.
- `novapolis-dev/docs/todo.md` (vormals Coding-TODO): Status synchronisiert – Rückwärts‑Review bis part‑001 abgehakt; Day‑Switch‑Canvas abgehakt; QA‑Punkt zu Szenen‑Front‑Matter in "etabliert" (✓) und "Backfill" (offen) aufgeteilt; `last-updated` angepasst.

Canvas-Verbesserungen (2025-10-27)
Linter-Wrapper (2025-10-27T20:12:30+01:00)

- `coding/tools/validators/run_check_names.ps1` hinzugefügt: stabiler Aufruf des Name-Linters ohne PowerShell `-Command`‑Quoting; nutzt Docker (falls vorhanden) oder Node/npm, sonst Exit 1 mit klarer Meldung.
- `coding/tools/validators/README.md` ergänzt (Wrapper‑Hinweis); `novapolis-dev/docs/index.md` mit Fallback‑Befehl verlinkt.

PS1-Tasks ergänzt (2025-10-27T20:18:30+01:00)

- `.vscode/tasks.json`: zusätzliche Tasks ohne Inline‑`-Command` aufgenommen:
  - `lint:names (ps1)` → `run_check_names.ps1`
  - `validate:data (ps1)` → `run_validate_all.ps1`
  - `lint:markdown (ps1)` → `run_lint_markdown.ps1` (veraltet seit 2025-11-01; bitte Root-Task bzw. `npx` verwenden).
- Neue Wrapper: `run_validate_all.ps1`, `run_lint_markdown.ps1` (Docker bevorzugt; sonst lokal; klare Fehlermeldung bei fehlenden Voraussetzungen; Markdownlint-Wrapper obsolet seit 2025-11-01).

CI erweitert (2025-10-27T22:40:00+01:00)

- `.github/workflows/validate.yml` aufgeteilt:
  - Linux-Job (Node 20) mit npm cache; führt Validatoren, Name‑Check, Markdown‑Lint aus.
  - Windows-Job (PS1-Wrapper) – führt `run_validate_all.ps1`, `run_check_names.ps1`, `run_lint_markdown.ps1` aus, um PowerShell-Skripte in CI mitzuprüfen (Wrapper seit 2025-11-01 ohne Markdownlint-Einsatz).
- Validator-Fixes:
  - Ajv 2020‑12 für kuratiertes Manifest (`validate-curated.js`).
  - Front‑Matter‑Validator (`validate-rp.js`): `last-updated` tolerant (String/Date), H1‑Allowlist für `00-admin/system-prompt.md`.

Markdown-Lint Wrapper gefixt (2025-10-27T22:55:00+01:00) – veraltet seit 2025-11-01

- `coding/tools/validators/run_lint_markdown.ps1`: Fallbacks ergänzt (veraltet seit 2025-11-01)
  - absolute `node.exe` Erkennung; direkter Aufruf von `npx-cli.js` via `node.exe` (unabhängig von PATH)
  - Reihenfolge: Docker → node+npx-cli.js → npx.cmd → Fehlermeldung
  - Behebt Fehler "'node' is not recognized" bei fehlendem PATH.
- `00-admin/Canvas-Admin-Day-Switch-Debug.md`: ATSD-Definition ergänzt, Systemmeldungs-Template aufgenommen, Fehlerfälle/Recovery ergänzt.
- `00-admin/Canvas-T+0-Timeline.md`: Marker-Raster (Beginn/Ereignisse/Ende) und Delta-Log ergänzt.
- `00-admin/canon-canvas.draft.md`: Front-Matter (last-updated, status) hinzugefügt; Tippfehler "Akologie"→"Arkologie" korrigiert; Revision vermerkt.
- `06-scenes/scene-2025-10-27-a.md`: Erste Szenen-Kachel mit Front-Matter (characters/locations/inventoryRefs) und Cross-Links angelegt; Timeline T+0 verlinkt.
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.txt` (Quelle: Canvas; Entität Reflex – Wurzelgewebe D5 v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.flags.txt` (vorsichtig_behandeln; Grund: Regeln [REFLEX-*] abgleichen; "Entfernen möglich" vs [REFLEX-DETACH] klären; Frequenzband/Terminologie synchronisieren).
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.txt` (Quelle: Canvas; Charakter Dr. Liora Navesh v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.flags.txt` (vorsichtig_behandeln; Grund: [FR-KNOWLEDGE] wahren; H‑47/SÜDFRAGMENT gegen [EVENT-TIMELINE] prüfen; Arkologie_A1 Taxonomie mit Cluster/Relations harmonisieren).
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.txt` (Quelle: Canvas; Charakter Varek Solun v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: [FR-KNOWLEDGE] wahren; H‑47-Routenstatus prüfen; Standort-Taxonomie H12 vs "Sektor_H3" harmonisieren vor Promotion).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.txt` (Quelle: Canvas; Relationslog Novapolis v1; TIMESTAMP: 2025-10-16_08:07).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Namens-/ID-Drift – System „novapolis_logistik_v1“ vs. Schema `logistik_novapolis_v*`; Händlerkontakt „Senn Daru“ unbekannt; gegen Händlergilde-Kanon prüfen/normalisieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.txt` (Quelle: Canvas; AI Behavior Index v2; TIMESTAMP: 2025-10-16_11:05).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Globales Matrix-Canvas – Versionsabgleich mit [BEHAVIOR-VERSION] und `ai_psymatrix_index_v1`; Modifikatoren-/Code-Format vereinheitlichen, Mappings dokumentieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.txt` (Quelle: Canvas; Ereignislog Weltgeschehen v1; TIMESTAMP: 2025-10-16_05:34).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Timeline/Namensabgleich – H-47 Identität offen; "Allianz" gegen [SECRECY]/[FR-KNOWLEDGE] prüfen; mit Missionslog/Sim-Woche synchronisieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt` (Quelle: Canvas; Logistik Novapolis v2; TIMESTAMP: 2025-10-16_13:05).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Konsistenzprüfung Link-Graph v2; Curation vormerken).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.txt` (Quelle: Canvas; Logistik C6 v2; TIMESTAMP: 2025-10-16_12:55).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Verknüpfungen referenzieren `logistik_novapolis_v1` trotz v2; vor Promotion angleichen/begründen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-30-00-000Z.txt` (Quelle: Canvas; Inventar C6 v2; TIMESTAMP: 2025-10-16_12:30).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-30-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Systemverknüpfungen referenzieren `logistik_novapolis_v1`; v2-Set angleichen oder begründen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-00-00-000Z.txt` (Quelle: Canvas; Station D5 – Basis (legacy)); TIMESTAMP: 2025-10-16_12:00).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-00-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Legacy-Snapshot; mit D5 v2.1/Kanon abgleichen, erst danach promoten).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.txt` (Quelle: Canvas; Charakter Jonas v2; TIMESTAMP: 2025-10-16_14:12).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.flags.txt` (vorsichtig_behandeln, korrupt; Grund: Konflikt m

```

2025-11-07 21:29 | Panicgrinder | update Frontmatter und betroffene Dateien (commit d06ab6b)

Automatisierte Frontmatter-Updates (2025-11-07)

Ein Wrapper-Skript `scripts/append_done_and_push.ps1` wurde hinzugefügt und getestet. Das Skript ergänzt bzw. aktualisiert bei Dateiänderungen die YAML-Frontmatter (`stand`, `update`, optional `checks`), legt vor Änderungen Backups (`<file>.bak`) an, führt einen scoped Frontmatter-Validator für die betroffenen Dateien aus und protokolliert jede Aktion in `novapolis_agent/docs/DONELOG.txt` (optional zusätzlich in `DONELOG.md`). Relevante Commits aus der Sitzung: d06ab6b, 80f7e32, 0c98ea6. Validator-Wrapper: `scripts/run_frontmatter_validator.ps1`.

2025-11-07 21:46 | Panicgrinder | Implementiert: `scripts/append_done_and_push.ps1` — automatisierte Frontmatter-Updates (`stand`/`update`[, `checks`]), Backups `<file>.bak`, scoped Frontmatter-Validator, DONELOG-Append; Commits: d06ab6b, 80f7e32, 0c98ea6.

2025-11-07 22:11 | Copilot | Korrektur/Anmerkung: Vorheriger Eintrag (2025-11-07 21:46 | Panicgrinder) wurde geprüft; wegen partieller Anzeige/Kürzung im Editor habe ich die aktuelle Systemzeit dokumentiert. Originaleintrag bleibt unverändert; diese Zeile dient der Audit-Transparenz.
