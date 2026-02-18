---
description: Regeln für CI-Workflows, Release-Gates, Versionierung und wirksame Workflow-Pfade.
name: CI Release Instructions
applyTo: .github/workflows/**/*.yml,.github/workflows/**/*.yaml,pyproject.toml,requirements*.txt,PR_DESCRIPTION.md
---

CI & Release
============

Ziel
----
- Reproduzierbare Releases nur bei grünen Gates.

Regeln
------
- Wirksam sind nur Workflows unter `.github/workflows/` am Repo-Root.
- Release nur mit grünen Checks (Tests, Typen, Coverage, Frontmatter-Validator, Markdownlint bei Docs).
- Versionierung über `pyproject.toml`; Versionssprung + Tag `vX.Y.Z` in derselben PR.
- DONELOG-Updates zu Release-/Policy-Änderungen verpflichtend.

Regelmatrix
-----------
- `id: R-CI-PATH, priority: 1, scope: ci, trigger: workflow_change, action: use_root_github_workflows_only, validation: no_effective_mirror_workflows, exceptions: archival_stubs, notes: verify_references_before_cleanup`
- `id: R-REL-GATES, priority: 1, scope: release, trigger: release_or_merge_gate, action: require_all_quality_gates_green, validation: checks_pass_before_release, exceptions: explicit_stop_approved_override, notes: include_docs_gates_when_docs_touched`
- `id: R-VERSION, priority: 2, scope: release, trigger: version_bump, action: bump_in_pyproject_and_tag, validation: tag_matches_version, exceptions: none, notes: update_donelog`
