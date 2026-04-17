extends RefCounted

class_name AgentRegistryStateController


func load_dataset_registry_state(state: Dictionary) -> Dictionary:
	var updates: Dictionary = {
		"active_dataset_name": "",
		"active_dataset_tag": "",
	}
	var registry := _load_json_dictionary(str(state.get("dataset_registry_path", "")))
	if registry.is_empty():
		return {"updates": updates}
	var active_name := str(registry.get("active_dataset", ""))
	var active_tag := str(registry.get("active_tag", ""))
	updates["active_dataset_name"] = active_name
	updates["active_dataset_tag"] = active_tag
	if active_name != "":
		updates["dataset_status_text"] = "Datasets: active %s" % _dataset_label(active_name, active_tag)
	return {"updates": updates}


func load_synonym_registry_state(state: Dictionary) -> Dictionary:
	var updates: Dictionary = {
		"active_synonym_set": "",
		"active_synonym_tag": "",
	}
	var registry := _load_json_dictionary(str(state.get("synonym_registry_path", "")))
	if registry.is_empty():
		return {"updates": updates}
	var active_set := str(registry.get("active_set", ""))
	var active_tag := str(registry.get("active_tag", ""))
	updates["active_synonym_set"] = active_set
	updates["active_synonym_tag"] = active_tag
	if active_set != "":
		updates["synonym_status_text"] = "Synonyms: active %s" % _synonym_label(active_set, active_tag)
	return {"updates": updates}


func load_profile_registry_state(state: Dictionary) -> Dictionary:
	var updates: Dictionary = {
		"active_profile_name": "",
		"active_profile_mode": "",
	}
	var registry := _load_json_dictionary(str(state.get("profile_registry_path", "")))
	if registry.is_empty():
		return {"updates": updates}
	var active_name := str(registry.get("active_profile", ""))
	var active_mode := str(registry.get("active_mode", ""))
	updates["active_profile_name"] = active_name
	updates["active_profile_mode"] = active_mode
	if active_name != "":
		updates["profile_status_text"] = "Profiles: active %s" % _profile_label(active_name, active_mode)
	return {"updates": updates}


func load_advanced_settings_state(state: Dictionary) -> Dictionary:
	var updates: Dictionary = {
		"advanced_settings_status_text": "Advanced: idle",
	}
	var payload := _load_json_dictionary(str(state.get("advanced_settings_path", "")))
	if payload.is_empty():
		return {"updates": updates}
	var mode := str(payload.get("mode", "balanced"))
	var policy_profile := str(payload.get("policy_profile", "default"))
	var strictness_level := str(payload.get("strictness_level", "normal"))
	updates["advanced_settings_status_text"] = "Advanced: %s | policy=%s | strict=%s" % [mode, policy_profile, strictness_level]
	updates["policy_sandbox_summary_text"] = "Policy Sandbox: mode=%s | policy=%s | strict=%s" % [mode, policy_profile, strictness_level]
	return {"updates": updates}


func load_security_model_state(state: Dictionary) -> Dictionary:
	var security_path := str(state.get("security_model_path", ""))
	var payload := _load_json_dictionary(security_path)
	if payload.is_empty():
		persist_security_model_state(state)
		return {
			"updates": {
				"destructive_guard_enabled": bool(state.get("destructive_guard_enabled", true)),
				"destructive_guard_window_ms": int(state.get("destructive_guard_window_ms", 8000)),
				"destructive_guard_token": str(state.get("destructive_guard_token", "confirm")),
				"security_model_summary_text": "Security: destructive_guard=%s | token=%s" % [str(bool(state.get("destructive_guard_enabled", true))), str(state.get("destructive_guard_token", "confirm"))],
			}
		}
	return {
		"updates": {
			"destructive_guard_enabled": bool(payload.get("destructive_guard_enabled", true)),
			"destructive_guard_window_ms": int(payload.get("destructive_guard_window_ms", 8000)),
			"destructive_guard_token": str(payload.get("destructive_guard_token", "confirm")),
			"security_model_summary_text": "Security: destructive_guard=%s | token=%s" % [str(bool(payload.get("destructive_guard_enabled", true))), str(payload.get("destructive_guard_token", "confirm"))],
		}
	}


func persist_security_model_state(state: Dictionary) -> bool:
	var security_path := str(state.get("security_model_path", ""))
	if security_path == "":
		return false
	_ensure_parent_dir(security_path)
	var payload: Dictionary = {
		"destructive_guard_enabled": bool(state.get("destructive_guard_enabled", true)),
		"destructive_guard_window_ms": int(state.get("destructive_guard_window_ms", 8000)),
		"destructive_guard_token": str(state.get("destructive_guard_token", "confirm")),
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	var wf := FileAccess.open(security_path, FileAccess.WRITE)
	if wf == null:
		return false
	wf.store_string(JSON.stringify(payload, "  "))
	wf.close()
	return true


func _load_json_dictionary(path_text: String) -> Dictionary:
	if path_text == "" or not FileAccess.file_exists(path_text):
		return {}
	var rf := FileAccess.open(path_text, FileAccess.READ)
	if rf == null:
		return {}
	var raw := rf.get_as_text()
	rf.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return {}
	return parsed


func _ensure_parent_dir(path_text: String) -> void:
	var abs_path := path_text
	if path_text.begins_with("user://") or path_text.begins_with("res://"):
		abs_path = ProjectSettings.globalize_path(path_text)
	var parent_dir := abs_path.get_base_dir()
	if parent_dir != "":
		DirAccess.make_dir_recursive_absolute(parent_dir)


func _dataset_label(name: String, tag: String) -> String:
	if name == "":
		return "n/a"
	if tag == "":
		return name
	return "%s@%s" % [name, tag]


func _synonym_label(name: String, tag: String) -> String:
	if name == "":
		return "n/a"
	if tag == "":
		return name
	return "%s@%s" % [name, tag]


func _profile_label(name: String, mode: String) -> String:
	if name == "":
		return "n/a"
	if mode == "":
		return name
	return "%s (%s)" % [name, mode]