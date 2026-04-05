---
stand: 2026-04-05 19:43
update: Jonas Merek fuehrt jetzt einen eigenen Mind-Cluster fuer Werkstatt-, Freigabe- und Schutzbeziehungen des Startkorridors.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Jonas Merek Mind Cluster
category: admin
slug: jonas-merek-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T08:10:00+02:00
owner: jonas-merek
---

Jonas Merek Mind Cluster (Sphaerenmodell)
-----------------------------------------

Zweck
-----

- SSOT fuer die beziehungsnahe Startlage von Jonas Merek zwischen Werkstatt, Freigabe und Schutznetz.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Jonas-Merek.md`
- Startbogen D5: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`
- Missionslog: `../05-projects/Missionslog-Novapolis.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `JNS3=L55-T68-N40-E72-O50-C42-M78-P32-ab`
- Lesart: technisch verlaesslich, hilfsbereit und improvisationsstark, aber bei Ueberlast klar stressanfällig.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: arbeitsfaehig mit klaren Triggern bei Enge, Gasgeruch und Kontrollverlust
- Grundmodus: vorsichtig kooperativ, beweisorientiert
- Belastungsfaktor: Schuld und Schlafmangel koennen Aufmerksamkeit und Konfliktvermeidung verzerren
- Kernleitbild: Werkstatt und Crew nicht im Stich lassen

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:jonas-merek
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Mentorin, Rettungs- und Freigabeanker fuer Werkstatt und Logistik
    x: 16
    y: 28
    z: 20
    normtreue: 24
    vertrauen: 69
    loyalitaet: 58
    ansehen: 63
    ruf: 19
    machtprojektion: 18
    kooperationsneigung: 72
    konfliktneigung: 7
    einfluss: 43
    bedrohung: -16
    pos_streak: 0
    neg_streak: 0
    confidence: 0.74
    volatility: 0.34
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-jonas-mind-ronja-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, missionslog]
  - observer_id: char:jonas-merek
    target_id: char:pahl-brenner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: fachlicher Mentor mit realem Nutzwert, aber hoher Kontrolldruck und Hierarchiereibung
    x: -3
    y: 14
    z: 9
    normtreue: 18
    vertrauen: 34
    loyalitaet: 29
    ansehen: 52
    ruf: 14
    machtprojektion: 24
    kooperationsneigung: 39
    konfliktneigung: 26
    einfluss: 31
    bedrohung: 6
    pos_streak: 0
    neg_streak: 0
    confidence: 0.68
    volatility: 0.38
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-jonas-mind-pahl-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_d5]
  - observer_id: char:jonas-merek
    target_id: char:reflex
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Respekt fuer Schutz- und Diagnoseleistung; vorsichtige Faszination mit klaren Grenzen
    x: 11
    y: 19
    z: 12
    normtreue: 15
    vertrauen: 48
    loyalitaet: 36
    ansehen: 46
    ruf: 13
    machtprojektion: 22
    kooperationsneigung: 52
    konfliktneigung: 11
    einfluss: 28
    bedrohung: -4
    pos_streak: 0
    neg_streak: 0
    confidence: 0.7
    volatility: 0.33
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-jonas-mind-reflex-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_d5]
```

Audit-Felder (Template)
-----------------------

```yaml
audit:
  policy_version: v0.1.0
  pos_streak: 0
  neg_streak: 0
  confidence: 0.71
  volatility: 0.35
  last_updated: 2026-04-05T08:10:00+02:00
  event_id: evt:bootstrap-jonas-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startkorridor_ssot]
```
