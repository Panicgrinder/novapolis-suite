---
stand: 2025-12-13 04:24
update: Ran pytest -q at repo root
checks: returncode=2
---

# Postflight: pytest root

Log: F:\VS Code Workspace\Main\.tmp\results\reports\pytest_root_20251213_042439.log

Output (truncated):


=================================== ERRORS ====================================
_ ERROR collecting novapolis_agent/tests/scripts/test_customize_prompts_smoke.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_customize_prompts_smoke.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_customize_prompts_smoke.py:6: in <module>
    from novapolis_agent.scripts import customize_prompts as cp
E   ModuleNotFoundError: No module named 'novapolis_agent'
_ ERROR collecting novapolis_agent/tests/scripts/test_fine_tune_pipeline_smoke.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_fine_tune_pipeline_smoke.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_fine_tune_pipeline_smoke.py:5: in <module>
    from novapolis_agent.scripts import fine_tune_pipeline as ftp
E   ModuleNotFoundError: No module named 'novapolis_agent'
_ ERROR collecting novapolis_agent/tests/scripts/test_map_reduce_summary_llm_smoke.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_map_reduce_summary_llm_smoke.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_map_reduce_summary_llm_smoke.py:5: in <module>
    from novapolis_agent.scripts import map_reduce_summary_llm as mrl
E   ModuleNotFoundError: No module named 'novapolis_agent'
_ ERROR collecting novapolis_agent/tests/scripts/test_open_latest_summary_smoke.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_open_latest_summary_smoke.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_open_latest_summary_smoke.py:5: in <module>
    from novapolis_agent.scripts import open_latest_summary as ols
E   ModuleNotFoundError: No module named 'novapolis_agent'
__ ERROR collecting novapolis_agent/tests/scripts/test_run_eval_cli_hint.py ___
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_run_eval_cli_hint.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_run_eval_cli_hint.py:2: in <module>
    from scripts.run_eval import EvaluationItem, run_evaluation
E   ModuleNotFoundError: No module named 'scripts'
_ ERROR collecting novapolis_agent/tests/scripts/test_run_eval_hint_injection.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_run_eval_hint_injection.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_run_eval_hint_injection.py:1: in <module>
    from scripts.run_eval import inject_eval_hint
E   ModuleNotFoundError: No module named 'scripts'
_ ERROR collecting novapolis_agent/tests/scripts/test_run_eval_hint_terms.py __
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_run_eval_hint_terms.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_run_eval_hint_terms.py:4: in <module>
    from scripts.run_eval import EvaluationItem, compute_hint_terms
E   ModuleNotFoundError: No module named 'scripts'
__ ERROR collecting novapolis_agent/tests/scripts/test_todo_gather_smoke.py ___
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_todo_gather_smoke.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_todo_gather_smoke.py:5: in <module>
    from novapolis_agent.scripts import todo_gather as tg
E   ModuleNotFoundError: No module named 'novapolis_agent'
__ ERROR collecting novapolis_agent/tests/test_api_chat_internal_branches.py __
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_api_chat_internal_branches.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_api_chat_internal_branches.py:9: in <module>
    from app.api.models import ChatRequest
novapolis_agent\app\api\__init__.py:5: in <module>
    from . import sim
novapolis_agent\app\api\sim.py:6: in <module>
    import uvicorn
E   ModuleNotFoundError: No module named 'uvicorn'
__________ ERROR collecting novapolis_agent/tests/test_api_health.py __________
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_api_health.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_api_health.py:6: in <module>
    from app.main import app
novapolis_agent\app\main.py:12: in <module>
    import fastapi as _fastapi
E   ModuleNotFoundError: No module named 'fastapi'
________ ERROR collecting novapolis_agent/tests/test_api_sim_state.py _________
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_api_sim_state.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_api_sim_state.py:4: in <module>
    from app.api import sim
novapolis_agent\app\api\__init__.py:5: in <module>
    from . import sim
novapolis_agent\app\api\sim.py:6: in <module>
    import uvicorn
E   ModuleNotFoundError: No module named 'uvicorn'
______ ERROR collecting novapolis_agent/tests/test_app_404_request_id.py ______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_404_request_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_404_request_id.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
_____ ERROR collecting novapolis_agent/tests/test_app_chat_post_error.py ______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_chat_post_error.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_chat_post_error.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
_____ ERROR collecting novapolis_agent/tests/test_app_chat_post_happy.py ______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_chat_post_happy.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_a