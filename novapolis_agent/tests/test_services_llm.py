from __future__ import annotations

import asyncio
from typing import Any, Dict

import pytest


@pytest.mark.unit
def test_generate_reply_success_and_errors(monkeypatch: pytest.MonkeyPatch) -> None:
    import httpx
    from app.services.llm import generate_reply
    from app.api.models import ChatMessage

    class _OKResp:
        status_code = 200
        def raise_for_status(self) -> None:
            return
        def json(self) -> Dict[str, Any]:
            return {"message": {"content": "hi"}}

    class _ErrResp:
        def raise_for_status(self) -> None:
            raise httpx.HTTPStatusError("boom", request=httpx.Request("POST", "http://x"), response=httpx.Response(500))

    class _ClientOK:
        async def __aenter__(self) -> "_ClientOK":
            return self
        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False
        async def post(self, *args: Any, **kwargs: Any):
            return _OKResp()

    class _RespNoJson:
        status_code = 200
        text = "fallback"
        def raise_for_status(self) -> None:
            return
        def json(self) -> Dict[str, Any]:
            raise ValueError("no json")

    class _ClientNoJson:
        async def __aenter__(self) -> "_ClientNoJson":
            return self
        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False
        async def post(self, *args: Any, **kwargs: Any):
            return _RespNoJson()

    class _ClientHTTPError:
        async def __aenter__(self) -> "_ClientHTTPError":
            return self
        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False
        async def post(self, *args: Any, **kwargs: Any):
            return _ErrResp()

    # Success
    def _factory_ok(*a: Any, **k: Any) -> Any:
        return _ClientOK()
    monkeypatch.setattr(httpx, "AsyncClient", _factory_ok)
    ok = asyncio.run(generate_reply([ChatMessage(role="user", content="hi")]))
    assert ok.content == "hi"

    def _factory_no_json(*a: Any, **k: Any) -> Any:
        return _ClientNoJson()

    monkeypatch.setattr(httpx, "AsyncClient", _factory_no_json)
    fallback = asyncio.run(generate_reply([ChatMessage(role="user", content="fallback")]))
    assert fallback.content == "fallback"

    # HTTPStatusError
    def _factory_http_err(*a: Any, **k: Any) -> Any:
        return _ClientHTTPError()
    monkeypatch.setattr(httpx, "AsyncClient", _factory_http_err)
    http_err = asyncio.run(generate_reply([ChatMessage(role="user", content="hi")]))
    assert "HTTP-Fehler" in http_err.content

    # RequestError
    class _ClientReqErr:
        async def __aenter__(self) -> "_ClientReqErr":
            return self
        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False
        async def post(self, *args: Any, **kwargs: Any):
            raise httpx.RequestError("nope")

    def _factory_req_err(*a: Any, **k: Any) -> Any:
        return _ClientReqErr()
    monkeypatch.setattr(httpx, "AsyncClient", _factory_req_err)
    req_err = asyncio.run(generate_reply([ChatMessage(role="user", content="hi")]))
    assert "Verbindung" in req_err.content


@pytest.mark.unit
def test_generate_completion_success(monkeypatch: pytest.MonkeyPatch) -> None:
    import httpx
    from app.services.llm import generate_completion

    class _Resp:
        status_code = 200
        def raise_for_status(self) -> None:
            return
        def json(self) -> Dict[str, Any]:
            return {"response": "done"}

    class _Client:
        async def __aenter__(self) -> "_Client":
            return self
        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False
        async def post(self, *args: Any, **kwargs: Any):
            return _Resp()

    def _factory(*a: Any, **k: Any) -> Any:
        return _Client()
    monkeypatch.setattr(httpx, "AsyncClient", _factory)
    out = asyncio.run(generate_completion("ping", options={"temperature": 0.1}))
    assert out == "done"


@pytest.mark.unit
def test_get_llm_options_parses_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.services.llm import get_llm_options

    monkeypatch.setenv("LLM_NUM_CTX", "1024")
    monkeypatch.setenv("LLM_TEMPERATURE", "0.42")
    opts = get_llm_options()
    assert opts == {"num_ctx": 1024, "temperature": 0.42}

    monkeypatch.setenv("LLM_NUM_CTX", "not-a-number")
    monkeypatch.delenv("LLM_TEMPERATURE", raising=False)
    assert get_llm_options() == {}


@pytest.mark.unit
def test_system_message_helper() -> None:
    from app.services.llm import system_message

    msg = system_message("Hello")
    assert msg.role == "system"
    assert msg.content == "Hello"


@pytest.mark.unit
def test_generate_completion_handles_exception(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    from app.services.llm import generate_completion

    class _Client:
        async def __aenter__(self) -> "_Client":
            return self

        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False

        async def post(self, *args: Any, **kwargs: Any) -> Any:
            raise RuntimeError("fail")

    import httpx

    def _factory(*a: Any, **k: Any) -> Any:
        return _Client()

    monkeypatch.setattr(httpx, "AsyncClient", _factory)
    result = asyncio.run(generate_completion("ping"))
    assert result == ""
    captured = capsys.readouterr()
    assert "fail" in captured.out