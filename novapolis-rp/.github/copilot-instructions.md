# Copilot Working Rules (Novapolis)
SSOT: **/Main/novapolis-dev/**
- PLAN → DRY RUN → APPLY with hard STOP gates
- Minimal, transparent diffs; list touched files and a diffstat
- No shell commands, no history rewrites
- Working docs live in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index)
- `novapolis-rp/development/...` are redirect stubs. Do not write there.
- Before APPLY: scan for `development/docs` references (allowed only in the redirect README and in `meta.origin`)
- After APPLY: verify that all moved docs have sidecars with `source`, `origin`, `migrated_at`
