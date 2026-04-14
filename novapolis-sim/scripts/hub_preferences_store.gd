extends RefCounted

class_name HubPreferencesStore

const _SECTION_NAME: String = "hub"


func load_preferences(path: String, defaults: Dictionary) -> Dictionary:
	var values := defaults.duplicate(true)
	var cfg := ConfigFile.new()
	var err := cfg.load(path)
	if err != OK:
		return values

	for key in defaults.keys():
		values[key] = cfg.get_value(_SECTION_NAME, str(key), defaults[key])
	return values


func save_preferences(path: String, values: Dictionary) -> int:
	var cfg := ConfigFile.new()
	for key in values.keys():
		cfg.set_value(_SECTION_NAME, str(key), values[key])
	return cfg.save(path)