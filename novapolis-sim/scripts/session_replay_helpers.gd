extends RefCounted

class_name SessionReplayHelpers


func coerce_dict_array(value: Variant) -> Array[Dictionary]:
	var entries: Array[Dictionary] = []
	if typeof(value) != TYPE_ARRAY:
		return entries
	for item in value:
		if typeof(item) == TYPE_DICTIONARY:
			entries.append(item)
	return entries


func parse_slot_number(value: Variant) -> int:
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


func extract_slot_from_entry(entry: Dictionary) -> int:
	for key in ["slot", "hour", "slot_index", "slot_id"]:
		if entry.has(key):
			var slot_number := parse_slot_number(entry.get(key, -1))
			if slot_number >= 0:
				return slot_number
	return -1


func derive_initial_slot(pc_log: Array) -> int:
	for entry in pc_log:
		if typeof(entry) != TYPE_DICTIONARY:
			continue
		var slot_value := extract_slot_from_entry(entry)
		if slot_value >= 0:
			return slot_value
	return 0


func live_session_epoch_name(session_id: String) -> String:
	if session_id == "":
		return "live-session"
	return "session-%s" % session_id


func normalize_live_session_payload(session_payload: Dictionary, session_id: String, fallback_slot: int) -> Dictionary:
	var world_log := coerce_dict_array(session_payload.get("world_log", []))
	var pc_log := coerce_dict_array(session_payload.get("pc_log", []))
	var state_patches := coerce_dict_array(session_payload.get("state_patches", []))
	var artifact_paths: Dictionary = {}
	if typeof(session_payload.get("artifact_paths", {})) == TYPE_DICTIONARY:
		artifact_paths = session_payload.get("artifact_paths", {})

	var slot_number := parse_slot_number(session_payload.get("slot_index", -1))
	if slot_number < 0:
		slot_number = parse_slot_number(session_payload.get("slot_id", -1))
	if slot_number < 0:
		slot_number = derive_initial_slot(pc_log)
	if slot_number < 0:
		slot_number = fallback_slot

	var patch_count := 0
	if typeof(session_payload.get("state_patches", [])) == TYPE_ARRAY:
		patch_count = (session_payload.get("state_patches", []) as Array).size()

	return {
		"world_log": world_log,
		"pc_log": pc_log,
		"state_patches": state_patches,
		"artifact_paths": artifact_paths,
		"resume_checkpoint_id": str(session_payload.get("resume_checkpoint_id", "")).strip_edges(),
		"slot_number": clampi(slot_number, 0, 23),
		"patch_count": patch_count,
		"epoch_entry": {
			"name": live_session_epoch_name(session_id),
			"world_log": world_log,
			"pc_log": pc_log,
			"state_patches": state_patches,
			"artifact_paths": artifact_paths,
			"source": "session_api",
		},
	}


func build_session_endpoint(host: String, port: int, session_id: String) -> String:
	return "http://%s:%d/session/%s" % [host, port, session_id.uri_encode()]


func build_replay_endpoint(host: String, port: int, session_id: String) -> String:
	return "%s/replay" % build_session_endpoint(host, port, session_id)


func coerce_string_array(value: Variant) -> Array[String]:
	var result: Array[String] = []
	if typeof(value) != TYPE_ARRAY:
		return result
	for item in value:
		var text := str(item).strip_edges()
		if text != "":
			result.append(text)
	return result


func build_checkpoint_options(manifest: Dictionary, fallback_resume_checkpoint_id: String, current_selected_checkpoint_id: String) -> Dictionary:
	var checkpoints := coerce_string_array(manifest.get("checkpoints", []))
	var resume_checkpoint := str(manifest.get("resume_checkpoint_id", fallback_resume_checkpoint_id)).strip_edges()
	if resume_checkpoint != "" and not checkpoints.has(resume_checkpoint):
		checkpoints.insert(0, resume_checkpoint)

	var selected_checkpoint := current_selected_checkpoint_id.strip_edges()
	if not checkpoints.is_empty() and (selected_checkpoint == "" or not checkpoints.has(selected_checkpoint)):
		selected_checkpoint = resume_checkpoint if resume_checkpoint != "" else checkpoints[0]
	if checkpoints.is_empty():
		selected_checkpoint = ""

	return {
		"checkpoints": checkpoints,
		"selected_checkpoint_id": selected_checkpoint,
		"resume_checkpoint_id": resume_checkpoint,
	}


func parse_checkpoint_tick(checkpoint_id: String) -> int:
	var text := checkpoint_id.strip_edges()
	if not text.begins_with("tick-"):
		return -1
	var digits := text.substr(5)
	if digits.is_valid_int():
		return int(digits)
	return -1


func find_slot_for_checkpoint_in_entries(entries: Array, checkpoint_id: String) -> int:
	var checkpoint_tick := parse_checkpoint_tick(checkpoint_id)
	for item in entries:
		if typeof(item) != TYPE_DICTIONARY:
			continue
		var entry := item as Dictionary
		if str(entry.get("turn_id", "")).strip_edges() == checkpoint_id:
			var slot_number := extract_slot_from_entry(entry)
			if slot_number >= 0:
				return slot_number
		if checkpoint_tick >= 0 and int(entry.get("tick", -1)) == checkpoint_tick:
			var tick_slot := extract_slot_from_entry(entry)
			if tick_slot >= 0:
				return tick_slot
	return -1


func find_slot_for_checkpoint(loaded_epochs: Array, current_epoch_index: int, manifest: Dictionary, checkpoint_id: String) -> int:
	if checkpoint_id == "" or loaded_epochs.is_empty():
		return -1
	if current_epoch_index < 0 or current_epoch_index >= loaded_epochs.size():
		return -1
	var epoch_value: Variant = loaded_epochs[current_epoch_index]
	if typeof(epoch_value) != TYPE_DICTIONARY:
		return -1
	var epoch: Dictionary = epoch_value
	for key in ["pc_log", "world_log", "state_patches"]:
		var slot_number := find_slot_for_checkpoint_in_entries(epoch.get(key, []), checkpoint_id)
		if slot_number >= 0:
			return slot_number
	var manifest_slot := parse_slot_number(manifest.get("slot_index", -1))
	if manifest_slot >= 0:
		return manifest_slot
	manifest_slot = parse_slot_number(manifest.get("slot_id", -1))
	if manifest_slot >= 0:
		return manifest_slot
	return -1
