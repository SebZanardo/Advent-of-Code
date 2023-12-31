digits = '1234567890'
worded_digits_replacement = {
    'one': 'o1e',
    'two': 't2',
    'three': 't3e',
    'four': '4',
    'five': '5e',
    'six': '6',
    'seven': '7n',
    'eight': 'e8t',
    'nine': 'n9e',
}

lines = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        lines.append(line.strip())

calibration_sum = 0
for line in lines:
    # Replace worded digits with digits
    for worded_digit in worded_digits_replacement.keys():
        line = line.replace(
            worded_digit, worded_digits_replacement[worded_digit])

    # One pass through to find first and last digit
    first_digit = -1
    second_digit = -1
    i = 0
    while first_digit == -1 or second_digit == -1:
        if first_digit == -1 and line[i] in digits:
            first_digit = int(line[i])
        if second_digit == -1 and line[len(line)-1-i] in digits:
            second_digit = int(line[len(line)-1-i])
        i += 1

    value = first_digit * 10 + second_digit
    calibration_sum += value

print(calibration_sum)
