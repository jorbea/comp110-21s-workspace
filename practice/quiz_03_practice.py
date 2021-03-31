"""Practice for the upcoming Quiz 03."""


from typing import KeysView


def dictTransform(dictionary: dict[int, list[int]]) -> dict[int, list[int]]:
    """Multiplies every value in a list by its corresponding key."""

    for key in dictionary:
        for value in range(len(dictionary[key])):
            dictionary[key][value] *= key
    
    return dictionary

print(dictTransform({2: [1, 2], 5: [3, 4]}))


def listTransform(list_dict: list[dict[int, str]]) -> list[dict[int, str]]:
    """Returns a transformed list with changes to every even dictionary."""

    for i in range(0, len(list_dict), 2):
        for key in list_dict[i]:
            if key % 2 == 1:
                list_dict[i][key] = list_dict[i][key][0]
            else:
                list_dict[i][key] = list_dict[i][key][len(list_dict[i][key]) - 1]
    return list_dict

print(listTransform([{3: 'roy', 2: 'unc'}, {1: 'kris'}, {9: 'hello', 11: 'there', 2: '!!'}]))
