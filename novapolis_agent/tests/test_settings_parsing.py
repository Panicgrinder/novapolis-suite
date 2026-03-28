from __future__ import annotations

import os
from importlib import reload

import pytest
from app.core import settings as settings_module
from pytest import MonkeyPatch


def test_settings_parsing_from_env(monkeypatch: MonkeyPatch) -> None:
    # Set env vars
    monkeypatch.setenv("PROJECT_NAME", "My App")
    monkeypatch.setenv("PROJECT_DESCRIPTION", "Desc")
    monkeypatch.setenv("PROJECT_VERSION", "9.9.9")
    # In pydantic-settings v2 müssen Listenfelder als JSON serialisiert werden
    monkeypatch.setenv("BACKEND_CORS_ORIGINS", '["http://localhost:3000", "http://127.0.0.1:5173"]')
    monkeypatch.setenv("OLLAMA_HOST", "http://host:11434")
    monkeypatch.setenv("MODEL_NAME", "m:1")

    # Recreate settings via module reload (settings instance is created at import time)
    reload(settings_module)
    s = settings_module.settings

    assert s.PROJECT_NAME == "My App"
    assert s.PROJECT_DESCRIPTION == "Desc"
    assert s.PROJECT_VERSION == "9.9.9"

    assert s.BACKEND_CORS_ORIGINS == [
        "http://localhost:3000",
        "http://127.0.0.1:5173",
    ]
    assert s.OLLAMA_HOST == "http://host:11434"
    assert s.MODEL_NAME == "m:1"


def test_settings_contract_fallbacks(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.delenv("STRICT_CONFIG", raising=False)
    monkeypatch.setenv("REQUEST_TIMEOUT", "0")
    monkeypatch.setenv("REQUEST_MAX_INPUT_CHARS", "0")
    monkeypatch.setenv("RATE_LIMIT_WINDOW_SEC", "0")
    monkeypatch.setenv("OLLAMA_HOST", "localhost:11434/")
    monkeypatch.setenv("MODEL_NAME", "")

    reload(settings_module)
    s = settings_module.settings

    assert s.REQUEST_TIMEOUT == 60.0
    assert s.REQUEST_MAX_INPUT_CHARS == 16000
    assert s.RATE_LIMIT_WINDOW_SEC == 60.0
    assert s.OLLAMA_HOST == "http://localhost:11434"
    assert s.MODEL_NAME == "llama3.1:8b"
    assert len(s.SETTINGS_CONTRACT_ISSUES) >= 3


def test_settings_contract_strict_mode_raises(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("STRICT_CONFIG", "true")
    monkeypatch.setenv("REQUEST_TIMEOUT", "0")

    with pytest.raises(ValueError):
        reload(settings_module)


def test_settings_default_eval_paths_are_module_local(monkeypatch: MonkeyPatch) -> None:
    for name in (
        "EVAL_DIRECTORY",
        "EVAL_DATASET_DIR",
        "EVAL_RESULTS_DIR",
        "EVAL_CONFIG_DIR",
        "RAG_INDEX_PATH",
    ):
        monkeypatch.delenv(name, raising=False)

    reload(settings_module)
    s = settings_module.settings

    assert s.EVAL_DIRECTORY == os.path.join("novapolis_agent", "eval")
    assert s.EVAL_DATASET_DIR == os.path.join("novapolis_agent", "eval", "datasets")
    assert s.EVAL_RESULTS_DIR == os.path.join("novapolis_agent", "eval", "results")
    assert s.EVAL_CONFIG_DIR == os.path.join("novapolis_agent", "eval", "config")
    assert s.RAG_INDEX_PATH == str(
        os.path.join("novapolis_agent", "eval", "results", "rag", "index.json")
    )
