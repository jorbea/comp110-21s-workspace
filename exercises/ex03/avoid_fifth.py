"""EX03 - avoid_fifth function."""

__author__: str = "730151647"


def main() -> None:
    """Entrypoint of the program."""
    print("Hello")
    print(avoid_fifth("Hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(phrase: str) -> str:
    """Takes a word or group of words and removes the letter "e" (both uppercase and lowercase)."""
    phrase_length: int = len(phrase)
    phrase_list: list[str] = list(phrase)
    i: int = 0
    while phrase_length > 0:
        if (phrase[i] == "e") or (phrase[i] == "E"):
            # This does not work because it is removing the last character of the string everytime an "e" or "E" is detected.
            phrase_list.pop()
            phrase_length -= 1
            i += 1
    phrase = phrase.join(phrase_list)
    return phrase


if __name__ == "__main__":
    main()