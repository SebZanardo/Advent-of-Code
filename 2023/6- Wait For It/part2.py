with open('input.txt', 'r') as file:
    times = file.readline().split()[1:]
    distances = file.readline().split()[1:]

max_time = int(''.join(times))
record = int(''.join(distances))

winning_ways = 0
inside = False  # Variable used to exit loop early
for hold in range(1, max_time):
    distance_travelled = (max_time - hold) * hold
    if distance_travelled > record:
        winning_ways += 1
        inside = True
    elif inside:
        break

# There will always be a way to win, no need to worry about
#   edge case of multiplying by zero
print(winning_ways)
