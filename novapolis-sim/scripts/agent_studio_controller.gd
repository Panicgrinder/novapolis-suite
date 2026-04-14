extends RefCounted

class_name AgentStudioController


func set_module_exclusive_ui(controls: Dictionary, open: bool) -> void:
	(controls.get("agent_studio_panel") as Control).visible = open
	(controls.get("agent_back_button") as Control).visible = open
	for key in [
		"agent_operate_button",
		"agent_author_button",
		"agent_eval_run_button",
		"agent_datasets_button",
		"agent_synonyms_button",
		"agent_finetune_button",
		"agent_profiles_button",
		"agent_ai_status_button",
	]:
		(controls.get(key) as BaseButton).disabled = not open


func apply_module_layout(controls: Dictionary, exclusive_open: bool) -> void:
	var agent_studio_panel := controls.get("agent_studio_panel") as Control
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

		_set_rect(controls.get("agent_back_button") as Control, right - 210.0, 10.0, right, 42.0)
		_set_rect(controls.get("agent_studio_mode_label") as Control, left, 56.0, right, 76.0)
		_set_rect(controls.get("agent_operate_button") as Control, col1_left, 88.0, col1_right, 132.0)
		_set_rect(controls.get("agent_author_button") as Control, col2_left, 88.0, col2_right, 132.0)
		_set_rect(controls.get("agent_dataset_source_button") as Control, col3_left, 88.0, col3_right, 132.0)
		_set_rect(controls.get("agent_eval_suite_button") as Control, col3_left, 46.0, col3_right, 80.0)
		_set_rect(controls.get("agent_eval_run_button") as Control, col1_left, 152.0, col1_right, 196.0)
		_set_rect(controls.get("agent_datasets_button") as Control, col2_left, 152.0, col2_right, 196.0)
		_set_rect(controls.get("agent_synonyms_button") as Control, col3_left, 152.0, col3_right, 196.0)
		_set_rect(controls.get("agent_finetune_button") as Control, col1_left, 212.0, col1_right, 256.0)
		_set_rect(controls.get("agent_profiles_button") as Control, col2_left, 212.0, col2_right, 256.0)
		_set_rect(controls.get("agent_ai_status_button") as Control, col3_left, 212.0, col3_right, 256.0)
		_set_rect(controls.get("agent_eval_status_label") as Control, left, 286.0, right, 306.0)
		_set_rect(controls.get("agent_system_metrics_label") as Control, left, 320.0, right, 340.0)
		_set_rect(controls.get("agent_latest_runs_label") as Control, left, 356.0, right, 376.0)

		var form_top := clampf(panel_height * 0.49, 430.0, 560.0)
		_set_rect(controls.get("agent_studio_hint_label") as Control, left, form_top - 40.0, right, form_top - 20.0)
		_set_rect(controls.get("agent_form_panel") as Control, left, form_top, right, panel_height - 18.0)
		return

	_set_rect(controls.get("agent_studio_mode_label") as Control, 10.0, 30.0, 10.0, 30.0)
	_set_rect(controls.get("agent_operate_button") as Control, 10.0, 54.0, 184.0, 88.0)
	_set_rect(controls.get("agent_author_button") as Control, 196.0, 54.0, 370.0, 88.0)
	_set_rect(controls.get("agent_dataset_source_button") as Control, 380.0, 54.0, 564.0, 88.0)

	var compact_right := agent_studio_panel.offset_right - agent_studio_panel.offset_left - 10.0
	_set_rect(controls.get("agent_back_button") as Control, compact_right - 170.0, 6.0, compact_right, 34.0)
	_set_rect(controls.get("agent_eval_suite_button") as Control, compact_right - 184.0, 38.0, compact_right, 68.0)
	_set_rect(controls.get("agent_eval_run_button") as Control, 10.0, 104.0, 280.0, 138.0)
	_set_rect(controls.get("agent_datasets_button") as Control, 294.0, 104.0, 564.0, 138.0)
	_set_rect(controls.get("agent_synonyms_button") as Control, 10.0, 148.0, 280.0, 182.0)
	_set_rect(controls.get("agent_finetune_button") as Control, 294.0, 148.0, 564.0, 182.0)
	_set_rect(controls.get("agent_profiles_button") as Control, 10.0, 192.0, 280.0, 226.0)
	_set_rect(controls.get("agent_ai_status_button") as Control, 294.0, 192.0, 564.0, 226.0)
	_set_rect(controls.get("agent_eval_status_label") as Control, 10.0, 246.0, 10.0, 246.0)
	_set_rect(controls.get("agent_system_metrics_label") as Control, 10.0, 278.0, 10.0, 278.0)
	_set_rect(controls.get("agent_latest_runs_label") as Control, 10.0, 316.0, 10.0, 316.0)
	_set_rect(controls.get("agent_studio_hint_label") as Control, 10.0, 390.0, 10.0, 390.0)
	_set_rect(controls.get("agent_form_panel") as Control, 10.0, 422.0, 564.0, 402.0)


func refresh_studio_ui(controls: Dictionary, state: Dictionary) -> Dictionary:
	var mode := str(state.get("studio_mode", "operate"))
	(controls.get("agent_studio_mode_label") as Label).text = "Modus: %s" % mode.capitalize()

	var eval_pid := int(state.get("eval_pid", -1))
	var last_eval_exit_code := int(state.get("last_eval_exit_code", -1))
	var now_ms := int(state.get("now_ms", Time.get_ticks_msec()))
	var eval_text := "Eval: idle"
	if eval_pid > 0:
		var elapsed_s := maxf(0.0, float(now_ms - int(state.get("eval_started_ms", now_ms))) / 1000.0)
		var expected_s := maxf(1.0, float(state.get("eval_expected_duration_seconds", 25.0)))
		var progress := mini(95, int((elapsed_s / expected_s) * 100.0))
		eval_text = "Eval: running [%s] (%d%%, ~%.1fs)" % [str(state.get("agent_eval_suite", "neutral")), progress, elapsed_s]
	elif last_eval_exit_code == 0:
		eval_text = "Eval: done (100%)"
	elif last_eval_exit_code > 0:
		eval_text = "Eval: failed (exit=%d)" % last_eval_exit_code
	(controls.get("agent_eval_status_label") as Label).text = eval_text

	if bool(state.get("enable_system_resource_monitoring", false)):
		(controls.get("agent_system_metrics_label") as Label).text = str(state.get("system_metrics_text", "System: n/a"))
	else:
		(controls.get("agent_system_metrics_label") as Label).text = "System: Monitoring deaktiviert (testweise)"

	var full_status_text := "• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n• %s\n• %s\n• %s" % [
		str(state.get("dataset_status_text", "Datasets: idle")),
		str(state.get("active_dataset_label", "Active Dataset: n/a")),
		str(state.get("synonym_status_text", "Synonyms: idle")),
		str(state.get("active_synonym_label", "Active Synonyms: n/a")),
		str(state.get("profile_status_text", "Profiles: idle")),
		str(state.get("active_profile_label", "Active Profile: n/a")),
		str(state.get("advanced_settings_status_text", "Advanced: idle")),
		str(state.get("jobs_status_text", "Jobs: idle")),
		str(state.get("finetune_status_text", "Finetune: idle")),
		str(state.get("latest_eval_summary_text", "Letzte Eval-Runs: n/a")),
		str(state.get("ai_trend_summary_text", "Trendkarte: n/a")),
		str(state.get("artifacts_summary_text", "Artifacts: n/a")),
		str(state.get("experiments_summary_text", "Experiments: n/a")),
		str(state.get("policy_sandbox_summary_text", "Policy Sandbox: n/a")),
		str(state.get("release_gate_summary_text", "Release Gate: n/a")),
		str(state.get("audit_trail_summary_text", "Audit Trail: n/a")),
		str(state.get("security_model_summary_text", "Security: guarded")),
	]
	var compact_status_text := "• %s\n• %s\n\n• %s\n• %s\n\n• %s\n• %s\n• %s" % [
		str(state.get("dataset_status_text", "Datasets: idle")),
		str(state.get("active_dataset_label", "Active Dataset: n/a")),
		str(state.get("jobs_status_text", "Jobs: idle")),
		str(state.get("synonym_status_text", "Synonyms: idle")),
		str(state.get("latest_eval_summary_text", "Letzte Eval-Runs: n/a")),
		str(state.get("release_gate_summary_text", "Release Gate: n/a")),
		str(state.get("security_model_summary_text", "Security: guarded")),
	]

	_select_option_value(
		controls.get("agent_eval_suite_button") as OptionButton,
		state.get("eval_suite_options", []) as Array[String],
		str(state.get("agent_eval_suite", "neutral"))
	)
	_select_option_value(
		controls.get("agent_dataset_source_button") as OptionButton,
		state.get("dataset_source_options", []) as Array[String],
		str(state.get("dataset_source_mode", "clean"))
	)

	var agent_submenu_open := bool(state.get("agent_submenu_open", false))
	var hint_base_top := 362.0
	if agent_submenu_open:
		hint_base_top = 430.0

	var agent_form_kind := str(state.get("agent_form_kind", ""))
	var form_should_show := agent_submenu_open and mode == "author" and (agent_form_kind == "datasets" or agent_form_kind == "synonyms" or agent_form_kind == "finetune" or agent_form_kind == "profiles" or agent_form_kind == "advanced" or agent_form_kind == "jobs")
	var collapse_status_block := form_should_show and bool(state.get("collapse_agent_status_when_form_open", true))

	var agent_latest_runs_label := controls.get("agent_latest_runs_label") as Label
	agent_latest_runs_label.text = compact_status_text if collapse_status_block else full_status_text

	var agent_eval_status_label := controls.get("agent_eval_status_label") as Control
	var agent_system_metrics_label := controls.get("agent_system_metrics_label") as Control
	var agent_form_panel := controls.get("agent_form_panel") as Control
	if collapse_status_block:
		agent_eval_status_label.visible = false
		agent_system_metrics_label.visible = false
		agent_latest_runs_label.modulate = state.get("agent_status_dim_tint", Color(0.78, 0.82, 0.88, 1.0))
		agent_form_panel.self_modulate = state.get("agent_form_panel_active_tint", Color(0.93, 0.97, 1.0, 1.0))
		if agent_submenu_open:
			agent_latest_runs_label.offset_top = 282.0
			agent_latest_runs_label.offset_bottom = 282.0
		else:
			agent_latest_runs_label.offset_top = 242.0
			agent_latest_runs_label.offset_bottom = 242.0
	else:
		agent_eval_status_label.visible = true
		agent_system_metrics_label.visible = true
		agent_latest_runs_label.modulate = state.get("agent_status_normal_tint", Color(0.95, 0.95, 0.9, 1.0))
		agent_form_panel.self_modulate = state.get("agent_form_panel_normal_tint", Color(1.0, 1.0, 1.0, 1.0))
		if agent_submenu_open:
			agent_latest_runs_label.offset_top = 356.0
			agent_latest_runs_label.offset_bottom = 356.0
		else:
			agent_latest_runs_label.offset_top = 316.0
			agent_latest_runs_label.offset_bottom = 316.0

	var latest_runs_lines: int = maxi(1, agent_latest_runs_label.get_line_count())
	var line_step := 22.0 if collapse_status_block else 24.0
	var hint_height := 26.0
	var hint_top := maxf(hint_base_top, agent_latest_runs_label.offset_top + (float(latest_runs_lines) * line_step) + 14.0)
	var hint_max_top := (controls.get("agent_studio_panel") as Control).offset_bottom - 30.0 - hint_height
	hint_top = minf(hint_top, hint_max_top)

	var agent_studio_hint_label := controls.get("agent_studio_hint_label") as Label
	agent_studio_hint_label.visible = false
	agent_studio_hint_label.offset_top = hint_top
	agent_studio_hint_label.offset_bottom = hint_top + hint_height

	if form_should_show:
		var form_bottom := (controls.get("agent_studio_panel") as Control).offset_bottom - 22.0
		var min_form_height := 300.0
		var desired_top := hint_top + 28.0
		if desired_top + min_form_height > form_bottom:
			desired_top = maxf(96.0, form_bottom - min_form_height)
		agent_form_panel.offset_top = desired_top
		agent_form_panel.offset_bottom = form_bottom

	if mode == "operate":
		(controls.get("agent_eval_run_button") as Button).text = "Eval Stop" if eval_pid > 0 else "Eval Start"
		if int(state.get("dataset_pid", -1)) > 0:
			(controls.get("agent_datasets_button") as Button).text = "Datasets Stop"
		else:
			(controls.get("agent_datasets_button") as Button).text = "Datasets Form [%s]" % str(state.get("dataset_source_mode_label", "Nur erfolgreiche"))
		if int(state.get("finetune_pid", -1)) > 0:
			(controls.get("agent_finetune_button") as Button).text = "Finetune Stop"
		else:
			(controls.get("agent_finetune_button") as Button).text = "Finetune Start"
		(controls.get("agent_profiles_button") as Button).text = "Profiles Form"
		(controls.get("agent_ai_status_button") as Button).text = "AI Status"
	else:
		(controls.get("agent_eval_run_button") as Button).text = "Jobs Config"
		if int(state.get("dataset_pid", -1)) > 0:
			(controls.get("agent_datasets_button") as Button).text = "Datasets Stop"
		else:
			(controls.get("agent_datasets_button") as Button).text = "Datasets Konfig [%s]" % str(state.get("dataset_source_mode_label", "Nur erfolgreiche"))
		if int(state.get("finetune_pid", -1)) > 0:
			(controls.get("agent_finetune_button") as Button).text = "Finetune Stop"
		else:
			(controls.get("agent_finetune_button") as Button).text = "Finetune Config"
		(controls.get("agent_profiles_button") as Button).text = "Profiles Config"
		(controls.get("agent_ai_status_button") as Button).text = "Advanced + Gate"

	var destructive_armed_action := str(state.get("destructive_armed_action", ""))
	if destructive_armed_action != "" and now_ms <= int(state.get("destructive_armed_until_ms", -1)):
		agent_studio_hint_label.visible = true
		agent_studio_hint_label.text = "Sicherheits-Gate aktiv: Aktion '%s' innerhalb 8s erneut bestaetigen" % destructive_armed_action
	else:
		agent_studio_hint_label.text = ""

	var disabled := bool(state.get("agent_action_busy", false)) or not agent_submenu_open
	(controls.get("agent_datasets_button") as BaseButton).disabled = disabled
	(controls.get("agent_synonyms_button") as BaseButton).disabled = disabled
	(controls.get("agent_finetune_button") as BaseButton).disabled = disabled
	(controls.get("agent_profiles_button") as BaseButton).disabled = disabled
	(controls.get("agent_ai_status_button") as BaseButton).disabled = disabled
	(controls.get("agent_eval_suite_button") as BaseButton).disabled = eval_pid > 0 or not agent_submenu_open
	(controls.get("agent_dataset_source_button") as BaseButton).disabled = int(state.get("dataset_pid", -1)) > 0 or not agent_submenu_open

	return {"form_should_show": form_should_show}


func _set_rect(control: Control, left: float, top: float, right: float, bottom: float) -> void:
	control.offset_left = left
	control.offset_top = top
	control.offset_right = right
	control.offset_bottom = bottom


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