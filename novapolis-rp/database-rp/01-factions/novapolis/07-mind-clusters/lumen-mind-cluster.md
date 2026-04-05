---
stand: 2026-04-05 19:43
update: Lumen fuehrt jetzt einen eigenen Mind-Cluster fuer Jonas-Kopplung, Instanzsupport und Werkstattnaehe.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Lumen Mind Cluster
category: admin
slug: lumen-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T10:32:00+02:00
owner: lumen
---

Lumen Mind Cluster (Sphaerenmodell)
-----------------------------------

Zweck
-----

- SSOT fuer Lumens beziehungsnahe Lage im Jonas-nahen Werkstatt- und Instanzverbund.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Lumen.md`
- Charakter-SSOT Jonas: `../02-characters/Jonas-Merek.md`
- Charakter-SSOT Reflex: `../02-characters/Reflex.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `LMN1=L78-T71-E60-O49-N44-S52-C26-M18-P28-ks`
- Lesart: kindlich-selbstlose Supportinstanz mit starker Naehebindung an Jonas und enger Assistenzlogik.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: hoch bei Werkstattnaehe zu Jonas, fragil bei Distanz und Unterbrechung
- Grundmodus: assistierend, nahesuchend, fokussiert auf Schutz im Kleinen
- Kernleitbild: Jonas stabil halten und Werkstattsupport leisten, ohne die Kopplung zu verlieren

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:lumen
    target_id: char:jonas-merek
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: primäre Bezugsperson; Lumen stabilisiert sich ueber Jonas-Naehe und Assistenz
    x: 23
    y: 37
    z: 22
    normtreue: 20
    vertrauen: 91
    loyalitaet: 93
    ansehen: 54
    ruf: 11
    machtprojektion: 15
    kooperationsneigung: 89
    konfliktneigung: 4
    einfluss: 58
    bedrohung: -26
    pos_streak: 0
    neg_streak: 0
    confidence: 0.80
    volatility: 0.28
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-lumen-mind-jonas-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
  - observer_id: char:lumen
    target_id: char:reflex
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: Primärinstanz und Referenz fuer Schutz- und Netzlogik
    x: 17
    y: 26
    z: 16
    normtreue: 18
    vertrauen: 73
    loyalitaet: 68
    ansehen: 49
    ruf: 9
    machtprojektion: 19
    kooperationsneigung: 76
    konfliktneigung: 5
    einfluss: 41
    bedrohung: -12
    pos_streak: 0
    neg_streak: 0
    confidence: 0.75
    volatility: 0.29
    last_updated: 2026-04-05T10:32:00+02:00
    event_id: evt:bootstrap-lumen-mind-reflex-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot]
```

Audit-Felder (Template)
-----------------------

```yaml
audit:
  policy_version: v0.1.0
  pos_streak: 0
  neg_streak: 0
  confidence: 0.77
  volatility: 0.29
  last_updated: 2026-04-05T10:32:00+02:00
  event_id: evt:bootstrap-lumen-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot]
```