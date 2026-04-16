extends RefCounted

class_name AgentRuntimeController


func confirm_destructive_action(state: Dictionary, action_key: String, hint_text: String) -> Dictionary:
	if not bool(state.get("destructive_guard_enabled", true)):
		return {"confirmed": true, "updates": {}}
	var now_ms := int(state.get("now_ms", Time.get_ticks_msec()))
	var armed_action := str(state.get("destructive_armed_action", ""))
	var armed_until_ms := int(state.get("destructive_armed_until_ms", -1))
	if armed_action == action_key and now_ms <= armed_until_ms:
		return {
			"confirmed": true,
			"updates": {
				"destructive_armed_action": "",
				"destructive_armed_until_ms": -1,
			},
		}
	var guard_window_ms := int(state.get("destructive_guard_window_ms", 8000))
	return {
		"confirmed": false,
		"updates": {
			"destructive_armed_action": action_key,
			"destructive_armed_until_ms": now_ms + guard_window_ms,
			"form_status_text": hint_text,
		},
		"events": [_event_record("SECURITY_GUARD", {"action": action_key, "status": "armed", "valid_for_ms": guard_window_ms})],
	}


func handle_eval_run(state: Dictionary) -> Dictionary:
	var mode := str(state.get("studio_mode", "operate"))
	if mode == "author":
		return {
			"open_form": "jobs",
			"events": [_event_record("AGENT_ACTION", {"action": "jobs", "mode": mode, "status": "form_opened"})],
		}
	if mode != "operate":
		return {
			"events": [_event_record("AGENT_ACTION", {"action": "eval_run", "mode": mode, "status": "blocked", "reason": "author_mode"})],
		}

	var eval_pid := int(state.get("eval_pid", -1))
	if eval_pid > 0:
		var confirm_result := confirm_destructive_action(state, "eval_stop", "Eval Stop: zweite Betaetigung zur Bestaetigung")
		if not bool(confirm_result.get("confirmed", false)):
			return confirm_result
		var stop_updates: Dictionary = confirm_result.get("updates", {})
		stop_updates["eval_pid"] = -1
		stop_updates["last_eval_exit_code"] = 130
		return {
			"updates": stop_updates,
			"events": [_event_record("AGENT_ACTION", {"action": "eval_run", "mode": mode, "status": "stop_requested", "pid": eval_pid, "rc": int(OS.kill(eval_pid))})],
		}

	var python_exec := str(state.get("python_exec", "python")).strip_edges()
	var eval_script_abs := str(state.get("eval_script_abs", "")).strip_edges()
	if eval_script_abs == "" or not FileAccess.file_exists(eval_script_abs):
		return {
			"events": [_event_record("AGENT_ACTION", {"action": "eval_run", "status": "failed", "reason": "script_missing", "path": eval_script_abs})],
		}

	var args := _build_eval_suite_args(
		eval_script_abs,
		str(state.get("agent_eval_suite", "neutral")),
		int(state.get("eval_quick_limit", 20)),
		str(state.get("repo_root", "")),
	)
	var pid := int(OS.create_process(python_exec, args, false))
	if pid <= 0:
		return {
			"events": [_event_record("AGENT_ACTION", {"action": "eval_run", "status": "start_failed", "python": python_exec})],
		}

	return {
		"updates": {
			"eval_pid": pid,
			"eval_started_ms": Time.get_ticks_msec(),
			"last_eval_exit_code": -1,
		},
		"events": [_event_record("AGENT_ACTION", {"action": "eval_run", "mode": mode, "status": "started", "pid": pid, "suite": str(state.get("agent_eval_suite", "neutral"))})],
	}


func handle_finetune_stop(state: Dictionary) -> Dictionary:
	var finetune_pid := int(state.get("finetune_pid", -1))
	if finetune_pid <= 0:
		return {}
	var confirm_result := confirm_destructive_action(state, "finetune_stop", "Finetune Stop: zweite Betaetigung zur Bestaetigung")
	if not bool(confirm_result.get("confirmed", false)):
		return confirm_result
	var stop_updates: Dictionary = confirm_result.get("updates", {})
	stop_updates["finetune_pid"] = -1
	stop_updates["last_finetune_exit_code"] = 130
	stop_updates["finetune_status_text"] = "Finetune: stop requested"
	return {
		"updates": stop_updates,
		"events": [_event_record("AGENT_FINETUNE", {"action": "stop_requested", "pid": finetune_pid, "rc": int(OS.kill(finetune_pid))})],
	}


func apply_finetune_form_payload(payload: Dictionary, state: Dictionary) -> Dictionary:
	if int(state.get("finetune_pid", -1)) > 0:
		return {"updates": {"form_status_text": "Form: Finetune laeuft bereits"}}

	var profile := _sanitize_name(str(payload.get("profile", "baseline")))
	if profile == "":
		profile = "baseline"
	var base_model := str(payload.get("base_model", "sshleifer/tiny-gpt2")).strip_edges()
	if base_model == "":
		return {"updates": {"form_status_text": "Form: base_model fehlt"}}

	var output_name := _sanitize_name(str(payload.get("output_name", state.get("finetune_output_name", "lora-agent-hub"))))
	if output_name == "":
		output_name = "lora-agent-hub"

	var epochs := int(payload.get("epochs", 1))
	var max_steps := int(payload.get("max_steps", 10))
	var batch_size := int(payload.get("batch_size", 1))
	var lr := _to_float_or_default(payload.get("lr", 0.0002), 0.0002)
	var no_check := bool(payload.get("no_check", true))
	if epochs < 1:
		return {"updates": {"form_status_text": "Form: epochs muss >= 1 sein"}}
	if max_steps < 1:
		return {"updates": {"form_status_text": "Form: max_steps muss >= 1 sein"}}
	if batch_size < 1:
		return {"updates": {"form_status_text": "Form: batch_size muss >= 1 sein"}}
	if lr <= 0.0:
		return {"updates": {"form_status_text": "Form: lr muss > 0 sein"}}

	var train_file := str(payload.get("train_file", "")).strip_edges()
	if train_file == "":
		train_file = _resolve_finetune_train_file(
			str(state.get("active_dataset_name", "")),
			str(state.get("fallback_finetune_train_file_res", "res://../novapolis_agent/eval/datasets/training/chronistin_operativ_kurz.v1.jsonl")),
		)
	if train_file == "":
		return {"updates": {"form_status_text": "Form: keine Train-Datei verfuegbar"}}

	var train_path_abs := ProjectSettings.globalize_path(train_file) if train_file.begins_with("user://") or train_file.begins_with("res://") else train_file
	if not FileAccess.file_exists(train_path_abs):
		return {"updates": {"form_status_text": "Form: train_file fehlt"}}

	var python_exec := str(state.get("python_exec", "python")).strip_edges()
	var script_abs := str(state.get("finetune_script_abs", "")).strip_edges()
	if script_abs == "" or not FileAccess.file_exists(script_abs):
		return {
			"updates": {
				"finetune_status_text": "Finetune: script fehlt",
				"form_status_text": "Form: Finetune konnte nicht gestartet werden",
			},
			"events": [_event_record("AGENT_FINETUNE", {"action": "start_failed", "reason": "script_missing", "path": script_abs})],
		}

	var output_abs := ProjectSettings.globalize_path("res://../outputs/%s" % output_name)
	var args: Array[String] = [
		script_abs,
		"--train-file",
		train_path_abs,
		"--model",
		base_model,
		"--output",
		output_abs,
		"--per-device-train-batch-size",
		str(batch_size),
		"--epochs",
		str(epochs),
		"--max-steps",
		str(max_steps),
		"--lr",
		str(lr),
	]
	if no_check:
		args.append("--no-check")

	var pid := int(OS.create_process(python_exec, args, false))
	if pid <= 0:
		return {
			"updates": {
				"finetune_status_text": "Finetune: start fehlgeschlagen",
				"form_status_text": "Form: Finetune konnte nicht gestartet werden",
			},
			"events": [_event_record("AGENT_FINETUNE", {"action": "start_failed", "python": python_exec})],
		}

	return {
		"updates": {
			"finetune_pid": pid,
			"finetune_started_ms": Time.get_ticks_msec(),
			"last_finetune_exit_code": -1,
			"finetune_profile": profile,
			"finetune_base_model": base_model,
			"finetune_output_name": output_name,
			"finetune_epochs": epochs,
			"finetune_max_steps": max_steps,
			"finetune_batch_size": batch_size,
			"finetune_lr": lr,
			"finetune_status_text": "Finetune: running (%s, e=%d, s=%d, b=%d, lr=%.5f)" % [profile, epochs, max_steps, batch_size, lr],
			"form_status_text": "Form: Finetune gestartet (%s, %s)" % [profile, base_model],
		},
		"events": [_event_record("AGENT_FINETUNE", {"action": "started", "pid": pid, "profile": profile, "model": base_model, "output": output_abs})],
	}


func apply_jobs_form_payload(payload: Dictionary, state: Dictionary) -> Dictionary:
	var target := str(payload.get("target", "new"))
	if target != "new" and target != "retry_latest" and target != "cancel_latest":
		return {"updates": {"form_status_text": "Form: target muss new/retry_latest/cancel_latest sein"}}

	var queue_path := str(state.get("jobs_queue_path", "user://agent_user_data/jobs/queue.json"))
	var queue_payload := _load_jobs_queue_payload(queue_path)
	var jobs := _jobs_array_from_payload(queue_payload)

	if target == "retry_latest":
		var retry_index := _find_latest_job_index_by_status(jobs, ["failed", "cancelled"])
		if retry_index < 0:
			return {"updates": {"form_status_text": "Form: kein fehlgeschlagener/abgebrochener Job fuer Retry"}}
		var base_any = jobs[retry_index]
		if typeof(base_any) != TYPE_DICTIONARY:
			return {"updates": {"form_status_text": "Form: Retry-Quelle ist ungueltig"}}
		var base_job: Dictionary = base_any
		var base_name := _sanitize_name(str(base_job.get("name", "job")))
		if base_name == "":
			base_name = "job"
		var retry_name := "%s_retry" % base_name
		var attempt := int(base_job.get("attempt", 1)) + 1
		jobs.append({
			"id": "job_%d" % Time.get_ticks_msec(),
			"name": retry_name,
			"type": str(base_job.get("type", "eval")),
			"status": "queued",
			"priority": int(base_job.get("priority", 10)),
			"created_at": Time.get_datetime_string_from_system(false, true),
			"retry_of": str(base_job.get("id", "")),
			"attempt": attempt,
			"payload": base_job.get("payload", {}),
		})
		queue_payload["jobs"] = jobs
		queue_payload["updated_at"] = Time.get_datetime_string_from_system(false, true)
		if not _write_jobs_queue_payload(queue_path, queue_payload):
			return {"updates": {"form_status_text": "Form: Jobs-Queue konnte nicht gespeichert werden"}}
		return {
			"updates": {
				"jobs_status_text": _build_jobs_status_text(jobs),
				"form_status_text": "Form: Retry eingereiht (%s)" % retry_name,
			},
			"events": [_event_record("AGENT_FORM", {"kind": "jobs", "action": "retry_latest", "retry_of": str(base_job.get("id", "")), "name": retry_name, "queue_size": jobs.size(), "path": queue_path})],
		}

	if target == "cancel_latest":
		var cancel_index := _find_latest_job_index_by_status(jobs, ["queued", "running"])
		if cancel_index < 0:
			return {"updates": {"form_status_text": "Form: kein aktiver Job fuer Cancel"}}
		var cancel_any = jobs[cancel_index]
		if typeof(cancel_any) != TYPE_DICTIONARY:
			return {"updates": {"form_status_text": "Form: Cancel-Ziel ist ungueltig"}}
		var cancel_job: Dictionary = cancel_any
		cancel_job["status"] = "cancelled"
		cancel_job["cancelled_at"] = Time.get_datetime_string_from_system(false, true)
		cancel_job["cancel_reason"] = str(payload.get("notes", "manual_cancel"))
		jobs[cancel_index] = cancel_job
		queue_payload["jobs"] = jobs
		queue_payload["updated_at"] = Time.get_datetime_string_from_system(false, true)
		if not _write_jobs_queue_payload(queue_path, queue_payload):
			return {"updates": {"form_status_text": "Form: Jobs-Queue konnte nicht gespeichert werden"}}
		return {
			"updates": {
				"jobs_status_text": _build_jobs_status_text(jobs),
				"form_status_text": "Form: Job abgebrochen (%s)" % str(cancel_job.get("name", "job")),
			},
			"events": [_event_record("AGENT_FORM", {"kind": "jobs", "action": "cancel_latest", "id": str(cancel_job.get("id", "")), "name": str(cancel_job.get("name", "job")), "queue_size": jobs.size(), "path": queue_path})],
		}

	var job_name := _sanitize_name(str(payload.get("job_name", "job")))
	if job_name == "":
		return {"updates": {"form_status_text": "Form: job_name fehlt"}}
	var job_type := _sanitize_name(str(payload.get("job_type", "eval")))
	if job_type == "":
		job_type = "eval"
	var priority := clampi(int(payload.get("priority", 10)), 0, 100)
	if not bool(payload.get("enqueue", true)):
		return {"updates": {"form_status_text": "Form: enqueue=false, kein Job angelegt"}}
	var job_payload_any = payload.get("payload", {})
	var job_payload: Dictionary = job_payload_any if typeof(job_payload_any) == TYPE_DICTIONARY else {}
	jobs.append({
		"id": "job_%d" % Time.get_ticks_msec(),
		"name": job_name,
		"type": job_type,
		"status": "queued",
		"priority": priority,
		"attempt": 1,
		"created_at": Time.get_datetime_string_from_system(false, true),
		"payload": job_payload,
	})
	queue_payload["jobs"] = jobs
	queue_payload["updated_at"] = Time.get_datetime_string_from_system(false, true)
	if not _write_jobs_queue_payload(queue_path, queue_payload):
		return {"updates": {"form_status_text": "Form: Jobs-Queue konnte nicht gespeichert werden"}}
	return {
		"updates": {
			"jobs_status_text": _build_jobs_status_text(jobs),
			"form_status_text": "Form: Job eingereiht (%s, prio=%d)" % [job_type, priority],
		},
		"events": [_event_record("AGENT_FORM", {"kind": "jobs", "action": "enqueue", "name": job_name, "job_type": job_type, "priority": priority, "queue_size": jobs.size(), "path": queue_path})],
	}


func load_jobs_state(queue_path: String) -> Dictionary:
	var queue_payload := _load_jobs_queue_payload(queue_path)
	var jobs := _jobs_array_from_payload(queue_payload)
	return {"updates": {"jobs_status_text": _build_jobs_status_text(jobs)}}


func refresh_finetune_runtime_state(state: Dictionary) -> Dictionary:
	var finetune_pid := int(state.get("finetune_pid", -1))
	if finetune_pid <= 0:
		return {}
	var finetune_profile := str(state.get("finetune_profile", "baseline"))
	var finetune_output_name := str(state.get("finetune_output_name", "lora-agent-hub"))
	var epochs := int(state.get("finetune_epochs", 1))
	var max_steps := int(state.get("finetune_max_steps", 10))
	var batch_size := int(state.get("finetune_batch_size", 1))
	var lr := _to_float_or_default(state.get("finetune_lr", 0.0002), 0.0002)
	var started_ms := int(state.get("finetune_started_ms", Time.get_ticks_msec()))
	if OS.is_process_running(finetune_pid):
		var elapsed_s := maxf(0.0, float(Time.get_ticks_msec() - started_ms) / 1000.0)
		return {
			"updates": {
				"finetune_status_text": "Finetune: running (%s, %.1fs, e=%d, s=%d, b=%d, lr=%.5f)" % [finetune_profile, elapsed_s, epochs, max_steps, batch_size, lr],
			},
		}

	var exit_code := int(OS.get_process_exit_code(finetune_pid))
	var total_runtime_s := maxf(0.0, float(Time.get_ticks_msec() - started_ms) / 1000.0)
	var updates := {
		"last_finetune_exit_code": exit_code,
		"finetune_pid": -1,
	}
	if exit_code == 0:
		updates["finetune_status_text"] = "Finetune: done (%s, %.1fs, e=%d, s=%d, b=%d, lr=%.5f)" % [finetune_output_name, total_runtime_s, epochs, max_steps, batch_size, lr]
		updates["agent_summary_refresh_pending"] = true
		updates["agent_summary_refresh_due_ms"] = Time.get_ticks_msec() + 400
	else:
		updates["finetune_status_text"] = "Finetune: failed (exit=%d, %.1fs, e=%d, s=%d)" % [exit_code, total_runtime_s, epochs, max_steps]
	return {
		"updates": updates,
		"events": [_event_record("AGENT_FINETUNE", {"action": "finished", "pid": finetune_pid, "exit_code": exit_code, "profile": finetune_profile, "model": str(state.get("finetune_base_model", "sshleifer/tiny-gpt2"))})],
	}


func refresh_eval_runtime_state(state: Dictionary) -> Dictionary:
	var eval_pid := int(state.get("eval_pid", -1))
	if eval_pid <= 0:
		return {}
	if OS.is_process_running(eval_pid):
		return {}
	var exit_code := int(OS.get_process_exit_code(eval_pid))
	return {
		"updates": {
			"last_eval_exit_code": exit_code,
			"eval_pid": -1,
		},
		"events": [_event_record("AGENT_ACTION", {"action": "eval_run", "status": "finished", "pid": eval_pid, "exit_code": exit_code})],
		"refresh_latest_eval_summary": true,
	}


func _build_eval_suite_args(eval_script_abs: String, eval_suite: String, eval_quick_limit: int, repo_root: String) -> Array[String]:
	var args: Array[String] = [
		eval_script_abs,
		"--asgi",
		"--limit",
		str(maxi(1, eval_quick_limit)),
		"--quiet",
	]
	match eval_suite:
		"rpg":
			args.append_array([
				"--profile",
				"unrestricted",
				"--checks",
				"must_include,keywords_any,keywords_at_least,not_include,regex",
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\rpg\\rpg_21_40_fantasy.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\rpg\\rpg_41_60_dialog.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\rpg\\rpg_61_80_szenen.v1.jsonl" % repo_root,
			])
		"quality_de":
			args.append_array([
				"--profile",
				"eval",
				"--tag",
				"quality_de",
				"--checks",
				"must_include,keywords_any,keywords_at_least,not_include,regex,quality_de",
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\quality_de_core.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\quality_de_drift.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\quality_de_canary.v1.jsonl" % repo_root,
			])
		_:
			args.append_array([
				"--profile",
				"eval",
				"--checks",
				"must_include,keywords_any,keywords_at_least,not_include,regex,rpg_style,quality_de",
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\neutral_01_20_core.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\neutral_81_100_tech.v1.jsonl" % repo_root,
				"--packages",
				"%s\\novapolis_agent\\eval\\datasets\\neutral\\neutral_smoke.v1.jsonl" % repo_root,
			])
	return args


func _resolve_finetune_train_file(active_dataset_name: String, fallback_train_file_res: String) -> String:
	if active_dataset_name.strip_edges() != "":
		var user_dataset := "user://agent_user_data/datasets/%s.jsonl" % active_dataset_name
		var user_dataset_abs := ProjectSettings.globalize_path(user_dataset)
		if FileAccess.file_exists(user_dataset_abs):
			return user_dataset_abs
	var fallback_abs := ProjectSettings.globalize_path(fallback_train_file_res)
	if FileAccess.file_exists(fallback_abs):
		return fallback_abs
	return ""


func _load_jobs_queue_payload(queue_path: String) -> Dictionary:
	_ensure_parent_dir(queue_path)
	var queue_payload: Dictionary = {
		"jobs": [],
		"updated_at": Time.get_datetime_string_from_system(false, true),
	}
	if not FileAccess.file_exists(queue_path):
		return queue_payload
	var rf := FileAccess.open(queue_path, FileAccess.READ)
	if rf == null:
		return queue_payload
	var raw := rf.get_as_text()
	rf.close()
	var parsed = JSON.parse_string(raw)
	if typeof(parsed) == TYPE_DICTIONARY:
		queue_payload = parsed
	if typeof(queue_payload.get("jobs", [])) != TYPE_ARRAY:
		queue_payload["jobs"] = []
	return queue_payload


func _jobs_array_from_payload(queue_payload: Dictionary) -> Array:
	var jobs_any = queue_payload.get("jobs", [])
	if typeof(jobs_any) != TYPE_ARRAY:
		return []
	return jobs_any


func _write_jobs_queue_payload(queue_path: String, queue_payload: Dictionary) -> bool:
	_ensure_parent_dir(queue_path)
	var wf := FileAccess.open(queue_path, FileAccess.WRITE)
	if wf == null:
		return false
	wf.store_string(JSON.stringify(queue_payload, "  "))
	wf.close()
	return true


func _find_latest_job_index_by_status(jobs: Array, statuses: Array[String]) -> int:
	for i in range(jobs.size() - 1, -1, -1):
		var item_any = jobs[i]
		if typeof(item_any) != TYPE_DICTIONARY:
			continue
		var item: Dictionary = item_any
		if statuses.has(str(item.get("status", ""))):
			return i
	return -1


func _build_jobs_status_text(jobs: Array) -> String:
	if jobs.is_empty():
		return "Jobs: queued=0"
	var queued := 0
	var running := 0
	var failed := 0
	var cancelled := 0
	for item_any in jobs:
		if typeof(item_any) != TYPE_DICTIONARY:
			continue
		var item: Dictionary = item_any
		var status := str(item.get("status", "queued"))
		if status == "queued":
			queued += 1
		elif status == "running":
			running += 1
		elif status == "failed":
			failed += 1
		elif status == "cancelled":
			cancelled += 1
	var latest_name := "job"
	var latest_type := "n/a"
	var latest_status := "n/a"
	for i in range(jobs.size() - 1, -1, -1):
		var latest_any = jobs[i]
		if typeof(latest_any) != TYPE_DICTIONARY:
			continue
		var latest: Dictionary = latest_any
		latest_name = str(latest.get("name", "job"))
		latest_type = str(latest.get("type", "n/a"))
		latest_status = str(latest.get("status", "n/a"))
		break
	return "Jobs: queued=%d | running=%d | failed=%d | cancelled=%d | latest=%s (%s/%s)" % [queued, running, failed, cancelled, latest_name, latest_type, latest_status]


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


func _ensure_parent_dir(path_text: String) -> void:
	var abs_path := ProjectSettings.globalize_path(path_text) if path_text.begins_with("user://") or path_text.begins_with("res://") else path_text
	var parent_dir := abs_path.get_base_dir()
	if parent_dir != "":
		DirAccess.make_dir_recursive_absolute(parent_dir)


func _event_record(tag: String, payload: Dictionary) -> Dictionary:
	return {"tag": tag, "payload": payload}


func _to_float_or_default(value, default_value: float) -> float:
	if value is float:
		return value
	if value is int:
		return float(value)
	if value is String and value.is_valid_float():
		return value.to_float()
	return default_value
