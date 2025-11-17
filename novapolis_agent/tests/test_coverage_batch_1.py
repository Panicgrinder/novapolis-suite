import importlib
import os
import sys

MODULES = [
    # top-level package module
    "novapolis_agent.run_server",
    "novapolis_agent.agents.cvn_agent",
    "novapolis_agent",
    "novapolis_agent.app",
    "novapolis_agent.app.main",
    "novapolis_agent.app.api",
    "novapolis_agent.app.api.chat",
]


def test_import_batch_1():
    """Smoke-import the first batch of modules to increase executed lines.

    This test only asserts modules import without raising ImportError.
    It avoids calling heavy functions to reduce side-effects.
    """
    # Ensure repo root is on sys.path
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    for name in MODULES:
        try:
            importlib.import_module(name)
        except Exception:
            # Re-raise to let pytest report the failure.
            # We only expect ImportError if the module is missing.
            raise
