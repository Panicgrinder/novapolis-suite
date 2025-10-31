# Shared packages

Put reusable Python code here. Everything under this directory is treated as part of the `novapolis-suite` editable install via `pyproject.toml`. Subfolders should expose proper packages (with `__init__.py`) so that callers from `novapolis_agent` or `novapolis-rp` can import them once the duplicates have been migrated.
