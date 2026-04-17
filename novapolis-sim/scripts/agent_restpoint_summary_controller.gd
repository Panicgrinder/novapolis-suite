extends RefCounted

class_name AgentRestpointSummaryController


func refresh_agent_restpoint_summaries(state: Dictionary) -> Dictionary:
	return {
		"updates": {
			"artifacts_summary_text": _build_artifacts_summary(state),
			"experiments_summary_text": _build_experiments_summary(state),
			"policy_sandbox_summary_text": _build_policy_sandbox_summary(state),
			"release_gate_summary_text": _build_release_gate_summary(state),
			"audit_trail_summary_text": _build_audit_trail_summary(state),
			"security_model_summary_text": "Security: destructive_guard=%s | token=%s" % [str(bool(state.get("destructive_guard_enabled", true))), str(state.get("destructive_guard_token", "confirm"))],
		}
	}


func _build_artifacts_summary(state: Dictionary) -> String:
	var dataset_ref := str(state.get("active_dataset_name", ""))
	var dataset_tag := str(state.get("active_dataset_tag", ""))
	if dataset_ref == "":
		dataset_ref = "n/a"
	elif dataset_tag != "":
		dataset_ref = "%s@%s" % [dataset_ref, dataset_tag]

	var synonym_ref := str(state.get("active_synonym_set", ""))
	var synonym_tag := str(state.get("active_synonym_tag", ""))
	if synonym_ref == "":
		synonym_ref = "n/a"
	elif synonym_tag != "":
		synonym_ref = "%s@%s" % [synonym_ref, synonym_tag]

	var model_ref := str(state.get("finetune_output_name", "lora-agent-hub"))
	if int(state.get("last_finetune_exit_code", -1)) != 0:
		model_ref = "n/a"

	var reports_ref := "tests=%s types=%s cov=%s" % [str(state.get("quality_tests_last", "n/a")), str(state.get("quality_types_last", "n/a")), str(state.get("quality_coverage_last", "n/a"))]
	return "Artifacts: dataset=%s | synonyms=%s | model=%s | %s" % [dataset_ref, synonym_ref, model_ref, reports_ref]


func _build_experiments_summary(state: Dictionary) -> String:
	var latest_eval_runs_any = state.get("latest_eval_runs", [])
	if typeof(latest_eval_runs_any) != TYPE_ARRAY:
		return "Experiments: n/a"
	var latest_eval_runs: Array = latest_eval_runs_any
	if latest_eval_runs.size() < 2:
		return "Experiments: n/a (mind. 2 Runs erforderlich)"
	var latest_any = latest_eval_runs[0]
	var prev_any = latest_eval_runs[1]
	if typeof(latest_any) != TYPE_DICTIONARY or typeof(prev_any) != TYPE_DICTIONARY:
		return "Experiments: n/a"
	var latest: Dictionary = latest_any
	var previous: Dictionary = prev_any
	var latest_pct := _to_float_or_default(latest.get("success_rate_percent", null), -1.0)
	var prev_pct := _to_float_or_default(previous.get("success_rate_percent", null), -1.0)
	if latest_pct < 0.0 or prev_pct < 0.0:
		return "Experiments: n/a"
	var delta := latest_pct - prev_pct
	var tag := "stable"
	if delta >= 2.0:
		tag = "A>B"
	elif delta <= -2.0:
		tag = "A<B"
	return "Experiments: A/B delta=%+.1fpp | tag=%s" % [delta, tag]


func _build_policy_sandbox_summary(state: Dictionary) -> String:
	var mode := "balanced"
	var policy := "default"
	var strict := "normal"
	var advanced_settings_path := str(state.get("advanced_settings_path", ""))
	if advanced_settings_path != "" and FileAccess.file_exists(advanced_settings_path):
		var rf := FileAccess.open(advanced_settings_path, FileAccess.READ)
		if rf != null:
			var parsed = JSON.parse_string(rf.get_as_text())
			rf.close()
			if typeof(parsed) == TYPE_DICTIONARY:
				var payload: Dictionary = parsed
				mode = str(payload.get("mode", mode))
				policy = str(payload.get("policy_profile", policy))
				strict = str(payload.get("strictness_level", strict))
	var quality_ok := str(state.get("quality_tests_last", "")) == "PASS" and str(state.get("quality_types_last", "")) == "PASS"
	var gate := "ready" if quality_ok else "hold"
	return "Policy Sandbox: mode=%s | policy=%s | strict=%s | gate=%s" % [mode, policy, strict, gate]


func _build_release_gate_summary(state: Dictionary) -> String:
	var coverage_value := _to_float_or_default(str(state.get("quality_coverage_last", "")).replace("%", ""), -1.0)
	var tests_ok := str(state.get("quality_tests_last", "")) == "PASS"
	var types_ok := str(state.get("quality_types_last", "")) == "PASS"
	var cov_ok := coverage_value >= 80.0
	var regression := str(state.get("ai_trend_summary_text", "")).find("regress=regression") >= 0
	var safety_ok := bool(state.get("destructive_guard_enabled", true))
	var go := tests_ok and types_ok and cov_ok and (not regression) and safety_ok
	return "Release Gate: %s | tests=%s | types=%s | cov=%s | regression=%s | safety=%s" % ["GO" if go else "NO-GO", str(tests_ok), str(types_ok), str(cov_ok), str(regression), str(safety_ok)]


func _build_audit_trail_summary(state: Dictionary) -> String:
	var audit_trail_path := str(state.get("audit_trail_path", ""))
	var abs_path := ProjectSettings.globalize_path(audit_trail_path)
	if not FileAccess.file_exists(abs_path):
		return "Audit Trail: entries=0"
	var rf := FileAccess.open(abs_path, FileAccess.READ)
	if rf == null:
		return "Audit Trail: unreadable"
	var count := 0
	var last_line := ""
	while not rf.eof_reached():
		var line := rf.get_line().strip_edges()
		if line == "":
			continue
		count += 1
		last_line = line
	rf.close()
	if count == 0:
		return "Audit Trail: entries=0"
	var tag := "n/a"
	var parsed = JSON.parse_string(last_line)
	if typeof(parsed) == TYPE_DICTIONARY:
		var payload: Dictionary = parsed
		tag = str(payload.get("tag", "n/a"))
	return "Audit Trail: entries=%d | last=%s" % [count, tag]


func _to_float_or_default(value, default_value: float) -> float:
	if value is float:
		return value
	if value is int:
		return float(value)
	if value is String and value.is_valid_float():
		return value.to_float()
	return default_value