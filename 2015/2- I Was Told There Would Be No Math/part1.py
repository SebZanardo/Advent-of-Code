dimensions = []
with open('input1.txt', 'r') as file:
    for line in file.readlines():
        lengths = list(map(int, line.strip().split('x')))
        dimensions.append(lengths)

total = 0
for dimension in dimensions:
    sides = [dimension[0]*dimension[1],
             dimension[1]*dimension[2],
             dimension[2]*dimension[0]]
    surface_area = sum(sides)*2
    smallest_side = min(sides)
    needed_paper = surface_area + smallest_side
    print(needed_paper)
    total += needed_paper
print(total)
