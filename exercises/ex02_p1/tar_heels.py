"""Tar Heels exercise redux as a structured program."""

__author__ = "730151647"


# from random import choice


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # choice: int = int(input("Enter an int: "))
    response: int = int(input("Enter an int: "))
    print(tar_heels(response))


def tar_heels(t: int) -> str:
    """Integer from user input is evaluated based on its divisibility and a string is returned to main()."""
    if ((t % 2 == 0) or (t % 7 == 0)):
        if (t % 2 == 0):
            if (t % 7 == 0):
                return("TAR HEELS")
            else:
                return("TAR")
        else:
            return("HEELS")
    else:
        return("CAROLINA")


if __name__ == "__main__":
    main()
