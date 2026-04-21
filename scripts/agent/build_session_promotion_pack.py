from __future__ import annotations

from ._run_module import import_module, run_module

MODULE = "novapolis_agent.scripts.build_session_promotion_pack"

_impl = import_module(MODULE)


def impl():
    return _impl


def __getattr__(name: str):
    return getattr(_impl, name)


def main(argv: list[str] | None = None) -> int:
    if argv is None and hasattr(_impl, "main"):
        return int(_impl.main())
    return run_module(MODULE, argv)


if __name__ == "__main__":
    raise SystemExit(main())