---
stand: 2026-04-05 19:43
update: Pahl Brenner fuehrt jetzt einen eigenen Mind-Cluster fuer D5-Freigaben, Technikautoritaet und Startkorridor-Reibung.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Pahl Brenner Mind Cluster
category: admin
slug: pahl-brenner-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T08:10:00+02:00
owner: pahl-brenner
---

Pahl Brenner Mind Cluster (Sphaerenmodell)
------------------------------------------

Zweck
-----

- SSOT fuer Pahls beziehungsnahe Startlage zwischen D5-Kontrolle, Ronjas Leitung und Jonas' Werkstattalltag.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Pahl-Brenner.md`
- Startbogen D5: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`
- Missionslog: `../05-projects/Missionslog-Novapolis.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `PHL2=L48-T60-N71-E50-O44-C62-M30-P25-bn`
- Lesart: berechnender Technik- und Sicherheitsanker mit deutlicher Ordnungsvorliebe und geringem Toleranzfenster fuer Kontrollverlust.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: funktional, aber koerperlich eingeschraenkt und daher kontrollorientiert kompensierend
- Grundmodus: pruefend, regelbezogen, skeptisch gegen unklare Eingriffe
- Belastungsfaktor: Atembeschwerden und Rekonvaleszenz erhoehen Sicherheitsbeduerfnis
- Kernleitbild: D5 nur unter nachvollziehbarer Aufsicht offen halten

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:pahl-brenner
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: anerkennt Leitung und Kompetenz, prueft aber jede Oeffnung auf System- und Sicherheitsfolgen
    x: 8
    y: 19
    z: 11
    normtreue: 26
    vertrauen: 51
    loyalitaet: 44
    ansehen: 67
    ruf: 22
    machtprojektion: 38
    kooperationsneigung: 46
    konfliktneigung: 18
    einfluss: 48
    bedrohung: -7
    pos_streak: 0
    neg_streak: 0
    confidence: 0.73
    volatility: 0.29
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-pahl-mind-ronja-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, missionslog]
  - observer_id: char:pahl-brenner
    target_id: char:jonas-merek
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: schuelerhafte Werkstattbeziehung; nuetzlich, aber aus Pahls Sicht eng zu beaufsichtigen
    x: 3
    y: 12
    z: 7
    normtreue: 21
    vertrauen: 39
    loyalitaet: 34
    ansehen: 43
    ruf: 11
    machtprojektion: 21
    kooperationsneigung: 42
    konfliktneigung: 16
    einfluss: 29
    bedrohung: -3
    pos_streak: 0
    neg_streak: 0
    confidence: 0.69
    volatility: 0.33
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-pahl-mind-jonas-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_d5]
  - observer_id: char:pahl-brenner
    target_id: char:reflex
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: akzeptierte Schutzinstanz, deren Eingriffslogik Pahl nur begrenzt berechenbar findet
    x: -10
    y: 9
    z: 4
    normtreue: 17
    vertrauen: 21
    loyalitaet: 15
    ansehen: 37
    ruf: 9
    machtprojektion: 34
    kooperationsneigung: 24
    konfliktneigung: 36
    einfluss: 35
    bedrohung: 19
    pos_streak: 0
    neg_streak: 0
    confidence: 0.67
    volatility: 0.37
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-pahl-mind-reflex-0001
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
  confidence: 0.7
  volatility: 0.33
  last_updated: 2026-04-05T08:10:00+02:00
  event_id: evt:bootstrap-pahl-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startkorridor_ssot]
```
