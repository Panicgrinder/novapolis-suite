"""Top-level `app` package shim.

This package makes `import app.*` work when tests are executed from the
repository root by pointing the package path at `novapolis_agent/app`.

Do not add runtime-only logic here; this shim is for test/compatibility only.
"""
from pathlib import Path

# Resolve novapolis_agent/app relative to repository root (one level up)
_repo_root = Path(__file__).resolve().parents[1]
_shim_path = str(_repo_root.joinpath("novapolis_agent", "app"))
# Prepend to package __path__ so submodule imports like `app.api` resolve
if _shim_path not in __path__:
	__path__.insert(0, _shim_path)
