extends RefCounted

class_name HubLayoutController


func get_safe_viewport_size(viewport_size: Vector2, min_width: float, min_height: float) -> Vector2:
	return Vector2(maxf(viewport_size.x, min_width), maxf(viewport_size.y, min_height))


func apply_responsive_hub_layout(controls: Dictionary, state: Dictionary, width: float, height: float) -> void:
	if bool(state.get("preserve_editor_hub_layout", false)) and not bool(state.get("agent_submenu_open", false)) and not bool(state.get("checks_submenu_open", false)) and not bool(state.get("rp_submenu_open", false)):
		_apply_editor_hub_layout(controls, state, width, height)
		return
	_layout_hub_shells(controls, state, width, height)
	_layout_hub_topbar(controls, state, width)
	_layout_hub_actions(controls, state, width, height)
	_layout_hub_log_and_cards(controls, state, width, height)


func _set_control_rect(control: Control, left: float, top: float, right: float, bottom: float) -> void:
	control.offset_left = left
	control.offset_top = top
	control.offset_right = right
	control.offset_bottom = bottom


func _scale_hub_x(value: float, width: float, base_width: float) -> float:
	return value * (width / base_width)


func _scale_hub_y(value: float, height: float, base_height: float) -> float:
	return value * (height / base_height)


func _hub_cards_shell_height(height: float) -> float:
	return clampf(height * 0.22, 196.0, 248.0)


func _hub_cards_shell_top(height: float, ui_margin: float) -> float:
	return height - ui_margin - _hub_cards_shell_height(height)


func _hub_content_top() -> float:
	return 132.0


func _hub_ops_rect(state: Dictionary, width: float, height: float) -> Rect2:
	var top := _hub_content_top()
	var bottom := _hub_cards_shell_top(height, float(state.get("ui_margin", 16.0))) - float(state.get("ui_gap", 12.0))
	var ui_margin := float(state.get("ui_margin", 16.0))
	var shell_width := clampf(width * 0.28, 320.0, 430.0)
	return Rect2(
		width - ui_margin - shell_width,
		top,
		shell_width,
		maxf(260.0, bottom - top)
	)


func _hub_stage_rect(state: Dictionary, width: float, height: float) -> Rect2:
	var top := _hub_content_top()
	var bottom := _hub_cards_shell_top(height, float(state.get("ui_margin", 16.0))) - float(state.get("ui_gap", 12.0))
	var ops_rect := _hub_ops_rect(state, width, height)
	var ui_margin := float(state.get("ui_margin", 16.0))
	var ui_gap := float(state.get("ui_gap", 12.0))
	return Rect2(
		ui_margin,
		top,
		maxf(420.0, ops_rect.position.x - ui_margin - ui_gap),
		maxf(260.0, bottom - top)
	)


func _layout_hub_shells(controls: Dictionary, state: Dictionary, width: float, height: float) -> void:
	var ui_margin := float(state.get("ui_margin", 16.0))
	_set_control_rect(controls.get("hub_top_band_panel") as Control, ui_margin, 16.0, width - ui_margin, 100.0)
	var stage_rect := _hub_stage_rect(state, width, height)
	_set_control_rect(controls.get("hub_stage_panel") as Control, stage_rect.position.x, stage_rect.position.y, stage_rect.position.x + stage_rect.size.x, stage_rect.position.y + stage_rect.size.y)
	var ops_rect := _hub_ops_rect(state, width, height)
	_set_control_rect(controls.get("hub_ops_panel") as Control, ops_rect.position.x, ops_rect.position.y, ops_rect.position.x + ops_rect.size.x, ops_rect.position.y + ops_rect.size.y)
	_set_control_rect(controls.get("hub_telemetry_panel") as Control, ui_margin, _hub_cards_shell_top(height, ui_margin), width - ui_margin, height - ui_margin)


func _apply_editor_hub_layout(controls: Dictionary, state: Dictionary, width: float, height: float) -> void:
	var base_width := float(state.get("ui_base_width", 1920.0))
	var base_height := float(state.get("ui_base_height", 1080.0))
	var area_01_left := _scale_hub_x(98.0, width, base_width)
	var area_01_top := _scale_hub_y(117.0, height, base_height)
	var area_01_right := _scale_hub_x(497.0, width, base_width)
	var area_01_right_inner := area_01_right
	var area_02_left := _scale_hub_x(520.0, width, base_width)
	var area_02_top := _scale_hub_y(116.0, height, base_height)
	var area_02_right := _scale_hub_x(902.0, width, base_width)
	var area_02_bottom := _scale_hub_y(229.0, height, base_height)
	var area_03_left := _scale_hub_x(1018.0, width, base_width)
	var area_03_top := _scale_hub_y(117.0, height, base_height)
	var area_03_right := _scale_hub_x(1399.0, width, base_width)
	var area_04_left := _scale_hub_x(1424.0, width, base_width)
	var area_04_top := _scale_hub_y(116.0, height, base_height)
	var area_04_right := _scale_hub_x(1821.0, width, base_width)
	var area_04_bottom := _scale_hub_y(228.0, height, base_height)

	var inner_pad_x := _scale_hub_x(8.0, width, base_width)
	var inner_pad_y := _scale_hub_y(8.0, height, base_height)
	var area_01_line_h := _scale_hub_y(17.0, height, base_height)
	var area_01_line_gap := _scale_hub_y(2.0, height, base_height)
	var area_01_line_y := area_01_top + inner_pad_y

	_set_control_rect(controls.get("hub_title_label") as Control, area_01_left + inner_pad_x, area_01_line_y, area_01_right_inner - inner_pad_x, area_01_line_y + area_01_line_h)
	area_01_line_y += area_01_line_h + area_01_line_gap
	_set_control_rect(controls.get("hub_api_label") as Control, area_01_left + inner_pad_x, area_01_line_y, area_01_right_inner - inner_pad_x, area_01_line_y + area_01_line_h)
	area_01_line_y += area_01_line_h + area_01_line_gap
	_set_control_rect(controls.get("slot_label") as Control, area_01_left + inner_pad_x, area_01_line_y, area_01_right_inner - inner_pad_x, area_01_line_y + area_01_line_h)
	area_01_line_y += area_01_line_h + area_01_line_gap
	_set_control_rect(controls.get("audio_status_label") as Control, area_01_left + inner_pad_x, area_01_line_y, area_01_right_inner - inner_pad_x, area_01_line_y + area_01_line_h)
	area_01_line_y += area_01_line_h + area_01_line_gap
	_set_control_rect(controls.get("epoch_label") as Control, area_01_left + inner_pad_x, area_01_line_y, area_01_left + _scale_hub_x(110.0, width, base_width), area_01_line_y + area_01_line_h)
	_set_control_rect(controls.get("epoch_status_label") as Control, area_01_left + _scale_hub_x(114.0, width, base_width), area_01_line_y, area_01_right_inner - inner_pad_x, area_01_line_y + area_01_line_h)

	var action_pad := _scale_hub_x(10.0, width, base_width)
	var action_gap := _scale_hub_x(10.0, width, base_width)
	var action_inner_left := area_02_left + action_pad
	var action_inner_right := area_02_right - action_pad
	var action_width := maxf(_scale_hub_x(140.0, width, base_width), (action_inner_right - action_inner_left - action_gap) / 2.0)
	var action_top_row_top := area_02_top + inner_pad_y
	var action_top_row_bottom := action_top_row_top + _scale_hub_y(46.0, height, base_height)
	var action_bottom_row_top := action_top_row_bottom + _scale_hub_y(10.0, height, base_height)
	var action_bottom_row_bottom := area_02_bottom - inner_pad_y

	_set_control_rect(controls.get("play_pc_button") as Control, action_inner_left, action_top_row_top, action_inner_left + action_width, action_top_row_bottom)
	_set_control_rect(controls.get("play_world_button") as Control, action_inner_left + action_width + action_gap, action_top_row_top, action_inner_right, action_top_row_bottom)
	_set_control_rect(controls.get("hub_checks_button") as Control, action_inner_left, action_bottom_row_top, action_inner_left + action_width, action_bottom_row_bottom)
	_set_control_rect(controls.get("hub_reload_button") as Control, action_inner_left + action_width + action_gap, action_bottom_row_top, action_inner_right, action_bottom_row_bottom)

	var status_pad := _scale_hub_x(8.0, width, base_width)
	var status_left := area_03_left + status_pad
	var status_right := area_03_right - status_pad
	var status_line_h := _scale_hub_y(16.0, height, base_height)
	var status_gap := _scale_hub_y(2.0, height, base_height)
	var status_y := area_03_top + inner_pad_y

	_set_control_rect(controls.get("server_toggle_button") as Control, status_left, status_y, status_left + _scale_hub_x(148.0, width, base_width), status_y + _scale_hub_y(30.0, height, base_height))
	_set_control_rect(controls.get("server_status_label") as Control, status_left + _scale_hub_x(154.0, width, base_width), status_y, status_right, status_y + _scale_hub_y(30.0, height, base_height))
	status_y += _scale_hub_y(32.0, height, base_height)
	_set_control_rect(controls.get("hub_errors_label") as Control, status_left, status_y, status_right, status_y + status_line_h)
	status_y += status_line_h + status_gap
	_set_control_rect(controls.get("hub_queue_label") as Control, status_left, status_y, status_right, status_y + status_line_h)
	status_y += status_line_h + status_gap
	_set_control_rect(controls.get("hub_polling_label") as Control, status_left, status_y, status_right, status_y + status_line_h)
	status_y += status_line_h + status_gap
	_set_control_rect(controls.get("tick_label") as Control, status_left, status_y, status_left + _scale_hub_x(188.0, width, base_width), status_y + status_line_h)
	_set_control_rect(controls.get("time_label") as Control, status_left + _scale_hub_x(194.0, width, base_width), status_y, status_right, status_y + status_line_h)

	_set_control_rect(controls.get("hub_config_panel") as Control, area_04_left, area_04_top, area_04_right, area_04_bottom)
	_set_control_rect(controls.get("status_label") as Control, _scale_hub_x(20.0, width, base_width), _scale_hub_y(92.0, height, base_height), _scale_hub_x(1825.0, width, base_width), _scale_hub_y(114.0, height, base_height))
	_set_control_rect(controls.get("log_label") as Control, _scale_hub_x(99.0, width, base_width), _scale_hub_y(256.0, height, base_height), _scale_hub_x(897.0, width, base_width), _scale_hub_y(565.0, height, base_height))
	_set_control_rect(controls.get("hub_chat_panel") as Control, _scale_hub_x(1020.0, width, base_width), _scale_hub_y(255.0, height, base_height), _scale_hub_x(1820.0, width, base_width), _scale_hub_y(558.0, height, base_height))
	_layout_hub_chat_contents(controls)
	_set_control_rect(controls.get("sim_card_panel") as Control, _scale_hub_x(104.0, width, base_width), _scale_hub_y(824.0, height, base_height), _scale_hub_x(898.0, width, base_width), _scale_hub_y(1002.0, height, base_height))
	_set_control_rect(controls.get("api_card_panel") as Control, _scale_hub_x(552.0, width, base_width), _scale_hub_y(630.0, height, base_height), _scale_hub_x(1358.0, width, base_width), _scale_hub_y(801.0, height, base_height))
	_set_control_rect(controls.get("eval_card_panel") as Control, _scale_hub_x(1016.0, width, base_width), _scale_hub_y(826.0, height, base_height), _scale_hub_x(1822.0, width, base_width), _scale_hub_y(998.0, height, base_height))


func _layout_hub_topbar(controls: Dictionary, state: Dictionary, width: float) -> void:
	var hub_top_band_panel := controls.get("hub_top_band_panel") as Control
	var ui_gap := float(state.get("ui_gap", 12.0))
	var ui_margin := float(state.get("ui_margin", 16.0))
	var left := hub_top_band_panel.offset_left + 20.0
	var top := hub_top_band_panel.offset_top + 14.0
	var right := hub_top_band_panel.offset_right - 20.0
	var title_w := clampf(width * 0.17, 240.0, 320.0)
	var errors_w := clampf(width * 0.18, 190.0, 280.0)

	var hub_title_label := controls.get("hub_title_label") as Control
	hub_title_label.offset_left = left
	hub_title_label.offset_top = top
	hub_title_label.offset_right = left + title_w
	hub_title_label.offset_bottom = top + 24.0

	var hub_errors_label := controls.get("hub_errors_label") as Control
	hub_errors_label.offset_left = right - errors_w
	hub_errors_label.offset_top = top
	hub_errors_label.offset_right = right
	hub_errors_label.offset_bottom = top + 24.0

	var hub_api_label := controls.get("hub_api_label") as Control
	hub_api_label.offset_left = hub_title_label.offset_right + ui_gap
	hub_api_label.offset_top = top
	hub_api_label.offset_right = hub_errors_label.offset_left - ui_gap
	hub_api_label.offset_bottom = top + 24.0

	var row2_top := top + 34.0
	var chip_width := (right - left - ui_gap * 3.0) / 4.0

	var tick_label := controls.get("tick_label") as Control
	tick_label.offset_left = left
	tick_label.offset_top = row2_top
	tick_label.offset_right = left + chip_width
	tick_label.offset_bottom = row2_top + 22.0

	var time_label := controls.get("time_label") as Control
	time_label.offset_left = tick_label.offset_right + ui_gap
	time_label.offset_top = row2_top
	time_label.offset_right = time_label.offset_left + chip_width
	time_label.offset_bottom = row2_top + 22.0

	var hub_polling_label := controls.get("hub_polling_label") as Control
	hub_polling_label.offset_left = time_label.offset_right + ui_gap
	hub_polling_label.offset_top = row2_top
	hub_polling_label.offset_right = hub_polling_label.offset_left + chip_width
	hub_polling_label.offset_bottom = row2_top + 22.0

	var hub_queue_label := controls.get("hub_queue_label") as Control
	hub_queue_label.offset_left = hub_polling_label.offset_right + ui_gap
	hub_queue_label.offset_top = row2_top
	hub_queue_label.offset_right = right
	hub_queue_label.offset_bottom = row2_top + 22.0

	var status_label := controls.get("status_label") as Control
	status_label.offset_left = ui_margin
	status_label.offset_top = hub_top_band_panel.offset_bottom + 8.0
	status_label.offset_right = width - ui_margin
	status_label.offset_bottom = status_label.offset_top + 22.0

	var hub_config_quit_button := controls.get("hub_config_quit_button") as Control
	var hub_config_close_button := controls.get("hub_config_close_button") as Control
	if hub_config_quit_button != null:
		hub_config_quit_button.offset_left = right - 236.0
		hub_config_quit_button.offset_top = row2_top
		hub_config_quit_button.offset_right = right - 124.0
		hub_config_quit_button.offset_bottom = row2_top + 30.0
		hub_config_quit_button.visible = true
	if hub_config_close_button != null:
		hub_config_close_button.offset_left = right - 118.0
		hub_config_close_button.offset_top = row2_top
		hub_config_close_button.offset_right = right - 12.0
		hub_config_close_button.offset_bottom = row2_top + 30.0
		hub_config_close_button.visible = true


func _layout_hub_actions(controls: Dictionary, state: Dictionary, width: float, height: float) -> void:
	var ops_rect := _hub_ops_rect(state, width, height)
	var ui_gap := float(state.get("ui_gap", 12.0))
	var left := ops_rect.position.x + 18.0
	var right := ops_rect.position.x + ops_rect.size.x - 18.0
	var top := ops_rect.position.y + 56.0
	var col_width := (right - left - ui_gap) / 2.0

	_set_control_rect(controls.get("server_toggle_button") as Control, left, top, right, top + 40.0)
	_set_control_rect(controls.get("server_status_label") as Control, left, top + 48.0, right, top + 70.0)

	top += 86.0
	_set_control_rect(controls.get("play_pc_button") as Control, left, top, left + col_width, top + 40.0)
	_set_control_rect(controls.get("play_world_button") as Control, left + col_width + ui_gap, top, right, top + 40.0)

	top += 50.0
	_set_control_rect(controls.get("hub_checks_button") as Control, left, top, left + col_width, top + 40.0)
	_set_control_rect(controls.get("hub_reload_button") as Control, left + col_width + ui_gap, top, right, top + 40.0)

	_set_control_rect(controls.get("audio_status_label") as Control, left, top + 52.0, right, top + 74.0)


func _layout_hub_log_and_cards(controls: Dictionary, state: Dictionary, width: float, height: float) -> void:
	var ui_gap := float(state.get("ui_gap", 12.0))
	var stage_rect := _hub_stage_rect(state, width, height)
	var stage_left := stage_rect.position.x + 24.0
	var stage_right := stage_rect.position.x + stage_rect.size.x - 24.0
	var stage_header_top := stage_rect.position.y + 56.0

	_set_control_rect(controls.get("epoch_label") as Control, stage_left, stage_header_top, stage_left + 180.0, stage_header_top + 22.0)
	_set_control_rect(controls.get("slot_label") as Control, stage_left + 196.0, stage_header_top, stage_right, stage_header_top + 22.0)
	_set_control_rect(controls.get("epoch_status_label") as Control, stage_left, stage_header_top + 28.0, stage_right, stage_header_top + 50.0)
	_set_control_rect(controls.get("log_label") as Control, stage_left, stage_header_top + 66.0, stage_right, stage_rect.position.y + stage_rect.size.y - 22.0)

	var ops_rect := _hub_ops_rect(state, width, height)
	var audio_status_label := controls.get("audio_status_label") as Control
	var hub_replay_panel := controls.get("hub_replay_panel") as Control
	var hub_chat_panel := controls.get("hub_chat_panel") as Control
	var hub_config_panel := controls.get("hub_config_panel") as Control
	hub_replay_panel.clip_contents = true
	if hub_chat_panel != null:
		hub_chat_panel.clip_contents = true
	hub_config_panel.clip_contents = true

	# New: If settings-stage mode is active, occupy the stage area with the config panel
	# and collapse the usual terminal/log presentation.
	var settings_stage_mode := bool(state.get("settings_stage_mode", false))
	if settings_stage_mode:
		_set_control_rect(hub_config_panel, stage_left, stage_header_top, stage_right, stage_rect.position.y + stage_rect.size.y - 22.0)
		# Move log and other stage content out of view but keep layout stable.
		_set_control_rect(controls.get("log_label") as Control, stage_left, stage_header_top, stage_left, stage_header_top)
		# Keep replay/chat stacked to the right column collapsed.
		var ops_rect2 := _hub_ops_rect(state, width, height)
		_set_control_rect(hub_replay_panel, ops_rect2.position.x + 18.0, ops_rect2.position.y + 56.0, ops_rect2.position.x + 18.0, ops_rect2.position.y + 56.0)
		if hub_chat_panel != null:
			_set_control_rect(hub_chat_panel, ops_rect2.position.x + 18.0, ops_rect2.position.y + 56.0, ops_rect2.position.x + 18.0, ops_rect2.position.y + 56.0)
		return

	var column_left := ops_rect.position.x + 18.0
	var column_right := ops_rect.position.x + ops_rect.size.x - 18.0
	var stack_top := audio_status_label.offset_bottom + 16.0
	var stack_bottom := ops_rect.position.y + ops_rect.size.y - 18.0
	var stack_height := maxf(0.0, stack_bottom - stack_top)
	var stack_gap := 12.0
	var replay_pref_height := 160.0
	var replay_hard_min_height := 64.0
	var chat_visible := hub_chat_panel != null and hub_chat_panel.visible
	var replay_visible := hub_replay_panel != null and hub_replay_panel.visible
	var config_visible := hub_config_panel != null and hub_config_panel.visible

	if not chat_visible and not replay_visible and not config_visible:
		_set_control_rect(hub_replay_panel, column_left, stack_top, column_left, stack_top)
		_set_control_rect(hub_chat_panel, column_left, stack_top, column_left, stack_top)
		_set_control_rect(hub_config_panel, column_left, stack_top, column_left, stack_top)

		var hub_telemetry_panel_compact := controls.get("hub_telemetry_panel") as Control
		var cards_left_compact := hub_telemetry_panel_compact.offset_left + 18.0
		var cards_right_compact := hub_telemetry_panel_compact.offset_right - 18.0
		var cards_top_compact := hub_telemetry_panel_compact.offset_top + 72.0
		var cards_bottom_compact := hub_telemetry_panel_compact.offset_bottom - 18.0
		var card_width_compact := (cards_right_compact - cards_left_compact - ui_gap * 2.0) / 3.0

		_set_control_rect(controls.get("sim_card_panel") as Control, cards_left_compact, cards_top_compact, cards_left_compact + card_width_compact, cards_bottom_compact)
		var sim_card_panel_compact := controls.get("sim_card_panel") as Control
		_set_control_rect(controls.get("api_card_panel") as Control, sim_card_panel_compact.offset_right + ui_gap, cards_top_compact, sim_card_panel_compact.offset_right + ui_gap + card_width_compact, cards_bottom_compact)
		var api_card_panel_compact := controls.get("api_card_panel") as Control
		_set_control_rect(controls.get("eval_card_panel") as Control, api_card_panel_compact.offset_right + ui_gap, cards_top_compact, api_card_panel_compact.offset_right + ui_gap + card_width_compact, cards_bottom_compact)
		return

	if not chat_visible:
		var config_height_no_chat := clampf(hub_config_panel.offset_bottom - hub_config_panel.offset_top, 42.0, 134.0)
		var replay_height_no_chat := clampf(stack_height - config_height_no_chat - stack_gap, replay_hard_min_height, replay_pref_height)
		var replay_top_no_chat := stack_top
		var replay_bottom_no_chat := replay_top_no_chat + replay_height_no_chat
		_set_control_rect(hub_replay_panel, column_left, replay_top_no_chat, column_right, replay_bottom_no_chat)
		_layout_hub_replay_contents(controls)

		var config_top_no_chat := replay_bottom_no_chat + stack_gap
		_set_control_rect(hub_config_panel, column_left, config_top_no_chat, column_right, stack_bottom)

		_set_control_rect(hub_chat_panel, column_left, replay_bottom_no_chat, column_left, replay_bottom_no_chat)

		var hub_telemetry_panel_no_chat := controls.get("hub_telemetry_panel") as Control
		var cards_left_no_chat := hub_telemetry_panel_no_chat.offset_left + 18.0
		var cards_right_no_chat := hub_telemetry_panel_no_chat.offset_right - 18.0
		var cards_top_no_chat := hub_telemetry_panel_no_chat.offset_top + 30.0
		var cards_bottom_no_chat := hub_telemetry_panel_no_chat.offset_bottom - 18.0
		var card_width_no_chat := (cards_right_no_chat - cards_left_no_chat - ui_gap * 2.0) / 3.0

		_set_control_rect(controls.get("sim_card_panel") as Control, cards_left_no_chat, cards_top_no_chat, cards_left_no_chat + card_width_no_chat, cards_bottom_no_chat)
		var sim_card_panel_no_chat := controls.get("sim_card_panel") as Control
		_set_control_rect(controls.get("api_card_panel") as Control, sim_card_panel_no_chat.offset_right + ui_gap, cards_top_no_chat, sim_card_panel_no_chat.offset_right + ui_gap + card_width_no_chat, cards_bottom_no_chat)
		var api_card_panel_no_chat := controls.get("api_card_panel") as Control
		_set_control_rect(controls.get("eval_card_panel") as Control, api_card_panel_no_chat.offset_right + ui_gap, cards_top_no_chat, api_card_panel_no_chat.offset_right + ui_gap + card_width_no_chat, cards_bottom_no_chat)
		return

	var chat_pref_height := 180.0
	var chat_min_height := 120.0
	var config_min_height := 42.0
	var config_pref_height := maxf(config_min_height, hub_config_panel.offset_bottom - hub_config_panel.offset_top)

	var config_height := config_pref_height
	var min_for_replay_and_chat := replay_hard_min_height + chat_min_height + stack_gap * 2.0
	if config_height + min_for_replay_and_chat > stack_height:
		config_height = maxf(config_min_height, stack_height - min_for_replay_and_chat)
	config_height = minf(config_height, stack_height)

	var replay_and_chat_height := maxf(0.0, stack_height - config_height - stack_gap * 2.0)
	var replay_height := clampf(replay_and_chat_height - chat_pref_height, replay_hard_min_height, replay_pref_height)
	var chat_height := maxf(0.0, replay_and_chat_height - replay_height)
	if chat_height < chat_min_height and config_height > config_min_height:
		var missing := chat_min_height - chat_height
		var reduce_config := minf(missing, config_height - config_min_height)
		config_height -= reduce_config
		replay_and_chat_height = maxf(0.0, stack_height - config_height - stack_gap * 2.0)
		replay_height = clampf(replay_and_chat_height - chat_pref_height, replay_hard_min_height, replay_pref_height)
		chat_height = maxf(0.0, replay_and_chat_height - replay_height)
	if chat_height < chat_min_height and replay_height > replay_hard_min_height:
		var shift := minf(chat_min_height - chat_height, replay_height - replay_hard_min_height)
		replay_height -= shift
		chat_height = maxf(0.0, replay_and_chat_height - replay_height)

	var replay_top := stack_top
	var replay_bottom := replay_top + replay_height
	_set_control_rect(hub_replay_panel, column_left, replay_top, column_right, replay_bottom)
	_layout_hub_replay_contents(controls)

	var config_bottom := stack_bottom
	var config_top := config_bottom - config_height
	_set_control_rect(hub_config_panel, column_left, config_top, column_right, config_bottom)

	var chat_top := replay_bottom + stack_gap
	var chat_bottom := config_top - stack_gap
	if chat_bottom < chat_top:
		chat_bottom = chat_top
	_set_control_rect(hub_chat_panel, column_left, chat_top, column_right, chat_bottom)
	_layout_hub_chat_contents(controls)

	var hub_telemetry_panel := controls.get("hub_telemetry_panel") as Control
	var cards_left := hub_telemetry_panel.offset_left + 18.0
	var cards_right := hub_telemetry_panel.offset_right - 18.0
	var cards_top := hub_telemetry_panel.offset_top + 72.0
	var cards_bottom := hub_telemetry_panel.offset_bottom - 18.0
	var card_width := (cards_right - cards_left - ui_gap * 2.0) / 3.0

	_set_control_rect(controls.get("sim_card_panel") as Control, cards_left, cards_top, cards_left + card_width, cards_bottom)
	var sim_card_panel := controls.get("sim_card_panel") as Control
	_set_control_rect(controls.get("api_card_panel") as Control, sim_card_panel.offset_right + ui_gap, cards_top, sim_card_panel.offset_right + ui_gap + card_width, cards_bottom)
	var api_card_panel := controls.get("api_card_panel") as Control
	_set_control_rect(controls.get("eval_card_panel") as Control, api_card_panel.offset_right + ui_gap, cards_top, api_card_panel.offset_right + ui_gap + card_width, cards_bottom)


func _layout_hub_chat_contents(controls: Dictionary) -> void:
	var hub_chat_panel := controls.get("hub_chat_panel") as Control
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

	var hub_chat_history_label := controls.get("hub_chat_history_label") as Control
	hub_chat_history_label.offset_left = pad
	hub_chat_history_label.offset_top = 30.0
	hub_chat_history_label.offset_right = panel_w - pad
	hub_chat_history_label.offset_bottom = maxf(64.0, history_bottom)

	var hub_chat_input_edit := controls.get("hub_chat_input_edit") as Control
	hub_chat_input_edit.offset_left = pad
	hub_chat_input_edit.offset_top = input_top
	hub_chat_input_edit.offset_right = panel_w - pad - send_w - 8.0
	hub_chat_input_edit.offset_bottom = input_top + input_h

	var hub_chat_send_button := controls.get("hub_chat_send_button") as Control
	hub_chat_send_button.offset_left = hub_chat_input_edit.offset_right + 8.0
	hub_chat_send_button.offset_top = input_top
	hub_chat_send_button.offset_right = panel_w - pad
	hub_chat_send_button.offset_bottom = input_top + input_h

	var hub_chat_status_label := controls.get("hub_chat_status_label") as Control
	hub_chat_status_label.offset_left = pad
	hub_chat_status_label.offset_top = hub_chat_input_edit.offset_bottom + 4.0
	hub_chat_status_label.offset_right = panel_w - pad
	hub_chat_status_label.offset_bottom = hub_chat_status_label.offset_top + status_h

	var chat_title := controls.get("hub_chat_title_label") as Control
	if chat_title != null:
		chat_title.offset_left = pad
		chat_title.offset_top = title_top
		chat_title.offset_right = panel_w - pad
		chat_title.offset_bottom = title_bottom


func _layout_hub_replay_contents(controls: Dictionary) -> void:
	var hub_replay_panel := controls.get("hub_replay_panel") as Control
	var panel_w := maxf(220.0, hub_replay_panel.offset_right - hub_replay_panel.offset_left)
	var pad := 10.0
	var button_gap := 8.0
	var button_w := (panel_w - pad * 2.0 - button_gap) / 2.0
	var title := controls.get("hub_replay_title_label") as Control
	var checkpoint_label := controls.get("hub_replay_checkpoint_label") as Control
	if title != null:
		title.offset_left = pad
		title.offset_top = 8.0
		title.offset_right = panel_w - pad
		title.offset_bottom = 26.0
	if checkpoint_label != null:
		checkpoint_label.offset_left = pad
		checkpoint_label.offset_top = 56.0
		checkpoint_label.offset_right = panel_w - pad
		checkpoint_label.offset_bottom = 76.0
	var hub_replay_summary_label := controls.get("hub_replay_summary_label") as Control
	hub_replay_summary_label.offset_left = pad
	hub_replay_summary_label.offset_top = 30.0
	hub_replay_summary_label.offset_right = panel_w - pad
	hub_replay_summary_label.offset_bottom = 50.0
	var hub_replay_checkpoint_button := controls.get("hub_replay_checkpoint_button") as Control
	hub_replay_checkpoint_button.offset_left = pad
	hub_replay_checkpoint_button.offset_top = 80.0
	hub_replay_checkpoint_button.offset_right = panel_w - pad
	hub_replay_checkpoint_button.offset_bottom = 110.0
	var hub_replay_fetch_button := controls.get("hub_replay_fetch_button") as Control
	hub_replay_fetch_button.offset_left = pad
	hub_replay_fetch_button.offset_top = 118.0
	hub_replay_fetch_button.offset_right = pad + button_w
	hub_replay_fetch_button.offset_bottom = 148.0
	var hub_replay_apply_button := controls.get("hub_replay_apply_button") as Control
	hub_replay_apply_button.offset_left = hub_replay_fetch_button.offset_right + button_gap
	hub_replay_apply_button.offset_top = 118.0
	hub_replay_apply_button.offset_right = panel_w - pad
	hub_replay_apply_button.offset_bottom = 148.0
	var hub_replay_status_label := controls.get("hub_replay_status_label") as Control
	hub_replay_status_label.offset_left = pad
	hub_replay_status_label.offset_top = 154.0
	hub_replay_status_label.offset_right = panel_w - pad
	hub_replay_status_label.offset_bottom = 176.0


func _layout_hub_config_panel(controls: Dictionary, state: Dictionary, width: float, height: float) -> void:
	var ops_rect := _hub_ops_rect(state, width, height)
	var left := ops_rect.position.x + 18.0
	var right := ops_rect.position.x + ops_rect.size.x - 18.0
	var bottom := ops_rect.position.y + ops_rect.size.y - 18.0
	var collapsed_height := float(state.get("hub_config_collapsed_height", 42.0))
	var expanded_height := float(state.get("hub_config_expanded_height", 220.0))
	var panel_height := collapsed_height
	if not bool(state.get("hub_config_collapsed", false)):
		panel_height = expanded_height
	var hub_config_panel := controls.get("hub_config_panel") as Control
	_set_control_rect(hub_config_panel, left, bottom - panel_height, right, bottom)

	var panel_width := right - left
	var hub_config_title_label := controls.get("hub_config_title_label") as Control
	hub_config_title_label.offset_left = 14.0
	hub_config_title_label.offset_top = 10.0
	hub_config_title_label.offset_right = panel_width - 250.0
	hub_config_title_label.offset_bottom = 32.0

	var hub_config_quit_button := controls.get("hub_config_quit_button") as Control
	hub_config_quit_button.offset_left = panel_width - 236.0
	hub_config_quit_button.offset_top = 10.0
	hub_config_quit_button.offset_right = panel_width - 124.0
	hub_config_quit_button.offset_bottom = 40.0

	var hub_config_close_button := controls.get("hub_config_close_button") as Control
	hub_config_close_button.offset_left = panel_width - 118.0
	hub_config_close_button.offset_top = 10.0
	hub_config_close_button.offset_right = panel_width - 12.0
	hub_config_close_button.offset_bottom = 40.0

	var hub_config_sim_card_button := controls.get("hub_config_sim_card_button") as Control
	hub_config_sim_card_button.offset_left = 12.0
	hub_config_sim_card_button.offset_top = 54.0
	hub_config_sim_card_button.offset_right = 118.0
	hub_config_sim_card_button.offset_bottom = 84.0

	var hub_config_api_card_button := controls.get("hub_config_api_card_button") as Control
	hub_config_api_card_button.offset_left = 12.0
	hub_config_api_card_button.offset_top = 90.0
	hub_config_api_card_button.offset_right = 118.0
	hub_config_api_card_button.offset_bottom = 120.0

	var hub_config_eval_card_button := controls.get("hub_config_eval_card_button") as Control
	hub_config_eval_card_button.offset_left = 12.0
	hub_config_eval_card_button.offset_top = 126.0
	hub_config_eval_card_button.offset_right = 118.0
	hub_config_eval_card_button.offset_bottom = 156.0

	var hub_config_default_panel_button := controls.get("hub_config_default_panel_button") as Control
	hub_config_default_panel_button.offset_left = 136.0
	hub_config_default_panel_button.offset_top = 54.0
	hub_config_default_panel_button.offset_right = panel_width - 136.0
	hub_config_default_panel_button.offset_bottom = 84.0

	var hub_config_refresh_button := controls.get("hub_config_refresh_button") as Control
	hub_config_refresh_button.offset_left = 136.0
	hub_config_refresh_button.offset_top = 92.0
	hub_config_refresh_button.offset_right = panel_width - 136.0
	hub_config_refresh_button.offset_bottom = 122.0

	var hub_config_save_button := controls.get("hub_config_save_button") as Control
	hub_config_save_button.offset_left = panel_width - 126.0
	hub_config_save_button.offset_top = 126.0
	hub_config_save_button.offset_right = panel_width - 12.0
	hub_config_save_button.offset_bottom = 156.0

	var hub_config_status_label := controls.get("hub_config_status_label") as Control
	hub_config_status_label.offset_left = 12.0
	hub_config_status_label.offset_top = 162.0
	hub_config_status_label.offset_right = panel_width - 12.0
	hub_config_status_label.offset_bottom = 182.0
