---
stand: 2026-01-07 10:06
update: Ran pytest -q at repo root
checks: returncode=1
---

# Postflight: pytest root

Log: F:\VS Code Workspace\Main\.tmp\results\reports\pytest_root_20260107_100600.log

Output (truncated):

.............................F.......................................... [ 20%]
.........s.............................................................. [ 40%]
........................................................................ [ 60%]
........................................................................ [ 81%]
...................................................................      [100%]
================================== FAILURES ===================================
_______________ test_export_out_dir_none_uses_settings_fallback _______________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x0000017E7DA96E90>
tmp_path = WindowsPath('C:/Users/FloAu/AppData/Local/Temp/pytest-of-FloAu/pytest-2/test_export_out_dir_none_uses_0')

    @pytest.mark.scripts
    @pytest.mark.unit
    def test_export_out_dir_none_uses_settings_fallback(
        monkeypatch: pytest.MonkeyPatch, tmp_path: os.PathLike[str]
    ) -> None:
        # Stelle settings so ein, dass EVAL_RESULTS_DIR auf einen temporären Unterpfad zeigt
        import app.core.settings as settings_mod
    
        from novapolis_agent.scripts import export_finetune as exporter
    
        monkeypatch.setattr(
            settings_mod.settings,
            "EVAL_RESULTS_DIR",
            os.path.join("eval", "results", "tmp-export"),
            raising=False,
        )
    
        ds = os.path.join(tmp_path, "d.jsonl")
        _write_dataset_messages(ds, "item-2", [{"role": "user", "content": "X"}])
        res = os.path.join(tmp_path, "r.jsonl")
        _write_results_single(res, "item-2", success=True, response="R2")
    
        out = asyncio.run(
            exporter.export_from_results(
                res, out_dir=None, format="alpaca", include_failures=False, patterns=[ds]
            )
        )
        assert out.get("ok")
        out_path = str(out.get("out"))
        # sollte innerhalb des projekt-root eval/results/tmp-export landen
>       assert "eval" in out_path.replace("\\", "/") and "tmp-export" in out_path.replace("\\", "/")
E       AssertionError: assert ('eval' in 'F:/VS Code Workspace/Main/novapolis_agent/eval/results/finetune_alpaca_r_20260107_1006.jsonl' and 'tmp-export' in 'F:/VS Code Workspace/Main/novapolis_agent/eval/results/finetune_alpaca_r_20260107_1006.jsonl')
E        +  where 'F:/VS Code Workspace/Main/novapolis_agent/eval/results/finetune_alpaca_r_20260107_1006.jsonl' = <built-in method replace of str object at 0x0000017E7DAB1A10>('\\', '/')
E        +    where <built-in method replace of str object at 0x0000017E7DAB1A10> = 'F:\\VS Code Workspace\\Main\\novapolis_agent\\eval\\results\\finetune_alpaca_r_20260107_1006.jsonl'.replace
E        +  and   'F:/VS Code Workspace/Main/novapolis_agent/eval/results/finetune_alpaca_r_20260107_1006.jsonl' = <built-in method replace of str object at 0x0000017E7DAB1A10>('\\', '/')
E        +    where <built-in method replace of str object at 0x0000017E7DAB1A10> = 'F:\\VS Code Workspace\\Main\\novapolis_agent\\eval\\results\\finetune_alpaca_r_20260107_1006.jsonl'.replace

novapolis_agent\tests\scripts\test_export_finetune_more_edges.py:111: AssertionError
============================== warnings summary ===============================
novapolis_agent/tests/scripts/test_open_latest_summary_edges.py::test_open_latest_summary_empty_dir
  <frozen runpy>:128: RuntimeWarning: 'scripts.open_latest_summary' found in sys.modules after import of package 'scripts', but prior to execution of 'scripts.open_latest_summary'; this may result in unpredictable behaviour

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
FAILED novapolis_agent/tests/scripts/test_export_finetune_more_edges.py::test_export_out_dir_none_uses_settings_fallback
