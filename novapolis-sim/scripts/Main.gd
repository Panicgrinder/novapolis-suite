extends Node2D

const AgentAuthoringPayloadControllerRef = preload("res://scripts/agent_authoring_payload_controller.gd")
const AgentAuthoringPersistenceControllerRef = preload("res://scripts/agent_authoring_persistence_controller.gd")
const AgentRegistryStateControllerRef = preload("res://scripts/agent_registry_state_controller.gd")
const AgentRestpointSummaryControllerRef = preload("res://scripts/agent_restpoint_summary_controller.gd")
const AgentStudioControllerRef = preload("res://scripts/agent_studio_controller.gd")
const AgentFormControllerRef = preload("res://scripts/agent_form_controller.gd")
const AgentRuntimeControllerRef = preload("res://scripts/agent_runtime_controller.gd")
const HubServerOpsControllerRef = preload("res://scripts/hub_server_ops_controller.gd")
const ChecksRpControllerRef = preload("res://scripts/checks_rp_controller.gd")
const RuntimeTelemetryControllerRef = preload("res://scripts/runtime_telemetry_controller.gd")
const RuntimeAuditControllerRef = preload("res://scripts/runtime_audit_controller.gd")
const SchedulerHookRef = preload("res://scripts/scheduler_hook.gd")
const HubChatControllerRef = preload("res://scripts/hub_chat_controller.gd")
const HubConfigControllerRef = preload("res://scripts/hub_config_controller.gd")
const HubLayoutControllerRef = preload("res://scripts/hub_layout_controller.gd")
const HubPreferencesStoreRef = preload("res://scripts/hub_preferences_store.gd")
const SessionReplayHelpersRef = preload("res://scripts/session_replay_helpers.gd")
const SessionReplayRequestControllerRef = preload("res://scripts/session_replay_request_controller.gd")
const SessionReplayStateControllerRef = preload("res://scripts/session_replay_state_controller.gd")

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
@onready var hub_top_band_panel: Panel = $HubTopBandPanel
@onready var hub_stage_panel: Panel = $HubStagePanel
@onready var hub_ops_panel: Panel = $HubOpsPanel
@onready var hub_telemetry_panel: Panel = $HubTelemetryPanel
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
@onready var hub_config_title_label: Label = $HubConfigPanel/HubConfigTitleLabel
@onready var hub_config_close_button: Button = $HubConfigPanel/HubConfigCloseButton
@onready var hub_config_quit_button: Button = $HubConfigPanel/HubConfigQuitButton
@onready var hub_config_save_button: Button = $HubConfigPanel/HubConfigSaveButton
@onready var hub_config_sim_card_button: Button = $HubConfigPanel/HubConfigSimCardButton
@onready var hub_config_api_card_button: Button = $HubConfigPanel/HubConfigApiCardButton
@onready var hub_config_eval_card_button: Button = $HubConfigPanel/HubConfigEvalCardButton
@onready var hub_config_default_panel_button: OptionButton = $HubConfigPanel/HubConfigDefaultPanelButton
@onready var hub_config_refresh_button: OptionButton = $HubConfigPanel/HubConfigRefreshButton
@onready var hub_config_status_label: Label = $HubConfigPanel/HubConfigStatusLabel
@onready var hub_replay_panel: Panel = $HubReplayPanel
@onready var hub_replay_summary_label: Label = $HubReplayPanel/HubReplaySummaryLabel
@onready var hub_replay_checkpoint_button: OptionButton = $HubReplayPanel/HubReplayCheckpointButton
@onready var hub_replay_fetch_button: Button = $HubReplayPanel/HubReplayFetchButton
@onready var hub_replay_apply_button: Button = $HubReplayPanel/HubReplayApplyButton
@onready var hub_replay_status_label: Label = $HubReplayPanel/HubReplayStatusLabel
@onready var hub_replay_title_label: Label = $HubReplayPanel/HubReplayTitleLabel
@onready var hub_replay_checkpoint_label: Label = $HubReplayPanel/HubReplayCheckpointLabel
@onready var hub_chat_panel: Panel = $HubChatPanel
@onready var hub_chat_title_label: Label = $HubChatPanel/HubChatTitleLabel
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
var _hub_replay_request: HTTPRequest
var _live_session_artifact_paths: Dictionary = {}
var _live_session_resume_checkpoint_id: String = ""
var _live_replay_manifest: Dictionary = {}
var _hub_selected_replay_checkpoint_id: String = ""
var _marquee_state: Dictionary = {}
var _lower_shared_topic: String = "agent_api"
var _agent_authoring_payload_controller = AgentAuthoringPayloadControllerRef.new()
var _agent_authoring_persistence_controller = AgentAuthoringPersistenceControllerRef.new()
var _agent_registry_state_controller = AgentRegistryStateControllerRef.new()
var _agent_restpoint_summary_controller = AgentRestpointSummaryControllerRef.new()
var _agent_studio_controller = AgentStudioControllerRef.new()
var _agent_form_controller = AgentFormControllerRef.new()
var _agent_runtime_controller = AgentRuntimeControllerRef.new()
var _hub_server_ops_controller = HubServerOpsControllerRef.new()
var _checks_rp_controller = ChecksRpControllerRef.new()
var _runtime_telemetry_controller = RuntimeTelemetryControllerRef.new()
var _runtime_audit_controller = RuntimeAuditControllerRef.new()
var _hub_chat_controller = HubChatControllerRef.new()
var _hub_config_controller = HubConfigControllerRef.new()
var _hub_layout_controller = HubLayoutControllerRef.new()
var _hub_preferences_store = HubPreferencesStoreRef.new()
var _session_replay_helpers = SessionReplayHelpersRef.new()
var _session_replay_request_controller = SessionReplayRequestControllerRef.new(_session_replay_helpers)
var _session_replay_state_controller = SessionReplayStateControllerRef.new(_session_replay_helpers)
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
@export var preserve_editor_hub_layout: bool = false

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
	hub_replay_fetch_button.pressed.connect(_on_hub_replay_fetch_pressed)
	hub_replay_apply_button.pressed.connect(_on_hub_replay_apply_pressed)
	hub_replay_checkpoint_button.item_selected.connect(_on_hub_replay_checkpoint_selected)
	hub_chat_send_button.pressed.connect(_on_hub_chat_send_pressed)
	hub_chat_input_edit.text_submitted.connect(_on_hub_chat_input_submitted)
	hub_chat_request.request_completed.connect(_on_hub_chat_request_completed)
	_hub_session_request = HTTPRequest.new()
	_hub_session_request.timeout = 4.0
	add_child(_hub_session_request)
	_hub_session_request.request_completed.connect(_on_hub_session_request_completed)
	_hub_replay_request = HTTPRequest.new()
	_hub_replay_request.timeout = 4.0
	add_child(_hub_replay_request)
	_hub_replay_request.request_completed.connect(_on_hub_replay_request_completed)
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
	if _hub_chat_scene_id == "":
		_hub_chat_scene_id = "hub_boot"
	var restored_live_session := _hub_chat_session_id.strip_edges() != ""
	if not restored_live_session:
		_hub_chat_session_id = _generate_hub_session_id()
		_persist_hub_session_state()
	_hub_chat_public_context = _build_hub_chat_public_context()
	_refresh_hub_chat_ui()
	_refresh_hub_replay_ui()
	hub_chat_status_label.text = "Live-Spielclient: Fortsetzung wird synchronisiert" if restored_live_session else "Live-Spielclient: bereit"
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
	if restored_live_session:
		_request_live_session_state()
		_request_live_session_replay()


func _on_viewport_size_changed() -> void:
	_apply_responsive_layout()


func _get_safe_viewport_size() -> Vector2:
	return _hub_layout_controller.get_safe_viewport_size(get_viewport_rect().size, _UI_MIN_WIDTH, _UI_MIN_HEIGHT)


func _apply_responsive_layout() -> void:
	var size := _get_safe_viewport_size()
	var width := size.x
	var height := size.y
	_hub_layout_controller.apply_responsive_hub_layout(_hub_layout_controls(), _hub_layout_state(), width, height)
	_layout_module_panels(width, height)


func _hub_layout_controls() -> Dictionary:
	return {
		"hub_top_band_panel": hub_top_band_panel,
		"hub_stage_panel": hub_stage_panel,
		"hub_ops_panel": hub_ops_panel,
		"hub_telemetry_panel": hub_telemetry_panel,
		"hub_title_label": hub_title_label,
		"hub_api_label": hub_api_label,
		"hub_polling_label": hub_polling_label,
		"hub_queue_label": hub_queue_label,
		"hub_errors_label": hub_errors_label,
		"tick_label": tick_label,
		"time_label": time_label,
		"status_label": status_label,
		"slot_label": slot_label,
		"audio_status_label": audio_status_label,
		"epoch_label": epoch_label,
		"epoch_status_label": epoch_status_label,
		"play_pc_button": play_pc_button,
		"play_world_button": play_world_button,
		"hub_checks_button": hub_checks_button,
		"hub_reload_button": hub_reload_button,
		"server_toggle_button": server_toggle_button,
		"server_status_label": server_status_label,
		"hub_config_panel": hub_config_panel,
		"hub_config_title_label": hub_config_title_label,
		"hub_config_quit_button": hub_config_quit_button,
		"hub_config_close_button": hub_config_close_button,
		"hub_config_sim_card_button": hub_config_sim_card_button,
		"hub_config_api_card_button": hub_config_api_card_button,
		"hub_config_eval_card_button": hub_config_eval_card_button,
		"hub_config_default_panel_button": hub_config_default_panel_button,
		"hub_config_refresh_button": hub_config_refresh_button,
		"hub_config_save_button": hub_config_save_button,
		"hub_config_status_label": hub_config_status_label,
		"hub_replay_panel": hub_replay_panel,
		"hub_replay_title_label": hub_replay_title_label,
		"hub_replay_checkpoint_label": hub_replay_checkpoint_label,
		"hub_replay_summary_label": hub_replay_summary_label,
		"hub_replay_checkpoint_button": hub_replay_checkpoint_button,
		"hub_replay_fetch_button": hub_replay_fetch_button,
		"hub_replay_apply_button": hub_replay_apply_button,
		"hub_replay_status_label": hub_replay_status_label,
		"hub_chat_panel": hub_chat_panel,
		"hub_chat_title_label": hub_chat_title_label,
		"hub_chat_history_label": hub_chat_history_label,
		"hub_chat_input_edit": hub_chat_input_edit,
		"hub_chat_send_button": hub_chat_send_button,
		"hub_chat_status_label": hub_chat_status_label,
		"log_label": log_label,
		"sim_card_panel": sim_card_panel,
		"api_card_panel": api_card_panel,
		"eval_card_panel": eval_card_panel,
	}


func _hub_layout_state() -> Dictionary:
	return {
		"preserve_editor_hub_layout": preserve_editor_hub_layout,
		"agent_submenu_open": _agent_submenu_open,
		"checks_submenu_open": _checks_submenu_open,
		"rp_submenu_open": _rp_submenu_open,
		"hub_config_collapsed": _hub_config_collapsed,
		"hub_config_collapsed_height": _HUB_CONFIG_COLLAPSED_HEIGHT,
		"hub_config_expanded_height": _HUB_CONFIG_EXPANDED_BOTTOM - 44.0,
		"ui_base_width": _UI_BASE_WIDTH,
		"ui_base_height": _UI_BASE_HEIGHT,
		"ui_margin": _UI_MARGIN,
		"ui_gap": _UI_GAP,
	}


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


func _agent_studio_controls() -> Dictionary:
	return {
		"agent_studio_panel": agent_studio_panel,
		"agent_back_button": agent_back_button,
		"agent_studio_mode_label": agent_studio_mode_label,
		"agent_operate_button": agent_operate_button,
		"agent_author_button": agent_author_button,
		"agent_eval_run_button": agent_eval_run_button,
		"agent_eval_suite_button": agent_eval_suite_button,
		"agent_dataset_source_button": agent_dataset_source_button,
		"agent_datasets_button": agent_datasets_button,
		"agent_synonyms_button": agent_synonyms_button,
		"agent_finetune_button": agent_finetune_button,
		"agent_profiles_button": agent_profiles_button,
		"agent_ai_status_button": agent_ai_status_button,
		"agent_eval_status_label": agent_eval_status_label,
		"agent_system_metrics_label": agent_system_metrics_label,
		"agent_latest_runs_label": agent_latest_runs_label,
		"agent_studio_hint_label": agent_studio_hint_label,
		"agent_form_panel": agent_form_panel,
	}


func _agent_form_ui_controls() -> Dictionary:
	return {
		"agent_form_panel": agent_form_panel,
		"agent_form_title_label": agent_form_title_label,
		"agent_form_mode_button": agent_form_mode_button,
		"agent_form_target_button": agent_form_target_button,
		"agent_form_name_edit": agent_form_name_edit,
		"agent_form_apply_button": agent_form_apply_button,
		"agent_form_payload_edit": agent_form_payload_edit,
		"agent_form_fields_scroll": agent_form_fields_scroll,
		"agent_form_fields_box": agent_form_fields_box,
		"agent_form_status_label": agent_form_status_label,
	}


func _agent_studio_state() -> Dictionary:
	return {
		"studio_mode": _agent_studio_mode,
		"eval_pid": _eval_pid,
		"eval_started_ms": _eval_started_ms,
		"eval_expected_duration_seconds": eval_expected_duration_seconds,
		"last_eval_exit_code": _last_eval_exit_code,
		"enable_system_resource_monitoring": enable_system_resource_monitoring,
		"system_metrics_text": _agent_system_metrics_text(),
		"dataset_status_text": _dataset_status_text,
		"active_dataset_label": _active_dataset_label(),
		"synonym_status_text": _synonym_status_text,
		"active_synonym_label": _active_synonym_label(),
		"profile_status_text": _profile_status_text,
		"active_profile_label": _active_profile_label(),
		"advanced_settings_status_text": _advanced_settings_status_text,
		"jobs_status_text": _jobs_status_text,
		"finetune_status_text": _finetune_status_text,
		"latest_eval_summary_text": _latest_eval_summary_text,
		"ai_trend_summary_text": _ai_trend_summary_text,
		"artifacts_summary_text": _artifacts_summary_text,
		"experiments_summary_text": _experiments_summary_text,
		"policy_sandbox_summary_text": _policy_sandbox_summary_text,
		"release_gate_summary_text": _release_gate_summary_text,
		"audit_trail_summary_text": _audit_trail_summary_text,
		"security_model_summary_text": _security_model_summary_text,
		"eval_suite_options": _EVAL_SUITE_OPTIONS,
		"dataset_source_options": _DATASET_SOURCE_OPTIONS,
		"agent_eval_suite": _agent_eval_suite,
		"dataset_source_mode": _dataset_source_mode,
		"dataset_source_mode_label": _dataset_source_mode_label(),
		"agent_submenu_open": _agent_submenu_open,
		"agent_form_kind": _agent_form_kind,
		"collapse_agent_status_when_form_open": collapse_agent_status_when_form_open,
		"agent_form_panel_normal_tint": _AGENT_FORM_PANEL_NORMAL_TINT,
		"agent_form_panel_active_tint": _AGENT_FORM_PANEL_ACTIVE_TINT,
		"agent_status_normal_tint": _AGENT_STATUS_NORMAL_TINT,
		"agent_status_dim_tint": _AGENT_STATUS_DIM_TINT,
		"destructive_armed_action": _destructive_armed_action,
		"destructive_armed_until_ms": _destructive_armed_until_ms,
		"now_ms": Time.get_ticks_msec(),
		"agent_action_busy": _agent_action_busy,
		"dataset_pid": _dataset_pid,
		"finetune_pid": _finetune_pid,
	}


func _agent_runtime_state() -> Dictionary:
	return {
		"studio_mode": _agent_studio_mode,
		"eval_pid": _eval_pid,
		"eval_started_ms": _eval_started_ms,
		"last_eval_exit_code": _last_eval_exit_code,
		"agent_eval_suite": _agent_eval_suite,
		"eval_quick_limit": maxi(1, eval_quick_limit),
		"python_exec": _resolve_python_executable(),
		"repo_root": ProjectSettings.globalize_path("res://.."),
		"eval_script_abs": ProjectSettings.globalize_path("res://../scripts/agent/run_eval.py"),
		"finetune_pid": _finetune_pid,
		"finetune_started_ms": _finetune_started_ms,
		"last_finetune_exit_code": _last_finetune_exit_code,
		"finetune_profile": _finetune_profile,
		"finetune_base_model": _finetune_base_model,
		"finetune_output_name": _finetune_output_name,
		"finetune_epochs": _finetune_epochs,
		"finetune_max_steps": _finetune_max_steps,
		"finetune_batch_size": _finetune_batch_size,
		"finetune_lr": _finetune_lr,
		"active_dataset_name": _active_dataset_name,
		"fallback_finetune_train_file_res": "res://../novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl",
		"finetune_script_abs": ProjectSettings.globalize_path("res://../scripts/agent/fine_tune_pipeline.py"),
		"jobs_queue_path": _JOBS_QUEUE_PATH,
		"destructive_guard_enabled": _destructive_guard_enabled,
		"destructive_guard_window_ms": _destructive_guard_window_ms,
		"destructive_armed_action": _destructive_armed_action,
		"destructive_armed_until_ms": _destructive_armed_until_ms,
		"now_ms": Time.get_ticks_msec(),
	}


func _agent_authoring_payload_state() -> Dictionary:
	return {
		"form_kind": _agent_form_kind,
		"form_mode_value": _agent_form_mode_value,
		"form_target_value": _agent_form_target_value,
		"form_name": agent_form_name_edit.text.strip_edges(),
		"form_controls": _agent_form_controls,
		"finetune_base_model": _finetune_base_model,
	}


func _agent_authoring_persistence_state() -> Dictionary:
	return {
		"form_target_value": _agent_form_target_value,
		"form_mode_value": _agent_form_mode_value,
		"dataset_registry_path": _DATASET_REGISTRY_PATH,
		"synonym_registry_path": _SYNONYM_REGISTRY_PATH,
		"profile_registry_path": _PROFILE_REGISTRY_PATH,
		"advanced_settings_path": _ADVANCED_SETTINGS_PATH,
		"active_dataset_name": _active_dataset_name,
		"active_dataset_tag": _active_dataset_tag,
		"active_synonym_set": _active_synonym_set,
		"active_synonym_tag": _active_synonym_tag,
		"active_profile_name": _active_profile_name,
		"active_profile_mode": _active_profile_mode,
		"profile_status_text": _profile_status_text,
	}


func _agent_registry_state() -> Dictionary:
	return {
		"dataset_registry_path": _DATASET_REGISTRY_PATH,
		"synonym_registry_path": _SYNONYM_REGISTRY_PATH,
		"profile_registry_path": _PROFILE_REGISTRY_PATH,
		"advanced_settings_path": _ADVANCED_SETTINGS_PATH,
		"security_model_path": _SECURITY_MODEL_PATH,
		"destructive_guard_enabled": _destructive_guard_enabled,
		"destructive_guard_window_ms": _destructive_guard_window_ms,
		"destructive_guard_token": _destructive_guard_token,
	}


func _agent_restpoint_summary_state() -> Dictionary:
	return {
		"active_dataset_name": _active_dataset_name,
		"active_dataset_tag": _active_dataset_tag,
		"active_synonym_set": _active_synonym_set,
		"active_synonym_tag": _active_synonym_tag,
		"finetune_output_name": _finetune_output_name,
		"last_finetune_exit_code": _last_finetune_exit_code,
		"quality_tests_last": _quality_tests_last,
		"quality_types_last": _quality_types_last,
		"quality_coverage_last": _quality_coverage_last,
		"latest_eval_runs": _latest_eval_runs,
		"ai_trend_summary_text": _ai_trend_summary_text,
		"destructive_guard_enabled": _destructive_guard_enabled,
		"destructive_guard_token": _destructive_guard_token,
		"advanced_settings_path": _ADVANCED_SETTINGS_PATH,
		"audit_trail_path": _AUDIT_TRAIL_PATH,
	}


func _server_ops_state() -> Dictionary:
	return {
		"server_pid": _server_pid,
		"server_status_text": _server_status_text,
		"server_exit_reported": _server_exit_reported,
		"python_exec": _resolve_python_executable(),
		"server_script_abs": ProjectSettings.globalize_path(server_script_path),
	}


func _runtime_audit_state() -> Dictionary:
	return {
		"runtime_events": _runtime_events,
		"runtime_event_timestamps_ms": _runtime_event_timestamps_ms,
		"max_runtime_events": _MAX_RUNTIME_EVENTS,
		"event_rate_window_seconds": _EVENT_RATE_WINDOW_SECONDS,
		"audit_trail_path": _AUDIT_TRAIL_PATH,
	}


func _runtime_telemetry_state() -> Dictionary:
	return {
		"server_python_path": server_python_path,
		"eval_summary_script_path": eval_summary_script_path,
		"system_snapshot_script_path": system_snapshot_script_path,
		"enable_system_resource_monitoring": enable_system_resource_monitoring,
		"metrics_refresh_interval_seconds": metrics_refresh_interval_seconds,
		"eval_summary_refresh_interval_seconds": eval_summary_refresh_interval_seconds,
		"agent_submenu_open": _agent_submenu_open,
		"last_eval_summary_refresh_ms": _last_eval_summary_refresh_ms,
		"latest_eval_runs": _latest_eval_runs,
		"ai_trend_summary_text": _ai_trend_summary_text,
		"last_metrics_refresh_ms": _last_metrics_refresh_ms,
		"system_cpu_percent": _system_cpu_percent,
		"system_ram_percent": _system_ram_percent,
		"system_gpu_vram_percent": _system_gpu_vram_percent,
		"system_gpu_vram_used_mb": _system_gpu_vram_used_mb,
		"system_gpu_vram_total_mb": _system_gpu_vram_total_mb,
		"system_cpu_temp_c": _system_cpu_temp_c,
		"system_gpu_temp_c": _system_gpu_temp_c,
		"sim_client": _sim_client,
		"last_status_message": _last_status_message,
		"last_success_ms": _last_success_ms,
		"server_pid": _server_pid,
		"server_status_text": _server_status_text,
	}


func _apply_agent_registry_state_result(result: Dictionary) -> void:
	var updates_any = result.get("updates", {})
	if typeof(updates_any) != TYPE_DICTIONARY:
		return
	var updates: Dictionary = updates_any
	if updates.has("active_dataset_name"):
		_active_dataset_name = str(updates.get("active_dataset_name", _active_dataset_name))
	if updates.has("active_dataset_tag"):
		_active_dataset_tag = str(updates.get("active_dataset_tag", _active_dataset_tag))
	if updates.has("dataset_status_text"):
		_dataset_status_text = str(updates.get("dataset_status_text", _dataset_status_text))
	if updates.has("active_synonym_set"):
		_active_synonym_set = str(updates.get("active_synonym_set", _active_synonym_set))
	if updates.has("active_synonym_tag"):
		_active_synonym_tag = str(updates.get("active_synonym_tag", _active_synonym_tag))
	if updates.has("synonym_status_text"):
		_synonym_status_text = str(updates.get("synonym_status_text", _synonym_status_text))
	if updates.has("active_profile_name"):
		_active_profile_name = str(updates.get("active_profile_name", _active_profile_name))
	if updates.has("active_profile_mode"):
		_active_profile_mode = str(updates.get("active_profile_mode", _active_profile_mode))
	if updates.has("profile_status_text"):
		_profile_status_text = str(updates.get("profile_status_text", _profile_status_text))
	if updates.has("advanced_settings_status_text"):
		_advanced_settings_status_text = str(updates.get("advanced_settings_status_text", _advanced_settings_status_text))
	if updates.has("policy_sandbox_summary_text"):
		_policy_sandbox_summary_text = str(updates.get("policy_sandbox_summary_text", _policy_sandbox_summary_text))
	if updates.has("destructive_guard_enabled"):
		_destructive_guard_enabled = bool(updates.get("destructive_guard_enabled", _destructive_guard_enabled))
	if updates.has("destructive_guard_window_ms"):
		_destructive_guard_window_ms = int(updates.get("destructive_guard_window_ms", _destructive_guard_window_ms))
	if updates.has("destructive_guard_token"):
		_destructive_guard_token = str(updates.get("destructive_guard_token", _destructive_guard_token))
	if updates.has("security_model_summary_text"):
		_security_model_summary_text = str(updates.get("security_model_summary_text", _security_model_summary_text))


func _apply_agent_restpoint_summary_result(result: Dictionary) -> void:
	var updates_any = result.get("updates", {})
	if typeof(updates_any) != TYPE_DICTIONARY:
		return
	var updates: Dictionary = updates_any
	if updates.has("artifacts_summary_text"):
		_artifacts_summary_text = str(updates.get("artifacts_summary_text", _artifacts_summary_text))
	if updates.has("experiments_summary_text"):
		_experiments_summary_text = str(updates.get("experiments_summary_text", _experiments_summary_text))
	if updates.has("policy_sandbox_summary_text"):
		_policy_sandbox_summary_text = str(updates.get("policy_sandbox_summary_text", _policy_sandbox_summary_text))
	if updates.has("release_gate_summary_text"):
		_release_gate_summary_text = str(updates.get("release_gate_summary_text", _release_gate_summary_text))
	if updates.has("audit_trail_summary_text"):
		_audit_trail_summary_text = str(updates.get("audit_trail_summary_text", _audit_trail_summary_text))
	if updates.has("security_model_summary_text"):
		_security_model_summary_text = str(updates.get("security_model_summary_text", _security_model_summary_text))


func _apply_server_ops_result(result: Dictionary) -> void:
	var updates_any = result.get("updates", {})
	if typeof(updates_any) == TYPE_DICTIONARY:
		var updates: Dictionary = updates_any
		if updates.has("server_pid"):
			_server_pid = int(updates.get("server_pid", _server_pid))
		if updates.has("server_status_text"):
			_server_status_text = str(updates.get("server_status_text", _server_status_text))
		if updates.has("server_exit_reported"):
			_server_exit_reported = bool(updates.get("server_exit_reported", _server_exit_reported))
		if updates.has("server_toggle_text"):
			server_toggle_button.text = str(updates.get("server_toggle_text", server_toggle_button.text))
		if updates.has("server_status_label_text"):
			server_status_label.text = str(updates.get("server_status_label_text", server_status_label.text))
	var events_any = result.get("events", [])
	if typeof(events_any) == TYPE_ARRAY:
		for event_any in events_any:
			if typeof(event_any) != TYPE_DICTIONARY:
				continue
			var event: Dictionary = event_any
			_append_runtime_event(str(event.get("tag", "SERVER_EVENT")), event.get("payload", {}))
	if bool(result.get("refresh_server_control_ui", false)):
		_update_server_control_ui()


func _apply_runtime_audit_result(result: Dictionary) -> void:
	var updates_any = result.get("updates", {})
	if typeof(updates_any) != TYPE_DICTIONARY:
		return
	var updates: Dictionary = updates_any
	if updates.has("runtime_events"):
		var runtime_events_any = updates.get("runtime_events", _runtime_events)
		if typeof(runtime_events_any) == TYPE_ARRAY:
			_runtime_events = runtime_events_any
	if updates.has("runtime_event_timestamps_ms"):
		var timestamps_any = updates.get("runtime_event_timestamps_ms", _runtime_event_timestamps_ms)
		if typeof(timestamps_any) == TYPE_ARRAY:
			_runtime_event_timestamps_ms = timestamps_any
	if updates.has("last_error_code"):
		_last_error_code = str(updates.get("last_error_code", _last_error_code))
	if bool(updates.get("render_pc_centric_view", false)):
		_render_pc_centric_view()


func _apply_runtime_telemetry_result(result: Dictionary) -> void:
	var updates_any = result.get("updates", {})
	if typeof(updates_any) != TYPE_DICTIONARY:
		return
	var updates: Dictionary = updates_any
	if updates.has("last_eval_summary_refresh_ms"):
		_last_eval_summary_refresh_ms = int(updates.get("last_eval_summary_refresh_ms", _last_eval_summary_refresh_ms))
	if updates.has("latest_eval_summary_text"):
		_latest_eval_summary_text = str(updates.get("latest_eval_summary_text", _latest_eval_summary_text))
	if updates.has("latest_eval_runs"):
		var latest_eval_runs_any = updates.get("latest_eval_runs", _latest_eval_runs)
		if typeof(latest_eval_runs_any) == TYPE_ARRAY:
			_latest_eval_runs = latest_eval_runs_any
	if updates.has("ai_trend_summary_text"):
		_ai_trend_summary_text = str(updates.get("ai_trend_summary_text", _ai_trend_summary_text))
	if updates.has("last_metrics_refresh_ms"):
		_last_metrics_refresh_ms = int(updates.get("last_metrics_refresh_ms", _last_metrics_refresh_ms))
	if updates.has("system_cpu_percent"):
		_system_cpu_percent = float(updates.get("system_cpu_percent", _system_cpu_percent))
	if updates.has("system_ram_percent"):
		_system_ram_percent = float(updates.get("system_ram_percent", _system_ram_percent))
	if updates.has("system_gpu_vram_percent"):
		_system_gpu_vram_percent = float(updates.get("system_gpu_vram_percent", _system_gpu_vram_percent))
	if updates.has("system_gpu_vram_used_mb"):
		_system_gpu_vram_used_mb = float(updates.get("system_gpu_vram_used_mb", _system_gpu_vram_used_mb))
	if updates.has("system_gpu_vram_total_mb"):
		_system_gpu_vram_total_mb = float(updates.get("system_gpu_vram_total_mb", _system_gpu_vram_total_mb))
	if updates.has("system_cpu_temp_c"):
		_system_cpu_temp_c = float(updates.get("system_cpu_temp_c", _system_cpu_temp_c))
	if updates.has("system_gpu_temp_c"):
		_system_gpu_temp_c = float(updates.get("system_gpu_temp_c", _system_gpu_temp_c))


func _apply_agent_authoring_persistence_result(result: Dictionary) -> void:
	var updates_any = result.get("updates", {})
	if typeof(updates_any) == TYPE_DICTIONARY:
		var updates: Dictionary = updates_any
		if updates.has("active_dataset_name"):
			_active_dataset_name = str(updates.get("active_dataset_name", _active_dataset_name))
		if updates.has("active_dataset_tag"):
			_active_dataset_tag = str(updates.get("active_dataset_tag", _active_dataset_tag))
		if updates.has("dataset_status_text"):
			_dataset_status_text = str(updates.get("dataset_status_text", _dataset_status_text))
		if updates.has("active_synonym_set"):
			_active_synonym_set = str(updates.get("active_synonym_set", _active_synonym_set))
		if updates.has("active_synonym_tag"):
			_active_synonym_tag = str(updates.get("active_synonym_tag", _active_synonym_tag))
		if updates.has("synonym_status_text"):
			_synonym_status_text = str(updates.get("synonym_status_text", _synonym_status_text))
		if updates.has("active_profile_name"):
			_active_profile_name = str(updates.get("active_profile_name", _active_profile_name))
		if updates.has("active_profile_mode"):
			_active_profile_mode = str(updates.get("active_profile_mode", _active_profile_mode))
		if updates.has("profile_status_text"):
			_profile_status_text = str(updates.get("profile_status_text", _profile_status_text))
		if updates.has("advanced_settings_status_text"):
			_advanced_settings_status_text = str(updates.get("advanced_settings_status_text", _advanced_settings_status_text))
		if updates.has("form_status_text"):
			agent_form_status_label.text = str(updates.get("form_status_text", agent_form_status_label.text))
	var events_any = result.get("events", [])
	if typeof(events_any) == TYPE_ARRAY:
		for event_any in events_any:
			if typeof(event_any) != TYPE_DICTIONARY:
				continue
			var event: Dictionary = event_any
			_append_runtime_event(str(event.get("tag", "AGENT_FORM")), event.get("payload", {}))


func _apply_agent_runtime_result(result: Dictionary) -> void:
	var updates_any = result.get("updates", {})
	if typeof(updates_any) == TYPE_DICTIONARY:
		var updates: Dictionary = updates_any
		if updates.has("destructive_armed_action"):
			_destructive_armed_action = str(updates.get("destructive_armed_action", _destructive_armed_action))
		if updates.has("destructive_armed_until_ms"):
			_destructive_armed_until_ms = int(updates.get("destructive_armed_until_ms", _destructive_armed_until_ms))
		if updates.has("eval_pid"):
			_eval_pid = int(updates.get("eval_pid", _eval_pid))
		if updates.has("eval_started_ms"):
			_eval_started_ms = int(updates.get("eval_started_ms", _eval_started_ms))
		if updates.has("last_eval_exit_code"):
			_last_eval_exit_code = int(updates.get("last_eval_exit_code", _last_eval_exit_code))
		if updates.has("finetune_pid"):
			_finetune_pid = int(updates.get("finetune_pid", _finetune_pid))
		if updates.has("finetune_started_ms"):
			_finetune_started_ms = int(updates.get("finetune_started_ms", _finetune_started_ms))
		if updates.has("last_finetune_exit_code"):
			_last_finetune_exit_code = int(updates.get("last_finetune_exit_code", _last_finetune_exit_code))
		if updates.has("finetune_profile"):
			_finetune_profile = str(updates.get("finetune_profile", _finetune_profile))
		if updates.has("finetune_base_model"):
			_finetune_base_model = str(updates.get("finetune_base_model", _finetune_base_model))
		if updates.has("finetune_output_name"):
			_finetune_output_name = str(updates.get("finetune_output_name", _finetune_output_name))
		if updates.has("finetune_epochs"):
			_finetune_epochs = int(updates.get("finetune_epochs", _finetune_epochs))
		if updates.has("finetune_max_steps"):
			_finetune_max_steps = int(updates.get("finetune_max_steps", _finetune_max_steps))
		if updates.has("finetune_batch_size"):
			_finetune_batch_size = int(updates.get("finetune_batch_size", _finetune_batch_size))
		if updates.has("finetune_lr"):
			_finetune_lr = _to_float_or_default(updates.get("finetune_lr", _finetune_lr), _finetune_lr)
		if updates.has("finetune_status_text"):
			_finetune_status_text = str(updates.get("finetune_status_text", _finetune_status_text))
		if updates.has("jobs_status_text"):
			_jobs_status_text = str(updates.get("jobs_status_text", _jobs_status_text))
		if updates.has("agent_summary_refresh_pending"):
			_agent_summary_refresh_pending = bool(updates.get("agent_summary_refresh_pending", _agent_summary_refresh_pending))
		if updates.has("agent_summary_refresh_due_ms"):
			_agent_summary_refresh_due_ms = int(updates.get("agent_summary_refresh_due_ms", _agent_summary_refresh_due_ms))
		if updates.has("form_status_text"):
			agent_form_status_label.text = str(updates.get("form_status_text", agent_form_status_label.text))
	if result.has("set_studio_mode"):
		_agent_studio_mode = str(result.get("set_studio_mode", _agent_studio_mode))
	if result.has("open_form"):
		_open_agent_form(str(result.get("open_form", "")))
	if bool(result.get("refresh_latest_eval_summary", false)):
		_refresh_latest_eval_summary(true)
	var events_any = result.get("events", [])
	if typeof(events_any) == TYPE_ARRAY:
		for event_any in events_any:
			if typeof(event_any) != TYPE_DICTIONARY:
				continue
			var event: Dictionary = event_any
			_append_runtime_event(str(event.get("tag", "AGENT_ACTION")), event.get("payload", {}))


func _agent_system_metrics_text() -> String:
	return "System: CPU %s | RAM %s | VRAM %s | Temp %s" % [
		_format_percent(_system_cpu_percent),
		_format_percent(_system_ram_percent),
		_format_vram(),
		_format_temperature(_effective_temperature_c()),
	]


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
	return _runtime_telemetry_controller.sim_runtime_status(_runtime_telemetry_state())


func _derive_health_state(runtime_status: Dictionary) -> Dictionary:
	return _runtime_telemetry_controller.derive_health_state(_runtime_telemetry_state(), runtime_status)


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
	return _session_replay_helpers.coerce_dict_array(value)


func _parse_slot_number(value: Variant) -> int:
	return _session_replay_helpers.parse_slot_number(value)


func _derive_initial_slot(pc_log: Array) -> int:
	return _session_replay_helpers.derive_initial_slot(pc_log)


func _extract_slot_from_entry(entry: Dictionary) -> int:
	return _session_replay_helpers.extract_slot_from_entry(entry)


func _live_session_epoch_name() -> String:
	return _session_replay_helpers.live_session_epoch_name(_hub_chat_session_id)


func _apply_session_replay_state_updates(updates: Dictionary) -> void:
	if updates.has("live_session_artifact_paths"):
		_live_session_artifact_paths = updates.get("live_session_artifact_paths", {})
	if updates.has("live_session_resume_checkpoint_id"):
		_live_session_resume_checkpoint_id = str(updates.get("live_session_resume_checkpoint_id", "")).strip_edges()
	if updates.has("loaded_epochs"):
		_loaded_epochs = updates.get("loaded_epochs", [])
	if updates.has("current_epoch_index"):
		_current_epoch_index = int(updates.get("current_epoch_index", _current_epoch_index))
	if updates.has("current_slot"):
		_current_slot = int(updates.get("current_slot", _current_slot))
	if updates.has("audio_assets_present"):
		_audio_assets_present = bool(updates.get("audio_assets_present", _audio_assets_present))
	if updates.has("live_replay_manifest"):
		_live_replay_manifest = updates.get("live_replay_manifest", {})
	if updates.has("hub_selected_replay_checkpoint_id"):
		_hub_selected_replay_checkpoint_id = str(updates.get("hub_selected_replay_checkpoint_id", "")).strip_edges()
	_persist_hub_session_state()


func _apply_live_session_state(session_payload: Dictionary) -> void:
	if session_payload.has("campaign_id"):
		_hub_chat_campaign_id = str(session_payload.get("campaign_id", _hub_chat_campaign_id)).strip_edges()
	if session_payload.has("scene_id"):
		_hub_chat_scene_id = str(session_payload.get("scene_id", _hub_chat_scene_id)).strip_edges()
	var updates: Dictionary = _session_replay_state_controller.build_live_session_state(
		session_payload,
		_hub_chat_session_id,
		_current_slot,
		_audio_assets_present,
		_hub_selected_replay_checkpoint_id
	)
	_apply_session_replay_state_updates(updates)
	_set_marquee_text(epoch_status_label, str(updates.get("epoch_status_text", "Epochen: Live-Session synchronisiert")))
	if updates.has("rp_replay_seed_text"):
		rp_replay_seed_label.text = str(updates.get("rp_replay_seed_text", rp_replay_seed_label.text))
	_render_pc_centric_view()
	_refresh_hub_replay_ui()
	_refresh_module_cards()


func _hub_request_host() -> String:
	var host := "127.0.0.1"
	if _sim_client:
		host = str(_sim_client.get("host"))
	return host


func _hub_request_port() -> int:
	var port := 8765
	if _sim_client:
		port = int(_sim_client.get("port"))
	return port


func _request_live_session_state() -> void:
	var request_state: Dictionary = _session_replay_request_controller.request_live_session(
		_hub_chat_session_id,
		_hub_session_request,
		_hub_request_host(),
		_hub_request_port()
	)
	if not bool(request_state.get("started", false)):
		var message := str(request_state.get("message", "")).strip_edges()
		if message != "":
			_set_marquee_text(epoch_status_label, message)
		return
	_append_runtime_event("SESSION_SYNC", request_state.get("event", {}))


func _request_live_session_replay() -> void:
	var request_state: Dictionary = _session_replay_request_controller.request_live_replay(
		_hub_chat_session_id,
		_hub_replay_request,
		_hub_request_host(),
		_hub_request_port()
	)
	if not bool(request_state.get("started", false)):
		var message := str(request_state.get("message", "")).strip_edges()
		if message != "":
			hub_replay_status_label.text = message
		return
	hub_replay_status_label.text = str(request_state.get("pending_status", hub_replay_status_label.text))
	_append_runtime_event("SESSION_REPLAY", request_state.get("event", {}))


func _coerce_string_array(value: Variant) -> Array[String]:
	return _session_replay_helpers.coerce_string_array(value)


func _refresh_hub_replay_checkpoint_options() -> void:
	var option_state: Dictionary = _session_replay_helpers.build_checkpoint_options(
		_live_replay_manifest,
		_live_session_resume_checkpoint_id,
		_hub_selected_replay_checkpoint_id
	)
	var checkpoints: Array[String] = option_state.get("checkpoints", [])
	hub_replay_checkpoint_button.clear()
	if checkpoints.is_empty():
		hub_replay_checkpoint_button.add_item("Keine Checkpoints")
		hub_replay_checkpoint_button.disabled = true
		_hub_selected_replay_checkpoint_id = ""
		return
	hub_replay_checkpoint_button.disabled = false
	for checkpoint in checkpoints:
		hub_replay_checkpoint_button.add_item(checkpoint)
	_hub_selected_replay_checkpoint_id = str(option_state.get("selected_checkpoint_id", "")).strip_edges()
	var selected_index := checkpoints.find(_hub_selected_replay_checkpoint_id)
	if selected_index < 0:
		selected_index = 0
	hub_replay_checkpoint_button.select(selected_index)


func _refresh_hub_replay_ui() -> void:
	var current_epoch := _loaded_epochs[0] if not _loaded_epochs.is_empty() else {}
	var manifest_status := str(_live_replay_manifest.get("session_status", "n/a"))
	var world_count := int(_live_replay_manifest.get("world_event_count", current_epoch.get("world_log", []).size()))
	var pc_count := int(_live_replay_manifest.get("pc_event_count", current_epoch.get("pc_log", []).size()))
	var patch_count := int(_live_replay_manifest.get("state_patch_count", current_epoch.get("state_patches", []).size()))
	hub_replay_summary_label.text = "Manifest: %s | world=%d | pc=%d | patches=%d" % [manifest_status, world_count, pc_count, patch_count]
	_refresh_hub_replay_checkpoint_options()
	var resume_checkpoint := _live_session_resume_checkpoint_id
	if resume_checkpoint == "":
		resume_checkpoint = str(_live_replay_manifest.get("resume_checkpoint_id", "")).strip_edges()
	if resume_checkpoint == "" and _hub_selected_replay_checkpoint_id == "":
		hub_replay_status_label.text = "Replay: kein Manifest/Checkpoint aktiv"
		return
	var status_parts: Array[String] = []
	if resume_checkpoint != "":
		status_parts.append("resume=%s" % resume_checkpoint)
	if _hub_selected_replay_checkpoint_id != "":
		status_parts.append("selected=%s" % _hub_selected_replay_checkpoint_id)
	var replay_path := ""
	if typeof(_live_replay_manifest.get("artifact_paths", {})) == TYPE_DICTIONARY:
		replay_path = str((_live_replay_manifest.get("artifact_paths", {}) as Dictionary).get("replay_manifest", "")).strip_edges()
	if replay_path != "":
		status_parts.append("manifest=%s" % replay_path)
	hub_replay_status_label.text = "Replay: %s" % (" | ".join(status_parts) if not status_parts.is_empty() else "n/a")


func _parse_checkpoint_tick(checkpoint_id: String) -> int:
	return _session_replay_helpers.parse_checkpoint_tick(checkpoint_id)


func _find_slot_for_checkpoint_in_entries(entries: Array, checkpoint_id: String) -> int:
	return _session_replay_helpers.find_slot_for_checkpoint_in_entries(entries, checkpoint_id)


func _find_slot_for_checkpoint(checkpoint_id: String) -> int:
	return _session_replay_helpers.find_slot_for_checkpoint(
		_loaded_epochs,
		_current_epoch_index,
		_live_replay_manifest,
		checkpoint_id
	)


func _apply_selected_replay_checkpoint() -> void:
	var checkpoint_id := _hub_selected_replay_checkpoint_id.strip_edges()
	if checkpoint_id == "":
		hub_replay_status_label.text = "Replay: kein Checkpoint ausgewaehlt"
		return
	var updates: Dictionary = _session_replay_state_controller.build_selected_replay_checkpoint_state(
		checkpoint_id,
		_loaded_epochs,
		_current_epoch_index,
		_live_replay_manifest,
		_current_slot
	)
	_apply_session_replay_state_updates(updates)
	rp_replay_seed_label.text = str(updates.get("rp_replay_seed_text", rp_replay_seed_label.text))
	_set_marquee_text(epoch_status_label, str(updates.get("epoch_status_text", epoch_status_label.text)))
	hub_chat_status_label.text = str(updates.get("hub_chat_status_text", hub_chat_status_label.text))
	_append_runtime_event("SESSION_REPLAY", updates.get("runtime_event", {"action": "apply", "checkpoint_id": checkpoint_id, "slot": _current_slot}))
	_render_pc_centric_view()
	_refresh_hub_replay_ui()


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
	if _live_session_resume_checkpoint_id != "":
		lines.append("- Resume-Anker: %s" % _live_session_resume_checkpoint_id)
	if _hub_selected_replay_checkpoint_id != "" and _hub_selected_replay_checkpoint_id != _live_session_resume_checkpoint_id:
		lines.append("- Replay-Auswahl: %s" % _hub_selected_replay_checkpoint_id)
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
	return _hub_chat_controller.build_slot_id(_current_slot)


func _next_hub_chat_turn_id() -> String:
	return _hub_chat_controller.next_turn_id(_hub_chat_turn_index)


func _build_hub_chat_public_context() -> String:
	return _hub_chat_controller.build_public_context(
		_current_slot,
		_hub_chat_current_scene_text,
		_hub_chat_current_consequence,
		_hub_chat_current_options
	)


func _build_hub_chat_retrieval_query(prompt: String) -> String:
	return _hub_chat_controller.build_retrieval_query(
		prompt,
		_hub_chat_slot_id(),
		_hub_chat_scene_id,
		_hub_chat_current_scene_text,
		_hub_chat_current_consequence
	)


func _coerce_hub_chat_string_array(value: Variant) -> Array[String]:
	return _hub_chat_controller.coerce_string_array(value)


func _parse_hub_chat_response(content: String) -> Dictionary:
	return _hub_chat_controller.parse_response(content)


func _refresh_hub_chat_ui() -> void:
	var chat_title := get_node_or_null("HubChatPanel/HubChatTitleLabel") as Label
	if chat_title:
		chat_title.text = "Live-Spielclient | %s | scene=%s | turn=%d" % [_hub_chat_slot_id(), _hub_chat_scene_id, _hub_chat_turn_index]

	var lines: Array[String] = []
	lines.append("Session: %s | Kampagne: %s" % [_hub_chat_session_id if _hub_chat_session_id != "" else "n/a", _hub_chat_campaign_id])
	if _live_session_resume_checkpoint_id != "" or _hub_selected_replay_checkpoint_id != "":
		lines.append("Replay/Resume: %s | selected=%s" % [
			_live_session_resume_checkpoint_id if _live_session_resume_checkpoint_id != "" else "n/a",
			_hub_selected_replay_checkpoint_id if _hub_selected_replay_checkpoint_id != "" else "n/a",
		])
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
	var updates := _hub_chat_controller.build_response_state(
		answer,
		_current_slot,
		_hub_chat_scene_id,
		_hub_chat_current_scene_text,
		_hub_chat_pending_turn_id,
		_hub_chat_turn_index
	)
	_hub_chat_scene_id = str(updates.get("scene_id", _hub_chat_scene_id))
	_hub_chat_current_scene_text = str(updates.get("scene_text", _hub_chat_current_scene_text))
	_hub_chat_current_consequence = str(updates.get("consequence", _hub_chat_current_consequence))
	_hub_chat_current_options = updates.get("options", _hub_chat_current_options)
	_hub_chat_current_state_patches = updates.get("state_patches", _hub_chat_current_state_patches)
	_hub_chat_public_context = str(updates.get("public_context", _hub_chat_public_context))
	_hub_chat_turn_index = int(updates.get("turn_index", _hub_chat_turn_index))
	_hub_chat_pending_turn_id = str(updates.get("pending_turn_id", _hub_chat_pending_turn_id))
	_persist_hub_session_state()
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


func _set_agent_module_exclusive(open: bool, defer_hub_refresh: bool = false) -> void:
	if open and _checks_submenu_open:
		_set_checks_module_exclusive(false, true)
	if open and _rp_submenu_open:
		_set_rp_module_exclusive(false, true)
	_agent_studio_controller.set_module_exclusive_ui(_agent_studio_controls(), open)
	_agent_submenu_open = open

	if defer_hub_refresh:
		return
	_apply_hub_visibility_for_modules()


func _set_checks_module_exclusive(open: bool, defer_hub_refresh: bool = false) -> void:
	if open and _agent_submenu_open:
		_set_agent_module_exclusive(false, true)
	if open and _rp_submenu_open:
		_set_rp_module_exclusive(false, true)

	_checks_rp_controller.set_checks_module_exclusive(_checks_rp_controls(), open, _checks_running)
	_checks_submenu_open = open

	if defer_hub_refresh:
		return
	_apply_hub_visibility_for_modules()
	_refresh_checks_studio_ui()


func _set_rp_module_exclusive(open: bool, defer_hub_refresh: bool = false) -> void:
	if open and _agent_submenu_open:
		_set_agent_module_exclusive(false, true)
	if open and _checks_submenu_open:
		_set_checks_module_exclusive(false, true)

	_checks_rp_controller.set_rp_module_exclusive(_checks_rp_controls(), open)
	_rp_submenu_open = open

	if defer_hub_refresh:
		return
	_apply_hub_visibility_for_modules()
	_refresh_rp_studio_ui()


func _apply_hub_visibility_for_modules() -> void:
	var in_hub := not _agent_submenu_open and not _checks_submenu_open and not _rp_submenu_open
	_set_hub_content_visible(in_hub)
	_apply_responsive_layout()


func _set_hub_content_visible(visible_state: bool) -> void:
	hub_top_band_panel.visible = visible_state
	hub_stage_panel.visible = visible_state
	hub_ops_panel.visible = visible_state
	hub_telemetry_panel.visible = visible_state and (_hub_show_sim_card or _hub_show_api_card or _hub_show_eval_card)
	hub_title_label.visible = visible_state
	hub_api_label.visible = visible_state
	hub_polling_label.visible = visible_state
	hub_queue_label.visible = visible_state
	hub_errors_label.visible = visible_state
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
	hub_replay_panel.visible = visible_state
	hub_chat_panel.visible = visible_state
	log_label.visible = visible_state
	rp_studio_panel.visible = _rp_submenu_open
	sim_card_panel.visible = visible_state and _hub_show_sim_card
	api_card_panel.visible = visible_state and _hub_show_api_card
	eval_card_panel.visible = visible_state and _hub_show_eval_card


func _apply_agent_module_layout(exclusive_open: bool) -> void:
	_agent_studio_controller.apply_module_layout(_agent_studio_controls(), exclusive_open)


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
	_hub_config_controller.refresh_ui(
		_hub_config_controls(),
		_hub_show_sim_card,
		_hub_show_api_card,
		_hub_show_eval_card,
		_hub_default_panel,
		_hub_refresh_profile,
		_hub_config_collapsed,
		_HUB_DEFAULT_PANEL_OPTIONS,
		_HUB_REFRESH_PROFILE_OPTIONS
	)
	_set_marquee_text(hub_config_status_label, "Refresh=%s | default=%s" % [_hub_refresh_profile, _hub_default_panel])


func _set_hub_config_collapsed(collapsed: bool) -> void:
	_hub_config_collapsed = collapsed
	_hub_config_controller.set_collapsed(
		_hub_config_controls(),
		collapsed,
		_HUB_CONFIG_COLLAPSED_HEIGHT,
		_HUB_CONFIG_EXPANDED_BOTTOM - 44.0
	)
	_apply_responsive_layout()


func _generate_hub_session_id() -> String:
	return "sim-hub-%s" % Time.get_datetime_string_from_system(false, true).replace(":", "").replace("-", "").replace(" ", "_")


func _persist_hub_session_state() -> void:
	if _hub_chat_session_id.strip_edges() == "":
		return
	_save_hub_preferences(true)


func _load_hub_preferences() -> void:
	var values: Dictionary = _hub_preferences_store.load_preferences(
		_HUB_PREFS_PATH,
		{
			"show_sim_card": _hub_show_sim_card,
			"show_api_card": _hub_show_api_card,
			"show_eval_card": _hub_show_eval_card,
			"default_panel": _hub_default_panel,
			"refresh_profile": _hub_refresh_profile,
			"session_id": _hub_chat_session_id,
			"scene_id": _hub_chat_scene_id,
			"resume_checkpoint_id": _live_session_resume_checkpoint_id,
			"selected_replay_checkpoint_id": _hub_selected_replay_checkpoint_id,
		}
	)
	_hub_show_sim_card = bool(values.get("show_sim_card", _hub_show_sim_card))
	_hub_show_api_card = bool(values.get("show_api_card", _hub_show_api_card))
	_hub_show_eval_card = bool(values.get("show_eval_card", _hub_show_eval_card))
	_hub_default_panel = str(values.get("default_panel", _hub_default_panel))
	_hub_refresh_profile = str(values.get("refresh_profile", _hub_refresh_profile))
	_hub_chat_session_id = str(values.get("session_id", _hub_chat_session_id)).strip_edges()
	_hub_chat_scene_id = str(values.get("scene_id", _hub_chat_scene_id)).strip_edges()
	_live_session_resume_checkpoint_id = str(values.get("resume_checkpoint_id", _live_session_resume_checkpoint_id)).strip_edges()
	_hub_selected_replay_checkpoint_id = str(values.get("selected_replay_checkpoint_id", _hub_selected_replay_checkpoint_id)).strip_edges()


func _save_hub_preferences(silent: bool = false) -> void:
	var err := _hub_preferences_store.save_preferences(
		_HUB_PREFS_PATH,
		{
			"show_sim_card": _hub_show_sim_card,
			"show_api_card": _hub_show_api_card,
			"show_eval_card": _hub_show_eval_card,
			"default_panel": _hub_default_panel,
			"refresh_profile": _hub_refresh_profile,
			"session_id": _hub_chat_session_id,
			"scene_id": _hub_chat_scene_id,
			"resume_checkpoint_id": _live_session_resume_checkpoint_id,
			"selected_replay_checkpoint_id": _hub_selected_replay_checkpoint_id,
		}
	)
	if err == OK:
		if not silent:
			hub_config_status_label.text = "Gespeichert: %s" % _HUB_PREFS_PATH
			_append_runtime_event("HUB_CONFIG", {"action": "save", "status": "ok", "path": _HUB_PREFS_PATH})
	else:
		if not silent:
			hub_config_status_label.text = "Speichern fehlgeschlagen (err=%d)" % err
		_append_runtime_event("HUB_CONFIG", {"action": "save", "status": "failed", "err": err})


func _apply_hub_preferences() -> void:
	_set_refresh_profile(_hub_refresh_profile)
	_apply_hub_visibility_for_modules()
	_apply_card_visibility_now()
	_refresh_hub_config_ui()


func _apply_card_visibility_now() -> void:
	var in_hub := not _agent_submenu_open and not _checks_submenu_open and not _rp_submenu_open
	_hub_config_controller.apply_card_visibility(
		_hub_config_controls(),
		in_hub,
		_hub_show_sim_card,
		_hub_show_api_card,
		_hub_show_eval_card
	)


func _set_refresh_profile(profile: String) -> void:
	var resolved: Dictionary = _hub_config_controller.resolve_refresh_profile(profile)
	_hub_refresh_profile = str(resolved.get("profile", "normal"))
	metrics_refresh_interval_seconds = float(resolved.get("metrics_interval", 4.0))
	eval_summary_refresh_interval_seconds = float(resolved.get("eval_interval", 8.0))


func _cycle_refresh_profile() -> void:
	_set_refresh_profile(_hub_config_controller.cycle_refresh_profile(_hub_refresh_profile))


func _cycle_default_panel() -> void:
	_hub_default_panel = _hub_config_controller.cycle_default_panel(_hub_default_panel)


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
	hub_config_status_label.text = _hub_config_controller.toggle_card_status("Sim Card", _hub_show_sim_card, _agent_submenu_open, _checks_submenu_open)


func _on_hub_config_api_card_pressed() -> void:
	_hub_show_api_card = not _hub_show_api_card
	_apply_hub_preferences()
	hub_config_status_label.text = _hub_config_controller.toggle_card_status("API Card", _hub_show_api_card, _agent_submenu_open, _checks_submenu_open)


func _on_hub_config_eval_card_pressed() -> void:
	_hub_show_eval_card = not _hub_show_eval_card
	_apply_hub_preferences()
	hub_config_status_label.text = _hub_config_controller.toggle_card_status("Eval Card", _hub_show_eval_card, _agent_submenu_open, _checks_submenu_open)


func _on_hub_config_default_panel_selected(index: int) -> void:
	_hub_default_panel = _hub_config_controller.resolve_selected_option(index, _HUB_DEFAULT_PANEL_OPTIONS, _hub_default_panel)
	_refresh_hub_config_ui()


func _on_hub_config_refresh_selected(index: int) -> void:
	_set_refresh_profile(_hub_config_controller.resolve_selected_option(index, _HUB_REFRESH_PROFILE_OPTIONS, _hub_refresh_profile))
	_apply_hub_preferences()


func _hub_config_controls() -> Dictionary:
	return {
		"hub_telemetry_panel": hub_telemetry_panel,
		"sim_card_panel": sim_card_panel,
		"api_card_panel": api_card_panel,
		"eval_card_panel": eval_card_panel,
		"hub_config_panel": hub_config_panel,
		"hub_config_sim_card_button": hub_config_sim_card_button,
		"hub_config_api_card_button": hub_config_api_card_button,
		"hub_config_eval_card_button": hub_config_eval_card_button,
		"hub_config_default_panel_button": hub_config_default_panel_button,
		"hub_config_refresh_button": hub_config_refresh_button,
		"hub_config_save_button": hub_config_save_button,
		"hub_config_status_label": hub_config_status_label,
		"hub_config_close_button": hub_config_close_button,
	}


func _refresh_checks_studio_ui() -> void:
	_checks_rp_controller.refresh_checks_ui(_checks_rp_controls(), _checks_target, _checks_type, _checks_running)


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
	_request_live_session_replay()
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
	var request_state: Dictionary = _hub_chat_controller.request_chat(
		hub_chat_input_edit.text,
		hub_chat_request,
		_hub_request_host(),
		_hub_request_port(),
		hub_chat_profile_id,
		_hub_chat_session_id,
		_hub_chat_campaign_id,
		_hub_chat_scene_id,
		_hub_chat_turn_index,
		_current_slot,
		_hub_chat_current_scene_text,
		_hub_chat_current_consequence,
		_hub_chat_current_options
	)
	if not bool(request_state.get("started", false)):
		_hub_chat_pending_turn_id = str(request_state.get("pending_turn_id", "")).strip_edges()
		hub_chat_status_label.text = str(request_state.get("message", hub_chat_status_label.text))
		var detail_line := str(request_state.get("detail_line", "")).strip_edges()
		if detail_line != "":
			_append_hub_chat_line("System", detail_line)
		return

	_hub_chat_pending_turn_id = str(request_state.get("pending_turn_id", "")).strip_edges()
	_hub_chat_scene_id = str(request_state.get("scene_id", _hub_chat_scene_id))
	_hub_chat_public_context = str(request_state.get("public_context", _hub_chat_public_context))
	hub_chat_send_button.disabled = true
	hub_chat_input_edit.editable = false
	hub_chat_status_label.text = "Live-Spielclient: sende an %s" % str(request_state.get("endpoint", _hub_chat_endpoint()))
	_append_hub_chat_line("Du", str(request_state.get("prompt", "")))
	hub_chat_input_edit.clear()
	_append_runtime_event("HUB_CHAT", request_state.get("event", {}))


func _hub_chat_endpoint() -> String:
	return _hub_chat_controller.build_endpoint(_hub_request_host(), _hub_request_port())


func _on_hub_chat_request_completed(result: int, response_code: int, _headers: PackedStringArray, body: PackedByteArray) -> void:
	hub_chat_send_button.disabled = false
	hub_chat_input_edit.editable = true
	var completion_state: Dictionary = _hub_chat_controller.complete_chat_request(result, response_code, body)
	if str(completion_state.get("status", "")) == "ok":
		var answer := str(completion_state.get("answer", "")).strip_edges()
		_append_hub_chat_line("SL", answer)
		_apply_hub_chat_response(answer)
		_request_live_session_state()
		_request_live_session_replay()
		hub_chat_status_label.text = str(completion_state.get("status_text", "Live-Spielclient: Antwort ok"))
	else:
		_hub_chat_pending_turn_id = str(completion_state.get("pending_turn_id", "")).strip_edges()
		var detail_line := str(completion_state.get("detail_line", "")).strip_edges()
		if detail_line != "":
			_append_hub_chat_line("System", detail_line)
		hub_chat_status_label.text = str(completion_state.get("status_text", "Live-Spielclient: Fehler"))

	_append_runtime_event("HUB_CHAT", completion_state.get("event", {}))


func _on_hub_session_request_completed(result: int, response_code: int, _headers: PackedStringArray, body: PackedByteArray) -> void:
	var completion_state: Dictionary = _session_replay_request_controller.complete_live_session(
		result,
		response_code,
		body,
		_hub_chat_session_id
	)
	if str(completion_state.get("status", "")) != "ok":
		_set_marquee_text(epoch_status_label, str(completion_state.get("message", "Epochen: Session-Sync fehlgeschlagen")))
		_append_runtime_event("SESSION_SYNC", completion_state.get("event", {}))
		return
	_apply_live_session_state(completion_state.get("payload", {}))
	_append_runtime_event("SESSION_SYNC", completion_state.get("event", {}))


func _on_hub_replay_fetch_pressed() -> void:
	_request_live_session_replay()


func _on_hub_replay_apply_pressed() -> void:
	_apply_selected_replay_checkpoint()


func _on_hub_replay_checkpoint_selected(index: int) -> void:
	if hub_replay_checkpoint_button.is_disabled():
		return
	if index < 0 or index >= hub_replay_checkpoint_button.item_count:
		return
	_hub_selected_replay_checkpoint_id = hub_replay_checkpoint_button.get_item_text(index)
	_persist_hub_session_state()
	_refresh_hub_replay_ui()


func _on_hub_replay_request_completed(result: int, response_code: int, _headers: PackedStringArray, body: PackedByteArray) -> void:
	var completion_state: Dictionary = _session_replay_request_controller.complete_live_replay(
		result,
		response_code,
		body,
		_hub_chat_session_id,
		_live_session_resume_checkpoint_id,
		_hub_selected_replay_checkpoint_id
	)
	if str(completion_state.get("status", "")) != "ok":
		hub_replay_status_label.text = str(completion_state.get("message", "Replay: Sync fehlgeschlagen"))
		_append_runtime_event("SESSION_REPLAY", completion_state.get("event", {}))
		return
	var updates: Dictionary = _session_replay_state_controller.build_replay_manifest_state(
		completion_state.get("manifest", {}),
		_live_session_resume_checkpoint_id,
		_hub_selected_replay_checkpoint_id
	)
	_apply_session_replay_state_updates(updates)
	_refresh_hub_replay_ui()
	_append_runtime_event("SESSION_REPLAY", completion_state.get("event", {}))


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
	var toggle_state: Dictionary = _checks_rp_controller.toggle_checks_panel(_checks_submenu_open, _checks_target, _checks_type)
	_set_checks_module_exclusive(bool(toggle_state.get("open", false)))
	_update_checks_menu_ui()
	_update_agent_menu_ui()
	audio_status_label.text = str(toggle_state.get("audio_status", audio_status_label.text))
	_append_runtime_event("CHECKS_UI", toggle_state.get("event", {}))
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
	var updates: Dictionary = _checks_rp_controller.apply_rp_hour_plus(_loaded_epochs, _current_slot)
	if str(updates.get("status", "")) != "ok":
		rp_status_label.text = str(updates.get("rp_status", "RP: keine Epochen geladen"))
		return
	_current_slot = int(updates.get("current_slot", _current_slot))
	_render_pc_centric_view()
	rp_status_label.text = str(updates.get("rp_status", rp_status_label.text))
	_append_runtime_event("RP_HOUR_JUMP", updates.get("event", {}))


func _on_rp_auto_advance_pressed() -> void:
	var updates: Dictionary = _checks_rp_controller.toggle_rp_auto_advance(_rp_auto_advance, Time.get_ticks_msec())
	_rp_auto_advance = bool(updates.get("enabled", _rp_auto_advance))
	if updates.has("last_auto_advance_ms"):
		_rp_last_auto_advance_ms = int(updates.get("last_auto_advance_ms", _rp_last_auto_advance_ms))
	_refresh_rp_studio_ui()
	_append_runtime_event("RP_AUTO_ADVANCE", updates.get("event", {"enabled": _rp_auto_advance}))


func _refresh_rp_studio_ui() -> void:
	_checks_rp_controller.refresh_rp_ui(
		_checks_rp_controls(),
		_last_world_state,
		_live_session_resume_checkpoint_id,
		_current_slot,
		_rp_auto_advance
	)


func _checks_rp_controls() -> Dictionary:
	return {
		"checks_studio_panel": checks_studio_panel,
		"checks_back_button": checks_back_button,
		"checks_target_sim_button": checks_target_sim_button,
		"checks_target_agent_button": checks_target_agent_button,
		"checks_target_eval_button": checks_target_eval_button,
		"checks_target_workspace_button": checks_target_workspace_button,
		"checks_type_smoke_button": checks_type_smoke_button,
		"checks_type_unit_button": checks_type_unit_button,
		"checks_type_api_button": checks_type_api_button,
		"checks_type_lint_button": checks_type_lint_button,
		"checks_type_full_button": checks_type_full_button,
		"checks_run_selected_button": checks_run_selected_button,
		"checks_run_module_pack_button": checks_run_module_pack_button,
		"checks_status_label": checks_status_label,
		"rp_studio_panel": rp_studio_panel,
		"rp_back_button": rp_back_button,
		"rp_hour_plus_button": rp_hour_plus_button,
		"rp_auto_advance_button": rp_auto_advance_button,
		"rp_replay_seed_label": rp_replay_seed_label,
		"rp_status_label": rp_status_label,
	}


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
	var form_state := _agent_form_controller.open_form(
		kind,
		{
			"dataset_source_mode": _dataset_source_mode,
			"finetune_profile": _finetune_profile,
			"finetune_output_name": _finetune_output_name,
			"active_profile_name": _active_profile_name,
			"active_profile_mode": _active_profile_mode,
		}
	)
	_agent_form_kind = str(form_state.get("form_kind", kind))
	_agent_form_mode_value = str(form_state.get("form_mode_value", _agent_form_mode_value))
	_agent_form_target_value = str(form_state.get("form_target_value", _agent_form_target_value))
	_agent_form_template_signature = ""
	_agent_form_controls.clear()
	agent_form_name_edit.text = str(form_state.get("form_name", "")).strip_edges()

	_refresh_agent_form_ui()


func _on_agent_form_mode_selected(index: int) -> void:
	if _form_dropdowns_syncing:
		return
	var options := _agent_form_controller.mode_options_for_kind(_agent_form_kind)
	if index < 0 or index >= options.size():
		return
	_agent_form_mode_value = options[index]
	_refresh_agent_form_ui()


func _on_agent_form_target_selected(index: int) -> void:
	if _form_dropdowns_syncing:
		return
	var options := _agent_form_controller.target_options_for_kind(_agent_form_kind)
	if index < 0 or index >= options.size():
		return
	_agent_form_target_value = options[index]
	_refresh_agent_form_ui()


func _on_agent_form_apply_pressed() -> void:
	if _agent_form_kind == "":
		return
	var payload_result := _agent_authoring_payload_controller.build_form_payload(_agent_authoring_payload_state())
	var payload_updates_any = payload_result.get("updates", {})
	if typeof(payload_updates_any) == TYPE_DICTIONARY:
		var payload_updates: Dictionary = payload_updates_any
		if payload_updates.has("form_status_text"):
			agent_form_status_label.text = str(payload_updates.get("form_status_text", agent_form_status_label.text))
	var payload_any = payload_result.get("payload", {})
	if typeof(payload_any) != TYPE_DICTIONARY:
		return
	var payload: Dictionary = payload_any
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


func _apply_dataset_form_payload(payload: Dictionary) -> void:
	var result := _agent_authoring_persistence_controller.apply_dataset_form_payload(payload, _agent_authoring_persistence_state())
	_apply_agent_authoring_persistence_result(result)


func _apply_synonym_form_payload(payload: Dictionary) -> void:
	var result := _agent_authoring_persistence_controller.apply_synonym_form_payload(payload, _agent_authoring_persistence_state())
	_apply_agent_authoring_persistence_result(result)


func _apply_finetune_form_payload(payload: Dictionary) -> void:
	var result := _agent_runtime_controller.apply_finetune_form_payload(payload, _agent_runtime_state())
	_apply_agent_runtime_result(result)


func _apply_profile_form_payload(payload: Dictionary) -> void:
	var result := _agent_authoring_persistence_controller.apply_profile_form_payload(payload, _agent_authoring_persistence_state())
	_apply_agent_authoring_persistence_result(result)


func _apply_advanced_settings_form_payload(payload: Dictionary) -> void:
	var result := _agent_authoring_persistence_controller.apply_advanced_settings_form_payload(payload, _agent_authoring_persistence_state())
	_apply_agent_authoring_persistence_result(result)


func _apply_jobs_form_payload(payload: Dictionary) -> void:
	var runtime_payload := payload.duplicate(true)
	if not runtime_payload.has("target"):
		runtime_payload["target"] = _agent_form_target_value
	if not runtime_payload.has("job_name"):
		runtime_payload["job_name"] = agent_form_name_edit.text
	if not runtime_payload.has("job_type"):
		runtime_payload["job_type"] = _agent_form_mode_value
	var result := _agent_runtime_controller.apply_jobs_form_payload(runtime_payload, _agent_runtime_state())
	_apply_agent_runtime_result(result)


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
	var form_state := _agent_form_controller.refresh_form_ui(
		_agent_form_ui_controls(),
		{
			"agent_submenu_open": _agent_submenu_open,
			"studio_mode": _agent_studio_mode,
			"form_kind": _agent_form_kind,
			"form_mode_value": _agent_form_mode_value,
			"form_target_value": _agent_form_target_value,
			"template_signature": _agent_form_template_signature,
			"form_controls": _agent_form_controls,
			"active_dataset_tag": _active_dataset_tag,
			"active_synonym_tag": _active_synonym_tag,
			"finetune_base_model": _finetune_base_model,
		}
	)
	_agent_form_mode_value = str(form_state.get("form_mode_value", _agent_form_mode_value))
	_agent_form_target_value = str(form_state.get("form_target_value", _agent_form_target_value))
	_agent_form_template_signature = str(form_state.get("template_signature", _agent_form_template_signature))
	_agent_form_controls = form_state.get("form_controls", _agent_form_controls)


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
	var result := _agent_runtime_controller.handle_eval_run(_agent_runtime_state())
	_apply_agent_runtime_result(result)
	_refresh_agent_studio_ui()


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
		var stop_result := _agent_runtime_controller.handle_finetune_stop(_agent_runtime_state())
		_apply_agent_runtime_result(stop_result)
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
	_agent_studio_controller.refresh_studio_ui(_agent_studio_controls(), _agent_studio_state())


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
	var result := _agent_registry_state_controller.load_dataset_registry_state(_agent_registry_state())
	_apply_agent_registry_state_result(result)


func _load_synonym_registry_state() -> void:
	var result := _agent_registry_state_controller.load_synonym_registry_state(_agent_registry_state())
	_apply_agent_registry_state_result(result)


func _load_profile_registry_state() -> void:
	var result := _agent_registry_state_controller.load_profile_registry_state(_agent_registry_state())
	_apply_agent_registry_state_result(result)


func _load_advanced_settings_state() -> void:
	var result := _agent_registry_state_controller.load_advanced_settings_state(_agent_registry_state())
	_apply_agent_registry_state_result(result)


func _load_jobs_state() -> void:
	_jobs_status_text = "Jobs: idle"
	var result := _agent_runtime_controller.load_jobs_state(_JOBS_QUEUE_PATH)
	_apply_agent_runtime_result(result)


func _load_security_model_state() -> void:
	var result := _agent_registry_state_controller.load_security_model_state(_agent_registry_state())
	_apply_agent_registry_state_result(result)


func _persist_security_model_state() -> void:
	_agent_registry_state_controller.persist_security_model_state(_agent_registry_state())


func _confirm_destructive_action(action_key: String, hint_text: String) -> bool:
	var result := _agent_runtime_controller.confirm_destructive_action(_agent_runtime_state(), action_key, hint_text)
	_apply_agent_runtime_result(result)
	return bool(result.get("confirmed", false))


func _refresh_agent_restpoint_summaries() -> void:
	var result := _agent_restpoint_summary_controller.refresh_agent_restpoint_summaries(_agent_restpoint_summary_state())
	_apply_agent_restpoint_summary_result(result)


func _refresh_finetune_runtime_state() -> void:
	var result := _agent_runtime_controller.refresh_finetune_runtime_state(_agent_runtime_state())
	_apply_agent_runtime_result(result)


func _refresh_eval_runtime_state() -> void:
	var result := _agent_runtime_controller.refresh_eval_runtime_state(_agent_runtime_state())
	_apply_agent_runtime_result(result)


func _refresh_latest_eval_summary(force: bool) -> void:
	var result := _runtime_telemetry_controller.refresh_latest_eval_summary(_runtime_telemetry_state(), force)
	_apply_runtime_telemetry_result(result)


func _build_ai_trend_summary(pcts: Array[float], avg_duration_values: Array[float]) -> String:
	return _runtime_telemetry_controller.build_ai_trend_summary(pcts, avg_duration_values)


func _refresh_system_metrics(force: bool) -> void:
	var result := _runtime_telemetry_controller.refresh_system_metrics(_runtime_telemetry_state(), force)
	_apply_runtime_telemetry_result(result)


func _format_percent(value: float) -> String:
	return _runtime_telemetry_controller.format_percent(value)


func _format_temperature(value_c: float) -> String:
	return _runtime_telemetry_controller.format_temperature(value_c)


func _format_vram() -> String:
	return _runtime_telemetry_controller.format_vram(_runtime_telemetry_state())


func _effective_temperature_c() -> float:
	return _runtime_telemetry_controller.effective_temperature_c(_runtime_telemetry_state())


func _to_float_or_default(value, default_value: float) -> float:
	if value is float:
		return value
	if value is int:
		return float(value)
	if value is String and value.is_valid_float():
		return value.to_float()
	return default_value


func _start_local_server() -> void:
	var result := _hub_server_ops_controller.start_local_server(_server_ops_state())
	_apply_server_ops_result(result)


func _stop_local_server() -> void:
	var result := _hub_server_ops_controller.stop_local_server(_server_ops_state())
	_apply_server_ops_result(result)


func _update_server_control_ui() -> void:
	var result := _hub_server_ops_controller.update_server_control_ui(_server_ops_state(), _derive_health_state(_sim_runtime_status()))
	_apply_server_ops_result(result)


func _resolve_python_executable() -> String:
	return _runtime_telemetry_controller.resolve_python_executable(_runtime_telemetry_state())


func _refresh_server_runtime_state() -> void:
	var result := _hub_server_ops_controller.refresh_server_runtime_state(_server_ops_state())
	_apply_server_ops_result(result)


func _is_external_server_reachable() -> bool:
	return _runtime_telemetry_controller.is_external_server_reachable(_runtime_telemetry_state(), _sim_runtime_status())


func _append_runtime_event(tag: String, payload: Dictionary) -> void:
	var result := _runtime_audit_controller.append_runtime_event(_runtime_audit_state(), tag, payload)
	_apply_runtime_audit_result(result)


func _append_audit_event(tag: String, payload: Dictionary) -> void:
	var result := _runtime_audit_controller.append_audit_event(_runtime_audit_state(), tag, payload)
	_apply_runtime_audit_result(result)


func _runtime_event_rate_per_second() -> float:
	return _runtime_audit_controller.runtime_event_rate_per_second(_runtime_audit_state())


func _trim_runtime_event_rate_window() -> void:
	var result := _runtime_audit_controller.trim_runtime_event_rate_window(_runtime_audit_state())
	_apply_runtime_audit_result(result)


func _extract_error_code(message: String) -> String:
	return _runtime_audit_controller.extract_error_code(message)


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
