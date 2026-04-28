from __future__ import annotations

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_guard_allows_non_runtime_mutation() -> None:
    from scripts import rp_runtime_loop_guard as mod

    payload = {
        "toolName": "functions.apply_patch",
        "toolInput": {"input": "*** Begin Patch\n*** Update File: README.md\n*** End Patch"},
        "userPrompt": "Bitte README anpassen.",
    }

    result = mod.evaluate(payload)

    assert result["hookSpecificOutput"]["permissionDecision"] == "allow"


@pytest.mark.scripts
@pytest.mark.unit
def test_guard_asks_without_workflow_anchor_for_runtime_edit() -> None:
    from scripts import rp_runtime_loop_guard as mod

    payload = {
        "toolName": "functions.apply_patch",
        "toolInput": {
            "input": (
                "*** Begin Patch\n"
                "*** Update File: "
                "novapolis-rp/database-curated/staging/rp-runtime/state/nordlinie-01.md\n"
                "*** End Patch"
            )
        },
        "userPrompt": "Bitte das nachziehen.",
    }

    result = mod.evaluate(payload)

    assert result["hookSpecificOutput"]["permissionDecision"] == "ask"


@pytest.mark.scripts
@pytest.mark.unit
def test_guard_denies_new_turn_after_admin_fix_without_release() -> None:
    from scripts import rp_runtime_loop_guard as mod

    payload = {
        "toolName": "functions.apply_patch",
        "toolInput": {
            "input": (
                "*** Begin Patch\n"
                "*** Update File: "
                "novapolis-rp/database-curated/staging/rp-runtime/sessions/demo/scene-log.md\n"
                "+Turn 8\n"
                "*** End Patch"
            )
        },
        "userPrompt": "Admin-Rueckmeldung: fixe Turn 7 bitte noch einmal.",
    }

    result = mod.evaluate(payload)

    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert (
        "ohne ausdrueckliche Freigabe" in result["hookSpecificOutput"]["permissionDecisionReason"]
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_guard_allows_new_turn_with_explicit_release() -> None:
    from scripts import rp_runtime_loop_guard as mod

    payload = {
        "toolName": "functions.apply_patch",
        "toolInput": {
            "input": (
                "*** Begin Patch\n"
                "*** Update File: "
                "novapolis-rp/database-curated/staging/rp-runtime/sessions/demo/scene-log.md\n"
                "+Turn 8\n"
                "*** End Patch"
            )
        },
        "userPrompt": "Admin-Freigabe liegt vor, spiele den naechsten Turn aus.",
    }

    result = mod.evaluate(payload)

    assert result["hookSpecificOutput"]["permissionDecision"] == "allow"
