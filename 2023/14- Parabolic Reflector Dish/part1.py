platform = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        platform.append(list(line.strip()))
# print(platform)

ROUND_ROCK = 'O'
CUBE_ROCK = '#'
EMPTY = '.'

# Go though matrix (platform) *top to bottom* left-> right.
# When cell is a round rock slide north!
width = len(platform[0])
height = len(platform)


def slide_rock(x, y, platform):
    new_y = y - 1  # North
    distance = 0
    while new_y >= 0 and platform[new_y][x] == EMPTY:
        new_y -= 1
        distance += 1
    return distance


def display_platform(platform):
    for row in platform:
        print(' '.join(row))
    print()


total_damage = 0
for y in range(height):
    for x in range(width):
        cell = platform[y][x]

        if cell != ROUND_ROCK:
            continue

        distance = slide_rock(x, y, platform)
        # Move rock in Matrix to new position
        platform[y][x] = EMPTY
        new_y = y - distance
        platform[new_y][x] = ROUND_ROCK
        # Calculate and add damage
        damage = height - new_y
        total_damage += damage

display_platform(platform)
print(total_damage)
