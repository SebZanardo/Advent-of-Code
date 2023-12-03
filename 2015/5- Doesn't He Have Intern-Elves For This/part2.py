strings = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        strings.append(line.strip())


nice = 0
for string in strings:
    # Find if has duplicate pair
    duplicate_pair = False
    pairs = set()
    last_pair = ''
    for i in range(len(string)-1):
        pair = string[i] + string[i+1]
        if last_pair and pair == last_pair:
            last_pair = ''
            continue
        if pair in pairs:
            duplicate_pair = True
            break
        last_pair = pair
        pairs.add(pair)

    if not duplicate_pair:
        continue

    # Find if has repeated letter with one space gap
    repeated_letter = False
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            repeated_letter = True
            break

    if not repeated_letter:
        continue

    print(string)
    nice += 1

print(nice)
