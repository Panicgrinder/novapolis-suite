---
stand: 2026-02-21 21:58
update: Missionslog-Querverweise als Evidenzblock ergänzt; Handelsaussagen strikt auf belegte Anker ausgerichtet.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md' PASS (2026-02-21 21:55); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md' PASS (EXITCODE=0, 2026-02-21 21:55)"
title: Relationslog – Novapolis (Handel & Diplomatie)
category: canon
slug: relationslog_novapolis_v1
version: "0.1"
---

<!-- markdownlint-disable MD025 -->

Relationslog – Novapolis (Handel & Diplomatie)
==============================================

Zweck
-----
Dieses Dokument konsolidiert die **Handels- und Diplomatie-Lage** von Novapolis (D5 als Kern, C6 als Außenposten) und dient als SSOT-Anker für:

- Partner-Übersichten (Status/Flows)
- Red Lines / Sicherheitsregeln
- Trigger/Events (z. B. H-47)
- Nächste Schritte (Fraktionszug)

Quellen
-------
- RAW: [RAW-canvas-2025-10-16T08-07-00-000Z](../../../../database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.txt)
  - `[DOCID: relationslog_novapolis_v1]` (`TYPE: relations_log`, `VERSION: v1`)

1) Ökonomisches Profil
----------------------

- Überfluss: technische Expertise, Energieerzeugung (reaktorbasiert), Organisationsstrukturen
- Bedarf: Nahrungsmittel, Rohmaterialien, Ersatzteile, medizinische Güter
- Handelsmodus: aktuell intern; externer Handel im Aufbau über C6
- Struktur: zentralisiert unter Leitung von Ronja Kerschner, technische Koordination durch Reflex

2) Aktive und potenzielle Handelspartner
----------------------------------------

### Händlergilde

- Status: im Aufbau (freundlich-neutral)
- Ströme:
  - Export: Energie, technische Reparaturen, Kommunikationszugang
  - Import: Nahrungsmittel, Filter, Grundbedarfsgüter
- Abhängigkeit: gering (autarkes Ziel)
- Bemerkung: erste Handelskontakte über Karawane H-47 (Senn Daru) in C6; siehe Charaktereintrag: [Senn Daru](../02-characters/Senn-Daru.md).

### Eisenkonklave

- Status: potenziell (neutral)
- Ströme:
  - Export: keine (vorbereitet: Energieübertragungen, technische Fertigung)
  - Import: Metall, Ersatzteile
- Abhängigkeit: keine (aber strategisch relevant)

### Flüsterkollektiv

- Status: unbekannt
- Ströme: unbestimmt
- Bemerkung: mehrere Funksignale registriert; Quelle und Absicht unbekannt.

### Arkologie A1 / Schattenbund

- Status: keine Interaktion
- Bemerkung: bisher keine Verbindung, aber in regionalen Analysen als mögliche Einflussfaktoren gelistet.

3) Diplomatische Lage
---------------------

- Grundhaltung: zurückhaltend, rekonstruktiv, autarkieorientiert
- Prioritäten: Stabilisierung der Infrastruktur (Tunnel D5–C6), Sicherung von Energieversorgung, Aufbau friedlicher Außenkontakte
- Militärische Bereitschaft: minimal – Verteidigung über Reflex-Einheit (biotechnologisch) und Drohnenabsicherung

Beziehungen (Skala: feindselig / misstrauisch / neutral / kooperativ)
---------------------------------------------------------------------

- Händlergilde: kooperativ (im Aufbau)
- Eisenkonklave: neutral
- Flüsterkollektiv: unbekannt
- Schattenbund: unbekannt
- Arkologie A1: neutral (keine Interaktion)

SECRECY-Hinweis (Außensicht)
----------------------------

- Außenkontakte ohne belegte Freigabe erhalten keine bestätigten Detaildaten zu D5/Novapolis.
- H-47 wird extern ggf. nur als Funkstille/unklar geführt; interne Lage wird in Novapolis-SSOT-Dateien gepflegt.

4) Handelsdoktrin & Red Lines
-----------------------------

- Keine externen Zugänge zu D5 ohne vorherige Genehmigung.
- Alle Handelsrouten laufen ausschließlich über C6 (Außenposten).
- Jede diplomatische Interaktion wird zentral protokolliert.
- Reflex validiert Kommunikationssicherheit vor jedem externen Kontakt.

5) Interner Logistikvermerk
---------------------------

Wichtiger Hinweis: Der Verbindungstunnel zwischen D5 und C6 befindet sich in kritischem Zustand.
Transporte erfordern derzeit manuelle Koordination und Unterstützung durch Reflex-Einheiten.

Für alle zukünftigen Handels- oder Materialtransfers ist die aktuelle Doctrine-Referenz `novapolis-logistics` zu berücksichtigen.

SSOT-Referenz: Logistik global ([Logistik](../../../00-admin/Logistik.md), slug: `logistik`) und fraktionsspezifisch ([novapolis-logistics](../00-doctrine/novapolis-logistics.md), slug: `novapolis-logistics`).
Hinweis: RAW nennt teilweise noch `novapolis_logistik_v1` (Legacy-Bezeichner).

6) Ereignisse & Trigger (Woche 3)
---------------------------------

- Installation der Luft- und Sensorsysteme in C6 abgeschlossen.
- Erstkontakt mit Händlerkarawane H-47 erfolgreich.
- Reflex hat provisorische Kommunikationsverbindung zwischen C6 und D5 eingerichtet.
- Interner Ressourcenstatus: stabil (ohne belastbare Prozentkennzahl).

7) Geplante Schritte (nächster Fraktionszug)
--------------------------------------------

1. Wiederherstellung der Tunnelstruktur (Projekt Nordlinie 01).
2. Erarbeitung eines formellen Handelsprotokolls mit Händlergilde.
3. Ausbau der Kommunikationskanäle für passive Diplomatie.
4. Einrichtung eines Handelsdepots in C6 (Phase I).

8) Querverweise & Evidenz
-------------------------

- Händler-Anbahnung/H-47-Kontext: [Missionslog-Novapolis - Policy/Setup: C6 als Puffer & Händler-Anbahnung](../05-projects/Missionslog-Novapolis.md#policysetup-c6-als-puffer--händler-anbahnung)
- Infrastruktur-/Tunnelrisiko (D5↔C6): [Missionslog-Novapolis - Anomalie: Verbindungstunnel D5-C6](../05-projects/Missionslog-Novapolis.md#anomalie-verbindungstunnel-d5-c6)
- C6-Monitoring als Lagegrundlage: [Missionslog-Novapolis - Monitoring: C6-Überwachung](../05-projects/Missionslog-Novapolis.md#monitoring-c6-überwachung-auswertung)
- Guardrail: Ohne belastbare Evidenz bleibt ein Zustand im Relationslog `unbestimmt` oder `offen`.

Verlinkungen
------------
- Handel/Diplomatie (Hub/Index): [Index-Handel-Diplomatie](../../../00-admin/Index-Handel-Diplomatie.md)
- Ereignislog Weltgeschehen: [Ereignislog-Weltgeschehen](../../../00-admin/Ereignislog-Weltgeschehen.md)
- Missionslog (Fraktion): [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md)
- Handel/Diplomatie (Händlergilde, Fraktionsakte): [Handel-Diplomatie-Haendlergilde](../../haendlerbund/06-handel-diplomatie/Handel-Diplomatie-Haendlergilde.md)
- Logistik: [Logistik](../../../00-admin/Logistik.md)
