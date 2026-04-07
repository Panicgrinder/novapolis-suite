extends Node2D

const SchedulerHookRef = preload("res://scripts/scheduler_hook.gd")

signal on_action_start(action_name: String, context: Dictionary)
signal on_action_end(action_name: String, context: Dictionary)
signal on_visibility_change(visible_state: bool, reason: String)
signal on_interrupt(reason: String, context: Dictionary)

@onready var tick_label: Label = $TickLabel
@onready var time_label: Label = $TimeLabel
@onready var status_label: Label = $StatusLabel
@onready var hub_title_label: Label = $HubTitleLabel
@onready var hub_api_label: Label = $HubApiLabel
@onready var hub_polling_label: Label = $HubPollingLabel
@onready var hub_queue_label: Label = $HubQueueLabel
@onready var hub_errors_label: Label = $HubErrorsLabel
@onready var sim_card_state_label: Label = $SimCardPanel/SimCardStateLabel
@onready var sim_card_tick_label: Label = $SimCardPanel/SimCardTickLabel
@onready var sim_card_queue_label: Label = $SimCardPanel/SimCardQueueLabel
@onready var sim_card_data_label: Label = $SimCardPanel/SimCardDataLabel
@onready var sim_card_panel: Panel = $SimCardPanel
@onready var api_card_health_label: Label = $ApiCardPanel/ApiCardHealthLabel
@onready var api_card_runtime_label: Label = $ApiCardPanel/ApiCardRuntimeLabel
@onready var api_card_backoff_label: Label = $ApiCardPanel/ApiCardBackoffLabel
@onready var api_card_endpoint_label: Label = $ApiCardPanel/ApiCardEndpointLabel
@onready var api_card_panel: Panel = $ApiCardPanel
@onready var eval_card_profile_label: Label = $EvalCardPanel/EvalCardProfileLabel
@onready var eval_card_artifacts_label: Label = $EvalCardPanel/EvalCardArtifactsLabel
@onready var eval_card_events_label: Label = $EvalCardPanel/EvalCardEventsLabel
@onready var eval_card_notes_label: Label = $EvalCardPanel/EvalCardNotesLabel
@onready var eval_card_panel: Panel = $EvalCardPanel
@onready var agent_studio_panel: Panel = $AgentStudioPanel
@onready var agent_back_button: Button = $AgentStudioPanel/AgentBackButton
@onready var agent_studio_mode_label: Label = $AgentStudioPanel/AgentStudioModeLabel
@onready var agent_operate_button: Button = $AgentStudioPanel/AgentOperateButton
@onready var agent_author_button: Button = $AgentStudioPanel/AgentAuthorButton
@onready var agent_eval_run_button: Button = $AgentStudioPanel/AgentEvalRunButton
@onready var agent_eval_suite_button: OptionButton = $AgentStudioPanel/AgentEvalSuiteButton
@onready var agent_dataset_source_button: OptionButton = $AgentStudioPanel/AgentDatasetSourceButton
@onready var agent_datasets_button: Button = $AgentStudioPanel/AgentDatasetsButton
@onready var agent_synonyms_button: Button = $AgentStudioPanel/AgentSynonymsButton
@onready var agent_finetune_button: Button = $AgentStudioPanel/AgentFinetuneButton
@onready var agent_profiles_button: Button = $AgentStudioPanel/AgentProfilesButton
@onready var agent_ai_status_button: Button = $AgentStudioPanel/AgentAiStatusButton
@onready var agent_eval_status_label: Label = $AgentStudioPanel/AgentEvalStatusLabel
@onready var agent_system_metrics_label: Label = $AgentStudioPanel/AgentSystemMetricsLabel
@onready var agent_latest_runs_label: Label = $AgentStudioPanel/AgentLatestRunsLabel
@onready var agent_studio_hint_label: Label = $AgentStudioPanel/AgentStudioHintLabel
@onready var agent_form_panel: Panel = $AgentStudioPanel/AgentFormPanel
@onready var agent_form_title_label: Label = $AgentStudioPanel/AgentFormPanel/AgentFormTitleLabel
@onready var agent_form_mode_button: OptionButton = $AgentStudioPanel/AgentFormPanel/AgentFormModeButton
@onready var agent_form_target_button: OptionButton = $AgentStudioPanel/AgentFormPanel/AgentFormTargetButton
@onready var agent_form_name_edit: LineEdit = $AgentStudioPanel/AgentFormPanel/AgentFormNameEdit
@onready var agent_form_apply_button: Button = $AgentStudioPanel/AgentFormPanel/AgentFormApplyButton
@onready var agent_form_payload_edit: TextEdit = $AgentStudioPanel/AgentFormPanel/AgentFormPayloadEdit
@onready var agent_form_fields_scroll: ScrollContainer = $AgentStudioPanel/AgentFormPanel/AgentFormFieldsScroll
@onready var agent_form_fields_box: VBoxContainer = $AgentStudioPanel/AgentFormPanel/AgentFormFieldsScroll/AgentFormFieldsBox
@onready var agent_form_status_label: Label = $AgentStudioPanel/AgentFormPanel/AgentFormStatusLabel
@onready var checks_studio_panel: Panel = $ChecksStudioPanel
@onready var checks_back_button: Button = $ChecksStudioPanel/ChecksBackButton
@onready var checks_target_sim_button: Button = $ChecksStudioPanel/ChecksTargetSimButton
@onready var checks_target_agent_button: Button = $ChecksStudioPanel/ChecksTargetAgentButton
@onready var checks_target_eval_button: Button = $ChecksStudioPanel/ChecksTargetEvalButton
@onready var checks_target_workspace_button: Button = $ChecksStudioPanel/ChecksTargetWorkspaceButton
@onready var checks_type_smoke_button: Button = $ChecksStudioPanel/ChecksTypeSmokeButton
@onready var checks_type_unit_button: Button = $ChecksStudioPanel/ChecksTypeUnitButton
@onready var checks_type_api_button: Button = $ChecksStudioPanel/ChecksTypeApiButton
@onready var checks_type_lint_button: Button = $ChecksStudioPanel/ChecksTypeLintButton
@onready var checks_type_full_button: Button = $ChecksStudioPanel/ChecksTypeFullButton
@onready var checks_run_selected_button: Button = $ChecksStudioPanel/ChecksRunSelectedButton
@onready var checks_run_module_pack_button: Button = $ChecksStudioPanel/ChecksRunModulePackButton
@onready var checks_status_label: Label = $ChecksStudioPanel/ChecksStatusLabel
@onready var checks_output_label: RichTextLabel = $ChecksStudioPanel/ChecksOutputLabel
@onready var rp_studio_panel: Panel = $RpStudioPanel
@onready var rp_back_button: Button = $RpStudioPanel/RpBackButton
@onready var rp_hour_plus_button: Button = $RpStudioPanel/RpHourPlusButton
@onready var rp_auto_advance_button: Button = $RpStudioPanel/RpAutoAdvanceButton
@onready var rp_replay_seed_label: Label = $RpStudioPanel/RpReplaySeedLabel
@onready var rp_status_label: Label = $RpStudioPanel/RpStatusLabel
@onready var epoch_label: Label = $EpochLabel
@onready var slot_label: Label = $SlotLabel
@onready var log_label: RichTextLabel = $PcLogLabel
@onready var epoch_status_label: Label = $EpochStatusLabel
@onready var audio_status_label: Label = $AudioStatusLabel
@onready var play_pc_button: Button = $PlayPcAudioButton
@onready var play_world_button: Button = $PlayWorldAudioButton
@onready var server_toggle_button: Button = $ServerToggleButton
@onready var hub_reload_button: Button = $HubReloadButton
@onready var hub_checks_button: Button = $HubChecksButton
@onready var server_status_label: Label = $ServerStatusLabel
@onready var hub_config_panel: Panel = $HubConfigPanel
@onready var hub_config_close_button: Button = $HubConfigPanel/HubConfigCloseButton
@onready var hub_config_quit_button: Button = $HubConfigPanel/HubConfigQuitButton
@onready var hub_config_save_button: Button = $HubConfigPanel/HubConfigSaveButton
@onready var hub_config_sim_card_button: Button = $HubConfigPanel/HubConfigSimCardButton
@onready var hub_config_api_card_button: Button = $HubConfigPanel/HubConfigApiCardButton
@onready var hub_config_eval_card_button: Button = $HubConfigPanel/HubConfigEvalCardButton
@onready var hub_config_default_panel_button: OptionButton = $HubConfigPanel/HubConfigDefaultPanelButton
@onready var hub_config_refresh_button: OptionButton = $HubConfigPanel/HubConfigRefreshButton
@onready var hub_config_status_label: Label = $HubConfigPanel/HubConfigStatusLabel
@onready var hub_chat_panel: Panel = $HubChatPanel
@onready var hub_chat_history_label: RichTextLabel = $HubChatPanel/HubChatHistoryLabel
@onready var hub_chat_input_edit: LineEdit = $HubChatPanel/HubChatInputEdit
@onready var hub_chat_send_button: Button = $HubChatPanel/HubChatSendButton
@onready var hub_chat_status_label: Label = $HubChatPanel/HubChatStatusLabel
@onready var hub_chat_request: HTTPRequest = $HubChatRequest
@onready var _sim_client: Node = get_node_or_null("/root/SimClient")

@export var epochs_dir: String = "res://data/epochs"
@export var audio_assets_dir: String = "res://assets/audio"
@export var server_python_path: String = "res://../.venv/Scripts/python.exe"
@export var server_script_path: String = "res://../novapolis_agent/scripts/run_sim_server.py"
@export var eval_script_path: String = "res://../novapolis_agent/scripts/quick_eval.py"
@export var system_snapshot_script_path: String = "res://../novapolis_agent/scripts/system_snapshot.py"
@export var eval_summary_script_path: String = "res://../novapolis_agent/scripts/latest_eval_summary.py"
@export var agent_actions_script_path: String = "res://../novapolis_agent/scripts/agent_module_actions.py"
@export var enable_system_resource_monitoring: bool = false
@export var collapse_agent_status_when_form_open: bool = true
@export var metrics_refresh_interval_seconds: float = 4.0
@export var eval_summary_refresh_interval_seconds: float = 8.0
@export var eval_expected_duration_seconds: float = 25.0
@export var eval_quick_limit: int = 30
@export var hub_chat_profile_id: String = "text_rpg"

var _loaded_epochs: Array[Dictionary] = []
var _current_epoch_index: int = 0
var _current_slot: int = 0
var _audio_player: AudioStreamPlayer
var _last_status_message: String = "Warte auf Agent..."
var _last_success_ms: int = -1
var _error_started_ms: int = -1
var _last_error_visible: bool = false
var _last_world_state: Dictionary = {}
var _runtime_events: Array[String] = []
var _runtime_event_timestamps_ms: Array[int] = []
const _MAX_RUNTIME_EVENTS: int = 80
const _EVENT_RATE_WINDOW_SECONDS: float = 30.0
var _scheduler_hook: SchedulerHook
var _audio_assets_present: bool = false
var _server_pid: int = -1
var _server_status_text: String = "stopped"
var _server_exit_reported: bool = false
var _agent_studio_mode: String = "operate"
var _eval_pid: int = -1
var _eval_started_ms: int = -1
var _last_eval_exit_code: int = -1
var _agent_eval_suite: String = "neutral"
var _dataset_pid: int = -1
var _dataset_started_ms: int = -1
var _last_dataset_exit_code: int = -1
var _dataset_source_mode: String = "clean"
var _dataset_status_text: String = "Datasets: idle"
var _active_dataset_name: String = ""
var _active_dataset_tag: String = ""
var _synonym_status_text: String = "Synonyms: idle"
var _active_synonym_set: String = ""
var _active_synonym_tag: String = ""
var _finetune_pid: int = -1
var _finetune_started_ms: int = -1
var _last_finetune_exit_code: int = -1
var _finetune_profile: String = "baseline"
var _finetune_base_model: String = "sshleifer/tiny-gpt2"
var _finetune_output_name: String = "lora-agent-hub"
var _finetune_epochs: int = 1
var _finetune_max_steps: int = 10
var _finetune_batch_size: int = 1
var _finetune_lr: float = 0.0002
var _finetune_status_text: String = "Finetune: idle"
var _profile_status_text: String = "Profiles: idle"
var _advanced_settings_status_text: String = "Advanced: idle"
var _jobs_status_text: String = "Jobs: idle"
var _active_profile_name: String = ""
var _active_profile_mode: String = ""
var _agent_form_kind: String = ""
var _agent_form_mode_value: String = "clean"
var _agent_form_target_value: String = "new"
var _agent_form_template_signature: String = ""
var _agent_form_controls: Dictionary = {}
var _form_dropdowns_syncing: bool = false
var _last_metrics_refresh_ms: int = -1
var _system_cpu_percent: float = -1.0
var _system_ram_percent: float = -1.0
var _system_gpu_vram_percent: float = -1.0
var _system_gpu_vram_used_mb: float = -1.0
var _system_gpu_vram_total_mb: float = -1.0
var _system_cpu_temp_c: float = -999.0
var _system_gpu_temp_c: float = -999.0
var _agent_submenu_open: bool = false
var _checks_submenu_open: bool = false
var _rp_submenu_open: bool = false
var _checks_target: String = "sim"
var _checks_type: String = "smoke"
var _checks_running: bool = false
var _rp_auto_advance: bool = false
var _rp_last_auto_advance_ms: int = -1
var _last_eval_summary_refresh_ms: int = -1
var _latest_eval_summary_text: String = "Letzte Eval-Runs: n/a"
var _ai_trend_summary_text: String = "Trendkarte: n/a"
var _latest_eval_runs: Array = []
var _artifacts_summary_text: String = "Artifacts: n/a"
var _experiments_summary_text: String = "Experiments: n/a"
var _policy_sandbox_summary_text: String = "Policy Sandbox: n/a"
var _release_gate_summary_text: String = "Release Gate: n/a"
var _audit_trail_summary_text: String = "Audit Trail: n/a"
var _security_model_summary_text: String = "Security: guarded"
var _destructive_guard_enabled: bool = true
var _destructive_guard_window_ms: int = 8000
var _destructive_guard_token: String = "confirm"
var _destructive_armed_action: String = ""
var _destructive_armed_until_ms: int = -1
var _agent_refresh_turn: int = 0
var _agent_action_busy: bool = false
var _agent_summary_refresh_pending: bool = false
var _agent_summary_refresh_due_ms: int = -1
var _last_error_code: String = "none"
var _last_quality_refresh_ms: int = -1
var _quality_tests_last: String = "n/a"
var _quality_types_last: String = "n/a"
var _quality_coverage_last: String = "n/a"
var _hub_show_sim_card: bool = true
var _hub_show_api_card: bool = true
var _hub_show_eval_card: bool = true
var _hub_default_panel: String = "hub"
var _hub_refresh_profile: String = "normal"
var _hub_config_collapsed: bool = false
var _hub_chat_in_flight: bool = false
var _hub_chat_lines: Array[String] = []
var _hub_chat_campaign_id: String = "novapolis_text_rpg_v1"
var _hub_chat_session_id: String = ""
var _hub_chat_scene_id: String = "hub_boot"
var _hub_chat_turn_index: int = 0
var _hub_chat_pending_turn_id: String = ""
var _hub_chat_current_scene_text: String = "Kein Live-Lauf aktiv."
var _hub_chat_current_consequence: String = ""
var _hub_chat_current_options: Array[String] = []
var _hub_chat_current_state_patches: Array[String] = []
var _hub_chat_public_context: String = ""
var _hub_session_request: HTTPRequest
var _hub_session_sync_in_flight: bool = false
var _live_session_artifact_paths: Dictionary = {}
var _live_session_resume_checkpoint_id: String = ""
var _marquee_state: Dictionary = {}
var _lower_shared_topic: String = "agent_api"
const _HUB_PREFS_PATH: String = "user://hub_prefs.cfg"
const _DATASET_REGISTRY_PATH: String = "user://agent_user_data/datasets/_registry.json"
const _SYNONYM_REGISTRY_PATH: String = "user://agent_user_data/synonyms/_registry.json"
const _PROFILE_REGISTRY_PATH: String = "user://agent_user_data/profiles/_registry.json"
const _ADVANCED_SETTINGS_PATH: String = "user://agent_user_data/settings/advanced.json"
const _JOBS_QUEUE_PATH: String = "user://agent_user_data/jobs/queue.json"
const _AUDIT_TRAIL_PATH: String = "user://agent_user_data/audit/trail.jsonl"
const _SECURITY_MODEL_PATH: String = "user://agent_user_data/security/model.json"
const _HUB_CONFIG_EXPANDED_BOTTOM: float = 264.0
const _HUB_CONFIG_COLLAPSED_HEIGHT: float = 42.0
const _EVAL_SUITE_OPTIONS: Array[String] = ["neutral", "rpg", "quality_de"]
const _DATASET_SOURCE_OPTIONS: Array[String] = ["clean", "with_failures"]
const _HUB_DEFAULT_PANEL_OPTIONS: Array[String] = ["hub", "agent", "checks"]
const _HUB_REFRESH_PROFILE_OPTIONS: Array[String] = ["normal", "fast", "slow"]
const _HUB_CHAT_MAX_LINES: int = 18
const _LOWER_SHARED_TOPIC_OPTIONS: Array[String] = ["agent_api", "runtime_ops", "eval_quality"]

const _AGENT_PANEL_DOCK_LEFT: float = 1320.0
const _AGENT_PANEL_DOCK_TOP: float = 620.0
const _AGENT_PANEL_DOCK_RIGHT: float = 1900.0
const _AGENT_PANEL_DOCK_BOTTOM: float = 1028.0
const _AGENT_PANEL_EXCLUSIVE_LEFT: float = 20.0
const _AGENT_PANEL_EXCLUSIVE_TOP: float = 44.0
const _AGENT_PANEL_EXCLUSIVE_RIGHT: float = 1900.0
const _AGENT_PANEL_EXCLUSIVE_BOTTOM: float = 1028.0
const _CHECKS_PANEL_EXCLUSIVE_LEFT: float = 20.0
const _CHECKS_PANEL_EXCLUSIVE_TOP: float = 44.0
const _CHECKS_PANEL_EXCLUSIVE_RIGHT: float = 1900.0
const _CHECKS_PANEL_EXCLUSIVE_BOTTOM: float = 1028.0
const _AGENT_FORM_PANEL_NORMAL_TINT: Color = Color(1.0, 1.0, 1.0, 1.0)
const _AGENT_FORM_PANEL_ACTIVE_TINT: Color = Color(0.93, 0.97, 1.0, 1.0)
const _AGENT_STATUS_NORMAL_TINT: Color = Color(0.95, 0.95, 0.9, 1.0)
const _AGENT_STATUS_DIM_TINT: Color = Color(0.78, 0.82, 0.88, 1.0)
const _UI_BASE_WIDTH: float = 1920.0
const _UI_BASE_HEIGHT: float = 1080.0
const _UI_MIN_WIDTH: float = 1100.0
const _UI_MIN_HEIGHT: float = 700.0
const _UI_MARGIN: float = 16.0
const _UI_GAP: float = 12.0
const _QUALITY_REFRESH_INTERVAL_SECONDS: float = 15.0
const _MARQUEE_STEP_MS: int = 180
const _MARQUEE_SEPARATOR: String = "     "
@export var preserve_editor_hub_layout: bool = true

func _ready() -> void:
	add_to_group("world_listeners")
	get_viewport().size_changed.connect(_on_viewport_size_changed)
	play_pc_button.pressed.connect(_on_play_pc_audio_pressed)
	play_world_button.pressed.connect(_on_play_world_audio_pressed)
	server_toggle_button.pressed.connect(_on_server_toggle_pressed)
	hub_reload_button.pressed.connect(_on_hub_reload_pressed)
	hub_checks_button.pressed.connect(_on_hub_checks_pressed)
	agent_operate_button.pressed.connect(_on_agent_operate_pressed)
	agent_author_button.pressed.connect(_on_agent_author_pressed)
	agent_eval_run_button.pressed.connect(_on_agent_eval_run_pressed)
	agent_eval_suite_button.item_selected.connect(_on_agent_eval_suite_selected)
	agent_dataset_source_button.item_selected.connect(_on_agent_dataset_source_selected)
	agent_form_mode_button.item_selected.connect(_on_agent_form_mode_selected)
	agent_form_target_button.item_selected.connect(_on_agent_form_target_selected)
	agent_form_apply_button.pressed.connect(_on_agent_form_apply_pressed)
	agent_datasets_button.pressed.connect(_on_agent_datasets_pressed)
	agent_synonyms_button.pressed.connect(_on_agent_synonyms_pressed)
	agent_finetune_button.pressed.connect(_on_agent_finetune_pressed)
	agent_profiles_button.pressed.connect(_on_agent_profiles_pressed)
	agent_ai_status_button.pressed.connect(_on_agent_ai_status_pressed)
	agent_back_button.pressed.connect(_on_agent_back_pressed)
	checks_back_button.pressed.connect(_on_checks_back_pressed)
	rp_back_button.pressed.connect(_on_rp_back_pressed)
	rp_hour_plus_button.pressed.connect(_on_rp_hour_plus_pressed)
	rp_auto_advance_button.pressed.connect(_on_rp_auto_advance_pressed)
	checks_target_sim_button.pressed.connect(_on_checks_target_sim_pressed)
	checks_target_agent_button.pressed.connect(_on_checks_target_agent_pressed)
	checks_target_eval_button.pressed.connect(_on_checks_target_eval_pressed)
	checks_target_workspace_button.pressed.connect(_on_checks_target_workspace_pressed)
	checks_type_smoke_button.pressed.connect(_on_checks_type_smoke_pressed)
	checks_type_unit_button.pressed.connect(_on_checks_type_unit_pressed)
	checks_type_api_button.pressed.connect(_on_checks_type_api_pressed)
	checks_type_lint_button.pressed.connect(_on_checks_type_lint_pressed)
	checks_type_full_button.pressed.connect(_on_checks_type_full_pressed)
	checks_run_selected_button.pressed.connect(_on_checks_run_selected_pressed)
	checks_run_module_pack_button.pressed.connect(_on_checks_run_module_pack_pressed)
	hub_config_save_button.pressed.connect(_on_hub_config_save_pressed)
	hub_config_close_button.pressed.connect(_on_hub_config_close_pressed)
	hub_config_quit_button.pressed.connect(_on_hub_config_quit_pressed)
	hub_config_sim_card_button.pressed.connect(_on_hub_config_sim_card_pressed)
	hub_config_api_card_button.pressed.connect(_on_hub_config_api_card_pressed)
	hub_config_eval_card_button.pressed.connect(_on_hub_config_eval_card_pressed)
	hub_config_default_panel_button.item_selected.connect(_on_hub_config_default_panel_selected)
	hub_config_refresh_button.item_selected.connect(_on_hub_config_refresh_selected)
	hub_chat_send_button.pressed.connect(_on_hub_chat_send_pressed)
	hub_chat_input_edit.text_submitted.connect(_on_hub_chat_input_submitted)
	hub_chat_request.request_completed.connect(_on_hub_chat_request_completed)
	_hub_session_request = HTTPRequest.new()
	_hub_session_request.timeout = 4.0
	add_child(_hub_session_request)
	_hub_session_request.request_completed.connect(_on_hub_session_request_completed)
	api_card_panel.gui_input.connect(Callable(self, "_on_api_card_panel_gui_input"))
	_audio_player = AudioStreamPlayer.new()
	add_child(_audio_player)
	_apply_state({"tick": 0, "time": 0.0})
	set_process(true)
	on_action_start.connect(_on_action_start_event)
	on_action_end.connect(_on_action_end_event)
	on_visibility_change.connect(_on_visibility_change_event)
	on_interrupt.connect(_on_interrupt_event)
	_scheduler_hook = SchedulerHookRef.new()
	_append_runtime_event("SCHEDULER_READY", {"queue_size": _scheduler_hook.size()})
	_refresh_hub_topbar()
	_refresh_module_cards()
	_display_status(_last_status_message)
	_load_epochs()
	_scan_audio_assets()
	_load_dataset_registry_state()
	_load_synonym_registry_state()
	_load_profile_registry_state()
	_load_advanced_settings_state()
	_load_jobs_state()
	_load_security_model_state()
	_refresh_agent_restpoint_summaries()
	_load_hub_preferences()
	_init_agent_dropdown_options()
	_init_hub_config_dropdown_options()
	_apply_hub_preferences()
	_set_agent_module_exclusive(false)
	_set_checks_module_exclusive(false)
	_set_rp_module_exclusive(false)
	_update_agent_menu_ui()
	_update_checks_menu_ui()
	_update_rp_menu_ui()
	_refresh_hub_config_ui()
	_set_hub_config_collapsed(false)
	hub_chat_history_label.bbcode_enabled = false
	_hub_chat_session_id = "sim-hub-%s" % Time.get_datetime_string_from_system(false, true).replace(":", "").replace("-", "").replace(" ", "_")
	_hub_chat_public_context = _build_hub_chat_public_context()
	_refresh_hub_chat_ui()
	hub_chat_status_label.text = "Live-Spielclient: bereit"
	_refresh_agent_studio_ui()
	_refresh_agent_form_ui()
	agent_studio_hint_label.visible = false
	agent_studio_hint_label.text = ""
	_refresh_checks_studio_ui()
	_refresh_rp_studio_ui()
	_update_server_control_ui()
	_open_default_panel_if_configured()
	_apply_responsive_layout()
	_render_pc_centric_view()


func _on_viewport_size_changed() -> void:
	_apply_responsive_layout()


func _get_safe_viewport_size() -> Vector2:
	var size := get_viewport_rect().size
	return Vector2(maxf(size.x, _UI_MIN_WIDTH), maxf(size.y, _UI_MIN_HEIGHT))


func _apply_responsive_layout() -> void:
	var size := _get_safe_viewport_size()
	var width := size.x
	var height := size.y
	if preserve_editor_hub_layout and not _agent_submenu_open and not _checks_submenu_open and not _rp_submenu_open:
		_apply_editor_hub_layout(width, height)
		return
	_layout_hub_config_panel(width)
	_layout_hub_topbar(width)
	_layout_hub_actions(width)
	_layout_hub_log_and_cards(width, height)
	_layout_module_panels(width, height)


func _set_control_rect(control: Control, left: float, top: float, right: float, bottom: float) -> void:
	control.offset_left = left
	control.offset_top = top
	control.offset_right = right
	control.offset_bottom = bottom


func _scale_hub_x(value: float, width: float) -> float:
	return value * (width / _UI_BASE_WIDTH)


func _scale_hub_y(value: float, height: float) -> float:
	return value * (height / _UI_BASE_HEIGHT)


func _apply_editor_hub_layout(width: float, height: float) -> void:
	# Preserve the dashboard arrangement authored in Main.tscn as hub source of truth.
	var area_01_left := _scale_hub_x(98.0, width)
	var area_01_top := _scale_hub_y(117.0, height)
	var area_01_right := _scale_hub_x(497.0, width)
	var area_01_bottom := _scale_hub_y(231.0, height)
	var area_02_left := _scale_hub_x(520.0, width)
	var area_02_top := _scale_hub_y(116.0, height)
	var area_02_right := _scale_hub_x(902.0, width)
	var area_02_bottom := _scale_hub_y(229.0, height)
	var area_03_left := _scale_hub_x(1018.0, width)
	var area_03_top := _scale_hub_y(117.0, height)
	var area_03_right := _scale_hub_x(1399.0, width)
	var _area_03_bottom := _scale_hub_y(230.0, height)
	var area_04_left := _scale_hub_x(1424.0, width)
	var area_04_top := _scale_hub_y(116.0, height)
	var area_04_right := _scale_hub_x(1821.0, width)
	var area_04_bottom := _scale_hub_y(228.0, height)

	var inner_pad_x := _scale_hub_x(8.0, width)
	var inner_pad_y := _scale_hub_y(8.0, height)
	var area_01_line_h := _scale_hub_y(17.0, height)
	var area_01_line_gap := _scale_hub_y(2.0, height)
	var area_01_line_y := area_01_top + inner_pad_y

	_set_control_rect(
		hub_title_label,
		area_01_left + inner_pad_x,
		area_01_line_y,
		area_01_right - inner_pad_x,
		area_01_line_y + area_01_line_h
	)
	area_01_line_y += area_01_line_h + area_01_line_gap
	_set_control_rect(
		hub_api_label,
		area_01_left + inner_pad_x,
		area_01_line_y,
		area_01_right - inner_pad_x,
		area_01_line_y + area_01_line_h
	)
	area_01_line_y += area_01_line_h + area_01_line_gap
	_set_control_rect(
		slot_label,
		area_01_left + inner_pad_x,
		area_01_line_y,
		area_01_right - inner_pad_x,
		area_01_line_y + area_01_line_h
	)
	area_01_line_y += area_01_line_h + area_01_line_gap
	_set_control_rect(
		audio_status_label,
		area_01_left + inner_pad_x,
		area_01_line_y,
		area_01_right - inner_pad_x,
		area_01_line_y + area_01_line_h
	)
	area_01_line_y += area_01_line_h + area_01_line_gap
	_set_control_rect(
		epoch_label,
		area_01_left + inner_pad_x,
		area_01_line_y,
		area_01_left + _scale_hub_x(110.0, width),
		area_01_line_y + area_01_line_h
	)
	_set_control_rect(
		epoch_status_label,
		area_01_left + _scale_hub_x(114.0, width),
		area_01_line_y,
		area_01_right - inner_pad_x,
		area_01_line_y + area_01_line_h
	)

	var action_pad := _scale_hub_x(10.0, width)
	var action_gap := _scale_hub_x(10.0, width)
	var action_inner_left := area_02_left + action_pad
	var action_inner_right := area_02_right - action_pad
	var action_width := maxf(
		_scale_hub_x(140.0, width),
		(action_inner_right - action_inner_left - action_gap) / 2.0
	)
	var action_top_row_top := area_02_top + inner_pad_y
	var action_top_row_bottom := action_top_row_top + _scale_hub_y(46.0, height)
	var action_bottom_row_top := action_top_row_bottom + _scale_hub_y(10.0, height)
	var action_bottom_row_bottom := area_02_bottom - inner_pad_y

	_set_control_rect(
		play_pc_button,
		action_inner_left,
		action_top_row_top,
		action_inner_left + action_width,
		action_top_row_bottom
	)
	_set_control_rect(
		play_world_button,
		action_inner_left + action_width + action_gap,
		action_top_row_top,
		action_inner_right,
		action_top_row_bottom
	)
	_set_control_rect(
		hub_checks_button,
		action_inner_left,
		action_bottom_row_top,
		action_inner_left + action_width,
		action_bottom_row_bottom
	)
	_set_control_rect(
		hub_reload_button,
		action_inner_left + action_width + action_gap,
		action_bottom_row_top,
		action_inner_right,
		action_bottom_row_bottom
	)

	var status_pad := _scale_hub_x(8.0, width)
	var status_left := area_03_left + status_pad
	var status_right := area_03_right - status_pad
	var status_line_h := _scale_hub_y(16.0, height)
	var status_gap := _scale_hub_y(2.0, height)
	var status_y := area_03_top + inner_pad_y

	_set_control_rect(
		server_toggle_button,
		status_left,
		status_y,
		status_left + _scale_hub_x(148.0, width),
		status_y + _scale_hub_y(30.0, height)
	)
	_set_control_rect(
		server_status_label,
		status_left + _scale_hub_x(154.0, width),
		status_y,
		status_right,
		status_y + _scale_hub_y(30.0, height)
	)
	status_y += _scale_hub_y(32.0, height)
	_set_control_rect(
		hub_errors_label,
		status_left,
		status_y,
		status_right,
		status_y + status_line_h
	)
	status_y += status_line_h + status_gap
	_set_control_rect(
		hub_queue_label,
		status_left,
		status_y,
		status_right,
		status_y + status_line_h
	)
	status_y += status_line_h + status_gap
	_set_control_rect(
		hub_polling_label,
		status_left,
		status_y,
		status_right,
		status_y + status_line_h
	)
	status_y += status_line_h + status_gap
	_set_control_rect(
		tick_label,
		status_left,
		status_y,
		status_left + _scale_hub_x(188.0, width),
		status_y + status_line_h
	)
	_set_control_rect(
		time_label,
		status_left + _scale_hub_x(194.0, width),
		status_y,
		status_right,
		status_y + status_line_h
	)

	_set_control_rect(
		hub_config_panel,
		area_04_left,
		area_04_top,
		area_04_right,
		area_04_bottom
	)
	_set_control_rect(
		status_label,
		_scale_hub_x(20.0, width),
		_scale_hub_y(92.0, height),
		_scale_hub_x(1825.0, width),
		_scale_hub_y(114.0, height)
	)
	_set_control_rect(
		log_label,
		_scale_hub_x(99.0, width),
		_scale_hub_y(256.0, height),
		_scale_hub_x(897.0, width),
		_scale_hub_y(565.0, height)
	)
	_set_control_rect(
		hub_chat_panel,
		_scale_hub_x(1020.0, width),
		_scale_hub_y(255.0, height),
		_scale_hub_x(1820.0, width),
		_scale_hub_y(558.0, height)
	)
	_layout_hub_chat_contents()

	_set_control_rect(
		sim_card_panel,
		_scale_hub_x(104.0, width),
		_scale_hub_y(824.0, height),
		_scale_hub_x(898.0, width),
		_scale_hub_y(1002.0, height)
	)
	_set_control_rect(
		api_card_panel,
		_scale_hub_x(552.0, width),
		_scale_hub_y(630.0, height),
		_scale_hub_x(1358.0, width),
		_scale_hub_y(801.0, height)
	)
	_set_control_rect(
		eval_card_panel,
		_scale_hub_x(1016.0, width),
		_scale_hub_y(826.0, height),
		_scale_hub_x(1822.0, width),
		_scale_hub_y(998.0, height)
	)

	_layout_module_panels(width, height)


func _layout_hub_topbar(width: float) -> void:
	var top := 4.0
	var left := _UI_MARGIN
	status_label.offset_left = _UI_MARGIN
	status_label.offset_top = 92.0
	status_label.offset_right = width - _UI_MARGIN
	status_label.offset_bottom = 114.0

	var title_w := clampf(width * 0.18, 240.0, 360.0)
	hub_title_label.offset_left = left
	hub_title_label.offset_top = top
	hub_title_label.offset_right = left + title_w
	hub_title_label.offset_bottom = top + 20.0

	var x := left + title_w + _UI_GAP
	var right := width - _UI_MARGIN
	var remaining := maxf(420.0, right - x)
	var api_w := remaining * 0.44
	var polling_w := remaining * 0.23
	var queue_w := remaining * 0.13
	var errors_w := maxf(130.0, remaining - api_w - polling_w - queue_w - _UI_GAP * 3.0)

	hub_api_label.offset_left = x
	hub_api_label.offset_top = top
	hub_api_label.offset_right = x + api_w
	hub_api_label.offset_bottom = top + 20.0
	x = hub_api_label.offset_right + _UI_GAP

	hub_polling_label.offset_left = x
	hub_polling_label.offset_top = top
	hub_polling_label.offset_right = x + polling_w
	hub_polling_label.offset_bottom = top + 20.0
	x = hub_polling_label.offset_right + _UI_GAP

	hub_queue_label.offset_left = x
	hub_queue_label.offset_top = top
	hub_queue_label.offset_right = x + queue_w
	hub_queue_label.offset_bottom = top + 20.0
	x = hub_queue_label.offset_right + _UI_GAP

	hub_errors_label.offset_left = x
	hub_errors_label.offset_top = top
	hub_errors_label.offset_right = minf(right, x + errors_w)
	hub_errors_label.offset_bottom = top + 20.0


func _layout_hub_actions(width: float) -> void:
	var y := 228.0
	var h := 38.0
	var left := _UI_MARGIN
	var right := minf(width - _UI_MARGIN, hub_config_panel.offset_left - _UI_GAP)
	if right <= left + 620.0:
		right = width - _UI_MARGIN
	var count := 5.0
	var available := maxf(680.0, right - left)
	var button_w := maxf(120.0, (available - _UI_GAP * (count - 1.0)) / count)

	play_pc_button.offset_left = left
	play_pc_button.offset_top = y
	play_pc_button.offset_right = left + button_w
	play_pc_button.offset_bottom = y + h

	play_world_button.offset_left = play_pc_button.offset_right + _UI_GAP
	play_world_button.offset_top = y
	play_world_button.offset_right = play_world_button.offset_left + button_w
	play_world_button.offset_bottom = y + h

	server_toggle_button.offset_left = play_world_button.offset_right + _UI_GAP
	server_toggle_button.offset_top = y
	server_toggle_button.offset_right = server_toggle_button.offset_left + button_w
	server_toggle_button.offset_bottom = y + h

	hub_reload_button.offset_left = server_toggle_button.offset_right + _UI_GAP
	hub_reload_button.offset_top = y
	hub_reload_button.offset_right = hub_reload_button.offset_left + button_w
	hub_reload_button.offset_bottom = y + h

	hub_checks_button.offset_left = hub_reload_button.offset_right + _UI_GAP
	hub_checks_button.offset_top = y
	hub_checks_button.offset_right = hub_checks_button.offset_left + button_w
	hub_checks_button.offset_bottom = y + h

	audio_status_label.offset_left = _UI_MARGIN
	audio_status_label.offset_top = 284.0
	audio_status_label.offset_right = _UI_MARGIN + 380.0
	audio_status_label.offset_bottom = 304.0

	server_status_label.offset_left = server_toggle_button.offset_left
	server_status_label.offset_top = 284.0
	server_status_label.offset_right = server_status_label.offset_left + 560.0
	server_status_label.offset_bottom = 304.0


func _layout_hub_log_and_cards(width: float, height: float) -> void:
	var cards_h := clampf(height * 0.19, 140.0, 190.0)
	var cards_top := height - _UI_MARGIN - cards_h
	var cards_bottom := height - _UI_MARGIN
	var card_w := (width - _UI_MARGIN * 2.0 - _UI_GAP * 2.0) / 3.0

	sim_card_panel.offset_left = _UI_MARGIN
	sim_card_panel.offset_top = cards_top
	sim_card_panel.offset_right = sim_card_panel.offset_left + card_w
	sim_card_panel.offset_bottom = cards_bottom

	api_card_panel.offset_left = sim_card_panel.offset_right + _UI_GAP
	api_card_panel.offset_top = cards_top
	api_card_panel.offset_right = api_card_panel.offset_left + card_w
	api_card_panel.offset_bottom = cards_bottom

	eval_card_panel.offset_left = api_card_panel.offset_right + _UI_GAP
	eval_card_panel.offset_top = cards_top
	eval_card_panel.offset_right = eval_card_panel.offset_left + card_w
	eval_card_panel.offset_bottom = cards_bottom

	log_label.offset_left = _UI_MARGIN
	log_label.offset_top = 318.0
	var chat_panel_w := clampf(width * 0.26, 300.0, 420.0)
	hub_chat_panel.offset_left = width - _UI_MARGIN - chat_panel_w
	hub_chat_panel.offset_top = 318.0
	hub_chat_panel.offset_right = width - _UI_MARGIN
	hub_chat_panel.offset_bottom = minf(height - _UI_MARGIN - cards_h - _UI_GAP, 620.0)
	_layout_hub_chat_contents()

	log_label.offset_right = hub_chat_panel.offset_left - _UI_GAP
	log_label.offset_bottom = maxf(log_label.offset_top + 140.0, cards_top - _UI_GAP)


func _layout_hub_chat_contents() -> void:
	var panel_w := maxf(220.0, hub_chat_panel.offset_right - hub_chat_panel.offset_left)
	var panel_h := maxf(140.0, hub_chat_panel.offset_bottom - hub_chat_panel.offset_top)
	var pad := 10.0
	var send_w := clampf(panel_w * 0.22, 84.0, 108.0)
	var input_h := 30.0
	var status_h := 20.0
	var title_top := 8.0
	var title_bottom := 26.0
	var input_top := panel_h - pad - status_h - 4.0 - input_h
	var history_bottom := input_top - 8.0

	hub_chat_history_label.offset_left = pad
	hub_chat_history_label.offset_top = 30.0
	hub_chat_history_label.offset_right = panel_w - pad
	hub_chat_history_label.offset_bottom = maxf(64.0, history_bottom)

	hub_chat_input_edit.offset_left = pad
	hub_chat_input_edit.offset_top = input_top
	hub_chat_input_edit.offset_right = panel_w - pad - send_w - 8.0
	hub_chat_input_edit.offset_bottom = input_top + input_h

	hub_chat_send_button.offset_left = hub_chat_input_edit.offset_right + 8.0
	hub_chat_send_button.offset_top = input_top
	hub_chat_send_button.offset_right = panel_w - pad
	hub_chat_send_button.offset_bottom = input_top + input_h

	hub_chat_status_label.offset_left = pad
	hub_chat_status_label.offset_top = hub_chat_input_edit.offset_bottom + 4.0
	hub_chat_status_label.offset_right = panel_w - pad
	hub_chat_status_label.offset_bottom = hub_chat_status_label.offset_top + status_h

	var chat_title := get_node_or_null("HubChatPanel/HubChatTitleLabel") as Label
	if chat_title:
		chat_title.offset_left = pad
		chat_title.offset_top = title_top
		chat_title.offset_right = panel_w - pad
		chat_title.offset_bottom = title_bottom


func _layout_hub_config_panel(width: float) -> void:
	var panel_w := clampf(width * 0.16, 240.0, 300.0)
	hub_config_panel.offset_left = width - _UI_MARGIN - panel_w
	hub_config_panel.offset_top = 44.0
	hub_config_panel.offset_right = width - _UI_MARGIN
	if _hub_config_collapsed:
		hub_config_panel.offset_bottom = hub_config_panel.offset_top + _HUB_CONFIG_COLLAPSED_HEIGHT
	else:
		hub_config_panel.offset_bottom = hub_config_panel.offset_top + (_HUB_CONFIG_EXPANDED_BOTTOM - 44.0)


func _layout_module_panels(width: float, height: float) -> void:
	var left := _UI_MARGIN
	var top := 44.0
	var right := width - _UI_MARGIN
	var bottom := height - _UI_MARGIN

	checks_studio_panel.offset_left = left
	checks_studio_panel.offset_top = top
	checks_studio_panel.offset_right = right
	checks_studio_panel.offset_bottom = bottom

	rp_studio_panel.offset_left = left
	rp_studio_panel.offset_top = top
	rp_studio_panel.offset_right = right
	rp_studio_panel.offset_bottom = bottom

	if _agent_submenu_open:
		agent_studio_panel.offset_left = left
		agent_studio_panel.offset_top = top
		agent_studio_panel.offset_right = right
		agent_studio_panel.offset_bottom = bottom
		_apply_agent_module_layout(true)
		return

	var dock_w := clampf(width * 0.31, 520.0, 680.0)
	var dock_h := clampf(height * 0.40, 380.0, 480.0)
	agent_studio_panel.offset_left = right - dock_w
	agent_studio_panel.offset_top = bottom - dock_h
	agent_studio_panel.offset_right = right
	agent_studio_panel.offset_bottom = bottom
	_apply_agent_module_layout(false)


func receive_world_state(state: Dictionary) -> void:
	_on_state_updated(state)


func receive_status(message: String) -> void:
	_on_status_updated(message)


func _on_state_updated(state: Dictionary) -> void:
	on_action_start.emit("state_update", {"source": "SimClient"})
	_last_success_ms = Time.get_ticks_msec()
	if _last_status_message != "":
		_error_started_ms = -1
	_apply_state(state)
	_refresh_status_label()
	on_action_end.emit("state_update", {"tick": state.get("tick", -1)})


func _on_status_updated(message: String) -> void:
	var had_error := _last_status_message != ""
	_last_status_message = message
	_last_error_code = _extract_error_code(message)
	if message == "":
		_error_started_ms = -1
	else:
		if _error_started_ms < 0:
			_error_started_ms = Time.get_ticks_msec()
		on_interrupt.emit("status_error", {"message": message})

	var has_error := message != ""
	if has_error != had_error:
		_last_error_visible = has_error
		on_visibility_change.emit(has_error, "status_error_visibility")
	_display_status(message)


func _process(_delta: float) -> void:
	_refresh_server_runtime_state()
	_refresh_eval_runtime_state()
	_refresh_dataset_runtime_state()
	_refresh_finetune_runtime_state()
	# Heavy script refreshes are staggered to avoid back-to-back OS.execute stalls.
	if _agent_submenu_open:
		if enable_system_resource_monitoring and _agent_refresh_turn % 2 == 0:
			_refresh_system_metrics(false)
		else:
			_refresh_latest_eval_summary(false)
		_agent_refresh_turn += 1
		if _agent_summary_refresh_pending and not _agent_action_busy:
			var now_ms := Time.get_ticks_msec()
			if _agent_summary_refresh_due_ms <= 0 or now_ms >= _agent_summary_refresh_due_ms:
				_refresh_latest_eval_summary(true)
				_agent_summary_refresh_pending = false
				_agent_summary_refresh_due_ms = -1
	if _rp_submenu_open:
		_run_rp_auto_advance(false)
	_refresh_status_label()
	_refresh_hub_topbar()
	_refresh_module_cards()
	_update_server_control_ui()
	_refresh_agent_studio_ui()
	_refresh_agent_form_ui()
	_refresh_checks_studio_ui()
	_refresh_rp_studio_ui()
	_refresh_agent_restpoint_summaries()


func _apply_state(state: Dictionary) -> void:
	_last_world_state = state
	if state.has("tick"):
		tick_label.text = "Tick: %d" % int(state["tick"])
	if state.has("time"):
		time_label.text = "Zeit: %.2f s" % float(state["time"])


func _display_status(message: String) -> void:
	_last_status_message = message
	_refresh_status_label()


func _refresh_status_label() -> void:
	if _agent_submenu_open or _checks_submenu_open or _rp_submenu_open:
		status_label.visible = false
		return

	var now_ms := Time.get_ticks_msec()
	var base_message := "Verbunden"
	if _last_status_message != "":
		base_message = _last_status_message

	var details: Array[String] = []
	if _last_success_ms >= 0:
		var since_ok := maxf(0.0, float(now_ms - _last_success_ms) / 1000.0)
		details.append("letztes OK vor %.1fs" % since_ok)

	if _error_started_ms >= 0:
		var error_for := maxf(0.0, float(now_ms - _error_started_ms) / 1000.0)
		details.append("Fehlerdauer %.1fs" % error_for)

	status_label.visible = true
	if details.is_empty():
		status_label.text = "Status: %s" % base_message
	else:
		status_label.text = "Status: %s (%s)" % [base_message, ", ".join(details)]

	var error_visible := _last_status_message != ""
	if error_visible != _last_error_visible:
		_last_error_visible = error_visible
		on_visibility_change.emit(error_visible, "status_refresh")


func _compact_reason_text(reason: String, max_len: int = 28) -> String:
	var cleaned := reason.strip_edges()
	if cleaned.length() <= max_len:
		return cleaned
	if max_len <= 3:
		return cleaned.left(max_len)
	var shortened := cleaned.left(max_len - 3)
	while shortened.length() > 0 and (
		shortened.ends_with("(")
		or shortened.ends_with("[")
		or shortened.ends_with("{")
		or shortened.ends_with("|")
		or shortened.ends_with("-")
		or shortened.ends_with(",")
		or shortened.ends_with(";")
		or shortened.ends_with(":")
	):
		shortened = shortened.left(shortened.length() - 1).strip_edges()
	if shortened == "":
		shortened = cleaned.left(max_len - 3)
	return "%s..." % shortened


func _label_text_width(label: Label, text: String) -> float:
	if text == "":
		return 0.0
	var font := label.get_theme_font("font")
	if font == null:
		return float(text.length()) * 8.0
	var font_size := label.get_theme_font_size("font_size")
	return font.get_string_size(text, HORIZONTAL_ALIGNMENT_LEFT, -1, font_size).x


func _build_marquee_slice(label: Label, loop_text: String, start_idx: int, max_width: float) -> String:
	var loop_len := loop_text.length()
	if loop_len <= 0:
		return ""
	var out := ""
	var max_chars: int = mini(256, loop_len * 2)
	for i in range(max_chars):
		var ch := loop_text.substr((start_idx + i) % loop_len, 1)
		var candidate := out + ch
		if _label_text_width(label, candidate) > max_width and out != "":
			break
		out = candidate
	return out.strip_edges()


func _set_marquee_text(label: Label, full_text: String) -> void:
	if label == null:
		return
	var max_width := maxf(24.0, label.offset_right - label.offset_left)
	if _label_text_width(label, full_text) <= max_width:
		label.text = full_text
		_marquee_state.erase(str(label.get_path()))
		return

	var key := str(label.get_path())
	var now_ms := Time.get_ticks_msec()
	var entry: Dictionary = _marquee_state.get(key, {"offset": 0, "last_ms": now_ms}) as Dictionary
	var offset := int(entry.get("offset", 0))
	var last_ms := int(entry.get("last_ms", now_ms))
	if now_ms - last_ms >= _MARQUEE_STEP_MS:
		offset += 1
		last_ms = now_ms

	var loop_text := full_text + _MARQUEE_SEPARATOR
	if loop_text.length() > 0:
		offset = offset % loop_text.length()
	_marquee_state[key] = {"offset": offset, "last_ms": last_ms}
	label.text = _build_marquee_slice(label, loop_text, offset, max_width)


func _refresh_hub_topbar() -> void:
	hub_title_label.text = "Hub v1 | Novapolis Framework"
	_set_marquee_text(hub_config_status_label, "Refresh=%s | default=%s" % [_hub_refresh_profile, _hub_default_panel])

	var runtime_status := _sim_runtime_status()
	var health := _derive_health_state(runtime_status)
	var api_state := str(health.get("state", "offline"))
	var reason := _compact_reason_text(str(health.get("reason", "n/a")))

	var last_ok_text := "n/a"
	if _last_success_ms >= 0:
		var age := maxf(0.0, float(Time.get_ticks_msec() - _last_success_ms) / 1000.0)
		last_ok_text = "%.1fs" % age
	_set_marquee_text(hub_api_label, "API: %s | reason=%s | last_ok=%s" % [api_state, reason, last_ok_text])

	var paused := bool(runtime_status.get("paused_due_to_failures", false))
	var polling_state := "active"
	if paused:
		polling_state = "paused"
	var failures := int(runtime_status.get("consecutive_failures", 0))
	var backoff := float(runtime_status.get("backoff", 0.0))
	_set_marquee_text(hub_polling_label, "Polling: %s | fail=%d | backoff=%.1fs" % [polling_state, failures, backoff])

	var queue_size := 0
	if _scheduler_hook:
		queue_size = _scheduler_hook.size()
	var event_rate := _runtime_event_rate_per_second()
	_set_marquee_text(hub_queue_label, "Queue: %d | rate=%.2f/s" % [queue_size, event_rate])
	_apply_card_visibility_now()

	if _last_status_message == "":
		_set_marquee_text(hub_errors_label, "Errors: none | code=%s" % _last_error_code)
	else:
		var error_for := maxf(0.0, float(Time.get_ticks_msec() - _error_started_ms) / 1000.0)
		var base_error := _last_status_message.split("|")[0].strip_edges()
		_set_marquee_text(hub_errors_label, "Errors: %s (%.1fs) | code=%s" % [base_error, error_for, _last_error_code])


func _refresh_module_cards() -> void:
	var runtime_status := _sim_runtime_status()
	var health := _derive_health_state(runtime_status)
	var sim_state := "INIT"
	if _last_success_ms >= 0:
		sim_state = "RUNNING"
	if _last_status_message != "":
		sim_state = "DEGRADED"

	var tick_value := int(_last_world_state.get("tick", -1))
	var time_value := float(_last_world_state.get("time", 0.0))
	var queue_size := 0
	if _scheduler_hook:
		queue_size = _scheduler_hook.size()
	var event_rate := _runtime_event_rate_per_second()

	sim_card_state_label.text = "State: %s" % sim_state
	sim_card_tick_label.text = "Tick/Time: %d / %.2fs" % [tick_value, time_value]
	sim_card_queue_label.text = "Queue: %d | rate=%.2f/s | slot=%02d" % [queue_size, event_rate, _current_slot]
	sim_card_data_label.text = "Data: epochs=%d | audio=%s" % [_loaded_epochs.size(), str(_audio_assets_present)]

	var api_state := str(health.get("state", "offline"))
	var reason := str(health.get("reason", "n/a"))
	var failures := int(runtime_status.get("consecutive_failures", 0))
	var paused := bool(runtime_status.get("paused_due_to_failures", false))
	var backoff := float(runtime_status.get("backoff", 0.0))
	var timeout := float(runtime_status.get("request_timeout", 0.0))
	var host := "n/a"
	var port := -1
	if _sim_client:
		host = str(_sim_client.get("host"))
		port = int(_sim_client.get("port"))

	var sim_meta: Dictionary = {}
	if _last_world_state.has("sim_meta") and typeof(_last_world_state.get("sim_meta")) == TYPE_DICTIONARY:
		sim_meta = _last_world_state.get("sim_meta", {})
	var mode := str(sim_meta.get("mode", "baseline"))
	var seed_text := str(sim_meta.get("seed", "n/a"))
	_refresh_quality_status(false)
	var dataset_ref := "n/a"
	if _active_dataset_name != "":
		dataset_ref = _active_dataset_name
		if _active_dataset_tag != "":
			dataset_ref = "%s@%s" % [_active_dataset_name, _active_dataset_tag]

	if _lower_shared_topic == "runtime_ops":
		api_card_health_label.text = "Thema: Runtime/Ops (Klick: wechseln)"
		api_card_runtime_label.text = "Queue: %d | rate=%.2f/s | tick=%d" % [queue_size, event_rate, tick_value]
		api_card_backoff_label.text = "Events: runtime=%d/%d | slot=%02d" % [_runtime_events.size(), _MAX_RUNTIME_EVENTS, _current_slot]
		api_card_endpoint_label.text = "RP: %s" % _rp_content_summary()
	elif _lower_shared_topic == "eval_quality":
		api_card_health_label.text = "Thema: Eval/Quality (Klick: wechseln)"
		api_card_runtime_label.text = "Profile: mode=%s | seed=%s" % [mode, seed_text]
		api_card_backoff_label.text = "Artifacts: epochs=%d | audio=%s | dataset=%s" % [_loaded_epochs.size(), str(_audio_assets_present), dataset_ref]
		api_card_endpoint_label.text = "Quality: tests=%s | types=%s | cov=%s" % [_quality_tests_last, _quality_types_last, _quality_coverage_last]
	else:
		api_card_health_label.text = "Thema: Agent/API (Klick: wechseln)"
		api_card_runtime_label.text = "Health: %s | reason=%s | paused=%s" % [api_state, reason, str(paused)]
		api_card_backoff_label.text = "Runtime: fail=%d | timeout=%.1fs | backoff=%.1fs" % [failures, timeout, backoff]
		if port > 0:
			api_card_endpoint_label.text = "Endpoint: http://%s:%d/world/step" % [host, port]
		else:
			api_card_endpoint_label.text = "Endpoint: n/a"

	eval_card_profile_label.text = "Profile: mode=%s | seed=%s" % [mode, seed_text]
	eval_card_artifacts_label.text = "Artifacts: epochs=%d | audio=%s | dataset=%s" % [_loaded_epochs.size(), str(_audio_assets_present), dataset_ref]
	eval_card_events_label.text = "Events: runtime=%d/%d | %s" % [_runtime_events.size(), _MAX_RUNTIME_EVENTS, _rp_content_summary()]
	eval_card_notes_label.text = "Quality: tests=%s | types=%s | cov=%s" % [_quality_tests_last, _quality_types_last, _quality_coverage_last]


func _rp_content_summary() -> String:
	var visibility := "hidden"
	if _rp_submenu_open:
		visibility = "visible"

	var source := "n/a"
	if not _loaded_epochs.is_empty() and _current_epoch_index >= 0 and _current_epoch_index < _loaded_epochs.size():
		var epoch := _loaded_epochs[_current_epoch_index]
		source = "%s/pc_log@%02d" % [str(epoch.get("name", "epoch")), _current_slot]

	var last_event := "none"
	for i in range(_runtime_events.size() - 1, -1, -1):
		var line := str(_runtime_events[i])
		if line.find("RP_") >= 0 or line.find("RP_MODULE") >= 0:
			if line.begins_with("- "):
				line = line.substr(2)
			last_event = line
			break

	return "module=rp | vis=%s | src=%s | last=%s" % [visibility, source, _compact_reason_text(last_event, 36)]


func _on_api_card_panel_gui_input(event: InputEvent) -> void:
	if event is InputEventMouseButton:
		var mb := event as InputEventMouseButton
		if mb.button_index == MOUSE_BUTTON_LEFT and mb.pressed:
			var idx := _LOWER_SHARED_TOPIC_OPTIONS.find(_lower_shared_topic)
			if idx < 0:
				idx = 0
			idx = (idx + 1) % _LOWER_SHARED_TOPIC_OPTIONS.size()
			_lower_shared_topic = _LOWER_SHARED_TOPIC_OPTIONS[idx]
			_refresh_module_cards()


func _refresh_quality_status(force: bool) -> void:
	var now_ms := Time.get_ticks_msec()
	if not force and _last_quality_refresh_ms >= 0:
		var delta_s := float(now_ms - _last_quality_refresh_ms) / 1000.0
		if delta_s < _QUALITY_REFRESH_INTERVAL_SECONDS:
			return
	_last_quality_refresh_ms = now_ms

	var reports_dir := ProjectSettings.globalize_path("res://../.tmp/results/reports")
	var dir := DirAccess.open(reports_dir)
	if dir == null:
		_quality_tests_last = "n/a"
		_quality_types_last = "n/a"
		_quality_coverage_last = "n/a"
		return

	var json_reports: Array[String] = []
	dir.list_dir_begin()
	while true:
		var entry := dir.get_next()
		if entry == "":
			break
		if dir.current_is_dir():
			continue
		if not entry.begins_with("checks_report_") or not entry.ends_with(".json"):
			continue
		json_reports.append(entry)
	dir.list_dir_end()

	if json_reports.is_empty():
		_quality_tests_last = "n/a"
		_quality_types_last = "n/a"
		_quality_coverage_last = "n/a"
		return

	json_reports.sort()
	var latest_path := "%s/%s" % [reports_dir, json_reports[json_reports.size() - 1]]
	if not FileAccess.file_exists(latest_path):
		return
	var file := FileAccess.open(latest_path, FileAccess.READ)
	if file == null:
		return
	var parsed = JSON.parse_string(file.get_as_text())
	if typeof(parsed) != TYPE_DICTIONARY:
		return
	var report := parsed as Dictionary

	var tests_status := "n/a"
	var pyright_status := "SKIP"
	var mypy_status := "SKIP"
	if report.has("checks") and typeof(report.get("checks")) == TYPE_ARRAY:
		for check_item in report.get("checks", []):
			if typeof(check_item) != TYPE_DICTIONARY:
				continue
			var check_dict := check_item as Dictionary
			var tool := str(check_dict.get("tool", ""))
			var status := str(check_dict.get("status", "n/a"))
			if tool == "pytest":
				tests_status = status
			elif tool == "pyright":
				pyright_status = status
			elif tool == "mypy":
				mypy_status = status

	_quality_tests_last = tests_status
	if pyright_status == "PASS" and mypy_status == "PASS":
		_quality_types_last = "PASS"
	elif pyright_status == "n/a" and mypy_status == "n/a":
		_quality_types_last = "n/a"
	else:
		_quality_types_last = "%s/%s" % [pyright_status, mypy_status]

	if report.has("metadata") and typeof(report.get("metadata")) == TYPE_DICTIONARY:
		var metadata := report.get("metadata", {}) as Dictionary
		if metadata.has("coverage_percent") and typeof(metadata.get("coverage_percent")) in [TYPE_FLOAT, TYPE_INT]:
			_quality_coverage_last = "%.2f%%" % float(metadata.get("coverage_percent", 0.0))
		else:
			_quality_coverage_last = "n/a"


func _sim_runtime_status() -> Dictionary:
	if _sim_client and _sim_client.has_method("get_runtime_status"):
		var payload = _sim_client.call("get_runtime_status")
		if typeof(payload) == TYPE_DICTIONARY:
			return payload
	return {}


func _derive_health_state(runtime_status: Dictionary) -> Dictionary:
	var failures := int(runtime_status.get("consecutive_failures", 0))
	var paused := bool(runtime_status.get("paused_due_to_failures", false))

	if _last_status_message != "":
		var reason_text := _last_status_message.split("|")[0].strip_edges()
		if reason_text == "":
			reason_text = "status error"
		return {
			"state": "degraded",
			"reason": reason_text,
		}

	if _server_pid > 0:
		var local_reason := "local pid=%d" % _server_pid
		if paused or failures > 0:
			local_reason = "%s, poll=paused fail=%d" % [local_reason, failures]
		return {
			"state": "local",
			"reason": local_reason,
		}

	if _is_external_server_reachable():
		return {
			"state": "external",
			"reason": "reachable without local pid",
		}

	var offline_reason := "no successful poll yet"
	if _last_success_ms >= 0:
		offline_reason = "last_ok expired"
	if _server_status_text != "stopped":
		offline_reason = _server_status_text
	return {
		"state": "offline",
		"reason": offline_reason,
	}


func _load_epochs() -> void:
	_loaded_epochs.clear()
	var base_dir := DirAccess.open(epochs_dir)
	if base_dir == null:
		_set_marquee_text(epoch_status_label, "Epochen: keine Daten unter %s" % epochs_dir)
		return

	var epoch_dirs: Array[String] = []
	base_dir.list_dir_begin()
	while true:
		var entry := base_dir.get_next()
		if entry == "":
			break
		if base_dir.current_is_dir() and not entry.begins_with("."):
			epoch_dirs.append(entry)
	base_dir.list_dir_end()
	epoch_dirs.sort()

	for epoch_dir in epoch_dirs:
		var epoch_path := "%s/%s" % [epochs_dir, epoch_dir]
		var world_log := _load_log_entries("%s/world_log.jsonl" % epoch_path)
		var pc_log := _load_log_entries("%s/pc_log.jsonl" % epoch_path)
		if world_log.is_empty() and pc_log.is_empty():
			continue
		_loaded_epochs.append({
			"name": epoch_dir,
			"world_log": world_log,
			"pc_log": pc_log,
		})

	if _loaded_epochs.is_empty():
		_set_marquee_text(epoch_status_label, "Epochen: keine verwertbaren world_log/pc_log Dateien gefunden")
		return

	_current_epoch_index = 0
	_current_slot = _derive_initial_slot(_loaded_epochs[_current_epoch_index].get("pc_log", []))
	_set_marquee_text(epoch_status_label, "Epochen geladen: %d" % _loaded_epochs.size())
	_scan_audio_assets()


func _load_log_entries(path: String) -> Array[Dictionary]:
	var entries: Array[Dictionary] = []
	if not FileAccess.file_exists(path):
		return entries

	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return entries
	var raw := file.get_as_text()

	var trimmed := raw.strip_edges()
	if trimmed.begins_with("["):
		var parsed = JSON.parse_string(trimmed)
		if typeof(parsed) == TYPE_ARRAY:
			for item in parsed:
				if typeof(item) == TYPE_DICTIONARY:
					entries.append(item)
		return entries

	var lines := raw.split("\n")
	for line in lines:
		var clean := line.strip_edges()
		if clean == "":
			continue
		var parsed_line = JSON.parse_string(clean)
		if typeof(parsed_line) == TYPE_DICTIONARY:
			entries.append(parsed_line)
		else:
			entries.append({"text": clean})
	return entries


func _coerce_dict_array(value: Variant) -> Array[Dictionary]:
	var entries: Array[Dictionary] = []
	if typeof(value) != TYPE_ARRAY:
		return entries
	for item in value:
		if typeof(item) == TYPE_DICTIONARY:
			entries.append(item)
	return entries


func _parse_slot_number(value: Variant) -> int:
	if typeof(value) == TYPE_INT:
		return int(value)
	if typeof(value) == TYPE_FLOAT:
		return int(value)
	var text := str(value).strip_edges()
	if text == "":
		return -1
	if text.is_valid_int():
		return int(text)
	var digits := ""
	for ch in text:
		if ch >= "0" and ch <= "9":
			digits += ch
	if digits.is_valid_int():
		return int(digits)
	return -1


func _derive_initial_slot(pc_log: Array) -> int:
	for entry in pc_log:
		if typeof(entry) != TYPE_DICTIONARY:
			continue
		var slot_value := _extract_slot_from_entry(entry)
		if slot_value >= 0:
			return slot_value
	return 0


func _extract_slot_from_entry(entry: Dictionary) -> int:
	for key in ["slot", "hour", "slot_index", "slot_id"]:
		if entry.has(key):
			var slot_number := _parse_slot_number(entry.get(key, -1))
			if slot_number >= 0:
				return slot_number
	return -1


func _live_session_epoch_name() -> String:
	if _hub_chat_session_id == "":
		return "live-session"
	return "session-%s" % _hub_chat_session_id


func _apply_live_session_state(session_payload: Dictionary) -> void:
	var world_log := _coerce_dict_array(session_payload.get("world_log", []))
	var pc_log := _coerce_dict_array(session_payload.get("pc_log", []))
	var artifact_paths := {}
	if typeof(session_payload.get("artifact_paths", {})) == TYPE_DICTIONARY:
		artifact_paths = session_payload.get("artifact_paths", {})
	_live_session_artifact_paths = artifact_paths
	_live_session_resume_checkpoint_id = str(session_payload.get("resume_checkpoint_id", "")).strip_edges()
	_loaded_epochs.clear()
	_loaded_epochs.append(
		{
			"name": _live_session_epoch_name(),
			"world_log": world_log,
			"pc_log": pc_log,
			"artifact_paths": artifact_paths,
			"source": "session_api",
		}
	)
	_current_epoch_index = 0
	var slot_number := _parse_slot_number(session_payload.get("slot_index", -1))
	if slot_number < 0:
		slot_number = _parse_slot_number(session_payload.get("slot_id", -1))
	if slot_number < 0:
		slot_number = _derive_initial_slot(pc_log)
	if slot_number < 0:
		slot_number = _current_slot
	_current_slot = clampi(slot_number, 0, 23)
	_audio_assets_present = _audio_assets_present or artifact_paths.has("tts_manifest")
	var patch_count := 0
	if typeof(session_payload.get("state_patches", [])) == TYPE_ARRAY:
		patch_count = (session_payload.get("state_patches", []) as Array).size()
	_set_marquee_text(
		epoch_status_label,
		"Epochen: Live-Session %s | pc=%d | world=%d | patches=%d" % [
			_hub_chat_session_id,
			pc_log.size(),
			world_log.size(),
			patch_count,
		]
	)
	if _live_session_resume_checkpoint_id != "":
		rp_replay_seed_label.text = "Replay-Seed: %s" % _live_session_resume_checkpoint_id
	_render_pc_centric_view()
	_refresh_module_cards()


func _hub_session_endpoint() -> String:
	var host := "127.0.0.1"
	var port := 8765
	if _sim_client:
		host = str(_sim_client.get("host"))
		port = int(_sim_client.get("port"))
	return "http://%s:%d/session/%s" % [host, port, _hub_chat_session_id.uri_encode()]


func _request_live_session_state() -> void:
	if _hub_chat_session_id == "":
		return
	if _hub_session_request == null:
		return
	if _hub_session_sync_in_flight:
		return
	if _hub_session_request.get_http_client_status() != HTTPClient.STATUS_DISCONNECTED:
		return
	var error := _hub_session_request.request(_hub_session_endpoint())
	if error != OK:
		_set_marquee_text(epoch_status_label, "Epochen: Session-Reload konnte nicht gestartet werden (%d)" % error)
		return
	_hub_session_sync_in_flight = true
	_append_runtime_event("SESSION_SYNC", {"action": "request", "session_id": _hub_chat_session_id})


func _render_pc_centric_view() -> void:
	if _loaded_epochs.is_empty():
		epoch_label.text = "Epoch: --"
		slot_label.text = "Slot: --"
		var empty_lines: Array[String] = []
		empty_lines.append("Keine Epochenlogs gefunden. Erwartet: res://data/epochs/<epoch>/world_log.jsonl + pc_log.jsonl")
		empty_lines.append("")
		empty_lines.append("Runtime-Events")
		if _runtime_events.is_empty():
			empty_lines.append("- keine Events")
		else:
			empty_lines.append_array(_runtime_events)
		log_label.text = "\n".join(empty_lines)
		_refresh_hub_chat_ui()
		return

	var epoch := _loaded_epochs[_current_epoch_index]
	var epoch_name := str(epoch.get("name", "epoch"))
	var world_log: Array = epoch.get("world_log", [])
	var pc_log: Array = epoch.get("pc_log", [])

	var unique_slots := _collect_unique_slots(world_log, pc_log)
	var pc_slot_events := _filter_events_for_slot(pc_log, _current_slot)

	epoch_label.text = "Epoch: %s" % epoch_name
	slot_label.text = "Slot: %02d (Slots geladen: %d)" % [_current_slot, unique_slots.size()]

	var lines: Array[String] = []
	lines.append("PC-zentrierte Ansicht")
	lines.append("- PC-Log-Eintraege: %d" % pc_log.size())
	lines.append("- World-Log-Eintraege: %d" % world_log.size())
	lines.append("- Slot-Eintraege (PC): %d" % pc_slot_events.size())
	lines.append("")
	if pc_slot_events.is_empty():
		lines.append("Keine PC-Eintraege fuer den aktuellen Slot gefunden.")
	else:
		for event in pc_slot_events:
			lines.append("- %s" % _event_to_text(event))

	lines.append("")
	lines.append("Runtime-Events")
	if _runtime_events.is_empty():
		lines.append("- keine Events")
	else:
		lines.append_array(_runtime_events)

	log_label.text = "\n".join(lines)
	_refresh_hub_chat_ui()


func _hub_chat_slot_id() -> String:
	return "slot-%02d" % _current_slot


func _next_hub_chat_turn_id() -> String:
	return "turn-%02d" % (_hub_chat_turn_index + 1)


func _build_hub_chat_public_context() -> String:
	var lines: Array[String] = []
	lines.append("slot: %02d" % _current_slot)
	if _hub_chat_current_scene_text != "" and _hub_chat_current_scene_text != "Kein Live-Lauf aktiv.":
		lines.append("szene: %s" % _hub_chat_current_scene_text)
	if _hub_chat_current_consequence != "":
		lines.append("konsequenz: %s" % _hub_chat_current_consequence)
	if not _hub_chat_current_options.is_empty():
		lines.append("optionen:")
		for option in _hub_chat_current_options:
			lines.append("- %s" % option)
	return "\n".join(lines)


func _build_hub_chat_retrieval_query(prompt: String) -> String:
	var parts: Array[String] = []
	parts.append(prompt.strip_edges())
	parts.append(_hub_chat_slot_id())
	if _hub_chat_scene_id != "":
		parts.append(_hub_chat_scene_id)
	if _hub_chat_current_scene_text != "" and _hub_chat_current_scene_text != "Kein Live-Lauf aktiv.":
		parts.append(_hub_chat_current_scene_text)
	if _hub_chat_current_consequence != "":
		parts.append(_hub_chat_current_consequence)
	return " | ".join(parts)


func _coerce_hub_chat_string_array(value: Variant) -> Array[String]:
	var result: Array[String] = []
	if typeof(value) != TYPE_ARRAY:
		return result
	for entry in value:
		var text := str(entry).strip_edges()
		if text != "":
			result.append(text)
	return result


func _extract_hub_chat_heading_value(line: String) -> String:
	var separator_index := line.find(":")
	if separator_index < 0:
		return ""
	return line.substr(separator_index + 1).strip_edges()


func _clean_hub_chat_item(line: String) -> String:
	var clean := line.strip_edges()
	for prefix in ["- ", "* ", "• "]:
		if clean.begins_with(prefix):
			return clean.substr(prefix.length()).strip_edges()
	return clean


func _parse_hub_chat_response(content: String) -> Dictionary:
	var scene_lines: Array[String] = []
	var consequence_lines: Array[String] = []
	var option_lines: Array[String] = []
	var state_patch_lines: Array[String] = []
	var current_section := ""

	for raw_line in content.split("\n"):
		var line := raw_line.strip_edges()
		if line == "":
			continue
		var lower := line.to_lower()
		if lower.begins_with("szene"):
			current_section = "scene"
			var scene_value := _extract_hub_chat_heading_value(line)
			if scene_value != "":
				scene_lines.append(scene_value)
			continue
		if lower.begins_with("konsequenz"):
			current_section = "consequence"
			var consequence_value := _extract_hub_chat_heading_value(line)
			if consequence_value != "":
				consequence_lines.append(consequence_value)
			continue
		if lower.begins_with("optionen"):
			current_section = "options"
			var option_value := _extract_hub_chat_heading_value(line)
			if option_value != "":
				option_lines.append(_clean_hub_chat_item(option_value))
			continue
		if lower.begins_with("state_patches") or lower.begins_with("state patches"):
			current_section = "state_patches"
			var patch_value := _extract_hub_chat_heading_value(line)
			if patch_value != "":
				state_patch_lines.append(_clean_hub_chat_item(patch_value))
			continue

		match current_section:
			"scene":
				scene_lines.append(line)
			"consequence":
				consequence_lines.append(line)
			"options":
				option_lines.append(_clean_hub_chat_item(line))
			"state_patches":
				state_patch_lines.append(_clean_hub_chat_item(line))
			_:
				pass

	var scene_text := " ".join(scene_lines).strip_edges()
	var consequence_text := " ".join(consequence_lines).strip_edges()
	if scene_text == "" and consequence_text == "" and content.strip_edges() != "":
		consequence_text = content.strip_edges().replace("\n", " ")
	return {
		"scene": scene_text,
		"consequence": consequence_text,
		"options": option_lines,
		"state_patches": state_patch_lines,
	}


func _refresh_hub_chat_ui() -> void:
	var chat_title := get_node_or_null("HubChatPanel/HubChatTitleLabel") as Label
	if chat_title:
		chat_title.text = "Live-Spielclient | %s | scene=%s | turn=%d" % [_hub_chat_slot_id(), _hub_chat_scene_id, _hub_chat_turn_index]

	var lines: Array[String] = []
	lines.append("Session: %s | Kampagne: %s" % [_hub_chat_session_id if _hub_chat_session_id != "" else "n/a", _hub_chat_campaign_id])
	lines.append("Slot/Scene: %s | %s" % [_hub_chat_slot_id(), _hub_chat_scene_id])
	lines.append("Szene: %s" % _hub_chat_current_scene_text)
	if _hub_chat_current_consequence != "":
		lines.append("Konsequenz: %s" % _hub_chat_current_consequence)
	if not _hub_chat_current_options.is_empty():
		lines.append("Optionen:")
		for option in _hub_chat_current_options:
			lines.append("- %s" % option)
	if not _hub_chat_current_state_patches.is_empty():
		lines.append("State-Patches:")
		for patch in _hub_chat_current_state_patches:
			lines.append("- %s" % patch)
	lines.append("")
	lines.append("Protokoll:")
	if _hub_chat_lines.is_empty():
		lines.append("System: Live-Spielclient bereit.")
	else:
		lines.append_array(_hub_chat_lines)
	hub_chat_history_label.text = "\n".join(lines)


func _apply_hub_chat_response(answer: String) -> void:
	var parsed := _parse_hub_chat_response(answer)
	var scene_text := str(parsed.get("scene", "")).strip_edges()
	if scene_text != "":
		_hub_chat_current_scene_text = scene_text
		_hub_chat_scene_id = _hub_chat_slot_id()
	var consequence_text := str(parsed.get("consequence", "")).strip_edges()
	_hub_chat_current_consequence = consequence_text
	_hub_chat_current_options = _coerce_hub_chat_string_array(parsed.get("options", []))
	_hub_chat_current_state_patches = _coerce_hub_chat_string_array(parsed.get("state_patches", []))
	_hub_chat_public_context = _build_hub_chat_public_context()
	if _hub_chat_pending_turn_id != "":
		_hub_chat_turn_index += 1
		_hub_chat_pending_turn_id = ""
	_refresh_hub_chat_ui()


func _collect_unique_slots(world_log: Array, pc_log: Array) -> Array[int]:
	var seen: Dictionary = {}
	for collection in [world_log, pc_log]:
		for item in collection:
			if typeof(item) != TYPE_DICTIONARY:
				continue
			var slot_value := _extract_slot_from_entry(item)
			if slot_value >= 0:
				seen[slot_value] = true
	var result: Array[int] = []
	for key in seen.keys():
		result.append(int(key))
	result.sort()
	return result


func _filter_events_for_slot(entries: Array, slot: int) -> Array[Dictionary]:
	var filtered: Array[Dictionary] = []
	for item in entries:
		if typeof(item) != TYPE_DICTIONARY:
			continue
		var item_slot := _extract_slot_from_entry(item)
		if item_slot == slot:
			filtered.append(item)
	if filtered.is_empty():
		for item in entries:
			if typeof(item) == TYPE_DICTIONARY:
				filtered.append(item)
			if filtered.size() >= 5:
				break
	return filtered


func _event_to_text(event: Dictionary) -> String:
	if event.has("text"):
		return str(event.get("text"))
	if event.has("content"):
		return str(event.get("content"))
	if event.has("event"):
		return str(event.get("event"))
	if event.has("message"):
		return str(event.get("message"))
	if event.has("summary"):
		return str(event.get("summary"))
	return JSON.stringify(event)


func _on_play_pc_audio_pressed() -> void:
	on_action_start.emit("agent_menu_toggle", {})
	if _checks_submenu_open:
		_set_checks_module_exclusive(false)
	if _rp_submenu_open:
		_set_rp_module_exclusive(false)
	_set_agent_module_exclusive(not _agent_submenu_open)
	_update_agent_menu_ui()
	_update_checks_menu_ui()
	_update_rp_menu_ui()
	if _agent_submenu_open:
		audio_status_label.text = "Agent-Modul: geöffnet"
		_refresh_latest_eval_summary(true)
	else:
		audio_status_label.text = "Agent-Modul: geschlossen"
	on_action_end.emit("agent_menu_toggle", {"open": _agent_submenu_open})

func _on_agent_back_pressed() -> void:
	_set_agent_module_exclusive(false)
	_update_agent_menu_ui()
	_update_checks_menu_ui()
	_update_rp_menu_ui()
	audio_status_label.text = "Hub-Modus aktiv"


func _set_agent_module_exclusive(open: bool) -> void:
	if open and _checks_submenu_open:
		_set_checks_module_exclusive(false)
	if open and _rp_submenu_open:
		_set_rp_module_exclusive(false)
	agent_studio_panel.visible = open
	agent_back_button.visible = open
	agent_operate_button.disabled = not open
	agent_author_button.disabled = not open
	agent_eval_run_button.disabled = not open
	agent_datasets_button.disabled = not open
	agent_synonyms_button.disabled = not open
	agent_finetune_button.disabled = not open
	agent_profiles_button.disabled = not open
	agent_ai_status_button.disabled = not open
	_agent_submenu_open = open

	_set_hub_content_visible(not open)
	_apply_responsive_layout()


func _set_checks_module_exclusive(open: bool) -> void:
	if open and _agent_submenu_open:
		_set_agent_module_exclusive(false)
	if open and _rp_submenu_open:
		_set_rp_module_exclusive(false)

	checks_studio_panel.visible = open
	checks_back_button.visible = open
	checks_target_sim_button.disabled = _checks_running or not open
	checks_target_agent_button.disabled = _checks_running or not open
	checks_target_eval_button.disabled = _checks_running or not open
	checks_target_workspace_button.disabled = _checks_running or not open
	checks_type_smoke_button.disabled = _checks_running or not open
	checks_type_unit_button.disabled = _checks_running or not open
	checks_type_api_button.disabled = _checks_running or not open
	checks_type_lint_button.disabled = _checks_running or not open
	checks_type_full_button.disabled = _checks_running or not open
	checks_run_selected_button.disabled = _checks_running or not open
	checks_run_module_pack_button.disabled = _checks_running or not open
	_checks_submenu_open = open

	_set_hub_content_visible(not open)
	_apply_responsive_layout()
	_refresh_checks_studio_ui()


func _set_rp_module_exclusive(open: bool) -> void:
	if open and _agent_submenu_open:
		_set_agent_module_exclusive(false)
	if open and _checks_submenu_open:
		_set_checks_module_exclusive(false)

	rp_studio_panel.visible = open
	rp_back_button.visible = open
	rp_hour_plus_button.disabled = not open
	rp_auto_advance_button.disabled = not open
	_rp_submenu_open = open

	_set_hub_content_visible(not open)
	_apply_responsive_layout()
	_refresh_rp_studio_ui()


func _set_hub_content_visible(visible_state: bool) -> void:
	tick_label.visible = visible_state
	time_label.visible = visible_state
	status_label.visible = visible_state
	epoch_label.visible = visible_state
	slot_label.visible = visible_state
	epoch_status_label.visible = visible_state
	play_pc_button.visible = visible_state
	play_world_button.visible = visible_state
	server_toggle_button.visible = visible_state
	hub_reload_button.visible = visible_state
	hub_checks_button.visible = visible_state
	audio_status_label.visible = visible_state
	server_status_label.visible = visible_state
	hub_config_panel.visible = visible_state
	hub_chat_panel.visible = visible_state
	log_label.visible = visible_state
	rp_studio_panel.visible = _rp_submenu_open
	sim_card_panel.visible = visible_state and _hub_show_sim_card
	api_card_panel.visible = visible_state and _hub_show_api_card
	eval_card_panel.visible = visible_state and _hub_show_eval_card


func _apply_agent_module_layout(exclusive_open: bool) -> void:
	if exclusive_open:
		var panel_width := agent_studio_panel.offset_right - agent_studio_panel.offset_left
		var panel_height := agent_studio_panel.offset_bottom - agent_studio_panel.offset_top
		var left := 24.0
		var right := panel_width - 24.0
		var col_gap := 18.0
		var col_width := maxf(240.0, (right - left - col_gap * 2.0) / 3.0)
		var col1_left := left
		var col2_left := col1_left + col_width + col_gap
		var col3_left := col2_left + col_width + col_gap
		var col1_right := col1_left + col_width
		var col2_right := col2_left + col_width
		var col3_right := minf(right, col3_left + col_width)

		agent_back_button.offset_left = right - 210.0
		agent_back_button.offset_top = 10.0
		agent_back_button.offset_right = right
		agent_back_button.offset_bottom = 42.0

		agent_studio_mode_label.offset_left = left
		agent_studio_mode_label.offset_top = 56.0
		agent_studio_mode_label.offset_right = right
		agent_studio_mode_label.offset_bottom = 76.0

		agent_operate_button.offset_left = col1_left
		agent_operate_button.offset_top = 88.0
		agent_operate_button.offset_right = col1_right
		agent_operate_button.offset_bottom = 132.0

		agent_author_button.offset_left = col2_left
		agent_author_button.offset_top = 88.0
		agent_author_button.offset_right = col2_right
		agent_author_button.offset_bottom = 132.0

		agent_dataset_source_button.offset_left = col3_left
		agent_dataset_source_button.offset_top = 88.0
		agent_dataset_source_button.offset_right = col3_right
		agent_dataset_source_button.offset_bottom = 132.0

		agent_eval_suite_button.offset_left = col3_left
		agent_eval_suite_button.offset_top = 46.0
		agent_eval_suite_button.offset_right = col3_right
		agent_eval_suite_button.offset_bottom = 80.0

		agent_eval_run_button.offset_left = col1_left
		agent_eval_run_button.offset_top = 152.0
		agent_eval_run_button.offset_right = col1_right
		agent_eval_run_button.offset_bottom = 196.0

		agent_datasets_button.offset_left = col2_left
		agent_datasets_button.offset_top = 152.0
		agent_datasets_button.offset_right = col2_right
		agent_datasets_button.offset_bottom = 196.0

		agent_synonyms_button.offset_left = col3_left
		agent_synonyms_button.offset_top = 152.0
		agent_synonyms_button.offset_right = col3_right
		agent_synonyms_button.offset_bottom = 196.0

		agent_finetune_button.offset_left = col1_left
		agent_finetune_button.offset_top = 212.0
		agent_finetune_button.offset_right = col1_right
		agent_finetune_button.offset_bottom = 256.0

		agent_profiles_button.offset_left = col2_left
		agent_profiles_button.offset_top = 212.0
		agent_profiles_button.offset_right = col2_right
		agent_profiles_button.offset_bottom = 256.0

		agent_ai_status_button.offset_left = col3_left
		agent_ai_status_button.offset_top = 212.0
		agent_ai_status_button.offset_right = col3_right
		agent_ai_status_button.offset_bottom = 256.0

		agent_eval_status_label.offset_left = left
		agent_eval_status_label.offset_top = 286.0
		agent_eval_status_label.offset_right = right
		agent_eval_status_label.offset_bottom = 306.0

		agent_system_metrics_label.offset_left = left
		agent_system_metrics_label.offset_top = 320.0
		agent_system_metrics_label.offset_right = right
		agent_system_metrics_label.offset_bottom = 340.0

		agent_latest_runs_label.offset_left = left
		agent_latest_runs_label.offset_top = 356.0
		agent_latest_runs_label.offset_right = right
		agent_latest_runs_label.offset_bottom = 376.0

		var form_top := clampf(panel_height * 0.49, 430.0, 560.0)
		agent_studio_hint_label.offset_left = left
		agent_studio_hint_label.offset_top = form_top - 40.0
		agent_studio_hint_label.offset_right = right
		agent_studio_hint_label.offset_bottom = form_top - 20.0

		agent_form_panel.offset_left = left
		agent_form_panel.offset_top = form_top
		agent_form_panel.offset_right = right
		agent_form_panel.offset_bottom = panel_height - 18.0
		return

	agent_studio_mode_label.offset_left = 10.0
	agent_studio_mode_label.offset_top = 30.0
	agent_studio_mode_label.offset_right = 10.0
	agent_studio_mode_label.offset_bottom = 30.0

	agent_operate_button.offset_left = 10.0
	agent_operate_button.offset_top = 54.0
	agent_operate_button.offset_right = 184.0
	agent_operate_button.offset_bottom = 88.0

	agent_author_button.offset_left = 196.0
	agent_author_button.offset_top = 54.0
	agent_author_button.offset_right = 370.0
	agent_author_button.offset_bottom = 88.0

	agent_dataset_source_button.offset_left = 380.0
	agent_dataset_source_button.offset_top = 54.0
	agent_dataset_source_button.offset_right = 564.0
	agent_dataset_source_button.offset_bottom = 88.0

	var compact_right := agent_studio_panel.offset_right - agent_studio_panel.offset_left - 10.0
	agent_back_button.offset_left = compact_right - 170.0
	agent_back_button.offset_top = 6.0
	agent_back_button.offset_right = compact_right
	agent_back_button.offset_bottom = 34.0

	agent_eval_suite_button.offset_left = compact_right - 184.0
	agent_eval_suite_button.offset_top = 38.0
	agent_eval_suite_button.offset_right = compact_right
	agent_eval_suite_button.offset_bottom = 68.0

	agent_eval_run_button.offset_left = 10.0
	agent_eval_run_button.offset_top = 104.0
	agent_eval_run_button.offset_right = 280.0
	agent_eval_run_button.offset_bottom = 138.0

	agent_datasets_button.offset_left = 294.0
	agent_datasets_button.offset_top = 104.0
	agent_datasets_button.offset_right = 564.0
	agent_datasets_button.offset_bottom = 138.0

	agent_synonyms_button.offset_left = 10.0
	agent_synonyms_button.offset_top = 148.0
	agent_synonyms_button.offset_right = 280.0
	agent_synonyms_button.offset_bottom = 182.0

	agent_finetune_button.offset_left = 294.0
	agent_finetune_button.offset_top = 148.0
	agent_finetune_button.offset_right = 564.0
	agent_finetune_button.offset_bottom = 182.0

	agent_profiles_button.offset_left = 10.0
	agent_profiles_button.offset_top = 192.0
	agent_profiles_button.offset_right = 280.0
	agent_profiles_button.offset_bottom = 226.0

	agent_ai_status_button.offset_left = 294.0
	agent_ai_status_button.offset_top = 192.0
	agent_ai_status_button.offset_right = 564.0
	agent_ai_status_button.offset_bottom = 226.0

	agent_eval_status_label.offset_left = 10.0
	agent_eval_status_label.offset_top = 246.0
	agent_eval_status_label.offset_right = 10.0
	agent_eval_status_label.offset_bottom = 246.0

	agent_system_metrics_label.offset_left = 10.0
	agent_system_metrics_label.offset_top = 278.0
	agent_system_metrics_label.offset_right = 10.0
	agent_system_metrics_label.offset_bottom = 278.0

	agent_latest_runs_label.offset_left = 10.0
	agent_latest_runs_label.offset_top = 316.0
	agent_latest_runs_label.offset_right = 10.0
	agent_latest_runs_label.offset_bottom = 316.0

	agent_studio_hint_label.offset_left = 10.0
	agent_studio_hint_label.offset_top = 390.0
	agent_studio_hint_label.offset_right = 10.0
	agent_studio_hint_label.offset_bottom = 390.0

	agent_form_panel.offset_left = 10.0
	agent_form_panel.offset_top = 422.0
	agent_form_panel.offset_right = 564.0
	agent_form_panel.offset_bottom = 402.0


func _on_play_world_audio_pressed() -> void:
	on_action_start.emit("rp_module_toggle", {})
	_set_rp_module_exclusive(not _rp_submenu_open)
	_update_rp_menu_ui()
	_update_agent_menu_ui()
	_update_checks_menu_ui()
	if _rp_submenu_open:
		audio_status_label.text = "RP-Modul: geoeffnet"
		_append_runtime_event("RP_MODULE", {"action": "toggle", "status": "opened", "auto_advance": _rp_auto_advance})
	else:
		audio_status_label.text = "Hub-Modus aktiv"
		_append_runtime_event("RP_MODULE", {"action": "toggle", "status": "closed"})
	on_action_end.emit("rp_module_toggle", {"status": "ok", "open": _rp_submenu_open})


func _update_agent_menu_ui() -> void:
	if _agent_submenu_open:
		play_pc_button.text = "Agent-Modul [offen]"
	else:
		play_pc_button.text = "Agent-Modul"


func _init_agent_dropdown_options() -> void:
	agent_eval_suite_button.clear()
	agent_eval_suite_button.add_item("Suite: Neutral")
	agent_eval_suite_button.add_item("Suite: RPG")
	agent_eval_suite_button.add_item("Suite: Quality DE")
	_select_option_value(agent_eval_suite_button, _EVAL_SUITE_OPTIONS, _agent_eval_suite)

	agent_dataset_source_button.clear()
	agent_dataset_source_button.add_item("Quelle: Nur erfolgreiche")
	agent_dataset_source_button.add_item("Quelle: Mit Fehlerfaellen")
	_select_option_value(agent_dataset_source_button, _DATASET_SOURCE_OPTIONS, _dataset_source_mode)


func _init_hub_config_dropdown_options() -> void:
	hub_config_default_panel_button.clear()
	hub_config_default_panel_button.add_item("Default: Hub")
	hub_config_default_panel_button.add_item("Default: Agent")
	hub_config_default_panel_button.add_item("Default: Checks")
	_select_option_value(hub_config_default_panel_button, _HUB_DEFAULT_PANEL_OPTIONS, _hub_default_panel)

	hub_config_refresh_button.clear()
	hub_config_refresh_button.add_item("Refresh: Normal")
	hub_config_refresh_button.add_item("Refresh: Fast")
	hub_config_refresh_button.add_item("Refresh: Slow")
	_select_option_value(hub_config_refresh_button, _HUB_REFRESH_PROFILE_OPTIONS, _hub_refresh_profile)


func _index_of_value(options: Array[String], value: String) -> int:
	for i in range(options.size()):
		if options[i] == value:
			return i
	return -1


func _select_option_value(button: OptionButton, options: Array[String], value: String) -> void:
	var idx := _index_of_value(options, value)
	if idx < 0:
		idx = 0
	if button.item_count > 0:
		button.select(idx)


func _update_checks_menu_ui() -> void:
	if _checks_submenu_open:
		hub_checks_button.text = "Run Checks [offen]"
	else:
		hub_checks_button.text = "Run Checks"


func _update_rp_menu_ui() -> void:
	if _rp_submenu_open:
		play_world_button.text = "RP Modul [offen]"
	else:
		play_world_button.text = "RP Modul"


func _refresh_hub_config_ui() -> void:
	hub_config_sim_card_button.text = _select_label("Sim", _hub_show_sim_card)
	hub_config_api_card_button.text = _select_label("API", _hub_show_api_card)
	hub_config_eval_card_button.text = _select_label("Eval", _hub_show_eval_card)
	_select_option_value(hub_config_default_panel_button, _HUB_DEFAULT_PANEL_OPTIONS, _hub_default_panel)
	_select_option_value(hub_config_refresh_button, _HUB_REFRESH_PROFILE_OPTIONS, _hub_refresh_profile)
	_set_marquee_text(hub_config_status_label, "Refresh=%s | default=%s" % [_hub_refresh_profile, _hub_default_panel])
	hub_config_close_button.text = "Öffnen" if _hub_config_collapsed else "Minimieren"


func _set_hub_config_collapsed(collapsed: bool) -> void:
	_hub_config_collapsed = collapsed
	var show_body := not collapsed
	hub_config_sim_card_button.visible = show_body
	hub_config_api_card_button.visible = show_body
	hub_config_eval_card_button.visible = show_body
	hub_config_default_panel_button.visible = show_body
	hub_config_refresh_button.visible = show_body
	hub_config_save_button.visible = show_body
	hub_config_status_label.visible = show_body

	if collapsed:
		hub_config_panel.offset_bottom = hub_config_panel.offset_top + _HUB_CONFIG_COLLAPSED_HEIGHT
	else:
		hub_config_panel.offset_bottom = hub_config_panel.offset_top + (_HUB_CONFIG_EXPANDED_BOTTOM - 44.0)

	hub_config_close_button.text = "Öffnen" if collapsed else "Minimieren"
	_apply_responsive_layout()


func _load_hub_preferences() -> void:
	var cfg := ConfigFile.new()
	var err := cfg.load(_HUB_PREFS_PATH)
	if err != OK:
		return

	_hub_show_sim_card = bool(cfg.get_value("hub", "show_sim_card", _hub_show_sim_card))
	_hub_show_api_card = bool(cfg.get_value("hub", "show_api_card", _hub_show_api_card))
	_hub_show_eval_card = bool(cfg.get_value("hub", "show_eval_card", _hub_show_eval_card))
	_hub_default_panel = str(cfg.get_value("hub", "default_panel", _hub_default_panel))
	_hub_refresh_profile = str(cfg.get_value("hub", "refresh_profile", _hub_refresh_profile))


func _save_hub_preferences() -> void:
	var cfg := ConfigFile.new()
	cfg.set_value("hub", "show_sim_card", _hub_show_sim_card)
	cfg.set_value("hub", "show_api_card", _hub_show_api_card)
	cfg.set_value("hub", "show_eval_card", _hub_show_eval_card)
	cfg.set_value("hub", "default_panel", _hub_default_panel)
	cfg.set_value("hub", "refresh_profile", _hub_refresh_profile)
	var err := cfg.save(_HUB_PREFS_PATH)
	if err == OK:
		hub_config_status_label.text = "Gespeichert: %s" % _HUB_PREFS_PATH
		_append_runtime_event("HUB_CONFIG", {"action": "save", "status": "ok", "path": _HUB_PREFS_PATH})
	else:
		hub_config_status_label.text = "Speichern fehlgeschlagen (err=%d)" % err
		_append_runtime_event("HUB_CONFIG", {"action": "save", "status": "failed", "err": err})


func _apply_hub_preferences() -> void:
	_set_refresh_profile(_hub_refresh_profile)
	_set_hub_content_visible(not _agent_submenu_open and not _checks_submenu_open and not _rp_submenu_open)
	_apply_card_visibility_now()
	_refresh_hub_config_ui()


func _apply_card_visibility_now() -> void:
	var in_hub := not _agent_submenu_open and not _checks_submenu_open and not _rp_submenu_open
	sim_card_panel.visible = in_hub and _hub_show_sim_card
	api_card_panel.visible = in_hub and _hub_show_api_card
	eval_card_panel.visible = in_hub and _hub_show_eval_card


func _set_refresh_profile(profile: String) -> void:
	match profile:
		"fast":
			_hub_refresh_profile = "fast"
			metrics_refresh_interval_seconds = 2.0
			eval_summary_refresh_interval_seconds = 4.0
		"slow":
			_hub_refresh_profile = "slow"
			metrics_refresh_interval_seconds = 8.0
			eval_summary_refresh_interval_seconds = 12.0
		_:
			_hub_refresh_profile = "normal"
			metrics_refresh_interval_seconds = 4.0
			eval_summary_refresh_interval_seconds = 8.0


func _cycle_refresh_profile() -> void:
	if _hub_refresh_profile == "normal":
		_set_refresh_profile("fast")
		return
	if _hub_refresh_profile == "fast":
		_set_refresh_profile("slow")
		return
	_set_refresh_profile("normal")


func _cycle_default_panel() -> void:
	if _hub_default_panel == "hub":
		_hub_default_panel = "agent"
		return
	if _hub_default_panel == "agent":
		_hub_default_panel = "checks"
		return
	_hub_default_panel = "hub"


func _open_default_panel_if_configured() -> void:
	if _hub_default_panel == "agent":
		_set_agent_module_exclusive(true)
		_update_agent_menu_ui()
		_update_checks_menu_ui()
		audio_status_label.text = "Agent-Modul: geöffnet (Default)"
		return
	if _hub_default_panel == "checks":
		_set_checks_module_exclusive(true)
		_update_checks_menu_ui()
		_update_agent_menu_ui()
		audio_status_label.text = "Checks-Modul: geöffnet (Default)"


func _on_hub_config_save_pressed() -> void:
	_save_hub_preferences()


func _on_hub_config_close_pressed() -> void:
	_set_hub_config_collapsed(not _hub_config_collapsed)


func _on_hub_config_quit_pressed() -> void:
	_append_runtime_event("HUB_CONFIG", {"action": "quit", "source": "HubConfigQuitButton"})
	get_tree().quit()


func _on_hub_config_sim_card_pressed() -> void:
	_hub_show_sim_card = not _hub_show_sim_card
	_apply_hub_preferences()
	hub_config_status_label.text = "Sim Card: %s" % ("sichtbar" if _hub_show_sim_card else "ausgeblendet")


func _on_hub_config_api_card_pressed() -> void:
	_hub_show_api_card = not _hub_show_api_card
	_apply_hub_preferences()
	hub_config_status_label.text = "API Card: %s" % ("sichtbar" if _hub_show_api_card else "ausgeblendet")


func _on_hub_config_eval_card_pressed() -> void:
	_hub_show_eval_card = not _hub_show_eval_card
	_apply_hub_preferences()
	if _agent_submenu_open or _checks_submenu_open:
		hub_config_status_label.text = "Eval Card gespeichert: %s (sichtbar im Hub)" % ("an" if _hub_show_eval_card else "aus")
	else:
		hub_config_status_label.text = "Eval Card: %s" % ("sichtbar" if _hub_show_eval_card else "ausgeblendet")


func _on_hub_config_default_panel_selected(index: int) -> void:
	if index < 0 or index >= _HUB_DEFAULT_PANEL_OPTIONS.size():
		return
	_hub_default_panel = _HUB_DEFAULT_PANEL_OPTIONS[index]
	_refresh_hub_config_ui()


func _on_hub_config_refresh_selected(index: int) -> void:
	if index < 0 or index >= _HUB_REFRESH_PROFILE_OPTIONS.size():
		return
	_set_refresh_profile(_HUB_REFRESH_PROFILE_OPTIONS[index])
	_apply_hub_preferences()


func _refresh_checks_studio_ui() -> void:
	checks_target_sim_button.text = _select_label("Sim", _checks_target == "sim")
	checks_target_agent_button.text = _select_label("Agent/API", _checks_target == "agent")
	checks_target_eval_button.text = _select_label("Eval/Training", _checks_target == "eval")
	checks_target_workspace_button.text = _select_label("Workspace", _checks_target == "workspace")

	checks_type_smoke_button.text = _select_label("Smoke", _checks_type == "smoke")
	checks_type_unit_button.text = _select_label("Unit", _checks_type == "unit")
	checks_type_api_button.text = _select_label("API/Integration", _checks_type == "api")
	checks_type_lint_button.text = _select_label("Lint/Type", _checks_type == "lint")
	checks_type_full_button.text = _select_label("Full", _checks_type == "full")

	checks_run_selected_button.disabled = _checks_running
	checks_run_module_pack_button.disabled = _checks_running

	if _checks_running:
		checks_status_label.text = "Checks: running..."
	else:
		checks_status_label.text = "Checks: target=%s | type=%s" % [_checks_target, _checks_type]


func _select_label(base: String, selected: bool) -> String:
	if selected:
		return "[x] %s" % base
	return "[ ] %s" % base


func _on_checks_target_sim_pressed() -> void:
	_checks_target = "sim"
	_refresh_checks_studio_ui()


func _on_checks_target_agent_pressed() -> void:
	_checks_target = "agent"
	_refresh_checks_studio_ui()


func _on_checks_target_eval_pressed() -> void:
	_checks_target = "eval"
	_refresh_checks_studio_ui()


func _on_checks_target_workspace_pressed() -> void:
	_checks_target = "workspace"
	_refresh_checks_studio_ui()


func _on_checks_type_smoke_pressed() -> void:
	_checks_type = "smoke"
	_refresh_checks_studio_ui()


func _on_checks_type_unit_pressed() -> void:
	_checks_type = "unit"
	_refresh_checks_studio_ui()


func _on_checks_type_api_pressed() -> void:
	_checks_type = "api"
	_refresh_checks_studio_ui()


func _on_checks_type_lint_pressed() -> void:
	_checks_type = "lint"
	_refresh_checks_studio_ui()


func _on_checks_type_full_pressed() -> void:
	_checks_type = "full"
	_refresh_checks_studio_ui()


func _on_checks_run_selected_pressed() -> void:
	if _checks_running:
		return
	_execute_check(_checks_target, _checks_type, false)


func _on_checks_run_module_pack_pressed() -> void:
	if _checks_running:
		return

	var pack := _build_module_check_pack(_checks_target)
	if pack.is_empty():
		checks_status_label.text = "Checks: keine Pack-Definition"
		return

	checks_output_label.text = ""
	for check_type in pack:
		_execute_check(_checks_target, check_type, true)


func _build_module_check_pack(target: String) -> Array[String]:
	match target:
		"sim":
			return ["smoke", "lint"]
		"agent":
			return ["smoke", "api", "unit"]
		"eval":
			return ["smoke", "lint"]
		"workspace":
			return ["smoke", "lint", "full"]
		_:
			return []


func _execute_check(target: String, check_type: String, append_output: bool) -> void:
	var spec := _build_check_command(target, check_type)
	if spec.is_empty():
		checks_status_label.text = "Checks: keine Command-Spezifikation"
		return

	var label := str(spec.get("label", "%s/%s" % [target, check_type]))
	var command_text := str(spec.get("command", ""))
	if command_text == "":
		checks_status_label.text = "Checks: Command leer"
		return

	_checks_running = true
	_refresh_checks_studio_ui()
	checks_status_label.text = "Checks: running %s" % label
	_append_checks_output("=== RUN %s ===" % label, append_output)
	_append_checks_output("$ %s" % command_text, true)

	var output := []
	var exec_code := OS.execute("pwsh", ["-NoLogo", "-NoProfile", "-Command", command_text], output, true)
	if not output.is_empty():
		_append_checks_output(str(output[0]).strip_edges(), true)

	_append_checks_output("EXITCODE=%d" % exec_code, true)
	_append_runtime_event("CHECKS_RUN", {"target": target, "type": check_type, "label": label, "exit_code": exec_code})
	if exec_code == 0:
		checks_status_label.text = "Checks: %s passed" % label
	else:
		checks_status_label.text = "Checks: %s failed (exit=%d)" % [label, exec_code]

	_checks_running = false
	_refresh_checks_studio_ui()


func _append_checks_output(chunk: String, keep_existing: bool) -> void:
	if not keep_existing:
		checks_output_label.text = chunk
		return
	if checks_output_label.text == "":
		checks_output_label.text = chunk
	else:
		checks_output_label.text += "\n" + chunk


func _build_check_command(target: String, check_type: String) -> Dictionary:
	var python_exec := _resolve_python_executable()
	var python_q := _ps_quote(python_exec)
	var workspace_root := _ps_quote(ProjectSettings.globalize_path("res://.."))
	var sim_root := _ps_quote(ProjectSettings.globalize_path("res://"))
	var godot_exec := _ps_quote(OS.get_executable_path())
	var script_summary := _ps_quote(ProjectSettings.globalize_path(eval_summary_script_path))
	var script_dataset_validate := _ps_quote(ProjectSettings.globalize_path("res://../novapolis_agent/scripts/validate_eval_datasets.py"))
	var suite_config := _ps_quote(ProjectSettings.globalize_path("res://../novapolis_agent/eval/config/suites.json"))
	var eval_script_q := _ps_quote(ProjectSettings.globalize_path(eval_script_path))

	if target == "sim":
		if check_type == "smoke":
			return {
				"label": "Sim/Smoke",
				"command": "Set-Location '%s'; & '%s' --headless --path '%s' --quit --scene res://Main.tscn" % [workspace_root, godot_exec, sim_root],
			}
		if check_type == "lint":
			return {
				"label": "Sim/Asset-Check",
				"command": "Set-Location '%s'; & '%s' scripts/check_sim_epoch_assets.py" % [workspace_root, python_q],
			}
		if check_type == "api":
			return {
				"label": "Sim/API-Tests",
				"command": "Set-Location '%s'; & '%s' -m pytest -q novapolis_agent/tests/tests_sim_api.py novapolis_agent/tests/test_api_sim_state.py" % [workspace_root, python_q],
			}
		if check_type == "unit":
			return {
				"label": "Sim/Unit",
				"command": "Set-Location '%s'; & '%s' -m pytest -q novapolis_agent/tests/test_api_sim_state.py" % [workspace_root, python_q],
			}
		if check_type == "full":
			return {
				"label": "Sim/Full",
				"command": "Set-Location '%s'; & '%s' --headless --path '%s' --quit --scene res://Main.tscn; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }; & '%s' scripts/check_sim_epoch_assets.py" % [workspace_root, godot_exec, sim_root, python_q],
			}

	if target == "agent":
		if check_type == "smoke":
			return {
				"label": "Agent/Smoke",
				"command": "Set-Location '%s'; & '%s' -m pytest -q novapolis_agent/tests/test_api_sim_state.py" % [workspace_root, python_q],
			}
		if check_type == "api":
			return {
				"label": "Agent/API",
				"command": "Set-Location '%s'; & '%s' -m pytest -q novapolis_agent/tests/tests_sim_api.py novapolis_agent/tests/test_api_sim_state.py" % [workspace_root, python_q],
			}
		if check_type == "unit":
			return {
				"label": "Agent/Unit",
				"command": "Set-Location '%s'; & '%s' -m pytest -q novapolis_agent/tests" % [workspace_root, python_q],
			}
		if check_type == "lint":
			return {
				"label": "Agent/Lint",
				"command": "Set-Location '%s'; & '%s' -m ruff check novapolis_agent" % [workspace_root, python_q],
			}
		if check_type == "full":
			return {
				"label": "Agent/Full",
				"command": "Set-Location '%s'; & '%s' -m pytest -q novapolis_agent/tests; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }; & '%s' -m ruff check novapolis_agent" % [workspace_root, python_q, python_q],
			}

	if target == "eval":
		if check_type == "smoke":
			return {
				"label": "Eval/Smoke",
				"command": "Set-Location '%s'; & '%s' '%s' --count 3" % [workspace_root, python_q, script_summary],
			}
		if check_type == "lint":
			return {
				"label": "Eval/Validate",
				"command": "Set-Location '%s'; & '%s' '%s' --strict --suite-config '%s' --suite neutral --suite rpg --suite quality_de" % [workspace_root, python_q, script_dataset_validate, suite_config],
			}
		if check_type == "api":
			return {
				"label": "Eval/Quick",
				"command": "Set-Location '%s'; & '%s' '%s' --limit 5" % [workspace_root, python_q, eval_script_q],
			}
		if check_type == "unit":
			return {
				"label": "Eval/Unit",
				"command": "Set-Location '%s'; & '%s' '%s' --strict --suite-config '%s' --suite neutral" % [workspace_root, python_q, script_dataset_validate, suite_config],
			}
		if check_type == "full":
			return {
				"label": "Eval/Full",
				"command": "Set-Location '%s'; & '%s' '%s' --strict --suite-config '%s' --suite neutral --suite rpg --suite quality_de; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }; & '%s' '%s' --count 3" % [workspace_root, python_q, script_dataset_validate, suite_config, python_q, script_summary],
			}

	if target == "workspace":
		if check_type == "smoke":
			return {
				"label": "Workspace/Smoke",
				"command": "Set-Location '%s'; & '%s' -m pytest -q novapolis_agent/tests/test_api_sim_state.py" % [workspace_root, python_q],
			}
		if check_type == "lint":
			return {
				"label": "Workspace/Lint",
				"command": "Set-Location '%s'; & '%s' -m ruff check ." % [workspace_root, python_q],
			}
		if check_type == "api":
			return {
				"label": "Workspace/API",
				"command": "Set-Location '%s'; & '%s' -m pytest -q novapolis_agent/tests/tests_sim_api.py novapolis_agent/tests/test_api_sim_state.py" % [workspace_root, python_q],
			}
		if check_type == "unit":
			return {
				"label": "Workspace/Unit",
				"command": "Set-Location '%s'; & '%s' -m pytest -q" % [workspace_root, python_q],
			}
		if check_type == "full":
			return {
				"label": "Workspace/Full",
				"command": "Set-Location '%s'; & '%s' -m ruff check .; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }; & '%s' -m pytest -q" % [workspace_root, python_q, python_q],
			}

	return {}


func _ps_quote(value: String) -> String:
	return value.replace("'", "''")


func _play_audio_for_channel(channel: String) -> void:
	if _play_audio_from_live_session(channel):
		return
	if _loaded_epochs.is_empty():
		audio_status_label.text = "Audio: keine Epochen geladen"
		return

	var epoch := _loaded_epochs[_current_epoch_index]
	var epoch_name := str(epoch.get("name", "epoch00"))
	var epoch_number := _extract_epoch_number(epoch_name)
	var file_name := "epoch%02d_slot%02d_%s.ogg" % [epoch_number, _current_slot, channel]
	var full_path := "%s/%s" % [audio_assets_dir, file_name]

	if not FileAccess.file_exists(full_path):
		audio_status_label.text = "Audio fehlt: %s" % file_name
		return

	var stream := load(full_path)
	if stream == null:
		audio_status_label.text = "Audio unlesbar: %s" % file_name
		return

	_audio_player.stream = stream
	_audio_player.play()
	audio_status_label.text = "Audio spielt: %s" % file_name


func _workspace_root_path() -> String:
	return ProjectSettings.globalize_path("res://..")


func _agent_root_path() -> String:
	return ProjectSettings.globalize_path("res://../novapolis_agent")


func _resolve_local_file_path(path: String, prefer_agent_root: bool = false) -> String:
	var normalized := path.strip_edges().replace("\\", "/")
	if normalized == "":
		return ""
	if normalized.find(":/") == 1:
		return normalized
	var workspace_root := _workspace_root_path()
	var agent_root := _agent_root_path()
	var candidates: Array[String] = []
	if prefer_agent_root or normalized.begins_with("tmp/"):
		candidates.append("%s/%s" % [agent_root, normalized])
		candidates.append("%s/%s" % [workspace_root, normalized])
	else:
		candidates.append("%s/%s" % [workspace_root, normalized])
		candidates.append("%s/%s" % [agent_root, normalized])
	for candidate in candidates:
		if FileAccess.file_exists(candidate):
			return candidate
	return candidates[0] if not candidates.is_empty() else normalized


func _load_tts_manifest_entries() -> Array[Dictionary]:
	if not _live_session_artifact_paths.has("tts_manifest"):
		return []
	var manifest_path := _resolve_local_file_path(str(_live_session_artifact_paths.get("tts_manifest", "")), true)
	return _load_log_entries(manifest_path)


func _play_audio_from_live_session(channel: String) -> bool:
	var entries := _load_tts_manifest_entries()
	if entries.is_empty():
		return false
	for idx in range(entries.size() - 1, -1, -1):
		var entry := entries[idx]
		if str(entry.get("channel", "")).strip_edges().to_lower() != channel:
			continue
		var artifact_path := _resolve_local_file_path(str(entry.get("artifact_path", "")))
		if artifact_path == "" or not FileAccess.file_exists(artifact_path):
			continue
		if artifact_path.to_lower().ends_with(".ogg"):
			var ogg_stream := AudioStreamOggVorbis.load_from_file(artifact_path)
			if ogg_stream != null:
				_audio_player.stream = ogg_stream
				_audio_player.play()
				audio_status_label.text = "Audio spielt (Session): %s" % artifact_path.get_file()
				return true
		if artifact_path.to_lower().ends_with(".wav"):
			var wav_stream := AudioStreamWAV.load_from_file(artifact_path)
			if wav_stream != null:
				_audio_player.stream = wav_stream
				_audio_player.play()
				audio_status_label.text = "Audio spielt (Session): %s" % artifact_path.get_file()
				return true
		audio_status_label.text = "Audio unlesbar (Session): %s" % artifact_path.get_file()
		return false
	audio_status_label.text = "Audio fehlt (Session): channel=%s" % channel
	return false


func _extract_epoch_number(epoch_name: String) -> int:
	var digits := ""
	for ch in epoch_name:
		if ch >= "0" and ch <= "9":
			digits += ch
	if digits.is_valid_int():
		return int(digits)
	return _current_epoch_index + 1


func _scan_audio_assets() -> void:
	_audio_assets_present = false
	if _live_session_artifact_paths.has("tts_manifest"):
		_audio_assets_present = true
		return
	var dir := DirAccess.open(audio_assets_dir)
	if dir == null:
		return
	dir.list_dir_begin()
	while true:
		var entry := dir.get_next()
		if entry == "":
			break
		if dir.current_is_dir():
			continue
		if entry.to_lower().ends_with(".ogg"):
			_audio_assets_present = true
			break
	dir.list_dir_end()


func _on_server_toggle_pressed() -> void:
	if _server_pid > 0:
		_stop_local_server()
	else:
		_start_local_server()
	_update_server_control_ui()


func _on_hub_reload_pressed() -> void:
	_request_live_session_state()
	on_action_start.emit("hub_reload", {})
	_refresh_status_label()
	_refresh_hub_topbar()
	_refresh_module_cards()
	_update_server_control_ui()
	on_action_end.emit("hub_reload", {"status": "ok"})


func _on_hub_chat_send_pressed() -> void:
	_send_hub_chat_message()


func _on_hub_chat_input_submitted(_text: String) -> void:
	_send_hub_chat_message()


func _send_hub_chat_message() -> void:
	if _hub_chat_in_flight:
		hub_chat_status_label.text = "Live-Spielclient: Anfrage laeuft bereits"
		return

	var prompt := hub_chat_input_edit.text.strip_edges()
	if prompt == "":
		hub_chat_status_label.text = "Live-Spielclient: Bitte Nachricht eingeben"
		return

	var endpoint := _hub_chat_endpoint()
	if _hub_chat_scene_id == "hub_boot":
		_hub_chat_scene_id = _hub_chat_slot_id()
	_hub_chat_public_context = _build_hub_chat_public_context()
	var turn_id := _next_hub_chat_turn_id()
	var payload := {
		"messages": [{"role": "user", "content": prompt}],
		"profile_id": hub_chat_profile_id,
		"session_id": _hub_chat_session_id,
		"options": {
			"session_id": _hub_chat_session_id,
			"orchestrator_enabled": true,
			"campaign_id": _hub_chat_campaign_id,
			"scene_id": _hub_chat_scene_id,
			"slot_id": _hub_chat_slot_id(),
			"turn_id": turn_id,
			"retrieval_query": _build_hub_chat_retrieval_query(prompt),
			"public_context": _hub_chat_public_context,
			"scheduler_hints": ["sim_live_client", _hub_chat_slot_id()],
			"state_patch_hints": ["scene.current", "pc_log.append", "world_log.append"],
		},
	}
	var body := JSON.stringify(payload, "")
	var headers := PackedStringArray(["Content-Type: application/json"])
	var err := hub_chat_request.request(endpoint, headers, HTTPClient.METHOD_POST, body)
	if err != OK:
		_hub_chat_pending_turn_id = ""
		hub_chat_status_label.text = "Live-Spielclient: Request-Fehler (%d)" % err
		_append_hub_chat_line("System", "Request konnte nicht gestartet werden.")
		return

	_hub_chat_pending_turn_id = turn_id
	_hub_chat_in_flight = true
	hub_chat_send_button.disabled = true
	hub_chat_input_edit.editable = false
	hub_chat_status_label.text = "Live-Spielclient: sende an %s" % endpoint
	_append_hub_chat_line("Du", prompt)
	hub_chat_input_edit.clear()
	_append_runtime_event("HUB_CHAT", {"action": "send", "endpoint": endpoint})


func _hub_chat_endpoint() -> String:
	var host := "127.0.0.1"
	var port := 8765
	if _sim_client:
		host = str(_sim_client.get("host"))
		port = int(_sim_client.get("port"))
	return "http://%s:%d/chat" % [host, port]


func _on_hub_chat_request_completed(result: int, response_code: int, _headers: PackedStringArray, body: PackedByteArray) -> void:
	_hub_chat_in_flight = false
	hub_chat_send_button.disabled = false
	hub_chat_input_edit.editable = true

	var text := body.get_string_from_utf8().strip_edges()
	var parsed: Variant = JSON.parse_string(text)
	if response_code >= 200 and response_code < 300:
		if typeof(parsed) == TYPE_DICTIONARY:
			var obj := parsed as Dictionary
			var answer := str(obj.get("content", ""))
			if answer == "":
				answer = str(obj.get("detail", "(leere Antwort)"))
			_append_hub_chat_line("SL", answer)
			_apply_hub_chat_response(answer)
			_request_live_session_state()
			hub_chat_status_label.text = "Live-Spielclient: Antwort ok (%d)" % response_code
		else:
			_append_hub_chat_line("SL", text)
			_apply_hub_chat_response(text)
			_request_live_session_state()
			hub_chat_status_label.text = "Live-Spielclient: Antwort ok (%d)" % response_code
	else:
		_hub_chat_pending_turn_id = ""
		var detail := "HTTP %d | result=%d" % [response_code, result]
		if typeof(parsed) == TYPE_DICTIONARY:
			var err_obj := parsed as Dictionary
			detail = "%s | %s" % [detail, str(err_obj.get("detail", "Fehler ohne Detail"))]
		elif text != "":
			detail = "%s | %s" % [detail, text]
		_append_hub_chat_line("System", detail)
		hub_chat_status_label.text = "Live-Spielclient: Fehler (%d)" % response_code

	_append_runtime_event("HUB_CHAT", {"action": "response", "http": response_code, "result": result})


func _on_hub_session_request_completed(result: int, response_code: int, _headers: PackedStringArray, body: PackedByteArray) -> void:
	_hub_session_sync_in_flight = false
	var text := body.get_string_from_utf8().strip_edges()
	var parsed: Variant = JSON.parse_string(text)
	if result != HTTPRequest.RESULT_SUCCESS:
		_set_marquee_text(epoch_status_label, "Epochen: Session-Sync fehlgeschlagen (%d)" % result)
		_append_runtime_event("SESSION_SYNC", {"action": "error", "result": result})
		return
	if response_code < 200 or response_code >= 300:
		var detail := "HTTP %d" % response_code
		if typeof(parsed) == TYPE_DICTIONARY:
			detail = "%s | %s" % [detail, str((parsed as Dictionary).get("detail", "Fehler ohne Detail"))]
		_set_marquee_text(epoch_status_label, "Epochen: %s" % detail)
		_append_runtime_event("SESSION_SYNC", {"action": "http_error", "http": response_code})
		return
	if typeof(parsed) != TYPE_DICTIONARY:
		_set_marquee_text(epoch_status_label, "Epochen: Session-Antwort unlesbar")
		_append_runtime_event("SESSION_SYNC", {"action": "parse_error", "http": response_code})
		return
	_apply_live_session_state(parsed as Dictionary)
	_append_runtime_event(
		"SESSION_SYNC",
		{
			"action": "applied",
			"session_id": _hub_chat_session_id,
			"http": response_code,
		}
	)


func _append_hub_chat_line(role: String, content: String) -> void:
	var clean := content.strip_edges().replace("\n", " ")
	if clean.length() > 220:
		clean = "%s..." % clean.left(217)
	var line := "%s %s: %s" % [Time.get_time_string_from_system(), role, clean]
	_hub_chat_lines.append(line)
	while _hub_chat_lines.size() > _HUB_CHAT_MAX_LINES:
		_hub_chat_lines.remove_at(0)
	_refresh_hub_chat_ui()


func _on_hub_checks_pressed() -> void:
	on_action_start.emit("hub_checks", {})
	_set_checks_module_exclusive(not _checks_submenu_open)
	_update_checks_menu_ui()
	_update_agent_menu_ui()
	if _checks_submenu_open:
		audio_status_label.text = "Checks-Modul: geöffnet"
		_append_runtime_event("CHECKS_UI", {"status": "opened", "target": _checks_target, "type": _checks_type})
	else:
		audio_status_label.text = "Checks-Modul: geschlossen"
		_append_runtime_event("CHECKS_UI", {"status": "closed"})
	on_action_end.emit("hub_checks", {"status": "ok", "open": _checks_submenu_open})


func _on_checks_back_pressed() -> void:
	_set_checks_module_exclusive(false)
	_update_checks_menu_ui()
	audio_status_label.text = "Hub-Modus aktiv"


func _on_rp_back_pressed() -> void:
	_set_rp_module_exclusive(false)
	_update_rp_menu_ui()
	audio_status_label.text = "Hub-Modus aktiv"


func _on_rp_hour_plus_pressed() -> void:
	if _loaded_epochs.is_empty():
		rp_status_label.text = "RP: keine Epochen geladen"
		return

	var from_slot := _current_slot
	_current_slot = (_current_slot + 1) % 24
	_render_pc_centric_view()
	rp_status_label.text = "RP: Hour +1 (%02d -> %02d)" % [from_slot, _current_slot]
	_append_runtime_event("RP_HOUR_JUMP", {"from": from_slot, "to": _current_slot})


func _on_rp_auto_advance_pressed() -> void:
	_rp_auto_advance = not _rp_auto_advance
	if _rp_auto_advance:
		_rp_last_auto_advance_ms = Time.get_ticks_msec()
	_refresh_rp_studio_ui()
	_append_runtime_event("RP_AUTO_ADVANCE", {"enabled": _rp_auto_advance})


func _refresh_rp_studio_ui() -> void:
	if _last_world_state.has("sim_meta") and typeof(_last_world_state.get("sim_meta")) == TYPE_DICTIONARY:
		var sim_meta: Dictionary = _last_world_state.get("sim_meta", {})
		rp_replay_seed_label.text = "Replay-Seed: %s" % str(sim_meta.get("seed", "n/a"))
	else:
		rp_replay_seed_label.text = "Replay-Seed: n/a"

	rp_auto_advance_button.text = _select_label("Auto-Advance", _rp_auto_advance)
	rp_status_label.text = "RP: slot=%02d | auto=%s" % [_current_slot, str(_rp_auto_advance)]


func _run_rp_auto_advance(force: bool) -> void:
	if not _rp_auto_advance:
		return
	if _loaded_epochs.is_empty():
		return

	var now_ms := Time.get_ticks_msec()
	if not force and _rp_last_auto_advance_ms >= 0:
		if (now_ms - _rp_last_auto_advance_ms) < 900:
			return
	_rp_last_auto_advance_ms = now_ms

	var epoch := _loaded_epochs[_current_epoch_index]
	var pc_log: Array = epoch.get("pc_log", [])
	var has_slot_events := not _filter_events_for_slot(pc_log, _current_slot).is_empty()
	if has_slot_events:
		return

	var from_slot := _current_slot
	_current_slot = (_current_slot + 1) % 24
	_render_pc_centric_view()
	rp_status_label.text = "RP: Auto-Advance %02d -> %02d" % [from_slot, _current_slot]
	_append_runtime_event("RP_AUTO_ADVANCE", {"from": from_slot, "to": _current_slot, "reason": "empty_pc_slot"})


func _open_agent_form(kind: String) -> void:
	_agent_form_kind = kind
	_agent_form_template_signature = ""
	if kind == "datasets":
		_agent_form_mode_value = _dataset_source_mode
		_agent_form_target_value = "new"
		agent_form_name_edit.text = "user_dataset_%s" % Time.get_datetime_string_from_system(false, true).replace(":", "").replace("-", "").replace(" ", "_")
	elif kind == "finetune":
		_agent_form_mode_value = _finetune_profile
		_agent_form_target_value = "new"
		agent_form_name_edit.text = _finetune_output_name
	elif kind == "profiles":
		_agent_form_mode_value = "balanced"
		if _active_profile_mode != "":
			_agent_form_mode_value = _active_profile_mode
		_agent_form_target_value = "new"
		agent_form_name_edit.text = "profile_default"
		if _active_profile_name != "":
			agent_form_name_edit.text = _active_profile_name
	elif kind == "advanced":
		_agent_form_mode_value = "balanced"
		_agent_form_target_value = "update"
		agent_form_name_edit.text = "advanced_settings"
	elif kind == "jobs":
		_agent_form_mode_value = "eval"
		_agent_form_target_value = "new"
		agent_form_name_edit.text = "job_%s" % Time.get_datetime_string_from_system(false, true).replace(":", "").replace("-", "").replace(" ", "_")
	else:
		_agent_form_mode_value = "pairs"
		_agent_form_target_value = "append_user"
		agent_form_name_edit.text = "user_synonyms"

	_refresh_agent_form_ui()


func _on_agent_form_mode_selected(index: int) -> void:
	if _form_dropdowns_syncing:
		return
	var options := _agent_form_mode_options_for_kind(_agent_form_kind)
	if index < 0 or index >= options.size():
		return
	_agent_form_mode_value = options[index]
	_refresh_agent_form_ui()


func _on_agent_form_target_selected(index: int) -> void:
	if _form_dropdowns_syncing:
		return
	var options := _agent_form_target_options_for_kind(_agent_form_kind)
	if index < 0 or index >= options.size():
		return
	_agent_form_target_value = options[index]
	_refresh_agent_form_ui()


func _agent_form_mode_options_for_kind(kind: String) -> Array[String]:
	if kind == "datasets":
		return ["clean", "with_failures"]
	if kind == "synonyms":
		return ["pairs", "broader_terms"]
	if kind == "finetune":
		return ["baseline", "quality", "extended"]
	if kind == "profiles":
		return ["balanced", "strict", "creative"]
	if kind == "advanced":
		return ["balanced", "strict", "explorative"]
	if kind == "jobs":
		return ["eval", "finetune", "datasets"]
	return ["pairs", "broader_terms"]


func _agent_form_target_options_for_kind(kind: String) -> Array[String]:
	if kind == "datasets" or kind == "synonyms":
		return ["new", "append_user"]
	if kind == "profiles":
		return ["new", "update"]
	if kind == "jobs":
		return ["new", "retry_latest", "cancel_latest"]
	return []


func _agent_form_mode_display_label(kind: String, value: String) -> String:
	if kind == "datasets":
		return _dataset_mode_label(value)
	if kind == "synonyms":
		return _synonym_mode_label(value)
	if kind == "finetune":
		return _finetune_profile_label(value)
	if kind == "profiles":
		return _profile_mode_label(value)
	if kind == "advanced":
		return _advanced_mode_label(value)
	if kind == "jobs":
		return _job_type_label(value)
	return value


func _refresh_agent_form_dropdowns() -> void:
	var mode_options := _agent_form_mode_options_for_kind(_agent_form_kind)
	if mode_options.is_empty():
		mode_options = ["default"]

	if _index_of_value(mode_options, _agent_form_mode_value) < 0:
		_agent_form_mode_value = mode_options[0]

	_form_dropdowns_syncing = true
	agent_form_mode_button.clear()
	for value in mode_options:
		agent_form_mode_button.add_item(_agent_form_mode_display_label(_agent_form_kind, value))
	_select_option_value(agent_form_mode_button, mode_options, _agent_form_mode_value)

	var target_options := _agent_form_target_options_for_kind(_agent_form_kind)
	agent_form_target_button.clear()
	if target_options.is_empty():
		agent_form_target_button.add_item("Nicht relevant")
		agent_form_target_button.disabled = true
	else:
		if _index_of_value(target_options, _agent_form_target_value) < 0:
			_agent_form_target_value = target_options[0]
		for value in target_options:
			agent_form_target_button.add_item(_form_target_label(value))
		agent_form_target_button.disabled = false
		_select_option_value(agent_form_target_button, target_options, _agent_form_target_value)
	_form_dropdowns_syncing = false


func _on_agent_form_apply_pressed() -> void:
	if _agent_form_kind == "":
		return
	var payload := _build_agent_form_payload_from_controls()
	if payload.is_empty():
		return
	if _agent_form_kind == "datasets":
		_apply_dataset_form_payload(payload)
		return

	if _agent_form_kind == "synonyms":
		_apply_synonym_form_payload(payload)
		return

	if _agent_form_kind == "finetune":
		_apply_finetune_form_payload(payload)
		return

	if _agent_form_kind == "profiles":
		_apply_profile_form_payload(payload)
		return

	if _agent_form_kind == "advanced":
		_apply_advanced_settings_form_payload(payload)
		return

	if _agent_form_kind == "jobs":
		_apply_jobs_form_payload(payload)
		return

	agent_form_status_label.text = "Form: Unbekannter Form-Typ"


func _build_agent_form_payload_from_controls() -> Dictionary:
	var payload: Dictionary = {}
	if _agent_form_kind == "datasets":
		var dataset_name := agent_form_name_edit.text.strip_edges()
		if dataset_name == "":
			agent_form_status_label.text = "Form: Name fehlt"
			return {}
		var sys_prompt := _form_control_text("dataset_system_prompt").strip_edges()
		var user_prompt := _form_control_text("dataset_user_prompt").strip_edges()
		var assistant_prompt := _form_control_text("dataset_assistant_prompt").strip_edges()
		if user_prompt == "" or assistant_prompt == "":
			agent_form_status_label.text = "Form: User/Assistant-Beispiel fehlt"
			return {}
		payload = {
			"dataset_name": dataset_name,
			"dataset_tag": _form_control_text("dataset_tag", "v1"),
			"target": _agent_form_target_value,
			"set_active": _form_control_bool("dataset_set_active", true),
			"source_mode": _agent_form_mode_value,
			"records": [
				{
					"messages": [
						{"role": "system", "content": sys_prompt if sys_prompt != "" else "Du bist Novapolis Agent."},
						{"role": "user", "content": user_prompt},
						{"role": "assistant", "content": assistant_prompt},
					],
				}
			],
			"train_ratio": _form_control_float("dataset_train_ratio", 0.9),
			"min_output_chars": _form_control_int("dataset_min_output_chars", 20),
			"notes": _form_control_text("dataset_notes", ""),
		}
		return payload

	if _agent_form_kind == "synonyms":
		var synonym_set := agent_form_name_edit.text.strip_edges()
		if synonym_set == "":
			agent_form_status_label.text = "Form: Name fehlt"
			return {}
		var term := _form_control_text("syn_term").strip_edges()
		var syn_csv := _form_control_text("syn_values_csv").strip_edges()
		if term == "" or syn_csv == "":
			agent_form_status_label.text = "Form: term/synonyms fehlt"
			return {}
		var synonyms: Array[String] = []
		for part in syn_csv.split(","):
			var clean := str(part).strip_edges()
			if clean != "":
				synonyms.append(clean)
		if synonyms.is_empty():
			agent_form_status_label.text = "Form: mind. ein Synonym erforderlich"
			return {}
		payload = {
			"synonym_set": synonym_set,
			"synonym_tag": _form_control_text("syn_tag", "v1"),
			"target": _agent_form_target_value,
			"set_active": _form_control_bool("syn_set_active", true),
			"mode": _agent_form_mode_value,
			"import_path": _form_control_text("syn_import_path", ""),
			"export_path": _form_control_text("syn_export_path", ""),
			"entries": [{"term": term, "synonyms": synonyms}],
			"notes": _form_control_text("syn_notes", ""),
		}
		return payload

	if _agent_form_kind == "finetune":
		payload = {
			"profile": _agent_form_mode_value,
			"base_model": _form_control_text("ft_base_model", _finetune_base_model),
			"output_name": agent_form_name_edit.text.strip_edges(),
			"train_file": _form_control_text("ft_train_file", ""),
			"epochs": _form_control_int("ft_epochs", 1),
			"max_steps": _form_control_int("ft_max_steps", 10),
			"batch_size": _form_control_int("ft_batch_size", 1),
			"lr": _form_control_float("ft_lr", 0.0002),
			"no_check": _form_control_bool("ft_no_check", true),
			"notes": _form_control_text("ft_notes", ""),
		}
		return payload

	if _agent_form_kind == "profiles":
		payload = {
			"profile_name": agent_form_name_edit.text.strip_edges(),
			"target": _agent_form_target_value,
			"mode": _agent_form_mode_value,
			"prompt_system": _form_control_text("profile_prompt_system", ""),
			"behavior_notes": _form_control_text("profile_behavior_notes", ""),
			"assign_to": _form_control_csv_array("profile_assign_to_csv"),
			"set_active": _form_control_bool("profile_set_active", true),
			"archive": _form_control_bool("profile_archive", false),
			"notes": _form_control_text("profile_notes", ""),
		}
		return payload

	if _agent_form_kind == "advanced":
		payload = {
			"mode": _agent_form_mode_value,
			"policy_profile": _form_control_text("adv_policy_profile", "default"),
			"strictness_level": _form_control_text("adv_strictness_level", "normal"),
			"safety_profile": _form_control_text("adv_safety_profile", "standard"),
			"debug_level": _form_control_text("adv_debug_level", "minimal"),
			"system_behavior": _form_control_text("adv_system_behavior", ""),
			"notes": _form_control_text("adv_notes", ""),
		}
		return payload

	if _agent_form_kind == "jobs":
		payload = {
			"job_name": agent_form_name_edit.text.strip_edges(),
			"job_type": _agent_form_mode_value,
			"target": _agent_form_target_value,
			"enqueue": _form_control_bool("job_enqueue", true),
			"priority": _form_control_int("job_priority", 10),
			"payload": {"notes": _form_control_text("job_payload_notes", "")},
			"notes": _form_control_text("job_notes", ""),
		}
		return payload

	return {}


func _form_control_text(key: String, fallback: String = "") -> String:
	var ctrl: Variant = _agent_form_controls.get(key, null)
	if ctrl is LineEdit:
		return (ctrl as LineEdit).text
	if ctrl is TextEdit:
		return (ctrl as TextEdit).text
	return fallback


func _form_control_int(key: String, fallback: int) -> int:
	var ctrl: Variant = _agent_form_controls.get(key, null)
	if ctrl is SpinBox:
		return int((ctrl as SpinBox).value)
	return fallback


func _form_control_float(key: String, fallback: float) -> float:
	var ctrl: Variant = _agent_form_controls.get(key, null)
	if ctrl is SpinBox:
		return float((ctrl as SpinBox).value)
	return fallback


func _form_control_bool(key: String, fallback: bool) -> bool:
	var ctrl: Variant = _agent_form_controls.get(key, null)
	if ctrl is CheckBox:
		return (ctrl as CheckBox).button_pressed
	return fallback


func _form_control_csv_array(key: String) -> Array[String]:
	var values: Array[String] = []
	var raw := _form_control_text(key, "")
	for part in raw.split(","):
		var clean := str(part).strip_edges()
		if clean != "":
			values.append(clean)
	return values


func _apply_dataset_form_payload(payload: Dictionary) -> void:
	var dataset_name := _sanitize_agent_form_name(str(payload.get("dataset_name", "")))
	if dataset_name == "":
		agent_form_status_label.text = "Form: dataset_name fehlt"
		return
	var dataset_tag := _sanitize_agent_form_name(str(payload.get("dataset_tag", "v1")))
	if dataset_tag == "":
		dataset_tag = "v1"
	var set_active := bool(payload.get("set_active", true))

	var target := str(payload.get("target", _agent_form_target_value))
	if target != "new" and target != "append_user":
		agent_form_status_label.text = "Form: target muss new/append_user sein"
		return

	var records_any = payload.get("records", [])
	if typeof(records_any) != TYPE_ARRAY:
		agent_form_status_label.text = "Form: records muss Array sein"
		return
	var records: Array = records_any
	if records.is_empty():
		agent_form_status_label.text = "Form: records ist leer"
		return

	for rec_any in records:
		if typeof(rec_any) != TYPE_DICTIONARY:
			agent_form_status_label.text = "Form: records enthaelt ungueltige Eintraege"
			return
		var rec: Dictionary = rec_any
		var msgs_any = rec.get("messages", [])
		if typeof(msgs_any) != TYPE_ARRAY or msgs_any.is_empty():
			agent_form_status_label.text = "Form: jeder record braucht messages[]"
			return

	var base_dir := "user://agent_user_data/datasets"
	DirAccess.make_dir_recursive_absolute(base_dir)
	var file_path := "%s/%s.jsonl" % [base_dir, dataset_name]
	var exists := FileAccess.file_exists(file_path)

	if target == "new" and exists:
		agent_form_status_label.text = "Form: Dataset existiert bereits"
		return
	if target == "append_user" and not exists:
		agent_form_status_label.text = "Form: Dataset fuer append nicht gefunden"
		return

	var mode := FileAccess.WRITE
	if exists:
		mode = FileAccess.READ_WRITE
	var f := FileAccess.open(file_path, mode)
	if f == null:
		agent_form_status_label.text = "Form: Datei konnte nicht geoeffnet werden"
		return

	if exists:
		f.seek_end()

	for rec_out in records:
		f.store_string(JSON.stringify(rec_out, "") + "\n")
	f.close()
	_update_dataset_registry(dataset_name, dataset_tag, set_active)

	agent_form_status_label.text = "Form: Dataset gespeichert (%s@%s, +%d)" % [dataset_name, dataset_tag, records.size()]
	_append_runtime_event("AGENT_FORM", {"kind": "datasets", "target": target, "name": dataset_name, "tag": dataset_tag, "set_active": set_active, "records": records.size(), "path": file_path})


func _apply_synonym_form_payload(payload: Dictionary) -> void:
	var synonym_set := _sanitize_agent_form_name(str(payload.get("synonym_set", "")))
	if synonym_set == "":
		agent_form_status_label.text = "Form: synonym_set fehlt"
		return
	var synonym_tag := _sanitize_agent_form_name(str(payload.get("synonym_tag", "v1")))
	if synonym_tag == "":
		synonym_tag = "v1"
	var set_active := bool(payload.get("set_active", true))

	var target := str(payload.get("target", _agent_form_target_value))
	if target != "new" and target != "append_user":
		agent_form_status_label.text = "Form: target muss new/append_user sein"
		return

	var entries_any = payload.get("entries", [])
	if typeof(entries_any) != TYPE_ARRAY:
		agent_form_status_label.text = "Form: entries muss Array sein"
		return
	var entries: Array = entries_any
	if entries.is_empty():
		agent_form_status_label.text = "Form: entries ist leer"
		return
	var import_path := str(payload.get("import_path", "")).strip_edges()
	var export_path := str(payload.get("export_path", "")).strip_edges()
	if import_path != "":
		var imported_result := _load_synonym_entries_from_path(import_path)
		if not bool(imported_result.get("ok", false)):
			agent_form_status_label.text = "Form: Import fehlgeschlagen (%s)" % str(imported_result.get("reason", "parse"))
			return
		var imported_any = imported_result.get("entries", [])
		if typeof(imported_any) == TYPE_ARRAY:
			for imported_entry_any in imported_any:
				entries.append(imported_entry_any)

	for e_any in entries:
		if typeof(e_any) != TYPE_DICTIONARY:
			agent_form_status_label.text = "Form: entries enthaelt ungueltige Eintraege"
			return
		var e: Dictionary = e_any
		if str(e.get("term", "")).strip_edges() == "":
			agent_form_status_label.text = "Form: jeder Eintrag braucht term"
			return

	var base_dir := "user://agent_user_data/synonyms"
	DirAccess.make_dir_recursive_absolute(base_dir)
	var file_path := "%s/%s.json" % [base_dir, synonym_set]
	var exists := FileAccess.file_exists(file_path)

	if target == "new" and exists:
		agent_form_status_label.text = "Form: Synonym-Set existiert bereits"
		return
	if target == "append_user" and not exists:
		agent_form_status_label.text = "Form: Synonym-Set fuer append nicht gefunden"
		return

	var merged_entries: Array = []
	var existing_entries_snapshot: Array = []
	if exists:
		var rf := FileAccess.open(file_path, FileAccess.READ)
		if rf != null:
			var raw := rf.get_as_text()
			rf.close()
			var parsed_existing = JSON.parse_string(raw)
			if typeof(parsed_existing) == TYPE_DICTIONARY:
				var existing_dict: Dictionary = parsed_existing
				var ex = existing_dict.get("entries", [])
				if typeof(ex) == TYPE_ARRAY:
					merged_entries = ex
					existing_entries_snapshot = ex.duplicate(true)

	for add_item in entries:
		merged_entries.append(add_item)

	var delta := _build_synonym_delta(existing_entries_snapshot, merged_entries)
	var validator := _validate_synonym_entries(merged_entries)
	var validator_status := str(validator.get("status", "warn"))
	if validator_status == "error":
		agent_form_status_label.text = "Form: Synonyms ungueltig (%s)" % str(validator.get("reason", "validation"))
		return

	var out_payload: Dictionary = {
		"synonym_set": synonym_set,
		"synonym_tag": synonym_tag,
		"mode": str(payload.get("mode", _agent_form_mode_value)),
		"entries": merged_entries,
		"validator_status": validator_status,
		"validator_warnings": validator.get("warnings", []),
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	var wf := FileAccess.open(file_path, FileAccess.WRITE)
	if wf == null:
		agent_form_status_label.text = "Form: Synonym-Datei konnte nicht geschrieben werden"
		return
	wf.store_string(JSON.stringify(out_payload, "  "))
	wf.close()
	if export_path != "":
		var export_ok := _write_json_to_path(export_path, out_payload)
		if not export_ok:
			agent_form_status_label.text = "Form: Exportpfad konnte nicht geschrieben werden"
			return
	_update_synonym_registry(synonym_set, synonym_tag, set_active)

	_synonym_status_text = "Synonyms: active %s | delta=+%d terms/+%d syns | validator=%s" % [_active_synonym_label().replace("Active Synonyms: ", ""), int(delta.get("terms_added", 0)), int(delta.get("synonyms_added", 0)), validator_status]
	agent_form_status_label.text = "Form: Synonyms gespeichert (%s@%s, +%d)" % [synonym_set, synonym_tag, entries.size()]
	_append_runtime_event("AGENT_FORM", {
		"kind": "synonyms",
		"target": target,
		"name": synonym_set,
		"tag": synonym_tag,
		"set_active": set_active,
		"entries_added": entries.size(),
		"delta_terms": int(delta.get("terms_added", 0)),
		"delta_synonyms": int(delta.get("synonyms_added", 0)),
		"validator_status": validator_status,
		"path": file_path,
	})


func _load_synonym_entries_from_path(path_text: String) -> Dictionary:
	var normalized := path_text.strip_edges()
	if normalized == "":
		return {"ok": false, "reason": "empty_path", "entries": []}
	var exists_path := normalized
	if normalized.begins_with("user://") or normalized.begins_with("res://"):
		exists_path = ProjectSettings.globalize_path(normalized)
	if not FileAccess.file_exists(exists_path):
		return {"ok": false, "reason": "file_missing", "entries": []}

	var rf := FileAccess.open(normalized, FileAccess.READ)
	if rf == null:
		rf = FileAccess.open(exists_path, FileAccess.READ)
	if rf == null:
		return {"ok": false, "reason": "open_failed", "entries": []}
	var raw := rf.get_as_text()
	rf.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return {"ok": false, "reason": "parse_failed", "entries": []}
	var doc: Dictionary = parsed
	var entries_any = doc.get("entries", [])
	if typeof(entries_any) != TYPE_ARRAY:
		return {"ok": false, "reason": "entries_not_array", "entries": []}
	return {"ok": true, "reason": "ok", "entries": entries_any}


func _build_synonym_delta(before_entries: Array, after_entries: Array) -> Dictionary:
	var before_terms := {}
	var before_pair_count := 0
	for item_any in before_entries:
		if typeof(item_any) != TYPE_DICTIONARY:
			continue
		var item: Dictionary = item_any
		var term := str(item.get("term", "")).strip_edges().to_lower()
		if term == "":
			continue
		before_terms[term] = true
		var syn_any = item.get("synonyms", [])
		if typeof(syn_any) == TYPE_ARRAY:
			before_pair_count += (syn_any as Array).size()

	var after_terms := {}
	var after_pair_count := 0
	for item2_any in after_entries:
		if typeof(item2_any) != TYPE_DICTIONARY:
			continue
		var item2: Dictionary = item2_any
		var term2 := str(item2.get("term", "")).strip_edges().to_lower()
		if term2 == "":
			continue
		after_terms[term2] = true
		var syn2_any = item2.get("synonyms", [])
		if typeof(syn2_any) == TYPE_ARRAY:
			after_pair_count += (syn2_any as Array).size()

	return {
		"terms_added": maxi(0, after_terms.size() - before_terms.size()),
		"synonyms_added": maxi(0, after_pair_count - before_pair_count),
	}


func _validate_synonym_entries(entries: Array) -> Dictionary:
	var warnings: Array[String] = []
	var seen_terms := {}
	for idx in range(entries.size()):
		var item_any = entries[idx]
		if typeof(item_any) != TYPE_DICTIONARY:
			return {"status": "error", "reason": "entry_not_object_%d" % idx, "warnings": warnings}
		var item: Dictionary = item_any
		var term := str(item.get("term", "")).strip_edges().to_lower()
		if term == "":
			return {"status": "error", "reason": "term_missing_%d" % idx, "warnings": warnings}
		if seen_terms.has(term):
			warnings.append("duplicate_term:%s" % term)
		seen_terms[term] = true
		var syn_any = item.get("synonyms", [])
		if typeof(syn_any) != TYPE_ARRAY:
			return {"status": "error", "reason": "synonyms_not_array_%s" % term, "warnings": warnings}
		var syn_arr: Array = syn_any
		if syn_arr.is_empty():
			warnings.append("empty_synonyms:%s" % term)
	return {
		"status": "ok" if warnings.is_empty() else "warn",
		"reason": "ok",
		"warnings": warnings,
	}


func _write_json_to_path(path_text: String, payload: Dictionary) -> bool:
	var normalized := path_text.strip_edges()
	if normalized == "":
		return false
	var abs_path := normalized
	if normalized.begins_with("user://") or normalized.begins_with("res://"):
		abs_path = ProjectSettings.globalize_path(normalized)
	var parent_dir := abs_path.get_base_dir()
	if parent_dir != "":
		DirAccess.make_dir_recursive_absolute(parent_dir)
	var wf := FileAccess.open(normalized, FileAccess.WRITE)
	if wf == null:
		wf = FileAccess.open(abs_path, FileAccess.WRITE)
	if wf == null:
		return false
	wf.store_string(JSON.stringify(payload, "  "))
	wf.close()
	return true


func _apply_finetune_form_payload(payload: Dictionary) -> void:
	if _finetune_pid > 0:
		agent_form_status_label.text = "Form: Finetune laeuft bereits"
		return

	var profile := _sanitize_agent_form_name(str(payload.get("profile", "baseline")))
	if profile == "":
		profile = "baseline"
	var base_model := str(payload.get("base_model", "sshleifer/tiny-gpt2")).strip_edges()
	if base_model == "":
		agent_form_status_label.text = "Form: base_model fehlt"
		return

	var output_name := _sanitize_agent_form_name(str(payload.get("output_name", _finetune_output_name)))
	if output_name == "":
		output_name = "lora-agent-hub"

	var epochs := int(payload.get("epochs", 1))
	var max_steps := int(payload.get("max_steps", 10))
	var batch_size := int(payload.get("batch_size", 1))
	var lr := _to_float_or_default(payload.get("lr", 0.0002), 0.0002)
	var no_check := bool(payload.get("no_check", true))

	if epochs < 1:
		agent_form_status_label.text = "Form: epochs muss >= 1 sein"
		return
	if max_steps < 1:
		agent_form_status_label.text = "Form: max_steps muss >= 1 sein"
		return
	if batch_size < 1:
		agent_form_status_label.text = "Form: batch_size muss >= 1 sein"
		return
	if lr <= 0.0:
		agent_form_status_label.text = "Form: lr muss > 0 sein"
		return

	var train_file := str(payload.get("train_file", "")).strip_edges()
	if train_file == "":
		train_file = _resolve_finetune_train_file()
	if train_file == "":
		agent_form_status_label.text = "Form: keine Train-Datei verfuegbar"
		return

	var train_path_abs := ProjectSettings.globalize_path(train_file) if train_file.begins_with("user://") else train_file
	if not FileAccess.file_exists(train_path_abs):
		agent_form_status_label.text = "Form: train_file fehlt"
		return

	var options: Dictionary = {
		"profile": profile,
		"base_model": base_model,
		"output_name": output_name,
		"train_file": train_path_abs,
		"epochs": epochs,
		"max_steps": max_steps,
		"batch_size": batch_size,
		"lr": lr,
		"no_check": no_check,
	}

	var started := _start_finetune_run(options)
	if not started:
		agent_form_status_label.text = "Form: Finetune konnte nicht gestartet werden"
		return

	agent_form_status_label.text = "Form: Finetune gestartet (%s, %s)" % [profile, base_model]


func _apply_profile_form_payload(payload: Dictionary) -> void:
	var profile_name := _sanitize_agent_form_name(str(payload.get("profile_name", "")))
	if profile_name == "":
		agent_form_status_label.text = "Form: profile_name fehlt"
		return

	var target := str(payload.get("target", _agent_form_target_value))
	if target != "new" and target != "update":
		agent_form_status_label.text = "Form: target muss new/update sein"
		return

	var mode := _sanitize_agent_form_name(str(payload.get("mode", _agent_form_mode_value)))
	if mode == "":
		mode = "balanced"

	var prompt_system := str(payload.get("prompt_system", "")).strip_edges()
	if prompt_system == "":
		agent_form_status_label.text = "Form: prompt_system fehlt"
		return

	var assign_any = payload.get("assign_to", [])
	if typeof(assign_any) != TYPE_ARRAY:
		agent_form_status_label.text = "Form: assign_to muss Array sein"
		return
	var assign_to: Array = assign_any

	var set_active := bool(payload.get("set_active", true))
	var archive := bool(payload.get("archive", false))

	var base_dir := "user://agent_user_data/profiles"
	DirAccess.make_dir_recursive_absolute(base_dir)
	var file_path := "%s/%s.json" % [base_dir, profile_name]
	var exists := FileAccess.file_exists(file_path)

	if target == "new" and exists:
		agent_form_status_label.text = "Form: Profil existiert bereits"
		return
	if target == "update" and not exists:
		agent_form_status_label.text = "Form: Profil fuer update nicht gefunden"
		return

	var out_payload: Dictionary = {
		"profile_name": profile_name,
		"mode": mode,
		"prompt_system": prompt_system,
		"behavior_notes": str(payload.get("behavior_notes", "")).strip_edges(),
		"assign_to": assign_to,
		"archive": archive,
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}

	var wf := FileAccess.open(file_path, FileAccess.WRITE)
	if wf == null:
		agent_form_status_label.text = "Form: Profil-Datei konnte nicht geschrieben werden"
		return
	wf.store_string(JSON.stringify(out_payload, "  "))
	wf.close()

	_update_profile_registry(profile_name, mode, set_active and not archive, archive)
	agent_form_status_label.text = "Form: Profil gespeichert (%s, mode=%s)" % [profile_name, mode]
	_append_runtime_event("AGENT_FORM", {"kind": "profiles", "target": target, "name": profile_name, "mode": mode, "set_active": set_active, "archive": archive, "path": file_path})


func _apply_advanced_settings_form_payload(payload: Dictionary) -> void:
	var mode := _sanitize_agent_form_name(str(payload.get("mode", _agent_form_mode_value)))
	if mode == "":
		mode = "balanced"

	var policy_profile := _sanitize_agent_form_name(str(payload.get("policy_profile", "default")))
	if policy_profile == "":
		policy_profile = "default"

	var strictness_level := _sanitize_agent_form_name(str(payload.get("strictness_level", "normal")))
	if strictness_level == "":
		strictness_level = "normal"

	var safety_profile := _sanitize_agent_form_name(str(payload.get("safety_profile", "standard")))
	if safety_profile == "":
		safety_profile = "standard"

	var debug_level := _sanitize_agent_form_name(str(payload.get("debug_level", "minimal")))
	if debug_level == "":
		debug_level = "minimal"

	var system_behavior := str(payload.get("system_behavior", "")).strip_edges()
	if system_behavior == "":
		agent_form_status_label.text = "Form: system_behavior fehlt"
		return

	DirAccess.make_dir_recursive_absolute("user://agent_user_data/settings")
	var out_payload: Dictionary = {
		"mode": mode,
		"policy_profile": policy_profile,
		"strictness_level": strictness_level,
		"safety_profile": safety_profile,
		"debug_level": debug_level,
		"system_behavior": system_behavior,
		"notes": str(payload.get("notes", "")).strip_edges(),
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}

	var wf := FileAccess.open(_ADVANCED_SETTINGS_PATH, FileAccess.WRITE)
	if wf == null:
		agent_form_status_label.text = "Form: Advanced Settings konnten nicht gespeichert werden"
		return
	wf.store_string(JSON.stringify(out_payload, "  "))
	wf.close()

	_advanced_settings_status_text = "Advanced: %s | policy=%s | strict=%s" % [mode, policy_profile, strictness_level]
	agent_form_status_label.text = "Form: Advanced Settings gespeichert (%s)" % mode
	_append_runtime_event("AGENT_FORM", {"kind": "advanced", "mode": mode, "policy_profile": policy_profile, "strictness_level": strictness_level, "path": _ADVANCED_SETTINGS_PATH})


func _apply_jobs_form_payload(payload: Dictionary) -> void:
	var target := str(payload.get("target", _agent_form_target_value))
	if target != "new" and target != "retry_latest" and target != "cancel_latest":
		agent_form_status_label.text = "Form: target muss new/retry_latest/cancel_latest sein"
		return

	var queue_payload := _load_jobs_queue_payload()
	var jobs := _jobs_array_from_payload(queue_payload)

	if target == "retry_latest":
		var retry_index := _find_latest_job_index_by_status(jobs, ["failed", "cancelled"])
		if retry_index < 0:
			agent_form_status_label.text = "Form: kein fehlgeschlagener/abgebrochener Job fuer Retry"
			return
		var base_any = jobs[retry_index]
		if typeof(base_any) != TYPE_DICTIONARY:
			agent_form_status_label.text = "Form: Retry-Quelle ist ungueltig"
			return
		var base_job: Dictionary = base_any
		var base_name := _sanitize_agent_form_name(str(base_job.get("name", "job")))
		if base_name == "":
			base_name = "job"
		var retry_name := "%s_retry" % base_name
		var attempt := int(base_job.get("attempt", 1)) + 1
		var retry_entry: Dictionary = {
			"id": "job_%d" % Time.get_ticks_msec(),
			"name": retry_name,
			"type": str(base_job.get("type", "eval")),
			"status": "queued",
			"priority": int(base_job.get("priority", 10)),
			"created_at": Time.get_datetime_string_from_system(false, true),
			"retry_of": str(base_job.get("id", "")),
			"attempt": attempt,
			"payload": base_job.get("payload", {}),
		}
		jobs.append(retry_entry)
		queue_payload["jobs"] = jobs
		queue_payload["updated_at"] = Time.get_datetime_string_from_system(false, true)
		if not _write_jobs_queue_payload(queue_payload):
			agent_form_status_label.text = "Form: Jobs-Queue konnte nicht gespeichert werden"
			return
		_refresh_jobs_status_text(jobs)
		agent_form_status_label.text = "Form: Retry eingereiht (%s)" % retry_name
		_append_runtime_event("AGENT_FORM", {"kind": "jobs", "action": "retry_latest", "retry_of": str(base_job.get("id", "")), "name": retry_name, "queue_size": jobs.size(), "path": _JOBS_QUEUE_PATH})
		return

	if target == "cancel_latest":
		var cancel_index := _find_latest_job_index_by_status(jobs, ["queued", "running"])
		if cancel_index < 0:
			agent_form_status_label.text = "Form: kein aktiver Job fuer Cancel"
			return
		var cancel_any = jobs[cancel_index]
		if typeof(cancel_any) != TYPE_DICTIONARY:
			agent_form_status_label.text = "Form: Cancel-Ziel ist ungueltig"
			return
		var cancel_job: Dictionary = cancel_any
		cancel_job["status"] = "cancelled"
		cancel_job["cancelled_at"] = Time.get_datetime_string_from_system(false, true)
		cancel_job["cancel_reason"] = str(payload.get("notes", "manual_cancel"))
		jobs[cancel_index] = cancel_job
		queue_payload["jobs"] = jobs
		queue_payload["updated_at"] = Time.get_datetime_string_from_system(false, true)
		if not _write_jobs_queue_payload(queue_payload):
			agent_form_status_label.text = "Form: Jobs-Queue konnte nicht gespeichert werden"
			return
		_refresh_jobs_status_text(jobs)
		agent_form_status_label.text = "Form: Job abgebrochen (%s)" % str(cancel_job.get("name", "job"))
		_append_runtime_event("AGENT_FORM", {"kind": "jobs", "action": "cancel_latest", "id": str(cancel_job.get("id", "")), "name": str(cancel_job.get("name", "job")), "queue_size": jobs.size(), "path": _JOBS_QUEUE_PATH})
		return

	var job_name := _sanitize_agent_form_name(str(payload.get("job_name", agent_form_name_edit.text)))
	if job_name == "":
		agent_form_status_label.text = "Form: job_name fehlt"
		return

	var job_type := _sanitize_agent_form_name(str(payload.get("job_type", _agent_form_mode_value)))
	if job_type == "":
		job_type = "eval"

	var priority := int(payload.get("priority", 10))
	if priority < 0:
		priority = 0
	if priority > 100:
		priority = 100

	var enqueue_now := bool(payload.get("enqueue", true))
	if not enqueue_now:
		agent_form_status_label.text = "Form: enqueue=false, kein Job angelegt"
		return

	var job_payload_any = payload.get("payload", {})
	if typeof(job_payload_any) != TYPE_DICTIONARY:
		job_payload_any = {}
	var job_payload: Dictionary = job_payload_any

	var job_entry: Dictionary = {
		"id": "job_%d" % Time.get_ticks_msec(),
		"name": job_name,
		"type": job_type,
		"status": "queued",
		"priority": priority,
		"attempt": 1,
		"created_at": Time.get_datetime_string_from_system(false, true),
		"payload": job_payload,
	}
	jobs.append(job_entry)
	queue_payload["jobs"] = jobs
	queue_payload["updated_at"] = Time.get_datetime_string_from_system(false, true)

	if not _write_jobs_queue_payload(queue_payload):
		agent_form_status_label.text = "Form: Jobs-Queue konnte nicht gespeichert werden"
		return

	_refresh_jobs_status_text(jobs)
	agent_form_status_label.text = "Form: Job eingereiht (%s, prio=%d)" % [job_type, priority]
	_append_runtime_event("AGENT_FORM", {"kind": "jobs", "action": "enqueue", "name": job_name, "job_type": job_type, "priority": priority, "queue_size": jobs.size(), "path": _JOBS_QUEUE_PATH})


func _load_jobs_queue_payload() -> Dictionary:
	DirAccess.make_dir_recursive_absolute("user://agent_user_data/jobs")
	var queue_payload: Dictionary = {
		"jobs": [],
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	if not FileAccess.file_exists(_JOBS_QUEUE_PATH):
		return queue_payload
	var rf := FileAccess.open(_JOBS_QUEUE_PATH, FileAccess.READ)
	if rf == null:
		return queue_payload
	var raw := rf.get_as_text()
	rf.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) == TYPE_DICTIONARY:
		queue_payload = parsed
	if typeof(queue_payload.get("jobs", [])) != TYPE_ARRAY:
		queue_payload["jobs"] = []
	return queue_payload


func _jobs_array_from_payload(queue_payload: Dictionary) -> Array:
	var jobs_any = queue_payload.get("jobs", [])
	if typeof(jobs_any) != TYPE_ARRAY:
		return []
	return jobs_any


func _write_jobs_queue_payload(queue_payload: Dictionary) -> bool:
	var wf := FileAccess.open(_JOBS_QUEUE_PATH, FileAccess.WRITE)
	if wf == null:
		return false
	wf.store_string(JSON.stringify(queue_payload, "  "))
	wf.close()
	return true


func _find_latest_job_index_by_status(jobs: Array, statuses: Array[String]) -> int:
	for i in range(jobs.size() - 1, -1, -1):
		var item_any = jobs[i]
		if typeof(item_any) != TYPE_DICTIONARY:
			continue
		var item: Dictionary = item_any
		var status := str(item.get("status", ""))
		if statuses.has(status):
			return i
	return -1


func _refresh_jobs_status_text(jobs: Array) -> void:
	if jobs.is_empty():
		_jobs_status_text = "Jobs: queued=0"
		return
	var queued := 0
	var running := 0
	var failed := 0
	var cancelled := 0
	for item_any in jobs:
		if typeof(item_any) != TYPE_DICTIONARY:
			continue
		var item: Dictionary = item_any
		var status := str(item.get("status", "queued"))
		if status == "queued":
			queued += 1
		elif status == "running":
			running += 1
		elif status == "failed":
			failed += 1
		elif status == "cancelled":
			cancelled += 1

	var latest_name := "job"
	var latest_type := "n/a"
	var latest_status := "n/a"
	for i in range(jobs.size() - 1, -1, -1):
		var latest_any = jobs[i]
		if typeof(latest_any) != TYPE_DICTIONARY:
			continue
		var latest: Dictionary = latest_any
		latest_name = str(latest.get("name", "job"))
		latest_type = str(latest.get("type", "n/a"))
		latest_status = str(latest.get("status", "n/a"))
		break

	_jobs_status_text = "Jobs: queued=%d | running=%d | failed=%d | cancelled=%d | latest=%s (%s/%s)" % [queued, running, failed, cancelled, latest_name, latest_type, latest_status]


func _sanitize_agent_form_name(value: String) -> String:
	var result := value.strip_edges().to_lower()
	result = result.replace(" ", "_")
	result = result.replace("/", "_")
	result = result.replace("\\", "_")
	result = result.replace(":", "_")
	result = result.replace(";", "_")
	result = result.replace("\"", "")
	result = result.replace("'", "")
	return result


func _refresh_agent_form_ui() -> void:
	var show_form := _agent_submenu_open and _agent_studio_mode == "author" and (_agent_form_kind == "datasets" or _agent_form_kind == "synonyms" or _agent_form_kind == "finetune" or _agent_form_kind == "profiles" or _agent_form_kind == "advanced" or _agent_form_kind == "jobs")
	agent_form_panel.visible = show_form
	if not show_form:
		return
	agent_form_payload_edit.visible = false
	agent_form_fields_scroll.visible = true
	_refresh_agent_form_dropdowns()
	agent_form_name_edit.placeholder_text = _agent_form_name_placeholder_for_kind(_agent_form_kind)
	agent_form_payload_edit.placeholder_text = _agent_form_payload_placeholder_for_kind(_agent_form_kind)

	var signature := "%s|%s|%s" % [_agent_form_kind, _agent_form_mode_value, _agent_form_target_value]
	var template_changed := signature != _agent_form_template_signature
	_agent_form_template_signature = signature
	if template_changed:
		_rebuild_agent_form_fields()

	_layout_agent_form_controls()

	if _agent_form_kind == "datasets":
		agent_form_title_label.text = "Form: Datasets"
		if template_changed:
			agent_form_status_label.text = "Form: Datasets-Konfiguration bereit"
	elif _agent_form_kind == "finetune":
		agent_form_title_label.text = "Form: Finetune"
		if template_changed:
			agent_form_status_label.text = "Form: Finetune-Konfiguration bereit"
	elif _agent_form_kind == "profiles":
		agent_form_title_label.text = "Form: Profiles"
		if template_changed:
			agent_form_status_label.text = "Form: Profile-Konfiguration bereit"
	elif _agent_form_kind == "advanced":
		agent_form_title_label.text = "Form: Advanced Settings"
		if template_changed:
			agent_form_status_label.text = "Form: Advanced-Settings-Konfiguration bereit"
	elif _agent_form_kind == "jobs":
		agent_form_title_label.text = "Form: Jobs"
		if template_changed:
			agent_form_status_label.text = "Form: Jobs-Konfiguration bereit"
	else:
		agent_form_title_label.text = "Form: Synonyms"
		if template_changed:
			agent_form_status_label.text = "Form: Synonym-Konfiguration bereit"


func _layout_agent_form_controls() -> void:
	var panel_w := agent_form_panel.offset_right - agent_form_panel.offset_left
	var panel_h := agent_form_panel.offset_bottom - agent_form_panel.offset_top
	var left := 12.0
	var right := maxf(left + 24.0, panel_w - 12.0)

	agent_form_title_label.offset_left = left
	agent_form_title_label.offset_top = 10.0
	agent_form_title_label.offset_right = right
	agent_form_title_label.offset_bottom = 28.0

	var row_top := 38.0
	var row_bottom := 72.0
	var field_gap := 12.0
	var field_w := maxf(140.0, (right - left - field_gap) / 2.0)

	agent_form_mode_button.offset_left = left
	agent_form_mode_button.offset_top = row_top
	agent_form_mode_button.offset_right = left + field_w
	agent_form_mode_button.offset_bottom = row_bottom

	agent_form_target_button.offset_left = agent_form_mode_button.offset_right + field_gap
	agent_form_target_button.offset_top = row_top
	agent_form_target_button.offset_right = right
	agent_form_target_button.offset_bottom = row_bottom

	agent_form_name_edit.offset_left = left
	agent_form_name_edit.offset_top = 84.0
	agent_form_name_edit.offset_right = right - 98.0
	agent_form_name_edit.offset_bottom = 114.0

	agent_form_apply_button.offset_left = right - 90.0
	agent_form_apply_button.offset_top = 84.0
	agent_form_apply_button.offset_right = right
	agent_form_apply_button.offset_bottom = 114.0

	var fields_bottom := maxf(164.0, panel_h - 44.0)
	agent_form_fields_scroll.offset_left = left
	agent_form_fields_scroll.offset_top = 126.0
	agent_form_fields_scroll.offset_right = right
	agent_form_fields_scroll.offset_bottom = fields_bottom

	agent_form_payload_edit.offset_left = left
	agent_form_payload_edit.offset_top = 126.0
	agent_form_payload_edit.offset_right = right
	agent_form_payload_edit.offset_bottom = fields_bottom

	agent_form_status_label.offset_left = left
	agent_form_status_label.offset_top = fields_bottom + 12.0
	agent_form_status_label.offset_right = right
	agent_form_status_label.offset_bottom = fields_bottom + 30.0


func _rebuild_agent_form_fields() -> void:
	for child in agent_form_fields_box.get_children():
		child.queue_free()
	_agent_form_controls.clear()

	if _agent_form_kind == "datasets":
		_add_form_line_field("dataset_tag", "Dataset-Tag", _active_dataset_tag if _active_dataset_tag != "" else "v1", "z. B. v1")
		_add_form_int_field("dataset_min_output_chars", "Min. Output Chars", 20, 1, 2000)
		_add_form_float_field("dataset_train_ratio", "Train-Ratio", 0.9, 0.1, 0.99, 0.01)
		_add_form_bool_field("dataset_set_active", "Als aktives Dataset setzen", true)
		_add_form_text_field("dataset_system_prompt", "System-Prompt", "Du bist Novapolis Agent.", "Optionaler System-Kontext", 66.0)
		_add_form_text_field("dataset_user_prompt", "User-Beispiel", "", "z. B. Erstelle eine kurze RP-Szene mit Konflikt und Hook.", 66.0)
		_add_form_text_field("dataset_assistant_prompt", "Assistant-Beispiel", "", "z. B. Hier ist eine kurze RP-Szene...", 66.0)
		_add_form_text_field("dataset_notes", "Notizen", "", "Optional", 56.0)
		return

	if _agent_form_kind == "synonyms":
		_add_form_line_field("syn_tag", "Synonym-Tag", _active_synonym_tag if _active_synonym_tag != "" else "v1", "z. B. v1")
		_add_form_bool_field("syn_set_active", "Als aktives Synonym-Set setzen", true)
		_add_form_line_field("syn_term", "Begriff", "", "z. B. Aufstand")
		_add_form_line_field("syn_values_csv", "Synonyme (CSV)", "", "z. B. rebell, revolt, uprising")
		_add_form_text_field("syn_notes", "Notizen", "", "Optional", 56.0)
		return

	if _agent_form_kind == "finetune":
		_add_form_line_field("ft_base_model", "Base Model", _finetune_base_model, "z. B. sshleifer/tiny-gpt2")
		_add_form_line_field("ft_train_file", "Train-Datei (optional)", "", "Leer = automatische Aufloesung")
		_add_form_int_field("ft_epochs", "Epochs", 1, 1, 20)
		_add_form_int_field("ft_max_steps", "Max Steps", 10, 1, 100000)
		_add_form_int_field("ft_batch_size", "Batch Size", 1, 1, 128)
		_add_form_float_field("ft_lr", "Learning Rate", 0.0002, 0.000001, 0.01, 0.0001)
		_add_form_bool_field("ft_no_check", "Pre-Checks ueberspringen", true)
		_add_form_text_field("ft_notes", "Notizen", "", "Optional", 56.0)
		return

	if _agent_form_kind == "profiles":
		_add_form_text_field("profile_prompt_system", "System-Prompt", "Du bist ein hilfreicher Novapolis-Agent mit klaren, kurzen Antworten.", "Pflichtfeld", 90.0)
		_add_form_text_field("profile_behavior_notes", "Behavior Notes", "Priorisiert Klarheit, Korrektheit und kurze Struktur.", "Optional", 72.0)
		_add_form_line_field("profile_assign_to_csv", "Assign To (CSV)", "eval,finetune", "z. B. eval,finetune")
		_add_form_bool_field("profile_set_active", "Als aktives Profil setzen", true)
		_add_form_bool_field("profile_archive", "Profil archivieren", false)
		_add_form_text_field("profile_notes", "Notizen", "", "Optional", 56.0)
		return

	if _agent_form_kind == "advanced":
		_add_form_line_field("adv_policy_profile", "Policy Profile", "default", "z. B. default")
		_add_form_line_field("adv_strictness_level", "Strictness", "normal", "z. B. normal")
		_add_form_line_field("adv_safety_profile", "Safety Profile", "standard", "z. B. standard")
		_add_form_line_field("adv_debug_level", "Debug Level", "minimal", "z. B. minimal")
		_add_form_text_field("adv_system_behavior", "System Behavior", "", "Pflichtfeld", 90.0)
		_add_form_text_field("adv_notes", "Notizen", "", "Optional", 56.0)
		return

	if _agent_form_kind == "jobs":
		_add_form_bool_field("job_enqueue", "Job sofort einreihen", true)
		_add_form_int_field("job_priority", "Prioritaet", 10, 0, 100)
		_add_form_text_field("job_payload_notes", "Payload Notes", "", "z. B. limit=20, suite=neutral", 72.0)
		_add_form_text_field("job_notes", "Notizen", "", "Optional", 56.0)


func _add_form_line_field(key: String, label_text: String, value: String, placeholder: String) -> void:
	var label := Label.new()
	label.text = label_text
	agent_form_fields_box.add_child(label)

	var edit := LineEdit.new()
	edit.text = value
	edit.placeholder_text = placeholder
	agent_form_fields_box.add_child(edit)
	_agent_form_controls[key] = edit


func _add_form_text_field(key: String, label_text: String, value: String, placeholder: String, height: float) -> void:
	var label := Label.new()
	label.text = label_text
	agent_form_fields_box.add_child(label)

	var edit := TextEdit.new()
	edit.text = value
	edit.placeholder_text = placeholder
	edit.custom_minimum_size = Vector2(0.0, height)
	agent_form_fields_box.add_child(edit)
	_agent_form_controls[key] = edit


func _add_form_int_field(key: String, label_text: String, value: int, min_value: int, max_value: int) -> void:
	var label := Label.new()
	label.text = label_text
	agent_form_fields_box.add_child(label)

	var spin := SpinBox.new()
	spin.min_value = min_value
	spin.max_value = max_value
	spin.step = 1.0
	spin.rounded = true
	spin.value = value
	agent_form_fields_box.add_child(spin)
	_agent_form_controls[key] = spin


func _add_form_float_field(key: String, label_text: String, value: float, min_value: float, max_value: float, step_value: float) -> void:
	var label := Label.new()
	label.text = label_text
	agent_form_fields_box.add_child(label)

	var spin := SpinBox.new()
	spin.min_value = min_value
	spin.max_value = max_value
	spin.step = step_value
	spin.value = value
	agent_form_fields_box.add_child(spin)
	_agent_form_controls[key] = spin


func _add_form_bool_field(key: String, label_text: String, value: bool) -> void:
	var check := CheckBox.new()
	check.text = label_text
	check.button_pressed = value
	agent_form_fields_box.add_child(check)
	_agent_form_controls[key] = check


func _agent_form_name_placeholder_for_kind(kind: String) -> String:
	if kind == "datasets":
		return "z. B. user_dataset_support_faq"
	if kind == "synonyms":
		return "z. B. user_synonyms_novapolis"
	if kind == "finetune":
		return "z. B. lora-novapolis-v1"
	if kind == "profiles":
		return "z. B. profile_strict_short"
	if kind == "advanced":
		return "z. B. advanced_settings"
	if kind == "jobs":
		return "z. B. job_eval_neutral"
	return "Name eingeben"


func _agent_form_payload_placeholder_for_kind(kind: String) -> String:
	if kind == "datasets":
		return "JSON-Beispiel: dataset_name, dataset_tag, records[] ..."
	if kind == "synonyms":
		return "JSON-Beispiel: synonym_set, entries[] ..."
	if kind == "finetune":
		return "JSON-Beispiel: base_model, train_file, epochs ..."
	if kind == "profiles":
		return "JSON-Beispiel: profile_name, mode, prompt_system ..."
	if kind == "advanced":
		return "JSON-Beispiel: mode, policy_profile, strictness_level ..."
	if kind == "jobs":
		return "JSON-Beispiel: job_name, job_type, priority, payload ..."
	return "JSON eingeben"


func _dataset_mode_label(mode_value: String) -> String:
	if mode_value == "with_failures":
		return "Mit Fehlerfaellen"
	return "Nur erfolgreiche"


func _synonym_mode_label(mode_value: String) -> String:
	if mode_value == "broader_terms":
		return "Weitere Begriffe"
	return "Paare"


func _finetune_profile_label(profile_value: String) -> String:
	if profile_value == "quality":
		return "Qualitaet"
	if profile_value == "extended":
		return "Extended"
	return "Baseline"


func _form_target_label(target_value: String) -> String:
	if target_value == "append_user":
		return "Bestehende User-Datei erweitern"
	if target_value == "update":
		return "Bestehende Datei aktualisieren"
	if target_value == "retry_latest":
		return "Retry: letzten failed/cancelled Job einreihen"
	if target_value == "cancel_latest":
		return "Cancel: letzten queued/running Job abbrechen"
	return "Neue Datei erstellen"


func _profile_mode_label(mode_value: String) -> String:
	if mode_value == "strict":
		return "Strict"
	if mode_value == "creative":
		return "Creative"
	return "Balanced"


func _profile_target_label(target_value: String) -> String:
	if target_value == "update":
		return "Bestehendes Profil aktualisieren"
	return "Neues Profil erstellen"


func _advanced_mode_label(mode_value: String) -> String:
	if mode_value == "strict":
		return "Strict"
	if mode_value == "explorative":
		return "Explorative"
	return "Balanced"


func _job_type_label(job_type: String) -> String:
	if job_type == "finetune":
		return "Finetune"
	if job_type == "datasets":
		return "Datasets"
	return "Eval"


func _build_dataset_form_template() -> String:
	var name_value := agent_form_name_edit.text.strip_edges()
	if name_value == "":
		name_value = "user_dataset"
	var tag_value := "v1"
	if _active_dataset_tag != "":
		tag_value = _active_dataset_tag
	return JSON.stringify(
		{
			"dataset_name": name_value,
			"dataset_tag": tag_value,
			"target": _agent_form_target_value,
			"set_active": true,
			"source_mode": _agent_form_mode_value,
			"records": [
				{
					"messages": [
						{"role": "system", "content": "Du bist Novapolis Agent."},
						{"role": "user", "content": "Kurze Beispielanfrage"},
						{"role": "assistant", "content": "Kurze Beispielantwort"}
					]
				}
			],
			"train_ratio": 0.9,
			"min_output_chars": 20,
			"notes": "Records fuellen; dataset_tag setzen; set_active=true markiert dieses Dataset als aktiv.",
		},
		"  "
	)


func _build_synonym_form_template() -> String:
	var name_value := agent_form_name_edit.text.strip_edges()
	if name_value == "":
		name_value = "user_synonyms"
	var tag_value := "v1"
	if _active_synonym_tag != "":
		tag_value = _active_synonym_tag
	return JSON.stringify(
		{
			"synonym_set": name_value,
			"synonym_tag": tag_value,
			"target": _agent_form_target_value,
			"set_active": true,
			"mode": _agent_form_mode_value,
			"entries": [
				{"term": "beispiel", "synonyms": ["muster", "sample"]}
			],
			"notes": "Entries fuellen; synonym_tag setzen; set_active=true markiert dieses Synonym-Set als aktiv.",
		},
		"  "
	)


func _build_finetune_form_template() -> String:
	var output_name := agent_form_name_edit.text.strip_edges()
	if output_name == "":
		output_name = _finetune_output_name
	var train_file := _resolve_finetune_train_file()
	if train_file == "":
		train_file = "res://../novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl"

	return JSON.stringify(
		{
			"profile": _agent_form_mode_value,
			"base_model": _finetune_base_model,
			"output_name": output_name,
			"train_file": train_file,
			"epochs": 1,
			"max_steps": 10,
			"batch_size": 1,
			"lr": 0.0002,
			"no_check": true,
			"notes": "Apply startet den Finetune-Run. Im Operate-Modus kann ueber Finetune Stop abgebrochen werden.",
		},
		"  "
	)


func _build_profile_form_template() -> String:
	var name_value := agent_form_name_edit.text.strip_edges()
	if name_value == "":
		name_value = "profile_default"

	return JSON.stringify(
		{
			"profile_name": name_value,
			"target": _agent_form_target_value,
			"mode": _agent_form_mode_value,
			"prompt_system": "Du bist ein hilfreicher Novapolis-Agent mit klaren, kurzen Antworten.",
			"behavior_notes": "Priorisiert Klarheit, Korrektheit und kurze Struktur.",
			"assign_to": ["eval", "finetune"],
			"set_active": true,
			"archive": false,
			"notes": "target=new|update; archive=true setzt Profil auf Archivstatus.",
		},
		"  "
	)


func _build_advanced_settings_form_template() -> String:
	return JSON.stringify(
		{
			"mode": _agent_form_mode_value,
			"policy_profile": "default",
			"strictness_level": "normal",
			"safety_profile": "standard",
			"debug_level": "minimal",
			"system_behavior": "Antworten knapp, regelkonform und nachvollziehbar; bei Unsicherheit defensiv.",
			"notes": "Wird unter user://agent_user_data/settings/advanced.json gespeichert.",
		},
		"  "
	)


func _build_jobs_form_template() -> String:
	var job_name := agent_form_name_edit.text.strip_edges()
	if job_name == "":
		job_name = "job_default"

	return JSON.stringify(
		{
			"job_name": job_name,
			"job_type": _agent_form_mode_value,
			"enqueue": true,
			"priority": 10,
			"payload": {
				"notes": "Ausfuehrungsdetails folgen in Jobs Schritt 2.",
			},
			"notes": "Schritt 1: Queue-Eintrag in user://agent_user_data/jobs/queue.json",
		},
		"  "
	)


func _on_agent_operate_pressed() -> void:
	_agent_studio_mode = "operate"
	_refresh_agent_studio_ui()
	_append_runtime_event("AGENT_STUDIO_MODE", {"mode": _agent_studio_mode})


func _on_agent_author_pressed() -> void:
	_agent_studio_mode = "author"
	_refresh_agent_studio_ui()
	_append_runtime_event("AGENT_STUDIO_MODE", {"mode": _agent_studio_mode})


func _on_agent_eval_suite_selected(index: int) -> void:
	if index < 0 or index >= _EVAL_SUITE_OPTIONS.size():
		return
	if _eval_pid > 0:
		_append_runtime_event("AGENT_ACTION", {"action": "eval_suite", "status": "blocked", "reason": "eval_running", "pid": _eval_pid})
		_select_option_value(agent_eval_suite_button, _EVAL_SUITE_OPTIONS, _agent_eval_suite)
		return

	_agent_eval_suite = _EVAL_SUITE_OPTIONS[index]

	_refresh_agent_studio_ui()
	_append_runtime_event("AGENT_ACTION", {"action": "eval_suite", "status": "selected", "suite": _agent_eval_suite})


func _on_agent_dataset_source_selected(index: int) -> void:
	if index < 0 or index >= _DATASET_SOURCE_OPTIONS.size():
		return
	if _dataset_pid > 0:
		_append_runtime_event("AGENT_DATASETS", {"action": "source_mode", "status": "blocked", "reason": "running", "pid": _dataset_pid})
		_select_option_value(agent_dataset_source_button, _DATASET_SOURCE_OPTIONS, _dataset_source_mode)
		return

	_dataset_source_mode = _DATASET_SOURCE_OPTIONS[index]

	_dataset_status_text = "Datasets: source=%s" % _dataset_source_mode
	_refresh_agent_studio_ui()
	_append_runtime_event("AGENT_DATASETS", {"action": "source_mode", "mode": _dataset_source_mode})


func _on_agent_eval_run_pressed() -> void:
	if _agent_studio_mode == "author":
		_open_agent_form("jobs")
		_append_runtime_event("AGENT_ACTION", {"action": "jobs", "mode": _agent_studio_mode, "status": "form_opened"})
		return

	if _agent_studio_mode != "operate":
		_append_runtime_event("AGENT_ACTION", {"action": "eval_run", "mode": _agent_studio_mode, "status": "blocked", "reason": "author_mode"})
		return
	if _eval_pid > 0:
		if not _confirm_destructive_action("eval_stop", "Eval Stop: zweite Betaetigung zur Bestaetigung"):
			_refresh_agent_studio_ui()
			return
		var stop_rc := int(OS.kill(_eval_pid))
		_append_runtime_event("AGENT_ACTION", {"action": "eval_run", "mode": _agent_studio_mode, "status": "stop_requested", "pid": _eval_pid, "rc": stop_rc})
		_eval_pid = -1
		_last_eval_exit_code = 130
		_refresh_agent_studio_ui()
		return

	var python_exec := _resolve_python_executable()
	var eval_script_abs := ProjectSettings.globalize_path("res://../scripts/agent/run_eval.py")
	if not FileAccess.file_exists(eval_script_abs):
		_append_runtime_event("AGENT_ACTION", {"action": "eval_run", "status": "failed", "reason": "script_missing", "path": eval_script_abs})
		return

	var args: Array[String] = _build_eval_suite_args(eval_script_abs)
	var pid := int(OS.create_process(python_exec, args, false))
	if pid <= 0:
		_append_runtime_event("AGENT_ACTION", {"action": "eval_run", "status": "start_failed", "python": python_exec})
		return

	_eval_pid = pid
	_eval_started_ms = Time.get_ticks_msec()
	_last_eval_exit_code = -1
	_append_runtime_event("AGENT_ACTION", {"action": "eval_run", "mode": _agent_studio_mode, "status": "started", "pid": _eval_pid, "suite": _agent_eval_suite})


func _build_eval_suite_args(eval_script_abs: String) -> Array[String]:
	var repo_root := ProjectSettings.globalize_path("res://..")
	var limit_text := str(maxi(1, eval_quick_limit))
	var args: Array[String] = [
		eval_script_abs,
		"--asgi",
		"--limit",
		limit_text,
		"--quiet",
	]

	match _agent_eval_suite:
		"rpg":
			args.append_array([
				"--profile",
				"unrestricted",
				"--checks",
				"must_include,keywords_any,keywords_at_least,not_include,regex",
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\rpg\\rpg_21_40_fantasy.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\rpg\\rpg_41_60_dialog.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\rpg\\rpg_61_80_szenen.v1.jsonl" % repo_root,
			])
		"quality_de":
			args.append_array([
				"--profile",
				"eval",
				"--tag",
				"quality_de",
				"--checks",
				"must_include,keywords_any,keywords_at_least,not_include,regex,quality_de",
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\quality_de_core.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\quality_de_drift.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\quality_de_canary.v1.jsonl" % repo_root,
			])
		_:
			args.append_array([
				"--profile",
				"eval",
				"--checks",
				"must_include,keywords_any,keywords_at_least,not_include,regex,rpg_style,quality_de",
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\neutral_01_20_core.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\neutral_81_100_tech.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\neutral_smoke.v1.jsonl" % repo_root,
			])

	return args


func _on_agent_datasets_pressed() -> void:
	if _dataset_pid > 0:
		if not _confirm_destructive_action("datasets_stop", "Datasets Stop: zweite Betaetigung zur Bestaetigung"):
			_refresh_agent_studio_ui()
			return
		var stop_rc := int(OS.kill(_dataset_pid))
		_append_runtime_event("AGENT_DATASETS", {"action": "stop_requested", "pid": _dataset_pid, "rc": stop_rc})
		_dataset_pid = -1
		_last_dataset_exit_code = 130
		_dataset_status_text = "Datasets: stop requested"
		_refresh_agent_studio_ui()
		return

	if _agent_studio_mode != "author":
		_agent_studio_mode = "author"
		_append_runtime_event("AGENT_ACTION", {"action": "datasets", "status": "switch_to_author"})
	_open_agent_form("datasets")


func _start_dataset_curation() -> void:
	var python_exec := _resolve_python_executable()
	var script_abs := ProjectSettings.globalize_path("res://../novapolis_agent/scripts/curate_dataset_from_latest.py")
	if not FileAccess.file_exists(script_abs):
		_dataset_status_text = "Datasets: script fehlt"
		_append_runtime_event("AGENT_DATASETS", {"action": "start_failed", "reason": "script_missing", "path": script_abs})
		return

	var args: Array[String] = [
		script_abs,
		"--format",
		"openai_chat",
		"--train-ratio",
		"0.9",
		"--min-output-chars",
		"20",
	]
	if _dataset_source_mode == "with_failures":
		args.append("--include-failures")

	var pid := int(OS.create_process(python_exec, args, false))
	if pid <= 0:
		_dataset_status_text = "Datasets: start fehlgeschlagen"
		_append_runtime_event("AGENT_DATASETS", {"action": "start_failed", "python": python_exec, "mode": _dataset_source_mode})
		return

	_dataset_pid = pid
	_dataset_started_ms = Time.get_ticks_msec()
	_last_dataset_exit_code = -1
	_dataset_status_text = "Datasets: running (%s)" % _dataset_source_mode
	_append_runtime_event("AGENT_DATASETS", {"action": "started", "pid": _dataset_pid, "mode": _dataset_source_mode})


func _refresh_dataset_runtime_state() -> void:
	if _dataset_pid <= 0:
		return
	if OS.is_process_running(_dataset_pid):
		return

	var exit_code := int(OS.get_process_exit_code(_dataset_pid))
	_last_dataset_exit_code = exit_code
	_append_runtime_event("AGENT_DATASETS", {"action": "finished", "pid": _dataset_pid, "exit_code": exit_code, "mode": _dataset_source_mode})
	_dataset_pid = -1
	if exit_code == 0:
		_dataset_status_text = "Datasets: done (%s)" % _dataset_source_mode
	else:
		_dataset_status_text = "Datasets: failed (exit=%d)" % exit_code


func _on_agent_synonyms_pressed() -> void:
	if _agent_studio_mode != "author":
		_agent_studio_mode = "author"
		_append_runtime_event("AGENT_ACTION", {"action": "synonyms", "status": "switch_to_author"})
	_open_agent_form("synonyms")


func _on_agent_finetune_pressed() -> void:
	if _finetune_pid > 0:
		if not _confirm_destructive_action("finetune_stop", "Finetune Stop: zweite Betaetigung zur Bestaetigung"):
			_refresh_agent_studio_ui()
			return
		var stop_rc := int(OS.kill(_finetune_pid))
		_append_runtime_event("AGENT_FINETUNE", {"action": "stop_requested", "pid": _finetune_pid, "rc": stop_rc})
		_finetune_pid = -1
		_last_finetune_exit_code = 130
		_finetune_status_text = "Finetune: stop requested"
		_refresh_agent_studio_ui()
		return

	if _agent_studio_mode != "author":
		_agent_studio_mode = "author"
		_append_runtime_event("AGENT_FINETUNE", {"action": "switch_to_author"})
	_open_agent_form("finetune")


func _on_agent_profiles_pressed() -> void:
	if _agent_studio_mode != "author":
		_agent_studio_mode = "author"
		_append_runtime_event("AGENT_ACTION", {"action": "profiles", "status": "switch_to_author"})
	_open_agent_form("profiles")


func _on_agent_ai_status_pressed() -> void:
	if _agent_studio_mode == "author":
		_open_agent_form("advanced")
		_append_runtime_event("AGENT_ACTION", {"action": "advanced_settings", "mode": _agent_studio_mode, "status": "form_opened"})
		return

	if _agent_action_busy:
		_append_runtime_event("AGENT_ACTION", {"action": "ai_status", "mode": _agent_studio_mode, "status": "busy"})
		return

	_agent_action_busy = true
	if enable_system_resource_monitoring:
		_refresh_system_metrics(true)
	_agent_summary_refresh_pending = true
	_agent_summary_refresh_due_ms = Time.get_ticks_msec() + 700
	_agent_action_busy = false
	_append_runtime_event("AGENT_ACTION", {"action": "ai_status", "mode": _agent_studio_mode, "status": "refreshed"})


func _run_agent_action_summary(action_name: String) -> void:
	if _agent_action_busy:
		_append_runtime_event("AGENT_ACTION", {"action": action_name, "status": "busy"})
		agent_latest_runs_label.text = "Aktion %s: bitte warten" % action_name
		return

	_agent_action_busy = true
	var python_exec := _resolve_python_executable()
	var actions_script_res := agent_actions_script_path
	if actions_script_res.strip_edges() == "":
		actions_script_res = "res://../novapolis_agent/scripts/agent_module_actions.py"
	var actions_script_abs := ProjectSettings.globalize_path(actions_script_res)
	if not FileAccess.file_exists(actions_script_abs):
		_append_runtime_event("AGENT_ACTION", {"action": action_name, "status": "script_missing", "path": actions_script_abs})
		agent_latest_runs_label.text = "Aktion %s: Script fehlt" % action_name
		_agent_action_busy = false
		return

	var output := []
	var exec_code := OS.execute(
		python_exec,
		[actions_script_abs, "--action", action_name],
		output,
		true,
	)
	if exec_code != 0 or output.is_empty():
		_append_runtime_event("AGENT_ACTION", {"action": action_name, "status": "failed", "exit_code": exec_code})
		agent_latest_runs_label.text = "Aktion %s: nicht verfügbar" % action_name
		_agent_action_busy = false
		return

	var raw := str(output[0]).strip_edges()
	if raw == "":
		_append_runtime_event("AGENT_ACTION", {"action": action_name, "status": "empty"})
		agent_latest_runs_label.text = "Aktion %s: keine Daten" % action_name
		_agent_action_busy = false
		return

	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		_append_runtime_event("AGENT_ACTION", {"action": action_name, "status": "parse_error"})
		agent_latest_runs_label.text = "Aktion %s: Antwort unlesbar" % action_name
		_agent_action_busy = false
		return

	var payload: Dictionary = parsed
	var title := str(payload.get("title", action_name.capitalize()))
	var lines_any = payload.get("lines", [])
	var lines: Array[String] = ["%s:" % title]
	if typeof(lines_any) == TYPE_ARRAY:
		for line_any in lines_any:
			lines.append("- %s" % str(line_any))

	agent_latest_runs_label.text = "\n".join(lines)
	_append_runtime_event("AGENT_ACTION", {"action": action_name, "status": "ok", "title": title})
	_agent_action_busy = false


func _refresh_agent_studio_ui() -> void:
	agent_studio_mode_label.text = "Modus: %s" % _agent_studio_mode.capitalize()
	var eval_text := "Eval: idle"
	if _eval_pid > 0:
		var elapsed_s := maxf(0.0, float(Time.get_ticks_msec() - _eval_started_ms) / 1000.0)
		var expected_s := maxf(1.0, eval_expected_duration_seconds)
		var progress := mini(95, int((elapsed_s / expected_s) * 100.0))
		eval_text = "Eval: running [%s] (%d%%, ~%.1fs)" % [_agent_eval_suite, progress, elapsed_s]
	elif _last_eval_exit_code == 0:
		eval_text = "Eval: done (100%)"
	elif _last_eval_exit_code > 0:
		eval_text = "Eval: failed (exit=%d)" % _last_eval_exit_code
	agent_eval_status_label.text = eval_text
	if enable_system_resource_monitoring:
		agent_system_metrics_label.text = "System: CPU %s | RAM %s | VRAM %s | Temp %s" % [
			_format_percent(_system_cpu_percent),
			_format_percent(_system_ram_percent),
			_format_vram(),
			_format_temperature(_effective_temperature_c()),
		]
	else:
		agent_system_metrics_label.text = "System: Monitoring deaktiviert (testweise)"
	var full_status_text := "• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n• %s\n• %s\n• %s" % [_dataset_status_text, _active_dataset_label(), _synonym_status_text, _active_synonym_label(), _profile_status_text, _active_profile_label(), _advanced_settings_status_text, _jobs_status_text, _finetune_status_text, _latest_eval_summary_text, _ai_trend_summary_text, _artifacts_summary_text, _experiments_summary_text, _policy_sandbox_summary_text, _release_gate_summary_text, _audit_trail_summary_text, _security_model_summary_text]
	var compact_status_text := "• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n• %s" % [_dataset_status_text, _active_dataset_label(), _jobs_status_text, _synonym_status_text, _latest_eval_summary_text, _release_gate_summary_text, _security_model_summary_text]
	_select_option_value(agent_eval_suite_button, _EVAL_SUITE_OPTIONS, _agent_eval_suite)
	_select_option_value(agent_dataset_source_button, _DATASET_SOURCE_OPTIONS, _dataset_source_mode)

	var hint_base_top := 362.0
	if _agent_submenu_open:
		hint_base_top = 430.0
	var form_should_show := _agent_submenu_open and _agent_studio_mode == "author" and (_agent_form_kind == "datasets" or _agent_form_kind == "synonyms" or _agent_form_kind == "finetune" or _agent_form_kind == "profiles" or _agent_form_kind == "advanced" or _agent_form_kind == "jobs")
	var collapse_status_block := form_should_show and collapse_agent_status_when_form_open
	agent_latest_runs_label.text = compact_status_text if collapse_status_block else full_status_text

	if collapse_status_block:
		agent_eval_status_label.visible = false
		agent_system_metrics_label.visible = false
		agent_latest_runs_label.modulate = _AGENT_STATUS_DIM_TINT
		agent_form_panel.self_modulate = _AGENT_FORM_PANEL_ACTIVE_TINT
		if _agent_submenu_open:
			agent_latest_runs_label.offset_top = 282.0
			agent_latest_runs_label.offset_bottom = 282.0
		else:
			agent_latest_runs_label.offset_top = 242.0
			agent_latest_runs_label.offset_bottom = 242.0
	else:
		agent_eval_status_label.visible = true
		agent_system_metrics_label.visible = true
		agent_latest_runs_label.modulate = _AGENT_STATUS_NORMAL_TINT
		agent_form_panel.self_modulate = _AGENT_FORM_PANEL_NORMAL_TINT
		if _agent_submenu_open:
			agent_latest_runs_label.offset_top = 356.0
			agent_latest_runs_label.offset_bottom = 356.0
		else:
			agent_latest_runs_label.offset_top = 316.0
			agent_latest_runs_label.offset_bottom = 316.0

	var latest_runs_lines: int = maxi(1, agent_latest_runs_label.get_line_count())
	var line_step := 22.0 if collapse_status_block else 24.0
	var hint_height := 26.0
	var hint_top := maxf(hint_base_top, agent_latest_runs_label.offset_top + (float(latest_runs_lines) * line_step) + 14.0)
	var hint_max_top := agent_studio_panel.offset_bottom - 30.0 - hint_height
	hint_top = minf(hint_top, hint_max_top)
	agent_studio_hint_label.visible = false
	agent_studio_hint_label.offset_top = hint_top
	agent_studio_hint_label.offset_bottom = hint_top + hint_height
	if form_should_show:
		var form_bottom := agent_studio_panel.offset_bottom - 22.0
		var min_form_height := 300.0
		var desired_top := hint_top + 28.0
		if desired_top + min_form_height > form_bottom:
			desired_top = maxf(96.0, form_bottom - min_form_height)
		agent_form_panel.offset_top = desired_top
		agent_form_panel.offset_bottom = form_bottom
		_layout_agent_form_controls()

	if _agent_studio_mode == "operate":
		if _eval_pid > 0:
			agent_eval_run_button.text = "Eval Stop"
		else:
			agent_eval_run_button.text = "Eval Start"
		if _dataset_pid > 0:
			agent_datasets_button.text = "Datasets Stop"
		else:
			agent_datasets_button.text = "Datasets Form [%s]" % _dataset_source_mode_label()
		if _finetune_pid > 0:
			agent_finetune_button.text = "Finetune Stop"
		else:
			agent_finetune_button.text = "Finetune Start"
		agent_profiles_button.text = "Profiles Form"
		agent_ai_status_button.text = "AI Status"
	else:
		agent_eval_run_button.text = "Jobs Config"
		if _dataset_pid > 0:
			agent_datasets_button.text = "Datasets Stop"
		else:
			agent_datasets_button.text = "Datasets Konfig [%s]" % _dataset_source_mode_label()
		if _finetune_pid > 0:
			agent_finetune_button.text = "Finetune Stop"
		else:
			agent_finetune_button.text = "Finetune Config"
		agent_profiles_button.text = "Profiles Config"
		agent_ai_status_button.text = "Advanced + Gate"

	if _destructive_armed_action != "" and Time.get_ticks_msec() <= _destructive_armed_until_ms:
		agent_studio_hint_label.visible = true
		agent_studio_hint_label.text = "Sicherheits-Gate aktiv: Aktion '%s' innerhalb 8s erneut bestaetigen" % _destructive_armed_action
	else:
		agent_studio_hint_label.text = ""

	agent_datasets_button.disabled = _agent_action_busy or not _agent_submenu_open
	agent_synonyms_button.disabled = _agent_action_busy or not _agent_submenu_open
	agent_finetune_button.disabled = _agent_action_busy or not _agent_submenu_open
	agent_profiles_button.disabled = _agent_action_busy or not _agent_submenu_open
	agent_ai_status_button.disabled = _agent_action_busy or not _agent_submenu_open
	agent_eval_suite_button.disabled = _eval_pid > 0 or not _agent_submenu_open
	agent_dataset_source_button.disabled = _dataset_pid > 0 or not _agent_submenu_open


func _dataset_source_mode_label() -> String:
	if _dataset_source_mode == "with_failures":
		return "Mit Fehlerfaellen"
	return "Nur erfolgreiche"


func _active_dataset_label() -> String:
	if _active_dataset_name == "":
		return "Active Dataset: n/a"
	if _active_dataset_tag == "":
		return "Active Dataset: %s" % _active_dataset_name
	return "Active Dataset: %s@%s" % [_active_dataset_name, _active_dataset_tag]


func _active_synonym_label() -> String:
	if _active_synonym_set == "":
		return "Active Synonyms: n/a"
	if _active_synonym_tag == "":
		return "Active Synonyms: %s" % _active_synonym_set
	return "Active Synonyms: %s@%s" % [_active_synonym_set, _active_synonym_tag]


func _active_profile_label() -> String:
	if _active_profile_name == "":
		return "Active Profile: n/a"
	if _active_profile_mode == "":
		return "Active Profile: %s" % _active_profile_name
	return "Active Profile: %s (%s)" % [_active_profile_name, _active_profile_mode]


func _load_dataset_registry_state() -> void:
	_active_dataset_name = ""
	_active_dataset_tag = ""
	if not FileAccess.file_exists(_DATASET_REGISTRY_PATH):
		return

	var f := FileAccess.open(_DATASET_REGISTRY_PATH, FileAccess.READ)
	if f == null:
		return
	var raw := f.get_as_text()
	f.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return

	var registry: Dictionary = parsed
	_active_dataset_name = str(registry.get("active_dataset", ""))
	_active_dataset_tag = str(registry.get("active_tag", ""))
	if _active_dataset_name != "":
		_dataset_status_text = "Datasets: active %s" % _active_dataset_label().replace("Active Dataset: ", "")


func _load_synonym_registry_state() -> void:
	_active_synonym_set = ""
	_active_synonym_tag = ""
	if not FileAccess.file_exists(_SYNONYM_REGISTRY_PATH):
		return

	var f := FileAccess.open(_SYNONYM_REGISTRY_PATH, FileAccess.READ)
	if f == null:
		return
	var raw := f.get_as_text()
	f.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return

	var registry: Dictionary = parsed
	_active_synonym_set = str(registry.get("active_set", ""))
	_active_synonym_tag = str(registry.get("active_tag", ""))
	if _active_synonym_set != "":
		_synonym_status_text = "Synonyms: active %s" % _active_synonym_label().replace("Active Synonyms: ", "")


func _load_profile_registry_state() -> void:
	_active_profile_name = ""
	_active_profile_mode = ""
	if not FileAccess.file_exists(_PROFILE_REGISTRY_PATH):
		return

	var f := FileAccess.open(_PROFILE_REGISTRY_PATH, FileAccess.READ)
	if f == null:
		return
	var raw := f.get_as_text()
	f.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return

	var registry: Dictionary = parsed
	_active_profile_name = str(registry.get("active_profile", ""))
	_active_profile_mode = str(registry.get("active_mode", ""))
	if _active_profile_name != "":
		_profile_status_text = "Profiles: active %s" % _active_profile_label().replace("Active Profile: ", "")


func _load_advanced_settings_state() -> void:
	_advanced_settings_status_text = "Advanced: idle"
	if not FileAccess.file_exists(_ADVANCED_SETTINGS_PATH):
		return

	var f := FileAccess.open(_ADVANCED_SETTINGS_PATH, FileAccess.READ)
	if f == null:
		return
	var raw := f.get_as_text()
	f.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return

	var payload: Dictionary = parsed
	var mode := str(payload.get("mode", "balanced"))
	var policy_profile := str(payload.get("policy_profile", "default"))
	var strictness_level := str(payload.get("strictness_level", "normal"))
	_advanced_settings_status_text = "Advanced: %s | policy=%s | strict=%s" % [mode, policy_profile, strictness_level]
	_policy_sandbox_summary_text = "Policy Sandbox: mode=%s | policy=%s | strict=%s" % [mode, policy_profile, strictness_level]


func _load_jobs_state() -> void:
	_jobs_status_text = "Jobs: idle"
	var queue_payload := _load_jobs_queue_payload()
	var jobs := _jobs_array_from_payload(queue_payload)
	_refresh_jobs_status_text(jobs)


func _load_security_model_state() -> void:
	if not FileAccess.file_exists(_SECURITY_MODEL_PATH):
		_persist_security_model_state()
		return
	var rf := FileAccess.open(_SECURITY_MODEL_PATH, FileAccess.READ)
	if rf == null:
		return
	var raw := rf.get_as_text()
	rf.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return
	var payload: Dictionary = parsed
	_destructive_guard_enabled = bool(payload.get("destructive_guard_enabled", true))
	_destructive_guard_window_ms = int(payload.get("destructive_guard_window_ms", 8000))
	_destructive_guard_token = str(payload.get("destructive_guard_token", "confirm"))
	_security_model_summary_text = "Security: destructive_guard=%s | token=%s" % [str(_destructive_guard_enabled), _destructive_guard_token]


func _persist_security_model_state() -> void:
	DirAccess.make_dir_recursive_absolute("user://agent_user_data/security")
	var payload: Dictionary = {
		"destructive_guard_enabled": _destructive_guard_enabled,
		"destructive_guard_window_ms": _destructive_guard_window_ms,
		"destructive_guard_token": _destructive_guard_token,
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	var wf := FileAccess.open(_SECURITY_MODEL_PATH, FileAccess.WRITE)
	if wf == null:
		return
	wf.store_string(JSON.stringify(payload, "  "))
	wf.close()


func _confirm_destructive_action(action_key: String, hint_text: String) -> bool:
	if not _destructive_guard_enabled:
		return true
	var now_ms := Time.get_ticks_msec()
	if _destructive_armed_action == action_key and now_ms <= _destructive_armed_until_ms:
		_destructive_armed_action = ""
		_destructive_armed_until_ms = -1
		return true
	_destructive_armed_action = action_key
	_destructive_armed_until_ms = now_ms + _destructive_guard_window_ms
	agent_form_status_label.text = hint_text
	_append_runtime_event("SECURITY_GUARD", {"action": action_key, "status": "armed", "valid_for_ms": _destructive_guard_window_ms})
	return false


func _refresh_agent_restpoint_summaries() -> void:
	_artifacts_summary_text = _build_artifacts_summary()
	_experiments_summary_text = _build_experiments_summary()
	_policy_sandbox_summary_text = _build_policy_sandbox_summary()
	_release_gate_summary_text = _build_release_gate_summary()
	_audit_trail_summary_text = _build_audit_trail_summary()
	_security_model_summary_text = "Security: destructive_guard=%s | token=%s" % [str(_destructive_guard_enabled), _destructive_guard_token]


func _build_artifacts_summary() -> String:
	var dataset_ref := _active_dataset_name
	if dataset_ref == "":
		dataset_ref = "n/a"
	elif _active_dataset_tag != "":
		dataset_ref = "%s@%s" % [_active_dataset_name, _active_dataset_tag]

	var synonym_ref := _active_synonym_set
	if synonym_ref == "":
		synonym_ref = "n/a"
	elif _active_synonym_tag != "":
		synonym_ref = "%s@%s" % [_active_synonym_set, _active_synonym_tag]

	var model_ref := _finetune_output_name
	if _last_finetune_exit_code != 0:
		model_ref = "n/a"

	var reports_ref := "tests=%s types=%s cov=%s" % [_quality_tests_last, _quality_types_last, _quality_coverage_last]
	return "Artifacts: dataset=%s | synonyms=%s | model=%s | %s" % [dataset_ref, synonym_ref, model_ref, reports_ref]


func _build_experiments_summary() -> String:
	if _latest_eval_runs.size() < 2:
		return "Experiments: n/a (mind. 2 Runs erforderlich)"
	var latest_any = _latest_eval_runs[0]
	var prev_any = _latest_eval_runs[1]
	if typeof(latest_any) != TYPE_DICTIONARY or typeof(prev_any) != TYPE_DICTIONARY:
		return "Experiments: n/a"
	var latest: Dictionary = latest_any
	var previous: Dictionary = prev_any
	var latest_pct := _to_float_or_default(latest.get("success_rate_percent", null), -1.0)
	var prev_pct := _to_float_or_default(previous.get("success_rate_percent", null), -1.0)
	if latest_pct < 0.0 or prev_pct < 0.0:
		return "Experiments: n/a"
	var delta := latest_pct - prev_pct
	var tag := "stable"
	if delta >= 2.0:
		tag = "A>B"
	elif delta <= -2.0:
		tag = "A<B"
	return "Experiments: A/B delta=%+.1fpp | tag=%s" % [delta, tag]


func _build_policy_sandbox_summary() -> String:
	var mode := "balanced"
	var policy := "default"
	var strict := "normal"
	if FileAccess.file_exists(_ADVANCED_SETTINGS_PATH):
		var rf := FileAccess.open(_ADVANCED_SETTINGS_PATH, FileAccess.READ)
		if rf != null:
			var parsed = JSON.parse_string(rf.get_as_text())
			rf.close()
			if typeof(parsed) == TYPE_DICTIONARY:
				var p: Dictionary = parsed
				mode = str(p.get("mode", mode))
				policy = str(p.get("policy_profile", policy))
				strict = str(p.get("strictness_level", strict))
	var quality_ok := (_quality_tests_last == "PASS") and (_quality_types_last == "PASS")
	var gate := "ready" if quality_ok else "hold"
	return "Policy Sandbox: mode=%s | policy=%s | strict=%s | gate=%s" % [mode, policy, strict, gate]


func _build_release_gate_summary() -> String:
	var coverage_value := _to_float_or_default(_quality_coverage_last.replace("%", ""), -1.0)
	var tests_ok := _quality_tests_last == "PASS"
	var types_ok := _quality_types_last == "PASS"
	var cov_ok := coverage_value >= 80.0
	var regression := _ai_trend_summary_text.find("regress=regression") >= 0
	var safety_ok := _destructive_guard_enabled
	var go := tests_ok and types_ok and cov_ok and (not regression) and safety_ok
	return "Release Gate: %s | tests=%s | types=%s | cov=%s | regression=%s | safety=%s" % ["GO" if go else "NO-GO", str(tests_ok), str(types_ok), str(cov_ok), str(regression), str(safety_ok)]


func _build_audit_trail_summary() -> String:
	var abs_path := ProjectSettings.globalize_path(_AUDIT_TRAIL_PATH)
	if not FileAccess.file_exists(abs_path):
		return "Audit Trail: entries=0"
	var rf := FileAccess.open(abs_path, FileAccess.READ)
	if rf == null:
		return "Audit Trail: unreadable"
	var count := 0
	var last_line := ""
	while not rf.eof_reached():
		var line := rf.get_line().strip_edges()
		if line == "":
			continue
		count += 1
		last_line = line
	rf.close()
	if count == 0:
		return "Audit Trail: entries=0"
	var tag := "n/a"
	var parsed = JSON.parse_string(last_line)
	if typeof(parsed) == TYPE_DICTIONARY:
		var p: Dictionary = parsed
		tag = str(p.get("tag", "n/a"))
	return "Audit Trail: entries=%d | last=%s" % [count, tag]


func _update_dataset_registry(dataset_name: String, dataset_tag: String, set_active: bool) -> void:
	var registry: Dictionary = {}
	if FileAccess.file_exists(_DATASET_REGISTRY_PATH):
		var rf := FileAccess.open(_DATASET_REGISTRY_PATH, FileAccess.READ)
		if rf != null:
			var raw := rf.get_as_text()
			rf.close()
			var parsed = JSON.parse_string(raw)
			if typeof(parsed) == TYPE_DICTIONARY:
				registry = parsed

	var datasets_any = registry.get("datasets", {})
	if typeof(datasets_any) != TYPE_DICTIONARY:
		datasets_any = {}
	var datasets: Dictionary = datasets_any
	datasets[dataset_name] = {
		"tag": dataset_tag,
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	registry["datasets"] = datasets

	if set_active or str(registry.get("active_dataset", "")) == "":
		registry["active_dataset"] = dataset_name
		registry["active_tag"] = dataset_tag
		_active_dataset_name = dataset_name
		_active_dataset_tag = dataset_tag

	DirAccess.make_dir_recursive_absolute("user://agent_user_data/datasets")
	var wf := FileAccess.open(_DATASET_REGISTRY_PATH, FileAccess.WRITE)
	if wf == null:
		return
	wf.store_string(JSON.stringify(registry, "  "))
	wf.close()
	if _active_dataset_name != "":
		_dataset_status_text = "Datasets: active %s" % _active_dataset_label().replace("Active Dataset: ", "")


func _update_synonym_registry(synonym_set: String, synonym_tag: String, set_active: bool) -> void:
	var registry: Dictionary = {}
	if FileAccess.file_exists(_SYNONYM_REGISTRY_PATH):
		var rf := FileAccess.open(_SYNONYM_REGISTRY_PATH, FileAccess.READ)
		if rf != null:
			var raw := rf.get_as_text()
			rf.close()
			var parsed = JSON.parse_string(raw)
			if typeof(parsed) == TYPE_DICTIONARY:
				registry = parsed

	var sets_any = registry.get("sets", {})
	if typeof(sets_any) != TYPE_DICTIONARY:
		sets_any = {}
	var sets: Dictionary = sets_any
	sets[synonym_set] = {
		"tag": synonym_tag,
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	registry["sets"] = sets

	if set_active or str(registry.get("active_set", "")) == "":
		registry["active_set"] = synonym_set
		registry["active_tag"] = synonym_tag
		_active_synonym_set = synonym_set
		_active_synonym_tag = synonym_tag

	DirAccess.make_dir_recursive_absolute("user://agent_user_data/synonyms")
	var wf := FileAccess.open(_SYNONYM_REGISTRY_PATH, FileAccess.WRITE)
	if wf == null:
		return
	wf.store_string(JSON.stringify(registry, "  "))
	wf.close()
	if _active_synonym_set != "":
		_synonym_status_text = "Synonyms: active %s" % _active_synonym_label().replace("Active Synonyms: ", "")


func _update_profile_registry(profile_name: String, mode: String, set_active: bool, archive: bool) -> void:
	var registry: Dictionary = {}
	if FileAccess.file_exists(_PROFILE_REGISTRY_PATH):
		var rf := FileAccess.open(_PROFILE_REGISTRY_PATH, FileAccess.READ)
		if rf != null:
			var raw := rf.get_as_text()
			rf.close()
			var parsed = JSON.parse_string(raw)
			if typeof(parsed) == TYPE_DICTIONARY:
				registry = parsed

	var profiles_any = registry.get("profiles", {})
	if typeof(profiles_any) != TYPE_DICTIONARY:
		profiles_any = {}
	var profiles: Dictionary = profiles_any
	profiles[profile_name] = {
		"mode": mode,
		"archive": archive,
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	registry["profiles"] = profiles

	if archive:
		if str(registry.get("active_profile", "")) == profile_name:
			registry["active_profile"] = ""
			registry["active_mode"] = ""
			_active_profile_name = ""
			_active_profile_mode = ""
		_profile_status_text = "Profiles: archived %s" % profile_name
	else:
		if set_active or str(registry.get("active_profile", "")) == "":
			registry["active_profile"] = profile_name
			registry["active_mode"] = mode
			_active_profile_name = profile_name
			_active_profile_mode = mode
		if _active_profile_name != "":
			_profile_status_text = "Profiles: active %s" % _active_profile_label().replace("Active Profile: ", "")

	DirAccess.make_dir_recursive_absolute("user://agent_user_data/profiles")
	var wf := FileAccess.open(_PROFILE_REGISTRY_PATH, FileAccess.WRITE)
	if wf == null:
		return
	wf.store_string(JSON.stringify(registry, "  "))
	wf.close()


func _resolve_finetune_train_file() -> String:
	if _active_dataset_name != "":
		var user_dataset := "user://agent_user_data/datasets/%s.jsonl" % _active_dataset_name
		var user_dataset_abs := ProjectSettings.globalize_path(user_dataset)
		if FileAccess.file_exists(user_dataset_abs):
			return user_dataset_abs

	var fallback_res := "res://../novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl"
	var fallback_abs := ProjectSettings.globalize_path(fallback_res)
	if FileAccess.file_exists(fallback_abs):
		return fallback_abs

	return ""


func _start_finetune_run(options: Dictionary) -> bool:
	var python_exec := _resolve_python_executable()
	var script_abs := ProjectSettings.globalize_path("res://../scripts/agent/fine_tune_pipeline.py")
	if not FileAccess.file_exists(script_abs):
		_append_runtime_event("AGENT_FINETUNE", {"action": "start_failed", "reason": "script_missing", "path": script_abs})
		_finetune_status_text = "Finetune: script fehlt"
		return false

	var output_name := _sanitize_agent_form_name(str(options.get("output_name", "lora-agent-hub")))
	if output_name == "":
		output_name = "lora-agent-hub"
	var output_abs := ProjectSettings.globalize_path("res://../outputs/%s" % output_name)

	var args: Array[String] = [
		script_abs,
		"--train-file",
		str(options.get("train_file", "")),
		"--model",
		str(options.get("base_model", "sshleifer/tiny-gpt2")),
		"--output",
		output_abs,
		"--per-device-train-batch-size",
		str(int(options.get("batch_size", 1))),
		"--epochs",
		str(int(options.get("epochs", 1))),
		"--max-steps",
		str(int(options.get("max_steps", 10))),
		"--lr",
		str(float(options.get("lr", 0.0002))),
	]
	if bool(options.get("no_check", true)):
		args.append("--no-check")

	var pid := int(OS.create_process(python_exec, args, false))
	if pid <= 0:
		_append_runtime_event("AGENT_FINETUNE", {"action": "start_failed", "python": python_exec})
		_finetune_status_text = "Finetune: start fehlgeschlagen"
		return false

	_finetune_pid = pid
	_finetune_started_ms = Time.get_ticks_msec()
	_last_finetune_exit_code = -1
	_finetune_profile = str(options.get("profile", "baseline"))
	_finetune_base_model = str(options.get("base_model", "sshleifer/tiny-gpt2"))
	_finetune_output_name = output_name
	_finetune_epochs = int(options.get("epochs", 1))
	_finetune_max_steps = int(options.get("max_steps", 10))
	_finetune_batch_size = int(options.get("batch_size", 1))
	_finetune_lr = _to_float_or_default(options.get("lr", 0.0002), 0.0002)
	_finetune_status_text = "Finetune: running (%s, e=%d, s=%d, b=%d, lr=%.5f)" % [_finetune_profile, _finetune_epochs, _finetune_max_steps, _finetune_batch_size, _finetune_lr]
	_append_runtime_event("AGENT_FINETUNE", {
		"action": "started",
		"pid": _finetune_pid,
		"profile": _finetune_profile,
		"model": _finetune_base_model,
		"output": output_abs,
	})
	return true


func _refresh_finetune_runtime_state() -> void:
	if _finetune_pid <= 0:
		return

	if OS.is_process_running(_finetune_pid):
		var elapsed_s := maxf(0.0, float(Time.get_ticks_msec() - _finetune_started_ms) / 1000.0)
		_finetune_status_text = "Finetune: running (%s, %.1fs, e=%d, s=%d, b=%d, lr=%.5f)" % [_finetune_profile, elapsed_s, _finetune_epochs, _finetune_max_steps, _finetune_batch_size, _finetune_lr]
		return

	var exit_code := int(OS.get_process_exit_code(_finetune_pid))
	_last_finetune_exit_code = exit_code
	_append_runtime_event("AGENT_FINETUNE", {
		"action": "finished",
		"pid": _finetune_pid,
		"exit_code": exit_code,
		"profile": _finetune_profile,
		"model": _finetune_base_model,
	})
	_finetune_pid = -1
	var total_runtime_s := maxf(0.0, float(Time.get_ticks_msec() - _finetune_started_ms) / 1000.0)
	if exit_code == 0:
		_finetune_status_text = "Finetune: done (%s, %.1fs, e=%d, s=%d, b=%d, lr=%.5f)" % [_finetune_output_name, total_runtime_s, _finetune_epochs, _finetune_max_steps, _finetune_batch_size, _finetune_lr]
		_agent_summary_refresh_pending = true
		_agent_summary_refresh_due_ms = Time.get_ticks_msec() + 400
	else:
		_finetune_status_text = "Finetune: failed (exit=%d, %.1fs, e=%d, s=%d)" % [exit_code, total_runtime_s, _finetune_epochs, _finetune_max_steps]


func _refresh_eval_runtime_state() -> void:
	if _eval_pid <= 0:
		return
	if OS.is_process_running(_eval_pid):
		return

	var exit_code := int(OS.get_process_exit_code(_eval_pid))
	_last_eval_exit_code = exit_code
	_append_runtime_event("AGENT_ACTION", {"action": "eval_run", "status": "finished", "pid": _eval_pid, "exit_code": exit_code})
	_eval_pid = -1
	_refresh_latest_eval_summary(true)


func _refresh_latest_eval_summary(force: bool) -> void:
	if not _agent_submenu_open and not force:
		return

	var now_ms := Time.get_ticks_msec()
	if not force and _last_eval_summary_refresh_ms >= 0:
		var delta_s := float(now_ms - _last_eval_summary_refresh_ms) / 1000.0
		if delta_s < maxf(2.0, eval_summary_refresh_interval_seconds):
			return
	_last_eval_summary_refresh_ms = now_ms

	var python_exec := _resolve_python_executable()
	var summary_script_abs := ProjectSettings.globalize_path(eval_summary_script_path)
	if not FileAccess.file_exists(summary_script_abs):
		_latest_eval_summary_text = "Letzte Eval-Runs: Script fehlt"
		return

	var output := []
	var exec_code := OS.execute(
		python_exec,
		[summary_script_abs, "--count", "3"],
		output,
		true,
	)
	if exec_code != 0 or output.is_empty():
		_latest_eval_summary_text = "Letzte Eval-Runs: nicht verfügbar"
		return

	var raw := str(output[0]).strip_edges()
	if raw == "":
		_latest_eval_summary_text = "Letzte Eval-Runs: keine Daten"
		return

	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		_latest_eval_summary_text = "Letzte Eval-Runs: Antwort unlesbar"
		return

	var payload: Dictionary = parsed
	var runs_any = payload.get("runs", [])
	if typeof(runs_any) != TYPE_ARRAY:
		_latest_eval_summary_text = "Letzte Eval-Runs: keine Daten"
		return

	var runs: Array = runs_any
	if runs.is_empty():
		_latest_eval_summary_text = "Letzte Eval-Runs: keine Runs gefunden"
		_latest_eval_runs = []
		_ai_trend_summary_text = "Trendkarte: keine Daten"
		return

	var lines: Array[String] = ["Letzte Eval-Runs (Success Rate):"]
	var pcts: Array[float] = []
	var avg_duration_values: Array[float] = []
	for run_any in runs:
		if typeof(run_any) != TYPE_DICTIONARY:
			continue
		var run: Dictionary = run_any
		var stamp := str(run.get("timestamp", "n/a"))
		var pct := _to_float_or_default(run.get("success_rate_percent", null), -1.0)
		var ok_count := int(run.get("success", 0))
		var total_count := int(run.get("items", 0))
		var avg_ms := _to_float_or_default(run.get("avg_duration_ms", null), -1.0)
		lines.append("- %s: %.1f%% (%d/%d), avg %.0fms" % [stamp, pct, ok_count, total_count, maxf(0.0, avg_ms)])
		if pct >= 0.0:
			pcts.append(pct)
		if avg_ms >= 0.0:
			avg_duration_values.append(avg_ms)

	_latest_eval_runs = runs

	var trend_line := _build_ai_trend_summary(pcts, avg_duration_values)
	lines.append(trend_line)
	_ai_trend_summary_text = trend_line

	_latest_eval_summary_text = "\n".join(lines)


func _build_ai_trend_summary(pcts: Array[float], avg_duration_values: Array[float]) -> String:
	if pcts.is_empty():
		return "Trendkarte: n/a"
	var newest := pcts[0]
	var oldest := pcts[pcts.size() - 1]
	var delta := newest - oldest
	var min_pct := pcts[0]
	var max_pct := pcts[0]
	var sum_pct := 0.0
	for value in pcts:
		sum_pct += value
		min_pct = minf(min_pct, value)
		max_pct = maxf(max_pct, value)
	var avg_pct := sum_pct / float(pcts.size())

	var regression_status := "stabil"
	if delta <= -3.0:
		regression_status = "regression"
	elif delta >= 3.0:
		regression_status = "verbessert"

	var drift_status := "stable"
	if (max_pct - min_pct) >= 12.0:
		drift_status = "watch"

	var avg_ms_text := "n/a"
	if not avg_duration_values.is_empty():
		var sum_ms := 0.0
		for ms in avg_duration_values:
			sum_ms += ms
		avg_ms_text = "%.0f" % (sum_ms / float(avg_duration_values.size()))

	return "Trendkarte: pass=%.1f%% (delta=%+.1f) | regress=%s | drift=%s | avg_ms=%s" % [avg_pct, delta, regression_status, drift_status, avg_ms_text]


func _refresh_system_metrics(force: bool) -> void:
	if not enable_system_resource_monitoring:
		_system_cpu_percent = -1.0
		_system_ram_percent = -1.0
		_system_gpu_vram_percent = -1.0
		_system_gpu_vram_used_mb = -1.0
		_system_gpu_vram_total_mb = -1.0
		_system_cpu_temp_c = -999.0
		_system_gpu_temp_c = -999.0
		return

	var now_ms := Time.get_ticks_msec()
	if not force and _last_metrics_refresh_ms >= 0:
		var delta_s := float(now_ms - _last_metrics_refresh_ms) / 1000.0
		if delta_s < maxf(1.0, metrics_refresh_interval_seconds):
			return
	_last_metrics_refresh_ms = now_ms

	var python_exec := _resolve_python_executable()
	var metrics_script_abs := ProjectSettings.globalize_path(system_snapshot_script_path)
	if not FileAccess.file_exists(metrics_script_abs):
		return

	var output := []
	var exec_code := OS.execute(python_exec, [metrics_script_abs], output, true)
	if exec_code != 0:
		return
	if output.is_empty():
		return

	var raw := str(output[0]).strip_edges()
	if raw == "":
		return
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return

	var payload: Dictionary = parsed
	_system_cpu_percent = _to_float_or_default(payload.get("cpu_percent", null), -1.0)
	_system_ram_percent = _to_float_or_default(payload.get("ram_percent", null), -1.0)
	_system_gpu_vram_percent = _to_float_or_default(payload.get("gpu_vram_percent", null), -1.0)
	_system_gpu_vram_used_mb = _to_float_or_default(payload.get("gpu_vram_used_mb", null), -1.0)
	_system_gpu_vram_total_mb = _to_float_or_default(payload.get("gpu_vram_total_mb", null), -1.0)
	_system_cpu_temp_c = _to_float_or_default(payload.get("cpu_temp_c", null), -999.0)
	_system_gpu_temp_c = _to_float_or_default(payload.get("gpu_temp_c", null), -999.0)


func _format_percent(value: float) -> String:
	if value < 0.0:
		return "n/a"
	return "%.1f%%" % value


func _format_temperature(value_c: float) -> String:
	if value_c < -100.0:
		return "n/a"
	return "%.1fC" % value_c


func _format_vram() -> String:
	if _system_gpu_vram_percent < 0.0:
		return "n/a"
	if _system_gpu_vram_used_mb >= 0.0 and _system_gpu_vram_total_mb > 0.0:
		var used_gb := _system_gpu_vram_used_mb / 1024.0
		var total_gb := _system_gpu_vram_total_mb / 1024.0
		return "%.1f%% (%.1f/%.1fGB)" % [_system_gpu_vram_percent, used_gb, total_gb]
	return "%.1f%%" % _system_gpu_vram_percent


func _effective_temperature_c() -> float:
	if _system_gpu_temp_c > -100.0:
		return _system_gpu_temp_c
	return _system_cpu_temp_c


func _to_float_or_default(value, default_value: float) -> float:
	if value is float:
		return value
	if value is int:
		return float(value)
	if value is String and value.is_valid_float():
		return value.to_float()
	return default_value


func _start_local_server() -> void:
	var python_exec := _resolve_python_executable()
	var script_abs := ProjectSettings.globalize_path(server_script_path)
	if not FileAccess.file_exists(script_abs):
		_server_status_text = "script missing"
		_append_runtime_event("SERVER_START_FAILED", {"reason": "script_missing", "path": script_abs})
		return

	var args: Array[String] = [script_abs]
	var pid := int(OS.create_process(python_exec, args, false))
	if pid <= 0:
		_server_status_text = "start failed"
		_append_runtime_event("SERVER_START_FAILED", {"python": python_exec, "script": script_abs})
		return

	_server_pid = pid
	_server_exit_reported = false
	_server_status_text = "running (pid=%d)" % _server_pid
	_append_runtime_event("SERVER_STARTED", {"pid": _server_pid, "python": python_exec})


func _stop_local_server() -> void:
	if _server_pid <= 0:
		_server_status_text = "stopped"
		return

	var kill_rc := int(OS.kill(_server_pid))
	if kill_rc == OK:
		_append_runtime_event("SERVER_STOPPED", {"pid": _server_pid})
		_server_pid = -1
		_server_status_text = "stopped"
		_server_exit_reported = false
		return

	_server_status_text = "stop failed (rc=%d)" % kill_rc
	_append_runtime_event("SERVER_STOP_FAILED", {"pid": _server_pid, "rc": kill_rc})


func _update_server_control_ui() -> void:
	var health := _derive_health_state(_sim_runtime_status())
	var state := str(health.get("state", "offline"))
	var _reason := str(health.get("reason", "n/a"))

	if _server_pid > 0:
		server_toggle_button.text = "Stop Server"
	else:
		if state == "external":
			server_toggle_button.text = "Start Local Server"
		elif state == "offline":
			server_toggle_button.text = "Start Server"
		elif state == "degraded":
			server_toggle_button.text = "Start Server"
		else:
			server_toggle_button.text = "Start Server"
	server_status_label.text = "Server: %s" % state


func _resolve_python_executable() -> String:
	var preferred_res := server_python_path
	if preferred_res.strip_edges() == "":
		preferred_res = "res://../.venv/Scripts/python.exe"
	var preferred := ProjectSettings.globalize_path(preferred_res)
	if FileAccess.file_exists(preferred):
		return preferred
	var local_venv := ProjectSettings.globalize_path("res://../.venv/Scripts/python.exe")
	if FileAccess.file_exists(local_venv):
		return local_venv
	return "python"


func _refresh_server_runtime_state() -> void:
	if _server_pid <= 0:
		return
	if OS.is_process_running(_server_pid):
		return
	if _server_exit_reported:
		return

	_append_runtime_event("SERVER_EXITED", {"pid": _server_pid})
	_server_pid = -1
	_server_status_text = "exited"
	_server_exit_reported = true
	_update_server_control_ui()


func _is_external_server_reachable() -> bool:
	if _last_status_message != "":
		return false
	if _last_success_ms < 0:
		return false
	if _server_pid > 0:
		return false

	var runtime_status := _sim_runtime_status()
	var step_interval := float(runtime_status.get("step_interval", 0.5))
	var max_age_s := maxf(1.2, step_interval * 3.0)
	var age_s := maxf(0.0, float(Time.get_ticks_msec() - _last_success_ms) / 1000.0)
	return age_s <= max_age_s


func _append_runtime_event(tag: String, payload: Dictionary) -> void:
	var line := "- %s %s" % [tag, JSON.stringify(payload)]
	_runtime_events.append(line)
	_runtime_event_timestamps_ms.append(Time.get_ticks_msec())
	_append_audit_event(tag, payload)
	_trim_runtime_event_rate_window()
	if _runtime_events.size() > _MAX_RUNTIME_EVENTS:
		_runtime_events = _runtime_events.slice(_runtime_events.size() - _MAX_RUNTIME_EVENTS, _runtime_events.size())
	_render_pc_centric_view()


func _append_audit_event(tag: String, payload: Dictionary) -> void:
	DirAccess.make_dir_recursive_absolute("user://agent_user_data/audit")
	var wf := FileAccess.open(_AUDIT_TRAIL_PATH, FileAccess.READ_WRITE)
	if wf == null:
		wf = FileAccess.open(_AUDIT_TRAIL_PATH, FileAccess.WRITE)
	if wf == null:
		return
	wf.seek_end()
	var entry := {
		"ts": Time.get_datetime_string_from_system(false, true),
		"tag": tag,
		"payload": payload,
	}
	wf.store_string(JSON.stringify(entry, "") + "\n")
	wf.close()


func _runtime_event_rate_per_second() -> float:
	_trim_runtime_event_rate_window()
	if _runtime_event_timestamps_ms.is_empty():
		return 0.0
	return float(_runtime_event_timestamps_ms.size()) / _EVENT_RATE_WINDOW_SECONDS


func _trim_runtime_event_rate_window() -> void:
	if _runtime_event_timestamps_ms.is_empty():
		return
	var now_ms := Time.get_ticks_msec()
	var min_ms := int(_EVENT_RATE_WINDOW_SECONDS * 1000.0)
	while not _runtime_event_timestamps_ms.is_empty() and now_ms - _runtime_event_timestamps_ms[0] > min_ms:
		_runtime_event_timestamps_ms.remove_at(0)


func _extract_error_code(message: String) -> String:
	if message == "":
		return "none"
	var marker := "code="
	var idx := message.find(marker)
	if idx < 0:
		return "n/a"
	var start := idx + marker.length()
	var end := start
	while end < message.length():
		var ch := message[end]
		if ch == '|' or ch == ' ' or ch == ')' or ch == ',':
			break
		end += 1
	var value := message.substr(start, end - start).strip_edges()
	if value == "":
		return "n/a"
	return value


func _on_action_start_event(action_name: String, context: Dictionary) -> void:
	if action_name == "state_update":
		return
	_append_runtime_event("START:%s" % action_name, context)


func _on_action_end_event(action_name: String, context: Dictionary) -> void:
	if action_name == "state_update":
		return
	_append_runtime_event("END:%s" % action_name, context)


func _on_visibility_change_event(visible_state: bool, reason: String) -> void:
	_append_runtime_event("VISIBILITY", {"is_visible": visible_state, "reason": reason})


func _on_interrupt_event(reason: String, context: Dictionary) -> void:
	_append_runtime_event("INTERRUPT:%s" % reason, context)
