---
stand: 2026-01-07 09:01
update: Ran pytest -q at repo root
checks: returncode=2
---

# Postflight: pytest root

Log: F:\VS Code Workspace\Main\.tmp\results\reports\pytest_root_20260107_090133.log

Output (truncated):


=================================== ERRORS ====================================
__ ERROR collecting novapolis_agent/tests/scripts/test_run_eval_cli_hint.py ___
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_run_eval_cli_hint.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_run_eval_cli_hint.py:2: in <module>
    from scripts.agent.run_eval import EvaluationItem, run_evaluation
E   ModuleNotFoundError: No module named 'scripts.agent'
_ ERROR collecting novapolis_agent/tests/scripts/test_run_eval_hint_injection.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_run_eval_hint_injection.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_run_eval_hint_injection.py:1: in <module>
    from scripts.agent.run_eval import inject_eval_hint
E   ModuleNotFoundError: No module named 'scripts.agent'
_ ERROR collecting novapolis_agent/tests/scripts/test_run_eval_hint_terms.py __
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\scripts\test_run_eval_hint_terms.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\scripts\test_run_eval_hint_terms.py:4: in <module>
    from scripts.agent.run_eval import EvaluationItem, compute_hint_terms
E   ModuleNotFoundError: No module named 'scripts.agent'
____ ERROR collecting novapolis_agent/tests/test_dependency_check_utils.py ____
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_dependency_check_utils.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_dependency_check_utils.py:6: in <module>
    from scripts.agent.dependency_check import coerce_json_to_jsonl
E   ModuleNotFoundError: No module named 'scripts.agent'
_________ ERROR collecting novapolis_agent/tests/test_eval_loader.py __________
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_eval_loader.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_eval_loader.py:8: in <module>
    from scripts.agent.run_eval import load_prompts
E   ModuleNotFoundError: No module named 'scripts.agent'
____ ERROR collecting novapolis_agent/tests/test_map_reduce_summary_llm.py ____
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_map_reduce_summary_llm.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_map_reduce_summary_llm.py:5: in <module>
    import scripts.agent.map_reduce_summary_llm as mr
E   ModuleNotFoundError: No module named 'scripts.agent'
_ ERROR collecting novapolis_agent/tests/test_prepare_finetune_alpaca_edgecases.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_prepare_finetune_alpaca_edgecases.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_prepare_finetune_alpaca_edgecases.py:8: in <module>
    from scripts.agent.prepare_finetune_pack import prepare_pack
E   ModuleNotFoundError: No module named 'scripts.agent'
__ ERROR collecting novapolis_agent/tests/test_prepare_finetune_near_dup.py ___
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_prepare_finetune_near_dup.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_prepare_finetune_near_dup.py:7: in <module>
    from scripts.agent.prepare_finetune_pack import prepare_pack
E   ModuleNotFoundError: No module named 'scripts.agent'
_ ERROR collecting novapolis_agent/tests/test_prepare_finetune_pack_extras.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_prepare_finetune_pack_extras.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_prepare_finetune_pack_extras.py:8: in <module>
    from scripts.agent.prepare_finetune_pack import prepare_pack
E   ModuleNotFoundError: No module named 'scripts.agent'
_ ERROR collecting novapolis_agent/tests/test_prepare_finetune_pack_nodedupe.py _
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_prepare_finetune_pack_nodedupe.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_prepare_finetune_pack_nodedupe.py:8: in <module>
    from scripts.agent.prepare_finetune_pack import prepare_pack
E   ModuleNotFoundError: No module named 'scripts.agent'
______ ERROR collecting novapolis_agent/tests/test_quick_eval_sanity.py _______
ImportError while importing test module 'F:\VS Code Workspace\Main\novapolis_agent\tests\test_quick_eval_sanity.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\FloAu\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
novapolis_agent\tests\test_quick_eval_sanity.py:6: in <module>
    import scripts.agent.quick_eval as qe
E   ModuleNotFoundError: No module named 'scripts.agent'
=========================== short test summary info ===========================
ERROR novapolis_agent/tests/scripts/test_run_eval_cli_hint.py
ERROR novapolis_agent/tests/scripts/test_run_eval_hint_injection.py
ERROR novapolis_agent/tests/scripts/test_run_eval_hint_terms.py
ERROR novapolis_agent/tests/test_dependency_check_utils.py
ERROR novapolis_agent/tests/test_eval_loader.py
ERROR novapolis_agent/tests/test_map_reduce_summary_llm.py
ERROR novapolis_agent/tests/test_prepare_finetune_alpaca_edgecases.py
ERROR novapolis_agent/tests/test_prepare_finetune_near_dup.py
ERROR novapolis_agent/tests/test_prepare_finetune_pack_extras.py
ERROR novapolis_agent/tests/test_prepare_finetune_pack_nodedupe.py
ERROR novapolis_agent/tests/test_quick_eval_sanity.py
!!!!!!!!!!!!!!!!!! Interrupted: 11 errors during collection !!!!!!!!!!!!!!!!!!!
