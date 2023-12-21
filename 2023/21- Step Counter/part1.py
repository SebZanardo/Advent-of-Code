matrix = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        matrix.append(list(line.strip()))

# print(matrix)

width = len(matrix[0])
height = len(matrix)

START = 'S'
GARDEN_PLOT = '.'
ROCK = '#'

# Find start
for y in range(height):
    for x in range(width):
        if matrix[y][x] == START:
            start_x = x
            start_y = y

# BFS to find all reachable plots
stack = [(start_x, start_y)]
seen = set()
steps = 64

while steps > 0:
    length_of_turn = len(stack)
    for _ in range(length_of_turn):
        x, y = stack.pop(0)

        for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_x = x + direction[0]
            new_y = y + direction[1]

            # Inside bounds
            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                continue

            if matrix[new_y][new_x] == ROCK:
                continue

            if (new_x, new_y) in seen or (new_x, new_y) in stack:
                continue

            seen.add((new_x, new_y))
            stack.append((new_x, new_y))
    steps -= 1

# Similar idea to deciding whether square on chess board is white or black
#   based on x, y position. Need to check if start_square is white or black 
#   first to determine the colour of the rest of the squares
is_odd = (start_x + start_y) % 2
valid_plots = 0
for x, y in seen:
    if (x + y) % 2 == is_odd:
        valid_plots += 1
print(valid_plots)
