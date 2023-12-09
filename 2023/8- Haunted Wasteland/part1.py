nodes = {}
with open('input.txt', 'r') as file:
    directions = file.readline().strip()
    for line in file.readlines():
        line = line.strip().split()
        if not line:
            continue
        left = line[2][1:-1]
        right = line[3][:-1]
        nodes[line[0]] = (left, right)
# print(nodes)

# Use directions until on 'ZZZ'
target = 'ZZZ'
current_node = 'AAA'
steps = 0

while current_node != target:
    for direction in directions:
        if direction == 'L':
            current_node = nodes[current_node][0]
        elif direction == 'R':
            current_node = nodes[current_node][1]
        steps += 1
print(steps)
