import unittest
from typing import Any, cast
from unittest.mock import patch

import pytest
from app.api.chat import process_chat_request
from app.api.models import ChatRequest
from app.core.prompts import (
    DEFAULT_SYSTEM_PROMPT,
    EVAL_SYSTEM_PROMPT,
    UNRESTRICTED_SYSTEM_PROMPT,
)


class ResponseStub:
    status_code = 200

    def raise_for_status(self):
        return None

    def json(self):
        return {"message": {"content": "OK"}}


class FakeClient:
    def __init__(self, *args, **kwargs):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return None

    async def post(self, url, json, headers=None):
        return ResponseStub()


@pytest.mark.unit
@pytest.mark.eval
class TestPromptModes(unittest.IsolatedAsyncioTestCase):
    async def _capture_messages(
        self, req: ChatRequest, **kwargs: Any
    ) -> tuple[list[dict[str, Any]], dict[str, Any]]:
        sent_payload: dict[str, Any] = {}

        class CaptureClient(FakeClient):
            async def post(self, url, json, headers=None):
                nonlocal sent_payload
                sent_payload = cast(dict[str, Any], json)
                return ResponseStub()

        with patch("app.api.chat.httpx.AsyncClient", CaptureClient):
            await process_chat_request(req, **kwargs)
        msgs = cast(list[dict[str, Any]], sent_payload.get("messages") or [])
        return msgs, sent_payload

    async def test_default_inserts_default_system_prompt(self):
        req = ChatRequest(messages=[{"role": "user", "content": "Hallo"}])
        messages, _ = await self._capture_messages(req, eval_mode=False, unrestricted_mode=False)
        assert messages and isinstance(messages, list)
        assert messages[0]["role"] == "system"
        assert str(messages[0]["content"]).strip() == DEFAULT_SYSTEM_PROMPT.strip()
        assert str(messages[-1]["content"]).find("Hallo") >= 0

    async def test_unrestricted_overrides_system_prompt(self):
        req = ChatRequest(
            messages=[{"role": "system", "content": "ALT"}, {"role": "user", "content": "Ping"}]
        )
        messages, _ = await self._capture_messages(req, eval_mode=False, unrestricted_mode=True)
        assert messages and messages[0]["role"] == "system"
        assert str(messages[0]["content"]).strip() == UNRESTRICTED_SYSTEM_PROMPT.strip()
        typed_msgs = [cast(dict[str, Any], m) for m in messages]
        assert all(m.get("content") != "ALT" for m in typed_msgs)

    async def test_eval_overrides_system_prompt(self):
        req = ChatRequest(
            messages=[{"role": "system", "content": "ALT"}, {"role": "user", "content": "DNS"}]
        )
        messages, _ = await self._capture_messages(req, eval_mode=True, unrestricted_mode=False)
        assert messages and messages[0]["role"] == "system"
        assert str(messages[0]["content"]).strip() == EVAL_SYSTEM_PROMPT.strip()
        typed_msgs2 = [cast(dict[str, Any], m) for m in messages]
        assert all(m.get("content") != "ALT" for m in typed_msgs2)
