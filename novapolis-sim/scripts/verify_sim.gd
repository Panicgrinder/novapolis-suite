extends SceneTree

# Minimal headless verifier for the Novapolis Sim project.
# Run with: Godot --path <project> -s res://scripts/verify_sim.gd

func _init() -> void:
    var ok := ProjectSettings.has_setting("application/config/name")
    if ok:
        print("SIM_VERIFY: OK")
    else:
        print("SIM_VERIFY: WARN - project setting missing")
    # exit immediately
    quit()
