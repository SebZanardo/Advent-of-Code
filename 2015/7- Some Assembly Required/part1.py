instructions = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        instructions.append(line.strip().split())
print(instructions)


def get_value(string):
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


signals = {}
while instructions:
    instruction = instructions.pop(0)
    target_wire = instruction[-1]
    instruction_length = len(instruction)
    # A operation B -> c
    if instruction_length == 5:
        a = get_value(instruction[0])
        b = get_value(instruction[2])
        # Don't have all information
        if a is None or b is None:
            print("Skipped:", instruction)
            instructions.append(instruction)
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
            signals[instruction[4]] = int(value, 2)

        if operator == 'OR':
            a = to_16bit(a)
            b = to_16bit(b)
            value = ''
            for i in range(16):
                if a[i] == '1' or b[i] == '1':
                    value += '1'
                else:
                    value += '0'
            signals[instruction[4]] = int(value, 2)

        if operator == 'LSHIFT':
            a = to_16bit(a)
            value = a[b:]
            value = value + '0'*b
            signals[instruction[4]] = int(value, 2)

        if operator == 'RSHIFT':
            a = to_16bit(a)
            value = a[:-b]
            value = '0'*b + value
            signals[instruction[4]] = int(value, 2)

    # NOT A -> B
    elif instruction_length == 4:
        value = get_value(instruction[1])
        # Don't have all information
        if value is None:
            print("Skipped:", instruction)
            instructions.append(instruction)
            continue
        binary = bin(value)[2:]
        binary = (16-len(binary))*'0' + binary
        inverse = ''
        for i in binary:
            inverse += '1' if i == '0' else '0'
        signals[instruction[3]] = int(inverse, 2)
    # A -> B
    else:
        value = get_value(instruction[0])
        # Don't have all information
        if value is None:
            print("Skipped:", instruction)
            instructions.append(instruction)
            continue
        signals[instruction[2]] = value
print(signals)
print(signals['a'])
