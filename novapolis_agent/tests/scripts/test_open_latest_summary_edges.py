from __future__ import annotations

import importlib
import runpy
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_open_latest_summary_empty_dir(tmp_path: Path) -> None:
    mod = importlib.import_module("scripts.open_latest_summary")
    script_path = Path(mod.__file__).resolve()

    # find_latest_summary liefert None bei leerem Verzeichnis
    assert mod.find_latest_summary(tmp_path) is None

    # main mit --print und leerem Ordner gibt 2 zurück
    import sys

    argv_bak = sys.argv
    try:
        sys.argv = ["open_latest_summary.py", "--print", "--dir", str(tmp_path)]
        with pytest.raises(SystemExit) as se:
            runpy.run_path(str(script_path), run_name="__main__")
        assert se.value.code == 2
    except AttributeError:
        # Fallback: direkte Ausführung von main()
        code = mod.main()
        assert code in (0, 2)
    finally:
        sys.argv = argv_bak
