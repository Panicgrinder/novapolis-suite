extends RefCounted

class_name AgentAuthoringPersistenceController


func apply_dataset_form_payload(payload: Dictionary, state: Dictionary) -> Dictionary:
	var dataset_name := _sanitize_name(str(payload.get("dataset_name", "")))
	if dataset_name == "":
		return _validation_error("Form: dataset_name fehlt")
	var dataset_tag := _sanitize_name(str(payload.get("dataset_tag", "v1")))
	if dataset_tag == "":
		dataset_tag = "v1"
	var set_active := bool(payload.get("set_active", true))

	var target := str(payload.get("target", state.get("form_target_value", "new")))
	if target != "new" and target != "append_user":
		return _validation_error("Form: target muss new/append_user sein")

	var records_any = payload.get("records", [])
	if typeof(records_any) != TYPE_ARRAY:
		return _validation_error("Form: records muss Array sein")
	var records: Array = records_any
	if records.is_empty():
		return _validation_error("Form: records ist leer")
	for rec_any in records:
		if typeof(rec_any) != TYPE_DICTIONARY:
			return _validation_error("Form: records enthaelt ungueltige Eintraege")
		var rec: Dictionary = rec_any
		var msgs_any = rec.get("messages", [])
		if typeof(msgs_any) != TYPE_ARRAY or msgs_any.is_empty():
			return _validation_error("Form: jeder record braucht messages[]")

	var base_dir := "user://agent_user_data/datasets"
	DirAccess.make_dir_recursive_absolute(base_dir)
	var file_path := "%s/%s.jsonl" % [base_dir, dataset_name]
	var exists := FileAccess.file_exists(file_path)
	if target == "new" and exists:
		return _validation_error("Form: Dataset existiert bereits")
	if target == "append_user" and not exists:
		return _validation_error("Form: Dataset fuer append nicht gefunden")

	var mode := FileAccess.WRITE
	if exists:
		mode = FileAccess.READ_WRITE
	var handle := FileAccess.open(file_path, mode)
	if handle == null:
		return _validation_error("Form: Datei konnte nicht geoeffnet werden")
	if exists:
		handle.seek_end()
	for rec_out in records:
		handle.store_string(JSON.stringify(rec_out, "") + "\n")
	handle.close()

	var updates: Dictionary = _update_dataset_registry(dataset_name, dataset_tag, set_active, state)
	updates["form_status_text"] = "Form: Dataset gespeichert (%s@%s, +%d)" % [dataset_name, dataset_tag, records.size()]
	return {
		"updates": updates,
		"events": [_event_record("AGENT_FORM", {"kind": "datasets", "target": target, "name": dataset_name, "tag": dataset_tag, "set_active": set_active, "records": records.size(), "path": file_path})],
	}


func apply_synonym_form_payload(payload: Dictionary, state: Dictionary) -> Dictionary:
	var synonym_set := _sanitize_name(str(payload.get("synonym_set", "")))
	if synonym_set == "":
		return _validation_error("Form: synonym_set fehlt")
	var synonym_tag := _sanitize_name(str(payload.get("synonym_tag", "v1")))
	if synonym_tag == "":
		synonym_tag = "v1"
	var set_active := bool(payload.get("set_active", true))

	var target := str(payload.get("target", state.get("form_target_value", "new")))
	if target != "new" and target != "append_user":
		return _validation_error("Form: target muss new/append_user sein")

	var entries_any = payload.get("entries", [])
	if typeof(entries_any) != TYPE_ARRAY:
		return _validation_error("Form: entries muss Array sein")
	var entries: Array = (entries_any as Array).duplicate(true)
	if entries.is_empty():
		return _validation_error("Form: entries ist leer")

	var import_path := str(payload.get("import_path", "")).strip_edges()
	var export_path := str(payload.get("export_path", "")).strip_edges()
	if import_path != "":
		var imported_result := _load_synonym_entries_from_path(import_path)
		if not bool(imported_result.get("ok", false)):
			return _validation_error("Form: Import fehlgeschlagen (%s)" % str(imported_result.get("reason", "parse")))
		var imported_any = imported_result.get("entries", [])
		if typeof(imported_any) == TYPE_ARRAY:
			for imported_entry_any in imported_any:
				entries.append(imported_entry_any)

	for entry_any in entries:
		if typeof(entry_any) != TYPE_DICTIONARY:
			return _validation_error("Form: entries enthaelt ungueltige Eintraege")
		var entry: Dictionary = entry_any
		if str(entry.get("term", "")).strip_edges() == "":
			return _validation_error("Form: jeder Eintrag braucht term")

	var base_dir := "user://agent_user_data/synonyms"
	DirAccess.make_dir_recursive_absolute(base_dir)
	var file_path := "%s/%s.json" % [base_dir, synonym_set]
	var exists := FileAccess.file_exists(file_path)
	if target == "new" and exists:
		return _validation_error("Form: Synonym-Set existiert bereits")
	if target == "append_user" and not exists:
		return _validation_error("Form: Synonym-Set fuer append nicht gefunden")

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
		return _validation_error("Form: Synonyms ungueltig (%s)" % str(validator.get("reason", "validation")))

	var out_payload: Dictionary = {
		"synonym_set": synonym_set,
		"synonym_tag": synonym_tag,
		"mode": str(payload.get("mode", state.get("form_mode_value", "pairs"))),
		"entries": merged_entries,
		"validator_status": validator_status,
		"validator_warnings": validator.get("warnings", []),
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	var wf := FileAccess.open(file_path, FileAccess.WRITE)
	if wf == null:
		return _validation_error("Form: Synonym-Datei konnte nicht geschrieben werden")
	wf.store_string(JSON.stringify(out_payload, "  "))
	wf.close()
	if export_path != "" and not _write_json_to_path(export_path, out_payload):
		return _validation_error("Form: Exportpfad konnte nicht geschrieben werden")

	var updates: Dictionary = _update_synonym_registry(synonym_set, synonym_tag, set_active, state)
	var active_set := str(updates.get("active_synonym_set", state.get("active_synonym_set", "")))
	var active_tag := str(updates.get("active_synonym_tag", state.get("active_synonym_tag", "")))
	updates["synonym_status_text"] = "Synonyms: active %s | delta=+%d terms/+%d syns | validator=%s" % [_synonym_label(active_set, active_tag), int(delta.get("terms_added", 0)), int(delta.get("synonyms_added", 0)), validator_status]
	updates["form_status_text"] = "Form: Synonyms gespeichert (%s@%s, +%d)" % [synonym_set, synonym_tag, entries.size()]
	return {
		"updates": updates,
		"events": [_event_record("AGENT_FORM", {
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
		})],
	}


func apply_profile_form_payload(payload: Dictionary, state: Dictionary) -> Dictionary:
	var profile_name := _sanitize_name(str(payload.get("profile_name", "")))
	if profile_name == "":
		return _validation_error("Form: profile_name fehlt")

	var target := str(payload.get("target", state.get("form_target_value", "new")))
	if target != "new" and target != "update":
		return _validation_error("Form: target muss new/update sein")

	var mode := _sanitize_name(str(payload.get("mode", state.get("form_mode_value", "balanced"))))
	if mode == "":
		mode = "balanced"

	var prompt_system := str(payload.get("prompt_system", "")).strip_edges()
	if prompt_system == "":
		return _validation_error("Form: prompt_system fehlt")

	var assign_any = payload.get("assign_to", [])
	if typeof(assign_any) != TYPE_ARRAY:
		return _validation_error("Form: assign_to muss Array sein")
	var assign_to: Array = assign_any
	var set_active := bool(payload.get("set_active", true))
	var archive := bool(payload.get("archive", false))

	var base_dir := "user://agent_user_data/profiles"
	DirAccess.make_dir_recursive_absolute(base_dir)
	var file_path := "%s/%s.json" % [base_dir, profile_name]
	var exists := FileAccess.file_exists(file_path)
	if target == "new" and exists:
		return _validation_error("Form: Profil existiert bereits")
	if target == "update" and not exists:
		return _validation_error("Form: Profil fuer update nicht gefunden")

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
		return _validation_error("Form: Profil-Datei konnte nicht geschrieben werden")
	wf.store_string(JSON.stringify(out_payload, "  "))
	wf.close()

	var updates: Dictionary = _update_profile_registry(profile_name, mode, set_active and not archive, archive, state)
	updates["form_status_text"] = "Form: Profil gespeichert (%s, mode=%s)" % [profile_name, mode]
	return {
		"updates": updates,
		"events": [_event_record("AGENT_FORM", {"kind": "profiles", "target": target, "name": profile_name, "mode": mode, "set_active": set_active, "archive": archive, "path": file_path})],
	}


func apply_advanced_settings_form_payload(payload: Dictionary, state: Dictionary) -> Dictionary:
	var mode := _sanitize_name(str(payload.get("mode", state.get("form_mode_value", "balanced"))))
	if mode == "":
		mode = "balanced"
	var policy_profile := _sanitize_name(str(payload.get("policy_profile", "default")))
	if policy_profile == "":
		policy_profile = "default"
	var strictness_level := _sanitize_name(str(payload.get("strictness_level", "normal")))
	if strictness_level == "":
		strictness_level = "normal"
	var safety_profile := _sanitize_name(str(payload.get("safety_profile", "standard")))
	if safety_profile == "":
		safety_profile = "standard"
	var debug_level := _sanitize_name(str(payload.get("debug_level", "minimal")))
	if debug_level == "":
		debug_level = "minimal"
	var system_behavior := str(payload.get("system_behavior", "")).strip_edges()
	if system_behavior == "":
		return _validation_error("Form: system_behavior fehlt")

	var advanced_settings_path := str(state.get("advanced_settings_path", "user://agent_user_data/settings/advanced.json"))
	_ensure_parent_dir(advanced_settings_path)
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
	var wf := FileAccess.open(advanced_settings_path, FileAccess.WRITE)
	if wf == null:
		return _validation_error("Form: Advanced Settings konnten nicht gespeichert werden")
	wf.store_string(JSON.stringify(out_payload, "  "))
	wf.close()

	return {
		"updates": {
			"advanced_settings_status_text": "Advanced: %s | policy=%s | strict=%s" % [mode, policy_profile, strictness_level],
			"form_status_text": "Form: Advanced Settings gespeichert (%s)" % mode,
		},
		"events": [_event_record("AGENT_FORM", {"kind": "advanced", "mode": mode, "policy_profile": policy_profile, "strictness_level": strictness_level, "path": advanced_settings_path})],
	}


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


func _update_dataset_registry(dataset_name: String, dataset_tag: String, set_active: bool, state: Dictionary) -> Dictionary:
	var registry_path := str(state.get("dataset_registry_path", "user://agent_user_data/datasets/_registry.json"))
	var registry := _load_registry(registry_path)
	var datasets_any = registry.get("datasets", {})
	if typeof(datasets_any) != TYPE_DICTIONARY:
		datasets_any = {}
	var datasets: Dictionary = datasets_any
	datasets[dataset_name] = {
		"tag": dataset_tag,
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	registry["datasets"] = datasets

	var active_dataset_name := str(state.get("active_dataset_name", ""))
	var active_dataset_tag := str(state.get("active_dataset_tag", ""))
	if set_active or str(registry.get("active_dataset", "")) == "":
		registry["active_dataset"] = dataset_name
		registry["active_tag"] = dataset_tag
		active_dataset_name = dataset_name
		active_dataset_tag = dataset_tag

	_ensure_parent_dir(registry_path)
	var wf := FileAccess.open(registry_path, FileAccess.WRITE)
	if wf != null:
		wf.store_string(JSON.stringify(registry, "  "))
		wf.close()

	var updates: Dictionary = {
		"active_dataset_name": active_dataset_name,
		"active_dataset_tag": active_dataset_tag,
	}
	if active_dataset_name != "":
		updates["dataset_status_text"] = "Datasets: active %s" % _dataset_label(active_dataset_name, active_dataset_tag)
	return updates


func _update_synonym_registry(synonym_set: String, synonym_tag: String, set_active: bool, state: Dictionary) -> Dictionary:
	var registry_path := str(state.get("synonym_registry_path", "user://agent_user_data/synonyms/_registry.json"))
	var registry := _load_registry(registry_path)
	var sets_any = registry.get("sets", {})
	if typeof(sets_any) != TYPE_DICTIONARY:
		sets_any = {}
	var sets: Dictionary = sets_any
	sets[synonym_set] = {
		"tag": synonym_tag,
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	registry["sets"] = sets

	var active_synonym_set := str(state.get("active_synonym_set", ""))
	var active_synonym_tag := str(state.get("active_synonym_tag", ""))
	if set_active or str(registry.get("active_set", "")) == "":
		registry["active_set"] = synonym_set
		registry["active_tag"] = synonym_tag
		active_synonym_set = synonym_set
		active_synonym_tag = synonym_tag

	_ensure_parent_dir(registry_path)
	var wf := FileAccess.open(registry_path, FileAccess.WRITE)
	if wf != null:
		wf.store_string(JSON.stringify(registry, "  "))
		wf.close()

	return {
		"active_synonym_set": active_synonym_set,
		"active_synonym_tag": active_synonym_tag,
	}


func _update_profile_registry(profile_name: String, mode: String, set_active: bool, archive: bool, state: Dictionary) -> Dictionary:
	var registry_path := str(state.get("profile_registry_path", "user://agent_user_data/profiles/_registry.json"))
	var registry := _load_registry(registry_path)
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

	var active_profile_name := str(state.get("active_profile_name", ""))
	var active_profile_mode := str(state.get("active_profile_mode", ""))
	var profile_status_text := str(state.get("profile_status_text", "Profiles: idle"))
	if archive:
		if str(registry.get("active_profile", "")) == profile_name:
			registry["active_profile"] = ""
			registry["active_mode"] = ""
			active_profile_name = ""
			active_profile_mode = ""
		profile_status_text = "Profiles: archived %s" % profile_name
	else:
		if set_active or str(registry.get("active_profile", "")) == "":
			registry["active_profile"] = profile_name
			registry["active_mode"] = mode
			active_profile_name = profile_name
			active_profile_mode = mode
		if active_profile_name != "":
			profile_status_text = "Profiles: active %s" % _profile_label(active_profile_name, active_profile_mode)

	_ensure_parent_dir(registry_path)
	var wf := FileAccess.open(registry_path, FileAccess.WRITE)
	if wf != null:
		wf.store_string(JSON.stringify(registry, "  "))
		wf.close()

	return {
		"active_profile_name": active_profile_name,
		"active_profile_mode": active_profile_mode,
		"profile_status_text": profile_status_text,
	}


func _load_registry(path_text: String) -> Dictionary:
	var registry: Dictionary = {}
	if not FileAccess.file_exists(path_text):
		return registry
	var rf := FileAccess.open(path_text, FileAccess.READ)
	if rf == null:
		return registry
	var raw := rf.get_as_text()
	rf.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) == TYPE_DICTIONARY:
		registry = parsed
	return registry


func _ensure_parent_dir(path_text: String) -> void:
	var abs_path := path_text
	if path_text.begins_with("user://") or path_text.begins_with("res://"):
		abs_path = ProjectSettings.globalize_path(path_text)
	var parent_dir := abs_path.get_base_dir()
	if parent_dir != "":
		DirAccess.make_dir_recursive_absolute(parent_dir)


func _sanitize_name(value: String) -> String:
	var result := value.strip_edges().to_lower()
	result = result.replace(" ", "_")
	result = result.replace("/", "_")
	result = result.replace("\\", "_")
	result = result.replace(":", "_")
	result = result.replace(";", "_")
	result = result.replace("\"", "")
	result = result.replace("'", "")
	return result


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


func _validation_error(status_text: String) -> Dictionary:
	return {"updates": {"form_status_text": status_text}}


func _event_record(tag: String, payload: Dictionary) -> Dictionary:
	return {"tag": tag, "payload": payload}