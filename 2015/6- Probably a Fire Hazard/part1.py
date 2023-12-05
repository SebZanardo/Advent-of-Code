instructions = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        instructions.append(line.strip().split())

# print(instructions)

# Create 2D matrix of boolean values
# I'm assuming lights start off
lights = [[False for x in range(1000)]for y in range(1000)]

for instruction in instructions:
    if instruction[0] == "toggle":
        # start x and y
        sx, sy = list(map(int, instruction[1].split(',')))
        # end x and y
        ex, ey = list(map(int, instruction[3].split(',')))

        # Traverse and make changes
        for y in range(sy, ey+1):
            for x in range(sx, ex+1):
                # Switch to opposite
                current = lights[y][x]
                lights[y][x] = not current

    elif instruction[0] == "turn":
        direction = True if instruction[1] == "on" else False
        # start x and y
        sx, sy = list(map(int, instruction[2].split(',')))
        # end x and y
        ex, ey = list(map(int, instruction[4].split(',')))

        # Traverse and make changes
        for y in range(sy, ey+1):
            for x in range(sx, ex+1):
                # Set to direction
                lights[y][x] = direction

# Go through at the end and count
switched_on = 0
for y in range(1000):
    for x in range(1000):
        if not lights[y][x]:
            continue
        switched_on += 1
print(switched_on)
