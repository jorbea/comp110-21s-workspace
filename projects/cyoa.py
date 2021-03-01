"""Choose your own adventure!"""
from random import randint

"""Went above and beyond per specification #10: Battle simulation with health updates 
and emoji in the nasal function call."""
"""Went above and beyond per specification #9: In the main function the player can choose 
to replay their first mission, continue, or end the game. If the player replays their
first mission then they will have the opportunity to continue or end the game after
that round."""

__author__ = "730151647"

player: str = ""
points: int = 0
emoji_constant = "\U0001F974"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    global points
    print("Thymus: In order to stop the COVID invasion you must go to the source... The lungs!")
    print("Thymus: I'm also recieving word that our host didn't follow the BCCDC guidelines last night...")
    print("Thymus: We have detected an unknown invader proliferating in the nasal passage.")
    print("Thymus: It's your choice where to go first, but go ASAP before we're completely overrun...")
    print("Thymus: Show those virions the meaning of apoptosis!")
    print("Would you like to (1) - continue to the nasal passage, (2) - continue to the lungs, (3) - quit?")
    path_1: str = input("1, 2, or 3: ")
    if path_1 == "1" or path_1 == "2":
        if path_1 == "1":
            points += 50
            points += nasal(points)
        else:
            points += 200
            points += lungs(points)
    else:
        print(f"Adventure points: {str(points)}")
        print("Goodbye!")
        return None
    print(f"Adventure points: {str(points)}")

    print("Thymus: Great work! Our host is starting to feel better. Let's finish this!")
    print("Would you like to (1) - continue to the nasal passage, (2) - continue to the lungs, (3) - quit?")
    path_2: str = input("1, 2, or 3: ")
    if path_2 == "1" or path_2 == "2":
        if path_2 == "1":
            points += 50
            points += nasal(points)
        else:
            points += 200
            points += lungs(points)
    else:
        print(f"Adventure points: {str(points)}")
        print("Goodbye!")
        return None
    print(f"Adventure points: {str(points)}")

    path_3 = ["1", "2", "3"]
    path_3.remove(path_1)
    print(f"Would you like to ({path_3[0]}) - continue or (3) - quit?")
    choice: str = input()
    if choice == "1" or choice == "2":
        if choice == "1":
            points += 50
            points += nasal(points)
        else:
            points += 200
            points += lungs(points)
    else:
        print(f"Adventure points: {str(points)}")
        print("Goodbye!")
        return None
    print("Thymus: You defeated the Flu and COVID!")
    print("\U0001F389")
    print(f"Adventure points: {str(points)}")
    print("The End!")


def greet() -> None:
    """Welcomes the player, provides background on the game, and asks for player input of their name."""
    print("Welcome to 14 Days Later: Wrath of COVID-19!")
    print("You have been called out of retirement... As the most elite T-cell in the history of SEAL TEAM Sick you") 
    print("are our last hope to stop the ongoing invasion.")
    print("Thymus: I am Thymus, the commander in chief of SEAL Team Sick, and I will be your eyes and ears")
    print("throughout your mission.")
    global player
    player = input("Player 1: ")
    print("Thymus: I don't need to tell you this will be no small task, but we know if anyone can save")
    print(f"this ship from sinking it's you {str(player)}!")
    return None


def nasal(nasal_points: int) -> int:
    """Takes the user through the mission of defeating the unknown invader."""
    points = 0
    global emoji_constant
    print("You waste little time traveling to the site of the unknown invader!")
    print("Thymus: Not this guy again!")
    print("You come across a mass of spike proteins bound to sialic acid...")
    print("Thymus: Looks like our ole frenemie is trying to take advantage of all the chaos.")
    print("When will the Flu ever learn?") 
    print(f"Flu: {str(player)} \U0001F628! Not you again!")
    flu_health: int = 100
    print(f"Flu Heath: {flu_health}")
    print("Attack! (1) - Perforin or (2) - Cytotoxin")
    while flu_health > 0:
        if input("1 or 2: ") == "1":
            flu_health -= 25
            print(emoji_constant)
            print(f"Flu Heath: {flu_health}")
        else:
            flu_health -= 50
            print(emoji_constant)
            print(f"Flu Heath: {flu_health}")
    print("\U0001F635")
    points += 250
    return points


def lungs(lungs_points: int) -> int:
    """Takes the user through the mission of defeating COVID."""
    global points
    print("After a quick ride through the bloodstream you find yourself in the belly of the beast.")
    print("Thymus: Heads up! I'm detecting multiple COVID virions coming your way.")
    print("Thymus: If you destroy the queeen then all of the other COVID particles will die with it.")
    print("Thymus: However, I can't identify which is the queen.")
    print("It's up to you to find the queen and end all of this!")
    print("COVID: Say goodbye to your most elite T-cell Thymus!")
    drone_or_queen: int = randint(1, 4)
    while int(input("Pick a number 1 - 4: ")) != drone_or_queen:
        print("\U0001F608")
        print("Drone destroyed!")
    print("\U0001F635")
    print("You destroyed the queen!")
    return 500


if __name__ == "__main__":
    main()
