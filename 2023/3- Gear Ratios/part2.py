digits = '0123456789'

engine_schematic = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        engine_schematic.append(list(line.strip()))

# All rows are same width
width = len(engine_schematic[0])
height = len(engine_schematic)

sum_of_gear_ratios = 0

# Step 1: Go through matrix and turn
#   numbered cells into numbers in parts array
#   and fill cell with index to part
inside_number = False
number = ''

parts = []
for y in range(height):
    for x in range(width):
        cell = engine_schematic[y][x]

        if cell in digits:
            # Number
            inside_number = True
            number += cell
            engine_schematic[y][x] = len(parts)
        elif inside_number:
            parts.append(int(number))
            inside_number = False
            number = ''
    if inside_number:
        parts.append(int(number))
        inside_number = False
        number = ''

# Step 2: Go through and find gears with 2
#   missing parts and calculate gear ratio
for y in range(height):
    for x in range(width):
        cell = engine_schematic[y][x]

        if cell == '*':
            # Gear!
            adjacent_part_values = []
            directions = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]

                # Outside schematic
                if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                    continue

                adjacent_cell = engine_schematic[new_y][new_x]

                if isinstance(adjacent_cell, int) and parts[adjacent_cell] not in adjacent_part_values:
                    adjacent_part_values.append(parts[adjacent_cell])

            # Valid! Calculate gear ratio and add to sum
            if len(adjacent_part_values) == 2:
                sum_of_gear_ratios += adjacent_part_values[0]*adjacent_part_values[1]

print(sum_of_gear_ratios)
