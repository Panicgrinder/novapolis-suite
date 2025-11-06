---
stand: 2025-11-06 02:55
update: Frontmatter auf YAML migriert; markdownlint PASS
checks: markdownlint-cli2 PASS
---

Annotation‑Spec (Knowledge · Actions · Skill‑Ableitung)
=======================================================

Ziel: Schlanke, konsistente Annotationen, die im 24×1h‑Modus sofort nutzbar sind und später ohne Rework auf einen feingranularen „Zug‑um‑Zug“‑Scheduler umschalten können. Fokus auf Copy‑&‑Paste‑Snippets (YAML) in Canvases.

1) Knowledge (Wissens-/Sichtbarkeitsmodell)
------------------------------------------

Grundidee: Ereignisse/Informationen werden als Knowledge‑Items erfasst. Sichtbarkeit ist pro Akteur steuerbar, inklusive Quelle, Kanal, Vertrauensgrad und Frische. Rückblenden ändern Sichtbarkeit (kein Retcon der Weltwahrheit).

Felder (minimal, stabil)
- id: eindeutige ID (kebab, zeit-/ortsbasiert sinnvoll)
- about: Entität/Thema (z. B. alarm_c6, jonas_position)
- channel: direct | overhear | rumor | log | reflex_link | system
- source: wer/was liefert die Info (Person/Instanz/System)
- scope: private | allies_only | pc | public | redacted
- confidence: 0.0–1.0 (Vertrauen)
- freshness: ISO‑Zeitpunkt der Gewinnung
- ttl_min: Gültigkeit in Minuten (optional; 0 = kein TTL)
- visibility_to: [actor_ids] (feingranular; optional, ergänzt scope)
- derivation: optionale Ableitung/Bezug (z. B. aus Reflex‑Signal)
- attachments: Referenzen (log:..., audio:..., scene:..., doc:...)

YAML‑Snippet (Beispiel)

```yaml
knowledge:
  - id: alarm_c6_2025-11-01T03:00
    about: alarm_c6
    channel: reflex_link
    source: Reflex
    scope: allies_only
    confidence: 0.95
    freshness: 2025-11-01T03:00:00Z
    ttl_min: 120
    visibility_to: [ronja, reflex]
    attachments: [log:ALRM-2301, audio:epoch03_slot03_pc]
```

Anwendung je Stunde (24×1h‑Modus)
- world_log: enthält alle Events/Knowledge (Wahrheit).
- pc_log: materialisiert nur Items, die für den PC sichtbar sind (scope/visibility_to/ttl/confidence prüfen).
- Rückblenden: Änderungsoperation auf Items (z. B. scope allies_only → pc; confidence ↑ via log), aber keine Umschreibung der Vergangenheit.

Hinweise
- Wichtige Charaktere können eine eigene Datei für Detailwissen führen (z. B. `Reflex-Wissensstand-Trainingsstand.md`).
- Knowledge‑Items sind ideale Trigger/Interrupts im späteren Mikro‑Scheduler (z. B. „Reflex weckt Ronja“).

2) Actions (für möglichen „Zug‑um‑Zug“‑Wechsel vorbereiten)
-----------------------------------------------------------

Eine Aktion definiert Basisdauer, Ressourcen/Locks und Interrupt‑Regeln. Effektive Dauer ergibt sich aus Skill/Tools/Umständen. So könnt ihr später ohne Rework einen tick‑losen Scheduler (Min‑Heap nach end_at) einsetzen.

Felder (minimal, stabil)
- id: interne ID (kebab)
- verb: Tätigkeitswort (reinigen, reparieren, reisen, wache, funk, erste_hilfe, erkunden)
- base_duration_min: Basisdauer in Minuten (integer)
- effort: grober Aufwand 1–5 (für Balancing/Reporting)
- interruptible: true|false (kann unterbrochen werden?)
- locks: [ressource|location] (exklusive Nutzung, z. B. werkbank)
- may_trigger_event: true|false (kann ein Ereignis auslösen)
- resources: benötigte Dinge (IDs)
- prerequisites: optionale Vorbedingungen (IDs/Knowledge)
- outputs: erwartete Effekte (IDs/Änderungen)
- risks: optionale Risiken (IDs/Prozentsatz/Bedingungen)

YAML‑Snippet (Beispiel in Missions‑/Orts‑Canvas)

```yaml
actions:
  - id: reinigen_filter
    verb: reinigen
    base_duration_min: 15
    effort: 2
    interruptible: true
    locks: [werkbank]
    may_trigger_event: true
    resources: [filter, reinigungsset]
    prerequisites: []
    outputs: [filter_status:clean]
    risks: []
```

Deterministische Dauerformel (für späteren Scheduler)
- $t_{eff} = \left\lceil \dfrac{t_{base}}{f_{skill}(s)\cdot f_{tools}\cdot f_{cond}} \right\rceil$
- f_skill(s) (empirischer Start): 0=0.75, 1=1.0, 2=1.5, 3=2.0
- f_tools: 0.9–1.2 (Toolqualität), f_cond: 0.9–1.2 (Müdigkeit, Licht, Platz)
- Optionales Noise (±5–10%) nur mit festem Seed pro Epoche für Replays.

Event‑Queue (später)
- Plan: Für alle aktiven Akteure erste Aktion planen → Min‑Heap nach end_at → Pop → Outcome → Folgeaktion(en). Locks prüfen; Interrupts erlauben (Alarm, Funk, Unfall).
- Überläufe über das Epochenende werden gesplittet; Rest startet in der nächsten Stunde mit start_at=0.

3) Skill‑Ableitung aus Verhaltensmatrix (keine zweite Wahrheit)
--------------------------------------------------------------

Die Verhaltensmatrix bleibt die „dynamische Wahrheit“. Skills (0–3) sind eine abgeleitete Sicht für Dauer/Erfolg – jederzeit aus der Matrix berechenbar.

Notation
- m: Matrix‑Vektor der Dimensionen (normiert; −1..+1 oder 0..1)
- W: Gewichtsmatrix (k×s) für s Skills (reinigen, reparieren, verhandeln, medizin, stealth, wahrnehmung, …)
- b: Baseline je Skill (rollenabhängig möglich)

Formeln
- Kontinuierlich: $s_{raw} = b + W^T m$
- Diskret (Tier 0–3): $s = \mathrm{clamp}(\mathrm{round}(s_{raw}), 0, 3)$
- Dauer‑Effekt via f_skill(s) (siehe oben).

Beispiel‑Mapping (Auszug)
- reinigen ← Sorgfalt(+), Geduld(+), Hast(−)
- reparieren ← Technik(+), Ruhe(+), Hast(−)
- verhandeln ← Empathie(+), Dominanz(+/− je Stil), Impulsiv(−)
- medizin ← Empathie(+), Ruhe(+), Präzision(+)
- stealth ← Vorsicht(+), Disziplin(+), Hast(−)
- wahrnehmung ← Aufmerksamkeit(+), Ruhe(+), Überreizung(−)

YAML‑Snippet (globale Defaults oder pro Charakter)

```yaml
skill_mapping:
  version: 1
  base:
    reinigen: 1
    reparieren: 1
    verhandeln: 1
  weights:
    reinigen:
      sorgfalt: 0.9
      geduld: 0.4
      hast: -0.6
    reparieren:
      technik: 1.0
      ruhe: 0.3
      hast: -0.5
    verhandeln:
      empathie: 0.6
      dominanz: 0.3
      impulsiv: -0.5
```

Leitlinien
- Keine Speicherung der abgeleiteten Skills als „zweite Wahrheit“; bei Bedarf berechnen.
- Rollen/Tools/Umstände wirken als Faktoren (f_tools, f_cond), nicht als eigene Skill‑Systeme.
- Für wichtige Charaktere (z. B. Reflex/Ronja/Jonas) kann eine kleine "override"‑Sektion gepflegt werden, falls der Matrix‑Vektor temporär unvollständig ist (Debug).

4) Logs & Dateikonventionen (für RP/Sim/TTS)
--------------------------------------------

- 24×1h‑Modus: `epoch{dd}/slot{hh}/` als logische Einteilung (oder pro Tag ein Verzeichnis mit 24 Slots).
- Audio (OGG) Namensschema: `epoch{dd}_slot{hh}_{channel}.ogg` (channel: world|pc|sys|ally).
- Knowledge‑Attachments können auf diese IDs verweisen; pc_log spielt nur `*_pc.ogg`.

5) Akzeptanzkriterien
---------------------

- Jede Stunde erzeugt (mind.) world_log und pc_log; Sichtbarkeit konsistent mit Knowledge.
- Aktionen im Canvas besitzen verb + base_duration_min; 5–10 Kernaktionen existieren.
- Skill‑Ableitung definiert (W/base), mindestens 3 Skills mit Beispielgewichten.
- Späterer Wechsel zu Mikro‑Turns ist ohne Datenmigration möglich (nur Engine/Scheduler nötig).

6) Quick‑Start (Copy/Paste)
---------------------------

In Charakter‑ oder Missions‑Canvas (Frontmatter‑Block genügt):

```yaml
knowledge:
  - id: sample_event
    about: patrol_pass
    channel: overhear
    source: patrol_unit
    scope: allies_only
    confidence: 0.7
    freshness: 2025-11-01T05:00:00Z
    ttl_min: 90
    visibility_to: [kora, echo]

actions:
  - id: wache
    verb: wache
    base_duration_min: 60
    effort: 2
    interruptible: true
    locks: []
    may_trigger_event: true

skill_mapping:
  version: 1
  base: { wache: 1 }
  weights:
    wache:
      aufmerksam: 0.8
      ruhe: 0.2
      ueberreizung: -0.4
```

Verweise
- RP‑TODO: Zeitmodell/Annotation & Logs
- Sim‑TODO: Epoch‑Loader, Audio, Scheduler‑Hook
- Agent‑TODO: Coqui‑Exporter/Service (Build‑Time/Runtime)

