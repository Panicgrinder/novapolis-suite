from __future__ import annotations

import json
import pathlib

from scripts import prepare_finetune_pack as pack


def _validate_jsonl(path: pathlib.Path) -> None:
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                json.loads(line)
            except Exception as e:
                raise AssertionError(f"Invalid JSON at line {i} in {path}: {e}") from e


def test_prepare_pack_smoke(tmp_path: pathlib.Path) -> None:
    src = tmp_path / "openai_chat.jsonl"
    src.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "messages": [
                            {"role": "user", "content": "Wie geht es dir heute in Novapolis?"},
                            {
                                "role": "assistant",
                                "content": "Mir geht es gut. Danke der Nachfrage aus Novapolis.",
                            },
                        ]
                    },
                    ensure_ascii=False,
                ),
                json.dumps(
                    {
                        "messages": [
                            {"role": "user", "content": "Was ist dein Auftrag?"},
                            {
                                "role": "assistant",
                                "content": "Ich dokumentiere Ereignisse und helfe bei klaren Antworten.",
                            },
                        ]
                    },
                    ensure_ascii=False,
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = pack.prepare_pack(
        src_path=str(src),
        out_dir=str(tmp_path),
        format="openai_chat",
        train_ratio=0.5,
        seed=42,
        min_output_chars=20,
        dedupe_by_instruction=True,
    )

    assert result.get("ok") is True
    train_file = pathlib.Path(str(result["train"]))
    val_file = pathlib.Path(str(result["val"]))
    assert train_file.exists()
    assert val_file.exists()

    _validate_jsonl(train_file)
    _validate_jsonl(val_file)
