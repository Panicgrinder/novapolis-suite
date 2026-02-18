---
stand: 2026-01-07 09:13
update: Ran pytest -q at repo root
checks: returncode=0
---

# Postflight: pytest root

Log: F:\VS Code Workspace\Main\.tmp\results\reports\pytest_root_20260107_091212.log

Output (truncated):

........................................................................ [ 20%]
.........s.............................................................. [ 40%]
........................................................................ [ 60%]
........................................................................ [ 81%]
...................................................................      [100%]
============================== warnings summary ===============================
novapolis_agent/tests/scripts/test_open_latest_summary_edges.py::test_open_latest_summary_empty_dir
  <frozen runpy>:128: RuntimeWarning: 'scripts.open_latest_summary' found in sys.modules after import of package 'scripts', but prior to execution of 'scripts.open_latest_summary'; this may result in unpredictable behaviour

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
