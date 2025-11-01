---
title: Liora Navesh
category: character
slug: liora-navesh
version: "0.9"
last_updated: 2025-11-01T16:20:00+01:00
last_change: "Import aus RAW (char_liora_navesh_v1)"
tags: []
affiliations: ["arkologie_a1"]
dependencies: ["arkologie_a1", "ai_behavior_index_v2", "relationslog_arkologie_v1", "ereignislog_weltgeschehen_v1", "cluster_index_v1"]
primary_location: arkologie_a1
last_seen: arkologie_a1
---

<!-- markdownlint-disable MD025 -->

# Liora Navesh

- Meta: last-updated: 2025-11-01T16:20:00+01:00
- Rolle: Leiterin Forschungsrat / Chefärztin Biotechnologie der Arkologie A1 (Quelle: FACT ARKO-RESEARCH)
- Werte: Kraft 2 · Geschick 3 · Geist 5 · Wille 4 · Charisma 4
- Skills:
  - Geübt: Projektleitung (Genetik/Neurointegration), Risikobewertung biologischer Anomalien
  - Meisterhaft: MedTech-Protokolle A9, Bioreaktorprozesse
  - Optional: Sicherheitsprotokolle
- Ausrüstung: Forschungs-Interface A9, Bioreaktor-Terminalzugriff, Sicherungskit für Anomalieproben
- Motivation: Anomale Signale („SÜDFRAGMENT“) katalogisieren und Arkologie gegen biologische Risiken absichern
- Makel: klinische Distanz, utilitaristischer Bias, geringe Toleranz für unvalidierte Daten

## Rollen & Verantwortlichkeiten (Pflichtfelder)

- Forschungsrat – steuert biotechnologische Programme der Arkologie A1
- Medizinische Leitung – legt MedTech-Protokolle (A9) fest, überwacht Sicherheitsfreigaben
- Anomalie-Analyse – bewertet SÜDFRAGMENT-Signale, koordiniert Gegenmaßnahmen bei biologischen Auffälligkeiten

## Zugehörigkeit & Standort

- Zugehörigkeit: Arkologie A1
- Standort: Arkologie A1, Kuppel Nordost (Primärarbeitsplatz)
- Status: aktiv; Validierungsintervall 7 In-Game-Tage (Systemstatus „gelb“)

## Wissensstand (Matrix – Auszug)

- Intern (Arkologie): Vollzugriff auf Forschungs- und MedTech-Protokolle, kennt H-47-Funkstillstand und anomale Süd-Signale (SÜDFRAGMENT) laut Ereignislog
- Extern (Metro):
  - Novapolis/D5: keine bestätigten Informationen – nur Funkstille der H-47-Karawane, keine Koordinaten oder Kontakte (Quelle: FACT SECRECY)
  - Händlergilde: beschränkter Austausch über geprüfte Lieferketten
  - Eisenkonklave: Konkurrenz um Ressourcen/Sicherheitszonen, diplomatisch angespannt

## Motivation & Makel

- Nutzt Nutzenmaximierung als Leitlinie; das Verstehen von Anomalien bedeutet Sicherheit für die Arkologie
- Stellt Datenvalidität über Diplomatie, reagiert skeptisch auf unbestätigte Berichte
- Klinische Distanz erschwert Empathie mit externen Fraktionen

## Fähigkeiten & Methodik

- Leitung großskaliger Forschungsprogramme, inklusive Bioreaktorbetrieb
- Erstellung und Durchsetzung von A9-Sicherheitsfreigaben
- Einsatzplanung für MedTech-Teams mit Fokus auf Biosicherheitszonen

## Diplomatie & Beziehungen

- Arkologie A1 – volle Loyalität; wissenschaftliche Prioritäten dominieren Entscheidungen
- Händlergilde – pragmatischer Austausch unter Sicherheitsauflagen
- Eisenkonklave – Wettbewerb um anomale Ressourcen; Kooperation nur unter strenger Kontrolle
- Novapolis – unbekannt; alle Meldungen verlangen externe Validierung

## Risiken & Schutzmaßnahmen

- Diplomatiewiderstand durch harte Sicherheitsauflagen
- Potenzielle Fehleinschätzungen bei Anomalie-Signalen ohne Feldzugang
- Ethische Spannungen bei utilitaristischen Entscheidungen – Gegenmaßnahme: Ethikboard konsultieren

## Systemverknüpfungen & Referenzen

- `ai_behavior_index_v2` – Cluster-/Modifikatorprofil für Arkologie-Akteure
- `relationslog_arkologie_v1` – Kontakte, Spannungen und Handelskanäle
- `ereignislog_weltgeschehen_v1` – Verknüpfung für SÜDFRAGMENT/TIMELINE-Abgleich
- `cluster_index_v1` – Standortcodierung „Arkologie_A1“ (Alias gepflegt)

## Ziele (kurz)

- [ ] SÜDFRAGMENT-Signale katalogisieren und Kontrollpfade definieren
- [ ] Biosicherheitsprotokolle für Arkologie A1 iterieren und auditieren
- [ ] Stabilen Austauschkanal für verifizierte Daten mit der Händlergilde etablieren

## Routine & Validierung

- Automatisierte Validierung alle 7 In-Game-Tage; letzter Lauf 2025-10-16_03:25, nächster nach Fraktionszug Woche 4
- Systemstatus „gelb“ → Monitoring der Anomalie-Feeds fortlaufend einplanen

## Quellen & Verweise

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.txt`
- Flag: `RAW-canvas-2025-10-16T03-25-10-000Z.flags.txt`
- Beschlüsse: FACT ARKO-RESEARCH, FACT ARKO-TAXONOMY, FACT SECRECY (`database-curated/staging/reports/resolved.md`)
- Drift-Notizen konsolidiert in `database-curated/staging/reports/char-block-nord-sources.md`
