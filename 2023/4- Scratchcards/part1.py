cards = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        cards.append(line.strip().split())

# print(cards)

total = 0
for card in cards:
    matches = 0
    winning_numbers = []
    past_winning = False
    for i in range(2, len(card)):
        if card[i] == '|':
            past_winning = True
            continue

        number = card[i]
        if past_winning:
            if number in winning_numbers:
                matches += 1
        else:
            winning_numbers.append(number)

    if matches == 0:
        # print("Skip")
        continue

    score = 1
    if matches > 1:
        for i in range(matches-1):
            score *= 2

    # print("MATCHES: ", matches)
    # print("SCORE: ", score)
    total += score
print(total)
