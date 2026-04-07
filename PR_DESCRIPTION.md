---
stand: 2026-04-07 10:20
update: PR-Beschreibung beschreibt jetzt konsistent den aktuellen Text-RPG-Branch-Scope mit Orchestrator-, Sim-Live-Client- und Session-Replay-Bruecke.
checks: snapshot-lock PASS (2026-04-07 10:20); markdownlint PASS; frontmatter PASS
---

PR: Text-RPG Slice Scope Sync (2026-04-07)
==========================================

Summary
-------

This branch no longer matches the stale draft title of the active pull request.

The real scope of the current branch is the next Text-RPG product slice across Agent, Sim, and docs:

- local runtime baseline on `Ollama + qwen2.5:7b`,
- session contract and product gate SSOTs,
- opt-in game-master orchestrator on the existing `/chat` and `/chat/stream` path,
- minimal live-session client in the Sim hub,
- file-backed session/replay bridge for `savegame.json`, `world_log.jsonl`, `pc_log.jsonl`, and `replay_manifest.json`.

What Changed
------------

### Agent runtime and orchestrator

- `novapolis_agent/app/core/settings.py` and the environment docs now treat `qwen2.5:7b` as the local 8-GB baseline on top of `Ollama`.
- `novapolis_agent/app/api/models.py` and `novapolis_agent/app/api/chat.py` extend the existing chat path with the current orchestrator fields, including `retrieval_query` and the bundled context/retrieval injection.
- The orchestrator remains on `/chat` and `/chat/stream`; this branch does not add a parallel game-master endpoint.

### Sim live client and session artifacts

- `novapolis-sim/scripts/Main.gd` uses the existing hub chat as a minimal live-session client and sends session/orchestrator fields to `/chat`.
- `novapolis_agent/app/api/sim.py` now persists per-session artifacts under `novapolis_agent/tmp/sim_sessions/<session_id>/`.
- The new session endpoints are:
  - `PUT /session/{session_id}`
  - `GET /session/{session_id}`
  - `GET /session/{session_id}/replay`
- The persisted artifact set is:
  - `savegame.json`
  - `world_log.jsonl`
  - `pc_log.jsonl`
  - `replay_manifest.json`

### Docs and scope cleanup

- `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.index.md`, `novapolis_agent/docs/runbook.md`, `novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`, and `DONELOG.md` were synchronized to the actual Text-RPG slice.
- This file now reflects the current branch scope instead of the outdated stabilization/governance draft text.

Checks
------

- Targeted tests cover the new session bridge and replay manifest paths in:
  - `novapolis_agent/tests/test_api_sim_state.py`
  - `novapolis_agent/tests/tests_sim_api.py`
- Additional targeted Agent tests already cover the orchestrator path in:
  - `novapolis_agent/tests/test_api_chat_internal_branches.py`
  - `novapolis_agent/tests/test_models_chat_options.py`

Risks / Follow-up
-----------------

- The active GitHub draft PR title/body are still stale until they are updated on GitHub itself.
- The new session bridge is intentionally minimal and not yet wired directly into the `/chat` runtime path.
- Scheduler execution, GM eval gates, and session-TTS coupling remain open follow-up work.

