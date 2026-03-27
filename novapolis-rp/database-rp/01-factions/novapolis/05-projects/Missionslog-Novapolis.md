---
stand: 2026-03-27 09:54
update: Knowledge-Startset für Kernereignisse und Sichtbarkeits-Promotionsprozess (ohne Retcon) ergänzt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260327_011507.md
title: Missionslog (Novapolis)
category: project
slug: missionslog-novapolis
version: "1.0"
last_updated: 2026-03-20T11:40:00+01:00
status: active
owners: [novapolis]
authority_chain:
  - "fraktion:novapolis"
  - "fraktions-leitung:ronja-kerschner"
  - "stellv-fraktions-leitung:kora-malenkov"
  - "leitung-sicherheit:pahl-brenner"
  - "leitung-logistik:kora-malenkov"
  - "stationsleitung:ronja-kerschner"
tags: [rp, missionen, novapolis]
dependencies: [novapolis, nordlinie-01, logistik]
---

<!-- markdownlint-disable MD025 -->

Missionslog (Novapolis)
=======================

Zentrale Übersicht aller Missionen (aktiv und abgeschlossen). Quelle für Status, Belege/Quittungen und Verlinkungen in andere Canvas.

Felder je Eintrag
-----------------

- Name
- Ziel
- Start
- Ende
- Status (aktiv/abgeschlossen/fehlschlagend)
- Belege/Quittungen (Links)
- Verantwortliche (Personen/Rollen)
- Inventar-Link (Canvas/Abschnitt)

Hinweise
--------

- Rollenpflicht: Wächter, Technik, Leitung, Logistik, Med. Anführer/innen führen immer 2 Rollen (Anführer/in + eine weitere).
- Verknüpfungen: Relevante Locations/Projekte bitte verlinken.
- Legende: `-` = aktuell unbekannt/ungeklärt (keine neue Canon-Behauptung); `tbd` = konkrete Nacharbeit (mit Quelle) geplant.

---

Prozess L.1 - Missionsfluss
---------------------------

- Status → Inventarabschluss → Verlinkungen (Logistik/Missionen) → Archiv
- Referenz: [C6 - Logistik-Policy](../03-locations/C6-Logistik-Policy.md)

Knowledge-Items (Kernereignisse, Startset)
------------------------------------------

```yaml
knowledge:
  - id: know-mis-c6-monitoring-2026-02-22-01
    about: c6_monitoring_status
    channel: log
    source: scene-2025-10-27-b
    scope: allies_only
    confidence: 0.8
    freshness: 2026-02-22T00:00:00+01:00
    visibility_to: [ronja-kerschner, jonas-merek, kora-malenkov]
    attachments: [scene:scene-2025-10-27-b, log:missionslog-novapolis#monitoring-c6-ueberwachung-auswertung]
  - id: know-mis-c6n3-artifact-7a-2026-02-22-01
    about: c6_n3_artifact_7a
    channel: direct
    source: scene-2025-10-27-d
    scope: allies_only
    confidence: 0.75
    freshness: 2026-02-22T00:00:00+01:00
    visibility_to: [ronja-kerschner, reflex]
    attachments: [scene:scene-2025-10-27-d, log:missionslog-novapolis#c6-sicherungmarkierung-c6-n3--artefakt-7a]
  - id: know-mis-e3-risk-2026-02-22-01
    about: e3_risk_signal
    channel: system
    source: reflex
    scope: pc
    confidence: 0.7
    freshness: 2026-02-22T00:00:00+01:00
    visibility_to: [ronja-kerschner]
    attachments: [log:missionslog-novapolis#anomalie-e3-gefahr]
```

Rückblenden-/Promotion-Prozess (ohne Retcon)
--------------------------------------------

- Trigger: neue Evidenz (Funk, Log-Quittung, bestätigte Scene, Instanz-Report).
- Operation: bestehendes Knowledge-Item nur in der Sichtbarkeit heben (`private`/`allies_only` → `pc`), Inhalt/Quelle nicht rückwirkend umschreiben.
- Nachweis: im Missionslog bei betroffenem Eintrag mit Attachment referenzieren (`log:`/`scene:`/`doc:`).

Actions-Schema (Kernaktionen 24x1h)
-----------------------------------

```yaml
actions:
  - id: reinigen_filter
    verb: reinigen
    base_duration_min: 15
    effort: 2
    interruptible: true
    locks: [werkbank]
    may_trigger_event: false
    resources: [filter, reinigungsset]
  - id: reparatur_leitung
    verb: reparatur
    base_duration_min: 45
    effort: 4
    interruptible: true
    locks: [leitungsabschnitt]
    may_trigger_event: true
    resources: [werkzeugkit, ersatzteilset]
  - id: reise_tunnel_d5_c6
    verb: reise
    base_duration_min: 60
    effort: 3
    interruptible: false
    locks: [tunnelkorridor]
    may_trigger_event: true
    resources: [schutzmaske, lichtquelle]
  - id: wache_c6_posten
    verb: wache
    base_duration_min: 60
    effort: 2
    interruptible: true
    locks: [beobachtungsposten]
    may_trigger_event: true
    resources: [funkgeraet]
  - id: funk_scan
    verb: funk
    base_duration_min: 20
    effort: 2
    interruptible: true
    locks: [terminal]
    may_trigger_event: true
    resources: [funkterminal]
  - id: erste_hilfe_basis
    verb: erste_hilfe
    base_duration_min: 25
    effort: 3
    interruptible: true
    locks: [med_bereich]
    may_trigger_event: false
    resources: [medkit]
  - id: erkundung_schacht
    verb: erkundung
    base_duration_min: 40
    effort: 4
    interruptible: true
    locks: [schachtzugang]
    may_trigger_event: true
    resources: [karte, lichtquelle]
  - id: bergen_artefakt_7a
    verb: bergen
    base_duration_min: 50
    effort: 4
    interruptible: false
    locks: [fundstelle_c6_n3]
    may_trigger_event: true
    resources: [abschirmkit, transportbox]
```

Aktiv
-----

T+0: Scene-Anker (Tasks/Belege, ohne neue Fakten)
--------------------------------------------------

Hinweis: Diese Liste ergänzt nur belegte Anker aus den Scenes. Start/Ende/Verantwortliche/Inventar bleiben `-`, solange keine belastbaren Daten vorliegen.

### D5: Wartungsauftrag & Wartungsgang

- Ziel: Wartungsauftrag/Beobachtung als Anker dokumentieren; Ownership/Contents der Werkzeugtasche offen lassen
- Start: -
- Ende: -
- Status: -
- Belege/Quittungen: [scene-2025-10-27-g](../../../06-scenes/scene-2025-10-27-g.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [D5](../03-locations/D5.md)

### D5: Terminal/Port & System-Link

- Ziel: System-Link/Terminalzugriff als Anker dokumentieren; Outputs erst nach belegten Details übernehmen
- Start: -
- Ende: -
- Status: -
- Belege/Quittungen: [scene-2025-10-27-h](../../../06-scenes/scene-2025-10-27-h.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [D5](../03-locations/D5.md)

### D5: Basispflege & Exoskelett-Idee

- Ziel: Basispflege/Ordnung als wiederkehrenden Faden dokumentieren; Exoskelett-Idee als Projektfaden markieren
- Start: -
- Ende: -
- Status: -
- Belege/Quittungen: [scene-2025-10-27-i](../../../06-scenes/scene-2025-10-27-i.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [D5](../03-locations/D5.md)

### C6: Sicherung/Markierung (C6-N3) & Artefakt „7A“

- Ziel: Sicherung/Abschirmung vor Bergung; Artefakt-Markierung „7A“ als Arbeitsanker führen
- Start: -
- Ende: -
- Status: -
- Belege/Quittungen: [scene-2025-10-27-d](../../../06-scenes/scene-2025-10-27-d.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [C6](../03-locations/C6.md)

### C6: Abschluss/Übergabe & Echo-Moment

- Ziel: Abschluss-/Übergabemoment dokumentieren; Echo-Status nur als Notiz führen
- Start: -
- Ende: -
- Status: -
- Belege/Quittungen: [scene-2025-10-27-e](../../../06-scenes/scene-2025-10-27-e.md), [scene-2025-10-27-f](../../../06-scenes/scene-2025-10-27-f.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [C6](../03-locations/C6.md)

### C6: Funk/Scan & Stationssuche

- Ziel: Kontaktaufnahme/Scan/Suche als Arbeitsauftrag; Ergebnisse erst nach belegtem Output kanonisieren
- Start: -
- Ende: -
- Status: -
- Belege/Quittungen: [scene-2025-10-27-j](../../../06-scenes/scene-2025-10-27-j.md), [scene-2025-10-27-k](../../../06-scenes/scene-2025-10-27-k.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [C6](../03-locations/C6.md)

### Policy/Setup: C6 als Puffer & Händler-Anbahnung

- Ziel: C6 als Puffer-Policy festhalten; Händler-Anbahnung via Reflex als Faden; keine Reparatur-/Zustandsbeschönigung
- Start: -
- Ende: -
- Status: -
- Belege/Quittungen: [scene-2025-10-27-m](../../../06-scenes/scene-2025-10-27-m.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [C6](../03-locations/C6.md)

### D5 -> C6: Materiallauf / Guetertransport

- Ziel: Material fuer C6-Reparaturen und Betriebsaufnahme aus D5 nach C6 bringen, ohne den Tunnelzustand zu beschoenigen.
- Start: -
- Ende: -
- Status: -
- Belege/Quittungen: [Nordlinie-01](./Nordlinie-01.md), `../../../../database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `../../../../database-raw/99-exports/chat-export.txt`
- Verantwortliche: -
- Inventar-Link: [Novapolis-inventar](../04-inventory/Novapolis-inventar.md)
- Orte/Projekte: [D5](../03-locations/D5.md), [C6](../03-locations/C6.md), [Nordlinie-01](./Nordlinie-01.md)
  Hinweise:
  - RAW belegt die generische Fracht `D5 -> C6 (Bauteile, Werkzeuge, Versorgungsgueter)` sowie `C6 -> D5 (Materialrueckfuehrung)`.
  - Der Chatverlauf belegt bewusst keine feste Stueckliste vor dem Lauf; die Auswahl sollte situativ bzw. nach Funkabgleich erfolgen.
  - Fuer Entnahme, Ankunft, Zielbuchung und Quittung fehlen weiterhin belastbare Item-Zeilen; der Missionsanker taugt daher nur als Transferkontext, nicht als Mengenabschluss.

### Anomalie: C6-Nordanomalie

- Ziel: Lokalisieren, Effekte erfassen, Risiken/Trigger katalogisieren
- Hinweis: Bereich wurde damals von Ronja mit Reflex versiegelt; Zugang nur unter expliziter Freigabe.
- Start: -
- Ende: -
- Status: aktiv
- Belege/Quittungen: -
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [C6](../03-locations/C6.md)

### Anomalie: Verbindungstunnel D5-C6

- Ziel: Anomalie detektieren, Sicherung, Einfluss auf Bau/Verkehr
- Start: -
- Ende: -
- Status: aktiv
- Belege/Quittungen: [scene-2025-10-27-a](../../../06-scenes/scene-2025-10-27-a.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [Verbindungstunnel D5-C6](../03-locations/Verbindungstunnel-D5-C6.md)

### Monitoring: C6-Überwachung (Auswertung)

- Ziel: Monitoring-/Überwachungsdaten sichten, Signal/Rauschen trennen, Risiken priorisieren
- Start: -
- Ende: -
- Status: aktiv
- Belege/Quittungen: [scene-2025-10-27-b](../../../06-scenes/scene-2025-10-27-b.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [C6](../03-locations/C6.md)

### Anomalie: E3-Gefahr?

- Ziel: Quelle und Wirkung klären; Monitoring etablieren
- Kontext: Ronja und Reflex entdeckten akute Energieschwankungen; daraufhin wurde die Evakuierung nach C6 vorgeschlagen.
- Start: -
- Ende: -
- Status: aktiv
- Belege/Quittungen: -
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: -
  Hinweise:
  - Gasunfall-Station ist E2 (siehe Unklarheiten-Beschluss).
  - Wer die Netztrennung/Abschaltung von E3 bemerkt, hängt davon ab, wer E3 (bzw. die Energie-/Sensorstrecken) überwacht hat.

### Bauabschnitt: Nordlinie-01 (Projekt)

- Ziel: Fortschritt gemäß E/S/B + Arbeitsblöcken dokumentieren (skalierbar)
- Start: -
- Ende: -
- Status: aktiv (Fortschritt 40% von 2 600 m)
- Belege/Quittungen: [scene-2025-10-27-c](../../../06-scenes/scene-2025-10-27-c.md)
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [Nordlinie-01](./Nordlinie-01.md)

---

Abgeschlossen
-------------

### Erste Mission nach C6: Fehlschlag

- Ziel: tbd
- Start: -
- Ende: -
- Status: abgeschlossen (Ergebnis: Fehlschlag)
- Belege/Quittungen: -
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [C6](../03-locations/C6.md)

### Aufnahme von Jonas

- Ziel: Aufnahme/Integration
- Start: -
- Ende: -
- Status: abgeschlossen
- Belege/Quittungen: -
- Verantwortliche: -
- Inventar-Link: -
- Orte/Projekte: [C6](../03-locations/C6.md)
