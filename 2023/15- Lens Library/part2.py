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


def remove_duplicate_lens(box, label):
    for i, val in enumerate(box):
        if label == val[0]:
            box.pop(i)
            break


def display_boxes(boxes):
    for i, box in enumerate(boxes):
        if not box:
            continue
        print(i, box)
    print()


boxes = [[] for _ in range(256)]
for step in steps:
    # Hash the label -> to find box number

    # *NOTE* Label can be any length! Not only 2 characters >:(
    end_of_label = 0
    for c in step:
        if c == '-' or c == '=':
            break
        end_of_label += 1

    label = step[:end_of_label]
    box_number = perform_hash(label)
    operation = step[end_of_label]

    if operation == '-':
        remove_duplicate_lens(boxes[box_number], label)
    elif operation == '=':
        position = int(step[end_of_label+1])

        found = False
        # Replace
        for i, val in enumerate(boxes[box_number]):
            if label == val[0]:
                boxes[box_number][i] = (label, position)
                found = True
                break

        # Add to end
        if not found:
            boxes[box_number].append((label, position))
display_boxes(boxes)


# Calculate total
total_power = 0
for i, box in enumerate(boxes):
    if not box:
        continue
    for j, lens in enumerate(box):
        lens_power = (i + 1) * (j + 1) * lens[1]
        # print(lens_power)
        total_power += lens_power

print(total_power)
