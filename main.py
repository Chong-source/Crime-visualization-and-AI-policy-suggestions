"""The main back-end decision tree of the project"""

from __future__ import annotations

import csv
from typing import Any, Optional

class Tree:
    """The tree class that is the backbone for the project"""
    _root: Optional[Any]
    _subtrees: list[Tree]

    is_empty
