from __future__ import annotations

import builtins
import runpy
import sys
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_duplicate_helpers_match_paths_and_basenames() -> None:
    from scripts import validate_eval_datasets as mod

    assert mod._duplicate_allowed("a/combined_a.yaml", "b/other.yaml", ["*combined*"]) is True
    assert mod._duplicate_allowed("a/first.yaml", "b/combined_b.yaml", ["combined_b.yaml"]) is True
    assert mod._duplicate_allowed("a/first.yaml", "b/second.yaml", ["*combined*"]) is False
    assert mod._matches_any("folder/example.yaml", ["folder/*"]) is True
    assert mod._matches_any("folder/example.yaml", ["example.yaml"]) is True
    assert mod._matches_any("folder/example.yaml", ["other*"]) is False


@pytest.mark.scripts
@pytest.mark.unit
def test_load_suite_patterns_covers_continue_and_skip_paths(tmp_path: Path) -> None:
    from scripts import validate_eval_datasets as mod

    cfg = tmp_path / "suite_edges.json"
    cfg.write_text(
        '{"suites": {'
        '"skip": "no-dict", '
        '"empty": {"packages": "no-list"}, '
        '"mix": {"packages": ["", 1, "  ok.jsonl  "]}'
        "}}",
        encoding="utf-8",
    )

    assert mod._load_suite_patterns(str(cfg), ["skip", "empty", "mix"]) == ["ok.jsonl"]


@pytest.mark.scripts
@pytest.mark.unit
def test_main_fails_when_no_files_found(tmp_path: Path) -> None:
    from scripts import validate_eval_datasets as mod

    assert mod.main(["--pattern", str(tmp_path / "*.yaml")]) == 1


@pytest.mark.scripts
@pytest.mark.unit
def test_main_fails_for_invalid_tags_and_missing_payload_shape(tmp_path: Path) -> None:
    from scripts import validate_eval_datasets as mod

    ds = tmp_path / "bad.yaml"
    ds.write_text(
        """
- id: eval-a
  slug: bad.payload.v1
  tags: invalid
""",
        encoding="utf-8",
    )

    assert mod.main(["--pattern", str(ds), "--strict"]) == 1


@pytest.mark.scripts
@pytest.mark.unit
def test_main_warns_for_duplicate_id_in_non_strict_mode(tmp_path: Path) -> None:
    from scripts import validate_eval_datasets as mod

    (tmp_path / "a.yaml").write_text(
        """
- id: eval-a
  slug: slug-a
  messages:
    - role: user
      content: hi
""",
        encoding="utf-8",
    )
    (tmp_path / "b.yaml").write_text(
        """
- id: eval-a
  slug: slug-b
  messages:
    - role: user
      content: hi
""",
        encoding="utf-8",
    )

    assert mod.main(["--pattern", str(tmp_path / "*.yaml")]) == 0


@pytest.mark.scripts
@pytest.mark.unit
def test_main_allows_missing_id_pattern_in_strict_mode(tmp_path: Path) -> None:
    from scripts import validate_eval_datasets as mod

    ds = tmp_path / "allow_missing.yaml"
    ds.write_text(
        """
- tags: [neutral]
  prompt: hi
""",
        encoding="utf-8",
    )

    assert (
        mod.main(
            [
                "--pattern",
                str(ds),
                "--strict",
                "--allow-missing-id-pattern",
                "*allow_missing*",
            ]
        )
        == 0
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_main_handles_invalid_suite_config_and_no_records(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from scripts import validate_eval_datasets as mod

    cfg = tmp_path / "broken.json"
    cfg.write_text("not-json", encoding="utf-8")
    assert mod._load_suite_patterns(str(cfg), ["neutral"]) == []

    ds = tmp_path / "empty.yaml"
    ds.write_text("- id: eval-a\n  slug: a\n  prompt: hi\n", encoding="utf-8")
    monkeypatch.setattr(mod, "_load_coercer", lambda: (lambda text, file_path: []))

    assert mod.main(["--pattern", str(ds)]) == 1


@pytest.mark.scripts
@pytest.mark.unit
def test_load_coercer_and_suite_pattern_edges(monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import validate_eval_datasets as mod

    original_sys_path = list(sys.path)
    if str(Path(mod.__file__).resolve().parent.parent) in sys.path:
        sys.path.remove(str(Path(mod.__file__).resolve().parent.parent))

    fake_utils = type("_FakeUtils", (), {"coerce_eval_records": lambda text, file_path: []})
    monkeypatch.setattr(mod.importlib, "import_module", lambda name: fake_utils)
    assert mod._load_coercer() is fake_utils.coerce_eval_records
    assert str(Path(mod.__file__).resolve().parent.parent) in sys.path
    sys.path[:] = original_sys_path

    cfg = Path.cwd() / "dummy-suite.json"
    try:
        cfg.write_text('{"suites": []}', encoding="utf-8")
        assert mod._load_suite_patterns(str(cfg), ["neutral"]) == []
    finally:
        cfg.unlink(missing_ok=True)


@pytest.mark.scripts
@pytest.mark.unit
def test_main_covers_default_patterns_read_fail_duplicate_id_strict_and_missing_id_strict(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from scripts import validate_eval_datasets as mod

    assert mod.main([]) == 0

    read_fail = tmp_path / "read_fail.yaml"
    read_fail.write_text("- id: eval-a\n", encoding="utf-8")
    real_open = builtins.open

    def _fake_open(path, *args, **kwargs):
        if str(path) == str(read_fail):
            raise OSError("boom")
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", _fake_open)
    assert mod.main(["--pattern", str(read_fail), "--strict"]) == 1

    monkeypatch.setattr(builtins, "open", real_open)

    (tmp_path / "id_a.yaml").write_text(
        """
- id: eval-a
  slug: slug-a
  prompt: hi
""",
        encoding="utf-8",
    )
    (tmp_path / "id_b.yaml").write_text(
        """
- id: eval-a
  slug: slug-b
  prompt: hi
""",
        encoding="utf-8",
    )
    assert mod.main(["--pattern", str(tmp_path / "id_*.yaml"), "--strict"]) == 1

    missing = tmp_path / "missing_strict.yaml"
    missing.write_text("- prompt: hi\n", encoding="utf-8")
    assert mod.main(["--pattern", str(missing), "--strict"]) == 1


@pytest.mark.scripts
@pytest.mark.unit
def test_module_main_executes_via_runpy(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "validate_eval_datasets.py"
    dataset = tmp_path / "dataset.yaml"
    dataset.write_text(
        """
- id: eval-a
  slug: slug-a
  prompt: hi
""",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "validate_eval_datasets.py",
            "--pattern",
            str(dataset),
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        runpy.run_path(str(script_path), run_name="__main__")

    assert exc_info.value.code == 0
