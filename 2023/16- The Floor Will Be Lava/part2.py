contraption = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        contraption.append(list(line.strip()))

width = len(contraption[0])
height = len(contraption)
print(contraption)
print(width, height)


NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)


def inside_bounds(x, y):
    return x >= 0 and x < width and y >= 0 and y < height


def add(x, y, dir):
    if not inside_bounds(x, y):
        return
    stack.append((x, y, dir))


start_positions = []
for x in range(width):
    start_positions.append((x, 0, SOUTH))
    start_positions.append((x, height-1, NORTH))
for y in range(height):
    start_positions.append((0, y, EAST))
    start_positions.append((width-1, y, WEST))

maximum = 0
for start_position in start_positions:
    light_map = [[[] for x in range(width)] for y in range(height)]
    stack = [start_position]
    energized = 0
    while stack:
        x, y, direction = stack.pop(0)

        if direction in light_map[y][x]:
            continue

        cell = contraption[y][x]
        if cell == '|' and (direction == EAST or direction == WEST):
            add(x, y+1, SOUTH)
            add(x, y-1, NORTH)
        elif cell == '-' and (direction == NORTH or direction == SOUTH):
            add(x-1, y, WEST)
            add(x+1, y, EAST)
        elif cell == '/':
            if direction == NORTH:
                add(x + 1, y, EAST)
            elif direction == EAST:
                add(x, y - 1, NORTH)
            elif direction == WEST:
                add(x, y + 1, SOUTH)
            elif direction == SOUTH:
                add(x - 1, y, WEST)
        elif cell == '\\':
            if direction == NORTH:
                add(x - 1, y, WEST)
            elif direction == EAST:
                add(x, y + 1, SOUTH)
            elif direction == WEST:
                add(x, y - 1, NORTH)
            elif direction == SOUTH:
                add(x + 1, y, EAST)
        else:
            add(x+direction[0], y+direction[1], direction)

        if len(light_map[y][x]) == 0:
            energized += 1
        light_map[y][x].append(direction)

    print(energized)
    if energized > maximum:
        maximum = energized
print(maximum)
