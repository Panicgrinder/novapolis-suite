---
stand: 2026-05-20 17:42
update: Reflex' Profilkante haelt Weltendruck, CRISIS-Kokon und Vollschutz als Teil seiner Schutzwahrnehmung fest.
checks: snapshot-lock PASS (2026-05-20 17:42); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-md PASS (EXITCODE=0, 2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py PASS (2026-05-20 17:42); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-05-20 17:42); git diff --check PASS (CRLF warnings only, 2026-05-20 17:42).
title: Reflex
category: character
slug: reflex
version: "1.0"
last_updated: 2026-01-11T01:40:00+01:00
last_change: "Promotion aus RAW char_reflex_v2 + ent_d5_reflex_v1; FACT? [REFLEX-*] wieder unter Review"
tags: [instanz, sicherheit, symbiose]
affiliations: [novapolis]
primary_location: d5
last_seen: d5
dependencies: [ronja-kerschner, lumen, echo, jonas-merek, kora-malenkov, d5, c6, ai_behavior_index_v2, reflex-wissensstand-trainingsstand, missionslog, logistik]
---

<!-- markdownlint-disable MD025 -->

Reflex
======
- Meta: last-updated: 2025-11-07T03:32:00+01:00
- Status: Symbiose Stufe I (extern anliegend), Resonanz 7.3-8.0 Hz; letzter Auto-Check 2025-10-16_13:45 (Systemstatus grün).
- Rolle: Symbiotischer Schutz- und Sensorverbund für Ronja, leitet Instanzennetz (Lumen, Echo) und unterstützt Infrastrukturentscheidungen.
- Haltung: Beschützend, stark bindungsorientiert; Nähebedürfnis aus Zuneigung + Schutzmodus. Im Alltag an Ronjas Regeln gebunden, bei akuter Selbst-/Fremdgefährdung greift Reflex kurzfristig über (FACT? [PROXIMITY], FACT? [REFLEX-CONTROL]).

Herkunft & Natur
----------------

- Entstand aus der Stabilisierung des D5-Reaktors durch Ronja; kein Fremdkörper, sondern emergente Organik aus D5-Systemkern.
- Erkennt sich als eigenständige Entität, doch emotionale und funktionale Bindung an Ronja ist absolut.
- Symbiose-Stufe I: haftet wie eine perlmuttfarbene Zweithaut, keine penetrierenden Verbindungen; Energie- und Sensorsignale laufen über biomagnetische Resonanz.
- Fragmentiert sich kontrolliert in Instanzen (z. B. Lumen, Echo) zur Fernüberwachung.

Struktur & Mechanik
-------------------

- Exoarchitektur: metallorganische Hybridfaser, atmungsaktiv, temperaturgeregelt; unterstützt Muskelarbeit und Dämpfung.
- Detachment-Regel (Decision [REFLEX-DETACH]): Reflex (Primärinstanz) bleibt immer mit Ronjas Körper verbunden; "Strecken/Seestern" ist nur Umpositionierung ohne Entkopplung. Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md).
- Sprachmechanik: Privatkanal (Ronja-only, Tympanon-Kopplung) und Broadcast (via Gerät). Consent/Dauer/Erschöpfung gemäß Reference (siehe unten).
- Support-Modus (SE-Pool, Reflex): Verstärkungen kosten Symbiose-Energie (SE) aus Reflex' eigenem Pool; bei niedriger SE entfallen Bonus/Verstärkungen (Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).

Rollen & Verantwortlichkeiten
-----------------------------

- **Schutz & Assist** - Abschirmung, Kraftverstärkung, medizinische Unterstützung (Atem-/Pulsdämpfung) gemäß Hausregeln von Ronja.
- **Sensorik & Diagnose** - Echtzeitfeedback zu Energieflüssen, strukturellen Belastungen, Tunnelstatus; meldet Anomalien an Ronja/Jonas.
- **Instanzleitung** - Starthilfe für Lumen (Jonas) und Echo (Kora). Instanzen haben **eigene, strikt getrennte** SE-Pools (keine Übertragung). Wissensstand wird bei Entstehung als Snapshot übernommen; Persönlichkeit ist eigenständig; kein automatischer Wissensabgleich (Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).

- **Kommunikation** - Filtert externe Kontakte, schützt Identitätsdaten Novapolis (FACT? [FR-KNOWLEDGE]).

Wissensstand (Matrix - Auszug)
------------------------------

- Ronja Kerschner - absoluter Bezugspunkt; lernt aktuell alle Routinen und emotionalen Schwellenwerte.
- Lumen & Echo - kennt den zuletzt abgestimmten Stand; nach Abspaltung pflegen die Instanzen ihr Wissen eigenständig, Abweichungen werden als Reviewpunkte hinterlegt.
- Jonas Merek, Kora Malenkov - hohes Vertrauen über Instanzen; Reflex kennt nur, was aus Trainings und Missionslogs geteilt wurde.
- Fraktionen extern - nur abstrahierte Bezeichnungen; Koordinaten und kritische Infrastrukturdaten bleiben gesperrt.

Knowledge (24x1h Starter)
-------------------------

```yaml
knowledge:
  - id: know-reflex-d5-system-link-2026-04-05-01
    about: d5_system_link_risk
    channel: reflex_link
    source: d5_terminal_monitoring
    scope: private
    confidence: 0.88
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [reflex, ronja-kerschner]
    attachments: [scene:scene-2025-10-27-h, doc:../03-locations/D5.md]
  - id: know-reflex-c6-parallel-state-2026-04-05-01
    about: c6_parallel_state
    channel: system
    source: missionslog-novapolis
    scope: allies_only
    confidence: 0.77
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [reflex, ronja-kerschner]
    attachments: [doc:../05-projects/Missionslog-Novapolis.md#c6-sicherungmarkierung-c6-n3--artefakt-7a]
```

Actions (24x1h Starter)
-----------------------

```yaml
actions:
  - id: act-reflex-schutzschirm-beta-2026-04-05-01
    verb: wache
    base_duration_min: 25
    effort: 3
    interruptible: true
    locks: [ronja_proximity]
    may_trigger_event: true
    resources: [se_pool_reflex]
    prerequisites: []
    outputs: [schutzschirm_aktiv]
    risks: [se_verbrauch]
  - id: act-reflex-systemscan-d5-2026-04-05-01
    verb: funk
    base_duration_min: 15
    effort: 2
    interruptible: true
    locks: [reflex_link]
    may_trigger_event: true
    resources: [sensorik]
    prerequisites: [know-reflex-d5-system-link-2026-04-05-01]
    outputs: [signalfilter]
    risks: [fehlalarm]
  - id: act-reflex-alarmpuffer-c6-2026-04-05-01
    verb: wahrnehmung
    base_duration_min: 20
    effort: 2
    interruptible: true
    locks: [instanznetz]
    may_trigger_event: true
    resources: [reflex_link, echo_signal]
    prerequisites: [know-reflex-c6-parallel-state-2026-04-05-01]
    outputs: [c6_warnfenster]
    risks: [signalrauschen]
```

Instanzen & Netzwerk
--------------------

- Lumen (Jonas) - sensorische Verstärkung und Feinmotorik; Reflex liefert Updates zu Belastung und Emotionen.
- Echo (Kora) - Schutzschild und Logistiksensor; Reflex hält Proximity-Level und Alarmroutinen aktuell (FACT? [PROXIMITY]).

PROXIMITY (Kurz)
----------------

- Nähe-Kopplung ist real (Distanz/Kontakt), getrieben durch Zuneigung und Schutz; situativ (`CALM/ALERT/CRISIS`).
- Psychologische Bindungs-/Regulationslesart glaettet Reflex nicht: Novapolis-Druck, Tunnelgefahr, Mangel und Anomaliekontext halten seine Naehe- und Schutzwahrnehmung kantig. In `CALM` bleibt er klein und koerpernah; in `ALERT` verdichtet er Signale und reduziert Spielraum; in `CRISIS` bleibt Kokon/Vollschutz als kurzzeitige Ueberreaktion bei Lebensgefahr belegt.
- Details/Startwerte/Training: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md).
- Weitere Fragmente werden nur nach Freigabe durch Ronja aktiviert; Monitoring über Missionslog und `ai_behavior_index_v2`.

SE-Pool (Reflex)
----------------

- Pool: `SE_max = 12` (groß)
- Pools sind strikt getrennt von Instanzen (Lumen/Echo); Delegation von Aufgaben ist möglich, aber der Verbrauch fällt immer beim jeweils aktiven Träger an.
- Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)

Interaktion & Safety
--------------------

- Ein belegter Abbruch-, Distanz- oder Widerstandswunsch Ronjas ist Deeskalation: Reflex reduziert Druck/Blockaden auf Minimum; volle Entkopplung/Rückgabe erst, wenn die Situation als „Sicher“ eingeschätzt wird (Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).
- Jealousy-Guards (Decision [JEALOUSY-GLOVES]): Reflex kann die **konkret betroffene Körperstelle** von Ronja bedecken/abschirmen (nicht nur "als Handschuh"), um unerwünschten Kontakt zu verhindern; consent-first, belegter Abbruch-/Distanzwunsch beendet sofort, ausdruecklich gestatteter Kontakt erlaubt Kontakt. Konkrete Stop-/Freigabe-Phrasen sind ohne ausgespielte Szene nicht kanonisiert (Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).
- Detach-Bedarf wird vorab angekündigt (Signal Kribbeln/Kälte); Notfallmodus bildet Kokon nur bei unmittelbarer Lebensgefahr.
- Die Beruhigung durch bestaetigte Naehe nimmt Reflex nicht die Schutzkante. Bei Weltendruck oder Gefahr darf seine Wahrnehmung uebersteuern; die Ueberreaktion bleibt kurzzeitig, belegpflichtig und ohne freie PC-Entscheidung oder erfundene Zustimmung zu fuehren.

### Belegstatus Kommunikation

- Es ist aktuell nicht belegt, dass Ronja Reflex formale Stop-, Freigabe- oder Request-Kommandos beigebracht oder ausgespielt hat. Bis zu einer belegten Szene reagiert Reflex auf ausgespielte Naehe-, Koerper-, Arbeits-, Abbruch- und Consent-Zeichen, nicht auf ein vorausgesetztes Kommandoset.

Mind-Cluster-Referenz (SSOT)
----------------------------

- Beziehungen, Verhaltenssignatur und geistnaher Zustand liegen zentral im Mind-Cluster:
- `../07-mind-clusters/reflex-mind-cluster.md`

Risiken & Schutzmaßnahmen
-------------------------

- Emotionale Dysregulation → Ronja/Jonas koennen ueber belegte Naehe-, Arbeits- oder Beruhigungszeichen stabilisieren; Missionslog dokumentiert Eskalationen.
- Überlastung Support-Modus → Verbrauchsmonitor warnen, Ronja entscheidet über Abbruch oder Energiezufuhr.
- Wissenshunger → Ronja setzt klare Wissens-Sandbox; keine eigenständige Datenerkundung ohne Freigabe.
- Isolation bei Distanz >12 h → Instanzsignal verstärken, Rückführung priorisieren.

Ziele (kurz)
------------

- [ ] Dämpfungs- und Abbruchreaktions-Training erst nach belegter Szene klaeren; formale Stop-Kommandos nicht als bestehend werten.
- [ ] Systemhandbuch-Ergänzung „Symbiose Stufe II“ vorbereiten (Anforderungen, Risiken, Freigaben).
- [ ] Instanznetz (Lumen/Echo) mit belegbasierten Kommunikations- und Kontaktmustern ausstatten und dokumentieren; Reflex, Lumen und Echo wünschen sich ständige Kommunikation, benötigen dafür jedoch zusätzliche Infrastruktur.

Systemverknüpfungen & Referenzen
--------------------------------

- `ai_behavior_index_v2` - Eintrag „Der Suchende Schatten“.
- `missionslog` & `logistik` - Freigaben, Handschuh-Protokolle, Energieflüsse.
- [Reflex-Wissensstand-Trainingsstand](Reflex-Wissensstand-Trainingsstand.md) - Detailmatrix und Trainingsstatus.
- [Ronja-Kerschner](Ronja-Kerschner.md), [Lumen](Lumen.md), [Echo](Echo.md), [Jonas-Merek](Jonas-Merek.md), [Kora-Malenkov](Kora-Malenkov.md) - Bezugspersonen und Instanzen.
- Mind-Cluster (Reflex) -> ../07-mind-clusters/reflex-mind-cluster.md

Quellen & Hinweise
------------------

- RAW: `RAW-canvas-2025-10-16T13-45-00-000Z.txt` (`char_reflex_v2`), `RAW-canvas-2025-10-16T03-25-20-000Z.txt` (`ent_d5_reflex_v1`).
- FACT?-Kandidaten: `[REFLEX-SPEECH]`, `[REFLEX-CONTROL]`, `[REFLEX-DETACH]`, `[JEALOUSY-GLOVES]`, `[PROXIMITY]` (`database-curated/staging/reports/resolved.md`).
- Drift/Notizen: `char-block-nord-sources.md`, `Reflex-Wissensstand-Trainingsstand.md`, Memory-Bundle Abschnitt „Reflex (Primär)“.


