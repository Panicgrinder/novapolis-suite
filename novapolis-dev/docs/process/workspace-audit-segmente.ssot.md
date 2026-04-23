---
stand: 2026-04-23 19:03
update: Diese SSOT teilt den Workspace erstmals in feste, wiederverwendbare Pruefsegmente fuer Aktualitaet, Redundanz, Verdrahtung und Gate-Belege.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260423_155606.md; snapshot-lock PASS (2026-04-23 19:03)
---

Workspace-Audit-Segmente (SSOT)
===============================

Zweck
-----

Diese SSOT zerlegt den Workspace in feste, wiederverwendbare Pruefsegmente.
Jeder kuenftige Gesamtcheck soll dieselben Teile in derselben Reihenfolge lesen, statt den Workspace ad hoc neu zu zerlegen.

Audit-Achsen
------------

- `Aktualitaet`: Fuehrende Quellen, `stand`-Werte, Reports und Taskpfade zeigen auf denselben aktuellen Iststand.
- `Redundanz`: Gleichlautende Aussagen leben nicht als konkurrierende Wahrheiten in mehreren aktiven Pfaden.
- `Verdrahtung`: README, Index, Tasks, Wrapper, Prozess-SSOTs und Moduldocs zeigen auf dieselben kanonischen Start- und Checkpfade.
- `Gate-Beleg`: Fuer jedes Segment gibt es mindestens einen reproduzierbaren Check- oder Nachweispfad.

Kanonische Pruefsegmente
------------------------

| ID | Segment | Scope | Fuehrende Quellen | Primaere Checks/Tasks | Leitfragen |
| --- | --- | --- | --- | --- | --- |
| `W1` | Root-Steuerflaeche und Governance | Root-README, Root-Status, Root-Index, Root-DONELOG, `.github/`, `.vscode/` | `README.md`, `WORKSPACE_STATUS.md`, `WORKSPACE_INDEX.md`, `DONELOG.md`, `.github/copilot-instructions.md`, `.vscode/tasks.json` | `Checks: full`, `Checks: path portability`, `Checks: naming policy`, `Checks: todo index sync`, `Checks: doc freshness`, `Checks: logs policy` | Ist die Root-Navigation aktuell, sind Governance-Regeln eindeutig, und zeigen Tasks/Status auf dieselben Start- und Checkpfade? |
| `W2` | Shared Tooling und Paketlage | Root-`scripts/`, `packages/`, Root-Requirements, tools-only Root-Konfig | `scripts/`, `packages/novapolis_common`, `pyproject.toml`, `requirements.txt`, `requirements-dev.txt` | `Checks: linters (all)`, `Checks: types (pyright+mypy)`, `Tests: pytest (-q) [root]`, `Tests: coverage (fail-under)`, `scripts/check_scripts_layout.py` | Entstehen neue Wrapper am richtigen Ort, ist geteilte Logik nicht unnötig dupliziert, und sind Root-Skripte mit Tasks/Docs verdrahtet? |
| `W3` | Dev-Hub und aktive Dokuoberflaeche | `novapolis-dev/docs/**` ohne Archiv, inklusive Boards, Prozess- und Referenzdoku | `novapolis-dev/README.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/donelog.md`, `novapolis-dev/docs/active-surface-index.md`, `novapolis-dev/docs/process/**` | `Docs: sync after checks`, `Checks: todo index sync`, `Checks: doc freshness`, `Checks: logs policy`, markdownlint, Frontmatter-Validator | Sind aktive und historische Doku sauber getrennt, sind Board-/Index-Claims konsistent, und gibt es nur eine aktive Prozessquelle je Thema? |
| `W4` | Agent-Runtime, Eval und Training | `novapolis_agent/` Code, Datasets, Eval, Runbook, Runtime- und Trainingspfade | `novapolis_agent/README.md`, `novapolis_agent/docs/runbook.md`, `novapolis_agent/app/**`, `novapolis_agent/scripts/**`, `novapolis_agent/eval/**`, `novapolis-dev/docs/dataset-provenance.md` | `Tests: pytest (unit)`, `Tests: pytest (api+streaming)`, `Tests: coverage (fail-under)`, `Checks: full`, `Checks: text-rpg product gate`, `Checks: gm runtime preflight`, `Eval: validate suite datasets (strict)` | Stimmen Runtime-, Eval-, Export- und LoRA-Pfad ueberein, sind Release-Gates belegt, und driftet keine Agent-Doku gegen die kanonischen Skriptpfade? |
| `W5` | RP-Kanon, RAW und Curation | `novapolis-rp/` SSOT, RAW, curated staging, RP-Admin und Prozessbruecken | `novapolis-rp/README.md`, `novapolis-rp/database-rp/**`, `novapolis-rp/database-raw/**`, `novapolis-rp/database-curated/**`, RP-bezogene Prozess-SSOTs | `scripts/check_current_state_gate.py`, `scripts/check_rp_hard_gates.py`, `scripts/checks_rp_consistency.py`, `scripts/check_rp_staging_tag_coverage.py` | Bleibt RP-SSOT von RAW und Laufzeitspuren getrennt, sind Pflichtlinks vorhanden, und sind Promotions-/Staging-Pfade nachvollziehbar verdrahtet? |
| `W6` | Sim-Client, Export und Verify | `novapolis-sim/` Godot-Projekt, Hub-/Replay-/Exportpfade, Fixtures und Sim-bezogene Prozessdocs | `novapolis-sim/README.md`, `novapolis-sim/project.godot`, `novapolis-sim/Main.tscn`, `novapolis-sim/scripts/**`, `novapolis-dev/docs/todo.sim.md`, `novapolis-dev/docs/process/sim-*.ssot.md` | `Checks: sim headless verify`, `Checks: sim epoch assets`, `Checks: sim epoch assets (minimal fullstand)`, `Checks: sim export smoke`, `Checks: sim hub prefs contract` | Stimmen Hub-, Replay-, Export- und Verify-Pfad ueberein, sind ausgelagerte Controller mit `Main.gd` konsistent verdrahtet, und ist der Godot-Nachweis auf dem Ausfuehrungshost belegbar? |
| `W7` | Historische, generierte und forensische Flaechen | Archive, Quarantaene, Backups, Outputs, `.tmp`, Eval-Results, generierte Trees | `novapolis-dev/archive/**`, `Backups/**`, `outputs/**`, `.tmp/results/reports/**`, `workspace_tree*.txt`, `novapolis_agent/eval/results/**` | `Workspace tree:*`, `scripts/update_backups_manifest.py`, `Checks: logs policy` | Bleiben Archive und Laufzeitartefakte ausserhalb der aktiven SSOTs, und sind forensische Pfade nachvollziehbar statt still in aktive Navigation einzusickern? |

Verbindliche Reihenfolge
------------------------

1. `W1` Root-Steuerflaeche und Governance
2. `W3` Dev-Hub und aktive Dokuoberflaeche
3. `W2` Shared Tooling und Paketlage
4. `W4` Agent-Runtime, Eval und Training
5. `W5` RP-Kanon, RAW und Curation
6. `W6` Sim-Client, Export und Verify
7. `W7` Historische, generierte und forensische Flaechen

Mindestbeleg pro Auditlauf
--------------------------

- Fuer jedes Segment mindestens ein belegter Check, Task oder gerichteter Dateiabgleich.
- Befunde immer gegen die vier Audit-Achsen formulieren: `Aktualitaet`, `Redundanz`, `Verdrahtung`, `Gate-Beleg`.
- Wenn ein Segment keinen technischen Check besitzt, muss der manuelle Abgleich explizit benannt werden.

Initialer Iststand 2026-04-23
-----------------------------

- Der Workspace hatte vor diesem Lauf bereits Navigation, Boards und einzelne Gate-SSOTs, aber noch keinen eigenen, wiederverwendbaren Gesamt-Pruefschnitt.
- Mit dieser Datei ist die Zerlegung jetzt erstmals als kanonischer Zukunftsrahmen festgezogen.
- Der erste konkrete Restbefund nach dieser Zerlegung lag kurzzeitig in `W2` und `W5`: Mehrere bereits vorhandene Governance-/Audit-Skripte (`check_scripts_layout.py`, `check_current_state_gate.py`, `check_rp_hard_gates.py`, `checks_rp_consistency.py`, `check_rp_staging_tag_coverage.py`, `update_backups_manifest.py`) besassen zunaechst weder einen kanonischen VS-Code-Task noch einen Einstieg ueber `scripts/run_checks_and_report.py`.
- Dieser Befund ist im aktuellen Iststand geschlossen: `.vscode/tasks.json` fuehrt jetzt explizite Einstiege fuer `Checks: scripts layout`, `Checks: rp current-state gate`, `Checks: rp consistency`, `Checks: rp hard gates`, `Checks: rp staging tag coverage` sowie `Backups: update manifest`; die pruefbaren W2/W5-Checks liefen im direkten Validierungspfad gruen.
- `W6` ist im aktuellen Iststand ebenfalls gruen: Das Sim-Board steht nach dem Resolver-Fallback fuer `run_sim_headless_verify.py` wieder bei `offen: 0`, und `Checks: sim headless verify` ist laut aktueller Board-/Index-Synchronisation wieder belegbar PASS.

Verweise
--------

- Root-Navigation: `README.md`, `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`
- Dev-Hub: `novapolis-dev/README.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/active-surface-index.md`
- Abschlussrhythmus: `novapolis-dev/docs/process/abschluss-routine.ssot.md`
