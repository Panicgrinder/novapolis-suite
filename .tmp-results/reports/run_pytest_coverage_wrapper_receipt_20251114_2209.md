---
stand: 2025-11-14 22:09
checks: PASS
---

Wrapper run receipt


- wrapper: f:\VS Code Workspace\Main\scripts\task_wrappers\run_pytest_coverage.py
- sha256: c2d9f12fdb425ba0e491577c4b5580de8edfd6a4eb0da7e8ac83c521b4ddce62
- python: f:\VS Code Workspace\Main\.venv\Scripts\python.exe
- invocation: f:\VS Code Workspace\Main\.venv\Scripts\python.exe f:\VS Code Workspace\Main\scripts\task_wrappers\run_pytest_coverage.py
- exitcode: 0

Output (truncated 10000 chars):

```
........................................................................ [ 24%]
.........s.............................................................. [ 48%]
........................................................................ [ 72%]
........................................................................ [ 96%]
...........                                                              [100%]
============================== warnings summary ===============================
tests/scripts/test_open_latest_summary_edges.py::test_open_latest_summary_empty_dir
  <frozen runpy>:128: RuntimeWarning: 'scripts.open_latest_summary' found in sys.modules after import of package 'scripts', but prior to execution of 'scripts.open_latest_summary'; this may result in unpredictable behaviour

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================== tests coverage ================================
_______________ coverage: platform win32, python 3.13.2-final-0 _______________

Name                                             Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------------------------------
app\__init__.py                                      2      0      0      0   100%
app\api\__init__.py                                  3      0      0      0   100%
app\api\api.py                                       2      0      0      0   100%
app\api\chat.py                                    525    176    188     38    65%   20, 31-50, 66-67, 75-77, 87-89, 93->102, 98, 110-111, 112->117, 114, 126->147, 130->147, 140-144, 155-160, 164-165, 169, 180, 198-222, 231-236, 245->249, 249->262, 251->262, 259, 275, 312, 321->334, 323, 351-384, 401, 409, 419-421, 434, 449-450, 454, 494-496, 504-506, 510->519, 513-515, 527-528, 529->534, 531, 536-565, 576-577, 579-584, 588-589, 595, 605, 612->621, 622, 635, 644-649, 656-675, 692, 741, 763, 775, 790, 800-801, 814-815, 827-828, 833-834, 836
app\api\chat_helpers.py                            118      4     56     15    89%   27, 50-51, 63->69, 87, 105->108, 113->116, 117->120, 121->124, 129->132, 137->140, 141->144, 145->148, 149->151, 152->154, 155->158, 159->162
app\api\models.py                                   58      3      8      1    94%   50-52
app\api\sim.py                                      41      0      2      0   100%
app\core\__init__.py                                 2      0      0      0   100%
app\core\content_management.py                     206     27     66     12    85%   23-25, 29-35, 39, 89-90, 95, 98, 103, 182-183, 192-193, 194->189, 210, 212->257, 217, 222->224, 225->227, 231->233, 245->247, 255-256, 301-302, 321-322, 325-326, 330->333, 347-348
app\core\memory.py                                 149     12     36      5    91%   24, 29, 32, 58->61, 62->exit, 64, 124-125, 144->exit, 146, 159-160, 167-169
app\core\mode.py                                    61      0     24      0   100%
app\core\prompts.py                                  3      0      0      0   100%
app\core\settings.py                               107      3     16      4    94%   115-116, 128->126, 136->145, 140->138, 146
app\main.py                                        159     16     36      7    88%   87, 133, 138, 172, 190->196, 194, 201, 207, 212-215, 223->225, 291-295
app\prompt\__init__.py                               1      0      0      0   100%
app\routers\__init__.py                              1      0      0      0   100%
app\services\__init__.py                             3      0      0      0   100%
app\services\llm.py                                 56      1      6      1    97%   51->56, 59
app\tools\registry.py                               48      2     14      1    95%   15, 45
app\utils\__init__.py                                0      0      0      0   100%
app\utils\convlog.py                                22      0      6      3    89%   24->26, 26->28, 28->30
app\utils\session_memory.py                         23      0      6      1    97%   30->33
app\utils\summarize.py                              42      0     14      1    98%   31->35
scripts\__init__.py                                  0      0      0      0   100%
scripts\append_done.py                              48      1     10      2    95%   26->30, 59->68, 66
scripts\audit_workspace.py                         150     16     88     10    88%   30, 31->33, 60-62, 92, 95->94, 121->120, 132-133, 163->173, 169-170, 179-180, 186-190, 193, 196-200
scripts\curate_dataset_from_latest.py              126     29     52     14    71%   36, 57-58, 119-120, 137-138, 159, 181, 190, 202, 210, 213-230, 233->238, 239-244, 247->250, 249, 287-288
scripts\customize_prompts.py                        96     16     16      6    80%   55-56, 81-82, 106-111, 132-133, 138-139, 165, 167
scripts\dependency_check.py                        178     40     74     19    73%   26, 35-36, 54->53, 57, 72-74, 85-86, 93, 100-101, 105, 117-118, 128, 132, 145->144, 159->153, 170-171, 181-182, 188, 192-212, 235-252
scripts\export_finetune.py                         127     14     50      9    87%   24, 30, 67-68, 71->63, 79, 90->84, 111-112, 128-129, 138, 140->147, 145, 151, 169, 204
scripts\fine_tune_pipeline.py                       68     13     16      2    80%   42-56, 106->117, 109->117
scripts\map_reduce_summary.py                      213     22     82     16    86%   71, 74-75, 83-85, 100->99, 127->130, 134, 152, 155->149, 157-161, 171->175, 177-179, 187->186, 199->204, 201->204, 210, 236, 243-244, 280, 283, 308-309
scripts\map_reduce_summary_llm.py                  192     67     50      9    63%   28-34, 40->exit, 41->exit, 49-59, 92-93, 105-106, 116, 124-138, 145, 157-203, 223, 230-234, 248-253, 271-272, 283-284, 334, 350, 385-386, 390
scripts\migrate_dataset_schemas.py                  90     28     36      5    71%   36->56, 40-41, 46, 49->44, 53-54, 57-58, 81-89, 115-117, 122-137
scripts\open_context_notes.py                       50      3     16      3    91%   11->27, 51, 62, 64
scripts\open_latest_summary.py                      46      2     16      2    94%   38, 40
scripts\openai_ft_status.py                         74      5     26      6    89%   22, 60->exit, 73, 75, 86->84, 109, 111
scripts\reports\generate_consistency_report.py      57     23     10      1    58%   16, 28, 32-57
scripts\rerun_failed.py                            106     12     42     10    85%   39, 42-43, 50, 55->36, 70, 73-74, 76, 79->67, 87, 91->85, 94, 97->92, 101-102
scripts\rerun_from_results.py                       97     18     20      6    79%   19, 39, 49-52, 60-62, 66, 100->107, 141->144, 148-167
--------------------------------------------------------------------------------------------
TOTAL                                             3350    553   1082    209    81%
Coverage XML written to file F:\VS Code Workspace\Main\outputs\test-artifacts\coverage.xml
Required test coverage of 80% reached. Total coverage: 80.96%
298 passed, 1 skipped, 1 warning in 48.63s
Running: F:\VS Code Workspace\Main\.venv\Scripts\python.exe -m pytest --cov --cov-report=term-missing --cov-branch --cov-config=F:\VS Code Workspace\Main\novapolis_agent\.coveragerc --cov-report=xml:F:\VS Code Workspace\Main\outputs\test-artifacts\coverage.xml --junitxml=F:\VS Code Workspace\Main\outputs\test-artifacts\junit.xml --cov-fail-under=80
Pytest PASS

```


Summary file contents:

```
timestamp: 2025-11-14 22:09
exitcode: 0
junit: F:\VS Code Workspace\Main\outputs\test-artifacts\junit.xml
coverage_xml: F:\VS Code Workspace\Main\outputs\test-artifacts\coverage.xml
```
