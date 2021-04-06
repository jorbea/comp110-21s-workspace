"""Examples of object-oriented programming concepts."""

class Point:
    # Defining attributes (related variables) of our class.
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y arguments."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Magic method to represent object as string."""
        return f"{self.x}, {self.y}"

    def invert(self) -> None:
        """Method to invert the attributes (swap) of the Point."""
        temp: float = self.x
        self.x = self.y
        self.y = temp

    def move_up(self, dy: float) -> None:
        """Increase the y attribute of an object."""
        self.y += dy


a: Point = Point(4.0, 5.0)
print(a.__repr__()) # This is the same as print(a) ... typically will not do this!
# Conventional to just print(a)!
a.invert()
print(a)
a.move_up(10.0)
print(a)

b: Point = Point(0.0, 0.0)
# Assign to attributes of an object:
b.x = 2.0
b.y = -1.0
print(b)
b.invert()
print(b.x)
print(b.y)
