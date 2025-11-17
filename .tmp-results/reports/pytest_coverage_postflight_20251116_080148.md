---
stand: 2025-11-16 08:01
update: Ran pytest with coverage
checks: returncode=2
---

# Postflight: pytest coverage

Log: F:\VS Code Workspace\Main\.tmp-results\reports\pytest_coverage_20251116_080148.log

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
E   ModuleNotFoundError: No module named 'app'
__________ ERROR collecting novapolis_agent/tests/test_api_health.py __________
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_api_health.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_api_health.py:6: in <module>
    from app.main import app
E   ModuleNotFoundError: No module named 'app'
________ ERROR collecting novapolis_agent/tests/test_api_sim_state.py _________
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_api_sim_state.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_api_sim_state.py:4: in <module>
    from app.api import sim
E   ModuleNotFoundError: No module named 'app'
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
novapolis_agent\tests\test_app_chat_post_happy.py:6: in <module>
    from app.main import app
E   ModuleNotFoundError: No module named 'app'
_ ERROR collecting novapolis_agent/tests/test_app_chat_post_internal_error.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_chat_post_internal_error.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_chat_post_internal_error.py:5: in <module>
    import app.main as app_main
E   ModuleNotFoundError: No module named 'app'
____ ERROR collecting novapolis_agent/tests/test_app_chat_stream_error.py _____
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_chat_stream_error.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_chat_stream_error.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
______ ERROR collecting novapolis_agent/tests/test_app_docs_available.py ______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_docs_available.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_docs_available.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
____ ERROR collecting novapolis_agent/tests/test_app_health_request_id.py _____
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_health_request_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_health_request_id.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
____ ERROR collecting novapolis_agent/tests/test_app_rate_limit_headers.py ____
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_rate_limit_headers.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_rate_limit_headers.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
_____ ERROR collecting novapolis_agent/tests/test_app_redoc_available.py ______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_redoc_available.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_redoc_available.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
____ ERROR collecting novapolis_agent/tests/test_app_request_id_on_400.py _____
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_request_id_on_400.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_request_id_on_400.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
______ ERROR collecting novapolis_agent/tests/test_app_root_endpoint.py _______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_root_endpoint.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_root_endpoint.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
_______ ERROR collecting novapolis_agent/tests/test_app_root_message.py _______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_root_message.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_root_message.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
_____ ERROR collecting novapolis_agent/tests/test_app_root_request_id.py ______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_root_request_id.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_root_request_id.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
_____ ERROR collecting novapolis_agent/tests/test_app_version_endpoint.py _____
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_app_version_endpoint.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_app_version_endpoint.py:6: in <module>
    from fastapi.testclient import TestClient
E   ModuleNotFoundError: No module named 'fastapi'
_ ERROR collecting novapolis_agent/tests/test_chat_endpoint_prompt_injection.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_chat_endpoint_prompt_injection.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_chat_endpoint_prompt_injection.py:6: in <module>
    import app.api.chat as chat_module
novapolis_agent\app\api\__init__.py:5: in <module>
    from . import sim
novapolis_agent\app\api\sim.py:6: in <module>
    import uvicorn
E   ModuleNotFoundError: No module named 'uvicorn'
___ ERROR collecting novapolis_agent/tests/test_chat_helpers_and_options.py ___
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_chat_helpers_and_options.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_chat_helpers_and_options.py:8: in <module>
    from app.api.models import ChatRequest
novapolis_agent\app\api\__init__.py:5: in <module>
    from . import sim
novapolis_agent\app\api\sim.py:6: in <module>
    import uvicorn
E   ModuleNotFoundError: No module named 'uvicorn'
___ ERROR collecting novapolis_agent/tests/test_chat_options_and_context.py ___
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_chat_options_and_context.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_chat_options_and_context.py:6: in <module>
    import app.api.chat as chat_module
novapolis_agent\app\api\__init__.py:5: in <module>
    from . import sim
novapolis_agent\app\api\sim.py:6: in <module>
    import uvicorn
E   ModuleNotFoundError: No module named 'uvicorn'
__ ERROR collecting novapolis_agent/tests/test_chat_stream_backend_error.py ___
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_chat_stream_backend_error.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(n