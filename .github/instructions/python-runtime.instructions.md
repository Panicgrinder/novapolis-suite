---
description: Regeln für Python-Wrapper, pwsh-Einzeiler, Testsequenzen und Runtime-Ausführung im Repo.
name: Python Runtime Instructions
applyTo: scripts/**/*.py,novapolis_agent/scripts/**/*.py,novapolis_agent/tests/**/*.py,**/*test*.py
---

Python Runtime
==============

Ziel
----
- Einheitliche Ausführung für mehrschrittige Befehle, Tests und Artefaktläufe.

Regeln
------
- Mehrschrittige Abläufe über `& .\.venv\Scripts\python.exe scripts\<script>.py`.
- Inline `pwsh -Command` nur für echte Einzeiler.
- Interpreter: `.venv` bevorzugt, Fallback `python`.
- Bei Pfaden mit Leerzeichen `Join-Path` und `${workspaceFolder}` nutzen.

Prüfsequenz
-----------
- Reihenfolge standardisiert: Lint → Typen → Tests → Coverage.
- Coverage-Gate: Mindestwert gemäß Projekt-Gates (aktuell ≥ 80 %).
- Bei Unsicherheit/Scope-Drift: STOP und Rückfrage.

Regelmatrix
-----------
- `id: R-WRAP, priority: 1, scope: python_runtime, trigger: multistep_command, action: run_via_python_wrapper, validation: command_path_venv_or_python, exceptions: markdownlint_npx_yes, notes: pwsh_inline_only_oneliner`
- `id: R-COV, priority: 1, scope: tests, trigger: coverage_run, action: enforce_minimum_coverage, validation: fail_under_gate_green, exceptions: explicit_override_with_stop, notes: report_result_in_receipt`
- `id: R-ORDER, priority: 2, scope: checks, trigger: full_check_requested, action: run_lint_types_tests_coverage_ordered, validation: documented_sequence, exceptions: justified_partial_run, notes: deviations_must_be_logged`
