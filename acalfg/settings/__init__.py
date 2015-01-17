"""
Settings used by acalfg project.

This consists of the general production settings, with an optional import of any local
settings.
"""

# Import production settings.
from acalfg.settings.production import *

# Import optional local settings.
try:
    from acalfg.settings.local import *
except ImportError:
    pass
