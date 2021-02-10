"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730151647"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Takes a random number between 1 & 4, assigns it to x, and returns a fortune based on the relation to x."""
    x: int = randint(1, 4)
    if (x < 4):
        if (x < 3):
            if (x == 2):
                return("404 Fortune Not Found.")
            else:
                return("Your diamond hands remain unbreakable!")
        else:
            return("GME isn't the only thing going to the moon!")
    else:
        return("The mighty oak was once a little acorn that stood its ground!")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
