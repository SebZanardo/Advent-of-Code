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
                next_map.sort()
                seed_maps.append(next_map)
            next_map = []
            continue

        # Add values to map
        if len(split_line) > 2:  # Not title of map
            # print(line)
            next_map.append(list(map(int, split_line)))
    next_map.sort()
    seed_maps.append(next_map)

# print("seeds: ", seeds)
# print("seed_maps: ", seed_maps)


# Brute force backwards from end values. Seed maps are sorted when parsed!
# To solve I just set start value at different increments until it hit a value

# Create seed pairs
seed_pairs = []
seed_index = 0
while seed_index < len(seeds):
    start = seeds[seed_index]
    end = start + seeds[seed_index+1]

    seed_pairs.append((start, end))
    seed_index += 2

seed_pairs.sort()

# print(seed_pairs)

# Look for start value
start_value = 0
seed_maps.reverse()

lowest_value = -1
found = False
# Reverse seed maps so can work from possible location values
while not found:
    print(start_value)
    value = start_value
    # Backtrack through seed maps
    for seed_map in seed_maps:
        for line in seed_map:
            start = line[0]
            end = line[0] + line[2]

            # Inside range so change value
            if value >= start and value < end:
                difference = value - start
                value = line[1] + difference
                break

    # Check if value after travelled through maps is in one of the seed_map
    #   starting ranges
    for pair in seed_pairs:
        if value >= pair[0] and value < pair[1]:
            lowest_value = start_value
            found = True
            break

    start_value += 1

print(lowest_value)
