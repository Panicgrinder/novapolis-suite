"""Compatibility wrapper package.

This package exists to make `import scripts.agent.<name>` work even when the
current working directory (and thus import precedence) causes `scripts` to
resolve to `novapolis_agent/scripts`.

The canonical wrappers live at repo root: `scripts/agent/`.
"""
