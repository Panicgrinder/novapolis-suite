from __future__ import annotations

from typing import Any

import pytest

from scripts.agent.run_eval import EvaluationItem, evaluate_item


class _DummyResponse:
    def __init__(self, payload: dict[str, Any]) -> None:
        self._payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict[str, Any]:
        return dict(self._payload)


class _DummyClient:
    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    async def post(self, api_url: str, json: dict[str, Any], headers: dict[str, str] | None = None):
        payload = dict(json)
        payload["_api_url"] = api_url
        payload["_headers"] = dict(headers or {})
        self.calls.append(payload)
        return _DummyResponse({"content": "Antwort mit Rechnungsnummer"})


@pytest.mark.asyncio
async def test_evaluate_item_forwards_profile_id_override() -> None:
    item = EvaluationItem(
        id="eval-support-002",
        messages=[{"role": "user", "content": "Bitte frage nach der Rechnungsnummer."}],
        checks={
            "must_include": ["Rechnungsnummer"],
            "keywords_any": [],
            "keywords_at_least": {"count": 0, "items": []},
            "not_include": [],
            "regex": [],
        },
        source_file="support_fixture.jsonl",
        source_package="support_de_ab_core.v1",
        category="support_de",
        tags=["support"],
        slug="support.reply.forward-profile.v1",
    )

    client = _DummyClient()
    result = await evaluate_item(
        item,
        api_url="/chat",
        eval_mode=False,
        client=client,
        enabled_checks=["must_include"],
        profile_id_override="support_de_ab",
    )

    assert result.success is True
    assert client.calls[0]["profile_id"] == "support_de_ab"
    assert client.calls[0]["_api_url"] == "/chat"
