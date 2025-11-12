from __future__ import annotations

from typing import Any

import pytest
from app.main import app
from fastapi.testclient import TestClient


@pytest.mark.api
@pytest.mark.unit
def test_health_endpoint_returns_ok() -> None:
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    data: dict[str, Any] = resp.json()
    assert isinstance(data, dict)
    assert data.get("status") == "ok"
