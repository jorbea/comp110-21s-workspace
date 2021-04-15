"""Examples of vectorized operations on StrArray."""

from __future__ import annotations

from typing import Union

class StrArray:
    """Utility class for common string column operations."""
    
    values: list[str]

    def __init__(self, values: list[str]):
        self.values = values

    def __repr__(self) -> str:
        return f"StrArray({self.values})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        # Shows what is being added on the next line
        # print(f"__add__({self}, {rhs})")
        result: list[str] = []
        if isinstance(rhs, str):
            for item in self.values:
                result.append(item + rhs)
        # Can just use an "else" statement
        elif isinstance(rhs, StrArray):
            assert len(self.values) == len(rhs.values)
            # range(start[inclusive], stop[exclusive], step)
            # start and step can be dafaulted to 0 and 1 respectively when left out.
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return StrArray(result)


s: StrArray = StrArray(["a", "b", "c"])
t = StrArray(["d", "e", "f"])
print(s)
print(t)
print(s + "!")
print(t + " wow!")
print(s + t)

first = StrArray(["Kris", "Kaki", "Jordan"])
last = StrArray(["Jordan", "Ryan", "Bean"])
full_name = last + ", " + first
print(full_name)
full_name = first + "/" + last
print(full_name)

# This is an example of an AssertionError
t = StrArray(["d", "e", "f", "g"])
print(s + t)