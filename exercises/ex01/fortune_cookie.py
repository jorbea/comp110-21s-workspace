"""Program that outputs one of at least four random, good fortunes."""

__author__ = 730151647

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")
x: int = randint(1, 4)

if (x < 4):
    if (x < 3):
        if (x == 2):
            print("404 Fortune Not Found.")
        else:
            print("Your diamond hands remain unbreakable!")
    else:
        print("GME isn't the only thing going to the moon!")
else:
    print("The mighty oak was once a little acorn that stood its ground!")

print("Now, go spread positive vibes!")
