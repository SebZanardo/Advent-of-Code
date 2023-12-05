seeds = []
seed_maps = []  # 3Dimensional array
with open('input.txt', 'r') as file:
    next_map = []
    for i, line in enumerate(file.readlines()):
        split_line = line.strip().split()
        # Read seed values
        if i == 0:
            seeds = list(map(int, split_line[1:]))
            continue

        # If empty line, clear next map
        if not split_line:
            if next_map:
                seed_maps.append(next_map)
            next_map = []
            continue

        # Add values to map
        if len(split_line) > 2:  # Not title of map
            next_map.append(list(map(int, split_line)))
    seed_maps.append(next_map)

# print("seeds: ", seeds)
# print("seed_maps: ", seed_maps)

lowest_result = -1
for seed in seeds:
    value = seed
    for seed_map in seed_maps:
        found = False
        for line in seed_map:
            # Does the seed fit within the range?
            if value >= line[1] and value < line[1]+line[2]:
                difference = value - line[1]
                value = line[0] + difference
                found = True
                break
        if not found:
            # value remains the same
            pass
        # print(f"{seed}-> {value}")

    # print("location:", value)
    if lowest_result == -1 or value < lowest_result:
        lowest_result = value

print(lowest_result)
