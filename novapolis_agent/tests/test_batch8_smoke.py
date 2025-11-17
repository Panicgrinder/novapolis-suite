import sys
from pathlib import Path


# Ensure repository root is on sys.path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_smoke_imports():
    """Smoke-imports der Batch8-Module (sollten beim Import keine Fehler werfen)."""
    modules = [
        "scripts.eval_loader",
        "scripts.check_openai_key",
        "scripts.fix_donelog_times",
        "scripts.generate_eval_dataset",
        "scripts.eval_ui",
        "novapolis_agent.scripts.run_eval",
        "scripts.openai_finetune",
        "utils.eval_utils",
        "app.api.chat",
        "utils.context_notes",
    ]

    for m in modules:
        try:
            __import__(m)
        except SystemExit:
            # Some scripts run CLI checks at import-time and call sys.exit();
            # treat SystemExit as acceptable for a smoke-import test.
            continue
