"""Practice problem from Kaki's review session on 03/17/21."""


def find_capitals(word: str) -> str:
    capitals: str = ""
    # i is going from 0 up to len - 1
    for i in range(len(word)):
        if word[i].lower() != word[i]:
            capitals += word[i]
    return capitals


def phonebook(numbers: list[int], names: list[str]) -> dict[int, str]:
    book: dict[int,str] = {}
    for i in range(len(numbers)):
        abbreviation: str = find_capitals(names[i])
        book[numbers[i]] = abbreviation

        # book[number[i]] = find_capitals(names[i])]

    # or...
    # idx: int = 0
    # for num in phone_num:
    #   abbreviation: str = find_capitals(names[idx])
    #   book[num] = abbreviation
    #   idx += 1
    return book

