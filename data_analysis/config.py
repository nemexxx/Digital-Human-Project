"""Shared configuration for the data-analysis modules.

The raw export data is personal and is NOT included in this repository. Place
your own exported JSON files under a ``data/`` folder in the project root
(matching the structure documented in the README), or point ``DHP_DATA_DIR``
at wherever you keep them.
"""

import os

# Project root = one level up from this ``data_analysis`` package.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Override with the DHP_DATA_DIR environment variable if your data lives elsewhere.
DATA_DIR = os.environ.get("DHP_DATA_DIR", os.path.join(_PROJECT_ROOT, "data"))


def data_path(*parts):
    """Build an absolute path to a file inside the data directory."""
    return os.path.join(DATA_DIR, *parts)
