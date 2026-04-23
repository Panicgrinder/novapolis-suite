from __future__ import annotations

from ._proxy import load

_impl = load("novapolis_agent.scripts.build_training_from_rp")


def impl():
    return _impl


def __getattr__(name: str):
    return getattr(_impl, name)
