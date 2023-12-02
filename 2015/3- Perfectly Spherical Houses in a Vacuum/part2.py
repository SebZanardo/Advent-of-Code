with open('input.txt', 'r') as file:
    directions = file.readline()

delivered_houses = set()
sx = 0
sy = 0
rx = 0
ry = 0
i = 0
for direction in directions:
    if i % 2 == 0:
        delivered_houses.add((rx, ry))
        match(direction):
            case '>':
                sx += 1
            case '<':
                sx -= 1
            case '^':
                sy -= 1
            case 'v':
                sy += 1
    else:
        delivered_houses.add((sx, sy))
        match(direction):
            case '>':
                rx += 1
            case '<':
                rx -= 1
            case '^':
                ry -= 1
            case 'v':
                ry += 1
    i += 1
print(len(delivered_houses))
