---
description: Regeln für novapolis_agent Backend-Code, Tests, Typprüfungen, API/Streaming-Konventionen.
name: Agent Backend Instructions
applyTo: novapolis_agent/app/**/*.py,novapolis_agent/tests/**/*.py,novapolis_agent/utils/**/*.py,novapolis_agent/run_server.py
---

Agent Backend
=============

Ziel
----
- Stabiler Backend-Workflow mit grünen Gates und konsistenter API-/SSE-Qualität.

Gates
-----
- Tests: `pytest -q` (oder selektiv per Marker).
- Typen: `pyright -p pyrightconfig.json` und `python -m mypy --config-file mypy.ini app scripts`.
- Coverage: Mindest-Gate einhalten.

Konventionen
-----------
- Modelle über `app/api/models.py` referenzieren.
- Streaming/SSE-Events konsistent (`meta`, `delta`, `done`).
- Rate-Limit-/Header-Verhalten testbar und reproduzierbar halten.
- Änderungen an `app/`, `scripts/`, `utils/` in `novapolis_agent/docs/DONELOG.txt` dokumentieren.

Regelmatrix
-----------
- `id: R-AGENT-GATES, priority: 1, scope: novapolis_agent, trigger: backend_change, action: run_tests_and_types, validation: pytest_pyright_mypy_green, exceptions: stop_approved_partial_run, notes: keep_ci_green`
- `id: R-AGENT-SSE, priority: 2, scope: streaming, trigger: stream_related_change, action: preserve_event_contract, validation: tests_expect_meta_delta_done, exceptions: none, notes: policy_post_and_text_fields_consistent`
- `id: R-AGENT-DONELOG, priority: 1, scope: docs_traceability, trigger: app_scripts_utils_change, action: append_agent_donelog_entry, validation: donelog_entry_present, exceptions: explicit_skip_rule, notes: include_context`
