from __future__ import annotations

import json
from pathlib import Path

from scripts import validate_eval_datasets as mod


def test_validate_eval_datasets_ok(tmp_path: Path) -> None:
    ds = tmp_path / "ok.yaml"
    ds.write_text(
        """
- id: eval-a
  slug: a
  tags: [neutral]
  messages:
    - role: user
      content: hi
""",
        encoding="utf-8",
    )

    assert mod.main(["--pattern", str(tmp_path / "*.yaml")]) == 0


def test_validate_eval_datasets_duplicate_slug_fails(tmp_path: Path) -> None:
    (tmp_path / "a.yaml").write_text(
        """
- id: eval-a
  slug: same
  messages:
    - role: user
      content: hi
""",
        encoding="utf-8",
    )
    (tmp_path / "b.yaml").write_text(
        """
- id: eval-b
  slug: same
  messages:
    - role: user
      content: hi
""",
        encoding="utf-8",
    )

    assert mod.main(["--pattern", str(tmp_path / "*.yaml"), "--strict"]) == 1


def test_validate_eval_datasets_duplicate_slug_allowed_for_combined(tmp_path: Path) -> None:
    (tmp_path / "combined_a.yaml").write_text(
        """
- id: eval-a
  slug: same
  messages:
    - role: user
      content: hi
""",
        encoding="utf-8",
    )
    (tmp_path / "combined_b.yaml").write_text(
        """
- id: eval-b
  slug: same
  messages:
    - role: user
      content: hi
""",
        encoding="utf-8",
    )

    assert mod.main(["--pattern", str(tmp_path / "combined_*.yaml"), "--strict"]) == 0


def test_validate_eval_datasets_uses_suite_config(tmp_path: Path) -> None:
    ds = tmp_path / "suite_one.yaml"
    ds.write_text(
        """
- slug: neutral.test.v1
  tags: [neutral]
  messages:
    - role: user
      content: hi
""",
        encoding="utf-8",
    )

    cfg = tmp_path / "suites.json"
    cfg.write_text(
        json.dumps(
            {
                "version": "x",
                "suites": {"neutral": {"packages": [str(ds)]}},
            }
        ),
        encoding="utf-8",
    )

    assert mod.main(["--suite-config", str(cfg), "--suite", "neutral", "--strict"]) == 0
