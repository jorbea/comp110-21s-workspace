"""Example of elif."""

number: int = int(input("Pick a number: "))
answer: int = 50

# This form of nested else-if statement...
if number < answer:
    print("too low")
else: 
    if number > answer:
        print("too high")
    else:
        print("you got it!")
# ...if the same as using elif in this way
if number < answer:
    print("too low")
elif number > answer:
    # elif is short for else if
    print("too high")
else:
    print("you got it!")