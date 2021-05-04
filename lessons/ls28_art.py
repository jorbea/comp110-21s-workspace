from turtle import Turtle, done, up


TRUNK = 100.0
UP = 90.0
HALF_CIRCLE = 180.0

t: Turtle = Turtle()


def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    branch(TRUNK, UP)
    t.getscreen().update()


def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 3:
        ... # Base case: do nothing!
    else:
        # Recursive case! Branch again!
        branch(length * 0.6, angle + 25)
        branch(length * 0.65, angle - 20)
    # Bring the turtle back to its starting point
    t.setheading(angle + HALF_CIRCLE)
    t.forward(length)

if __name__ == "__main__":
    t.speed(0)
    t.getscreen().tracer(0, 0)
    t.getscreen().onclick(tree)
    tree(0, 0)
    done()