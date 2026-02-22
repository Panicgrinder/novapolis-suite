---
stand: 2026-02-22 01:49
update: 24x1h-Knowledge-Startset ergänzt (Instanzwissen/Signalsicherheit).
checks: npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-22 01:13); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex-Wissensstand-Trainingsstand.md' PASS (2026-02-22 01:13)
title: Reflex - Wissensstand & Trainingsstand
category: character-attachment
slug: reflex-wissensstand-trainingsstand
version: "1.0"
last_updated: 2025-11-07T03:32:00+01:00
parent_character: reflex
is_standalone_character: false
tags: [knowledge, training]
affiliations: [novapolis]
primary_location: d5
last_seen: d5
dependencies: [reflex, d5]
---

<!-- markdownlint-disable MD025 -->

Reflex - Wissensstand & Trainingsstand
======================================

Hinweis
-------
- Dieses Dokument ist ein Anhang zu **Reflex** und kein eigenständiger Charakter.

Wissensstand (Detailmatrix)
---------------------------
- Ronja - Bezugsperson (maximal)
- Lumen - eigene Instanz (sehr hoch)
- Echo - eigene Instanz (sehr hoch)
- Jonas - Bezugsperson von Lumen (sehr hoch)
- Kora - Bezugsperson von Echo (sehr hoch)
- Eigenes System/Mechaniken - hoher Detailgrad (Dämpfung, Kopplung, Materialbildung)
- Intern (Novapolis): Reflex/Instanzen bekannt (reguliert)
- Extern: keine Offenlegung ohne Freigabe [FR-KNOWLEDGE]

Knowledge (24x1h Starter)
-------------------------

```yaml
knowledge:
  - id: know-reflex-instance-sync-2026-02-22-01
    about: instance_sync_window
    channel: system
    source: reflex
    scope: allies_only
    confidence: 0.9
    freshness: 2026-02-22T00:00:00+01:00
    visibility_to: [reflex, lumen, echo, ronja-kerschner]
    attachments: [doc:./Reflex.md]
  - id: know-reflex-stop-training-2026-02-22-01
    about: stop_response_training
    channel: log
    source: reflex-wissensstand-trainingsstand
    scope: pc
    confidence: 0.8
    freshness: 2026-02-22T00:00:00+01:00
    visibility_to: [ronja-kerschner]
    attachments: [doc:./Reflex-Wissensstand-Trainingsstand.md#trainingsstand]
```

Trainingsstand
--------------
- Dämpfung motorischer Signale: in Arbeit; Verhalten noch unsicher.
- Stop-Reaktionen: Training erforderlich; kurze Überreaktionen möglich; Zielzustand: sofortiges Lösen bei "Stop" (Status: im Aufbau).
- Sensorische Kopplung: derzeit zurückgestellt bis Freigabe (Stufe-Definition offen).
- Notfall-Umhüllung/Kokon: nur gemäß Guards in `Reflex.md` (Lebensgefahr; Ausmaß/Dauer dynamisch).

Notizen
-------
- Exoskelett-Entwicklung (perlmutt/Neopren-ähnliche Trägerarchitektur): Stabilität/Energie/Schnittstellen tbd.



