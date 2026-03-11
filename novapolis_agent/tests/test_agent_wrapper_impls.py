from __future__ import annotations

import pytest


@pytest.mark.unit
def test_agent_dependency_check_impl_returns_module() -> None:
    import scripts.agent.dependency_check as mod

    impl = mod.impl()
    assert impl.__name__ == "novapolis_agent.scripts.dependency_check"


@pytest.mark.unit
def test_agent_estimate_tokens_impl_returns_module() -> None:
    import scripts.agent.estimate_tokens as mod

    impl = mod.impl()
    assert impl.__name__ == "novapolis_agent.scripts.estimate_tokens"


@pytest.mark.unit
def test_agent_migrate_dataset_schemas_impl_returns_module() -> None:
    import scripts.agent.migrate_dataset_schemas as mod

    impl = mod.impl()
    assert impl.__name__ == "novapolis_agent.scripts.migrate_dataset_schemas"


@pytest.mark.unit
def test_agent_prepare_finetune_pack_impl_returns_module() -> None:
    import scripts.agent.prepare_finetune_pack as mod

    impl = mod.impl()
    assert impl.__name__ == "novapolis_agent.scripts.prepare_finetune_pack"


@pytest.mark.unit
def test_agent_quick_eval_impl_returns_module() -> None:
    import scripts.agent.quick_eval as mod

    impl = mod.impl()
    assert impl.__name__ == "novapolis_agent.scripts.quick_eval"


@pytest.mark.unit
def test_agent_run_eval_impl_returns_module() -> None:
    import scripts.agent.run_eval as mod

    impl = mod.impl()
    assert impl.__name__ == "novapolis_agent.scripts.run_eval"
