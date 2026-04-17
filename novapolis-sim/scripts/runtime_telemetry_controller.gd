extends RefCounted

class_name RuntimeTelemetryController


func refresh_latest_eval_summary(state: Dictionary, force: bool) -> Dictionary:
	if not bool(state.get("agent_submenu_open", false)) and not force:
		return {}

	var now_ms := Time.get_ticks_msec()
	var last_refresh_ms := int(state.get("last_eval_summary_refresh_ms", -1))
	var refresh_interval_s := float(state.get("eval_summary_refresh_interval_seconds", 8.0))
	if not force and last_refresh_ms >= 0:
		var delta_s := float(now_ms - last_refresh_ms) / 1000.0
		if delta_s < maxf(2.0, refresh_interval_s):
			return {}

	var updates: Dictionary = {
		"last_eval_summary_refresh_ms": now_ms,
	}
	var python_exec := resolve_python_executable(state)
	var summary_script_abs := ProjectSettings.globalize_path(str(state.get("eval_summary_script_path", "")))
	if not FileAccess.file_exists(summary_script_abs):
		updates["latest_eval_summary_text"] = "Letzte Eval-Runs: Script fehlt"
		return {"updates": updates}

	var output := []
	var exec_code := OS.execute(python_exec, [summary_script_abs, "--count", "3"], output, true)
	if exec_code != 0 or output.is_empty():
		updates["latest_eval_summary_text"] = "Letzte Eval-Runs: nicht verfügbar"
		return {"updates": updates}

	var raw := str(output[0]).strip_edges()
	if raw == "":
		updates["latest_eval_summary_text"] = "Letzte Eval-Runs: keine Daten"
		return {"updates": updates}

	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		updates["latest_eval_summary_text"] = "Letzte Eval-Runs: Antwort unlesbar"
		return {"updates": updates}

	var payload: Dictionary = parsed
	var runs_any = payload.get("runs", [])
	if typeof(runs_any) != TYPE_ARRAY:
		updates["latest_eval_summary_text"] = "Letzte Eval-Runs: keine Daten"
		return {"updates": updates}

	var runs: Array = runs_any
	if runs.is_empty():
		updates["latest_eval_summary_text"] = "Letzte Eval-Runs: keine Runs gefunden"
		updates["latest_eval_runs"] = []
		updates["ai_trend_summary_text"] = "Trendkarte: keine Daten"
		return {"updates": updates}

	var lines: Array[String] = ["Letzte Eval-Runs (Success Rate):"]
	var pcts: Array[float] = []
	var avg_duration_values: Array[float] = []
	for run_any in runs:
		if typeof(run_any) != TYPE_DICTIONARY:
			continue
		var run: Dictionary = run_any
		var stamp := str(run.get("timestamp", "n/a"))
		var pct := _to_float_or_default(run.get("success_rate_percent", null), -1.0)
		var ok_count := int(run.get("success", 0))
		var total_count := int(run.get("items", 0))
		var avg_ms := _to_float_or_default(run.get("avg_duration_ms", null), -1.0)
		lines.append("- %s: %.1f%% (%d/%d), avg %.0fms" % [stamp, pct, ok_count, total_count, maxf(0.0, avg_ms)])
		if pct >= 0.0:
			pcts.append(pct)
		if avg_ms >= 0.0:
			avg_duration_values.append(avg_ms)

	var trend_line := build_ai_trend_summary(pcts, avg_duration_values)
	lines.append(trend_line)
	updates["latest_eval_runs"] = runs
	updates["ai_trend_summary_text"] = trend_line
	updates["latest_eval_summary_text"] = "\n".join(lines)
	return {"updates": updates}


func build_ai_trend_summary(pcts: Array[float], avg_duration_values: Array[float]) -> String:
	if pcts.is_empty():
		return "Trendkarte: n/a"
	var newest := pcts[0]
	var oldest := pcts[pcts.size() - 1]
	var delta := newest - oldest
	var min_pct := pcts[0]
	var max_pct := pcts[0]
	var sum_pct := 0.0
	for value in pcts:
		sum_pct += value
		min_pct = minf(min_pct, value)
		max_pct = maxf(max_pct, value)
	var avg_pct := sum_pct / float(pcts.size())

	var regression_status := "stabil"
	if delta <= -3.0:
		regression_status = "regression"
	elif delta >= 3.0:
		regression_status = "verbessert"

	var drift_status := "stable"
	if (max_pct - min_pct) >= 12.0:
		drift_status = "watch"

	var avg_ms_text := "n/a"
	if not avg_duration_values.is_empty():
		var sum_ms := 0.0
		for ms in avg_duration_values:
			sum_ms += ms
		avg_ms_text = "%.0f" % (sum_ms / float(avg_duration_values.size()))

	return "Trendkarte: pass=%.1f%% (delta=%+.1f) | regress=%s | drift=%s | avg_ms=%s" % [avg_pct, delta, regression_status, drift_status, avg_ms_text]


func refresh_system_metrics(state: Dictionary, force: bool) -> Dictionary:
	var updates: Dictionary = {}
	if not bool(state.get("enable_system_resource_monitoring", false)):
		updates["system_cpu_percent"] = -1.0
		updates["system_ram_percent"] = -1.0
		updates["system_gpu_vram_percent"] = -1.0
		updates["system_gpu_vram_used_mb"] = -1.0
		updates["system_gpu_vram_total_mb"] = -1.0
		updates["system_cpu_temp_c"] = -999.0
		updates["system_gpu_temp_c"] = -999.0
		return {"updates": updates}

	var now_ms := Time.get_ticks_msec()
	var last_refresh_ms := int(state.get("last_metrics_refresh_ms", -1))
	var refresh_interval_s := float(state.get("metrics_refresh_interval_seconds", 4.0))
	if not force and last_refresh_ms >= 0:
		var delta_s := float(now_ms - last_refresh_ms) / 1000.0
		if delta_s < maxf(1.0, refresh_interval_s):
			return {}
	updates["last_metrics_refresh_ms"] = now_ms

	var python_exec := resolve_python_executable(state)
	var metrics_script_abs := ProjectSettings.globalize_path(str(state.get("system_snapshot_script_path", "")))
	if not FileAccess.file_exists(metrics_script_abs):
		return {"updates": updates}

	var output := []
	var exec_code := OS.execute(python_exec, [metrics_script_abs], output, true)
	if exec_code != 0 or output.is_empty():
		return {"updates": updates}

	var raw := str(output[0]).strip_edges()
	if raw == "":
		return {"updates": updates}
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) != TYPE_DICTIONARY:
		return {"updates": updates}

	var payload: Dictionary = parsed
	updates["system_cpu_percent"] = _to_float_or_default(payload.get("cpu_percent", null), -1.0)
	updates["system_ram_percent"] = _to_float_or_default(payload.get("ram_percent", null), -1.0)
	updates["system_gpu_vram_percent"] = _to_float_or_default(payload.get("gpu_vram_percent", null), -1.0)
	updates["system_gpu_vram_used_mb"] = _to_float_or_default(payload.get("gpu_vram_used_mb", null), -1.0)
	updates["system_gpu_vram_total_mb"] = _to_float_or_default(payload.get("gpu_vram_total_mb", null), -1.0)
	updates["system_cpu_temp_c"] = _to_float_or_default(payload.get("cpu_temp_c", null), -999.0)
	updates["system_gpu_temp_c"] = _to_float_or_default(payload.get("gpu_temp_c", null), -999.0)
	return {"updates": updates}


func format_percent(value: float) -> String:
	if value < 0.0:
		return "n/a"
	return "%.1f%%" % value


func format_temperature(value_c: float) -> String:
	if value_c < -100.0:
		return "n/a"
	return "%.1fC" % value_c


func format_vram(state: Dictionary) -> String:
	var gpu_vram_percent := float(state.get("system_gpu_vram_percent", -1.0))
	var gpu_vram_used_mb := float(state.get("system_gpu_vram_used_mb", -1.0))
	var gpu_vram_total_mb := float(state.get("system_gpu_vram_total_mb", -1.0))
	if gpu_vram_percent < 0.0:
		return "n/a"
	if gpu_vram_used_mb >= 0.0 and gpu_vram_total_mb > 0.0:
		var used_gb := gpu_vram_used_mb / 1024.0
		var total_gb := gpu_vram_total_mb / 1024.0
		return "%.1f%% (%.1f/%.1fGB)" % [gpu_vram_percent, used_gb, total_gb]
	return "%.1f%%" % gpu_vram_percent


func effective_temperature_c(state: Dictionary) -> float:
	var gpu_temp_c := float(state.get("system_gpu_temp_c", -999.0))
	if gpu_temp_c > -100.0:
		return gpu_temp_c
	return float(state.get("system_cpu_temp_c", -999.0))


func resolve_python_executable(state: Dictionary) -> String:
	var preferred_res := str(state.get("server_python_path", ""))
	if preferred_res.strip_edges() == "":
		preferred_res = "res://../.venv/Scripts/python.exe"
	var preferred := ProjectSettings.globalize_path(preferred_res)
	if FileAccess.file_exists(preferred):
		return preferred
	var local_venv := ProjectSettings.globalize_path("res://../.venv/Scripts/python.exe")
	if FileAccess.file_exists(local_venv):
		return local_venv
	return "python"


func sim_runtime_status(state: Dictionary) -> Dictionary:
	var sim_client = state.get("sim_client", null)
	if sim_client != null and sim_client.has_method("get_runtime_status"):
		var payload = sim_client.call("get_runtime_status")
		if typeof(payload) == TYPE_DICTIONARY:
			return payload
	return {}


func derive_health_state(state: Dictionary, runtime_status: Dictionary) -> Dictionary:
	var failures := int(runtime_status.get("consecutive_failures", 0))
	var paused := bool(runtime_status.get("paused_due_to_failures", false))
	var last_status_message := str(state.get("last_status_message", ""))
	if last_status_message != "":
		var reason_text := last_status_message.split("|")[0].strip_edges()
		if reason_text == "":
			reason_text = "status error"
		return {"state": "degraded", "reason": reason_text}

	var server_pid := int(state.get("server_pid", -1))
	if server_pid > 0:
		var local_reason := "local pid=%d" % server_pid
		if paused or failures > 0:
			local_reason = "%s, poll=paused fail=%d" % [local_reason, failures]
		return {"state": "local", "reason": local_reason}

	if is_external_server_reachable(state, runtime_status):
		return {"state": "external", "reason": "reachable without local pid"}

	var offline_reason := "no successful poll yet"
	var last_success_ms := int(state.get("last_success_ms", -1))
	if last_success_ms >= 0:
		offline_reason = "last_ok expired"
	var server_status_text := str(state.get("server_status_text", "stopped"))
	if server_status_text != "stopped":
		offline_reason = server_status_text
	return {"state": "offline", "reason": offline_reason}


func is_external_server_reachable(state: Dictionary, runtime_status: Dictionary) -> bool:
	if str(state.get("last_status_message", "")) != "":
		return false
	var last_success_ms := int(state.get("last_success_ms", -1))
	if last_success_ms < 0:
		return false
	if int(state.get("server_pid", -1)) > 0:
		return false
	var step_interval := float(runtime_status.get("step_interval", 0.5))
	var max_age_s := maxf(1.2, step_interval * 3.0)
	var age_s := maxf(0.0, float(Time.get_ticks_msec() - last_success_ms) / 1000.0)
	return age_s <= max_age_s


func _to_float_or_default(value, default_value: float) -> float:
	if value is float:
		return value
	if value is int:
		return float(value)
	if value is String and value.is_valid_float():
		return value.to_float()
	return default_value