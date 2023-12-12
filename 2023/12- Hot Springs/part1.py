spring_records = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        record, criteria = line.strip().split()
        criteria = tuple(map(int, criteria.split(',')))
        spring_records.append([record, criteria])
# print(spring_records)

# Constants
UNKNOWN = '?'
OPERATIONAL = '.'
DAMAGED = '#'


def is_valid(record, criteria):
    criteria_index = 0
    group_count = 0

    for char in record:
        if char == UNKNOWN:
            return True
        if char == OPERATIONAL:
            # Then was in a group
            if group_count > 0:
                if criteria_index < len(criteria):
                    if group_count == criteria[criteria_index]:
                        group_count = 0
                        criteria_index += 1
                    else:
                        return False
                else:
                    return False

        if char == DAMAGED:
            group_count += 1

    # Then was in a group
    if group_count > 0:
        if criteria_index < len(criteria):
            if group_count == criteria[criteria_index]:
                group_count = 0
                criteria_index += 1
            else:
                return False
        else:
            return False
    # Met all criteria
    if criteria_index != len(criteria):
        return False
    return True


total_arrangements = 0
for row in spring_records:
    record, criteria = row

    total_on = sum(criteria)
    total_off = len(record) - total_on
    already_on = record.count(DAMAGED)
    already_off = record.count(OPERATIONAL)
    missing_on = total_on - already_on
    missing_off = total_off - already_off
    print(record, criteria)
    print(f"ON | total: {total_on}, already: {already_on}, missing: {missing_on}")
    print(f"OFF | total: {total_off}, already: {already_off}, missing: {missing_off}")

    arrangements = 0
    stack = [(record, missing_on, missing_off)]
    while stack:
        editted = False
        current, mon, moff = stack.pop(0)
        for i, char in enumerate(current):
            if char == UNKNOWN:
                editted = True
                open_record = list(current)
                # Try to add on
                if mon > 0:
                    mon -= 1
                    open_record[i] = DAMAGED
                    tidy = ''.join(open_record)
                    if is_valid(tidy, criteria):
                        stack.append((tidy, mon, moff))
                mon += 1
                # Add off
                if moff > 0:
                    moff -= 1
                    open_record[i] = OPERATIONAL
                    tidy = ''.join(open_record)
                    if is_valid(tidy, criteria):
                        stack.append((tidy, mon, moff))
                break

        if not editted:
            print(current)
            arrangements += 1
    print(arrangements)
    total_arrangements += arrangements
print(total_arrangements)
