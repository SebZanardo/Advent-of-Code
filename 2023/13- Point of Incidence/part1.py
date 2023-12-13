patterns = []
with open('input.txt', 'r') as file:
    pattern = []
    for line in file.readlines():
        line = list(line.strip())
        if not line:
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)

print(patterns)


def display_pattern(pattern):
    for row in pattern:
        print(' '.join(row))
    print()


def find_reflection(pattern):
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            # Confirm match
            confirmed = True
            first = i-1
            second = i+2
            while second < len(pattern) and first >= 0:
                if pattern[first] != pattern[second]:
                    confirmed = False
                    break
                first -= 1
                second += 1
            if confirmed:
                return i + 1
    return -1


total = 0
for pattern in patterns:
    # Check for horizontal reflection
    horizontal_reflection = find_reflection(pattern)

    if horizontal_reflection != -1:
        display_pattern(pattern)
        print(horizontal_reflection)
        total += 100 * horizontal_reflection
        continue

    # Rotate pattern to check for vertical! (Easier I think)
    v_pattern = []
    for x in range(len(pattern[0])):
        row = []
        for y in range(len(pattern)):
            row.append(pattern[y][x])
        v_pattern.append(row)
    vertical_reflection = find_reflection(v_pattern)
    display_pattern(v_pattern)
    print(vertical_reflection)
    total += vertical_reflection
print(total)
