instructions = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        instructions.append(line.strip().split())
# print(instructions)


def get_value(string, signals):
    is_digit = False
    for c in string:
        if c in '0123456789':
            is_digit = True
            break
    if is_digit:
        return int(string)
    elif string in signals:
        return signals[string]
    else:
        return None


def to_16bit(value):
    binary = bin(value)[2:]
    return (16-len(binary))*'0' + binary


def write_value(signals, key, value):
    # Can't overwrite existing signal
    if key in signals:
        return
    signals[key] = value


def solve(signals, answer_key):
    instructions_copy = instructions.copy()
    while instructions_copy:
        instruction = instructions_copy.pop(0)
        instruction_length = len(instruction)
        # A operation B -> c
        if instruction_length == 5:
            a = get_value(instruction[0], signals)
            b = get_value(instruction[2], signals)
            # Don't have all information
            if a is None or b is None:
                instructions_copy.append(instruction)
                continue

            operator = instruction[1]

            if operator == 'AND':
                a = to_16bit(a)
                b = to_16bit(b)
                value = ''
                for i in range(16):
                    if a[i] == '1' and b[i] == '1':
                        value += '1'
                    else:
                        value += '0'

            if operator == 'OR':
                a = to_16bit(a)
                b = to_16bit(b)
                value = ''
                for i in range(16):
                    if a[i] == '1' or b[i] == '1':
                        value += '1'
                    else:
                        value += '0'

            if operator == 'LSHIFT':
                a = to_16bit(a)
                value = a[b:]
                value = value + '0'*b

            if operator == 'RSHIFT':
                a = to_16bit(a)
                value = a[:-b]
                value = '0'*b + value

            write_value(signals, instruction[4], int(value, 2))

        # NOT A -> B
        elif instruction_length == 4:
            value = get_value(instruction[1], signals)
            # Don't have all information
            if value is None:
                instructions_copy.append(instruction)
                continue
            binary = bin(value)[2:]
            binary = (16-len(binary))*'0' + binary
            inverse = ''
            for i in binary:
                inverse += '1' if i == '0' else '0'
            write_value(signals, instruction[3], int(inverse, 2))

        # A -> B
        else:
            value = get_value(instruction[0], signals)
            # Don't have all information
            if value is None:
                instructions_copy.append(instruction)
                continue
            write_value(signals, instruction[2], value)
    return signals[answer_key]


a = solve({}, 'a')
print('a =', a)
print(solve({'b': a}, 'a'))
