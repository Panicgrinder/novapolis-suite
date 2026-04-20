extends RefCounted

class_name AgentFormSessionController


var _form_kind: String = ""
var _form_mode_value: String = "clean"
var _form_target_value: String = "new"
var _template_signature: String = ""
var _form_controls: Dictionary = {}


func form_kind() -> String:
	return _form_kind


func form_mode_value() -> String:
	return _form_mode_value


func form_target_value() -> String:
	return _form_target_value


func open_form(form_controller: AgentFormController, kind: String, state: Dictionary) -> Dictionary:
	var form_state := form_controller.open_form(kind, state)
	_form_kind = str(form_state.get("form_kind", kind))
	_form_mode_value = str(form_state.get("form_mode_value", _form_mode_value))
	_form_target_value = str(form_state.get("form_target_value", _form_target_value))
	_template_signature = ""
	_form_controls = {}
	return form_state


func select_mode(form_controller: AgentFormController, index: int) -> bool:
	var options := form_controller.mode_options_for_kind(_form_kind)
	if index < 0 or index >= options.size():
		return false
	_form_mode_value = options[index]
	return true


func select_target(form_controller: AgentFormController, index: int) -> bool:
	var options := form_controller.target_options_for_kind(_form_kind)
	if index < 0 or index >= options.size():
		return false
	_form_target_value = options[index]
	return true


func build_payload_state(form_name: String, finetune_base_model: String) -> Dictionary:
	return {
		"form_kind": _form_kind,
		"form_mode_value": _form_mode_value,
		"form_target_value": _form_target_value,
		"form_name": form_name,
		"form_controls": _form_controls,
		"finetune_base_model": finetune_base_model,
	}


func build_persistence_state(base_state: Dictionary) -> Dictionary:
	var state := base_state.duplicate(true)
	state["form_target_value"] = _form_target_value
	state["form_mode_value"] = _form_mode_value
	return state


func refresh_form_ui(form_controller: AgentFormController, controls: Dictionary, state: Dictionary) -> void:
	var form_state_input := state.duplicate(true)
	form_state_input["form_kind"] = _form_kind
	form_state_input["form_mode_value"] = _form_mode_value
	form_state_input["form_target_value"] = _form_target_value
	form_state_input["template_signature"] = _template_signature
	form_state_input["form_controls"] = _form_controls

	var form_state := form_controller.refresh_form_ui(controls, form_state_input)
	_form_mode_value = str(form_state.get("form_mode_value", _form_mode_value))
	_form_target_value = str(form_state.get("form_target_value", _form_target_value))
	_template_signature = str(form_state.get("template_signature", _template_signature))
	var controls_any = form_state.get("form_controls", _form_controls)
	if typeof(controls_any) == TYPE_DICTIONARY:
		_form_controls = controls_any