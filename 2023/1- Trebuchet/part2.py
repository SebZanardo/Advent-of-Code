digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
spelled_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


lines = []
with open('input2.txt', 'r') as file:
    for line in file.readlines():
        lines.append(line.strip())

calibration_sum = 0
for line in lines:
    found_digits = []
    for index, char in enumerate(line):
        if char in digits:
            found_digits.append(int(char))
        for spelled_digit in spelled_digits:
            valid = True
            for i in range(len(spelled_digit)):
                if index+i >= len(line):
                    valid = False
                    break
                if line[index+i] != spelled_digit[i]:
                    valid = False
                    break
            if valid:
                found_digits.append(int(digits[spelled_digits.index(spelled_digit)]))

    first_digit = found_digits[0]
    second_digit = found_digits[-1]

    value = first_digit * 10 + second_digit
    print(value)
    calibration_sum += value

print(calibration_sum)
