from __future__ import annotations

import importlib

import pytest

from scripts.agent.run_eval import EvaluationItem, run_evaluation


@pytest.mark.asyncio
async def test_run_evaluation_keeps_case_metadata(monkeypatch: pytest.MonkeyPatch) -> None:
    item = EvaluationItem(
        id="eval-gm-201",
        messages=[
            {
                "role": "user",
                "content": "Antworte exakt mit Szene:, Konsequenz:, Optionen:, State_Patches:.",
            }
        ],
        checks={
            "must_include": ["Szene:", "Konsequenz:", "Optionen:", "State_Patches:"],
            "keywords_any": [],
            "keywords_at_least": {"count": 0, "items": []},
            "not_include": [],
            "regex": [],
        },
        source_file="gm_fixture.jsonl",
        source_package="rpg_gm_session_core.v1",
        category="gm_session",
        tags=["gm", "blocker", "continuity"],
        slug="gm.session.continuity.v1",
    )

    async def _fake_loader(_patterns):
        return [item]

    runner = importlib.import_module("novapolis_agent.scripts.run_eval")

    monkeypatch.setattr(runner, "load_evaluation_items", _fake_loader)

    results = await run_evaluation(
        patterns=["dummy"],
        api_url="http://localhost:8000/chat",
        eval_mode=False,
        asgi=True,
        enabled_checks=["must_include"],
        quiet=True,
        retries=0,
        use_cache=False,
    )

    assert len(results) == 1
    result = results[0]
    assert result.slug == "gm.session.continuity.v1"
    assert result.category == "gm_session"
    assert result.tags == ["gm", "blocker", "continuity"]
