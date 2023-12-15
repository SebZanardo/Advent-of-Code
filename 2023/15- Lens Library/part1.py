with open('input.txt', 'r') as file:
    steps = file.readline().strip().split(',')
# print(steps)


def perform_hash(string):
    current_value = 0
    for char in string:
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256
    return current_value


total = 0
for step in steps:
    step_value = perform_hash(step)
    print(step_value)
    total += step_value
print(total)
