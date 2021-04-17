"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730151647"


class Simpy:
    """Utility class for common float column operations."""
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
        
    def sum(self) -> float:
        """Compute and return the sum of all items in the values attributes."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Combines each index of self with a float value or the respective index of rhs."""
        add_list: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                add_list.append(item + rhs)
        else:
            # isinstance(rhs, Simpy)
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                add_list.append(self.values[i] + rhs.values[i])
        return Simpy(add_list)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponentiates each index of self with a float value or the respective index of rhs."""
        pow_list: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                pow_list.append(item ** rhs)
        else:
            # isinstance(rhs, Simpy)
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                pow_list.append(self.values[i] ** rhs.values[i])
        return Simpy(pow_list)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Finds the remainder of each index of self with respect to a float value or Simpy object."""
        mod_list: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                mod_list.append(item % rhs)
        else:
            # isinstance(rhs, Simpy)
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                mod_list.append(self.values[i] % rhs.values[i])
        return Simpy(mod_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Generates a mask based on the equality of each index of self..."""
        """...and a float value, or Simpy object."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            # isinstance(rhs, Simpy)
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Generates a mask based on the greater than relationship between each index of self..."""
        """...and a float value, or Simpy object."""
        greater_mask: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    greater_mask.append(True)
                else:
                    greater_mask.append(False)
        else:
            # isinstance(rhs, Simpy)
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    greater_mask.append(True)
                else:
                    greater_mask.append(False)
        return greater_mask
    
    def __getitem__(self, rhs: int) -> float:
        """Gives the ability to use the subscription notation operator with Simpy objects."""
        return self.values[rhs]

    
        
        
