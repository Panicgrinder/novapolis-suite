import importlib
import pytest

MODULES = [
    "novapolis_agent.scripts.eval_loader",
    "novapolis_agent.scripts.generate_eval_dataset",
    "novapolis_agent.scripts.train_lora",
    "novapolis_agent.scripts.summarize_eval_results",
    "novapolis_agent.scripts.openai_finetune",
    "novapolis_agent.scripts.fix_donelog_times",
    "novapolis_agent.scripts.rag_indexer",
    "novapolis_agent.scripts.syn_loader",
    "novapolis_agent.test_settings",
    "novapolis_agent.scripts.openai_ft_status",
]


@pytest.mark.parametrize("mod_name", MODULES)
def test_smoke_imports_batch5(mod_name):
    """Smoke-import next set of heavy modules to verify import-safety.

    Keep tests minimal and side-effect-free; importing may execute module
    top-level but these modules are designed to be import-safe in the test
    environment used previously.
    """
    m = importlib.import_module(mod_name)
    assert m is not None
