extends RefCounted

class_name SessionReplayStateController

const SessionReplayHelpersRef = preload("res://scripts/session_replay_helpers.gd")

var _helpers = SessionReplayHelpersRef.new()


func _init(helpers: RefCounted = null) -> void:
	if helpers != null:
		_helpers = helpers


func build_live_session_state(
	session_payload: Dictionary,
	session_id: String,
	fallback_slot: int,
	audio_assets_present: bool,
	current_selected_checkpoint_id: String
) -> Dictionary:
	var normalized: Dictionary = _helpers.normalize_live_session_payload(
		session_payload,
		session_id,
		fallback_slot
	)
	var artifact_paths: Dictionary = normalized.get("artifact_paths", {})
	var resume_checkpoint_id := str(normalized.get("resume_checkpoint_id", "")).strip_edges()
	var updates := {
		"live_session_artifact_paths": artifact_paths,
		"live_session_resume_checkpoint_id": resume_checkpoint_id,
		"loaded_epochs": [normalized.get("epoch_entry", {})],
		"current_epoch_index": 0,
		"current_slot": int(normalized.get("slot_number", fallback_slot)),
		"audio_assets_present": audio_assets_present or artifact_paths.has("tts_manifest"),
		"epoch_status_text": "Epochen: Live-Session %s | pc=%d | world=%d | patches=%d" % [
			session_id,
			(normalized.get("pc_log", []) as Array).size(),
			(normalized.get("world_log", []) as Array).size(),
			int(normalized.get("patch_count", 0)),
		],
	}
	if resume_checkpoint_id != "":
		updates["rp_replay_seed_text"] = "Replay-Seed: %s" % resume_checkpoint_id
		if current_selected_checkpoint_id == "":
			updates["hub_selected_replay_checkpoint_id"] = resume_checkpoint_id
	return updates


func build_replay_manifest_state(
	manifest: Dictionary,
	fallback_resume_checkpoint_id: String,
	current_selected_checkpoint_id: String
) -> Dictionary:
	var updates := {
		"live_replay_manifest": manifest,
	}
	if current_selected_checkpoint_id == "":
		var option_state: Dictionary = _helpers.build_checkpoint_options(
			manifest,
			fallback_resume_checkpoint_id,
			current_selected_checkpoint_id
		)
		updates["hub_selected_replay_checkpoint_id"] = str(option_state.get("selected_checkpoint_id", "")).strip_edges()
	return updates


func build_selected_replay_checkpoint_state(
	checkpoint_id: String,
	loaded_epochs: Array,
	current_epoch_index: int,
	live_replay_manifest: Dictionary,
	current_slot: int
) -> Dictionary:
	var updates := {
		"live_session_resume_checkpoint_id": checkpoint_id,
		"hub_selected_replay_checkpoint_id": checkpoint_id,
		"rp_replay_seed_text": "Replay-Seed: %s" % checkpoint_id,
	}
	var slot_number: int = int(_helpers.find_slot_for_checkpoint(
		loaded_epochs,
		current_epoch_index,
		live_replay_manifest,
		checkpoint_id
	))
	if slot_number >= 0:
		updates["current_slot"] = clampi(slot_number, 0, 23)
	var effective_slot := int(updates.get("current_slot", current_slot))
	updates["epoch_status_text"] = "Epochen: Resume-Anker %s | slot=%02d" % [checkpoint_id, effective_slot]
	updates["hub_chat_status_text"] = "Live-Spielclient: Resume-Anker %s aktiv" % checkpoint_id
	updates["runtime_event"] = {"action": "apply", "checkpoint_id": checkpoint_id, "slot": effective_slot}
	return updates
