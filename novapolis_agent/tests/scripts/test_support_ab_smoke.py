from __future__ import annotations

from typing import Any

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_build_payload_includes_support_profile_and_optional_judge() -> None:
    from scripts import support_ab_smoke as mod

    payload = mod.build_payload(
        prompt="Bitte helfen Sie kurz.",
        profile_id="support_de_ab",
        candidate_models=["llama3.1:8b", "qwen3.5:4b"],
        judge_model="qwen2.5:7b",
        force_judge=True,
        host_override="http://localhost:11434",
    )

    assert payload["profile_id"] == "support_de_ab"
    assert payload["messages"][0]["content"] == "Bitte helfen Sie kurz."
    assert payload["options"]["support_ab_enabled"] is True
    assert payload["options"]["support_candidate_models"] == ["llama3.1:8b", "qwen3.5:4b"]
    assert payload["options"]["support_judge_model"] == "qwen2.5:7b"
    assert payload["options"]["support_force_judge"] is True
    assert payload["options"]["host"] == "http://localhost:11434"


class _DummyResponse:
    def __init__(self, status_code: int, payload: dict[str, Any]) -> None:
        self.status_code = status_code
        self._payload = payload
        self.headers = {"content-type": "application/json"}

    def json(self) -> dict[str, Any]:
        return dict(self._payload)


class _DummyClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def post(self, api_url: str, json: dict[str, Any]) -> _DummyResponse:
        self.calls.append((api_url, json))
        return _DummyResponse(200, {"model": "llama3.1:8b", "content": "Antwort"})


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_post_support_request_posts_payload_and_parses_json() -> None:
    from scripts import support_ab_smoke as mod

    client = _DummyClient()
    status_code, data = await mod.post_support_request(
        client=client,
        api_url="/chat",
        payload={"profile_id": "support_de_ab", "messages": [{"role": "user", "content": "x"}]},
    )

    assert status_code == 200
    assert data["model"] == "llama3.1:8b"
    assert client.calls == [
        (
            "/chat",
            {"profile_id": "support_de_ab", "messages": [{"role": "user", "content": "x"}]},
        )
    ]