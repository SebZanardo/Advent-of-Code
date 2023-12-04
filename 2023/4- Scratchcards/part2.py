cards = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        cards.append(line.strip().split())

# print(cards)

# Step 1: Go through all scratch cards and calculate
#   matches. Save to dict

scratch_card_winnings = {}

for index, card in enumerate(cards):
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
    scratch_card_winnings[index] = matches

# print(scratch_card_winnings)

# Step 2: Go through and calculate number of cards.
#   copies saves count of how many of card[x] to duplicate
scratch_card_count = 0
copy_count = {}

for i in range(len(cards)):
    # 1. Get amount of cards from copies
    copies = 1
    if i in copy_count:
        copies += copy_count[i]

    # 2. Add to scratch_card_count
    scratch_card_count += copies

    # 3. Retrieve matches and create copies of next cards
    for c in range(scratch_card_winnings[i]):
        next_i = i + c + 1
        if next_i in copy_count:
            copy_count[next_i] += copies
        else:
            copy_count[next_i] = copies

    # print(copy_count)
    # print("copies:", copies)
    # print("count:", scratch_card_count)
print(scratch_card_count)
