instructions = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        instructions.append(line.strip().split())

# print(instructions)

# Create 2D matrix of values
lights = [[0 for x in range(1000)]for y in range(1000)]

for instruction in instructions:
    if instruction[0] == "toggle":
        # start x and y
        sx, sy = list(map(int, instruction[1].split(',')))
        # end x and y
        ex, ey = list(map(int, instruction[3].split(',')))

        # Traverse and make changes
        for y in range(sy, ey+1):
            for x in range(sx, ex+1):
                # increase by 2
                lights[y][x] += 2

    elif instruction[0] == "turn":
        direction = 1 if instruction[1] == "on" else -1
        # start x and y
        sx, sy = list(map(int, instruction[2].split(',')))
        # end x and y
        ex, ey = list(map(int, instruction[4].split(',')))

        # Traverse and make changes
        for y in range(sy, ey+1):
            for x in range(sx, ex+1):
                # Set to direction
                lights[y][x] += direction
                if lights[y][x] < 0:
                    lights[y][x] = 0

# Go through at the end and count
total_brightness = 0
for y in range(1000):
    for x in range(1000):
        total_brightness += lights[y][x]
print(total_brightness)
