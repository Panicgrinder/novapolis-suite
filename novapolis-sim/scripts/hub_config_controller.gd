extends RefCounted

class_name HubConfigController


func refresh_ui(
	controls: Dictionary,
	_hub_show_sim_card: bool,
	hub_show_api_card: bool,
	hub_show_eval_card: bool,
	hub_default_panel: String,
	hub_refresh_profile: String,
	hub_config_collapsed: bool,
	default_panel_options: Array[String],
	refresh_profile_options: Array[String],
	server_autostart_enabled: bool
) -> void:
	var hub_config_sim_card_button := controls.get("hub_config_sim_card_button") as Button
	var hub_config_api_card_button := controls.get("hub_config_api_card_button") as Button
	var hub_config_eval_card_button := controls.get("hub_config_eval_card_button") as Button
	var hub_config_default_panel_button := controls.get("hub_config_default_panel_button") as OptionButton
	var hub_config_refresh_button := controls.get("hub_config_refresh_button") as OptionButton
	var hub_config_close_button := controls.get("hub_config_close_button") as Button
	# Keep the sim/api/eval card toggles hidden (telemetry cards fixed visible elsewhere).
	if hub_config_sim_card_button != null:
		hub_config_sim_card_button.visible = false
	var hub_config_autostart_checkbox := controls.get("hub_config_autostart_checkbox") as CheckBox
	if hub_config_autostart_checkbox != null:
		hub_config_autostart_checkbox.set_pressed(server_autostart_enabled)
		hub_config_autostart_checkbox.visible = true
	if hub_config_api_card_button != null:
		hub_config_api_card_button.text = _select_label("API", hub_show_api_card)
		hub_config_api_card_button.visible = false
	if hub_config_eval_card_button != null:
		hub_config_eval_card_button.text = _select_label("Eval", hub_show_eval_card)
		hub_config_eval_card_button.visible = false
	_select_option_value(hub_config_default_panel_button, default_panel_options, hub_default_panel)
	_select_option_value(hub_config_refresh_button, refresh_profile_options, hub_refresh_profile)
	hub_config_close_button.text = "Öffnen" if hub_config_collapsed else "Minimieren"


func set_collapsed(controls: Dictionary, collapsed: bool, collapsed_height: float, expanded_height: float) -> void:
	var show_body := not collapsed
	for key in [
		"hub_config_default_panel_button",
		"hub_config_refresh_button",
		"hub_config_save_button",
		"hub_config_status_label",
	]:
		var control := controls.get(key) as Control
		control.visible = show_body
	var hub_config_panel := controls.get("hub_config_panel") as Control
	if collapsed:
		hub_config_panel.offset_bottom = hub_config_panel.offset_top + collapsed_height
	else:
		hub_config_panel.offset_bottom = hub_config_panel.offset_top + expanded_height
	var hub_config_close_button := controls.get("hub_config_close_button") as Button
	hub_config_close_button.text = "Öffnen" if collapsed else "Minimieren"


func apply_card_visibility(controls: Dictionary, in_hub: bool, show_sim: bool, show_api: bool, show_eval: bool) -> void:
	var hub_telemetry_panel := controls.get("hub_telemetry_panel") as Control
	var sim_card_panel := controls.get("sim_card_panel") as Control
	var api_card_panel := controls.get("api_card_panel") as Control
	var eval_card_panel := controls.get("eval_card_panel") as Control
	hub_telemetry_panel.visible = in_hub and (show_sim or show_api or show_eval)
	sim_card_panel.visible = in_hub and show_sim
	api_card_panel.visible = in_hub and show_api
	eval_card_panel.visible = in_hub and show_eval


func resolve_refresh_profile(profile: String) -> Dictionary:
	match profile:
		"fast":
			return {"profile": "fast", "metrics_interval": 2.0, "eval_interval": 4.0}
		"slow":
			return {"profile": "slow", "metrics_interval": 8.0, "eval_interval": 12.0}
		_:
			return {"profile": "normal", "metrics_interval": 4.0, "eval_interval": 8.0}


func cycle_refresh_profile(current_profile: String) -> String:
	if current_profile == "normal":
		return "fast"
	if current_profile == "fast":
		return "slow"
	return "normal"


func cycle_default_panel(current_panel: String) -> String:
	if current_panel == "hub":
		return "agent"
	if current_panel == "agent":
		return "checks"
	return "hub"


func resolve_selected_option(index: int, options: Array[String], current_value: String) -> String:
	if index < 0 or index >= options.size():
		return current_value
	return options[index]


func toggle_card_status(card_name: String, next_visible: bool, agent_open: bool, checks_open: bool) -> String:
	if card_name == "Eval Card" and (agent_open or checks_open):
		return "Eval Card gespeichert: %s (sichtbar im Hub)" % ("an" if next_visible else "aus")
	return "%s: %s" % [card_name, ("sichtbar" if next_visible else "ausgeblendet")]


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


func _select_label(base: String, selected: bool) -> String:
	if selected:
		return "[x] %s" % base
	return "[ ] %s" % base