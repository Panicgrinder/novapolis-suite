---
stand: 2026-03-11 04:45
update: Schlanken Changelog im Keep-a-Changelog-Stil eingefuehrt.
checks: pending (laufender Umbau)
---

Changelog
=========

Alle nennenswerten Aenderungen an diesem Repository werden hier dokumentiert.
Format orientiert sich an Keep a Changelog.

[Unreleased]
------------

### Added

- Standard-Governance-Dokumente eingefuehrt: `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `docs/adr/README.md`.

### Changed

- `README.md` und `novapolis-dev/README.md`: Archiv-Matrix und DONELOG-Ebenen klar definiert.
- `novapolis-dev/docs/todo.sim.md` und `novapolis-dev/docs/todo.index.md`: aktive Oberflaeche auf operative Kerndaten reduziert.
- `scripts/check_todo_index_sync.py`: Open-Count-Konsistenz und Widerspruchscheck erweitert.
- `.github/workflows/enforce-donelog.yml`: Agent-Codeaenderungen erfordern echte DONELOG-Dateiaenderung.
