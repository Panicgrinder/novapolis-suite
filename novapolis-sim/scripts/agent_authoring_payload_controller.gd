extends RefCounted

class_name AgentAuthoringPayloadController


func build_form_payload(state: Dictionary) -> Dictionary:
	var kind := str(state.get("form_kind", ""))
	var form_mode_value := str(state.get("form_mode_value", ""))
	var form_target_value := str(state.get("form_target_value", ""))
	var form_name := str(state.get("form_name", "")).strip_edges()
	var finetune_base_model := str(state.get("finetune_base_model", "sshleifer/tiny-gpt2"))
	var controls_any = state.get("form_controls", {})
	var controls: Dictionary = controls_any if typeof(controls_any) == TYPE_DICTIONARY else {}

	if kind == "datasets":
		return _build_dataset_payload(form_name, form_target_value, form_mode_value, controls)
	if kind == "synonyms":
		return _build_synonym_payload(form_name, form_target_value, form_mode_value, controls)
	if kind == "finetune":
		return _build_finetune_payload(form_name, form_mode_value, finetune_base_model, controls)
	if kind == "profiles":
		return _build_profile_payload(form_name, form_target_value, form_mode_value, controls)
	if kind == "advanced":
		return _build_advanced_payload(form_mode_value, controls)
	if kind == "jobs":
		return _build_jobs_payload(form_name, form_target_value, form_mode_value, controls)
	return _validation_error("Form: Unbekannter Form-Typ")


func _build_dataset_payload(form_name: String, form_target_value: String, form_mode_value: String, controls: Dictionary) -> Dictionary:
	if form_name == "":
		return _validation_error("Form: Name fehlt")
	var sys_prompt := _control_text(controls, "dataset_system_prompt").strip_edges()
	var user_prompt := _control_text(controls, "dataset_user_prompt").strip_edges()
	var assistant_prompt := _control_text(controls, "dataset_assistant_prompt").strip_edges()
	if user_prompt == "" or assistant_prompt == "":
		return _validation_error("Form: User/Assistant-Beispiel fehlt")
	return {
		"payload": {
			"dataset_name": form_name,
			"dataset_tag": _control_text(controls, "dataset_tag", "v1"),
			"target": form_target_value,
			"set_active": _control_bool(controls, "dataset_set_active", true),
			"source_mode": form_mode_value,
			"records": [
				{
					"messages": [
						{"role": "system", "content": sys_prompt if sys_prompt != "" else "Du bist Novapolis Agent."},
						{"role": "user", "content": user_prompt},
						{"role": "assistant", "content": assistant_prompt},
					],
				}
			],
			"train_ratio": _control_float(controls, "dataset_train_ratio", 0.9),
			"min_output_chars": _control_int(controls, "dataset_min_output_chars", 20),
			"notes": _control_text(controls, "dataset_notes", ""),
		}
	}


func _build_synonym_payload(form_name: String, form_target_value: String, form_mode_value: String, controls: Dictionary) -> Dictionary:
	if form_name == "":
		return _validation_error("Form: Name fehlt")
	var term := _control_text(controls, "syn_term").strip_edges()
	var syn_csv := _control_text(controls, "syn_values_csv").strip_edges()
	if term == "" or syn_csv == "":
		return _validation_error("Form: term/synonyms fehlt")
	var synonyms := _control_csv_array(controls, "syn_values_csv")
	if synonyms.is_empty():
		return _validation_error("Form: mind. ein Synonym erforderlich")
	return {
		"payload": {
			"synonym_set": form_name,
			"synonym_tag": _control_text(controls, "syn_tag", "v1"),
			"target": form_target_value,
			"set_active": _control_bool(controls, "syn_set_active", true),
			"mode": form_mode_value,
			"import_path": _control_text(controls, "syn_import_path", ""),
			"export_path": _control_text(controls, "syn_export_path", ""),
			"entries": [{"term": term, "synonyms": synonyms}],
			"notes": _control_text(controls, "syn_notes", ""),
		}
	}


func _build_finetune_payload(form_name: String, form_mode_value: String, finetune_base_model: String, controls: Dictionary) -> Dictionary:
	return {
		"payload": {
			"profile": form_mode_value,
			"base_model": _control_text(controls, "ft_base_model", finetune_base_model),
			"output_name": form_name,
			"train_file": _control_text(controls, "ft_train_file", ""),
			"epochs": _control_int(controls, "ft_epochs", 1),
			"max_steps": _control_int(controls, "ft_max_steps", 10),
			"batch_size": _control_int(controls, "ft_batch_size", 1),
			"lr": _control_float(controls, "ft_lr", 0.0002),
			"no_check": _control_bool(controls, "ft_no_check", true),
			"notes": _control_text(controls, "ft_notes", ""),
		}
	}


func _build_profile_payload(form_name: String, form_target_value: String, form_mode_value: String, controls: Dictionary) -> Dictionary:
	return {
		"payload": {
			"profile_name": form_name,
			"target": form_target_value,
			"mode": form_mode_value,
			"prompt_system": _control_text(controls, "profile_prompt_system", ""),
			"behavior_notes": _control_text(controls, "profile_behavior_notes", ""),
			"assign_to": _control_csv_array(controls, "profile_assign_to_csv"),
			"set_active": _control_bool(controls, "profile_set_active", true),
			"archive": _control_bool(controls, "profile_archive", false),
			"notes": _control_text(controls, "profile_notes", ""),
		}
	}


func _build_advanced_payload(form_mode_value: String, controls: Dictionary) -> Dictionary:
	return {
		"payload": {
			"mode": form_mode_value,
			"policy_profile": _control_text(controls, "adv_policy_profile", "default"),
			"strictness_level": _control_text(controls, "adv_strictness_level", "normal"),
			"safety_profile": _control_text(controls, "adv_safety_profile", "standard"),
			"debug_level": _control_text(controls, "adv_debug_level", "minimal"),
			"system_behavior": _control_text(controls, "adv_system_behavior", ""),
			"notes": _control_text(controls, "adv_notes", ""),
		}
	}


func _build_jobs_payload(form_name: String, form_target_value: String, form_mode_value: String, controls: Dictionary) -> Dictionary:
	return {
		"payload": {
			"job_name": form_name,
			"job_type": form_mode_value,
			"target": form_target_value,
			"enqueue": _control_bool(controls, "job_enqueue", true),
			"priority": _control_int(controls, "job_priority", 10),
			"payload": {"notes": _control_text(controls, "job_payload_notes", "")},
			"notes": _control_text(controls, "job_notes", ""),
		}
	}


func _control_text(controls: Dictionary, key: String, fallback: String = "") -> String:
	var ctrl: Variant = controls.get(key, null)
	if ctrl is LineEdit:
		return (ctrl as LineEdit).text
	if ctrl is TextEdit:
		return (ctrl as TextEdit).text
	return fallback


func _control_int(controls: Dictionary, key: String, fallback: int) -> int:
	var ctrl: Variant = controls.get(key, null)
	if ctrl is SpinBox:
		return int((ctrl as SpinBox).value)
	return fallback


func _control_float(controls: Dictionary, key: String, fallback: float) -> float:
	var ctrl: Variant = controls.get(key, null)
	if ctrl is SpinBox:
		return float((ctrl as SpinBox).value)
	return fallback


func _control_bool(controls: Dictionary, key: String, fallback: bool) -> bool:
	var ctrl: Variant = controls.get(key, null)
	if ctrl is CheckBox:
		return (ctrl as CheckBox).button_pressed
	return fallback


func _control_csv_array(controls: Dictionary, key: String) -> Array[String]:
	var values: Array[String] = []
	var raw := _control_text(controls, key, "")
	for part in raw.split(","):
		var clean := str(part).strip_edges()
		if clean != "":
			values.append(clean)
	return values


func _validation_error(status_text: String) -> Dictionary:
	return {"updates": {"form_status_text": status_text}}