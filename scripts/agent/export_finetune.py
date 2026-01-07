from __future__ import annotations

from ._run_module import run_module

MODULE = "novapolis_agent.scripts.export_finetune"


def main(argv: list[str] | None = None) -> int:
    return run_module(MODULE, argv)


if __name__ == "__main__":
    raise SystemExit(main())
