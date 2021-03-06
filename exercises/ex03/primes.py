"""EX03 - prime functions."""

__author__: str = "730151647"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))

    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(num: int) -> bool:
    """Returns True if argument of function is prime (can only be divided by 1 and itself)."""
    """Returns False if argument is not prime or is less than or equal to 1."""
    divide_two: bool = (num % 2 == 0) and num > 2
    less_two: bool = num < 2
    divide_three: bool = (num % 3 == 0) and num > 3
    divide_five: bool = (num % 5 == 0) and num > 5
    while divide_two or less_two or divide_three or divide_five:
        return False
    return True


def list_primes(min: int, max: int) -> list[int]:
    """Returns list of prime numbers within the range [x, y)."""
    prime_nums: list[int] = []
    while min < max:
        if is_prime(min) is True:
            prime_nums.append(min)
        min += 1
    return prime_nums


if __name__ == "__main__":
    main()