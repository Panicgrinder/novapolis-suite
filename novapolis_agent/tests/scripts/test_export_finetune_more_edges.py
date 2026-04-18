from __future__ import annotations

import builtins
import asyncio
import importlib
import json
import os
import runpy
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


def _write_results_single(
    path: str, item_id: str, success: bool = True, response: str = "OK"
) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps({"_meta": True}) + "\n")
        f.write(
            json.dumps(
                {
                    "item_id": item_id,
                    "response": response,
                    "checks_passed": {"must_include": success},
                    "success": success,
                    "failed_checks": ([] if success else ["must_include"]),
                    "source_file": "eval-x.jsonl",
                    "source_package": "general",
                },
                ensure_ascii=False,
            )
            + "\n"
        )


def _write_dataset_messages(path: str, item_id: str, messages: list[dict[str, str]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {"id": item_id, "messages": messages, "source_package": "general"},
                ensure_ascii=False,
            )
            + "\n"
        )


def _load_module():
    return importlib.import_module("scripts.export_finetune")


@pytest.mark.scripts
@pytest.mark.unit
def test_helper_paths_and_pair_collection_cover_edge_paths(tmp_path: Path) -> None:
    exporter = _load_module()

    absolute_path = str((tmp_path / "abs.jsonl").resolve())
    assert exporter._resolve_eval_path(absolute_path) == absolute_path

    bracket_dataset = tmp_path / "dataset[1].jsonl"
    plain_dataset = tmp_path / "plain.jsonl"
    bracket_dataset.write_text("{}\n", encoding="utf-8")
    plain_dataset.write_text("{}\n", encoding="utf-8")

    resolved = exporter._resolve_existing_inputs(
        ["", str(bracket_dataset), "plain.jsonl", "plain.jsonl"],
        str(tmp_path),
    )

    assert str(bracket_dataset) in resolved
    assert str(plain_dataset) in resolved

    pairs, unmapped = exporter._collect_export_pairs(
        [{"item_id": "item-ok"}, {"item_id": "item-missing"}],
        {"item-ok": object()},
    )

    assert len(pairs) == 1
    assert unmapped == ["item-missing"]
    assert exporter._first_user_message([]) == ("", "")


@pytest.mark.scripts
@pytest.mark.unit
def test_helper_skip_branches_cover_empty_values() -> None:
    exporter = _load_module()

    assert exporter._dedupe_preserve_order(["", "alpha", "alpha", "beta"]) == [
        "alpha",
        "beta",
    ]
    assert exporter._result_lookup_keys(
        {"item_id": "", "slug": "slug-a", "id": None, "eval_id": "eval-z"}
    ) == ["slug-a", "eval-slug-a", "eval-z", "z"]


@pytest.mark.scripts
@pytest.mark.unit
def test_load_run_eval_module_raises_when_loader_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    exporter = _load_module()

    while exporter.PROJECT_ROOT in sys.path:
        sys.path.remove(exporter.PROJECT_ROOT)

    monkeypatch.setattr(
        "importlib.util.spec_from_file_location",
        lambda *args, **kwargs: SimpleNamespace(loader=None),
    )

    with pytest.raises(RuntimeError, match="Konnte run_eval.py nicht laden"):
        exporter._load_run_eval_module()

    assert exporter.PROJECT_ROOT in sys.path


@pytest.mark.scripts
@pytest.mark.unit
def test_export_alpaca_instruction_and_input_split(tmp_path: os.PathLike[str]) -> None:
    from novapolis_agent.scripts import export_finetune as exporter

    # Dataset mit mehreren Nachrichten: erste user = instruction, Rest wird input
    dataset = os.path.join(tmp_path, "ds.jsonl")
    messages = [
        {"role": "system", "content": "S"},
        {"role": "user", "content": "U1"},
        {"role": "assistant", "content": "A1"},
        {"role": "user", "content": "U2"},
    ]
    _write_dataset_messages(dataset, "item-1", messages)
    results = os.path.join(tmp_path, "res.jsonl")
    _write_results_single(results, "item-1", success=True, response="R1")

    out = asyncio.run(
        exporter.export_from_results(
            results,
            out_dir=str(tmp_path),
            format="alpaca",
            include_failures=False,
            patterns=[dataset],
        )
    )
    assert out.get("ok")
    out_path = str(out.get("out"))
    with open(out_path, encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    assert len(rows) == 1
    rec = rows[0]
    assert rec.get("instruction") == "U1"
    # input sammelt restliche Inhalte (ohne erste user-Nachricht)
    assert "U2" in rec.get("input", "") or "A1" in rec.get("input", "")
    assert rec.get("output") == "R1"


@pytest.mark.scripts
@pytest.mark.unit
def test_export_out_dir_none_uses_settings_fallback(
    monkeypatch: pytest.MonkeyPatch, tmp_path: os.PathLike[str]
) -> None:
    exporter = _load_module()
    settings_mod = importlib.import_module("novapolis_agent.app.core.settings")

    monkeypatch.setattr(
        settings_mod.settings,
        "EVAL_RESULTS_DIR",
        os.path.join("eval", "results", "tmp-export"),
        raising=False,
    )

    original_import = builtins.__import__

    def _fallback_import(name: str, *args, **kwargs):
        if name == "app.core.settings":
            raise ImportError("force secondary settings import")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", _fallback_import)

    ds = os.path.join(tmp_path, "d.jsonl")
    _write_dataset_messages(ds, "item-2", [{"role": "user", "content": "X"}])
    res = os.path.join(tmp_path, "r.jsonl")
    _write_results_single(res, "item-2", success=True, response="R2")

    out = asyncio.run(
        exporter.export_from_results(
            res, out_dir=None, format="alpaca", include_failures=False, patterns=[ds]
        )
    )
    assert out.get("ok")
    out_path = str(out.get("out"))
    # sollte innerhalb des projekt-root eval/results/tmp-export landen
    assert "eval" in out_path.replace("\\", "/") and "tmp-export" in out_path.replace("\\", "/")


@pytest.mark.scripts
@pytest.mark.unit
def test_export_out_dir_none_uses_run_eval_defaults_when_settings_imports_fail(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    exporter = _load_module()

    result_dir = tmp_path / "fallback-results"
    result_dir.mkdir()
    dataset_path = tmp_path / "dataset.jsonl"
    results_path = tmp_path / "results.jsonl"
    _write_dataset_messages(str(dataset_path), "item-3", [{"role": "user", "content": "Hallo"}])
    _write_results_single(str(results_path), "item-3", success=True, response="R3")

    monkeypatch.setattr(exporter.run_eval, "DEFAULT_RESULTS_DIR", str(result_dir), raising=False)
    monkeypatch.setattr(exporter.run_eval, "DEFAULT_EVAL_DIR", str(result_dir), raising=False)

    original_import = builtins.__import__

    def _blocked_import(name: str, *args, **kwargs):
        if name in {"app.core.settings", "novapolis_agent.app.core.settings"}:
            raise ImportError("force default results dir")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", _blocked_import)

    out = asyncio.run(
        exporter.export_from_results(
            str(results_path), out_dir=None, format="alpaca", patterns=[str(dataset_path)]
        )
    )

    assert out.get("ok") is True
    assert Path(str(out.get("out"))).parent == result_dir


@pytest.mark.scripts
@pytest.mark.unit
def test_export_unmapped_item_returns_error(tmp_path: os.PathLike[str]) -> None:
    from novapolis_agent.scripts import export_finetune as exporter

    # Ergebnis referenziert nicht existierendes Item
    res = os.path.join(tmp_path, "r.jsonl")
    _write_results_single(res, "missing-id", success=True, response="R3")
    out = asyncio.run(
        exporter.export_from_results(
            res,
            out_dir=str(tmp_path),
            format="alpaca",
            include_failures=True,
            patterns=[os.path.join(tmp_path, "empty.jsonl")],
        )
    )
    assert out.get("ok") is False
    assert "Kein exportierbares Item gefunden" in str(out.get("error"))
    assert out.get("exportable_count") == 0
    assert out.get("unmapped_item_ids") == ["missing-id"]


@pytest.mark.scripts
@pytest.mark.unit
def test_inspect_results_for_export_reports_no_successful_rows(tmp_path: Path) -> None:
    exporter = _load_module()

    results = tmp_path / "results.jsonl"
    results.write_text(
        json.dumps(
            {
                "item_id": "item-fail",
                "response": "",
                "success": False,
                "failed_checks": ["x"],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    out = asyncio.run(exporter.inspect_results_for_export(str(results), include_failures=False))

    assert out == {"ok": False, "error": "Keine erfolgreichen Ergebnisse für Export"}


@pytest.mark.scripts
@pytest.mark.unit
def test_inspect_results_for_export_uses_broad_fallback(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    exporter = _load_module()

    results = tmp_path / "results.jsonl"
    _write_results_single(str(results), "item-4", success=True, response="R4")

    calls: list[list[str] | None] = []

    async def _fake_load_items_map(patterns: list[str] | None = None) -> dict[str, object]:
        calls.append(patterns)
        if len(calls) == 1:
            return {}
        item = SimpleNamespace(id="item-4", slug="", messages=[], source_package="pkg")
        return {"item-4": item, "eval-item-4": item}

    monkeypatch.setattr(exporter, "_load_items_map", _fake_load_items_map)
    monkeypatch.setattr(exporter, "_dataset_dir", lambda: str(tmp_path / "datasets"))

    out = asyncio.run(exporter.inspect_results_for_export(str(results), include_failures=False))

    assert out["ok"] is True
    assert out["used_broad_fallback"] is True
    assert out["exportable_count"] == 1
    assert calls[0] == [] or calls[0] is None
    assert calls[1] == [os.path.join(str(tmp_path / "datasets"), "**", "*.json*")]


@pytest.mark.scripts
@pytest.mark.unit
def test_export_from_results_rejects_unknown_format(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    exporter = _load_module()

    async def _fake_inspect_results_for_export(*args, **kwargs) -> dict[str, object]:
        item = SimpleNamespace(id="item-5", messages=[], source_package="pkg")
        return {
            "ok": True,
            "export_pairs": [
                (
                    {
                        "item_id": "item-5",
                        "response": "Antwort",
                        "success": True,
                        "failed_checks": [],
                    },
                    item,
                )
            ],
        }

    monkeypatch.setattr(exporter, "inspect_results_for_export", _fake_inspect_results_for_export)

    with pytest.raises(ValueError, match="Unbekanntes Format"):
        asyncio.run(
            exporter.export_from_results(
                results_path=str(tmp_path / "results.jsonl"),
                out_dir=str(tmp_path),
                format="invalid-format",
            )
        )


@pytest.mark.scripts
@pytest.mark.unit
@pytest.mark.parametrize(
    ("async_result", "expected_output"),
    [
        ({"ok": True, "out": "demo.jsonl", "count": 2}, "Export: demo.jsonl (2 Einträge)"),
        ({"ok": False, "error": "kaputt"}, "Fehler: kaputt"),
    ],
)
def test_module_main_cli_prints_result(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    tmp_path: Path,
    async_result: dict[str, object],
    expected_output: str,
) -> None:
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "export_finetune.py"

    def _fake_asyncio_run(coro):
        coro.close()
        return async_result

    monkeypatch.setattr("asyncio.run", _fake_asyncio_run)
    monkeypatch.setattr(
        "sys.argv",
        ["export_finetune.py", str(tmp_path / "results.jsonl"), "--format", "alpaca"],
    )

    runpy.run_path(str(script_path), run_name="__main__")

    assert expected_output in capsys.readouterr().out
