extends Node2D

@onready var tick_label: Label = $TickLabel
@onready var time_label: Label = $TimeLabel
@onready var status_label: Label = $StatusLabel
@onready var _sim_client: Node = get_node_or_null("/root/SimClient")

func _ready() -> void:
    add_to_group("world_listeners")
    if _sim_client:
        _sim_client.state_updated.connect(_on_state_updated)
        _sim_client.status_updated.connect(_on_status_updated)
    _apply_state({"tick": 0, "time": 0.0})
    _display_status("Warte auf Agent...")


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
