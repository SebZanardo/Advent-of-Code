# read input into 2D array
pipes = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        pipes.append(list(line.strip()))

width = len(pipes[0])
height = len(pipes)


def display_pipes(pipes):
    for row in pipes:
        print(' '.join(row))


def display_maze(pipes):
    for row in pipes:
        print(''.join(row))


# Find start position
for y in range(height):
    for x in range(width):
        if pipes[y][x] == 'S':
            start_x = x
            start_y = y

# To find furthest point from the start of the loop
#   traverse the maze of pipes with BFS Algorithm.

EMPTY = '.'
VISITED = '*'
# Create second matrix for second part of problem. Either visited or not
pipes_loop = [[EMPTY for x in range(width)] for y in range(height)]

# Direction constants
NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)
PIPE_FLOW = {
    'S': (NORTH, EAST, SOUTH, WEST),
    '|': (NORTH, SOUTH),
    '-': (EAST, WEST),
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (SOUTH, WEST),
    'F': (SOUTH, EAST),
}

stack = [(start_x, start_y)]

start_type = set()
# Repeat until the stack is not empty, (no more paths to explore)
while stack:
    # Loop through points on stack backwards so can pop them as we go
    for i in range(len(stack)-1, -1, -1):
        x, y = stack.pop(i)
        pipe = pipes[y][x]

        directions = PIPE_FLOW[pipe]

        # Add valid directions to stack and update pipes matrix
        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            # Check if inside 2D matrix
            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                continue

            new_pipe = pipes[new_y][new_x]

            # Check that neighbour is a pipe and not visited
            if new_pipe not in PIPE_FLOW or pipes_loop[new_y][new_x] == VISITED:
                continue

            # Check that pipe connects to current pipe.
            #   Opposite directions connect!
            new_directions = PIPE_FLOW[new_pipe]
            connects = False
            for new_direction in new_directions:
                if new_direction == NORTH and direction != SOUTH:
                    continue
                elif new_direction == SOUTH and direction != NORTH:
                    continue
                elif new_direction == WEST and direction != EAST:
                    continue
                elif new_direction == EAST and direction != WEST:
                    continue
                connects = True
                break

            if connects and (new_x, new_y) not in stack:
                stack.append((new_x, new_y))

                # For later! Turn start into regular pipe
                if pipe == 'S':
                    start_type.add((new_x-start_x, new_y-start_y))

        # Mark current as visited in another matrix
        pipes_loop[y][x] = VISITED

# Work out what start pipe is
if NORTH in start_type and SOUTH in start_type:
    start_pipe = '|'
elif EAST in start_type and WEST in start_type:
    start_pipe = '-'
elif NORTH in start_type and EAST in start_type:
    start_pipe = 'L'
elif NORTH in start_type and WEST in start_type:
    start_pipe = 'J'
elif SOUTH in start_type and EAST in start_type:
    start_pipe = 'F'
elif SOUTH in start_type and WEST in start_type:
    start_pipe = '7'
print("start is:", start_pipe)
pipes[start_y][start_x] = start_pipe

# Flood fill algorithm!
# Go through all the tiles in the pipes matrix and if EMPTY, flood fill.
#   If the region needs to check neighbours outside of the bounds of the matrix
#   then it can be assumed that the region is on the edge and not enclosed.

# display_pipes(pipes_loop)

OUTSIDE = 'O'
POSSIBLE_INSIDE = '?'
enclosed_tiles = 0  # Count is not accurate yet as have to do another step

for y in range(height):
    for x in range(width):
        tile = pipes_loop[y][x]

        if tile == EMPTY:
            # Start of a new_region
            is_enclosed = True
            region_size = 0
            stack = [(x, y)]
            region = []

            while stack:
                tx, ty = stack.pop()
                for direction in (NORTH, EAST, SOUTH, WEST):
                    new_x = tx + direction[0]
                    new_y = ty + direction[1]

                    # Check if inside
                    if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                        is_enclosed = False
                        continue

                    if pipes_loop[new_y][new_x] == EMPTY and (new_x, new_y) not in stack:
                        stack.append((new_x, new_y))
                # Mark current as VISITED!
                pipes_loop[ty][tx] = OUTSIDE
                region.append((tx, ty))
                region_size += 1

            if is_enclosed:
                enclosed_tiles += region_size
                for pos in region:
                    rx, ry = pos
                    pipes_loop[ry][rx] = POSSIBLE_INSIDE

print("before quirks: ", enclosed_tiles)
# To solve quirk of the problem where gaps that can be traced between parallel pipes is considered
#   a way for a region to be *outside* and not enclosed, create larger version of actual maze.
# 3x3 for each cell
WALL = '#'
OPEN = '.'
large_maze = []
for y in range(height):
    row1 = []
    row2 = []
    row3 = []
    for x in range(width):
        cell = pipes_loop[y][x]
        if cell == VISITED:
            # Check which pipe configuration
            pipe = pipes[y][x]
            if pipe == '|':
                row1 += [OPEN, WALL, OPEN]
                row2 += [OPEN, WALL, OPEN]
                row3 += [OPEN, WALL, OPEN]
            elif pipe == '-':
                row1 += [OPEN, OPEN, OPEN]
                row2 += [WALL, WALL, WALL]
                row3 += [OPEN, OPEN, OPEN]
            elif pipe == 'F':
                row1 += [OPEN, OPEN, OPEN]
                row2 += [OPEN, WALL, WALL]
                row3 += [OPEN, WALL, OPEN]
            elif pipe == '7':
                row1 += [OPEN, OPEN, OPEN]
                row2 += [WALL, WALL, OPEN]
                row3 += [OPEN, WALL, OPEN]
            elif pipe == 'L':
                row1 += [OPEN, WALL, OPEN]
                row2 += [OPEN, WALL, WALL]
                row3 += [OPEN, OPEN, OPEN]
            elif pipe == 'J':
                row1 += [OPEN, WALL, OPEN]
                row2 += [WALL, WALL, OPEN]
                row3 += [OPEN, OPEN, OPEN]
        else:
            row1 += [OPEN, OPEN, OPEN]
            row2 += [OPEN, OPEN, OPEN]
            row3 += [OPEN, OPEN, OPEN]

    large_maze.append(row1)
    large_maze.append(row2)
    large_maze.append(row3)


display_pipes(pipes_loop)
display_maze(large_maze)

# Traverse large maze starting from possibe open cells.
#   If cell is open and multiple of 3 then check pipes_loop array
#   if a ? then remove 1 from enclosed_tiles counter!
stack = []
for y in range(height):
    for x in range(width):
        if pipes_loop[y][x] == OUTSIDE:
            stack.append((x*3, y*3))

while stack:
    x, y = stack.pop()
    for direction in (NORTH, EAST, SOUTH, WEST):
        new_x = x + direction[0]
        new_y = y + direction[1]

        # Check if inside
        if new_x < 0 or new_x >= width*3 or new_y < 0 or new_y >= height*3:
            continue

        cell = large_maze[new_y][new_x]
        # Check if visited, wall or in stack
        if cell == VISITED or cell == WALL or (new_x, new_y) in stack:
            continue

        stack.append((new_x, new_y))
    large_maze[y][x] = VISITED

    # Check if is possible inside and if so reduce!
    if y % 3 == 0 and x % 3 == 0:
        cell = pipes_loop[int(y/3)][int(x/3)]
        if cell == POSSIBLE_INSIDE:
            enclosed_tiles -= 1

display_maze(large_maze)
print(enclosed_tiles)
