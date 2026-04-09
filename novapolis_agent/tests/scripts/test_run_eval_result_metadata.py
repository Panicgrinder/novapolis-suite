from __future__ import annotations

import importlib
import json
from pathlib import Path

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


@pytest.mark.asyncio
async def test_run_evaluation_meta_header_prefers_model_override(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    runner = importlib.import_module("novapolis_agent.scripts.run_eval")

    item = EvaluationItem(
        id="eval-gm-202",
        messages=[{"role": "user", "content": "Antwort."}],
        checks={
            "must_include": [],
            "keywords_any": [],
            "keywords_at_least": {"count": 0, "items": []},
            "not_include": [],
            "regex": [],
        },
        source_file="gm_fixture.jsonl",
        source_package="rpg_gm_session_core.v1",
        category="gm_session",
        tags=["gm"],
        slug="gm.session.override-metadata.v1",
    )

    async def _fake_loader(_patterns):
        return [item]

    async def _fake_evaluate_item(*_args, **_kwargs):
        return runner.EvaluationResult(
            item_id=item.id,
            response="ok",
            checks_passed={"must_include": True},
            success=True,
            failed_checks=[],
            source_file=item.source_file,
            source_package=item.source_package,
            slug=item.slug,
            category=item.category,
            tags=list(item.tags),
            duration_ms=1,
        )

    monkeypatch.setattr(runner, "load_evaluation_items", _fake_loader)
    monkeypatch.setattr(runner, "evaluate_item", _fake_evaluate_item)
    monkeypatch.setattr(runner, "DEFAULT_RESULTS_DIR", str(tmp_path))
    monkeypatch.setattr(runner, "now_compact", lambda: "20260409_004000")

    await run_evaluation(
        patterns=["dummy"],
        api_url="http://localhost:8000/chat",
        eval_mode=False,
        asgi=False,
        enabled_checks=["must_include"],
        model_override="llama3.1:8b",
        quiet=True,
        retries=0,
        use_cache=False,
    )

    rows = (tmp_path / "results_20260409_004000.jsonl").read_text(encoding="utf-8").splitlines()
    meta = json.loads(rows[0])

    assert meta["model"] == "llama3.1:8b"
    assert meta["overrides"]["model"] == "llama3.1:8b"
