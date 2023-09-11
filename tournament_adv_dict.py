entrants = {
    'Dan': 10,
    'Wolfgang': 20,
    'June': 53,
    'Tany': 37,
    'Sharon': 14
}

new_player = {"Benji" : 49, "Angel" : 26}
entrants.update(new_player)

print(f"Original Entrants: {entrants}")

## To eliminate people from the entrants, can use filter or for loop:

# Using a for loop:
quarter_finals = {}
for player, score in entrants.items():
    if score >= 20:
        quarter_finals[player] = score

print(f"\nQuarter-finalists = {quarter_finals}")

# Using filter:
# Note how the dictionaries are turned into lists of tuples using .items()

semi_finals = dict(filter(lambda player : player[1] > 30, quarter_finals.items()))
print(f"\nSemi-finalists = {semi_finals}")

finals = dict(filter(lambda player : player[1] > 45, semi_finals.items()))
print(f"\nFinalists = {finals}")