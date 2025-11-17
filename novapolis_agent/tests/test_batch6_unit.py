import importlib

import pytest

MODULES = [
    "novapolis_agent.app.api.chat",
    "novapolis_agent.utils.eval_utils",
    "novapolis_agent.utils.context_notes",
    "novapolis_agent.scripts.eval_loader",
    "novapolis_agent.scripts.summarize_eval_results",
    "novapolis_agent.scripts.train_lora",
    "novapolis_agent.scripts.generate_eval_dataset",
    "novapolis_agent.test_settings",
    "novapolis_agent.scripts.fix_donelog_times",
    "novapolis_agent.scripts.syn_loader",
]


@pytest.mark.parametrize("mod_name", MODULES)
def test_smoke_imports_batch6(mod_name):
    """Smoke-import next 10 modules to ensure import-time safety.

    These tests are intentionally minimal to avoid side-effects; they only
    assert the module can be imported in the test environment.
    """
    m = importlib.import_module(mod_name)
    assert m is not None
