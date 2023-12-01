with open('input.txt', 'r') as file:
    directions = file.readline()

floor = 0
for char in directions:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
print(floor)
