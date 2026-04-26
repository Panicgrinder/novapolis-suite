---
stand: 2026-04-27 01:53
update: Arkologie-A1 fuehrt jetzt ihren Nahraum T0 mit Kerngebiet, erstem und zweitem Ring, verdeckten Raumtypen und Gefahrenherden konservativ aus.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_015145.md
slug: arkologie-a1-nahraum-t0
category: canon
version: "0.1"
---

Arkologie A1 - Nahraum T0
=========================

Zweck
-----

- Dieser SSOT zieht den unmittelbaren Arkologie-Nahraum konservativ bis zwei Stationsschritte um den Kern `A1/A3/A5` nach.
- Er dient als Arbeitsanker fuer Lage, Puffer, Gefahrenherde und verdeckte Raumtypen, ohne aus der Metrokarte freie Detailgeographie zu erfinden.

Scope
-----

- Kerngebiet: [A1](../03-locations/A1.md), [A3](../03-locations/A3.md), [A5](../03-locations/A5.md)
- Erster Ring: [A2](../../../03-locations/A2.md), [A4](../../../03-locations/A4.md), [B5](../../../03-locations/B5.md)
- Zweiter Ring: [B1](../../../03-locations/B1.md), [A6](../../../03-locations/A6.md), [C5](../../../03-locations/C5.md)
- Naechster belegter Fremdfraktionskontakt im Nahraum: [B2](../../schienenbund/03-locations/B2.md) hinter `A1 -> A2 -> B1`

Raumringe (operativ)
--------------------

| Ring | Bereich | Lesart |
| --- | --- | --- |
| 0 | `A1/A3/A5` | kontrollierter Arkologie-Kern aus Fuehrung, Validierung und Versorgungsvorbereitung |
| 1 | `A2/A4/B5` | neutrale oder teilaktive Puffer, die Sichtung, Umlenkung und Abbremsung von Bewegung leisten |
| 2 | `B1/A6/C5` | Vorfeld zur naechsten Fremdfraktion, restriktive Randkante und neutraler Weiterlauf in die breitere Metro |

Ausbau- und Zustandsstatus
--------------------------

| Station | Kontrolle | Status | Zustandslesart | Funktionswert im Nahraum |
| --- | --- | --- | --- | --- |
| [A1](../03-locations/A1.md) | Arkologie-A1 | aktiv | Kernknoten, stabiler als Randraeume | Leitung, Forschung, Screening, Freigabe |
| [A3](../03-locations/A3.md) | Arkologie-A1 | teilaktiv | verschlankter, kontrollierter Puffer | Validierung, Quarantaene, Sicherung |
| [A5](../03-locations/A5.md) | Arkologie-A1 | aktiv | innerer Versorgungsarm | Aufbereitung, Versorgung, Austauschvorbereitung |
| [A2](../../../03-locations/A2.md) | neutral | aktiv | offenerer Transit- und Kontaktpuffer | Vorzone zwischen Arkologie und neutralem Weiterlauf |
| [A4](../../../03-locations/A4.md) | neutral | teilaktiv | ermuedeter Zwischenraum | Puffer Richtung restriktiver Peripherie |
| [B5](../../../03-locations/B5.md) | neutral | teilaktiv | fragiler Umschlag- und Umlenkraum | Puffer zwischen Arkologie-Rueckseite und Metroweiterlauf |
| [B1](../../../03-locations/B1.md) | neutral | aktiv | funktionaler Vorpuffer | letzter neutrale Filter vor dem Schienenbund |
| [A6](../../../03-locations/A6.md) | neutral | restricted | kritischer Randraum | Gefahrenkante, kein regulaerer Arkologie-Puffer |
| [C5](../../../03-locations/C5.md) | neutral | aktiv | breiterer Transitknoten | neutraler Weiterlauf aus dem A5/B5-Korridor |

Korridore
---------

### A1-Front: Kontakt und Filter

- Pfad: `A1 -> A2 -> B1 -> B2`
- Lesart: Arkologie oeffnet sich nach aussen nicht direkt in eine Fremdfraktion, sondern ueber zwei Filterstufen.
- `A2` bleibt Vorzone fuer Sichtung und erste Kontaktaufnahme.
- `B1` ist der letzte neutrale Vorpuffer, bevor hinter `B2` der Schienenbund beginnt.

### A3-Front: Abschirmung und Restriktion

- Pfad: `A3 -> A4 -> A6`
- Lesart: Dieser Arm fuehrt nicht in offenen Transit, sondern in einen zunehmend kritischen Randraum.
- `A4` bleibt nutzbar als Zwischenhalte- und Sichtungsraum.
- `A6` markiert die restriktive Kante; dort kippt der Nahraum von kontrollierter Pufferung in Blockade- und Gefahrenlogik.

### A5-Front: Versorgung und Rueckseite

- Pfad: `A5 -> B5 -> C5`
- Lesart: Dieser Arm ist die ruhigere Rueckseite des Arkologie-Kerns und eignet sich eher fuer Versorgungsvorbereitung, Umlenkung und verdeckte Bewegungsruhe als fuer sichtbare Diplomatie.
- `B5` puffert und bremst.
- `C5` oeffnet wieder in den neutralen Metrofluss, ohne schon selbst ein Fraktionsraum zu sein.

Verdeckte Orte (konservativ, noch nicht genau)
----------------------------------------------

Hinweise

- Die folgenden Raumtypen sind keine exakt bezeugten Einzelraeume, sondern konservative Lesarten aus Status, Pufferfunktion und Tunnellogik.
- Sie duerfen als verdeckte Orte mitgelesen werden, solange keine konkretere Szenen- oder Missionsbelegung vorliegt.

| Bereich | Wahrscheinlicher Raumtyp | Lesart | Guardrail |
| --- | --- | --- | --- |
| `A1 <-> A2` | Screeningnischen, Sichtungsraeume, kurze Haltezonen | kontrollierte Vorpruefung vor Aussenkontakt | keine exakten Tuer-, Deck- oder Personallisten behaupten |
| `A3 <-> A4` | Quarantaene-Nebenraeume, blinde Wartungsbuchten, Rueckzugsnischen | Abschirmung, Pruefung, Verzahnung von Kontrolle und Engstelle | keine konkreten Labor- oder Haftkomplexe behaupten |
| `A4 <-> A6` | versiegelte Seitengaenge, blockierte Schachtkoepfe, tote Servicestreifen | Randzone, in der Wege abbrechen oder gesperrt werden | keine konkrete Kontamination oder Kreatur frei erfinden |
| `A5 <-> B5` | Packnischen, stille Pufferflaechen, temporare Bereitstellungszonen | Rueckseitenlogik fuer Versorgung und enge Freigabefenster | keine frei inventarisierten Lagerkammern behaupten |
| `B5 <-> C5` | Umschlagecken, alte Servicekammern, verdeckte Wartebuchten | neutraler Weiterlauf mit Raum fuer Stau und Umlenkung | keine feste Schmuggler- oder Marktinfrastruktur behaupten |
| `A2 <-> B1` | Zwischenkontrollpunkte, Sichtliniennischen, kurzzeitige Sperrraeume | letzter neutraler Filter vor dem Schienenbund-Korridor | keine diplomatischen Kontaktzonen als belegt setzen |

Gefahrenherde (konservativ, noch nicht genau)
---------------------------------------------

| Herd | Bereich | Lesart | Schwere |
| --- | --- | --- | --- |
| Screeningstau | `A1/A2` | Sicherheits- und Biosicherheitsdruck kann jeden offenen Kontakt sofort abbremsen | mittel |
| Pufferermuedung | `A3/A4` | teilaktive Trakte, schlechtere Uebersicht und geringe Bewegungsreserve machen den Arm fragil | mittel |
| Restriktive Kante | `A4/A6` | Blockade- oder Kontaminationslogik ist hier naheliegender als regulaerer Transit | hoch |
| Rueckseitenstau | `A5/B5` | Versorgung und Freigabe konkurrieren um denselben schmalen Korridor | mittel |
| Neutraler Durchsatzdruck | `B5/C5` | neutraler Transit kann sich stauen oder unklar werden, ohne dass Arkologie dort echte Kontrolle hat | mittel |
| Fremdfraktionsnahe Trassenkontrolle | `B1 -> B2` | hinter dem neutralen Vorpuffer kippt der Raum in Schienenbund-nahe Reglementierung | mittel bis hoch |

Naechster Fremdfraktionskontakt
------------------------------

- Der naechste belastbare Fremdfraktionskontakt des Arkologie-Nahraums liegt nicht direkt an `A1`, sondern hinter der Neutralfolge `A2 -> B1` in [B2](../../schienenbund/03-locations/B2.md).
- Fuer T0 bedeutet das: Arkologie hat im Nahraum zuerst Filter- und Pufferstationen, bevor der Schienenbund als klarer Fremdraum beginnt.
- Diese Trennung passt zur globalen Regel der neutralen Zwischenstation und schuetzt die Arkologie vor einer zu direkten Frontlesart.

Guardrails
----------

- Keine exakten Unterraeume, Decknummern oder Hazard-Typen ohne Missions- oder Szenenbeleg.
- Verdeckte Orte bleiben Raumtypen, keine bereits geoeffneten Kanon-Orte.
- Gefahrenherde bleiben Lagebilder; erst bei neuem Beleg werden sie in konkrete Ereignisse oder Entitaeten zerlegt.
- Der Nahraum-SSOT ersetzt keine Einzel-Ortsdatei, sondern ordnet sie.
