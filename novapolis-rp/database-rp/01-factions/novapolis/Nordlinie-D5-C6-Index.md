---
stand: 2026-04-26 21:23
update: Der Fortsetzungsindex markiert jetzt explizit den Nordlinie-Strang als chronologisch aktuellen Weltstand; C6-H47 bleibt nur als frueher verworfener Einstiegspunkt dokumentiert.
checks: snapshot-lock PASS (2026-04-26 21:23); markdownlint=PASS; frontmatter=PASS; path-portability=PASS
slug: nordlinie-d5-c6-index
category: index
version: "0.1"
---

Nordlinie D5-C6 - Fortsetzungsindex
===================================

Zweck
-----

Dieser Index buendelt die RP-relevanten SSOTs fuer die laufende Fortsetzung rund um `Nordlinie 01`, den Verbindungstunnel `D5-C6`, die D5-Werkstattarbeit am Draisine-Prototyp und den aktuellen Handover in den SSOT-/Lore-Modus.

Kanonischer Fokus
-----------------

- Der Nordlinie-D5-C6-Strang ist der chronologisch aktuelle Welt- und Fortsetzungsstand fuer das laufende Bespielen im Chat.
- Das fruehere C6-H47-Handelsfenster bleibt als Probe- und Routingversuch dokumentiert, ist aber bewusst nicht der aktuelle Hauptpfad der Weltfortsetzung.
- `Nordlinie 01` bleibt das aktive Tunnelprojekt zwischen `D5` und `C6`.
- Der [Verbindungstunnel D5-C6](./03-locations/Verbindungstunnel-D5-C6.md) bleibt beschaedigt; belastbar offene Bedarfe sind Schweißgeraet, Adapter `DN60` und Stuetzelemente.
- Auf der D5-Seite arbeiten [Ronja Kerschner](./02-characters/Ronja-Kerschner.md) und [Reflex](./02-characters/Reflex.md) im Tunnel.
- Parallel dazu tragen [Jonas Merek](./02-characters/Jonas-Merek.md) und [Pahl Brenner](./02-characters/Pahl-Brenner.md) in `D5` die Werkstatt- und Freigabeschiene fuer das [Draisine-Transportmodul](./05-projects/Draisine-Transportmodul.md).
- Ein freier Durchbruch, ein Materialwunder oder eine vollstaendige Betriebsfreigabe sind aktuell nicht belegt.

SSOT-Kernpfad
-------------

- Fraktionsrahmen: [Novapolis](./Novapolis.md)
- Projektanker: [Nordlinie 01](./05-projects/Nordlinie-01.md)
- Projektanker: [Draisine-Transportmodul](./05-projects/Draisine-Transportmodul.md)
- Missionsanker: [Missionslog-Novapolis](./05-projects/Missionslog-Novapolis.md)
- Ortsanker: [D5](./03-locations/D5.md)
- Ortsanker: [Verbindungstunnel D5-C6](./03-locations/Verbindungstunnel-D5-C6.md)
- Ortsanker: [C6](./03-locations/C6.md)
- Figurenanker: [Ronja Kerschner](./02-characters/Ronja-Kerschner.md)
- Figurenanker: [Reflex](./02-characters/Reflex.md)
- Figurenanker: [Jonas Merek](./02-characters/Jonas-Merek.md)
- Figurenanker: [Pahl Brenner](./02-characters/Pahl-Brenner.md)
- Inventaranker: [D5-Inventar](./04-inventory/D5-inventar.md)
- Inventaranker: [C6-Inventar](./04-inventory/C6-inventar.md)

Prozess- und Fortsetzungsrahmen
-------------------------------

- Produktiver Folgeblock: [RP Folgekorridor Slot 41-45](../../../../novapolis-dev/docs/process/rp-folgekorridor-slot-41-45.ssot.md)
- Gemeinsamer Resume-Vertrag: [Text-RPG Slice 2 Handover v1](../../../../novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md)
- Globale Mechanik-SSOT: [Reference Campaign State](../../00-admin/Reference-Campaign-State.md)

Arbeitsstand fuer die naechste Szene (nicht SSOT)
-------------------------------------------------

- Aktueller Runtime-Hauptanker fuer die Fortsetzung: Nordlinie-D5-C6.
- Runtime-Handover: [scene-log](../../../database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md)
- Runtime-Projektstand: [state/nordlinie-01](../../../database-curated/staging/rp-runtime/state/nordlinie-01.md)

Lesereihenfolge fuer Fortsetzung
--------------------------------

1. [Nordlinie 01](./05-projects/Nordlinie-01.md) fuer Projektstand, Phasen und Teamaufteilung.
2. [Verbindungstunnel D5-C6](./03-locations/Verbindungstunnel-D5-C6.md) fuer Schadlage, Bedarf und Arbeitsraum.
3. [Draisine-Transportmodul](./05-projects/Draisine-Transportmodul.md) fuer die parallele Werkstattlinie in `D5`.
4. [Missionslog-Novapolis](./05-projects/Missionslog-Novapolis.md) fuer belegte Missions- und Transportanker.
5. [Ronja Kerschner](./02-characters/Ronja-Kerschner.md), [Reflex](./02-characters/Reflex.md), [Jonas Merek](./02-characters/Jonas-Merek.md) und [Pahl Brenner](./02-characters/Pahl-Brenner.md) fuer Figurenstimme, Rollen und Actions.
6. Erst danach den nichtkanonischen Arbeitsstand aus dem Runtime-Handover lesen, wenn die naechste Szene direkt an den aktuellen Wechselpunkt anschliessen soll.

Guardrails
----------

- Runtime-Artefakte unter `database-curated/staging/rp-runtime/` sind Arbeitsstand und keine automatische RP-SSOT.
- Das probeweise C6-H47-Handelsfenster darf nicht still als aktueller Fortsetzungsanker gelesen oder weitergeschrieben werden, solange kein ausdruecklicher Richtungswechsel beschlossen ist.
- Neue Fortschritte duerfen `D5`, `C6`, `Nordlinie 01`, Tunnelbedarf und D5-Werkstattdruck fortschreiben, aber keinen freien Vollerfolg oder neue Raeume behaupten.
- Ein Materialfluss wird erst dann RP-SSOT, wenn er in Missions-, Inventar- oder Ortsbelegen sauber belastbar ist.
