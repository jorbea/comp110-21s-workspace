"""Examples using loops."""

count: int = 0
while input("Do you need more love? yes/no - ") == "yes":
    # Body block of the while loop is evaluated
    # when the test expression is true.
    print("I love you!")
    count += 1
    print(f"Count is {count}")
    if count > 3:
        print("Wow, I really, truly, deeply love you")

# Iterating a specific number of times
i: int = 0 # i is typically short for index
itereations: int = 1000000

while i < itereations:
    if i % 1000 == 0:
        print(f"I love you! i: {i}")
    i += 1 # Important that this increment is NOT in the if statement

print("Have a lovely day.")
