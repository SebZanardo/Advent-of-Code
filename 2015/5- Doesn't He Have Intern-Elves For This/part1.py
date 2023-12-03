vowels = 'aeiou'
disallowed_substrings = ['ab', 'cd', 'pq', 'xy']

strings = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        strings.append(line.strip())

# print(strings)

nice = 0
for string in strings:
    # Check for disallowed substrings
    valid = True
    for sub_string in disallowed_substrings:
        if sub_string in string:
            valid = False

    if not valid:
        continue

    # Count vowels and check for double letters
    vowel_count = 0
    double_letter = False
    last_char = ''
    for char in string:
        if char in vowels:
            vowel_count += 1
        if last_char and char == last_char:
            double_letter = True
        last_char = char

    if vowel_count < 3 or not double_letter:
        continue

    print(string)
    nice += 1

print(nice)
