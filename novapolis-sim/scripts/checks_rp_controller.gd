extends RefCounted

class_name ChecksRpController


func set_checks_module_exclusive(controls: Dictionary, open: bool, checks_running: bool) -> void:
	var checks_studio_panel := controls.get("checks_studio_panel") as Control
	var checks_back_button := controls.get("checks_back_button") as Control
	checks_studio_panel.visible = open
	checks_back_button.visible = open
	for key in [
		"checks_target_sim_button",
		"checks_target_agent_button",
		"checks_target_eval_button",
		"checks_target_workspace_button",
		"checks_type_smoke_button",
		"checks_type_unit_button",
		"checks_type_api_button",
		"checks_type_lint_button",
		"checks_type_full_button",
		"checks_run_selected_button",
		"checks_run_module_pack_button",
	]:
		var button := controls.get(key) as BaseButton
		button.disabled = checks_running or not open


func set_rp_module_exclusive(controls: Dictionary, open: bool) -> void:
	var rp_studio_panel := controls.get("rp_studio_panel") as Control
	var rp_back_button := controls.get("rp_back_button") as Control
	var rp_hour_plus_button := controls.get("rp_hour_plus_button") as BaseButton
	var rp_auto_advance_button := controls.get("rp_auto_advance_button") as BaseButton
	rp_studio_panel.visible = open
	rp_back_button.visible = open
	rp_hour_plus_button.disabled = not open
	rp_auto_advance_button.disabled = not open


func refresh_checks_ui(controls: Dictionary, checks_target: String, checks_type: String, checks_running: bool) -> void:
	(controls.get("checks_target_sim_button") as Button).text = _select_label("Sim", checks_target == "sim")
	(controls.get("checks_target_agent_button") as Button).text = _select_label("Agent/API", checks_target == "agent")
	(controls.get("checks_target_eval_button") as Button).text = _select_label("Eval/Training", checks_target == "eval")
	(controls.get("checks_target_workspace_button") as Button).text = _select_label("Workspace", checks_target == "workspace")
	(controls.get("checks_type_smoke_button") as Button).text = _select_label("Smoke", checks_type == "smoke")
	(controls.get("checks_type_unit_button") as Button).text = _select_label("Unit", checks_type == "unit")
	(controls.get("checks_type_api_button") as Button).text = _select_label("API/Integration", checks_type == "api")
	(controls.get("checks_type_lint_button") as Button).text = _select_label("Lint/Type", checks_type == "lint")
	(controls.get("checks_type_full_button") as Button).text = _select_label("Full", checks_type == "full")
	(controls.get("checks_run_selected_button") as BaseButton).disabled = checks_running
	(controls.get("checks_run_module_pack_button") as BaseButton).disabled = checks_running
	var checks_status_label := controls.get("checks_status_label") as Label
	if checks_running:
		checks_status_label.text = "Checks: running..."
	else:
		checks_status_label.text = "Checks: target=%s | type=%s" % [checks_target, checks_type]


func toggle_checks_panel(current_open: bool, checks_target: String, checks_type: String) -> Dictionary:
	var next_open := not current_open
	if next_open:
		return {
			"open": true,
			"audio_status": "Checks-Modul: geöffnet",
			"event": {"status": "opened", "target": checks_target, "type": checks_type},
		}
	return {
		"open": false,
		"audio_status": "Checks-Modul: geschlossen",
		"event": {"status": "closed"},
	}


func toggle_rp_panel(current_open: bool, rp_auto_advance: bool) -> Dictionary:
	var next_open := not current_open
	if next_open:
		return {
			"open": true,
			"audio_status": "RP-Modul: geoeffnet",
			"event": {"action": "toggle", "status": "opened", "auto_advance": rp_auto_advance},
		}
	return {
		"open": false,
		"audio_status": "Hub-Modus aktiv",
		"event": {"action": "toggle", "status": "closed"},
	}


func target_value(target: String) -> String:
	return target


func type_value(check_type: String) -> String:
	return check_type


func apply_rp_hour_plus(loaded_epochs: Array, current_slot: int) -> Dictionary:
	if loaded_epochs.is_empty():
		return {"status": "empty", "rp_status": "RP: keine Epochen geladen"}
	var next_slot := (current_slot + 1) % 24
	return {
		"status": "ok",
		"current_slot": next_slot,
		"rp_status": "RP: Hour +1 (%02d -> %02d)" % [current_slot, next_slot],
		"event": {"from": current_slot, "to": next_slot},
	}


func toggle_rp_auto_advance(current_enabled: bool, now_ms: int) -> Dictionary:
	var next_enabled := not current_enabled
	var updates := {"enabled": next_enabled}
	if next_enabled:
		updates["last_auto_advance_ms"] = now_ms
	updates["event"] = {"enabled": next_enabled}
	return updates


func refresh_rp_ui(controls: Dictionary, last_world_state: Dictionary, live_session_resume_checkpoint_id: String, current_slot: int, rp_auto_advance: bool) -> void:
	var rp_replay_seed_label := controls.get("rp_replay_seed_label") as Label
	if last_world_state.has("sim_meta") and typeof(last_world_state.get("sim_meta")) == TYPE_DICTIONARY:
		var sim_meta: Dictionary = last_world_state.get("sim_meta", {})
		if live_session_resume_checkpoint_id != "":
			rp_replay_seed_label.text = "Replay-Seed: %s" % live_session_resume_checkpoint_id
		else:
			rp_replay_seed_label.text = "Replay-Seed: %s" % str(sim_meta.get("seed", "n/a"))
	else:
		if live_session_resume_checkpoint_id != "":
			rp_replay_seed_label.text = "Replay-Seed: %s" % live_session_resume_checkpoint_id
		else:
			rp_replay_seed_label.text = "Replay-Seed: n/a"
	(controls.get("rp_auto_advance_button") as Button).text = _select_label("Auto-Advance", rp_auto_advance)
	(controls.get("rp_status_label") as Label).text = "RP: slot=%02d | auto=%s" % [current_slot, str(rp_auto_advance)]


func _select_label(base: String, selected: bool) -> String:
	if selected:
		return "[x] %s" % base
	return "[ ] %s" % base