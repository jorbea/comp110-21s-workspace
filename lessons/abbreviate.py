"""Practice problem from Kaki's review session on 03/17/21."""


def find_capitals(word: str) -> str:
    capitals: str = ""
    # i is going from 0 up to len - 1
    for i in range(len(word)):
        if word[i].lower() != word[i]:
            capitals += word[i]
    return capitals    


def abbreviate(strings: list[str]) -> dict[str, str]:
    abbreviations: dict[str, str] = {}
    for name in strings:
        abbreviated: str = find_capitals(name)
        abbreviations[name] = abbreviated
    return abbreviations

abbreviate(["United States of America", "Happy BDay"])

