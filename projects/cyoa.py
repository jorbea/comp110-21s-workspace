"""Choose your own adventure!"""

__author__ = "730151647"

def main() -> None:
    greet("welcome")
    player: str = "Player 1: "
    points: int = 0
    health: int = 100

    
def greet(welcome: str) -> None:
    print("Welcome to 14 Days Later: Wrath of COVID-19!")
    print("You have been called out of retirement... As the most elite T-cell in the history of SEAL TEAM Sick you are our last hope to stop the ongoing invasion.")
    print("I am Thymus, the commander in chief of SEAL Team Sick, and I will be your eyes and ears throughout your mission.")
    global player
    player = input("Player 1: ")
    print("I don't need to tell you this will be no small task, but we know if anyone can save this ship from sinking it's you " + player + "!")
    return None







if __name__ == "__main__":
    main()
