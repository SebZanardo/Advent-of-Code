patterns = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        patterns.append(list(map(int, line.strip().split())))
print(patterns)


def calculate_differences(sequence):
    difference = []
    for i in range(len(sequence)-1):
        n1 = sequence[i]
        n2 = sequence[i+1]
        difference.append(n2-n1)
    return difference


extrapolated_sum = 0
for pattern in patterns:
    sequences = [pattern]
    next_sequence = calculate_differences(pattern)

    while True:
        all_same = True
        for i in range(len(next_sequence)-2):
            if next_sequence[i] != next_sequence[i+1]:
                all_same = False
                break

        sequences.append(next_sequence)
        if not all_same:
            next_sequence = calculate_differences(next_sequence)
        else:
            break
    print(sequences)

    # Extrapolate previous value in sequence
    value = sequences[-1][0]
    for i in range(len(sequences)-2, -1, -1):
        value = sequences[i][0] - value
    print(value)

    extrapolated_sum += value
print(extrapolated_sum)
