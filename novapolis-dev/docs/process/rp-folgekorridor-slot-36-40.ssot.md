---
stand: 2026-04-17 04:39
update: Der Folgepfad hinter slot 35 fuehrt jetzt slot 36-40 als fuenfte Kampagnenstufe auf demselben Slice-2-Handover-Rahmen.
checks: snapshot-lock PASS (2026-04-17 02:49); markdownlint=PASS; frontmatter=PASS
---

RP Folgekorridor: Slot 36-40
============================

Zweck
-----

Diese SSOT fuehrt den Produktpfad hinter `slot 35` in eine fuenfte Kampagnenstufe. Der Fokus liegt auf einem lesbaren Wiederanlauf nach dem ersten Folgeblock, der sauberen Fortschreibung von Carry-Over-Arbeiten zwischen `D5`, `C6`, `G7`, `E2` und `F1` sowie einem belastbaren Anschluss fuer den naechsten adapterfaehigen Ausbau statt freier Weltverbreiterung.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`
- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md`
- `novapolis-rp/database-rp/03-locations/E2.md`
- `novapolis-rp/database-rp/03-locations/F1.md`

Korridorvertrag
---------------

- `slot 36-40` setzt `Text-RPG Slice 2 Handover v1` und den Folgeblock `slot 31-35` ohne Namens-, Resume- oder Reveal-Drift fort.
- `D5`, `C6`, `G7`, `E2` und `F1` bleiben die einzigen belastbaren Anschlussraeume; neue Stationen, Verbindungen, Crews oder Fraktionsrechte werden nicht frei ergaenzt.
- Der Block bleibt save-, resume- und replay-lesbar; `slot 40` endet mit einem klaren Folgeanker fuer den naechsten adapterfaehigen Ausbau statt mit freier Expansion.
- Innenpfad, Kontaktpfad und schmaler Randpfad bleiben gegeneinander verschiebbar, duerfen aber weder den Missionsrahmen noch die bestehende Reveal-Matrix verlassen.

Carry-Over- und Resume-Lesart
-----------------------------

- Startanker des Blocks ist derselbe Folgeanker aus `slot 35`; `resume_checkpoint_id`, letzter abgeschlossener `turn_id` und die offenen Carry-Over-Arbeiten muessen auf denselben Handover zeigen.
- `turn_resume_ready` bleibt auch in `slot 36-40` der einzige kanonische Zustand fuer Checkpoint, Resume und Replay.
- Offener Restdruck bleibt mindestens in drei lesbaren Klassen sichtbar: Innen-/Wartungsdruck in `D5/C6`, Reichweiten-/Kontaktbedarf ueber `G7` sowie begrenzter Randdruck ueber `E2/F1`.
- Der Wiedereinstieg muss fuer jeden Slot weiter zeigen koennen, welche Arbeiten `begonnen`, `unterbrochen` oder `offen` in denselben Folgeblock getragen werden.

Slotfolge
---------

### Slot 36 - Folgeanker aus slot 35 in eine knappe Arbeitsliste uebersetzen

- Primaerlinse: `pc_visible` mit Resume- und Restdrucksicht.
- Startanker: derselbe konsolidierte Folgeanker aus `slot 35`.
- Kernentscheidungen:
  1) den staerksten offenen Restdruck zuerst stabilisieren,
  2) Innen- und Aussenarbeit klar voneinander trennen,
  3) nur einen Randpfad gleichzeitig wieder oeffnen,
  4) den Folgeblock bewusst auf wenige lesbare Anschluesse begrenzen.
- Konsequenzklassen: Restdruckklarheit, Starttempo, begrenzte Flexibilitaet, stabiler Wiedereinstieg.
- Fail-forward: Ein holpriger Wiederanlauf kostet Tempo oder Reichweite, aber nicht den Kampagnenast.

### Slot 37 - D5 und C6 als belastbares Rueckgrat unter Folgekosten halten

- Primaerlinse: `pc_visible` mit `allies_only`-Rueckkopplung im Innenpfad.
- Startanker: gekoppelte Werkstatt-, Sicherungs- und Nordlinienarbeit zwischen `D5` und `C6`.
- Kernentscheidungen:
  1) `D5` als Planungs- und Reparaturkern priorisieren,
  2) `C6` nur so weit mitziehen, wie der laufende Fokus es traegt,
  3) Innenstabilitaet gegen spaeteren Kontaktbedarf abwaegen,
  4) laufende Arbeiten nicht in freie Parallelaufgaben zerfasern lassen.
- Konsequenzklassen: Wartungskosten, Sicherheitsdruck, Innenklarheit, spaeterer Anschlussbedarf.
- Fail-forward: Zu breite Innenarbeit kostet Ressourcen oder Zeit, zerlegt den Slice aber nicht.

### Slot 38 - G7 als begrenzten Kontakt-, Tausch- oder Entlastungshebel lesen

- Primaerlinse: `pc_visible` mit schmalem `allies_only`-Wissen im Kontaktpfad.
- Startanker: `G7` als belegter externer Rueckzugs- und Kontaktkorridor.
- Kernentscheidungen:
  1) `G7` aktiv als Entlastung oder Reichweitenpflege nutzen,
  2) nur einen schmalen Kontaktkanal offenhalten,
  3) Kontakt zugunsten des Innenpfads wieder verengen,
  4) Kontaktarbeit nur als Folgehebel fuer den naechsten Block lesen.
- Konsequenzklassen: Reichweitengewinn, Konditionsdruck, Reservewert, spaetere Anschlussqualitaet.
- Fail-forward: Ein knapper oder spaeter Kontakt reduziert Spielraum, aber loest keinen freien Produktzweig aus.

### Slot 39 - E2 und F1 als begrenzte Randpuffer unter Druck halten

- Primaerlinse: `pc_visible` mit `world_only`-Druck an den Randraeumen.
- Startanker: `E2/F1` als duenne Rand- und Pufferraeume ohne freie Tiefennetzlogik.
- Kernentscheidungen:
  1) nur einen Randraum aktiv anfassen,
  2) Reichweite bewusst klein und lesbar halten,
  3) Randdruck zugunsten der stabileren Korridore wieder schliessen,
  4) Erkenntnisgewinn nicht mit freier Expansion verwechseln.
- Konsequenzklassen: Routenfragilitaet, Informationsgewinn, Erschoepfung, klare Begrenzung.
- Fail-forward: Zu viel Ehrgeiz fuehrt zu Zusatzkosten, Rueckschritt oder engerem Fokus, nicht zu neuen freien Raeumen.

### Slot 40 - Adapterfaehigen Folgeanker fuer den naechsten Block festschreiben

- Primaerlinse: `pc_visible` mit Produkt-, Resume- und Hand-off-Sicht.
- Startanker: konsolidierter Folgeblock aus `slot 36-39`.
- Kernentscheidungen:
  1) den Innenpfad als stabiles Rueckgrat lesbar abschliessen,
  2) den Kontaktpfad als begrenzten Folgehebel markieren,
  3) den Randpfad bewusst schmal und kontrollierbar halten,
  4) den naechsten Block so benennen, dass RP-Adapter, Product Gate und Sim denselben Anschluss lesen koennen.
- Konsequenzklassen: Wiederanlaufbarkeit, Fokusklarheit, adapterfaehiger Restdruck, sauberer Hand-off.
- Fail-forward: Auch ein rauer Abschluss bleibt ein belastbarer Folgeanker statt eines freien Abrisses.

Konsequenzklassen
-----------------

- Carry-Over-Kosten: Offene Arbeiten muessen lesbar priorisiert und begrenzt weitergetragen werden.
- Innenkosten: `D5/C6` sichern Stabilitaet gegen Wartungs- und Sicherheitsdruck.
- Kontaktkosten: `G7` vergroessert Reichweite gegen Konditions- und Fokusverlust.
- Randkosten: `E2/F1` bleiben nutzbar, aber nie frei skalierbar oder tief vernetzt.
- Adapterkosten: Ein sauberer Anschluss hinter `slot 40` verlangt Resume-Klarheit statt maximaler Expansion.

Guardrails
----------

- Keine direkte freie Verbindung `C6 -> F1` oder neue Tiefennetzpfade behaupten.
- Keine neuen Stationen, Crews, Besitzansprueche oder Infrastrukturretcons aus dem Folgekorridor ableiten.
- Keine neue Tick-, Save-, Replay- oder Resume-Logik neben dem bestehenden Sessionvertrag einbauen.
- Keine freie Neutral- oder Fraktionserweiterung hinter `E2/F1` erfinden.

Weiterer Ausbau
---------------

- Der weitere Ausbau hinter `slot 40` soll entweder `slot 41-45` als naechste SSOT fuehren oder einen explizit benannten adapterfaehigen Folgeblock unter demselben Vertragsrahmen ausweisen.