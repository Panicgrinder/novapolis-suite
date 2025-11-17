import importlib

import pytest

MODULES = [
    "novapolis_agent.app.api.chat",
    "novapolis_agent.scripts.run_eval",
    "novapolis_agent.scripts.eval_ui",
    "novapolis_agent.utils.eval_utils",
    "novapolis_agent.utils.context_notes",
    "novapolis_agent.scripts.curate_dataset_from_latest",
    "novapolis_agent.scripts.map_reduce_summary_llm",
    "novapolis_agent.scripts.dependency_check",
    "novapolis_agent.scripts.export_finetune",
    "novapolis_agent.scripts.prepare_finetune_pack",
]


@pytest.mark.parametrize("mod_name", MODULES)
def test_smoke_imports(mod_name):
    """Smoke-import each target module to ensure import-time codepaths are import-safe.

    These are minimal, side-effect-light checks: they only assert the module
    imports without raising an exception.
    """
    m = importlib.import_module(mod_name)
    assert m is not None
