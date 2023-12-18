dig_plan = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        dig_plan.append(line.strip().split())

# print(dig_plan)

max_left = 0
max_right = 0
max_up = 0
max_down = 0

x = 0
y = 0

for instruction in dig_plan:
    direction, length, hex = instruction
    length = int(length)

    match(direction):
        case 'L':
            x -= length
        case 'R':
            x += length
        case 'U':
            y -= length
        case 'D':
            y += length
    if x <= max_left:
        max_left = x
    if x >= max_right:
        max_right = x
    if y <= max_up:
        max_up = y
    if y >= max_down:
        max_down = y

start_x = x - max_left
start_y = y - max_up

print(max_left, max_right, max_up, max_down)
width = abs(max_left) + abs(max_right) + 1
height = abs(max_down) + abs(max_up) + 1
dig_site = [[0 for x in range(width)] for y in range(height)]

x = start_x
y = start_y
edge = 0
for instruction in dig_plan:
    direction, length, hex = instruction
    length = int(length)

    new_x = x
    new_y = y
    match(direction):
        case 'L':
            new_x -= length
        case 'R':
            new_x += length
        case 'U':
            new_y -= length
        case 'D':
            new_y += length

    if new_x > x:
        for i in range(x, new_x+1):
            dig_site[new_y][i] = 1
    else:
        for i in range(new_x, x+1):
            dig_site[new_y][i] = 1
    if new_y > y:
        for j in range(y, new_y+1):
            dig_site[j][new_x] = 1
    else:
        for j in range(new_y, y+1):
            dig_site[j][new_x] = 1
    edge += abs(new_x - x) + abs(new_y - y)
    x = new_x
    y = new_y


start_positions = []
for x in range(width):
    if dig_site[0][x] == 0:
        start_positions.append((x, 0))
    if dig_site[height-1][x] == 0:
        start_positions.append((x, height-1))
for y in range(1, height-1):
    if dig_site[y][0] == 0:
        start_positions.append((0, y))
    if dig_site[y][width-1] == 0:
        start_positions.append((width-1, y))

outside = 0
stack = start_positions
visited = set()
while stack:
    x, y = stack.pop(0)
    for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
            continue
        if dig_site[new_y][new_x] == 1:
            continue
        if (new_x, new_y) not in stack and (new_x, new_y) not in visited:
            stack.append((new_x, new_y))
            visited.add((new_x, new_y))
            outside += 1

print(outside)

for row in dig_site:
    print(''.join(map(str, row)))

volume = width*height - outside
print(volume)
