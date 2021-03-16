"""Examples of dictionaries."""

# Establish a type with dict[key type, value type]
# Key type always precedes value type
# Empty dictionary literal is {}
players: dict[str, int] = {}

# Insert a new key-value pair
# Reference keys inside subscription notation, associated values are assigned
players["Brooks"] = 15
# Can have duplicate values but not duplicate keys.
players["Love"] = 2
players["Bacot"] = 4 # This is intentionally off by one
players["Bacot"] = players["Bacot"] + 1
print(players)
print(players["Brooks"])

# for..in loops will give you each key one-by-one
for player_name in players:
    # for-in loops allow the variable following "for" to be inferred rather than being explicitly defined
    key: str = player_name
    value: int = players[key]
    print(f"{player_name} -> {players[player_name]}")
    print(f"{key} -> {value}")

# You can have keys and values of any types! Notice this is the opposite mapping
# that we have above. Additionally this is an example of a dictionary literal.
jerseys: dict[int, str] = {15: "Brooks", 2: "Love", 5: "Bacot"}
jerseys[23] = "Jordan"
print(jerseys)
print(jerseys[23])

# The pop method allows you to remove a key-value pair by its key. The pop
# method returns the value associated with the popped key.
popped_name: str = jerseys.pop(23)
print(popped_name)
print(jerseys)