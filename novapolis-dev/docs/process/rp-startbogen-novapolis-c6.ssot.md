---
stand: 2026-04-05 19:43
update: Der C6-Startbogen referenziert jetzt den geschlossenen Mind-Cluster-Unterbau fuer Kerncast und direkten Anschlussraum.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Novapolis C6
===========================

Zweck
-----

Diese SSOT definiert den ersten eigenstaendigen Novapolis-Start in C6 als Parallelstart zum D5-Default-Slice.

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-d.md`
- `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-e.md`
- `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-k.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Kora-Malenkov.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md`
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md`
- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`

Startklasse
-----------

- Modus: `faction_start`
- Bereich: `C6`
- Gebietsklasse: `faction_core`
- Dichtegrad: `full_slice`

Startpraemisse
--------------

Der PC startet in einem teilaktiven Aussenposten mit knapper Kernzone, hohem Sicherungsdruck und staendigem Abgleich zwischen lokaler Gefahr und Rueckmeldung nach D5. Der Start ist operativer, enger und riskozentrierter als der D5-Default-Slice.

Belegte Ausgangslage
--------------------

- C6 ist teilaktiv mit stabilisiertem Reaktor, aktiver Kernzone A/B/C und begrenzter nutzbarer Flaeche.
- Kora fuehrt C6 intern; Echo ist ihr lokaler Schutz- und Sensorverbund.
- C6-N3 fuehrt einen belegten Sicherungs- und Markierungsanker um Artefakt `7A`.
- Ein Abschluss-/Uebergabemoment mit Echo ist belegt.
- Funk-/Scan- und Suchaktivitaet in C6 ist belegt.
- C6 ist zugleich Logistik-, Handels- und Tunnelknoten zwischen D5, E3 und dem weiteren Aussenraum.

Startkern
---------

- Kora Malenkov: Leitung C6, Logistik, Sicherheitskoordination, Handelsschnittstelle
- Echo: lokaler Schutz, Naehe-, Warn- und Schildinstanz
- zweiter Ring: C6-Helper, Evakuierte, H-47-Praesenz vor Ort

Erste Stakes
------------

- C6 ist nicht voll gesichert; Sicherung und Informationsdisziplin gehen vor Neugier.
- Jede Entscheidung beruehrt lokale Sicherheit, Tunnelanbindung, D5-Vertrauen und spaetere Handelslage zugleich.
- Das Artefaktfeld C6-N3 darf nicht unkontrolliert von Sicherung auf Analyse kippen.
- Echo und Kora muessen Informationen filtern, bevor sie Richtung D5 gespiegelt werden.

Erster Entscheidungsraum
------------------------

1. C6-N3 zuerst sichern und die Markierung `7A` sauber im Arbeitsmodus halten.
2. Funk/Scan und Stationssuche priorisieren, bevor lokale Folgehandlungen eskalieren.
3. D5 frueh informieren oder Informationen zunaechst lokal halten.
4. Tunnel-, Lager- oder Aussenkontaktpfad vorziehen, je nach aktueller Risikolage.

Fail-forward
------------

- Zu spaete Meldungen fuehren zuerst zu Misstrauen, Verzerrung oder spaeterem Reveal, nicht zu einem harten Dead End.
- Eine uebervorsichtige Sicherung verlangsamt C6, laesst aber den Start spielbar.
- Ein riskanter Such- oder Scanpfad darf Folgeaufwand und Schutzbedarf erhoehen, aber den Run nicht abschneiden.

Reveal-Regeln
-------------

- `pc_visible`: lokale C6-Lage, Kernzone, Sicherungsdruck, Funk-/Scanauftrag, unmittelbare Echo-/Kora-Optionen
- `allies_only`: bestaetigte Statusmeldungen, Abschluss-/Uebergabefenster, intern verteilte Logistik- und Sicherheitsinfos
- `world_only`: ungepruefte Deutungen zum Artefakt `7A`, rohe Aussen- und Anomalielage, nicht freigegebene Langfristfolgen
- `rumor`: Lebenszeichen, Schattensignale oder unklare Tunnelhinweise ohne bestaetigten Output

Abgrenzung gegen D5
-------------------

- D5 ist der stabilere, sozial dichtere und systemzentrierte Default-Start.
- C6 ist der enger gefasste Aussenposten-Start mit staerkerem Fokus auf Sicherung, Filterung und lokalem Risikomanagement.
- Beide Starts teilen dieselbe Novapolis-SSOT, aber nicht denselben unmittelbaren Informations- und Entscheidungsraum.

Offene Luecken
--------------

- Details zum Artefakt `7A` bleiben bewusst offen.
- Exakte Ergebnisse der C6-Suche und des Funk-/Scanlaufs bleiben offen, solange kein weiterer belegter Output vorliegt.
- Mind-Cluster fuer `Kora`, `Echo`, `Marven`, `Arlen`, `Marei` und `Senn` liegen jetzt als eigenstaendige SSOTs vor.

Guardrails
----------

- Keine freien Artefakt- oder Anomaliedetails erfinden.
- Keine Vollsicherheit fuer C6 behaupten, die die Statusangabe `teilaktiv` unterlaeuft.
- Keine D5-Wissenslage ungeprueft in den C6-Start hineinschieben.
