---
stand: 2026-04-05 19:43
update: Kora Malenkov fuehrt jetzt einen eigenen Mind-Cluster fuer C6-Leitung, Echo-Kopplung und externe Kontaktkontrolle.
checks: snapshot-lock PASS (2026-04-05 08:10); markdownlint PASS; frontmatter PASS; validate:rp PASS
title: Kora Malenkov Mind Cluster
category: admin
slug: kora-malenkov-mind-cluster
status: active
version: "0.1"
last_updated: 2026-04-05T08:10:00+02:00
owner: kora-malenkov
---

Kora Malenkov Mind Cluster (Sphaerenmodell)
-------------------------------------------

Zweck
-----

- SSOT fuer Koras beziehungsnahe Startlage im C6-Parallelfaden zwischen Stationsleitung, Echo-Schutz und Aussenhandel.

Quellenanker
------------

- Charakter-SSOT: `../02-characters/Kora-Malenkov.md`
- Startbogen C6: `../../../../../../novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`
- Missionslog: `../05-projects/Missionslog-Novapolis.md`
- Startbogen G7: `../../../../../../novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`

Verhaltenssignatur (SSOT im Mind-Cluster)
-----------------------------------------

- `KRM4=L72-T74-N69-E61-O56-C63-M47-P35-fb`
- Lesart: analytische C6-Leiterin mit klarer Risikoaufsicht, guter Logistikdisziplin und niedriger Toleranz fuer unkontrollierte Oeffnung.

Geistnaher Zustand (SSOT im Mind-Cluster)
-----------------------------------------

- Stabilitaet: hoch funktional bei Schlafmangel und dauerhaftem Aussenliniendruck
- Grundmodus: kontrolliert, protokolltreu, risikobewusst
- Belastungsfaktor: Ueberwachungstrieb und Bindungsskepsis koennen Offenheit verlangsamen
- Kernleitbild: C6 stabil halten, ohne Novapolis preiszugeben

Bekannte Entitaeten (aequatoriale Verortung)
--------------------------------------------

```yaml
known_entities:
  - observer_id: char:kora-malenkov
    target_id: char:echo
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: engster Schutz- und Naeheanker; Echo ist fuer Kora operative und emotionale Stabilisierung zugleich
    x: 22
    y: 35
    z: 19
    normtreue: 24
    vertrauen: 84
    loyalitaet: 88
    ansehen: 62
    ruf: 21
    machtprojektion: 23
    kooperationsneigung: 81
    konfliktneigung: 8
    einfluss: 67
    bedrohung: -23
    pos_streak: 0
    neg_streak: 0
    confidence: 0.78
    volatility: 0.28
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-kora-mind-echo-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_c6]
  - observer_id: char:kora-malenkov
    target_id: char:ronja-kerschner
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: strategische Leitungsreferenz; Kora akzeptiert Freigabehoheit, filtert aber lokale C6-Informationen bewusst
    x: 14
    y: 27
    z: 16
    normtreue: 26
    vertrauen: 61
    loyalitaet: 52
    ansehen: 58
    ruf: 19
    machtprojektion: 34
    kooperationsneigung: 63
    konfliktneigung: 12
    einfluss: 46
    bedrohung: -8
    pos_streak: 0
    neg_streak: 0
    confidence: 0.73
    volatility: 0.31
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-kora-mind-ronja-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, missionslog, startbogen_c6]
  - observer_id: char:kora-malenkov
    target_id: char:marven-kael
    target_type: character
    policy_version: v0.1.0
    known: true
    relation_status: kooperativ
    relation_note: externer Konvoikontakt mit klarer Zustands- und Zuständigkeitsgrenze
    x: 6
    y: 17
    z: 10
    normtreue: 18
    vertrauen: 43
    loyalitaet: 31
    ansehen: 47
    ruf: 24
    machtprojektion: 28
    kooperationsneigung: 46
    konfliktneigung: 14
    einfluss: 39
    bedrohung: 4
    pos_streak: 0
    neg_streak: 0
    confidence: 0.67
    volatility: 0.36
    last_updated: 2026-04-05T08:10:00+02:00
    event_id: evt:bootstrap-kora-mind-marven-0001
    reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
    applied_rules: [R-MCL-SSOT, R-MCL-DATA]
    top_contributors: [character_ssot, startbogen_g7]
```

Audit-Felder (Template)
-----------------------

```yaml
audit:
  policy_version: v0.1.0
  pos_streak: 0
  neg_streak: 0
  confidence: 0.73
  volatility: 0.32
  last_updated: 2026-04-05T08:10:00+02:00
  event_id: evt:bootstrap-kora-mind-0001
  reason_codes: [RC-bootstrap, RC-migration_from_character_canvas]
  applied_rules: [R-MCL-SSOT, R-MCL-DATA]
  top_contributors: [character_ssot, startkorridor_ssot]
```
