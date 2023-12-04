digits = '0123456789'

engine_schematic = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        engine_schematic.append(list(line.strip()))
# print(engine_schematic)

# All rows are same width
width = len(engine_schematic[0])
height = len(engine_schematic)

sum_of_parts = 0

inside_number = False
adjacent = False
number = ''

for y in range(height):
    for x in range(width):
        cell = engine_schematic[y][x]

        if cell not in digits and inside_number:
            if adjacent:
                # Then add part number
                sum_of_parts += int(number)
            inside_number = False
            adjacent = False
            number = ''
        elif cell in digits:
            # Number
            inside_number = True
            number += cell

            # Check if adjacent to part (diag included)
            if not adjacent:
                directions = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
                for direction in directions:
                    new_x = x + direction[0]
                    new_y = y + direction[1]

                    # Outside schematic
                    if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                        continue

                    adjacent_cell = engine_schematic[new_y][new_x]

                    if adjacent_cell not in digits and adjacent_cell != '.':
                        adjacent = True
                        break
    if inside_number:
        if adjacent:
            # Then add part number
            sum_of_parts += int(number)
        inside_number = False
        adjacent = False
        number = ''

print(sum_of_parts)
