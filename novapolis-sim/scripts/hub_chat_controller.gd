extends RefCounted

class_name HubChatController

const _IDLE_SCENE_TEXT: String = "Kein Live-Lauf aktiv."

var _request_in_flight: bool = false


func build_slot_id(slot: int) -> String:
	return "slot-%02d" % slot


func next_turn_id(turn_index: int) -> String:
	return "turn-%02d" % (turn_index + 1)


func build_public_context(slot: int, scene_text: String, consequence: String, options: Array[String]) -> String:
	var lines: Array[String] = []
	lines.append("slot: %02d" % slot)
	if scene_text != "" and scene_text != _IDLE_SCENE_TEXT:
		lines.append("szene: %s" % scene_text)
	if consequence != "":
		lines.append("konsequenz: %s" % consequence)
	if not options.is_empty():
		lines.append("optionen:")
		for option in options:
			lines.append("- %s" % option)
	return "\n".join(lines)


func build_retrieval_query(prompt: String, slot_id: String, scene_id: String, scene_text: String, consequence: String) -> String:
	var parts: Array[String] = []
	parts.append(prompt.strip_edges())
	parts.append(slot_id)
	if scene_id != "":
		parts.append(scene_id)
	if scene_text != "" and scene_text != _IDLE_SCENE_TEXT:
		parts.append(scene_text)
	if consequence != "":
		parts.append(consequence)
	return " | ".join(parts)


func build_endpoint(host: String, port: int) -> String:
	return "http://%s:%d/chat" % [host, port]


func request_chat(
	prompt: String,
	request: HTTPRequest,
	host: String,
	port: int,
	profile_id: String,
	session_id: String,
	campaign_id: String,
	scene_id: String,
	turn_index: int,
	slot: int,
	current_scene_text: String,
	current_consequence: String,
	current_options: Array[String]
) -> Dictionary:
	if _request_in_flight:
		return {"started": false, "message": "Live-Spielclient: Anfrage laeuft bereits"}
	var clean_prompt := prompt.strip_edges()
	if clean_prompt == "":
		return {"started": false, "message": "Live-Spielclient: Bitte Nachricht eingeben"}
	if request == null:
		return {"started": false, "message": "Live-Spielclient: Chat-Request fehlt"}
	if request.get_http_client_status() != HTTPClient.STATUS_DISCONNECTED:
		return {"started": false, "message": "Live-Spielclient: Anfrage laeuft bereits"}

	var slot_id := build_slot_id(slot)
	var normalized_scene_id := scene_id
	if normalized_scene_id == "hub_boot":
		normalized_scene_id = slot_id
	var public_context := build_public_context(slot, current_scene_text, current_consequence, current_options)
	var turn_id := next_turn_id(turn_index)
	var endpoint := build_endpoint(host, port)
	var payload := {
		"messages": [{"role": "user", "content": clean_prompt}],
		"profile_id": profile_id,
		"session_id": session_id,
		"options": {
			"session_id": session_id,
			"orchestrator_enabled": true,
			"campaign_id": campaign_id,
			"scene_id": normalized_scene_id,
			"slot_id": slot_id,
			"turn_id": turn_id,
			"retrieval_query": build_retrieval_query(clean_prompt, slot_id, normalized_scene_id, current_scene_text, current_consequence),
			"public_context": public_context,
			"scheduler_hints": ["sim_live_client", slot_id],
			"state_patch_hints": ["scene.current", "pc_log.append", "world_log.append"],
		},
	}
	var body := JSON.stringify(payload, "")
	var headers := PackedStringArray(["Content-Type: application/json"])
	var error := request.request(endpoint, headers, HTTPClient.METHOD_POST, body)
	if error != OK:
		return {
			"started": false,
			"message": "Live-Spielclient: Request-Fehler (%d)" % error,
			"detail_line": "Request konnte nicht gestartet werden.",
		}

	_request_in_flight = true
	return {
		"started": true,
		"prompt": clean_prompt,
		"endpoint": endpoint,
		"pending_turn_id": turn_id,
		"scene_id": normalized_scene_id,
		"public_context": public_context,
		"event": {"action": "send", "endpoint": endpoint},
	}


func complete_chat_request(result: int, response_code: int, body: PackedByteArray) -> Dictionary:
	_request_in_flight = false
	var text := body.get_string_from_utf8().strip_edges()
	var parsed: Variant = JSON.parse_string(text)
	if response_code >= 200 and response_code < 300:
		var answer := text
		if typeof(parsed) == TYPE_DICTIONARY:
			var obj := parsed as Dictionary
			answer = str(obj.get("content", ""))
			if answer == "":
				answer = str(obj.get("detail", "(leere Antwort)"))
		return {
			"status": "ok",
			"answer": answer,
			"status_text": "Live-Spielclient: Antwort ok (%d)" % response_code,
			"event": {"action": "response", "http": response_code, "result": result},
		}

	var detail := "HTTP %d | result=%d" % [response_code, result]
	if typeof(parsed) == TYPE_DICTIONARY:
		var err_obj := parsed as Dictionary
		detail = "%s | %s" % [detail, str(err_obj.get("detail", "Fehler ohne Detail"))]
	elif text != "":
		detail = "%s | %s" % [detail, text]
	return {
		"status": "error",
		"detail_line": detail,
		"status_text": "Live-Spielclient: Fehler (%d)" % response_code,
		"pending_turn_id": "",
		"event": {"action": "response", "http": response_code, "result": result},
	}


func build_response_state(
	answer: String,
	slot: int,
	current_scene_id: String,
	current_scene_text: String,
	pending_turn_id: String,
	turn_index: int
) -> Dictionary:
	var parsed := parse_response(answer)
	var slot_id := build_slot_id(slot)
	var next_scene_text := current_scene_text
	var next_scene_id := current_scene_id
	var scene_text := str(parsed.get("scene", "")).strip_edges()
	if scene_text != "":
		next_scene_text = scene_text
		next_scene_id = slot_id
	var consequence_text := str(parsed.get("consequence", "")).strip_edges()
	var options := coerce_string_array(parsed.get("options", []))
	var state_patches := coerce_string_array(parsed.get("state_patches", []))
	var next_turn_index := turn_index
	var next_pending_turn_id := pending_turn_id
	if next_pending_turn_id != "":
		next_turn_index += 1
		next_pending_turn_id = ""
	return {
		"scene_id": next_scene_id,
		"scene_text": next_scene_text,
		"consequence": consequence_text,
		"options": options,
		"state_patches": state_patches,
		"public_context": build_public_context(slot, next_scene_text, consequence_text, options),
		"turn_index": next_turn_index,
		"pending_turn_id": next_pending_turn_id,
	}


func coerce_string_array(value: Variant) -> Array[String]:
	var result: Array[String] = []
	if typeof(value) != TYPE_ARRAY:
		return result
	for entry in value:
		var text := str(entry).strip_edges()
		if text != "":
			result.append(text)
	return result


func _extract_heading_value(line: String) -> String:
	var separator_index := line.find(":")
	if separator_index < 0:
		return ""
	return line.substr(separator_index + 1).strip_edges()


func _clean_item(line: String) -> String:
	var clean := line.strip_edges()
	for prefix in ["- ", "* ", "• "]:
		if clean.begins_with(prefix):
			return clean.substr(prefix.length()).strip_edges()
	return clean


func parse_response(content: String) -> Dictionary:
	var scene_lines: Array[String] = []
	var consequence_lines: Array[String] = []
	var option_lines: Array[String] = []
	var state_patch_lines: Array[String] = []
	var current_section := ""

	for raw_line in content.split("\n"):
		var line := raw_line.strip_edges()
		if line == "":
			continue
		var lower := line.to_lower()
		if lower.begins_with("szene"):
			current_section = "scene"
			var scene_value := _extract_heading_value(line)
			if scene_value != "":
				scene_lines.append(scene_value)
			continue
		if lower.begins_with("konsequenz"):
			current_section = "consequence"
			var consequence_value := _extract_heading_value(line)
			if consequence_value != "":
				consequence_lines.append(consequence_value)
			continue
		if lower.begins_with("optionen"):
			current_section = "options"
			var option_value := _extract_heading_value(line)
			if option_value != "":
				option_lines.append(_clean_item(option_value))
			continue
		if lower.begins_with("state_patches") or lower.begins_with("state patches"):
			current_section = "state_patches"
			var patch_value := _extract_heading_value(line)
			if patch_value != "":
				state_patch_lines.append(_clean_item(patch_value))
			continue

		match current_section:
			"scene":
				scene_lines.append(line)
			"consequence":
				consequence_lines.append(line)
			"options":
				option_lines.append(_clean_item(line))
			"state_patches":
				state_patch_lines.append(_clean_item(line))
			_:
				pass

	var scene_text := " ".join(scene_lines).strip_edges()
	var consequence_text := " ".join(consequence_lines).strip_edges()
	if scene_text == "" and consequence_text == "" and content.strip_edges() != "":
		consequence_text = content.strip_edges().replace("\n", " ")
	return {
		"scene": scene_text,
		"consequence": consequence_text,
		"options": option_lines,
		"state_patches": state_patch_lines,
	}