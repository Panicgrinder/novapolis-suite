extends RefCounted

class_name HubServerOpsController


func start_local_server(state: Dictionary) -> Dictionary:
	var script_abs := str(state.get("server_script_abs", ""))
	var python_exec := str(state.get("python_exec", "python"))
	if not FileAccess.file_exists(script_abs):
		return {
			"updates": {"server_status_text": "script missing"},
			"events": [_event_record("SERVER_START_FAILED", {"reason": "script_missing", "path": script_abs})],
		}

	var pid := int(OS.create_process(python_exec, [script_abs], false))
	if pid <= 0:
		return {
			"updates": {"server_status_text": "start failed"},
			"events": [_event_record("SERVER_START_FAILED", {"python": python_exec, "script": script_abs})],
		}

	return {
		"updates": {
			"server_pid": pid,
			"server_exit_reported": false,
			"server_status_text": "running (pid=%d)" % pid,
		},
		"events": [_event_record("SERVER_STARTED", {"pid": pid, "python": python_exec})],
	}


func stop_local_server(state: Dictionary) -> Dictionary:
	var server_pid := int(state.get("server_pid", -1))
	if server_pid <= 0:
		return {"updates": {"server_status_text": "stopped"}}

	var kill_rc := int(OS.kill(server_pid))
	if kill_rc == OK:
		return {
			"updates": {
				"server_pid": -1,
				"server_status_text": "stopped",
				"server_exit_reported": false,
			},
			"events": [_event_record("SERVER_STOPPED", {"pid": server_pid})],
		}

	return {
		"updates": {"server_status_text": "stop failed (rc=%d)" % kill_rc},
		"events": [_event_record("SERVER_STOP_FAILED", {"pid": server_pid, "rc": kill_rc})],
	}


func update_server_control_ui(state: Dictionary, health: Dictionary) -> Dictionary:
	var server_pid := int(state.get("server_pid", -1))
	var server_toggle_text := "Start Server"
	var server_state := str(health.get("state", "offline"))
	if server_pid > 0:
		server_toggle_text = "Stop Server"
	elif server_state == "external":
		server_toggle_text = "Start Local Server"
	return {
		"updates": {
			"server_toggle_text": server_toggle_text,
			"server_status_label_text": "Server: %s" % server_state,
		}
	}


func refresh_server_runtime_state(state: Dictionary) -> Dictionary:
	var server_pid := int(state.get("server_pid", -1))
	if server_pid <= 0:
		return {}
	if OS.is_process_running(server_pid):
		return {}
	if bool(state.get("server_exit_reported", false)):
		return {}
	return {
		"updates": {
			"server_pid": -1,
			"server_status_text": "exited",
			"server_exit_reported": true,
			"refresh_server_control_ui": true,
		},
		"events": [_event_record("SERVER_EXITED", {"pid": server_pid})],
	}


func _event_record(tag: String, payload: Dictionary) -> Dictionary:
	return {"tag": tag, "payload": payload}