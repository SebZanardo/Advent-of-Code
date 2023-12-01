digits = '1234567890'

lines = []
with open('input1.txt', 'r') as file:
    for line in file.readlines():
        lines.append(line.strip())

calibration_sum = 0

for line in lines:
    first_digit = -1
    second_digit = -1
    i = 0
    while first_digit == -1 or second_digit == -1:
        if line[i] in digits and first_digit == -1:
            first_digit = int(line[i])
        if line[len(line)-1-i] in digits and second_digit == -1:
            second_digit = int(line[len(line)-1-i])
        i += 1
    value = first_digit * 10 + second_digit
    # print(value)
    calibration_sum += value

print(calibration_sum)
