---
stand: 2025-11-06 02:55
update: Frontmatter auf YAML migriert; markdownlint PASS
checks: markdownlint-cli2 PASS
---

Scheduler-Spec (ticklos, Min-Heap, 24×1h-Epochen)
=================================================

Diese Spezifikation beschreibt den mikroskopischen Zeitablauf innerhalb einer 24×1h-Epoche mittels einer ticklosen, ereignisgetriebenen Min-Heap-Queue. Sie ergänzt die Annotation-Spezifikation (Knowledge/Actions/Skills) und definiert Schnittstellen, Datenstrukturen, Invarianten und Fehlerpfade.

- Referenz: `novapolis-dev/docs/specs/annotation-spec.md` (Felder: `knowledge`, `actions`, Skill-Ableitung)
- Verweise: `novapolis-dev/docs/todo.dev.md`, `novapolis-dev/docs/todo.sim.md`, `novapolis-dev/docs/todo.rp.md`

Kurz-Kontrakt
-------------

- Eingaben
  - epoch: `{ index: int, start_at: ISO8601, end_at: ISO8601 }` (24×1h; PC-zentriert)
  - actions_submitted: Liste von Action-Instanzen mit minimalem Schema aus der Annotation-Spec: `{ id, actor, verb, params, submitted_at }`
  - action_defs: Lookup für `verb → { base_duration_min, effort, interruptible, locks, may_trigger_event, resources }`
  - skills: `actor → skill_levels` (diskret 0–3 je Skill); Mapping beeinflusst Dauer via `f_skill`
  - world_state/resources: optionaler Kontext (Verfügbarkeit, Orte, Tag/Nacht-Modifikatoren)
- Ausgaben
  - schedule_events: geordnete Liste von Events `{ type: start|end|interrupt|visibility_change, action_id, t, meta }`
  - updated_locks/resources: Zustände nach Ablauf der Epoche
  - logs: Append-Records für `world_log` und `pc_log` (chunking an Epochen-Grenzen)
- Invarianten / Erfolg
  - Keine zwei Aktionen halten gleichzeitig dasselbe exklusive Lock
  - Nicht-unterbrechbare Aktionen laufen zwischen `start` und `end` ohne Preemption
  - Sichtbarkeit wird nur durch Events verändert (keine Retcons)
  - Komplexität: O((N+E) · log E) für N Einreichungen, E Events
- Fehlerpfade
  - Ungültige Dauer (≤ 0) → Reject mit Fehler `InvalidDuration`
  - Lock-Konflikt ohne Warte-Strategie → Queueing oder `CannotAcquireLock`
  - Ressourcenmangel → `InsufficientResources`
  - Zeitüberlauf jenseits `epoch.end_at` → Carry-over in nächste Epoche (Split-Policy, s. u.)

Datenmodell
-----------

- ActionDef
  - `verb: string`, `base_duration_min: int ≥ 1`, `effort: low|medium|high`, `interruptible: bool`
  - `locks: string[]` (z. B. `workshop`, `radio`), `may_trigger_event: bool`
  - `resources: { name: string, amount: number }[]` (optional)
- ActionInstance
  - `id: string`, `actor: string`, `verb: string`, `params: any`, `submitted_at: ISO8601`
- Event
  - `type: start|end|interrupt|visibility_change`, `action_id: string`, `t: int (min seit epoch.start)`, `meta: any`
- LockTable / ResourceTable
  - `held_by: action_id | null`, `queue: action_id[]`
- Zeitrepräsentation
  - Intern `t` in Minuten relativ zu `epoch.start` (int); extern zusätzlich ISO8601

Dauerformel
-----------

Die effektive Dauer ergibt sich aus Basisdauer, Anstrengung und Skill-Faktoren sowie optionalen Modifikatoren (z. B. Tageszeit, Wetter):

$$
\begin{aligned}
 d_\text{eff} &= \left\lceil \max\{1,\; d_0 \cdot f_\text{effort}(e) \cdot f_\text{skill}(s) \cdot f_\text{mod}(ctx) \} \right\rceil \\
 f_\text{effort}(e) &:= \begin{cases}
  0.9 & e=low \\
  1.0 & e=medium \\
  1.1 & e=high
 \end{cases} \\
 f_\text{skill}(s) &:= \begin{cases}
  1.25 & s=0 \\
  1.00 & s=1 \\
  0.85 & s=2 \\
  0.70 & s=3
 \end{cases}
\end{aligned}
$$

Hinweis: Skill-Level `s` stammt aus der Annotation-Spec (lineare Ableitung aus der Verhaltensmatrix) und wird per Mapping in einen Faktor überführt.

Algorithmus (ticklos)
---------------------

- Neue Aktion `A` wird eingereicht (Zeit `t_submit`):
  1) Validieren (`verb` bekannt, Dauer > 0, Ressourcen vorhanden)
  2) Locks akquirieren (atomare Reihenfolge; Deadlock-Vermeidung via globale Lock-Order)
  3) `t_start = max(t_submit, t_release_needed_locks)`
  4) `t_end = t_start + d_eff(A)`; Event `start@t_start`, `end@t_end` erzeugen
  5) `end` ins Min-Heap (Key `t_end`) pushen
- Ereignisverarbeitung:
  - Solange `heap.peek().t ≤ epoch_end`: pop→process
    - Bei `end`: Locks freigeben, Ressourcen verbrauchen/erstatten, Folgeevent (`visibility_change`/Trigger) emittieren
    - Bei `interrupt`: Wenn `interruptible`, Restdauer speichern und optionale Wiederaufnahme einplanen; ansonsten ignorieren
- Überlauf über `epoch.end_at`:
  - Carry-over in nächste Epoche: `start` verbleibt, `end` wird in Epoche+1 fortgeführt
  - `world_log`: kontinuierlich; `pc_log`: chunked je Epoche (keine Retcons)

### Pseudocode (vereinfachte Skizze)

```text
function schedule(actions_submitted, action_defs, skills, epoch):
  heap = MinHeap()  # key: t_end
  locks = LockTable()
  for A in actions_submitted:
    defn = action_defs[A.verb]
    d_eff = compute_duration(defn, skills[A.actor])
    t_start = acquire_locks_when_available(locks, defn.locks, A.submitted_at)
    t_end = t_start + d_eff
    emit(Event('start', A.id, t_start))
    heap.push(Event('end', A.id, t_end))
  while heap.not_empty() and heap.peek().t <= epoch.end:
    ev = heap.pop()
    process_end_event(ev)
    if may_trigger_followup(ev):
      schedule_followup(heap, ev)
  carry_over(heap, epoch.next)
```

Interrupts & Prioritäten
------------------------

- Interrupt-Quelle: Notfall-/PC-relevantes Event mit höherer Priorität
- Regel: Nur `interruptible=true`-Aktionen werden präemptiert; Restdauer `d_rem = t_end - t_interrupt` wird gespeichert (nicht verfallen)
- Wiederaufnahme: Neue Instanz mit gleicher `id` und `d_eff = d_rem` (Locks neu erwerben)

Locks & Deadlocks
-----------------

- Exklusive Locks werden in fester globaler Reihenfolge erworben (z. B. alphabetisch), um zyklische Abhängigkeiten zu vermeiden
- Warte-Strategie: FIFO-Queue pro Lock; `t_start` einer Aktion ist das Maximum der Freigabezeiten aller benötigten Locks

Beispiele (3 Aktionen)
----------------------

### Beispiel 1: Reinigen (60m, medium, interruptible)

Eingabe (ActionDef + Instance):

```yaml
action_defs:
  clean:
    base_duration_min: 60
    effort: medium
    interruptible: true
    locks: []
    may_trigger_event: false

actions_submitted:
  - id: A1
    actor: Reflex
    verb: clean
    params: {}
    submitted_at: 2025-07-01T08:05:00
```

Ergebnis (vereinfacht): Start bei 08:05, Ende bei 09:05 (ohne Modifikatoren)

### Beispiel 2: Reparatur (45m, high, lock=workshop)

```yaml
action_defs:
  repair:
    base_duration_min: 45
    effort: high
    interruptible: false
    locks: [workshop]
    may_trigger_event: false

actions_submitted:
  - id: A2
    actor: Ronja
    verb: repair
    params: { part: "valve" }
    submitted_at: 2025-07-01T08:10:00
```

- Falls `workshop` frei: Start 08:10, Ende ca. 08:59 (`45 * 1.1 ≈ 50` → ceil)
- Falls belegt: `t_start` auf Freigabezeit des Locks verschoben

### Beispiel 3: Funk (5m, low, lock=radio, interruptible; kann Event auslösen)

```yaml
action_defs:
  radio:
    base_duration_min: 5
    effort: low
    interruptible: true
    locks: [radio]
    may_trigger_event: true

actions_submitted:
  - id: A3
    actor: Jonas
    verb: radio
    params: { channel: "ally" }
    submitted_at: 2025-07-01T08:12:00
```

- Belegt `radio` exklusiv; kann `visibility_change` auslösen (z. B. Nachricht erreicht PC)
- Interrupt-Regel: Darf andere `interruptible` Jobs mit niedrigerer Priorität unterbrechen, wenn so konfiguriert

Logs & Sichtbarkeit
-------------------

- `world_log`: vollständige Kette aller Events in Echtzeit
- `pc_log`: nur PC-sichtbare Events; Retro-Reveals erfolgen als `visibility_change`-Events (keine Änderung historischer Einträge)
- Audio-Dateien (wenn erzeugt) folgen dem Schema `epoch{dd}_slot{hh}_{channel}.ogg`

Akzeptanzkriterien
------------------

- Locks werden nie doppelt vergeben; Deadlocks verhindert durch Reihenfolge
- Nicht-unterbrechbare Aktionen laufen ohne Preemption durch
- Epochen-Überlauf erzeugt Carry-over ohne Informationsverlust
- Beispiel-Inputs ergeben deterministische, nachvollziehbare Event-Sequenzen

Anhang: Schnittstellen (Skizze)
--------------------------------

```yaml
# ActionInstance (eingereicht)
- id: string
  actor: string
  verb: string
  params: any
  submitted_at: ISO8601

# Event (geplant/ausgeführt)
- type: start|end|interrupt|visibility_change
  action_id: string
  t: int  # Minuten relativ zu epoch.start
  meta: any

# LockTable (zur Laufzeit)
locks:
  workshop:
    held_by: A2
    queue: [A4]
```

