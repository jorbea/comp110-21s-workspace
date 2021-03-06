"""EX03 - avoid_fifth function."""

__author__: str = "730151647"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
    print(avoid_fifth("taaaaar heeeels!"))
    print(avoid_fifth("TAAAAR HEEEELS!"))


def avoid_fifth(word: str) -> str:
    """Removes the "e"s and "E"s from strings."""
    i: int = 0 
    edit: str = ""
    while i < len(word):
        if (word[i] != "e") and (word[i] != "E"):
            edit += word[i]
        i += 1
    return edit


if __name__ == "__main__":
    main()