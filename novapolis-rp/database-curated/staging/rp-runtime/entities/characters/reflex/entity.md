---
stand: 2026-05-20 17:42
update: Reflex' Runtime-Sheet fuehrt jetzt Turn 15 als kantige Schutzwahrnehmung ohne Kontroll- oder Technikdelta.
checks: snapshot-lock PASS (2026-05-20 17:42); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-md PASS (EXITCODE=0, 2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py PASS (2026-05-20 17:42); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-05-20 17:42); git diff --check PASS (CRLF warnings only, 2026-05-20 17:42).
---
Reflex - Runtime Working Sheet
==============================

Status
------

- slug: reflex
- name: Reflex
- state: Arbeitsstand
- review_state: working
- first_seen_session: d5-c6-nordlinie-sanierung-01

Role
----

- faction: Novapolis
- function: koerpernahe Exoskelett-, Schutz- und Sensorassistenz an Ronjas Tunnelzug
- current_goal: Ronjas Tunnelarbeit stabilisieren, Lastspitzen abfedern und den Arbeitszug nicht von ihrer Fuehrung entkoppeln

Signals
-------

- confirmed:
  - Reflex bleibt im aktuellen Hauptpfad koerpernah an Ronja gebunden.
  - Tragen, Setzen und Fehlerlesung werden nicht als freie Zweitfigur ausgespielt.
  - Reflex wirkt im Tunnelzug praktisch mit, ohne eine eigene Nebenhandlung zu oeffnen.
  - Auch am direkten Kontaktpunkt zum C6-Trupp bleibt Reflex Schutz-, Sensor- und Stabilisierungsassistenz statt eigenstaendiger Kontaktfigur.
  - Turn 14 bestaetigt, dass Reflex Ronjas kurze Geste als Wahrnehmungs- und Naehesignal aufnehmen kann, ohne daraus Kontrolle, Entkopplung oder eine neue Symbiose-Stufe abzuleiten.
  - Turn 15 bestaetigt, dass dieses Naehesignal Reflex stabilisiert, aber nicht entkantet: Weltendruck, Tunnelgefahr und offene technische Risiken bleiben als scharfer Schutzfilter lesbar.
- tentative:
  - Die gemeinsame Befundaufnahme koennte den Schutzfokus im naechsten Zug von reiner Tunnelassistenz auf abgesicherte Begegnung und Materialuebergabe erweitern.
  - Bei echter Lebensgefahr bleibt Kokon/Vollschutz als kurzfristige CRISIS-Reaktion moeglich; Turn 15 loest ihn nicht aus.
- contradictions:
  - keine; die Runtime bestaetigt ausdruecklich die bestehende Detachment-Lesart

Promotion Notes
---------------

- Sessionbezug: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 5-15
- Detailwirkung auf Naehe- und Schutzachsen liegt zusaetzlich in `mind.md`.
