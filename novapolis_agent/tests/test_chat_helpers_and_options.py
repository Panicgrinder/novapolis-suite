from __future__ import annotations

import importlib
import asyncio
from typing import Any, Iterable

import pytest

from app.api.models import ChatRequest


@pytest.mark.unit
def test_chat_helpers_insert_system_prompt(monkeypatch: pytest.MonkeyPatch) -> None:
    # ensure_system_message fügt system-turn hinzu, falls keiner existiert
    from app.api.chat_helpers import ensure_system_message, get_system_prompt
    from app.api.models import ChatMessage

    messages = [ChatMessage(role="user", content="hi")]  # kein system
    res = ensure_system_message(messages)
    assert res[0].role == "system"
    assert isinstance(get_system_prompt(), str) and len(get_system_prompt()) > 0


@pytest.mark.unit
@pytest.mark.api
def test_process_chat_ignores_invalid_top_p(monkeypatch: pytest.MonkeyPatch) -> None:
    # top_p als nicht-floatbarer String -> soll ignoriert werden (None)
    import app.api.chat as chat_module
    import httpx

    captured_payload: dict[str, Any] = {}

    class _Resp:
        status_code = 200
        def raise_for_status(self) -> None:
            return
        def json(self) -> dict[str, Any]:
            return {"message": {"content": "ok"}}

    class _Client:
        async def __aenter__(self):
            return self
        async def __aexit__(self, exc_type, exc, tb):
            return False
        async def post(self, url, json, headers):
            captured_payload.update(json)
            return _Resp()

    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    importlib.reload(importlib.import_module("app.core.settings"))
    monkeypatch.setattr(chat_module.httpx, "AsyncClient", lambda *a, **k: _Client())

    req = ChatRequest(messages=[{"role": "user", "content": "hi"}], options={"top_p": "not-a-number"})
    res = asyncio.run(chat_module.process_chat_request(req))
    assert res.content == "ok"
    # options.top_p sollte nicht gesetzt sein
    opts = captured_payload.get("options", {})
    assert "top_p" not in opts


@pytest.mark.unit
@pytest.mark.api
def test_process_chat_uses_host_override(monkeypatch: pytest.MonkeyPatch) -> None:
    # host-Override in options soll URL beeinflussen
    import app.api.chat as chat_module
    import httpx

    seen_url: list[str] = []

    class _Resp:
        status_code = 200
        def raise_for_status(self) -> None:
            return
        def json(self) -> dict[str, Any]:
            return {"message": {"content": "ok"}}

    class _Client:
        async def __aenter__(self):
            return self
        async def __aexit__(self, exc_type, exc, tb):
            return False
        async def post(self, url, json, headers):
            seen_url.append(url)
            return _Resp()

    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    importlib.reload(importlib.import_module("app.core.settings"))
    monkeypatch.setattr(chat_module.httpx, "AsyncClient", lambda *a, **k: _Client())

    req = ChatRequest(messages=[{"role": "user", "content": "hi"}], options={"host": "http://override:1234"})
    res = asyncio.run(chat_module.process_chat_request(req))
    assert res.content == "ok"
    assert any(u.startswith("http://override:1234") for u in seen_url)


@pytest.mark.unit
@pytest.mark.api
def test_num_predict_invalid_string_clamps(monkeypatch: pytest.MonkeyPatch) -> None:
    import app.api.chat as chat_module
    import httpx
    from app.core.settings import settings

    captured_opts: dict[str, Any] = {}

    class _Resp:
        status_code = 200
        def raise_for_status(self) -> None:
            return
        def json(self) -> dict[str, Any]:
            return {"message": {"content": "ok"}}

    class _Client:
        async def __aenter__(self):
            return self
        async def __aexit__(self, exc_type, exc, tb):
            return False
        async def post(self, url, json, headers):
            captured_opts.update(json.get("options", {}))
            return _Resp()

    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    importlib.reload(importlib.import_module("app.core.settings"))
    monkeypatch.setattr(chat_module.httpx, "AsyncClient", lambda *a, **k: _Client())

    req = ChatRequest(messages=[{"role": "user", "content": "hi"}], options={"num_predict": "NaN"})
    res = asyncio.run(chat_module.process_chat_request(req))
    assert res.content == "ok"
    # sollte auf REQUEST_MAX_TOKENS gedeckelt sein; wenn parsing fehlschlägt, nutzt der Code REQUEST_MAX_TOKENS und clamped min 1
    assert 1 <= int(captured_opts.get("num_predict", 0)) <= settings.REQUEST_MAX_TOKENS


@pytest.mark.unit
@pytest.mark.streaming
def test_stream_injects_eval_or_unrestricted_system_prompt(monkeypatch: pytest.MonkeyPatch) -> None:
    import app.api.chat as chat_module
    import httpx, json

    captured_payloads: list[dict[str, Any]] = []

    class _Resp:
        status_code = 200
        def raise_for_status(self) -> None:
            return
        async def aiter_lines(self):
            # eine leere Antwort + done
            yield json.dumps({"message": {"content": ""}})
            yield json.dumps({"done": True})

    class _CM:
        async def __aenter__(self):
            return _Resp()
        async def __aexit__(self, exc_type, exc, tb):
            return False

    class _Client:
        async def __aenter__(self):
            return self
        async def __aexit__(self, exc_type, exc, tb):
            return False
        def stream(self, *args: Any, **kwargs: Any):
            # args[1] ist die URL, kwargs["json"] ist Payload
            captured_payloads.append(kwargs.get("json") or {})
            return _CM()

    monkeypatch.setattr(chat_module.httpx, "AsyncClient", lambda *a, **k: _Client())

    # eval_mode: True
    req = ChatRequest(messages=[{"role": "user", "content": "hi"}])
    agen = asyncio.run(chat_module.stream_chat_request(req, eval_mode=True))
    asyncio.run(_consume_all(agen))

    # unrestricted_mode: True
    agen2 = asyncio.run(chat_module.stream_chat_request(req, unrestricted_mode=True))
    asyncio.run(_consume_all(agen2))

    # Prüfen, dass jeweils system prompt am Index 0 entsprechend ersetzt wurde
    assert len(captured_payloads) >= 2
    msgs_eval = captured_payloads[0].get("messages", [])
    msgs_unres = captured_payloads[1].get("messages", [])
    assert msgs_eval and msgs_eval[0].get("role") == "system"
    assert msgs_unres and msgs_unres[0].get("role") == "system"


async def _consume_all(agen: Any) -> None:
    async for _ in agen:
        pass


@pytest.mark.unit
def test_normalize_ollama_options_comprehensive(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat_helpers
    from types import SimpleNamespace

    monkeypatch.setattr(
        chat_helpers,
        "settings",
        SimpleNamespace(
            TEMPERATURE=0.8,
            REQUEST_MAX_TOKENS=128,
            TOP_P=0.9,
            TOP_K=40,
            NUM_CTX_DEFAULT=1024,
            REPEAT_PENALTY=1.1,
            MIN_P=0.0,
            TYPICAL_P=0.8,
            TFS_Z=0.5,
            MIROSTAT=1,
            MIROSTAT_TAU=5.0,
            MIROSTAT_ETA=0.1,
            PENALIZE_NEWLINE=False,
            REPEAT_LAST_N=64,
            OLLAMA_HOST="http://ollama.local",
        ),
        raising=False,
    )

    raw = {
        "temperature": "0.6",
        "num_predict": "256",
        "top_p": 1.5,
        "top_k": "12",
        "num_ctx": 2048,
        "repeat_penalty": "1.3",
        "presence_penalty": "0.2",
        "frequency_penalty": "0.4",
        "seed": "123",
        "repeat_last_n": 32,
        "stop": "END",
        "min_p": -0.5,
        "typical_p": 1.5,
        "tfs_z": 2.0,
        "mirostat": 5,
        "mirostat_tau": "3.5",
        "mirostat_eta": "0.6",
        "penalize_newline": "on",
        "host": "http://custom",
    }

    options, host = chat_helpers.normalize_ollama_options(raw, eval_mode=True)
    assert host == "http://custom"
    assert 0.0 <= options["temperature"] <= 0.25  # clamped for eval_mode
    assert options["num_predict"] == 128  # clamped to max tokens
    assert options["top_p"] == 1.0
    assert options["top_k"] == 12
    assert options["num_ctx"] == 2048
    assert options["repeat_penalty"] == 1.3
    assert options["presence_penalty"] == 0.2
    assert options["frequency_penalty"] == 0.4
    assert options["seed"] == 123
    assert options["repeat_last_n"] == 32
    assert options["stop"] == ["END"]
    assert options["min_p"] == 0.0
    assert options["typical_p"] == 1.0
    assert options["tfs_z"] == 1.0
    assert options["mirostat"] == 2
    assert options["mirostat_tau"] == 3.5
    assert options["mirostat_eta"] == 0.6
    assert options["penalize_newline"] is True


@pytest.mark.unit
def test_chat_helper_coercers_handle_invalid_inputs() -> None:
    from app.api import chat_helpers

    assert chat_helpers._coerce_float(object()) is None
    assert chat_helpers._coerce_int(object()) is None
    assert chat_helpers._coerce_str_list(42) is None
    assert chat_helpers._coerce_str_list(["a", 1, None]) == ["a", "1", "None"]
    assert chat_helpers._coerce_bool("off") is False
    assert chat_helpers._coerce_bool(0) is False
    assert chat_helpers._coerce_bool(1) is True
    assert chat_helpers._coerce_bool("maybe") is None
