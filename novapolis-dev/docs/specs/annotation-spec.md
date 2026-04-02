---
stand: 2026-04-02 06:27
update: Skill-Mapping-V1 fuehrt jetzt einen dokumentierten Realabgleich fuer Ronja/Reflex, Pahl sowie Kora/Echo inklusive Kontext-Guard fuer D5-Interimkommando.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
---

Annotation-Spec (Knowledge · Actions · Skill-Ableitung)
=======================================================

Ziel: Schlanke, konsistente Annotationen, die im 24×1h-Modus sofort nutzbar sind und später ohne Rework auf einen feingranularen „Zug-um-Zug“-Scheduler umschalten können. Fokus auf Copy-&-Paste-Snippets (YAML) in Canvases.

1) Knowledge (Wissens-/Sichtbarkeitsmodell)
------------------------------------------

Grundidee: Ereignisse/Informationen werden als Knowledge-Items erfasst. Sichtbarkeit ist pro Akteur steuerbar, inklusive Quelle, Kanal, Vertrauensgrad und Frische. Rückblenden ändern Sichtbarkeit (kein Retcon der Weltwahrheit).

Felder (minimal, stabil)
- id: eindeutige ID (kebab, zeit-/ortsbasiert sinnvoll)
- about: Entität/Thema (z. B. alarm_c6, jonas_position)
- channel: direct | overhear | rumor | log | reflex_link | system
- source: wer/was liefert die Info (Person/Instanz/System)
- scope: private | allies_only | pc | public | redacted
- confidence: 0.0-1.0 (Vertrauen)
- freshness: ISO-Zeitpunkt der Gewinnung
- ttl_min: Gültigkeit in Minuten (optional; 0 = kein TTL)
- visibility_to: [actor_ids] (feingranular; optional, ergänzt scope)
- derivation: optionale Ableitung/Bezug (z. B. aus Reflex-Signal)
- attachments: Referenzen (log:..., audio:..., scene:..., doc:...)

YAML-Snippet (Beispiel)

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

Anwendung je Stunde (24×1h-Modus)
- world_log: enthält alle Events/Knowledge (Wahrheit).
- pc_log: materialisiert nur Items, die für den PC sichtbar sind (scope/visibility_to/ttl/confidence prüfen).
- Rückblenden: Änderungsoperation auf Items (z. B. scope allies_only → pc; confidence ↑ via log), aber keine Umschreibung der Vergangenheit.

Hinweise
- Wichtige Charaktere können eine eigene Datei für Detailwissen führen (z. B. `Reflex-Wissensstand-Trainingsstand.md`).
- Knowledge-Items sind ideale Trigger/Interrupts im späteren Mikro-Scheduler (z. B. „Reflex weckt Ronja“).

2) Actions (für möglichen „Zug-um-Zug“-Wechsel vorbereiten)
-----------------------------------------------------------

Eine Aktion definiert Basisdauer, Ressourcen/Locks und Interrupt-Regeln. Effektive Dauer ergibt sich aus Skill/Tools/Umständen. So könnt ihr später ohne Rework einen tick-losen Scheduler (Min-Heap nach end_at) einsetzen.

Felder (minimal, stabil)
- id: interne ID (kebab)
- verb: Tätigkeitswort (reinigen, reparieren, reisen, wache, funk, erste_hilfe, erkunden)
- base_duration_min: Basisdauer in Minuten (integer)
- effort: grober Aufwand 1-5 (für Balancing/Reporting)
- interruptible: true|false (kann unterbrochen werden?)
- locks: [ressource|location] (exklusive Nutzung, z. B. werkbank)
- may_trigger_event: true|false (kann ein Ereignis auslösen)
- resources: benötigte Dinge (IDs)
- prerequisites: optionale Vorbedingungen (IDs/Knowledge)
- outputs: erwartete Effekte (IDs/Änderungen)
- risks: optionale Risiken (IDs/Prozentsatz/Bedingungen)

YAML-Snippet (Beispiel in Missions-/Orts-Canvas)

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
- f_tools: 0.9-1.2 (Toolqualität), f_cond: 0.9-1.2 (Müdigkeit, Licht, Platz)
- Optionales Noise (±5-10%) nur mit festem Seed pro Epoche für Replays.

Event-Queue (später)
- Plan: Für alle aktiven Akteure erste Aktion planen → Min-Heap nach end_at → Pop → Outcome → Folgeaktion(en). Locks prüfen; Interrupts erlauben (Alarm, Funk, Unfall).
- Überläufe über das Epochenende werden gesplittet; Rest startet in der nächsten Stunde mit start_at=0.

3) Skill-Ableitung aus Verhaltensmatrix (keine zweite Wahrheit)
--------------------------------------------------------------

Die Verhaltensmatrix bleibt die „dynamische Wahrheit“. Skills (0-3) sind eine abgeleitete Sicht für Dauer/Erfolg - jederzeit aus der Matrix berechenbar.

Notation
- m: Matrix-Vektor der Dimensionen (normiert; −1..+1 oder 0..1)
- W: Gewichtsmatrix (k×s) für s Skills (reinigen, reparieren, verhandeln, medizin, stealth, wahrnehmung, …)
- b: Baseline je Skill (rollenabhängig möglich)

Formeln
- Kontinuierlich: $s_{raw} = b + W^T m$
- Diskret (Tier 0-3): $s = \mathrm{clamp}(\mathrm{round}(s_{raw}), 0, 3)$
- Dauer-Effekt via f_skill(s) (siehe oben).

Beispiel-Mapping (Auszug)
- reinigen ← Sorgfalt(+), Geduld(+), Hast(−)
- reparieren ← Technik(+), Ruhe(+), Hast(−)
- verhandeln ← Empathie(+), Dominanz(+/− je Stil), Impulsiv(−)
- medizin ← Empathie(+), Ruhe(+), Präzision(+)
- stealth ← Vorsicht(+), Disziplin(+), Hast(−)
- wahrnehmung ← Aufmerksamkeit(+), Ruhe(+), Überreizung(−)

YAML-Snippet (globale Defaults oder pro Charakter)

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

Novapolis V1 (konservative Arbeitsfassung)
------------------------------------------

Ziel dieser V1 ist nicht ein zweites Progressionssystem, sondern eine stabile Startabbildung fuer die bereits geplanten RP-Kernskills `reparieren`, `wache`, `funk` und `wahrnehmung`.

Normalisierung
- Clusterwerte aus dem Behavior-Canvas werden fuer die Ableitung auf $0.00 .. 0.99$ normiert: $n(c) = c / 100$.
- Verwendet werden nur die im Register belegten Cluster `O, E, M, N, C, S, L, T`.

Rollen-Baselines (V1)
- `wartung_technik`: `reparieren=1.2`, `funk=0.7`, `wahrnehmung=0.6`, `wache=0.4`
- `stationsleitung`: `reparieren=0.8`, `funk=0.8`, `wahrnehmung=0.8`, `wache=1.1`
- `sicherung_monitoring`: `reparieren=0.6`, `funk=0.8`, `wahrnehmung=1.0`, `wache=1.2`

Gewichtsmatrix (V1)
- `reparieren` <- `T +1.0`, `O +0.7`, `N +0.2`, `S +0.1`, `C -0.4`
- `funk` <- `T +0.5`, `O +0.4`, `E +0.3`, `L +0.2`, `C -0.3`
- `wahrnehmung` <- `S +0.7`, `N +0.6`, `O +0.2`, `C -0.4`
- `wache` <- `S +0.7`, `L +0.4`, `O +0.3`, `M +0.2`, `C -0.5`

YAML-Snippet (Novapolis V1)

```yaml
skill_mapping:
  version: 2
  normalize: intensity_div_100
  role_base:
    wartung_technik: { reparieren: 1.2, funk: 0.7, wahrnehmung: 0.6, wache: 0.4 }
    stationsleitung: { reparieren: 0.8, funk: 0.8, wahrnehmung: 0.8, wache: 1.1 }
    sicherung_monitoring: { reparieren: 0.6, funk: 0.8, wahrnehmung: 1.0, wache: 1.2 }
  weights:
    reparieren: { T: 1.0, O: 0.7, N: 0.2, S: 0.1, C: -0.4 }
    funk: { T: 0.5, O: 0.4, E: 0.3, L: 0.2, C: -0.3 }
    wahrnehmung: { S: 0.7, N: 0.6, O: 0.2, C: -0.4 }
    wache: { S: 0.7, L: 0.4, O: 0.3, M: 0.2, C: -0.5 }
```

Beispielableitungen (V1)
- Ronja (`R4`, Rolle `wartung_technik`, Signatur `O82-T79-L70-E60-N69-C45-S38-M20`) -> `reparieren=3`, `funk=2`, `wahrnehmung=1`, `wache=1`
- Jonas (`JNS3`, Rolle `wartung_technik`, Signatur `L55-T68-N40-E72-O50-C42-M78`; nur belegte Cluster genutzt) -> `reparieren=2`, `funk=1`, `wahrnehmung=1`, `wache=1`
- Kora (`KRM4`, Rolle `stationsleitung`, Signatur `L72-T74-N69-E61-O56-C63-M47`) -> `reparieren=2`, `funk=2`, `wahrnehmung=1`, `wache=2`

Rollenfit fuer weitere Kernfiguren (V1)
- `Pahl` bleibt trotz Sicherheitsfreigaben primaer `wartung_technik`, weil die belegte Grundrolle auf Leittechnik, Wartungsplanung und Systemaufsicht liegt; bei explizitem D5-Interimkommando darf V1 situativ `funk +1` und `wache +1` geben, ohne die Grundrolle umzuschreiben.
- `Reflex` und `Echo` werden als `sicherung_monitoring` gelesen, weil Schutz, Sensorik, Alarmroutinen und lokale Signalisierung ihr belegter Primarscope sind.
- `Lumen` bleibt `wartung_technik`, weil Werkstattassistenz und Diagnose der belegte Schwerpunkt sind; Schutz bleibt eng am Werkstatt-/Jonas-Kontext.

Weitere Referenzableitungen (V1)
- Pahl (`PHL2`, Rollenfit `wartung_technik`, Signatur `L48-T60-N71-E50-O44-C62-M30`) -> `reparieren=2`, `funk=1`, `wahrnehmung=1`, `wache=1` (Baseline; im dokumentierten D5-Interimkommando situativ `funk=2`, `wache=2`)
- Reflex (`RFX4`, Rollenfit `sicherung_monitoring`, Signatur `L80-S68-N77-T83-E64-O51-M25-C44`) -> `reparieren=2`, `funk=2`, `wahrnehmung=2`, `wache=2`
- Lumen (`LMN1`, Rollenfit `wartung_technik`, Signatur `L78-T71-E60-O49-N44-S52-C26-M18`) -> `reparieren=2`, `funk=2`, `wahrnehmung=1`, `wache=1`
- Echo (`ECO1`, Rollenfit `sicherung_monitoring`, Signatur `L85-S74-T62-E58-N52-O44-C28-M16`) -> `reparieren=2`, `funk=2`, `wahrnehmung=2`, `wache=2`

Lesart der Beispiele
- Ronja bleibt die staerkste V1-Referenz fuer `reparieren`, weil `O` und `T` sehr hoch sind und `C` nur moderat stoert.
- Jonas ist solide in `reparieren`, aber in `funk` und `wahrnehmung` bewusst nur mittlere V1-Basis, solange kein staerkerer Monitoring-Kontext belegt ist.
- Kora bekommt ueber `stationsleitung` den klarsten `wache`-Wert in Novapolis V1, ohne dass sie zu einer reinen Sicherheitsrolle umgedeutet wird.
- Pahl zeigt, dass V1 technische Leitungsfiguren mit Sicherheitsanteil konservativ lesen kann, ohne sofort eine eigene Hybrid-Baseline einzufuehren.
- Reflex und Echo bestaetigen die `sicherung_monitoring`-Baseline als Schutz-/Sensorprofil; beide bleiben breit stabil, aber ohne ueberzogenes 3er-Niveau.
- Lumen ist die passende Bruecke zwischen Werkstattassistenz und leichtem Schutzkontext: gutes `funk`/`reparieren`, aber bewusst nur mittlere `wache`-Tiefe.

Realabgleich gegen aktive RP-Pfade (2026-04-02)
- `Ronja` + `Reflex` im Missionspfad `D5 -> C6: Materiallauf / Guetertransport` bestaetigen die bestehende Kombination `wartung_technik` + `sicherung_monitoring`: Packen, Abmeldung, Transportassist, Ankunft und Bestandsaufnahme erfordern keinen Rollenlift.
- `Pahl` im belegten D5-Interimkommando bestaetigt keine neue Dauerrolle, aber einen szenengebundenen Zusatzkontext: Wenn D5 explizit unter seinem Freigabe-, Hausregel- und Sicherheitskommando laeuft, darf V1 `funk` und `wache` situativ um je `+1` anheben.
- `Kora` + `Echo` im C6-Schutz-/Logistikkontext bestaetigen die bestehende Kombination `stationsleitung` + `sicherung_monitoring`: Logistikfuehrung, Signalisierung, Nahschutz und Sichtkontakt bleiben damit ohne Zusatzrolle plausibel abgedeckt.
- Referenzpfade: `Missionslog-Novapolis.md`, `scene-2025-10-27-ak.md`, `scene-2025-10-27-d.md`, `scene-2025-10-27-e.md`, `Ronja-Kerschner.md`, `Pahl-Brenner.md`, `Kora-Malenkov.md`, `Reflex.md`, `Echo.md`.

Guardrails fuer V1
- V1 ist absichtlich konservativ: nur 4 Skills, nur 3 Rollen-Baselines, keine versteckten Synergieboni.
- Modifikatoren (`k`, `p`, `r` usw.) bleiben qualitative Driftmarker und werden in V1 nicht direkt verrechnet.
- Kontext-Lifts sind nur zulaessig, wenn Mission, Szene oder Rollenlog die Zusatzlast explizit belegt; sie heben hoechstens zwei Skills um je `+1` und ersetzen keine neue Dauerrolle.
- Ableitungen bleiben on-demand; die Tierwerte werden nicht dauerhaft als zweite Wahrheit in Charakterdateien gespeichert.

Leitlinien
- Keine Speicherung der abgeleiteten Skills als „zweite Wahrheit“; bei Bedarf berechnen.
- Rollen/Tools/Umstände wirken als Faktoren (f_tools, f_cond), nicht als eigene Skill-Systeme.
- Für wichtige Charaktere (z. B. Reflex/Ronja/Jonas) kann eine kleine "override"-Sektion gepflegt werden, falls der Matrix-Vektor temporär unvollständig ist (Debug).

4) Logs & Dateikonventionen (für RP/Sim/TTS)
--------------------------------------------

- 24×1h-Modus: `epoch{dd}/slot{hh}/` als logische Einteilung (oder pro Tag ein Verzeichnis mit 24 Slots).
- Audio (OGG) Namensschema: `epoch{dd}_slot{hh}_{channel}.ogg` (channel: world|pc|sys|ally).
- Knowledge-Attachments können auf diese IDs verweisen; pc_log spielt nur `*_pc.ogg`.

5) Akzeptanzkriterien
---------------------

- Jede Stunde erzeugt (mind.) world_log und pc_log; Sichtbarkeit konsistent mit Knowledge.
- Aktionen im Canvas besitzen verb + base_duration_min; 5-10 Kernaktionen existieren.
- Skill-Ableitung definiert (W/base), mindestens 3 Skills mit Beispielgewichten.
- Späterer Wechsel zu Mikro-Turns ist ohne Datenmigration möglich (nur Engine/Scheduler nötig).

6) Quick-Start (Copy/Paste)
---------------------------

In Charakter- oder Missions-Canvas (Frontmatter-Block genügt):

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
- RP-TODO: Zeitmodell/Annotation & Logs
- Sim-TODO: Epoch-Loader, Audio, Scheduler-Hook
- Agent-TODO: Coqui-Exporter/Service (Build-Time/Runtime)



