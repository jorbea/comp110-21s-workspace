"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730151647"


class Simpy:
    """Class with a single attribute of a list of floats."""
    values: list[float]

    def __init__(self, list_values: list[float]) -> None:
        """Initializes a new object with the values attribute."""
        self.values = list_values
    
    def __repr__(self) -> str:
        """Magic method to represent object as string."""
        return f"Simpy({self.values})"

    def fill(self, number: float, times: int) -> None:
        """Fills an object with a specific value that repeats a specific number of times."""
        fill_list: list[float] = []
        i: int = times
        while i > 0:
            fill_list.append(number)
            i -= 1
        self.values = fill_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills an object's 'values' attribute with a range of values."""
        assert step != 0.0
        
        arange_list: list[float] = []
        i: float = start

        if step > 0.0:
            if i < stop:
                while i < stop:
                    arange_list.append(i)
                    i += step
            elif i > stop:
                while i > stop:
                    arange_list.append(i)
                    i -= step
            self.values = arange_list
        
        elif step < 0.0:
            if i < stop:
                while i < stop:
                    arange_list.append(i)
                    i -= step
            elif i > stop:
                while i > stop:
                    arange_list.append(i)
                    i += step
            self.values = arange_list

        
        
        
