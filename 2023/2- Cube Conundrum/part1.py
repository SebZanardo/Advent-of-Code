digits = '0123456789'
games = []
# Games are ordered in input
with open('input.txt', 'r') as file:
    for line in file.readlines():
        highest_red = 0
        highest_green = 0
        highest_blue = 0

        value = ''
        inside = False
        for i, char in enumerate(line):
            if value and not inside:
                # Then end of number
                int_value = int(value)
                value = ''
                if line[i] == 'r' and highest_red < int_value:
                    highest_red = int_value
                if line[i] == 'g' and highest_green < int_value:
                    highest_green = int_value
                if line[i] == 'b' and highest_blue < int_value:
                    highest_blue = int_value
            if char not in digits:
                inside = False
                continue
            value += char
            inside = True
        games.append((highest_red, highest_green, highest_blue))
print(games)

max_red = 12
max_green = 13
max_blue = 14

total_id = 0
for id, game in enumerate(games):
    if game[0] > max_red or game[1] > max_green or game[2] > max_blue:
        continue
    total_id += id + 1
print(total_id)
