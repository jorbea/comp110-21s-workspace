"""Practice with writing function definitions."""

def main() -> None:
    print(reverse("hello"))
    return None


def reverse(string: str) -> str:
    i: int = 0
    gnirts: str = ""
    while i < len(string):
        gnirts += string[(len(string) - 1) - i]
        i += 1
    return gnirts


if __name__ == "__main__":
    main()