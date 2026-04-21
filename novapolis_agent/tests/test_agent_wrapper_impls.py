from __future__ import annotations

import importlib
import types

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


@pytest.mark.unit
@pytest.mark.parametrize(
    ("module_name", "impl_name"),
    [
        (
            "scripts.agent.build_session_promotion_pack",
            "novapolis_agent.scripts.build_session_promotion_pack",
        ),
        (
            "scripts.agent.build_training_from_rp",
            "novapolis_agent.scripts.build_training_from_rp",
        ),
        ("scripts.agent.export_finetune", "novapolis_agent.scripts.export_finetune"),
        (
            "scripts.agent.fine_tune_pipeline",
            "novapolis_agent.scripts.fine_tune_pipeline",
        ),
        ("scripts.agent.rerun_failed", "novapolis_agent.scripts.rerun_failed"),
        (
            "scripts.agent.rerun_from_results",
            "novapolis_agent.scripts.rerun_from_results",
        ),
        ("scripts.agent.train_lora", "novapolis_agent.scripts.train_lora"),
    ],
)
def test_agent_extra_wrappers_impl_returns_module(module_name: str, impl_name: str) -> None:
    mod = importlib.import_module(module_name)

    impl = mod.impl()
    assert impl.__name__ == impl_name


@pytest.mark.unit
@pytest.mark.parametrize(
    "module_name",
    [
        "scripts.agent.build_session_promotion_pack",
        "scripts.agent.build_training_from_rp",
        "scripts.agent.export_finetune",
        "scripts.agent.fine_tune_pipeline",
        "scripts.agent.rerun_failed",
        "scripts.agent.rerun_from_results",
        "scripts.agent.train_lora",
    ],
)
def test_agent_extra_wrappers_proxy_attributes_and_main_paths(
    module_name: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    mod = importlib.import_module(module_name)
    calls: list[tuple[str, list[str]]] = []

    fake_impl = types.SimpleNamespace(main=lambda: 7, marker="wrapped-value")

    def fake_run_module(target: str, argv: list[str] | None = None) -> int:
        calls.append((target, [] if argv is None else list(argv)))
        return 11

    monkeypatch.setattr(mod, "_impl", fake_impl)

    assert mod.marker == "wrapped-value"
    assert mod.impl() is fake_impl

    if hasattr(mod, "run_module") and hasattr(mod, "main") and hasattr(mod, "MODULE"):
        monkeypatch.setattr(mod, "run_module", fake_run_module)

        assert mod.main() == 7
        assert mod.main(["--dry-run", "demo"]) == 11
        assert calls == [(mod.MODULE, ["--dry-run", "demo"])]
