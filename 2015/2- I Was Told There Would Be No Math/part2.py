dimensions = []
with open('input2.txt', 'r') as file:
    for line in file.readlines():
        lengths = list(map(int, line.strip().split('x')))
        dimensions.append(lengths)

total = 0
for dimension in dimensions:
    ribbon_length = dimension[0]*dimension[1]*dimension[2]
    largest = max(dimension)
    dimension.remove(largest)
    present_length = sum(dimension)*2
    needed_length = present_length + ribbon_length
    print(needed_length)
    total += needed_length
print(total)
