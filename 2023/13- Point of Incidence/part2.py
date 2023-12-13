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


def count_differences(p1, p2):
    differences = 0
    for c in range(len(p1)):
        if p1[c] != p2[c]:
            differences += 1
    return differences


def find_reflection(pattern):
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            if confirm_match(pattern, i, 0):
                return i + 1
        else:
            differences = count_differences(pattern[i], pattern[i+1])

            # If only one difference then try to confirm.
            # Note: passed 1 in as difference so function knows a difference
            #   has already been fixed
            if differences == 1:
                if confirm_match(pattern, i, 1):
                    return i + 1
    return -1


def confirm_match(pattern, i, differences):
    # Two pointers, look until either are outside of pattern
    first = i-1
    second = i+2
    while second < len(pattern) and first >= 0:
        if pattern[first] != pattern[second]:
            if differences == 1:
                return False
            else:
                diff = count_differences(pattern[first], pattern[second])

                if diff == 1:
                    differences += 1
                else:
                    return False
        first -= 1
        second += 1

    # If didn't fix smudge then not match we are looking for
    if differences == 0:
        return False

    return True


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
