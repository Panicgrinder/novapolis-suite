# Compatibility shim für alte Import-Pfade:
# from agents.cvn_agent import ...  -> verweist nun auf novapolis_agent.app
from novapolis_agent.app import *  # noqa
