extends Node2D

@onready var tick_label: Label = $TickLabel
@onready var time_label: Label = $TimeLabel
@onready var status_label: Label = $StatusLabel
@onready var epoch_label: Label = $EpochLabel
@onready var slot_label: Label = $SlotLabel
@onready var log_label: RichTextLabel = $PcLogLabel
@onready var epoch_status_label: Label = $EpochStatusLabel
@onready var audio_status_label: Label = $AudioStatusLabel
@onready var play_pc_button: Button = $PlayPcAudioButton
@onready var play_world_button: Button = $PlayWorldAudioButton
@onready var _sim_client: Node = get_node_or_null("/root/SimClient")

@export var epochs_dir: String = "res://data/epochs"
@export var audio_assets_dir: String = "res://assets/audio"

var _loaded_epochs: Array[Dictionary] = []
var _current_epoch_index: int = 0
var _current_slot: int = 0
var _audio_player: AudioStreamPlayer

func _ready() -> void:
	add_to_group("world_listeners")
	if _sim_client:
		_sim_client.state_updated.connect(_on_state_updated)
		_sim_client.status_updated.connect(_on_status_updated)
	play_pc_button.pressed.connect(_on_play_pc_audio_pressed)
	play_world_button.pressed.connect(_on_play_world_audio_pressed)
	_audio_player = AudioStreamPlayer.new()
	add_child(_audio_player)
	_apply_state({"tick": 0, "time": 0.0})
	_display_status("Warte auf Agent...")
	_load_epochs()
	_render_pc_centric_view()


func receive_world_state(state: Dictionary) -> void:
	_apply_state(state)


func receive_status(message: String) -> void:
	_display_status(message)


func _on_state_updated(state: Dictionary) -> void:
	_apply_state(state)


func _on_status_updated(message: String) -> void:
	_display_status(message)


func _apply_state(state: Dictionary) -> void:
	if state.has("tick"):
		tick_label.text = "Tick: %d" % int(state["tick"])
	if state.has("time"):
		time_label.text = "Zeit: %.2f s" % float(state["time"])


func _display_status(message: String) -> void:
	if message == "":
		status_label.visible = false
	else:
		status_label.visible = true
		status_label.text = "Status: %s" % message


func _load_epochs() -> void:
	_loaded_epochs.clear()
	var base_dir := DirAccess.open(epochs_dir)
	if base_dir == null:
		epoch_status_label.text = "Epochen: keine Daten unter %s" % epochs_dir
		return

	var epoch_dirs: Array[String] = []
	base_dir.list_dir_begin()
	while true:
		var entry := base_dir.get_next()
		if entry == "":
			break
		if base_dir.current_is_dir() and not entry.begins_with("."):
			epoch_dirs.append(entry)
	base_dir.list_dir_end()
	epoch_dirs.sort()

	for epoch_dir in epoch_dirs:
		var epoch_path := "%s/%s" % [epochs_dir, epoch_dir]
		var world_log := _load_log_entries("%s/world_log.jsonl" % epoch_path)
		var pc_log := _load_log_entries("%s/pc_log.jsonl" % epoch_path)
		if world_log.is_empty() and pc_log.is_empty():
			continue
		_loaded_epochs.append({
			"name": epoch_dir,
			"world_log": world_log,
			"pc_log": pc_log,
		})

	if _loaded_epochs.is_empty():
		epoch_status_label.text = "Epochen: keine verwertbaren world_log/pc_log Dateien gefunden"
		return

	_current_epoch_index = 0
	_current_slot = _derive_initial_slot(_loaded_epochs[_current_epoch_index].get("pc_log", []))
	epoch_status_label.text = "Epochen geladen: %d" % _loaded_epochs.size()


func _load_log_entries(path: String) -> Array[Dictionary]:
	var entries: Array[Dictionary] = []
	if not FileAccess.file_exists(path):
		return entries

	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return entries
	var raw := file.get_as_text()

	var trimmed := raw.strip_edges()
	if trimmed.begins_with("["):
		var parsed := JSON.parse_string(trimmed)
		if typeof(parsed) == TYPE_ARRAY:
			for item in parsed:
				if typeof(item) == TYPE_DICTIONARY:
					entries.append(item)
		return entries

	var lines := raw.split("\n")
	for line in lines:
		var clean := line.strip_edges()
		if clean == "":
			continue
		var parsed_line := JSON.parse_string(clean)
		if typeof(parsed_line) == TYPE_DICTIONARY:
			entries.append(parsed_line)
		else:
			entries.append({"text": clean})
	return entries


func _derive_initial_slot(pc_log: Array) -> int:
	for entry in pc_log:
		if typeof(entry) != TYPE_DICTIONARY:
			continue
		var slot_value := _extract_slot_from_entry(entry)
		if slot_value >= 0:
			return slot_value
	return 0


func _extract_slot_from_entry(entry: Dictionary) -> int:
	for key in ["slot", "hour", "slot_index"]:
		if entry.has(key):
			return int(entry.get(key, 0))
	return -1


func _render_pc_centric_view() -> void:
	if _loaded_epochs.is_empty():
		epoch_label.text = "Epoch: --"
		slot_label.text = "Slot: --"
		log_label.text = "Keine Epochenlogs gefunden. Erwartet: res://data/epochs/<epoch>/world_log.jsonl + pc_log.jsonl"
		return

	var epoch := _loaded_epochs[_current_epoch_index]
	var epoch_name := str(epoch.get("name", "epoch"))
	var world_log: Array = epoch.get("world_log", [])
	var pc_log: Array = epoch.get("pc_log", [])

	var unique_slots := _collect_unique_slots(world_log, pc_log)
	var pc_slot_events := _filter_events_for_slot(pc_log, _current_slot)

	epoch_label.text = "Epoch: %s" % epoch_name
	slot_label.text = "Slot: %02d (Slots geladen: %d)" % [_current_slot, unique_slots.size()]

	var lines: Array[String] = []
	lines.append("PC-zentrierte Ansicht")
	lines.append("- PC-Log-Eintraege: %d" % pc_log.size())
	lines.append("- World-Log-Eintraege: %d" % world_log.size())
	lines.append("- Slot-Eintraege (PC): %d" % pc_slot_events.size())
	lines.append("")
	if pc_slot_events.is_empty():
		lines.append("Keine PC-Eintraege fuer den aktuellen Slot gefunden.")
	else:
		for event in pc_slot_events:
			lines.append("- %s" % _event_to_text(event))

	log_label.text = "\n".join(lines)


func _collect_unique_slots(world_log: Array, pc_log: Array) -> Array[int]:
	var seen: Dictionary = {}
	for collection in [world_log, pc_log]:
		for item in collection:
			if typeof(item) != TYPE_DICTIONARY:
				continue
			var slot_value := _extract_slot_from_entry(item)
			if slot_value >= 0:
				seen[slot_value] = true
	var result: Array[int] = []
	for key in seen.keys():
		result.append(int(key))
	result.sort()
	return result


func _filter_events_for_slot(entries: Array, slot: int) -> Array[Dictionary]:
	var filtered: Array[Dictionary] = []
	for item in entries:
		if typeof(item) != TYPE_DICTIONARY:
			continue
		var item_slot := _extract_slot_from_entry(item)
		if item_slot == slot:
			filtered.append(item)
	if filtered.is_empty():
		for item in entries:
			if typeof(item) == TYPE_DICTIONARY:
				filtered.append(item)
			if filtered.size() >= 5:
				break
	return filtered


func _event_to_text(event: Dictionary) -> String:
	if event.has("text"):
		return str(event.get("text"))
	if event.has("event"):
		return str(event.get("event"))
	if event.has("message"):
		return str(event.get("message"))
	if event.has("summary"):
		return str(event.get("summary"))
	return JSON.stringify(event)


func _on_play_pc_audio_pressed() -> void:
	_play_audio_for_channel("pc")


func _on_play_world_audio_pressed() -> void:
	_play_audio_for_channel("world")


func _play_audio_for_channel(channel: String) -> void:
	if _loaded_epochs.is_empty():
		audio_status_label.text = "Audio: keine Epochen geladen"
		return

	var epoch := _loaded_epochs[_current_epoch_index]
	var epoch_name := str(epoch.get("name", "epoch00"))
	var epoch_number := _extract_epoch_number(epoch_name)
	var file_name := "epoch%02d_slot%02d_%s.ogg" % [epoch_number, _current_slot, channel]
	var full_path := "%s/%s" % [audio_assets_dir, file_name]

	if not FileAccess.file_exists(full_path):
		audio_status_label.text = "Audio fehlt: %s" % file_name
		return

	var stream := load(full_path)
	if stream == null:
		audio_status_label.text = "Audio unlesbar: %s" % file_name
		return

	_audio_player.stream = stream
	_audio_player.play()
	audio_status_label.text = "Audio spielt: %s" % file_name


func _extract_epoch_number(epoch_name: String) -> int:
	var digits := ""
	for ch in epoch_name:
		if ch >= "0" and ch <= "9":
			digits += ch
	if digits.is_valid_int():
		return int(digits)
	return _current_epoch_index + 1
