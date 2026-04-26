from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts import training_release_gate as mod


def _write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_release_gate_passes_with_green_rp_content_and_repo_provenance(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    repo_root = tmp_path / "repo"
    project_root = repo_root / "novapolis_agent"
    results_dir = project_root / "eval" / "results"
    dataset_path = (
        project_root / "eval" / "datasets" / "training" / "chronistin_operativ_kurz.v1.jsonl"
    )
    provenance_doc = repo_root / "novapolis-dev" / "docs" / "dataset-provenance.md"

    _write_jsonl(
        results_dir / "results_20260423_1610_rp_content.jsonl",
        [
            {"_meta": True},
            {"item_id": "rp-1", "success": True},
        ],
    )
    _write_jsonl(dataset_path, [{"id": "train-1", "messages": [{"role": "user", "content": "hi"}]}])
    provenance_doc.parent.mkdir(parents=True, exist_ok=True)
    provenance_doc.write_text(
        "| Datensatz | Pfad | Herkunft | Freigabe | Nachweis |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| Train | `novapolis_agent/eval/datasets/training/"
        "chronistin_operativ_kurz.v1.jsonl` | intern | gruen | ok |\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(mod, "REPO_ROOT", str(repo_root))
    monkeypatch.setattr(mod, "PROJECT_ROOT", str(project_root))
    monkeypatch.setattr(mod, "DEFAULT_RESULTS_DIR", str(results_dir))
    monkeypatch.setattr(mod, "DEFAULT_PROVENANCE_DOC", str(provenance_doc))
    monkeypatch.setattr(
        mod,
        "DEFAULT_SUITE_CONFIG",
        str(project_root / "eval" / "config" / "suites.json"),
    )
    monkeypatch.setattr(mod.dataset_validator, "main", lambda argv: 0)

    result = mod.ensure_release_gate(train_file=str(dataset_path), require_green_provenance=True)

    assert result.ok is True
    assert (
        result.details["provenance"][
            "novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl"
        ]
        == "gruen"
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_release_gate_blocks_train_on_yellow_provenance(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    repo_root = tmp_path / "repo"
    project_root = repo_root / "novapolis_agent"
    results_dir = project_root / "eval" / "results"
    dataset_path = project_root / "eval" / "datasets" / "curation" / "session_promotions.v1.jsonl"
    provenance_doc = repo_root / "novapolis-dev" / "docs" / "dataset-provenance.md"

    _write_jsonl(
        results_dir / "results_20260423_1610_rp_content.jsonl",
        [
            {"_meta": True},
            {"item_id": "rp-1", "success": True},
        ],
    )
    _write_jsonl(dataset_path, [{"id": "promo-1", "messages": [{"role": "user", "content": "hi"}]}])
    provenance_doc.parent.mkdir(parents=True, exist_ok=True)
    provenance_doc.write_text(
        "| Datensatz | Pfad | Herkunft | Freigabe | Nachweis |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| Promo | `novapolis_agent/eval/datasets/curation/"
        "session_promotions.v1.jsonl` | intern | gelb | ok |\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(mod, "REPO_ROOT", str(repo_root))
    monkeypatch.setattr(mod, "PROJECT_ROOT", str(project_root))
    monkeypatch.setattr(mod, "DEFAULT_RESULTS_DIR", str(results_dir))
    monkeypatch.setattr(mod, "DEFAULT_PROVENANCE_DOC", str(provenance_doc))
    monkeypatch.setattr(
        mod,
        "DEFAULT_SUITE_CONFIG",
        str(project_root / "eval" / "config" / "suites.json"),
    )
    monkeypatch.setattr(mod.dataset_validator, "main", lambda argv: 0)

    result = mod.ensure_release_gate(train_file=str(dataset_path), require_green_provenance=True)

    assert result.ok is False
    assert result.code == 6
    assert "below required gruen" in result.errors[0]
