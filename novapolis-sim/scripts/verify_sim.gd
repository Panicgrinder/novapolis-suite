extends SceneTree
# Stand: 2026-04-14 13:57

# Headless smoke verifier for the Novapolis Sim project.
# Run with: Godot --path <project> -s res://scripts/verify_sim.gd

const _EXPECTED_PROJECT_NAME: String = "Novapolis Sim"
const _EXPECTED_MAIN_SCENE: String = "res://Main.tscn"
const _EXPECTED_MAIN_SCRIPT: String = "res://scripts/Main.gd"
const _EXPECTED_AUTOLOAD_SETTING: String = "autoload/SimClient"
const _EXPECTED_AUTOLOAD_PATH: String = "*res://autoload/SimClient.gd"
const _REQUIRED_NODE_PATHS: Array[String] = [
	"HubTopBandPanel",
	"HubStagePanel",
	"HubOpsPanel",
	"HubTelemetryPanel",
	"HubReplayPanel",
	"HubReplayPanel/HubReplayCheckpointButton",
	"HubReplayPanel/HubReplayFetchButton",
	"HubReplayPanel/HubReplayApplyButton",
	"HubChatPanel",
	"HubChatPanel/HubChatInputEdit",
	"HubChatPanel/HubChatSendButton",
	"AgentStudioPanel",
	"ChecksStudioPanel",
	"RpStudioPanel",
]

func _init() -> void:
	var errors: Array[String] = []
	_validate_project_settings(errors)
	var scene_root := _load_main_scene(errors)
	if scene_root != null:
		_validate_main_scene(scene_root, errors)
		_cleanup_main_scene(scene_root)

	if errors.is_empty():
		print("SIM_VERIFY: OK")
		quit(0)
		return

	print("SIM_VERIFY: FAIL")
	for entry in errors:
		print("- %s" % entry)
	quit(1)


func _validate_project_settings(errors: Array[String]) -> void:
	_expect_setting(errors, "application/config/name", _EXPECTED_PROJECT_NAME)
	_expect_setting(errors, "application/run/main_scene", _EXPECTED_MAIN_SCENE)
	_expect_setting(errors, _EXPECTED_AUTOLOAD_SETTING, _EXPECTED_AUTOLOAD_PATH)

	var autoload_path := _EXPECTED_AUTOLOAD_PATH.trim_prefix("*")
	if not ResourceLoader.exists(autoload_path):
		errors.append("autoload script missing: %s" % autoload_path)


func _expect_setting(errors: Array[String], key: String, expected_value: String) -> void:
	if not ProjectSettings.has_setting(key):
		errors.append("missing project setting: %s" % key)
		return
	var actual_value := str(ProjectSettings.get_setting(key))
	if actual_value != expected_value:
		errors.append("project setting %s expected %s but found %s" % [key, expected_value, actual_value])


func _load_main_scene(errors: Array[String]) -> Node:
	if not ResourceLoader.exists(_EXPECTED_MAIN_SCENE):
		errors.append("main scene missing: %s" % _EXPECTED_MAIN_SCENE)
		return null
	var scene_resource := load(_EXPECTED_MAIN_SCENE)
	if scene_resource == null:
		errors.append("main scene could not be loaded: %s" % _EXPECTED_MAIN_SCENE)
		return null
	if not (scene_resource is PackedScene):
		errors.append("main scene is not a PackedScene: %s" % _EXPECTED_MAIN_SCENE)
		return null
	var scene_root := (scene_resource as PackedScene).instantiate()
	if scene_root == null:
		errors.append("main scene could not be instantiated: %s" % _EXPECTED_MAIN_SCENE)
		return null
	return scene_root


func _validate_main_scene(scene_root: Node, errors: Array[String]) -> void:
	if scene_root.name != "Main":
		errors.append("main scene root expected Main but found %s" % scene_root.name)
	var root_script = scene_root.get_script()
	if root_script == null:
		errors.append("main scene root has no script attached")
	elif str(root_script.resource_path) != _EXPECTED_MAIN_SCRIPT:
		errors.append("main scene root script expected %s but found %s" % [_EXPECTED_MAIN_SCRIPT, str(root_script.resource_path)])

	for node_path in _REQUIRED_NODE_PATHS:
		if scene_root.get_node_or_null(NodePath(node_path)) == null:
			errors.append("required node missing: %s" % node_path)


func _cleanup_main_scene(scene_root: Node) -> void:
	scene_root.free()
