from __future__ import annotations

import pytest


@pytest.mark.unit
def test_api_router_module_exists() -> None:
    from app.api import api

    assert hasattr(api, "api_router")


@pytest.mark.unit
def test_prompt_package_exposes_all() -> None:
    from app import prompt

    assert prompt.__all__ == []


@pytest.mark.unit
def test_router_package_is_removed() -> None:
    import importlib

    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("app.routers")
