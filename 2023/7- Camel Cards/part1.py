hands = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        hands.append(tuple(line.strip().split()))
# print(hands)

# Ordered
card_order = list('AKQJT98765432')

ordered_hands = {
    'five': [],
    'four': [],
    'full': [],
    'three': [],
    'two': [],
    'one': [],
    'high': []
}
for hand in hands:
    cards = hand[0]
    bid = hand[1]

    # Count occurences of each card in hand
    count = {}
    for card in cards:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1

    # Hands are always 5 cards. Go through rules
    if len(count.keys()) == 1:
        # five
        ordered_hands['five'].append(hand)
    elif len(count.keys()) == 2:
        # four or full
        if 1 in count.values():
            ordered_hands['four'].append(hand)
        else:
            ordered_hands['full'].append(hand)
    elif len(count.keys()) == 3:
        # three or two
        if 3 in count.values():
            ordered_hands['three'].append(hand)
        else:
            ordered_hands['two'].append(hand)
        pass
    elif len(count.keys()) == 4:
        # open
        ordered_hands['one'].append(hand)
    elif len(count.keys()) == 5:
        # high
        ordered_hands['high'].append(hand)


def find_higher_card(c1, c2):
    for i in range(5):
        l1 = card_order.index(c1[0][i])
        l2 = card_order.index(c2[0][i])
        if l1 > l2:
            return c2
        elif l2 > l1:
            return c1


# Sort within groups and add to final order
final_order = []
for hand_type, hand in ordered_hands.items():
    # if empty
    if not hand:
        print('skip:', hand_type)
        continue

    while hand:
        highest_hand = hand[0]
        for i in range(1, len(hand)):
            next_hand = hand[i]
            highest_hand = find_higher_card(highest_hand, next_hand)
        final_order.append(highest_hand)
        hand.remove(highest_hand)
final_order.reverse()
# print(final_order)

# Calculate totalwinnings
total_winnings = 0
for i, hand in enumerate(final_order):
    total_winnings += (i+1)*int(hand[1])

print(total_winnings)
