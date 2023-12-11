universe = []
# Read file into Matrix!
with open('input.txt', 'r') as file:
    for line in file.readlines():
        universe.append(list(line.strip()))


def display_universe(universe):
    for row in universe:
        print(' '.join(list(map(str, row))))


GALAXY = '#'
EMPTY = '.'


# Find and duplicate empty rows
new_row_spots = []
for i, row in enumerate(universe):
    if GALAXY not in row:
        new_row_spots.append(i)

# Find and duplicate empty columns
b_width = len(universe[0])
b_height = len(universe)
new_col_spots = []
for x in range(b_width):
    is_empty = True
    for y in range(b_height):
        if universe[y][x] == GALAXY:
            is_empty = False
            break
    if is_empty:
        new_col_spots.append(x)

print(new_col_spots)
print(new_row_spots)

# Find all galaxy positions
galaxies = []
x_offset = 0
y_offset = 0
for y in range(b_height):
    x_offset = 0
    if y in new_row_spots:
        y_offset += 1
    for x in range(b_width):
        if x in new_col_spots:
            x_offset += 1
        if universe[y][x] == GALAXY:
            galaxies.append((x+x_offset, y+y_offset))
print(galaxies)


# Initially I calculated distance map from each galaxy to all cells in
#   anticipation of a pathfinding BFS problem in part 2.
# Turns out part2 was just some simple vector maths offsetting galaxies
#   before calculating distances which can also be used to solve part1!

# Calculate sum
distance_sum = 0
for start, galaxy in enumerate(galaxies):
    sx, sy = galaxy
    # Calculate distance to remaining un paired galaxies and add to sum
    for g in range(start+1, len(galaxies)):
        ox, oy = galaxies[g]
        distance = abs(ox-sx) + abs(oy-sy)

        print(f"{start+1}->{g+1}={distance}")
        distance_sum += distance
print(distance_sum)
