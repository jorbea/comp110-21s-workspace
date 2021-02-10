"""Tar Heels exercise redux as a structured program."""

__author__ = "730151647"


from random import choice


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(choice: int) -> str:
    """Integer from user is evaluated and a string is returned."""
    if ((choice % 2 == 0) or (choice % 7 == 0)):
        if (choice % 2 == 0):
            if (choice % 7 == 0):
                return("TAR HEELS")
            else:
                return("TAR")
        else:
            return("HEELS")
    else:
        return("CAROLINA")


if __name__ == "__main__":
    main()
