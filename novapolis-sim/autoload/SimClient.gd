extends Node
# Stand: 2025-11-10 11:35

## Pollt die Agent-API zyklisch und verteilt den Weltzustand an "world_listeners".

signal state_updated(state: Dictionary)
signal status_updated(message: String)

@export var step_interval: float = 0.5
@export var step_dt: float = 0.1
@export var host: String = "127.0.0.1"
@export var port: int = 8765

var _status_message: String = ""
var _last_state: Dictionary = {}
var _http: HTTPRequest
var _timer: Timer
var _busy: bool = false

# Backoff / retry helpers
var _backoff: float
var _backoff_max: float = 8.0
var _consecutive_failures: int = 0

func _ready() -> void:
	_http = HTTPRequest.new()
	_http.timeout = 4.0
	add_child(_http)

	_timer = Timer.new()
	_timer.wait_time = step_interval
	_timer.autostart = true
	_timer.one_shot = false
	_timer.timeout.connect(_on_timer_timeout)
	add_child(_timer)
	_timer.start()
	_backoff = step_interval
	_set_status("Warte auf Agent...")


func _on_timer_timeout() -> void:
	if _busy:
		return
	_busy = true
	await _step_world()
	_busy = false


func _step_world() -> void:
	if _http.get_http_client_status() != HTTPClient.STATUS_DISCONNECTED:
		return

	var resolved_port := _resolve_port()
	var url := "http://%s:%d/world/step" % [host, resolved_port]
	var payload := JSON.stringify({"dt": step_dt})
	var headers := ["Content-Type: application/json"]

	var error := _http.request(url, headers, HTTPClient.METHOD_POST, payload)
	if error != OK:
		_consecutive_failures += 1
		_backoff = clamp(_backoff * 2.0, step_interval, _backoff_max)
		_timer.wait_time = _backoff
		_set_status("HTTP-Fehler %d" % error)
		return

	var response = await _http.request_completed
	var result_code: int = response[0]
	var http_status: int = response[1]
	var body: PackedByteArray = response[3]

	if result_code != HTTPRequest.RESULT_SUCCESS:
		_consecutive_failures += 1
		_backoff = clamp(_backoff * 2.0, step_interval, _backoff_max)
		_timer.wait_time = _backoff
		_set_status("Verbindungsproblem (%d)" % result_code)
		return

	if http_status < 200 or http_status >= 300:
		var resp_text := ""
		# try to get a short string from body
		if body.size() > 0:
			resp_text = body.get_string_from_utf8().substr(0, 200)
		_consecutive_failures += 1
		_backoff = clamp(_backoff * 2.0, step_interval, _backoff_max)
		_timer.wait_time = _backoff
		_set_status("Agent-Status %d: %s" % [http_status, resp_text])
		return

	var parsed = JSON.parse_string(body.get_string_from_utf8())
	if typeof(parsed) != TYPE_DICTIONARY:
		_consecutive_failures += 1
		_backoff = clamp(_backoff * 2.0, step_interval, _backoff_max)
		_timer.wait_time = _backoff
		_set_status("Antwort unlesbar")
		return

	_last_state = parsed
	# success: reset backoff and timer interval
	_consecutive_failures = 0
	_backoff = step_interval
	_timer.wait_time = step_interval
	_set_status("")
	state_updated.emit(_last_state)
	get_tree().call_group("world_listeners", "receive_world_state", _last_state)


func _set_status(message: String) -> void:
	if _status_message == message:
		return
	_status_message = message
	status_updated.emit(_status_message)
	get_tree().call_group("world_listeners", "receive_status", _status_message)


func _resolve_port() -> int:
	var env_port := OS.get_environment("AGENT_PORT")
	if env_port is String and env_port.is_valid_int():
		return int(env_port)
	return port
