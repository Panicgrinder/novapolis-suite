from __future__ import annotations

import builtins
import importlib
import os
import types
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_env_check_no_torch(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = importlib.import_module("scripts.fine_tune_pipeline")
    orig_import = builtins.__import__

    def _fake_import(name: str, *args: object, **kwargs: object):
        if name == "torch":
            raise ImportError("no torch")
        return orig_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", _fake_import)
    msg = mod.env_check()
    assert msg is not None
    assert "torch nicht importierbar" in msg


@pytest.mark.scripts
@pytest.mark.unit
def test_env_check_cuda_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = importlib.import_module("scripts.fine_tune_pipeline")

    class _Cuda:
        @staticmethod
        def is_available() -> bool:
            return False

    fake_torch = types.SimpleNamespace(cuda=_Cuda())
    monkeypatch.setitem(mod.sys.modules, "torch", fake_torch)

    msg = mod.env_check()
    assert msg is not None
    assert "CUDA nicht verfügbar" in msg


@pytest.mark.scripts
@pytest.mark.unit
def test_env_check_cuda_available(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = importlib.import_module("scripts.fine_tune_pipeline")

    class _Cuda:
        @staticmethod
        def is_available() -> bool:
            return True

    fake_torch = types.SimpleNamespace(cuda=_Cuda())
    monkeypatch.setitem(mod.sys.modules, "torch", fake_torch)

    assert mod.env_check() is None


@pytest.mark.scripts
@pytest.mark.unit
def test_env_check_cuda_probe_exception(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = importlib.import_module("scripts.fine_tune_pipeline")

    class _Cuda:
        @staticmethod
        def is_available() -> bool:
            raise RuntimeError("boom")

    fake_torch = types.SimpleNamespace(cuda=_Cuda())
    monkeypatch.setitem(mod.sys.modules, "torch", fake_torch)

    assert mod.env_check() is None


@pytest.mark.scripts
@pytest.mark.unit
def test_main_env_warning_soft_path(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mod = importlib.import_module("scripts.fine_tune_pipeline")
    train = tmp_path / "finetune_foo_train.jsonl"
    train.write_text("{}\n", encoding="utf-8")

    monkeypatch.setattr(mod, "latest_train_file", lambda *_a, **_k: os.fspath(train))
    monkeypatch.setattr(mod, "env_check", lambda: "CUDA nicht verfügbar; Training läuft vermutlich sehr langsam auf CPU.")

    calls: list[list[str]] = []

    def _call(args: list[str] | tuple[str, ...]) -> int:
        calls.append(list(args))
        return 0

    monkeypatch.setattr(mod, "subprocess", types.SimpleNamespace(call=_call))

    argv_backup = mod.sys.argv[:]
    try:
        mod.sys.argv = ["fine_tune_pipeline.py", "--model", "gpt2", "--finetune-dir", os.fspath(tmp_path)]
        rc = mod.main()
    finally:
        mod.sys.argv = argv_backup

    assert rc == 0
    assert calls
