import sys
from pathlib import Path

# Ensure both workspace root and package root are on sys.path so imports like
# `app.*` and `novapolis_agent.app.*` resolve regardless of test runner cwd.
P = Path(__file__).resolve()
MAIN_ROOT = str(P.parents[2])
PKG_ROOT = str(P.parents[1])
if PKG_ROOT not in sys.path:
    sys.path.insert(0, PKG_ROOT)
if MAIN_ROOT not in sys.path:
    sys.path.insert(0, MAIN_ROOT)


def test_smoke_imports_batch9():
    """Smoke-imports für Batch 9 - app/api und app/core Module."""
    modules = [
        "app.api.chat_helpers",
        "app.api.models",
        "app.api.sim",
        "app.core.content_management",
        "app.core.memory",
        "app.core.mode",
        "app.core.prompts",
        "app.core.settings",
        "app.main",
    ]

    for m in modules:
        try:
            __import__(m)
        except ModuleNotFoundError:
            # try with package prefix 'novapolis_agent.' as fallback
            try:
                __import__(f"novapolis_agent.{m}")
            except SystemExit:
                continue
        except SystemExit:
            # Some modules may call sys.exit() at import-time in scripts; treat as okay
            continue
