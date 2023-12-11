# read input into 2D array
pipes = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        pipes.append(list(line.strip()))

width = len(pipes[0])
height = len(pipes)

# Find start position
for y in range(height):
    for x in range(width):
        if pipes[y][x] == 'S':
            start_x = x
            start_y = y

# To find furthest point from the start of the loop
#   traverse the maze of pipes with BFS Algorithm.

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

steps = -1
stack = [(start_x, start_y)]

# Repeat until the stack is not empty, (no more paths to explore)
while stack:
    steps += 1
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

            # Check that neighbour is a pipe
            if new_pipe not in PIPE_FLOW:
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

        # Mark current as visited by changing value to int
        pipes[y][x] = str(steps)


def display_pipes(pipes):
    for row in pipes:
        print(' '.join(row))


display_pipes(pipes)
print(steps)
