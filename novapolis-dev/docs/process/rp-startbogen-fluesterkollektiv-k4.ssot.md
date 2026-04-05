---
stand: 2026-04-05 19:43
update: K4 fuehrt jetzt Mind-Cluster-Anbindung, lokale Unterraeume und konservative Nebenstart-Hooks.
checks: snapshot-lock PASS (2026-04-05 10:53); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Fluesterkollektiv K4
===================================

Zweck
-----

Dieser Startbogen definiert `K4` als spielbaren Start fuer das Fluesterkollektiv mit Schwerpunkt auf indirekten Kanaelen, Tarnung und kontrollierter Einflussnahme.

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/03-locations/K4.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/02-characters/Iris-Vey.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/02-characters/Corin-Mael.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/02-characters/Sera-Kaal.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/05-projects/Missionslog-Fluesterkollektiv.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/06-handel-diplomatie/Relationslog-Fluesterkollektiv.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `faction_start`
- Bereich: `K4`
- Gebietsklasse: `faction_core`
- Dichtegrad: `full_slice`

Startpraemisse
--------------

Der PC startet in einem Fluesterkollektiv-Knoten, der nicht auf offene Macht, sondern auf indirekte Kontakte, Signale und Abschirmung setzt.

Belegte Ausgangslage
--------------------

- `K4` ist aktiver Knoten des Fluesterkollektivs.
- Iris Vey fuehrt Strategie und Einflusslinien.
- Corin Mael fuehrt indirekte Tausch- und Informationskanaele.
- Sera Kaal sichert Freigaben, Zutrittszonen und Gegenaufklaerung.
- Gegen Novapolis ist nur `unbekannt` belegt; es existieren mehrere Signale, aber keine bestaetigte Quelle oder Absicht.
- Das Kollektiv ist als Informations- und Spezialgueterraum gerahmt, nicht als offener Warenraum.

Startkern
---------

- Iris Vey
- Corin Mael
- Sera Kaal

Mind-Cluster-Anbindung
----------------------

- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/07-mind-clusters/iris-vey-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/07-mind-clusters/corin-mael-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/07-mind-clusters/sera-kaal-mind-cluster.md`

Lokale Tiefenschaerfe (T0)
--------------------------

- Leitstand der Fluesterzelle: Iris fuehrt Tarnung, Richtung und Einflusslinien.
- Handelszelle: Corin haelt indirekte Tausch- und Informationskanaele schmal.
- Sicherheitsleitstand: Sera filtert Zutritt, Freigaben und Gegenaufklaerung.
- Signalhygiene: lokaler Konfliktraum zwischen Kontaktchance und Abschirmungszwang.

Erste Stakes
------------

- Jeder offene Kontakt droht Anonymitaet und Einflusslinien zu schaedigen.
- Der Wert der Fraktion liegt eher in Information und Signaltechnik als in offenen Sachguetern.
- Unbekannte Signale koennen Chance oder Risiko sein, aber nicht frei deutbar.

Erster Entscheidungsraum
------------------------

1. Ein indirektes Kontaktfenster vorsichtig oeffnen.
2. Erst Signal- und Quellenhygiene pruefen, bevor reagiert wird.
3. Spezialgut oder Information priorisieren und den Rest abschirmen.
4. Gegenaufklaerung ueber Tempo stellen und die Reichweite klein halten.

Fail-forward
------------

- Fehlentscheidungen fuehren zuerst zu verbrannten Kanaelen, Signalrauschen oder engeren Freigaben.
- Ein misslungener Kontakt bleibt reparierbar ueber neue indirekte Wege statt harten Dead Ends.

Nebenstart-Hooks
----------------

- Einfluss-Hook: Einstieg ueber Iris' Leitstand und eine kontrollierte Einflussentscheidung.
- Kanal-Hook: Einstieg ueber Corins Handelszelle und die Frage, welcher indirekte Kontakt priorisiert wird.
- Sicherheits-Hook: Einstieg ueber Seras Leitstand und Signal-/Zutrittshygiene.

Reveal-Regeln
-------------

- `pc_visible`: Kontaktfenster, Signalfragen, Sicherheitsfreigaben, unmittelbare Risikoabwaegung
- `allies_only`: interne Kanaltrennung und Einflussprioritaeten
- `world_only`: nicht validierte Gegenparteien, eigentliche Absichten, tiefe Netzlogik
- `rumor`: ungesicherte Signaldeutungen und potentielle Kontaktgeruechte

Guardrails
----------

- Keine benannten Gegenparteien oder Lieferwege erfinden.
- Keine offene Novapolis-Verbindung behaupten.
- Keine konkreten Spezialgueter- oder Mengenlisten setzen.
