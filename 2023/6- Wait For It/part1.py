with open('input.txt', 'r') as file:
    times = list(map(int, file.readline().split()[1:]))
    distances = list(map(int, file.readline().split()[1:]))

print(times)
print(distances)

multiplied_record = 0
for race in range(len(times)):
    winning_ways = 0
    inside = False  # Variable used to exit loop early
    max_time = times[race]
    record = distances[race]
    for hold in range(1, max_time):
        distance_travelled = (max_time - hold) * hold
        if distance_travelled > record:
            winning_ways += 1
            inside = True
        elif inside:
            break

    # print("w", winning_ways)

    # There will always be a way to win, no need to worry about
    #   edge case of multiplying by zero
    if multiplied_record == 0:
        multiplied_record = winning_ways
    else:
        multiplied_record *= winning_ways

print(multiplied_record)
