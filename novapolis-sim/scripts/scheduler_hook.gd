extends RefCounted

# Tickless scheduler hook with a min-heap queue.
# This layer intentionally contains no game/business logic.
class_name SchedulerHook

var _heap: Array[Dictionary] = []
var _next_seq: int = 0

func enqueue(event: Dictionary) -> bool:
	var normalized = _normalize_event(event)
	if normalized.is_empty():
		return false
	_heap.append(normalized)
	_sift_up(_heap.size() - 1)
	return true


func peek_next() -> Dictionary:
	if _heap.is_empty():
		return {}
	return _heap[0].duplicate(true)


func pop_next() -> Dictionary:
	if _heap.is_empty():
		return {}

	var first = _heap[0]
	var last = _heap.pop_back()
	if not _heap.is_empty():
		_heap[0] = last
		_sift_down(0)
	return first.duplicate(true)


func pop_due(max_t: int) -> Array[Dictionary]:
	var due: Array[Dictionary] = []
	while not _heap.is_empty():
		var top = _heap[0]
		if int(top.get("t", 0)) > max_t:
			break
		due.append(pop_next())
	return due


func clear() -> void:
	_heap.clear()
	_next_seq = 0


func size() -> int:
	return _heap.size()


func is_empty() -> bool:
	return _heap.is_empty()


func _normalize_event(event: Dictionary) -> Dictionary:
	if not event.has("type"):
		return {}
	if not event.has("action_id"):
		return {}
	if not event.has("t"):
		return {}

	var t_value = int(event.get("t", -1))
	if t_value < 0:
		return {}

	var normalized: Dictionary = {
		"type": str(event.get("type", "")),
		"action_id": str(event.get("action_id", "")),
		"t": t_value,
		"priority": int(event.get("priority", 0)),
		"meta": {},
		"seq": _next_seq,
	}
	if event.has("meta") and typeof(event.get("meta")) == TYPE_DICTIONARY:
		normalized["meta"] = event.get("meta").duplicate(true)
	_next_seq += 1
	return normalized


func _less(a: Dictionary, b: Dictionary) -> bool:
	var at = int(a.get("t", 0))
	var bt = int(b.get("t", 0))
	if at != bt:
		return at < bt

	var ap = int(a.get("priority", 0))
	var bp = int(b.get("priority", 0))
	if ap != bp:
		return ap < bp

	return int(a.get("seq", 0)) < int(b.get("seq", 0))


func _sift_up(index: int) -> void:
	var i = index
	while i > 0:
		var parent = (i - 1) >> 1
		if not _less(_heap[i], _heap[parent]):
			break
		_swap(i, parent)
		i = parent


func _sift_down(index: int) -> void:
	var i = index
	while true:
		var left = i * 2 + 1
		var right = left + 1
		var smallest = i

		if left < _heap.size() and _less(_heap[left], _heap[smallest]):
			smallest = left
		if right < _heap.size() and _less(_heap[right], _heap[smallest]):
			smallest = right

		if smallest == i:
			break
		_swap(i, smallest)
		i = smallest


func _swap(a: int, b: int) -> void:
	var tmp = _heap[a]
	_heap[a] = _heap[b]
	_heap[b] = tmp
