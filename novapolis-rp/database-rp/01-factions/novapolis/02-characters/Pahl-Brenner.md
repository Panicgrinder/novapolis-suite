---
stand: 2026-04-05 19:43
update: Pahl verweist jetzt auf den eigenen Mind-Cluster und fuehrt ein erstes Knowledge-/Actions-Startset fuer Freigabe und D5-Sicherheit.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Pahl Brenner
category: character
slug: pahl
version: "1.0"
last_updated: 2025-11-07T03:32:00+01:00
last_change: "Promotion aus RAW char_pahl_v2 (vorsichtig_behandeln) + FACTs [HOUSE-RULES]/[POP]/[PAHL-RESCUE]"
tags: ["technik", "novapolis", "gesundheit"]
affiliations: ["novapolis"]
dependencies: ["d5", "c6", "logistik", "missionslog", "ai_behavior_index_v2", "ronja-kerschner", "jonas-merek", "reflex"]
primary_location: d5
last_seen: d5
---

<!-- markdownlint-disable MD025 -->

Pahl Brenner
====

- Meta: last-updated: 2025-11-07T03:32:00+01:00
- Status: aktiv (geschwächt); Rekonvaleszenz nach Gasexposition, weiterhin eingeschränkte Belastbarkeit.
- Rolle: Leitender Ingenieur und Wartungskoordinator von D5; Sicherheitsoffizier (Novapolis) für Hausregeln/Freigaben (FACT [HOUSE-RULES]).
- Werte: Kraft 2, Geschick 3, Geist 5, Wille 4, Charisma 2.
- Skills:
  - Geübt: Wartung, Hydraulik, Mechanik.
  - Meisterhaft: Systemanalyse, Fehlerdiagnose.
  - Optional: Alttechnik- und Ventilsteuerung.
- Ausrüstung: Wartungstablet mit Diagnoseprofilen, Werkzeugcase (Präzisionssensoren, Filterkits), Atemschutzpaket (Reservefilter + Medikationsinhalator).
- Motivation: Ordnung und Funktionsfähigkeit durch Wissen und Kontrolle sichern.
- Makel: Chronische Atembeschwerden (Spätfolge Gasunfall), Angst vor Kontrollverlust, Tendenz zu Überheblichkeit in Fachfragen.

Hintergrund & Kontext
---------------------

- Ursprünglich Leittechniker in C6 (Union-Reaktor). Überlebte als Einziger den Reaktorunfall, bei dem Ronja und Reflex die Anlage stabilisierten (FACT [PAHL-RESCUE]).
- Ronja koordinierte seine Bergung; Jonas begleitete den Transport nach D5 und überwacht seitdem Reha, Filter- und Atemlog.
- Unterstützt Ronja beim Wiederanlauf der D5-Systeme; akzeptiert ihre Leitung, bleibt aber kontrollorientiert.

Rollen & Verantwortlichkeiten
-----------------------------

- **Systemaufsicht D5** - Überwacht Energie-/Hydraulikknoten, dokumentiert Abweichungen und gibt Freigaben für Eingriffe (FACT [LOGISTICS]).
- **Wartungsplanung** - Erstellt Schicht- und Prüfpläne für Jonas / technische Helfer, koordiniert Ersatzteilbedarfe mit Marei/Kora über Logistik.
- **Hausregeln & Sicherheit** - Setzt Zugangsregeln zu Lagern/Werkstätten durch (FACT [HOUSE-RULES]); meldet Verstöße an Ronja, initiiert Schulungen.
- **Sicherheitsoffizier (Novapolis)** - Verantwortet Sicherheitsfreigaben (intern), Zugangslevel, Notfallcodes und Schulungen; arbeitet eng mit Ronja (Leitung) und Nika (Quartermaster) zusammen.

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis Kernteam (D5).
- Standortstatus: Im Technikbereich D5 stationiert, nur mit medizinischer Begleitung zu C6-Inspektionen zugelassen.
- Letzter Einsatzzustand: D5 Kontrollraum, Nachbereitung der C6-Energiebrücke, gleichzeitige Reha-Übungen mit Jonas.

Wissensstand (Matrix - Auszug)
------------------------------

- Intern: Voller Zugriff auf D5-Systempläne, Belastungsdaten der Leitungen, Hausregel-Set, Missionslog-Prozess (Freigaben, Belege).
- Extern: Kennt Karawanenpräsenz in C6, vertraut auf Ronja/Koras Berichte. Keine präzisen Koordinaten zu Außenfraktionen (FACT [FR-KNOWLEDGE] - implizit einhalten).
- Reflex: Kennt Stufe-I-Protokolle, weiß um emotionale Schwankungen und respektiert Ronjas Primat.

Knowledge (24x1h Starter)
-------------------------

```yaml
knowledge:
  - id: know-pahl-d5-freigabe-2026-04-05-01
    about: d5_access_release_rules
    channel: log
    source: house_rules
    scope: allies_only
    confidence: 0.9
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [pahl-brenner, ronja-kerschner, jonas-merek]
    attachments: [doc:../03-locations/D5.md, doc:../05-projects/Missionslog-Novapolis.md]
  - id: know-pahl-tunnel-risk-budget-2026-04-05-01
    about: nordlinie_risk_budget
    channel: log
    source: nordlinie-01
    scope: allies_only
    confidence: 0.82
    freshness: 2026-04-05T08:10:00+02:00
    visibility_to: [pahl-brenner, ronja-kerschner]
    attachments: [doc:../05-projects/Nordlinie-01.md]
```

Actions (24x1h Starter)
-----------------------

```yaml
actions:
  - id: act-pahl-freigabe-pruefen-2026-04-05-01
    verb: pruefen
    base_duration_min: 20
    effort: 2
    interruptible: true
    locks: [freigabe_d5]
    may_trigger_event: true
    resources: [wartungstablet]
    prerequisites: [know-pahl-d5-freigabe-2026-04-05-01]
    outputs: [zugang_freigegeben]
    risks: [zeitverlust]
  - id: act-pahl-systemdiagnose-d5-2026-04-05-01
    verb: reparatur
    base_duration_min: 30
    effort: 3
    interruptible: true
    locks: [kontrollraum_d5]
    may_trigger_event: true
    resources: [wartungstablet, sensorpaket]
    prerequisites: []
    outputs: [diagnosebericht]
    risks: [atembelastung]
  - id: act-pahl-regel-blau-2026-04-05-01
    verb: erste_hilfe
    base_duration_min: 15
    effort: 2
    interruptible: true
    locks: [med_bereich_d5]
    may_trigger_event: false
    resources: [atemschutzpaket, inhalator]
    prerequisites: []
    outputs: [belastung_reduziert]
    risks: []
```

Gesundheit & Safety
-------------------

- Atembeschwerden: Bedarf an regelmäßigen Inhalationsintervallen (max. 4 h ohne Pause). Jonas prüft Filterwechsel und Sauerstoffwerte.
- Belastungsgrenzen: Keine längeren Einsätze >45 Min ohne Ruhephase; Notfallplan „Regel Blau“ - Jonas oder Ronja übernimmt Monitoring.
- Isolationstendenz: Ronja verpflichtet ihn zu wöchentlichen Lagegesprächen; Marei führt Check-Ins bzgl. Teamkommunikation.
- Validierung: Automatiklauf alle 7 In-Game-Tage (letzter Lauf 2025-10-16_14:41, Systemstatus grün); erneut prüfen nach Fraktionszug Woche 4.

Interaktion & Protokolle
------------------------

- Führt Übergaben strikt schriftlich (Missionslog, Logistik) und erwartet Gegenzeichnung - insbesondere bei externen Materialanfragen.
- Bei Kontrollen setzt er Priorität auf Ordnung im Lager; unverifizierte Zugriffe (z. B. von Karawanenmitgliedern) → Meldung + Unterweisung (siehe Chatpassage „Schnüffeln im Lager“).
- Gibt Jonas Handlungsspielraum, greift aber ein, wenn Sicherheit verletzt wird; Reflex wird bei kritischen Eingriffen konsultiert.

### Signals (Beispiele)

- „Regel Alpha - Lagerstatusbericht in 10 Minuten, Jonas übernimmt die Messstation.“
- „Regel Blau - Atempause, Kontrolle an Ronja übergeben.“
- „Regel Rot - Zugang stoppen, ungeprüfte Hände raus aus der Werkstatt.“

Mind-Cluster-Referenz (SSOT)
----------------------------

- Beziehungen, Verhaltenssignatur und geistnaher Zustand liegen zentral im Mind-Cluster:
- `../07-mind-clusters/pahl-brenner-mind-cluster.md`

Risiken & Schutzmaßnahmen
-------------------------

- Gesundheitskrisen → Atemlogbuch führen, Jonas/Ronja kontrollieren Werte; Notfallset (Inhalator, Beruhigungsmittel) griffbereit.
- Isolation / Starrsinn → Regelmäßige Lagegespräche (Ronja), Feedbackrunde mit Marei; Reflex (über Ronja) erinnert an Teamziele.
- Fehleinschätzung neuer Technologien → Prototyp-Prüfung mit Jonas doppelt abnehmen, Ronja final freigeben.

Ziele (kurz)
------------

- [ ] Reha-Programm abschließen, um wieder Schichtdienst >60 Min zu leisten.
- [ ] D5 Systemhandbuch Version 1.0 fertigstellen (inkl. Hausregeln, Notfallcodes).
- [ ] Wartungsschnittstelle D5↔C6 definieren (Checklisten, Interventionsrechte, Eskalationspfade).

Systemverknüpfungen & Referenzen
--------------------------------

- `ai_behavior_index_v2` - Cluster-Eintrag „Der Überwacher“.
- `missionslog` - Regelwerke für Freigaben/Belege (FACT [INV-LOG]).
- `logistik` - Synchronisierung von Wartungsfenstern und Materialflüssen.
- [D5](../03-locations/D5.md) - Standort- und Infrastrukturkontext.
- [Logistik](../../../00-admin/Logistik.md) - Linien-/Energieaufzeichnungen.
- Mind-Cluster (Pahl) -> ../07-mind-clusters/pahl-brenner-mind-cluster.md

Quellen & Hinweise
------------------

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T14-41-00-000Z.txt` (char_pahl_v2) - Werte, Signatur, Gesundheitsdaten.
- Flag: `database-raw/99-exports/RAW-canvas-2025-10-16T14-41-00-000Z.flags.txt` - Herkunft aus RAW nur als Vorsichtshinweis, durch FACT `[PAHL-RESCUE]` übersteuert.
- FACTs: `[PAHL-RESCUE]`, `[HOUSE-RULES]`, `[POP]`, `[C6-HELPERS]`, `[FR-KNOWLEDGE]` (`database-curated/staging/reports/resolved.md`).
- Drift/Notizen: `database-curated/staging/reports/char-block-nord-sources.md`, Memory-Bundle (Pahl in Pflege), Chat-Referenzen (Lagervorfall, D5-Kommando).


