import json
import os
import tempfile
import time
import unittest
from typing import Any

from scripts.agent.run_eval import load_evaluation_items, load_prompts


class TestEvalLoader(unittest.IsolatedAsyncioTestCase):
    async def test_newer_file_wins_on_same_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            f_old = os.path.join(tmp, "a.jsonl")
            f_new = os.path.join(tmp, "b.jsonl")

            rec_old: dict[str, Any] = {"id": "eval-999", "prompt": "ALT", "must_include": ["alt"]}
            rec_new: dict[str, Any] = {"id": "eval-999", "prompt": "NEU", "must_include": ["neu"]}

            with open(f_old, "w", encoding="utf-8") as f:
                f.write(json.dumps(rec_old, ensure_ascii=False) + "\n")
            # Stelle sicher, dass mtime unterschiedlich ist
            time.sleep(1.1)
            with open(f_new, "w", encoding="utf-8") as f:
                f.write(json.dumps(rec_new, ensure_ascii=False) + "\n")

            items = await load_prompts([os.path.join(tmp, "*.jsonl")])
            by_id = {i["id"]: i for i in items}
            assert "eval-999" in by_id
            assert by_id["eval-999"]["prompt"] == "NEU"

    async def test_yaml_loader_supports_slug_and_tags(self):
        with tempfile.TemporaryDirectory() as tmp:
            f_yaml = os.path.join(tmp, "suite.yaml")
            yaml_content = """
- slug: neutral.greeting.v1
  tags: [neutral, greeting]
  category: neutral
  messages:
    - role: user
      content: "Sag freundlich hallo."
  checks:
    must_include: ["hallo"]
"""
            with open(f_yaml, "w", encoding="utf-8") as f:
                f.write(yaml_content)

            items = await load_evaluation_items([f_yaml])
            assert len(items) == 1
            item = items[0]
            assert item.id == "eval-neutral.greeting.v1"
            assert item.slug == "neutral.greeting.v1"
            assert "neutral" in item.tags
