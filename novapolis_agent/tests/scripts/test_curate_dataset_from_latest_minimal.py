from __future__ import annotations

import contextlib
import importlib
import io
import json
import os
import types
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_curate_minimal_flow(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mod = importlib.import_module("scripts.curate_dataset_from_latest")

    res_dir = tmp_path / "eval" / "results"
    res_dir.mkdir(parents=True)
    res_file = res_dir / "results_20250101_0000.jsonl"
    res_file.write_text(
        json.dumps({"item_id": "eval-1", "success": True, "response": "ok"}) + "\n",
        encoding="utf-8",
    )

    # Stub export and prepare modules used by the script
    exp_out = str(res_dir / "finetune" / "fin.jsonl")
    (res_dir / "finetune").mkdir(parents=True)

    from typing import Any

    async def _inspect(
        results_path: str,
        include_failures: bool = False,
        patterns: list[str] | None = None,
    ) -> dict[str, Any]:
        return {
            "ok": True,
            "successful_rows": 1,
            "exportable_count": 1,
            "unmapped_item_ids": [],
        }

    async def _export(
        results_path: str, out_dir: str, format: str, include_failures: bool
    ) -> dict[str, Any]:
        # write a tiny exported file for prepare step
        p = Path(exp_out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            json.dumps(
                {
                    "messages": [
                        {"role": "user", "content": "q"},
                        {"role": "assistant", "content": "a"},
                    ]
                }
            )
            + "\n",
            encoding="utf-8",
        )
        return {"ok": True, "out": str(p), "count": 1}

    def _prepare_pack(
        src_path: str,
        out_dir: str,
        format: str,
        train_ratio: float,
        seed: int,
        min_output_chars: int,
        dedupe_by_instruction: bool,
    ) -> dict[str, Any]:
        # Create dummy train/val outputs
        out = Path(out_dir)
        (out / "train.jsonl").write_text("{}\n", encoding="utf-8")
        (out / "val.jsonl").write_text("{}\n", encoding="utf-8")
        return {
            "ok": True,
            "train": str(out / "train.jsonl"),
            "val": str(out / "val.jsonl"),
            "counts": {"train": 1, "val": 1},
        }

    # Patch the imported modules inside script
    monkeypatch.setattr(
        mod,
        "_export",
        types.SimpleNamespace(export_from_results=_export, inspect_results_for_export=_inspect),
    )
    monkeypatch.setattr(mod, "_prepare", types.SimpleNamespace(prepare_pack=_prepare_pack))

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        # Simuliere CLI-Aufruf
        mod.sys.argv = [
            "curate_dataset_from_latest.py",
            "--results-dir",
            str(res_dir),
            "--format",
            "openai_chat",
        ]
        rc = mod.main()
    assert rc == 0
    out = buf.getvalue()
    assert '"ok": true' in out.lower()
    assert "train" in out and "val" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_curate_skips_newest_unexportable_results(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    mod = importlib.import_module("scripts.curate_dataset_from_latest")

    res_dir = tmp_path / "eval" / "results"
    res_dir.mkdir(parents=True)
    newest = res_dir / "results_20250102_0000.jsonl"
    newest.write_text(
        json.dumps({"item_id": "eval-missing", "success": True, "response": "ok"}) + "\n",
        encoding="utf-8",
    )
    older = res_dir / "results_20250101_0000.jsonl"
    older.write_text(
        json.dumps({"item_id": "eval-ok", "success": True, "response": "brauchbarer output"})
        + "\n",
        encoding="utf-8",
    )

    export_calls: list[str] = []

    async def _inspect(
        results_path: str,
        include_failures: bool = False,
        patterns: list[str] | None = None,
    ) -> dict[str, object]:
        if results_path.endswith("results_20250102_0000.jsonl"):
            return {
                "ok": False,
                "error": (
                    "Kein exportierbares Item gefunden; Results verweisen wahrscheinlich "
                    "auf veraltete oder nicht mehr aufloesbare Dataset-Pfade."
                ),
                "successful_rows": 1,
                "exportable_count": 0,
                "unmapped_item_ids": ["eval-missing"],
            }
        return {
            "ok": True,
            "successful_rows": 1,
            "exportable_count": 1,
            "unmapped_item_ids": [],
        }

    async def _export(
        results_path: str, out_dir: str, format: str, include_failures: bool
    ) -> dict[str, object]:
        export_calls.append(results_path)
        p = Path(out_dir) / "fin.jsonl"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            json.dumps(
                {
                    "messages": [
                        {"role": "user", "content": "q"},
                        {"role": "assistant", "content": "antwort mit ausreichender länge"},
                    ]
                }
            )
            + "\n",
            encoding="utf-8",
        )
        return {"ok": True, "out": str(p), "count": 1}

    def _prepare_pack(
        src_path: str,
        out_dir: str,
        format: str,
        train_ratio: float,
        seed: int,
        min_output_chars: int,
        dedupe_by_instruction: bool,
    ) -> dict[str, object]:
        out = Path(out_dir)
        (out / "train.jsonl").write_text("{}\n", encoding="utf-8")
        (out / "val.jsonl").write_text("{}\n", encoding="utf-8")
        return {
            "ok": True,
            "train": str(out / "train.jsonl"),
            "val": str(out / "val.jsonl"),
            "counts": {"train": 1, "val": 1},
        }

    monkeypatch.setattr(
        mod,
        "_export",
        types.SimpleNamespace(
            export_from_results=_export,
            inspect_results_for_export=_inspect,
        ),
    )
    monkeypatch.setattr(mod, "_prepare", types.SimpleNamespace(prepare_pack=_prepare_pack))

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod.sys.argv = [
            "curate_dataset_from_latest.py",
            "--results-dir",
            str(res_dir),
            "--format",
            "openai_chat",
        ]
        rc = mod.main()

    assert rc == 0
    assert export_calls == [os.fspath(older)]
    payload = json.loads(buf.getvalue())
    assert payload["results"].endswith("results_20250101_0000.jsonl")
    assert payload["skipped_results"][0]["results"].endswith("results_20250102_0000.jsonl")


@pytest.mark.scripts
@pytest.mark.unit
def test_curate_uses_results_glob_for_session_promotion_feedback(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    mod = importlib.import_module("scripts.curate_dataset_from_latest")

    res_dir = tmp_path / "eval" / "results"
    res_dir.mkdir(parents=True)
    neutral = res_dir / "results_20250103_0000_neutral.jsonl"
    neutral.write_text(
        json.dumps({"item_id": "eval-neutral", "success": True, "response": "neutral"}) + "\n",
        encoding="utf-8",
    )
    promotions = res_dir / "results_20250102_0000_session_promotions.jsonl"
    promotions.write_text(
        json.dumps({"item_id": "eval-promo", "success": True, "response": "promotions"}) + "\n",
        encoding="utf-8",
    )

    export_calls: list[str] = []

    async def _inspect(
        results_path: str,
        include_failures: bool = False,
        patterns: list[str] | None = None,
    ) -> dict[str, object]:
        return {
            "ok": True,
            "successful_rows": 1,
            "exportable_count": 1,
            "unmapped_item_ids": [],
        }

    async def _export(
        results_path: str, out_dir: str, format: str, include_failures: bool
    ) -> dict[str, object]:
        export_calls.append(results_path)
        p = Path(out_dir) / "fin.jsonl"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            json.dumps(
                {
                    "messages": [
                        {"role": "user", "content": "q"},
                        {"role": "assistant", "content": "antwort mit ausreichender laenge"},
                    ]
                }
            )
            + "\n",
            encoding="utf-8",
        )
        return {"ok": True, "out": str(p), "count": 1}

    def _prepare_pack(
        src_path: str,
        out_dir: str,
        format: str,
        train_ratio: float,
        seed: int,
        min_output_chars: int,
        dedupe_by_instruction: bool,
    ) -> dict[str, object]:
        out = Path(out_dir)
        (out / "train.jsonl").write_text("{}\n", encoding="utf-8")
        (out / "val.jsonl").write_text("{}\n", encoding="utf-8")
        return {
            "ok": True,
            "train": str(out / "train.jsonl"),
            "val": str(out / "val.jsonl"),
            "counts": {"train": 1, "val": 1},
        }

    monkeypatch.setattr(
        mod,
        "_export",
        types.SimpleNamespace(
            export_from_results=_export,
            inspect_results_for_export=_inspect,
        ),
    )
    monkeypatch.setattr(mod, "_prepare", types.SimpleNamespace(prepare_pack=_prepare_pack))

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod.sys.argv = [
            "curate_dataset_from_latest.py",
            "--results-dir",
            str(res_dir),
            "--results-glob",
            "results_*_session_promotions.jsonl",
            "--format",
            "openai_chat",
        ]
        rc = mod.main()

    assert rc == 0
    assert export_calls == [os.fspath(promotions)]
    payload = json.loads(buf.getvalue())
    assert payload["results"].endswith("results_20250102_0000_session_promotions.jsonl")
