---
stand: 2026-03-03 14:48
update: Follow-up umgesetzt: Root-Asset-Quelle nach Verschiebung ins Sim-Modul wieder entfernt; Doku auf Ist-Zustand aktualisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'PR_DESCRIPTION.md' 'DONELOG.md' PASS (2026-03-03 14:48); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'PR_DESCRIPTION.md' 'DONELOG.md' PASS (EXITCODE=0, 2026-03-03 14:48)
---

PR: Stabilization And Governance Hardening (2026-03-03)
========================================================

Summary
-------

This PR finalizes the Novapolis stabilization and governance hardening run across RP, checks/tooling, docs, and sim UI.

What Changed
------------

### RP: Mind-Cluster governance and validation

- Hardened mind-cluster instruction rules with explicit enums/ranges/taxonomies.
- Extended RP validator with strict checks for:
  - `relation_status` enum
  - `confidence`/`volatility` in `0.0..1.0`
  - `event_id` schema (`evt:<domain>-<seq>`)
  - closed event taxonomy
  - registered `R-MCL-*` / `E-MCL-*` rule-id sets
  - registered `RC-*` reason-code taxonomy
- Migrated existing Novapolis mind-cluster reason codes to registered `RC-*` values.

### Checks/Tooling hardening

- Added naming-policy gate and wired it into consolidated checks.
- Hardened path-portability checker to ignore audit-style `checks:` frontmatter command traces.
- Expanded markdownlint ignore scope for vendor mirror path (`TTS/**`).
- Added workspace search utility and naming-policy checker scripts.
- Cleaned remaining lint/format issues in helper scripts and agent shim files.

### Sim UI and assets

- Added main menu page-1 background asset and scene binding.
- Implemented responsive Hub layout behavior.
- Replaced raw JSON form flow in Agent module with structured dynamic form fields and typed controls.
- Improved agent panel/form layout behavior in exclusive and docked modes.

### Docs and status synchronization

- Updated root/dev/module donelogs and status/todo index docs to reflect completed stabilization milestones.
- Updated portable command snippets in active docs/settings.

Validation
----------

- Consolidated quality run reports `overall=PASS` after stabilization.
- Relevant gates reported green in latest full run: lint/format/type/tests/coverage/frontmatter/naming/path portability.

Notes / Follow-up
-----------------

- The temporary root `assets/` source folder was removed after the asset handover to `novapolis-sim/assets/`.
- Large workspace tree artifacts were refreshed as part of status synchronization.
- Asset provenance note: assets in this change run were generated with GPT.

