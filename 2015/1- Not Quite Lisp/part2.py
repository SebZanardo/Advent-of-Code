with open('input.txt', 'r') as file:
    directions = file.readline()

index = 1
floor = 0
for char in directions:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor < 0:
        break
    index += 1
print(index)
