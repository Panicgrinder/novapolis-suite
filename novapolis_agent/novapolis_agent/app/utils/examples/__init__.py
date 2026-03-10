"""Kompatibilitaetsschicht fuer `novapolis_agent.app.utils.examples`.

Delegiert auf den kanonischen Top-Level-Shim unter `app.utils.examples`,
damit Archiv-/Fehlerlogik nur an einer Stelle gepflegt wird.
"""

from app.utils.examples import *  # noqa: F403
