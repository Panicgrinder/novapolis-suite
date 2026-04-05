---
stand: 2026-04-05 19:43
update: Reflex fuehrt jetzt einen eigenen Mind-Cluster fuer den Startkorridor statt verteilter Beziehungsnotizen in der Charakterdatei.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Reflex Mind Cluster
category: admin
slug: reflex-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T08:10:00+02:00
owner: reflex
---

Reflex Mind Cluster (Sphaerenmodell)
-----------------------------------

Zweck
-----

- SSOT fuer beziehungsnahe Zustandsdaten von Reflex im ersten Novapolis-Startkorridor.
- Trifft nur konservative Startaussagen aus Charakter-, Missions- und Start-SSOT.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Reflex.md`
- Startbogen D5: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`
- Startbogen C6: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`
- Missionslog: `../05-projects/Missionslog-Novapolis.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `RFX4=L80-S68-N77-T83-E64-O51-M25-C44-ka`
- Lesart: bindungsstarke Schutzinstanz mit hoher Sensorik, schneller Alarmreaktion und kontrollierter, aber realer Eingriffsneigung.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: funktional, aber stark an Naehe- und Schutzkontext gekoppelt
- Grundmodus: wachsam, suchend, beschuetzend
- Eskalationsmuster: priorisiert Schutz vor sozialer Bequemlichkeit
- Kernleitbild: Ronja sichern, Signale filtern, Instanznetz kohärent halten

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:reflex
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: absoluter Schutz- und Bindungsanker; hohe Naehe, hohe Eingriffsbereitschaft bei Gefahr
    x: 24
    y: 41
    z: 26
    normtreue: 28
    vertrauen: 92
    loyalitaet: 96
    ansehen: 74
    ruf: 38
    machtprojektion: 49
    kooperationsneigung: 88
    konfliktneigung: 22
    einfluss: 86
    bedrohung: -34
    pos_streak: 0
    neg_streak: 0
    confidence: 0.76
    volatility: 0.31
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-reflex-mind-ronja-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_d5, missionslog]
  - observer_id: char:reflex
    target_id: char:jonas-merek
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: technischer Verbuendeter; Reflex teilt Warn- und Diagnosekontext kontrolliert
    x: 14
    y: 24
    z: 15
    normtreue: 17
    vertrauen: 57
    loyalitaet: 42
    ansehen: 49
    ruf: 18
    machtprojektion: 19
    kooperationsneigung: 61
    konfliktneigung: 9
    einfluss: 34
    bedrohung: -9
    pos_streak: 0
    neg_streak: 0
    confidence: 0.69
    volatility: 0.35
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-reflex-mind-jonas-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, missionslog]
  - observer_id: char:reflex
    target_id: char:pahl-brenner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: angespannt
    relation_note: akzeptierte D5-Sicherheitsinstanz, aber mit Kontroll- und Eingriffsfriktion
    x: -8
    y: 13
    z: 6
    normtreue: 18
    vertrauen: 28
    loyalitaet: 19
    ansehen: 41
    ruf: 12
    machtprojektion: 27
    kooperationsneigung: 33
    konfliktneigung: 38
    einfluss: 32
    bedrohung: 14
    pos_streak: 0
    neg_streak: 0
    confidence: 0.67
    volatility: 0.39
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-reflex-mind-pahl-0001
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
  event_id: evt:bootstrap-reflex-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startkorridor_ssot]
```
