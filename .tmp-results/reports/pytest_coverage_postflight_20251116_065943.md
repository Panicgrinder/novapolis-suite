........................................................................ [ 24%]
.........s.............................................................. [ 48%]
........................................................................ [ 72%]
........................................................................ [ 96%]
...........
ERROR: Coverage failure: total of 79 is less than fail-under=80
                                                                         [100%]
============================== warnings summary ===============================
novapolis_agent/tests/scripts/test_open_latest_summary_edges.py::test_open_latest_summary_empty_dir
  <frozen runpy>:128: RuntimeWarning: 'scripts.open_latest_summary' found in sys.modules after import of package 'scripts', but prior to execution of 'scripts.open_latest_summary'; this may result in unpredictable behaviour

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================== tests coverage ================================
_______________ coverage: platform win32, python 3.13.2-final-0 _______________

Name                                                                             Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------------------------------------------------
novapolis_agent\__init__.py                                                          6      0      0      0   100%
novapolis_agent\app\__init__.py                                                      2      0      0      0   100%
novapolis_agent\app\api\__init__.py                                                  3      0      0      0   100%
novapolis_agent\app\api\api.py                                                       2      0      0      0   100%
novapolis_agent\app\api\chat.py                                                    528    181    180     37    65%   38-39, 47-50, 59-62, 65->74, 70-71, 82-83, 84->89, 86-87, 98->119, 102->119, 112-117, 127-132, 136-137, 141-142, 152, 170-195, 203-208, 217->221, 221->234, 223->234, 231-232, 247, 284-285, 293->306, 295, 323-356, 373-374, 381-382, 391-394, 406, 421-422, 426, 466-469, 476-479, 482->491, 485-488, 499-500, 501->506, 503-504, 508-538, 548-549, 551-556, 560-561, 567-568, 577, 584->593, 594, 607-608, 616-621, 628-648, 664, 713, 735, 747, 762-763, 772-773, 786-787, 799-800, 805-806, 808
novapolis_agent\app\api\chat_helpers.py                                            118      4     56     15    89%   27, 50-51, 63->69, 87, 105->108, 113->116, 117->120, 121->124, 129->132, 137->140, 141->144, 145->148, 149->151, 152->154, 155->158, 159->162
novapolis_agent\app\api\models.py                                                   58      3      8      1    94%   50-52
novapolis_agent\app\api\sim.py                                                      41      0      2      0   100%
novapolis_agent\app\core\__init__.py                                                 2      0      0      0   100%
novapolis_agent\app\core\content_management.py                                     219     30     74     13    85%   23-25, 29-35, 39, 89-90, 95, 98, 103, 182-183, 192-193, 194->189, 210, 212->257, 217, 222->224, 225->227, 231->233, 245->247, 255-256, 263, 266-267, 301-302, 321-322, 325-326, 330->333, 347-348
novapolis_agent\app\core\memory.py                                                 150     14     36      6    89%   24, 29, 32, 58->61, 62->exit, 64, 124-125, 144->exit, 146-147, 159-160, 167-169, 196
novapolis_agent\app\core\mode.py                                                    61      0     24      0   100%
novapolis_agent\app\core\prompts.py                                                  3      0      0      0   100%
novapolis_agent\app\core\settings.py                                               108      3     16      4    94%   115-116, 128->126, 136->145, 140->138, 146
novapolis_agent\app\main.py                                                        162     19     36      7    87%   87-88, 133-134, 138, 172, 190->196, 194-195, 201, 207, 212-215, 223->225, 291-295
novapolis_agent\app\prompt\__init__.py                                               1      0      0      0   100%
novapolis_agent\app\routers\__init__.py                                              1      0      0      0   100%
novapolis_agent\app\services\__init__.py                                             3      0      0      0   100%
novapolis_agent\app\services\llm.py                                                 58      2      6      1    95%   51->56, 59-60
novapolis_agent\app\tools\registry.py                                               46      1     14      1    97%   45
novapolis_agent\app\utils\__init__.py                                                0      0      0      0   100%
novapolis_agent\app\utils\convlog.py                                                22      0      6      3    89%   24->26, 26->28, 28->30
novapolis_agent\app\utils\session_memory.py                                         23      0      6      1    97%   30->33
novapolis_agent\app\utils\summarize.py                                              42      0     14      1    98%   31->35
novapolis_agent\scripts\__init__.py                                                  0      0      0      0   100%
novapolis_agent\scripts\append_done.py                                              52      3     12      3    91%   27->31, 60->69, 67-68, 76
novapolis_agent\scripts\audit_workspace.py                                         153     18     90     11    87%   31, 32->34, 61-64, 93, 96->95, 122->121, 133-134, 164->174, 170-171, 180-181, 187-191, 194, 197-201, 207
novapolis_agent\scripts\curate_dataset_from_latest.py                              128     30     54     15    71%   37, 58-59, 120-121, 138-139, 160, 182, 191, 203, 211, 214-231, 234->239, 240-245, 248->251, 250, 288-289, 305
novapolis_agent\scripts\customize_prompts.py                                       101     17     18      7    80%   55-56, 81-82, 106-111, 132-133, 138-139, 165, 167, 173
novapolis_agent\scripts\dependency_check.py                                        182     42     76     20    73%   26, 35-36, 54->53, 57, 72-74, 85-86, 93, 100-101, 105, 117-118, 128, 132, 145->144, 159->153, 170-171, 181-182, 188, 192-212, 235-252, 267
novapolis_agent\scripts\estimate_tokens.py                                          59      9     14      4    82%   14->23, 19, 45-48, 71, 82-83, 109
novapolis_agent\scripts\eval_ui.py                                                 554    457    208      9    15%   30, 36, 50, 70-71, 84-120, 124-130, 134-138, 142-155, 164->exit, 206-215, 219-291, 295-408, 418, 421, 448, 451, 455-457, 461-626, 630-685, 694-730, 734-774, 778-820, 824-859, 863
novapolis_agent\scripts\export_finetune.py                                         142     28     54     10    80%   25, 31, 68-69, 72->64, 80, 91->85, 112-113, 129-130, 139, 141->148, 146-147, 152-153, 170, 205, 214-237
novapolis_agent\scripts\fine_tune_pipeline.py                                       71     15     18      3    78%   43-57, 107->118, 110->118, 149
novapolis_agent\scripts\map_reduce_summary.py                                      215     23     84     17    86%   72, 75-76, 84-86, 101->100, 128->131, 135, 153, 156->150, 158-162, 172->176, 178-180, 188->187, 200->205, 202->205, 211, 237, 244-245, 281, 284, 309-310, 316
novapolis_agent\scripts\map_reduce_summary_llm.py                                  190     67     46      7    63%   29-35, 50-60, 93-94, 106-107, 117, 125-139, 158-204, 224, 231-235, 249-254, 272-273, 284-285, 335, 351, 386-387, 391, 395
novapolis_agent\scripts\migrate_dataset_schemas.py                                  92     29     38      6    70%   37->57, 41-42, 47, 50->45, 54-55, 58-59, 82-90, 116-118, 123-138, 142
novapolis_agent\scripts\open_context_notes.py                                       53      5     18      4    87%   11->27, 51-52, 62, 64, 85
novapolis_agent\scripts\open_latest_summary.py                                      49      2     18      2    94%   38, 40
novapolis_agent\scripts\openai_finetune.py                                          79     43     24      5    44%   21, 30-31, 38, 47, 53, 55, 76-140
novapolis_agent\scripts\openai_ft_status.py                                         77      7     28      7    87%   23-24, 61->exit, 74, 76, 87->85, 110, 112, 126
novapolis_agent\scripts\prepare_finetune_pack.py                                   111     21     46      8    80%   27, 30->24, 33-34, 46->45, 48, 58, 67, 81, 151-180
novapolis_agent\scripts\quick_eval.py                                               31      4      4      2    83%   23, 48-49, 69
novapolis_agent\scripts\reports\generate_consistency_report.py                      59     24     12      2    58%   17, 29, 33-58, 92
novapolis_agent\scripts\rerun_failed.py                                            108     13     44     11    84%   40, 43-44, 51, 56->37, 71, 74-75, 77, 80->68, 88, 92->86, 95, 98->93, 102-103, 139
novapolis_agent\scripts\rerun_from_results.py                                      100     20     24      8    77%   19, 39, 49-52, 60-62, 66, 73, 100->107, 141->144, 148-167, 171
novapolis_agent\scripts\run_eval.py                                               1150    705    502     51    38%   32-37, 42, 46-48, 51, 54, 57-64, 68-69, 72, 75, 78-80, 83-85, 95, 116-122, 151-160, 256, 265-266, 295, 300, 308, 314->319, 371, 378, 391->390, 417-418, 435, 480-481, 493-494, 509->497, 527-534, 542, 544, 549, 580->584, 585-586, 594-606, 614, 647-654, 668-670, 706, 772, 780-796, 799-821, 835, 837, 839-842, 859-873, 886-889, 926-930, 934-946, 951-973, 977-981, 985-994, 1004-1005, 1018-1023, 1026-1235, 1252-1256, 1304-1305, 1311-1552, 1562-1653, 1712-1742, 1767, 1770, 1780->1794, 1782->1794, 1787-1788, 1791, 1797->1806, 1800->1806, 1804-1805, 1811-1822, 1828, 1853, 1867-1886, 1954, 1982-1984, 1989-2389
novapolis_agent\scripts\run_tests.py                                                18      1      2      1    90%   28
novapolis_agent\scripts\smoke_asgi.py                                               32      5      6      3    79%   16, 46-49, 54
novapolis_agent\scripts\todo_gather.py                                             141     14     38     10    87%   43, 46-47, 54->56, 64->40, 88-95, 114, 136->140, 162, 163->171, 167-170, 222
novapolis_agent\tests\__init__.py                                                    0      0      0      0   100%
novapolis_agent\tests\scripts\test_append_done_additional.py                        59      0      0      0   100%
novapolis_agent\tests\scripts\test_append_done_error_path.py                        11      0      0      0   100%
novapolis_agent\tests\scripts\test_append_done_smoke.py                             18      0      0      0   100%
novapolis_agent\tests\scripts\test_audit_workspace_fallbacks.py                     15      0      0      0   100%
novapolis_agent\tests\scripts\test_curate_dataset_filters_empty.py                  36      1      0      0    97%   51
novapolis_agent\tests\scripts\test_curate_dataset_filters_positive.py               42      0      0      0   100%
novapolis_agent\tests\scripts\test_curate_dataset_from_latest_minimal.py            39      0      0      0   100%
novapolis_agent\tests\scripts\test_customize_prompts_io_and_cli.py                  44      0      0      0   100%
novapolis_agent\tests\scripts\test_customize_prompts_smoke.py                       24      0      0      0   100%
novapolis_agent\tests\scripts\test_customize_prompts_unrestricted.py                50      0      0      0   100%
novapolis_agent\tests\scripts\test_dependency_check_prompt_refs.py                  14      0      0      0   100%
novapolis_agent\tests\scripts\test_eval_failure_report.py                           18      0      0      0   100%
novapolis_agent\tests\scripts\test_eval_runner_overrides.py                         24      0      2      0   100%
novapolis_agent\tests\scripts\test_eval_ui_helpers_smoke.py                         31      0      0      0   100%
novapolis_agent\tests\scripts\test_eval_ui_trends_smoke.py                          23      0      0      0   100%
novapolis_agent\tests\scripts\test_export_and_prepare_pipeline_alpaca.py            30      0      0      0   100%
novapolis_agent\tests\scripts\test_export_and_rerun_missing_cases.py                30      0      0      0   100%
novapolis_agent\tests\scripts\test_export_finetune_edges.py                         48      0      0      0   100%
novapolis_agent\tests\scripts\test_export_finetune_fallback_outdir.py               30      0      0      0   100%
novapolis_agent\tests\scripts\test_export_finetune_more_edges.py                    58      0      0      0   100%
novapolis_agent\tests\scripts\test_export_finetune_openai_chat.py                   32      0      2      0   100%
novapolis_agent\tests\scripts\test_fine_tune_pipeline_edges.py                      54      0      0      0   100%
novapolis_agent\tests\scripts\test_fine_tune_pipeline_happy.py                      32      1      0      0    97%   28
novapolis_agent\tests\scripts\test_fine_tune_pipeline_interrupt_and_fp16.py         46      0      0      0   100%
novapolis_agent\tests\scripts\test_fine_tune_pipeline_smoke.py                      21      0      0      0   100%
novapolis_agent\tests\scripts\test_map_reduce_summary_heuristic_min.py              19      0      0      0   100%
novapolis_agent\tests\scripts\test_map_reduce_summary_json_modes.py                 21      0      0      0   100%
novapolis_agent\tests\scripts\test_map_reduce_summary_llm_smoke.py                  20      0      0      0   100%
novapolis_agent\tests\scripts\test_map_reduce_summary_markdown_and_excludes.py      53      0      0      0   100%
novapolis_agent\tests\scripts\test_map_reduce_summary_python_and_json.py            47      0      0      0   100%
novapolis_agent\tests\scripts\test_migrate_dataset_schemas_edges.py                 38      0      0      0   100%
novapolis_agent\tests\scripts\test_migrate_dataset_schemas_happy.py                 32      0      0      0   100%
novapolis_agent\tests\scripts\test_open_context_notes.py                           118      0      2      0   100%
novapolis_agent\tests\scripts\test_open_context_notes_happy.py                      27      0      0      0   100%
novapolis_agent\tests\scripts\test_open_context_notes_main_smoke.py                 24      0      0      0   100%
novapolis_agent\tests\scripts\test_open_context_notes_more_edges.py                 33      0      0      0   100%
novapolis_agent\tests\scripts\test_open_latest_summary.py                           98      0      0      0   100%
novapolis_agent\tests\scripts\test_open_latest_summary_edges.py                     21      3      0      0    86%   29-32
novapolis_agent\tests\scripts\test_open_latest_summary_open_mock.py                 31      5      0      0    84%   38-43
novapolis_agent\tests\scripts\test_open_latest_summary_open_path.py                 33      0      0      0   100%
novapolis_agent\tests\scripts\test_open_latest_summary_paths.py                     35      0      0      0   100%
novapolis_agent\tests\scripts\test_open_latest_summary_smoke.py                     17      0      0      0   100%
novapolis_agent\tests\scripts\test_openai_finetune_smoke.py                         54      3      0      0    94%   48-52
novapolis_agent\tests\scripts\test_openai_ft_status_stubbed.py                      70      0      0      0   100%
novapolis_agent\tests\scripts\test_prepare_pack_smoke.py                            27     14     10      1    38%   15-23, 33-39
novapolis_agent\tests\scripts\test_quick_eval_main_stubbed.py                       22      0      0      0   100%
novapolis_agent\tests\scripts\test_rerun_failed_json_array.py                       34      0      0      0   100%
novapolis_agent\tests\scripts\test_rerun_failed_no_results.py                       20      0      0      0   100%
novapolis_agent\tests\scripts\test_rerun_failed_only_success.py                     20      0      0      0   100%
novapolis_agent\tests\scripts\test_rerun_failed_smoke.py                            31      0      0      0   100%
novapolis_agent\tests\scripts\test_run_eval_cli_hint.py                             11      1      0      0    91%   23
novapolis_agent\tests\scripts\test_run_eval_hint_injection.py                       15      0      0      0   100%
novapolis_agent\tests\scripts\test_run_eval_hint_terms.py                           12      0      0      0   100%
novapolis_agent\tests\scripts\test_run_eval_no_files_smoke.py                       13      0      0      0   100%
novapolis_agent\tests\scripts\test_run_eval_term_helpers.py                         30      1      4      1    94%   33
novapolis_agent\tests\scripts\test_run_tests_error_path.py                          13      0      0      0   100%
novapolis_agent\tests\scripts\test_run_tests_script_smoke.py                        19      0      0      0   100%
novapolis_agent\tests\scripts\test_todo_gather_smoke.py                             22      0      0      0   100%
novapolis_agent\tests\test_api_chat_internal_branches.py                           186      0      2      1    99%   27->exit
novapolis_agent\tests\test_api_health.py                                            14      0      0      0   100%
novapolis_agent\tests\test_api_sim_state.py                                         32      0      0      0   100%
novapolis_agent\tests\test_app_404_request_id.py                                    12      0      0      0   100%
novapolis_agent\tests\test_app_chat_post_error.py                                   18      0      0      0   100%
novapolis_agent\tests\test_app_chat_post_happy.py                                   32      0      0      0   100%
novapolis_agent\tests\test_app_chat_post_internal_error.py                          18      0      0      0   100%
novapolis_agent\tests\test_app_chat_stream_error.py                                 21      0      0      0   100%
novapolis_agent\tests\test_app_docs_available.py                                    12      0      0      0   100%
novapolis_agent\tests\test_app_health_request_id.py                                 12      0      0      0   100%
novapolis_agent\tests\test_app_rate_limit_headers.py                                20      0      0      0   100%
novapolis_agent\tests\test_app_redoc_available.py                                   12      0      0      0   100%
novapolis_agent\tests\test_app_request_id_on_400.py                                 21      0      0      0   100%
novapolis_agent\tests\test_app_root_endpoint.py                                     12      0      0      0   100%
novapolis_agent\tests\test_app_root_message.py                                      13      0      0      0   100%
novapolis_agent\tests\test_app_root_request_id.py                                   12      0      0      0   100%
novapolis_agent\tests\test_app_version_endpoint.py                                  31      0      0      0   100%
novapolis_agent\tests\test_audit_workspace_reachability.py                          29      0      0      0   100%
novapolis_agent\tests\test_audit_workspace_references.py                            28      0      2      0   100%
novapolis_agent\tests\test_audit_workspace_smoke.py                                 26      0      2      0   100%
novapolis_agent\tests\test_chai_checks.py                                           22      0      0      0   100%
novapolis_agent\tests\test_chat_endpoint_prompt_injection.py                        70      3      2      1    94%   22-23, 27
novapolis_agent\tests\test_chat_helpers_and_options.py                             171      0      2      0   100%
novapolis_agent\tests\test_chat_