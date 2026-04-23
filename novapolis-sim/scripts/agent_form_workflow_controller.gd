extends RefCounted

class_name AgentFormWorkflowController


func open_form(session_controller: AgentFormSessionController, form_controller: AgentFormController, kind: String, state: Dictionary) -> Dictionary:
	return session_controller.open_form(form_controller, kind, state)


func select_mode(session_controller: AgentFormSessionController, form_controller: AgentFormController, index: int) -> bool:
	return session_controller.select_mode(form_controller, index)


func select_target(session_controller: AgentFormSessionController, form_controller: AgentFormController, index: int) -> bool:
	return session_controller.select_target(form_controller, index)


func apply_form(
		session_controller: AgentFormSessionController,
		payload_controller: AgentAuthoringPayloadController,
		authoring_payload_state: Dictionary,
		persistence_controller: AgentAuthoringPersistenceController,
		persistence_state: Dictionary,
		runtime_controller: AgentRuntimeController,
		runtime_state: Dictionary,
		fallback_form_name: String
	) -> Dictionary:
	var form_kind := session_controller.form_kind()
	if form_kind == "":
		return {}

	var payload_result := payload_controller.build_form_payload(authoring_payload_state)
	var status_text := ""
	var payload_updates_any = payload_result.get("updates", {})
	if typeof(payload_updates_any) == TYPE_DICTIONARY:
		status_text = str((payload_updates_any as Dictionary).get("form_status_text", ""))

	var payload_any = payload_result.get("payload", {})
	if typeof(payload_any) != TYPE_DICTIONARY:
		return {"form_status_text": status_text}

	var payload: Dictionary = payload_any
	if payload.is_empty():
		return {"form_status_text": status_text}

	if form_kind == "datasets":
		return {
			"form_status_text": status_text,
			"pipeline": "persistence",
			"result": persistence_controller.apply_dataset_form_payload(payload, persistence_state),
		}

	if form_kind == "synonyms":
		return {
			"form_status_text": status_text,
			"pipeline": "persistence",
			"result": persistence_controller.apply_synonym_form_payload(payload, persistence_state),
		}

	if form_kind == "finetune":
		return {
			"form_status_text": status_text,
			"pipeline": "runtime",
			"result": runtime_controller.apply_finetune_form_payload(payload, runtime_state),
		}

	if form_kind == "profiles":
		return {
			"form_status_text": status_text,
			"pipeline": "persistence",
			"result": persistence_controller.apply_profile_form_payload(payload, persistence_state),
		}

	if form_kind == "advanced":
		return {
			"form_status_text": status_text,
			"pipeline": "persistence",
			"result": persistence_controller.apply_advanced_settings_form_payload(payload, persistence_state),
		}

	if form_kind == "jobs":
		var runtime_payload := payload.duplicate(true)
		if not runtime_payload.has("target"):
			runtime_payload["target"] = session_controller.form_target_value()
		if not runtime_payload.has("job_name"):
			runtime_payload["job_name"] = fallback_form_name
		if not runtime_payload.has("job_type"):
			runtime_payload["job_type"] = session_controller.form_mode_value()
		return {
			"form_status_text": status_text,
			"pipeline": "runtime",
			"result": runtime_controller.apply_jobs_form_payload(runtime_payload, runtime_state),
		}

	return {"form_status_text": "Form: Unbekannter Form-Typ"}