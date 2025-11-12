from __future__ import annotations

import importlib

import pytest
from fastapi.testclient import TestClient


@pytest.mark.api
@pytest.mark.unit
def test_root_endpoint_message_exact() -> None:
    app_mod = importlib.import_module("app.main")
    client = TestClient(app_mod.app)
    r = client.get("/")
    assert r.status_code == 200
    data = r.json()
    assert data.get("message") == "CVN Agent API ist aktiv"
