with open('input.txt', 'r') as file:
    directions = file.readline()

delivered_houses = set()
x = 0
y = 0
for direction in directions:
    delivered_houses.add((x, y))
    match(direction):
        case '>':
            x += 1
        case '<':
            x -= 1
        case '^':
            y -= 1
        case 'v':
            y += 1
print(len(delivered_houses))
