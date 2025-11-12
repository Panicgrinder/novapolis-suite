from __future__ import annotations

from typing import Any

import app.main as app_main
import pytest
from app.main import app
from fastapi.testclient import TestClient


@pytest.mark.api
@pytest.mark.unit
def test_chat_post_endpoint_internal_error(monkeypatch: pytest.MonkeyPatch) -> None:
    # Stubbe process_chat_request damit es einen Fehler wirft
    async def _boom(*args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("kaputt")

    monkeypatch.setattr(app_main, "process_chat_request", _boom)

    client = TestClient(app)
    payload: dict[str, Any] = {
        "messages": [{"role": "user", "content": "hi"}],
    }
    resp = client.post("/chat", json=payload)
    assert resp.status_code == 500
    data = resp.json()
    assert "Interner Serverfehler" in data.get("detail", "")
