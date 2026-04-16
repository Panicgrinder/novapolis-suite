extends RefCounted

class_name AgentFormController


func open_form(kind: String, state: Dictionary) -> Dictionary:
	var result := {
		"form_kind": kind,
		"form_mode_value": "pairs",
		"form_target_value": "append_user",
		"form_name": "user_synonyms",
	}
	if kind == "datasets":
		result["form_mode_value"] = str(state.get("dataset_source_mode", "clean"))
		result["form_target_value"] = "new"
		result["form_name"] = "user_dataset_%s" % Time.get_datetime_string_from_system(false, true).replace(":", "").replace("-", "").replace(" ", "_")
	elif kind == "finetune":
		result["form_mode_value"] = str(state.get("finetune_profile", "baseline"))
		result["form_target_value"] = "new"
		result["form_name"] = str(state.get("finetune_output_name", "lora-agent-hub"))
	elif kind == "profiles":
		var active_profile_mode := str(state.get("active_profile_mode", "")).strip_edges()
		result["form_mode_value"] = active_profile_mode if active_profile_mode != "" else "balanced"
		result["form_target_value"] = "new"
		var active_profile_name := str(state.get("active_profile_name", "")).strip_edges()
		result["form_name"] = active_profile_name if active_profile_name != "" else "profile_default"
	elif kind == "advanced":
		result["form_mode_value"] = "balanced"
		result["form_target_value"] = "update"
		result["form_name"] = "advanced_settings"
	elif kind == "jobs":
		result["form_mode_value"] = "eval"
		result["form_target_value"] = "new"
		result["form_name"] = "job_%s" % Time.get_datetime_string_from_system(false, true).replace(":", "").replace("-", "").replace(" ", "_")
	return result


func mode_options_for_kind(kind: String) -> Array[String]:
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


func target_options_for_kind(kind: String) -> Array[String]:
	if kind == "datasets" or kind == "synonyms":
		return ["new", "append_user"]
	if kind == "profiles":
		return ["new", "update"]
	if kind == "jobs":
		return ["new", "retry_latest", "cancel_latest"]
	return []


func refresh_form_ui(controls: Dictionary, state: Dictionary) -> Dictionary:
	var kind := str(state.get("form_kind", ""))
	var show_form := _is_form_visible(bool(state.get("agent_submenu_open", false)), str(state.get("studio_mode", "operate")), kind)
	(controls.get("agent_form_panel") as Control).visible = show_form
	if not show_form:
		return {
			"form_mode_value": str(state.get("form_mode_value", "")),
			"form_target_value": str(state.get("form_target_value", "")),
			"template_signature": str(state.get("template_signature", "")),
			"form_controls": state.get("form_controls", {}),
		}

	(controls.get("agent_form_payload_edit") as Control).visible = false
	(controls.get("agent_form_fields_scroll") as Control).visible = true

	var mode_value := _normalize_value(mode_options_for_kind(kind), str(state.get("form_mode_value", "")))
	var target_value := _normalize_value(target_options_for_kind(kind), str(state.get("form_target_value", "")))
	_sync_form_dropdowns(controls, kind, mode_value, target_value)

	(controls.get("agent_form_name_edit") as LineEdit).placeholder_text = _form_name_placeholder_for_kind(kind)
	(controls.get("agent_form_payload_edit") as TextEdit).placeholder_text = _form_payload_placeholder_for_kind(kind)

	var template_signature := "%s|%s|%s" % [kind, mode_value, target_value]
	var previous_signature := str(state.get("template_signature", ""))
	var form_controls: Dictionary = state.get("form_controls", {})
	if template_signature != previous_signature:
		form_controls = _rebuild_form_fields(controls, kind, state)
		(controls.get("agent_form_status_label") as Label).text = _form_ready_status(kind)

	_layout_form_controls(controls)
	(controls.get("agent_form_title_label") as Label).text = _form_title(kind)

	return {
		"form_mode_value": mode_value,
		"form_target_value": target_value,
		"template_signature": template_signature,
		"form_controls": form_controls,
	}


func mode_display_label(kind: String, value: String) -> String:
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


func _is_form_visible(agent_submenu_open: bool, studio_mode: String, kind: String) -> bool:
	return agent_submenu_open and studio_mode == "author" and (kind == "datasets" or kind == "synonyms" or kind == "finetune" or kind == "profiles" or kind == "advanced" or kind == "jobs")


func _sync_form_dropdowns(controls: Dictionary, kind: String, mode_value: String, target_value: String) -> void:
	var mode_options := mode_options_for_kind(kind)
	var mode_button := controls.get("agent_form_mode_button") as OptionButton
	mode_button.clear()
	for value in mode_options:
		mode_button.add_item(mode_display_label(kind, value))
	_select_option_value(mode_button, mode_options, mode_value)

	var target_options := target_options_for_kind(kind)
	var target_button := controls.get("agent_form_target_button") as OptionButton
	target_button.clear()
	if target_options.is_empty():
		target_button.add_item("Nicht relevant")
		target_button.disabled = true
		return

	for value in target_options:
		target_button.add_item(_form_target_label(value))
	target_button.disabled = false
	_select_option_value(target_button, target_options, target_value)


func _layout_form_controls(controls: Dictionary) -> void:
	var panel := controls.get("agent_form_panel") as Control
	var panel_w := panel.offset_right - panel.offset_left
	var panel_h := panel.offset_bottom - panel.offset_top
	var left := 12.0
	var right := maxf(left + 24.0, panel_w - 12.0)

	_set_rect(controls.get("agent_form_title_label") as Control, left, 10.0, right, 28.0)
	var row_top := 38.0
	var row_bottom := 72.0
	var field_gap := 12.0
	var field_w := maxf(140.0, (right - left - field_gap) / 2.0)
	_set_rect(controls.get("agent_form_mode_button") as Control, left, row_top, left + field_w, row_bottom)
	_set_rect(controls.get("agent_form_target_button") as Control, left + field_w + field_gap, row_top, right, row_bottom)
	_set_rect(controls.get("agent_form_name_edit") as Control, left, 84.0, right - 98.0, 114.0)
	_set_rect(controls.get("agent_form_apply_button") as Control, right - 90.0, 84.0, right, 114.0)

	var fields_bottom := maxf(164.0, panel_h - 44.0)
	_set_rect(controls.get("agent_form_fields_scroll") as Control, left, 126.0, right, fields_bottom)
	_set_rect(controls.get("agent_form_payload_edit") as Control, left, 126.0, right, fields_bottom)
	_set_rect(controls.get("agent_form_status_label") as Control, left, fields_bottom + 12.0, right, fields_bottom + 30.0)


func _rebuild_form_fields(controls: Dictionary, kind: String, state: Dictionary) -> Dictionary:
	var form_fields_box := controls.get("agent_form_fields_box") as VBoxContainer
	for child in form_fields_box.get_children():
		child.queue_free()

	var form_controls: Dictionary = {}
	if kind == "datasets":
		_add_line_field(form_fields_box, form_controls, "dataset_tag", "Dataset-Tag", _default_string(state, "active_dataset_tag", "v1"), "z. B. v1")
		_add_int_field(form_fields_box, form_controls, "dataset_min_output_chars", "Min. Output Chars", 20, 1, 2000)
		_add_float_field(form_fields_box, form_controls, "dataset_train_ratio", "Train-Ratio", 0.9, 0.1, 0.99, 0.01)
		_add_bool_field(form_fields_box, form_controls, "dataset_set_active", "Als aktives Dataset setzen", true)
		_add_text_field(form_fields_box, form_controls, "dataset_system_prompt", "System-Prompt", "Du bist Novapolis Agent.", "Optionaler System-Kontext", 66.0)
		_add_text_field(form_fields_box, form_controls, "dataset_user_prompt", "User-Beispiel", "", "z. B. Erstelle eine kurze RP-Szene mit Konflikt und Hook.", 66.0)
		_add_text_field(form_fields_box, form_controls, "dataset_assistant_prompt", "Assistant-Beispiel", "", "z. B. Hier ist eine kurze RP-Szene...", 66.0)
		_add_text_field(form_fields_box, form_controls, "dataset_notes", "Notizen", "", "Optional", 56.0)
		return form_controls

	if kind == "synonyms":
		_add_line_field(form_fields_box, form_controls, "syn_tag", "Synonym-Tag", _default_string(state, "active_synonym_tag", "v1"), "z. B. v1")
		_add_bool_field(form_fields_box, form_controls, "syn_set_active", "Als aktives Synonym-Set setzen", true)
		_add_line_field(form_fields_box, form_controls, "syn_term", "Begriff", "", "z. B. Aufstand")
		_add_line_field(form_fields_box, form_controls, "syn_values_csv", "Synonyme (CSV)", "", "z. B. rebell, revolt, uprising")
		_add_text_field(form_fields_box, form_controls, "syn_notes", "Notizen", "", "Optional", 56.0)
		return form_controls

	if kind == "finetune":
		_add_line_field(form_fields_box, form_controls, "ft_base_model", "Base Model", str(state.get("finetune_base_model", "sshleifer/tiny-gpt2")), "z. B. sshleifer/tiny-gpt2")
		_add_line_field(form_fields_box, form_controls, "ft_train_file", "Train-Datei (optional)", "", "Leer = automatische Aufloesung")
		_add_int_field(form_fields_box, form_controls, "ft_epochs", "Epochs", 1, 1, 20)
		_add_int_field(form_fields_box, form_controls, "ft_max_steps", "Max Steps", 10, 1, 100000)
		_add_int_field(form_fields_box, form_controls, "ft_batch_size", "Batch Size", 1, 1, 128)
		_add_float_field(form_fields_box, form_controls, "ft_lr", "Learning Rate", 0.0002, 0.000001, 0.01, 0.0001)
		_add_bool_field(form_fields_box, form_controls, "ft_no_check", "Pre-Checks ueberspringen", true)
		_add_text_field(form_fields_box, form_controls, "ft_notes", "Notizen", "", "Optional", 56.0)
		return form_controls

	if kind == "profiles":
		_add_text_field(form_fields_box, form_controls, "profile_prompt_system", "System-Prompt", "Du bist ein hilfreicher Novapolis-Agent mit klaren, kurzen Antworten.", "Pflichtfeld", 90.0)
		_add_text_field(form_fields_box, form_controls, "profile_behavior_notes", "Behavior Notes", "Priorisiert Klarheit, Korrektheit und kurze Struktur.", "Optional", 72.0)
		_add_line_field(form_fields_box, form_controls, "profile_assign_to_csv", "Assign To (CSV)", "eval,finetune", "z. B. eval,finetune")
		_add_bool_field(form_fields_box, form_controls, "profile_set_active", "Als aktives Profil setzen", true)
		_add_bool_field(form_fields_box, form_controls, "profile_archive", "Profil archivieren", false)
		_add_text_field(form_fields_box, form_controls, "profile_notes", "Notizen", "", "Optional", 56.0)
		return form_controls

	if kind == "advanced":
		_add_line_field(form_fields_box, form_controls, "adv_policy_profile", "Policy Profile", "default", "z. B. default")
		_add_line_field(form_fields_box, form_controls, "adv_strictness_level", "Strictness", "normal", "z. B. normal")
		_add_line_field(form_fields_box, form_controls, "adv_safety_profile", "Safety Profile", "standard", "z. B. standard")
		_add_line_field(form_fields_box, form_controls, "adv_debug_level", "Debug Level", "minimal", "z. B. minimal")
		_add_text_field(form_fields_box, form_controls, "adv_system_behavior", "System Behavior", "", "Pflichtfeld", 90.0)
		_add_text_field(form_fields_box, form_controls, "adv_notes", "Notizen", "", "Optional", 56.0)
		return form_controls

	if kind == "jobs":
		_add_bool_field(form_fields_box, form_controls, "job_enqueue", "Job sofort einreihen", true)
		_add_int_field(form_fields_box, form_controls, "job_priority", "Prioritaet", 10, 0, 100)
		_add_text_field(form_fields_box, form_controls, "job_payload_notes", "Payload Notes", "", "z. B. limit=20, suite=neutral", 72.0)
		_add_text_field(form_fields_box, form_controls, "job_notes", "Notizen", "", "Optional", 56.0)
	return form_controls


func _form_title(kind: String) -> String:
	if kind == "datasets":
		return "Form: Datasets"
	if kind == "finetune":
		return "Form: Finetune"
	if kind == "profiles":
		return "Form: Profiles"
	if kind == "advanced":
		return "Form: Advanced Settings"
	if kind == "jobs":
		return "Form: Jobs"
	return "Form: Synonyms"


func _form_ready_status(kind: String) -> String:
	if kind == "datasets":
		return "Form: Datasets-Konfiguration bereit"
	if kind == "finetune":
		return "Form: Finetune-Konfiguration bereit"
	if kind == "profiles":
		return "Form: Profile-Konfiguration bereit"
	if kind == "advanced":
		return "Form: Advanced-Settings-Konfiguration bereit"
	if kind == "jobs":
		return "Form: Jobs-Konfiguration bereit"
	return "Form: Synonym-Konfiguration bereit"


func _form_name_placeholder_for_kind(kind: String) -> String:
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


func _form_payload_placeholder_for_kind(kind: String) -> String:
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


func _profile_mode_label(mode_value: String) -> String:
	if mode_value == "strict":
		return "Strict"
	if mode_value == "creative":
		return "Creative"
	return "Balanced"


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


func _normalize_value(options: Array[String], value: String) -> String:
	if options.is_empty() or _index_of_value(options, value) >= 0:
		return value
	return options[0]


func _select_option_value(button: OptionButton, options: Array[String], value: String) -> void:
	var selected_index := _index_of_value(options, value)
	button.select(maxi(0, selected_index))


func _index_of_value(options: Array[String], value: String) -> int:
	for i in range(options.size()):
		if options[i] == value:
			return i
	return -1


func _default_string(state: Dictionary, key: String, fallback: String) -> String:
	var value := str(state.get(key, "")).strip_edges()
	return value if value != "" else fallback


func _add_line_field(form_fields_box: VBoxContainer, form_controls: Dictionary, key: String, label_text: String, value: String, placeholder: String) -> void:
	var label := Label.new()
	label.text = label_text
	form_fields_box.add_child(label)

	var edit := LineEdit.new()
	edit.text = value
	edit.placeholder_text = placeholder
	form_fields_box.add_child(edit)
	form_controls[key] = edit


func _add_text_field(form_fields_box: VBoxContainer, form_controls: Dictionary, key: String, label_text: String, value: String, placeholder: String, height: float) -> void:
	var label := Label.new()
	label.text = label_text
	form_fields_box.add_child(label)

	var edit := TextEdit.new()
	edit.text = value
	edit.placeholder_text = placeholder
	edit.custom_minimum_size = Vector2(0.0, height)
	form_fields_box.add_child(edit)
	form_controls[key] = edit


func _add_int_field(form_fields_box: VBoxContainer, form_controls: Dictionary, key: String, label_text: String, value: int, min_value: int, max_value: int) -> void:
	var label := Label.new()
	label.text = label_text
	form_fields_box.add_child(label)

	var spin := SpinBox.new()
	spin.min_value = min_value
	spin.max_value = max_value
	spin.step = 1.0
	spin.rounded = true
	spin.value = value
	form_fields_box.add_child(spin)
	form_controls[key] = spin


func _add_float_field(form_fields_box: VBoxContainer, form_controls: Dictionary, key: String, label_text: String, value: float, min_value: float, max_value: float, step_value: float) -> void:
	var label := Label.new()
	label.text = label_text
	form_fields_box.add_child(label)

	var spin := SpinBox.new()
	spin.min_value = min_value
	spin.max_value = max_value
	spin.step = step_value
	spin.value = value
	form_fields_box.add_child(spin)
	form_controls[key] = spin


func _add_bool_field(form_fields_box: VBoxContainer, form_controls: Dictionary, key: String, label_text: String, value: bool) -> void:
	var check := CheckBox.new()
	check.text = label_text
	check.button_pressed = value
	form_fields_box.add_child(check)
	form_controls[key] = check


func _set_rect(control: Control, left: float, top: float, right: float, bottom: float) -> void:
	control.offset_left = left
	control.offset_top = top
	control.offset_right = right
	control.offset_bottom = bottom