from __future__ import annotations

import argparse
import contextlib
import json
from typing import Any

import httpx
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
    def __init__(
        self,
        status_code: int,
        payload: Any,
        *,
        content_type: str = "application/json",
        raises_json: bool = False,
    ) -> None:
        self.status_code = status_code
        self._payload = payload
        self._raises_json = raises_json
        self.headers = {"content-type": content_type}

    def json(self) -> Any:
        if self._raises_json:
            raise ValueError("broken json")
        return self._payload


class _DummyClient:
    def __init__(self, response: _DummyResponse | None = None) -> None:
        self.calls: list[tuple[str, dict[str, Any]]] = []
        self._response = response or _DummyResponse(
            200,
            {"model": "llama3.1:8b", "content": "Antwort"},
        )

    async def post(self, api_url: str, json: dict[str, Any]) -> _DummyResponse:
        self.calls.append((api_url, json))
        return self._response


class _AsyncClientFactory:
    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    def __call__(self, **kwargs: Any) -> contextlib.AbstractAsyncContextManager[_DummyClient]:
        self.calls.append(dict(kwargs))

        @contextlib.asynccontextmanager
        async def _manager() -> Any:
            yield _DummyClient()

        return _manager()


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


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_post_support_request_rejects_non_json_content_type() -> None:
    from scripts import support_ab_smoke as mod

    client = _DummyClient(
        _DummyResponse(200, {"model": "x", "content": "y"}, content_type="text/plain")
    )

    with pytest.raises(RuntimeError, match="unexpected content-type"):
        await mod.post_support_request(
            client=client,
            api_url="/chat",
            payload={"profile_id": "support_de_ab", "messages": [{"role": "user", "content": "x"}]},
        )


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_post_support_request_rejects_non_object_json() -> None:
    from scripts import support_ab_smoke as mod

    client = _DummyClient(_DummyResponse(200, ["not", "an", "object"]))

    with pytest.raises(RuntimeError, match="response JSON must be an object"):
        await mod.post_support_request(
            client=client,
            api_url="/chat",
            payload={"profile_id": "support_de_ab", "messages": [{"role": "user", "content": "x"}]},
        )


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_post_support_request_rejects_invalid_json_body() -> None:
    from scripts import support_ab_smoke as mod

    client = _DummyClient(_DummyResponse(200, None, raises_json=True))

    with pytest.raises(RuntimeError, match="response body is not valid JSON"):
        await mod.post_support_request(
            client=client,
            api_url="/chat",
            payload={"profile_id": "support_de_ab", "messages": [{"role": "user", "content": "x"}]},
        )


def _make_args(**overrides: Any) -> argparse.Namespace:
    defaults = {
        "api_url": "http://localhost:8000/chat",
        "asgi": False,
        "prompt": "Bitte helfen Sie kurz.",
        "profile_id": "support_de_ab",
        "candidate_model": [],
        "judge_model": None,
        "force_judge": False,
        "host": None,
        "timeout": 180.0,
    }
    defaults.update(overrides)
    return argparse.Namespace(**defaults)


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_run_support_smoke_returns_success_and_prints_json(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import support_ab_smoke as mod

    factory = _AsyncClientFactory()

    async def fake_post_support_request(
        *, client: Any, api_url: str, payload: dict[str, Any]
    ) -> tuple[int, dict[str, Any]]:
        assert api_url == "http://localhost:8000/chat"
        assert payload["profile_id"] == "support_de_ab"
        return 200, {"model": "llama3.1:8b", "content": "Versandfaehige Antwort"}

    monkeypatch.setattr(mod.httpx, "AsyncClient", factory)
    monkeypatch.setattr(mod, "post_support_request", fake_post_support_request)

    rc = await mod.run_support_smoke(_make_args())

    output = json.loads(capsys.readouterr().out)
    assert rc == mod.EXIT_SUCCESS
    assert output["status"] == "ok"
    assert output["selected_model"] == "llama3.1:8b"
    assert factory.calls == [{"timeout": 180.0}]


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_run_support_smoke_returns_http_error_with_detail(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import support_ab_smoke as mod

    factory = _AsyncClientFactory()

    async def fake_post_support_request(
        *, client: Any, api_url: str, payload: dict[str, Any]
    ) -> tuple[int, dict[str, Any]]:
        return 503, {"detail": "upstream unavailable", "model": "", "content": ""}

    monkeypatch.setattr(mod.httpx, "AsyncClient", factory)
    monkeypatch.setattr(mod, "post_support_request", fake_post_support_request)

    rc = await mod.run_support_smoke(_make_args())

    output = json.loads(capsys.readouterr().out)
    assert rc == mod.EXIT_HTTP_ERROR
    assert output["status"] == "http_error"
    assert output["error"] == "upstream unavailable"


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_run_support_smoke_returns_payload_error_for_missing_fields(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import support_ab_smoke as mod

    factory = _AsyncClientFactory()

    async def fake_post_support_request(
        *, client: Any, api_url: str, payload: dict[str, Any]
    ) -> tuple[int, dict[str, Any]]:
        return 200, {"model": "", "content": "   "}

    monkeypatch.setattr(mod.httpx, "AsyncClient", factory)
    monkeypatch.setattr(mod, "post_support_request", fake_post_support_request)

    rc = await mod.run_support_smoke(_make_args(judge_model="qwen2.5:7b"))

    output = json.loads(capsys.readouterr().out)
    assert rc == mod.EXIT_PAYLOAD_ERROR
    assert output["status"] == "payload_error"
    assert output["used_judge"] is True


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_run_support_smoke_returns_payload_error_for_runtime_parse_error(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import support_ab_smoke as mod

    factory = _AsyncClientFactory()

    async def fake_post_support_request(
        *, client: Any, api_url: str, payload: dict[str, Any]
    ) -> tuple[int, dict[str, Any]]:
        raise RuntimeError("unexpected content-type")

    monkeypatch.setattr(mod.httpx, "AsyncClient", factory)
    monkeypatch.setattr(mod, "post_support_request", fake_post_support_request)

    rc = await mod.run_support_smoke(_make_args())

    output = json.loads(capsys.readouterr().out)
    assert rc == mod.EXIT_PAYLOAD_ERROR
    assert output["status"] == "payload_error"
    assert output["error"] == "unexpected content-type"


@pytest.mark.asyncio
@pytest.mark.scripts
async def test_run_support_smoke_returns_network_error(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import support_ab_smoke as mod

    factory = _AsyncClientFactory()

    async def fake_post_support_request(
        *, client: Any, api_url: str, payload: dict[str, Any]
    ) -> tuple[int, dict[str, Any]]:
        request = httpx.Request("POST", api_url)
        raise httpx.ConnectError("connection refused", request=request)

    monkeypatch.setattr(mod.httpx, "AsyncClient", factory)
    monkeypatch.setattr(mod, "post_support_request", fake_post_support_request)

    rc = await mod.run_support_smoke(_make_args())

    output = json.loads(capsys.readouterr().out)
    assert rc == mod.EXIT_NETWORK_ERROR
    assert output["status"] == "network_error"
    assert "connection refused" in output["error"]


@pytest.mark.scripts
@pytest.mark.unit
def test_parse_args_supports_asgi_and_optional_flags() -> None:
    from scripts import support_ab_smoke as mod

    args = mod.parse_args(
        [
            "--asgi",
            "--candidate-model",
            "llama3.1:8b",
            "--candidate-model",
            "qwen3.5:4b",
            "--judge-model",
            "qwen2.5:7b",
            "--force-judge",
            "--host",
            "http://localhost:11434",
            "--timeout",
            "12",
        ]
    )

    assert args.asgi is True
    assert args.candidate_model == ["llama3.1:8b", "qwen3.5:4b"]
    assert args.judge_model == "qwen2.5:7b"
    assert args.force_judge is True
    assert args.host == "http://localhost:11434"
    assert args.timeout == 12.0


@pytest.mark.scripts
@pytest.mark.unit
def test_main_passes_parsed_args_to_async_runner(monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import support_ab_smoke as mod

    seen: dict[str, Any] = {}

    async def fake_run_support_smoke(args: argparse.Namespace) -> int:
        seen["profile_id"] = args.profile_id
        seen["force_judge"] = args.force_judge
        return 7

    monkeypatch.setattr(mod, "run_support_smoke", fake_run_support_smoke)

    rc = mod.main(["--profile-id", "support_de_ab", "--force-judge"])

    assert rc == 7
    assert seen == {"profile_id": "support_de_ab", "force_judge": True}
