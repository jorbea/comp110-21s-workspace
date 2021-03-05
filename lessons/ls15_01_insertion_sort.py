"""The insertion sort algorithm."""


def isort(xs: list[int]) -> None:
    """Example of a procedure, which returns None."""
    i: int = 1
    j: int
    """"Swapping back incorrect items."""
    while i < len(xs):
        j = i
        while j > 0 and xs[j] < xs[j - 1]:
            swap(xs, j, j - 1)
            j -= 1

        i += 1


def swap (xs: list[int], i: int, j: int) -> None:
    temp: int = xs[i]
    xs[i] = xs[j]
    xs[j] = temp


nums: list[int] = [2, 3, 1, 4, -1, 20, 10, 5, 2, 1]
isort(nums)
print(nums)
