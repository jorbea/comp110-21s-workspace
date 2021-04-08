"""Examples of object-oriented programming concepts."""

from __future__ import annotations

class Point:
    # Defining attributes (related variables) of our class.
    x: float
    y: float

    # Example of a constructor
    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y arguments."""
        self.x = x
        self.y = y

    # Example of a method
    # Python automatically calls this method
    def __repr__(self) -> str:
        """Magic method to represent object as string."""
        return f"{self.x}, {self.y}"

    def scale_by(self, factor: float) -> None:
        """Example method that mutates the object it is called on."""
        self.x *= factor
        self.y *= factor

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        print("__mul__ was called")
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

    # def scale(self, factor: float) -> Point:
        # """Example method that DOES NOT mutate the object it is called on."""
        # x: float = self.x * factor
        # y: float = self.y * factor
        # p: Point = Point(x, y)
        # return Point(self.x * factor, self.y * factor)

# Calls upon the constructor and establishes the object with x = 1.0 and y = 2.0.
a: Point = Point(1.0, 2.0)
# a.x *= 2 # x-attribute of the Point object = 2.0
# a.y *= 2 # y-attribute of the Point object = 4.0
# print(f"a: {a}")

# a.scale_by(2.0)
# print(f"a: {a}")

# b: Point = a.scale(2.0) # "b" is now an object with the attributes of "a" scaled twice
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])



