---
stand: 2026-01-07 09:03
update: Ran pytest -q at repo root
checks: returncode=1
---

# Postflight: pytest root

Log: F:\VS Code Workspace\Main\.tmp\results\reports\pytest_root_20260107_090239.log

Output (truncated):

........................................................................ [ 20%]
.........s.............................................................. [ 40%]
........................................................................ [ 60%]
.................................F...................................... [ 81%]
...................................................................      [100%]
================================== FAILURES ===================================
______________________ test_process_scope_llm_uses_stub _______________________

tmp_path = WindowsPath('C:/Users/FloAu/AppData/Local/Temp/pytest-of-FloAu/pytest-144/test_process_scope_llm_uses_st0')

    @pytest.mark.asyncio
    async def test_process_scope_llm_uses_stub(tmp_path):
        # Arrange: create a small text file
        base = Path(mr.PROJECT_ROOT) / ".__tmp_tests__" / "llm"
        base.mkdir(parents=True, exist_ok=True)
        p: Path = base / "sample.md"
        p.write_text("Hello World", encoding="utf-8")
    
        called: list[str] = []
    
        async def fake_llm(
            client,
            api_url: str,
            path: str,
            run_id: str,
            max_chars: int,
            num_predict: int,
            temperature: float,
        ) -> str:
            called.append(path)
            # keep it simple to avoid cross-drive relpath issues
            return f"Datei: {os.path.basename(path)}\nZusammenfassung: OK"
    
        # Patch llm function
        orig = mr.llm_summarize_file
        mr.llm_summarize_file = fake_llm
        try:
            # Act: use use_llm=True, but with stubbed function, no network used
            res = await mr.process_scope(
                scope="tmp",
                scope_dir=str(base),
                use_llm=True,
                api_url="http://unused/chat",
                asgi=False,
                run_id="run1",
                max_files=0,
                max_chars=200,
                num_predict=128,
                temperature=0.1,
                concurrency=1,
            )
        finally:
            mr.llm_summarize_file = orig
            try:
                import shutil
    
                shutil.rmtree(base.parent)
            except Exception:
                pass
    
        # Assert
        assert len(res) == 1
>       assert "Zusammenfassung: OK" in res[0]
E       AssertionError: assert 'Zusammenfassung: OK' in 'Datei: .__tmp_tests__\\llm\\sample.md\nHello World'

novapolis_agent\tests\test_map_reduce_summary_llm.py:60: AssertionError
============================== warnings summary ===============================
novapolis_agent/tests/scripts/test_open_latest_summary_edges.py::test_open_latest_summary_empty_dir
  <frozen runpy>:128: RuntimeWarning: 'scripts.open_latest_summary' found in sys.modules after import of package 'scripts', but prior to execution of 'scripts.open_latest_summary'; this may result in unpredictable behaviour

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
FAILED novapolis_agent/tests/test_map_reduce_summary_llm.py::test_process_scope_llm_uses_stub
