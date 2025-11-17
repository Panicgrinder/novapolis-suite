---
stand: 2025-11-16 06:52
update: YAML-Frontmatter ergänzt; H1/H2 auf Setext umgestellt.
checks: keine
---

Charakter-Block Nord - Quellenstand (2025-11-01)
================================================

Varek Solun
-----------

- **RAW** `RAW-canvas-2025-10-16T03-25-00-000Z.txt` (`char_varek_solun_v1`)
  - Kommandant/Führer der Eisenkonklave, Standort `H12`, Alias "Sektor_H3".
  - Ziele: Auffinden Union-Hauptarchiv; kontrollierte Informationsweitergabe.
  - Beziehungen: Eisenkonklave (loyal), Novapolis (neutral_wachsam), Händlergilde (wechselhaft), Schattenbund (feindselig).
  - Skill-Set: Taktik, Aufklärung, verdeckte Operationen; Kontrolle/Disziplin im Fokus.
- **Flag** `RAW-canvas-2025-10-16T03-25-00-000Z.flags.txt`
  - Hinweise: Außenwissen über Novapolis/D5 entfernen ([FR-KNOWLEDGE]); Standortcodierung `H12` harmonisieren, `Sektor_H3` als Redirect.
- **Curated**
  - `database-rp/02-characters/Varek-Solun.{md,json}` (Stand 2025-11-01T15:45+01:00) - Standortcode harmonisiert (H12, Alias "Sektor_H3"), Novapolis-Wissen auf Gerüchte eingeschränkt, Stellvertretung Lyra Hest verlinkt.
- **resolved.md Bezug**
  - `[FACT][EK-LEADERSHIP]`, `[FACT][EK-TAXONOMY]` - bestätigt Führung (Varek/Lyra) und Standortcode `H12` mit Alias.

Liora Navesh
------------

- **RAW** `RAW-canvas-2025-10-16T03-25-10-000Z.txt` (`char_liora_navesh_v1`)
  - Leiterin Forschungsrat/Chefärztin Biotechnologie Arkologie A1.
  - Kennt "SÜDFRAGMENT"/H-47 Signale, aber keine Daten zu Novapolis/D5.
  - Charakterisiert als utilitaristisch, analytisch, Sicherheitsprotokolle A9.
- **Flag** `RAW-canvas-2025-10-16T03-25-10-000Z.flags.txt`
  - Geheimhaltung gegenüber Novapolis betonen; Taxonomie `Arkologie A1` konsistent halten.
- **Curated**
  - `database-rp/02-characters/Liora-Navesh.{md,json}` (Stand 2025-11-01T16:20+01:00) - Novapolis-Wissen weiterhin unbekannt, Fokus auf SÜDFRAGMENT-Analyse und A9-Protokolle, Standortcodierung Arkologie A1 harmonisiert.
- **resolved.md Bezug**
  - `[FACT][ARKO-RESEARCH]`, `[FACT][ARKO-TAXONOMY]` - Rollenzuweisung und Namensschema bestätigt.

Kora Malenkov
-------------

- **RAW** `RAW-canvas-2025-10-16T14-56-00-000Z.txt` (`char_kora_malenkov_v2`)
  - Rolle: Karawanenführerin/Logistikkoordinatorin, aktuell in C6; betont paranoide Vorsicht.
  - Beziehungen: Ronja neutral, Reflex skeptisch neugierig, loyale Bindung an Händlergilde.
- **Flag** (selber Raw, kein separates Flagfile)
  - Keine Flag-Datei vorhanden; Leadership-Overlap mit Marven/Arlen über `[CARAVAN-LEADERSHIP]` adressiert.
- **Curated**
  - `database-rp/02-characters/Kora-Malenkov.md` (Version 1.0 - 2025-11-02T14:20+01:00) - Werte/Skills übernommen, Logistik/Sicherheitsrollen präzisiert, Echo-Protokolle dokumentiert, Scope-Abgrenzung zu Marven/Arlen festgehalten.
- **resolved.md Bezug**
  - `[FACT][CARAVAN-LEADERSHIP]` - weist interne Logistik Kora zu, externen Konvoi Marven, Arlen als Händler/Vermittler.

Marven Kael
-----------

- **RAW** `RAW-canvas-2025-10-16T14-56-10-000Z.txt` (`char_marven_v2`)
  - Rolle: Karawanenführer/Handelskoordinator, Ort C6 (Karawanen-HQ).
  - Verhalten analytisch/vorsichtig; hohe Loyalität zur Crew, prüfende Haltung gegenüber Ronja/Novapolis.
- **Flag** `RAW-canvas-2025-10-16T14-56-10-000Z.flags.txt`
  - Führungstitel mit Kora abstimmen; klarer Scope (Konvoi/Handel extern).
- **Curated**
  - `database-rp/02-characters/Marven-Kael.md` (Version 1.0 - 2025-11-02T14:45+01:00) - Konvoi-/Handelsrolle geklärt, Sicherheits- und Verhandlungsprotokolle dokumentiert, FACT `[CARAVAN-LEADERSHIP]` umgesetzt.
- **resolved.md Bezug**
  - `[FACT][CARAVAN-LEADERSHIP]` - bestätigt Marven als externe Konvoi-/Handelsleitung.

Arlen Dross
-----------

- **RAW** `RAW-canvas-2025-10-16T14-56-20-000Z.txt` (`char_arlen_dross_v2`)
  - Rolle: Karawanenführer/Händler, Ort C6; diplomatisch, Vermittlerrolle.
  - Fokussiert auf Freiheit vs Verantwortung, beobachtet Reflex mit Unbehagen/Faszination.
- **Flag** `RAW-canvas-2025-10-16T14-56-20-000Z.flags.txt`
  - Titel mit Kora/Marven abgleichen; Rolle als Händler/Vermittler konkretisieren.
- **Curated**
  - `database-rp/02-characters/Arlen-Dross.{md,json}` (Version 1.0 - 2025-11-02T15:05+01:00) - Diplomatie-/Vermittlerrolle ausgearbeitet, Abgrenzung zu Kora/Marven umgesetzt, Reflex-Wissensgrenzen dokumentiert, FACT `[CARAVAN-LEADERSHIP]` verankert.
- **resolved.md Bezug**
  - `[FACT][CARAVAN-LEADERSHIP]` - Arlen als Händler/Vermittler ohne Führungsduplikat.

Pahl
----

- **RAW** `RAW-canvas-2025-10-16T14-41-00-000Z.txt` (`char_pahl_v2`)
  - Rolle: Ingenieur/Wartungsleiter (geschwächt), Ort D5 Technikbereich.
  - Gesundheitsstatus: chronische Atembeschwerden nach Gasexposition; Risiko für Kontrollverlust.
- **Flag** `RAW-canvas-2025-10-16T14-41-00-000Z.flags.txt`
  - Status unsicher; Daten vor Promotion validieren.
- **Curated**
  - `database-rp/02-characters/Pahl.{md,json}` (Version 1.0 - 2025-11-02T15:25+01:00) - Herkunft korrigiert (einziger Überlebender des C6-Reaktorunfalls, Bergung durch Ronja/Reflex, Transfer nach D5 durch Jonas - FACT `[PAHL-RESCUE]`), Gesundheitsstatus dokumentiert, Hausregeln/Wartungsscope präzisiert.
- **resolved.md Bezug**
  - Keine explizite Pahl-spezifische Entscheidung in `resolved.md`; Pahl wird in Ronja-Canvas und FACT `[POP]`/`[C6-HELPERS]` implizit erwähnt.

Ronja Kerschner
---------------

- **RAW** `RAW-canvas-2025-10-16T11-45-00-000Z.txt` (`char_ronja_v2` - `korrupt`)
  - Nennt Nachnamen „Vallin“; beschreibt aktuelle Rollen, Motivationen, Systemverknüpfungen.
  - Enthält Gesundheits-/Zustandsmetriken, Inventar, Signaturcode.
- **Flag** `RAW-canvas-2025-10-16T11-45-00-000Z.flags.txt`
  - Markiert als korrupt; Nachname, Beziehungen, Locations gegen Kanon prüfen.
- **Curated**
  - `database-rp/02-characters/Ronja-Kerschner.md` (Stand 2025-11-01T17:10+01:00) - Version 1.0, Status-/Systemabschnitte aus RAW übernommen, Drift „Vallin“ dokumentiert.
- **resolved.md Bezug**
  - `[NAME-RONJA]` - bestätigter Nachname „Kerschner“; `[FACT][REFLEX-*]`, `[FACT][ROLES]` liefern weitere Leitplanken.

Reflex (Primärinstanz)
----------------------

- **RAW** `RAW-canvas-2025-10-16T13-45-00-000Z.txt` (`char_reflex_v2`)
  - Beschreibt Reflex als organische KI-Symbiontstruktur; betont Loyalität zu Ronja, mögliche emotionale Dysregulation.
- **RAW (Entity)** `RAW-canvas-2025-10-16T03-25-20-000Z.txt` (`ent_d5_reflex_v1`)
  - Technische Beschreibung (Symbiose-Stufe I, Frequenzband 7.3-8.0 Hz, Entfernung >12h Stress, keine vollständige Trennung).
- **Flag** `RAW-canvas-2025-10-16T03-25-20-000Z.flags.txt`
  - Abgleich mit bestehenden Reflex-Regeln (Detachment, Speech, Proximity etc.) erforderlich; Terminologie harmonisieren.
- **Curated**
  - `database-rp/02-characters/Reflex.{md,json}` (Version 1.0 - 2025-11-02T16:05+01:00) - Symbiose-Stufe I vollständig dokumentiert (Frequenzband, Detachment-Regeln, Instanzleitung, Sicherheitsprotokolle, Signalsätze).
  - `database-rp/02-characters/Reflex-Wissensstand-Trainingsstand.md` - Detailmatrix für Wissen/Training, Stop- und Dämpfungsziele.
- **resolved.md Bezug**
  - Mehrere `[FACT?]`-Einträge aktuell in Review: `[REFLEX]`, `[INSTANCES]`, `[PROXIMITY]`, `[REFLEX-SPEECH]`, `[REFLEX-CONTROL]`, `[REFLEX-DETACH]`, `[JEALOUSY-GLOVES]`.

Jonas Merek
-----------

- **RAW** `RAW-canvas-2025-10-16T03-12-00-000Z.txt` (`char_jonas_v1`)
  - Frühfassung: Werkstatt unter D5, Schwester beim E2-Vorfall zurückgelassen, Wahl zwischen C6 und Werkstatt.
- **RAW** `RAW-canvas-2025-10-16T14-12-00-000Z.txt` (`char_jonas_v2` - `korrupt`)
  - Aktualisierte Version mit Verhaltenssignatur; Makel listet „Schuld am Tod der Schwester“.
- **Flag** `RAW-canvas-2025-10-16T14-12-00-000Z.flags.txt`
  - Markiert als korrupt; Schwesterstatus gegen Kanon normalisieren.
- **Curated**
  - `database-rp/02-characters/Jonas-Merek.md` (Version 1.0 - 2025-11-02T13:55+01:00) - Werte/Skills übernommen, Schuldflag als Kommentar (Schwester vermisst), Rollen Logistik/Werkstatt/Terminal, Sicherheitsprotokolle ergänzt.
- **resolved.md Bezug**
  - `[FACT][JONAS-SIS]` - Schwesterstatus bleibt „vermisst/unklar“, Schuldflag als non-canon deklarieren.

Drift-Dokumentation (Overrides)
-------------------------------

- `char_ronja_v2` (RAW, korrupt) → Nachname „Vallin“. **Override:** Kanon bleibt „Ronja Kerschner“ (`resolved.md #[NAME-RONJA]`). Notiz hier behalten, falls die Fehlbenennung in weiteren Rohquellen auftaucht.
- `char_jonas_v2` (RAW, korrupt) → Makel „Schuld am Tod der Schwester“ impliziert ihren Tod. **Override:** Kanonischer Status „Schwester vermisst/unklar“ (`resolved.md #[JONAS-SIS]`). Schuldflag nur als Kommentar kennzeichnen, nicht als Fakt übernehmen.

