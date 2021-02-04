"""An exercise in remainders and boolean logic."""

__author__ = 730151647

x: int = int(input("Pick a number, any number..."))

if ((x % 2 == 0) or (x % 7 == 0)):
    if (x % 2 == 0):
        if (x % 7 == 0):
            if ((x % 2 == 0) and (x % 7 == 0)):
                print("TAR HEELS")
        else:
            print("TAR")
    else:
        print("HEELS")
else:
    print("CAROLINA")