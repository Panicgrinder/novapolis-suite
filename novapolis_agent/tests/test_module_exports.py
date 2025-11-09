from __future__ import annotations

import pytest


@pytest.mark.unit
def test_api_router_module_exists() -> None:
    from app.api import api

    assert hasattr(api, "api_router")


@pytest.mark.unit
def test_prompt_and_router_packages_expose_all() -> None:
    from app import prompt
    from app import routers

    assert prompt.__all__ == []
    assert routers.__all__ == []
