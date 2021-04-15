"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730151647"


class Simpy:
    values: list[float]

    def __init__(self, list_values: list[float]) -> None:
        "Initializes a new object with the values attribute."
        self.values = list_values
    
    def __repr__(self) -> str:
        """Magic method to represent object as string."""
        return f"Simpy({self.values})"

    def fill(self, number: float, times: int) -> None:
        i: int = times
        while i > 0: 
            self.values.append(number)
            i -= 1
