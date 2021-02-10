"""Tar Heels exercise redux as a structured program."""

__author__ = "730151647"


from random import choice


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(response: int) -> str:
    if ((response % 2 == 0) or (response % 7 == 0)):
        if (response % 2 == 0):
            if (response % 7 == 0):
                return("TAR HEELS")
            else:
                return("TAR")
        else:
            return("HEELS")
    else:
        return("CAROLINA")


if __name__ == "__main__":
    main()
