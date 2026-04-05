---
stand: 2026-04-05 19:43
update: Kora verweist jetzt auf den eigenen Mind-Cluster und fuehrt ein startkorridor-taugliches Knowledge-/Actions-Set fuer C6.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Kora Malenkov
category: character
slug: kora-malenkov
version: "1.0"
last_updated: 2026-02-16T12:01:00+01:00
last_change: "Zugehörigkeit/Position aktualisiert: Anschluss an Novapolis; Basis C6."
tags: ["logistik", "karawane", "novapolis"]
affiliations: ["novapolis"]
dependencies: ["echo", "c6", "logistik", "missionslog", "ai_behavior_index_v2", "caravan-moves"]
primary_location: c6
last_seen: c6
---

<!-- markdownlint-disable MD025 -->

Kora Malenkov
=============

- Meta: last-updated: 2026-02-16T12:01:00+01:00
- Rolle: Stellvertretung der Fraktionsleitung (Novapolis); Leitung C6; Logistik- und Handelskoordination (Außenhandel über C6) (FACT [CARAVAN-LEADERSHIP]).
- Werte: Kraft 3, Geschick 4, Geist 5, Wille 4, Charisma 5.
- Skills:
  - Geübt: Verhandlung, Navigation, Organisation.
  - Meisterhaft: Logistikplanung, Menschenführung.
  - Optional: Wartungskoordination / Schadensabschätzung.
- Ausrüstung: Kompakt-Klemmbrett mit Logistikschemata, verschlüsseltes Terminal/Com (D5↔C6), robuste Schutzkleidung + modulare Lampe, Reflex-geprüfte Signalbänder für Echo.
- Motivation: Stabiles Handels-/Versorgungsnetz ohne Kontrollverlust der Crew; Sicherheit vor Tempo.
- Makel: Überwachungstrieb nach Außenlinienüberfällen, Bindungsskepsis, Schlafmangel in Krisenphasen.

Hintergrund & Kontext
---------------------

- Herkunft in Außenlinien des Händlerbunds; nach wiederholten Überfällen Fokus auf kontrollierte Prozesse.
- Koordiniert gemeinsam mit Marei die 20 Evakuierten aus E3 und C6-Basiscrew; externer Konvoi (Marven Kael) bleibt getrennt geführt (FACT [CARAVAN-LEADERSHIP]).
- Echo ist als Reflex-Instanz eng an sie gekoppelt (Nähe aus Zuneigung + Schutz) und dient als mobile Schutz-/Sensorplattform (FACT? [PROXIMITY]).

Rollen & Verantwortlichkeiten
-----------------------------

- **Station C6 intern** - Aufgabenverteilung, Instandsetzung, Schichtpläne, Risikoabgleich mit Ronja/Marei.
- **Logistikknoten** - Bestandsführung, Materialübergaben D5↔C6, Dokumentation im Missionslog (Prozess L.1) und `Logistik`-Canvas.
- **Sicherheitskoordination** - Lagebild mit Echo, Ausgabe von Freigaben für Tunneltrupps, Abgleich mit Nordlinie-01-Projekten.
- **Handel (C6)** - Koordiniert Außenhandel/Übergaben über C6 (Lieferfenster, Austauschlisten, Trust/Protokolle) in Abstimmung mit Ronja (Diplomatie).

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis (C6; ehem. Karawane H-47).
- Status: aktiv, beobachtend; keine externe Mission ohne Marven/Arlen.
- Letzter bekannter Einsatz: C6, täglicher Terminal-Ping nach D5.

Wissensstand (Matrix - Auszug)
------------------------------

- Intern: Kennt D5-Kernteam (Ronja, Jonas, Lumen), Evakuierte, Nordlinie-Projektstatus; vertraulich mit Reflex-/Instanz-Grundregeln soweit für Echo erforderlich.
- Extern: Händlerbund-Kanäle, Außenlinienrouten; keine Weitergabe von Novapolis-Koordinaten ohne Ronjas Freigabe (FACT [FR-KNOWLEDGE]).
- Beobachtet D5/Reflex vorsichtig; hält Entscheidungsprotokolle schriftlich zur Nachvollziehbarkeit.

Knowledge (24x1h Starter)
-------------------------

```yaml
knowledge:
  - id: know-kora-c6-sicherungsstatus-2026-04-05-01
    about: c6_security_status
    channel: log
    source: missionslog-novapolis
    scope: allies_only
    confidence: 0.87
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [kora-malenkov, echo, ronja-kerschner]
    attachments: [doc:../03-locations/C6.md, doc:../05-projects/Missionslog-Novapolis.md#c6-sicherungmarkierung-c6-n3--artefakt-7a]
  - id: know-kora-c6-handover-window-2026-04-05-01
    about: c6_handover_window
    channel: direct
    source: echo
    scope: private
    confidence: 0.79
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [kora-malenkov]
    attachments: [scene:scene-2025-10-27-e]
```

Actions (24x1h Starter)
-----------------------

```yaml
actions:
  - id: act-kora-terminal-ping-d5-2026-04-05-01
    verb: funk
    base_duration_min: 15
    effort: 2
    interruptible: true
    locks: [terminal_c6]
    may_trigger_event: true
    resources: [verschluesseltes_terminal]
    prerequisites: []
    outputs: [d5_status_abgleich]
    risks: [signalverlust]
  - id: act-kora-sicherungskoordination-c6n3-2026-04-05-01
    verb: wache
    base_duration_min: 30
    effort: 3
    interruptible: true
    locks: [zugang_c6_n3]
    may_trigger_event: true
    resources: [echo_signalbaender, lageplan]
    prerequisites: [know-kora-c6-sicherungsstatus-2026-04-05-01]
    outputs: [c6_n3_sicherung]
    risks: [ueberlastung]
  - id: act-kora-uebergabefenster-c6-2026-04-05-01
    verb: handel
    base_duration_min: 25
    effort: 3
    interruptible: true
    locks: [uebergabepunkt_c6]
    may_trigger_event: true
    resources: [protokollmappe]
    prerequisites: []
    outputs: [uebergabe_protokolliert]
    risks: [misstrauen]
```

Interaktion & Safety
--------------------

- Echo-Nähe: Plant Tätigkeiten so, dass Echo physischen Kontakt halten kann; Distanzwarnung löst Schonmodus aus.
- REFLEX-DETACH (Instanz-Usecase): In sicheren Kontexten (z. B. kurze Hilfe bei Logistik/Handwerk) darf Echo kurz lokal ohne Dauer-Körperkontakt agieren; ohne externe Energiequelle steigt der SE-Verbrauch deutlich, daher Rückkehr in Nähe/Kontakt priorisieren. Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md).
- JEALOUSY-GLOVES (Kontakt-Guard): Wenn jemand Kora berühren will, kann Echo die **konkret betroffene Körperstelle** bedecken/abschirmen, um unerwünschten Kontakt zu verhindern; "Stop" beendet sofort, "Freigabe" erlaubt Kontakt (Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).

Hinweis: PROXIMITY-Mechanik (Zuneigung+Schutz, Zustände, Training) siehe [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md).
- Sicherheitsprioritäten: Crew vor Tempo → bei Alarm sofortige Sammelpunkte, Echo führt Schutzmantel.
- Kontrolllisten: Jede Freigabe doppelt (Kora→Marei/Ronja) dokumentieren; Terminalmeldungen an Jonas für Werksabgleich.

### Signals (Beispiele)

- „Echo, Schild bei mir - Blickrichtung Tor.“ → Echo verschiebt Material für Sichtlinie.
- „Echo, löst - Ruheschutz.“ → Echo zieht sich zurück, Kora übernimmt direkte Ansprache.

Mind-Cluster-Referenz (SSOT)
----------------------------

- Beziehungen, Verhaltenssignatur und geistnaher Zustand liegen zentral im Mind-Cluster:
- `../07-mind-clusters/kora-malenkov-mind-cluster.md`

Risiken & Schutzmaßnahmen
-------------------------

- Überkontrolle / Schlafmangel → Marei überwacht Ruhefenster; Echo erinnert an Pausen.
- Vertrauensdefizit → nutzt Protokolle & Witness-Logs, vermeidet Alleingänge.
- Externe Angriffe → Evakuierungsplan mit Echo als Vorwarnsystem, redundante Routen über Verbindungstunnel C6-E3.

Ziele (kurz)
------------

- [ ] C6-Bestandsführung vollständig mit D5/Missionslog synchronisieren.
- [ ] Evakuierte E3-Teams stabil einbinden (Schichtplan + Versorgung).
- [ ] Sicherheitsprotokolle (Echo + menschliche Wache) standardisieren und dokumentieren.

Systemverknüpfungen & Referenzen
--------------------------------

- `logistik` - zentrale Arbeitsgrundlage, Kora als Hauptautorin.
- `missionslog` - Prozess L.1, Freigaben/Terminalmeldungen.
- `caravan-moves` - Koordination externer Läufe mit Marven/Arlen.
- `ai_behavior_index_v2` - Verhaltenseintrag „Die Verhandlerin“.
- [G7](../../haendlerbund/03-locations/G7.md) & [C6](../../novapolis/03-locations/C6.md) - Lage/Risiko.
- Mind-Cluster (Kora) -> ../07-mind-clusters/kora-malenkov-mind-cluster.md

Quellen & Hinweise
------------------

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-00-000Z.txt` (char_kora_malenkov_v2).
- FACT: `[CARAVAN-LEADERSHIP]`, `[PROXIMITY]`, `[FR-KNOWLEDGE]` (`database-curated/staging/reports/resolved.md`).
- Drift & Notizen: `database-curated/staging/reports/char-block-nord-sources.md` (Paranoia/Leadership-Scope).
- Validierung: Automatik alle 7 In-Game-Tage; letzter Lauf 2025-10-16_14:56 (Systemstatus grün).


