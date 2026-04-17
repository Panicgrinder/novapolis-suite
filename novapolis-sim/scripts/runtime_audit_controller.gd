extends RefCounted

class_name RuntimeAuditController


func append_runtime_event(state: Dictionary, tag: String, payload: Dictionary) -> Dictionary:
	var runtime_events: Array = (state.get("runtime_events", []) as Array).duplicate(true)
	var timestamps: Array = (state.get("runtime_event_timestamps_ms", []) as Array).duplicate(true)
	runtime_events.append("- %s %s" % [tag, JSON.stringify(payload)])
	timestamps.append(Time.get_ticks_msec())
	timestamps = _trim_runtime_event_rate_window_array(timestamps, float(state.get("event_rate_window_seconds", 30.0)))
	var max_runtime_events := int(state.get("max_runtime_events", 80))
	if runtime_events.size() > max_runtime_events:
		runtime_events = runtime_events.slice(runtime_events.size() - max_runtime_events, runtime_events.size())
	_append_audit_event(str(state.get("audit_trail_path", "")), tag, payload)
	return {
		"updates": {
			"runtime_events": runtime_events,
			"runtime_event_timestamps_ms": timestamps,
			"render_pc_centric_view": true,
		}
	}


func append_audit_event(state: Dictionary, tag: String, payload: Dictionary) -> Dictionary:
	_append_audit_event(str(state.get("audit_trail_path", "")), tag, payload)
	return {}


func runtime_event_rate_per_second(state: Dictionary) -> float:
	var timestamps: Array = (state.get("runtime_event_timestamps_ms", []) as Array).duplicate(true)
	timestamps = _trim_runtime_event_rate_window_array(timestamps, float(state.get("event_rate_window_seconds", 30.0)))
	if timestamps.is_empty():
		return 0.0
	return float(timestamps.size()) / float(state.get("event_rate_window_seconds", 30.0))


func trim_runtime_event_rate_window(state: Dictionary) -> Dictionary:
	var timestamps: Array = (state.get("runtime_event_timestamps_ms", []) as Array).duplicate(true)
	timestamps = _trim_runtime_event_rate_window_array(timestamps, float(state.get("event_rate_window_seconds", 30.0)))
	return {"updates": {"runtime_event_timestamps_ms": timestamps}}


func extract_error_code(message: String) -> String:
	if message == "":
		return "none"
	var marker := "code="
	var idx := message.find(marker)
	if idx < 0:
		return "n/a"
	var start := idx + marker.length()
	var end := start
	while end < message.length():
		var ch := message[end]
		if ch == '|' or ch == ' ' or ch == ')' or ch == ',':
			break
		end += 1
	var value := message.substr(start, end - start).strip_edges()
	if value == "":
		return "n/a"
	return value


func _append_audit_event(audit_trail_path: String, tag: String, payload: Dictionary) -> void:
	if audit_trail_path == "":
		return
	_ensure_parent_dir(audit_trail_path)
	var wf := FileAccess.open(audit_trail_path, FileAccess.READ_WRITE)
	if wf == null:
		wf = FileAccess.open(audit_trail_path, FileAccess.WRITE)
	if wf == null:
		return
	wf.seek_end()
	var entry := {
		"ts": Time.get_datetime_string_from_system(false, true),
		"tag": tag,
		"payload": payload,
	}
	wf.store_string(JSON.stringify(entry, "") + "\n")
	wf.close()


func _trim_runtime_event_rate_window_array(timestamps: Array, event_rate_window_seconds: float) -> Array:
	if timestamps.is_empty():
		return timestamps
	var now_ms := Time.get_ticks_msec()
	var min_ms := int(event_rate_window_seconds * 1000.0)
	while not timestamps.is_empty() and now_ms - int(timestamps[0]) > min_ms:
		timestamps.remove_at(0)
	return timestamps


func _ensure_parent_dir(path_text: String) -> void:
	var abs_path := path_text
	if path_text.begins_with("user://") or path_text.begins_with("res://"):
		abs_path = ProjectSettings.globalize_path(path_text)
	var parent_dir := abs_path.get_base_dir()
	if parent_dir != "":
		DirAccess.make_dir_recursive_absolute(parent_dir)