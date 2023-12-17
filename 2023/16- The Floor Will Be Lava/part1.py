contraption = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        contraption.append(list(line.strip()))

width = len(contraption[0])
height = len(contraption)
print(contraption)
print(width, height)

light_map = [[[] for x in range(width)] for y in range(height)]

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


stack = [(0, 0, EAST)]
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
