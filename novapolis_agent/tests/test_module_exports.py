from __future__ import annotations

import pytest


@pytest.mark.unit
def test_api_router_module_exists() -> None:
    import importlib

    # The legacy router module was archived; importing should raise ModuleNotFoundError
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("app.api.api")


@pytest.mark.unit
def test_prompt_package_exposes_all() -> None:
    import importlib

    # Prompts were moved to archive; importing the legacy package should fail
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("app.prompt")


@pytest.mark.unit
def test_router_package_is_removed() -> None:
    import importlib

    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("app.routers")
