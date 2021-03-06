"""EX03 - palindromify function."""

__author__: str = "730151647"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("dances", False))
    print(palindromify("To", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(word: str, even: bool) -> str:
    """Takes a word and turns it into a palindrome."""
    i: int = 1
    palin: str = word
    if even is False:
        while i < len(word):
            NEW_LEN: int = len(word) - 1
            palin += word[NEW_LEN - i]
            i += 1
    i = 0
    if even is True:
        while i < len(word):
            NEW_LEN = len(word) - 1
            palin += word[NEW_LEN - i]
            i += 1
    return palin


if __name__ == "__main__":
    main()