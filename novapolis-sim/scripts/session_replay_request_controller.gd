extends RefCounted

class_name SessionReplayRequestController

const SessionReplayHelpersRef = preload("res://scripts/session_replay_helpers.gd")

var _helpers = SessionReplayHelpersRef.new()
var _session_sync_in_flight: bool = false
var _replay_sync_in_flight: bool = false


func _init(helpers: RefCounted = null) -> void:
	if helpers != null:
		_helpers = helpers


func request_live_session(session_id: String, request: HTTPRequest, host: String, port: int) -> Dictionary:
	if session_id == "":
		return {"started": false, "reason": "missing_session"}
	if request == null:
		return {"started": false, "reason": "missing_request"}
	if _session_sync_in_flight:
		return {"started": false, "reason": "already_running"}
	if request.get_http_client_status() != HTTPClient.STATUS_DISCONNECTED:
		return {"started": false, "reason": "busy"}
	var error := request.request(_helpers.build_session_endpoint(host, port, session_id))
	if error != OK:
		return {
			"started": false,
			"reason": "request_error",
			"message": "Epochen: Session-Reload konnte nicht gestartet werden (%d)" % error,
		}
	_session_sync_in_flight = true
	return {
		"started": true,
		"event": {"action": "request", "session_id": session_id},
	}


func request_live_replay(session_id: String, request: HTTPRequest, host: String, port: int) -> Dictionary:
	if session_id == "":
		return {"started": false, "reason": "missing_session"}
	if request == null:
		return {"started": false, "reason": "missing_request"}
	if _replay_sync_in_flight:
		return {"started": false, "reason": "already_running"}
	if request.get_http_client_status() != HTTPClient.STATUS_DISCONNECTED:
		return {"started": false, "reason": "busy"}
	var error := request.request(_helpers.build_replay_endpoint(host, port, session_id))
	if error != OK:
		return {
			"started": false,
			"reason": "request_error",
			"message": "Replay: Request konnte nicht gestartet werden (%d)" % error,
		}
	_replay_sync_in_flight = true
	return {
		"started": true,
		"pending_status": "Replay: Manifest wird geladen",
		"event": {"action": "request", "session_id": session_id},
	}


func complete_live_session(result: int, response_code: int, body: PackedByteArray, session_id: String) -> Dictionary:
	_session_sync_in_flight = false
	var text := body.get_string_from_utf8().strip_edges()
	var parsed: Variant = JSON.parse_string(text)
	if result != HTTPRequest.RESULT_SUCCESS:
		return {
			"status": "error",
			"message": "Epochen: Session-Sync fehlgeschlagen (%d)" % result,
			"event": {"action": "error", "result": result},
		}
	if response_code < 200 or response_code >= 300:
		var detail := "HTTP %d" % response_code
		if typeof(parsed) == TYPE_DICTIONARY:
			detail = "%s | %s" % [detail, str((parsed as Dictionary).get("detail", "Fehler ohne Detail"))]
		return {
			"status": "http_error",
			"message": "Epochen: %s" % detail,
			"event": {"action": "http_error", "http": response_code},
		}
	if typeof(parsed) != TYPE_DICTIONARY:
		return {
			"status": "parse_error",
			"message": "Epochen: Session-Antwort unlesbar",
			"event": {"action": "parse_error", "http": response_code},
		}
	return {
		"status": "ok",
		"payload": parsed as Dictionary,
		"event": {"action": "applied", "session_id": session_id, "http": response_code},
	}


func complete_live_replay(result: int, response_code: int, body: PackedByteArray, session_id: String, fallback_resume_checkpoint_id: String, current_selected_checkpoint_id: String) -> Dictionary:
	_replay_sync_in_flight = false
	var text := body.get_string_from_utf8().strip_edges()
	var parsed: Variant = JSON.parse_string(text)
	if result != HTTPRequest.RESULT_SUCCESS:
		return {
			"status": "error",
			"message": "Replay: Sync fehlgeschlagen (%d)" % result,
			"event": {"action": "error", "result": result},
		}
	if response_code < 200 or response_code >= 300:
		var detail := "HTTP %d" % response_code
		if typeof(parsed) == TYPE_DICTIONARY:
			detail = "%s | %s" % [detail, str((parsed as Dictionary).get("detail", "Fehler ohne Detail"))]
		return {
			"status": "http_error",
			"message": "Replay: %s" % detail,
			"event": {"action": "http_error", "http": response_code},
		}
	if typeof(parsed) != TYPE_DICTIONARY:
		return {
			"status": "parse_error",
			"message": "Replay: Antwort unlesbar",
			"event": {"action": "parse_error", "http": response_code},
		}
	var manifest := parsed as Dictionary
	var option_state: Dictionary = _helpers.build_checkpoint_options(
		manifest,
		fallback_resume_checkpoint_id,
		current_selected_checkpoint_id
	)
	return {
		"status": "ok",
		"manifest": manifest,
		"selected_checkpoint_id": str(option_state.get("selected_checkpoint_id", "")).strip_edges(),
		"event": {"action": "applied", "http": response_code, "session_id": session_id},
	}