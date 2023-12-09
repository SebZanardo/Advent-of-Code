import math


nodes = {}
start_nodes = []
with open('input.txt', 'r') as file:
    directions = file.readline().strip()
    for line in file.readlines():
        line = line.strip().split()
        if not line:
            continue
        left = line[2][1:-1]
        right = line[3][:-1]
        nodes[line[0]] = (left, right)
        start_nodes.append(line[0])

# Count how many ghosts
ghost_nodes = []
for node in start_nodes:
    if node[-1] == 'A':
        ghost_nodes.append(node)
print("# of ghosts", len(ghost_nodes))

# Simulating moves takes too long.
# All ghosts travel to unique target node!
# Ghosts distance to target node from start position is same as loop distance.
loop_length = []
for ghost in ghost_nodes:
    current = ghost
    print(current)
    # All ghosts steps to reach target
    steps = 0
    looped = False
    while not looped:
        for direction in directions:
            if direction == 'L':
                current = nodes[current][0]
            elif direction == 'R':
                current = nodes[current][1]
            steps += 1
            if current[-1] == 'Z':
                looped = True
                break
    loop_length.append(steps)

print(loop_length)

# Answer is LCM *not all loop lengths multiplied
lcm = loop_length[0]
for i in range(1, len(loop_length)):
    lcm = math.lcm(lcm, loop_length[i])
print(lcm)
