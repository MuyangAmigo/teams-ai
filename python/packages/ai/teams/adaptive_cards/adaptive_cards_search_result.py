"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AdaptiveCardsSearchResult:
    title: str
    value: str
