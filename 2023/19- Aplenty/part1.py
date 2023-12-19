workflow = {}
parts = []


def parse_workflow(string):
    label = ''
    for i, c in enumerate(string):
        if c == '{':
            break
        label += c

    rules = string[i+1:-1].split(',')
    tidy_rules = []
    for rule in rules:
        # Operator
        if ':' in rule:
            rule = rule.replace('<', ' < ')
            rule = rule.replace('>', ' > ')
            rule = rule.replace(':', ' ')
            tidy_rule = rule.split(' ')
            tidy_rule[2] = int(tidy_rule[2])
        else:
            tidy_rule = [rule]
        tidy_rules.append(tidy_rule)

    workflow[label] = tidy_rules


def parse_part(string):
    part = string[1:-1]
    part = part.replace('x=', '')
    part = part.replace('m=', '')
    part = part.replace('a=', '')
    part = part.replace('s=', '')
    parts.append(list(map(int, part.split(','))))


with open('input.txt', 'r') as file:
    is_ratings = False
    for line in file.readlines():
        line = line.strip()
        if not line:
            is_ratings = True
            continue

        if not is_ratings:
            parse_workflow(line)

        else:
            parse_part(line)

# print(workflow)
# print(parts)

ACCEPTED = 'A'
REJECTED = 'R'

accepted = 0
accepted_part_sum = 0
for part in parts:
    finished = False
    current = 'in'
    while not finished:
        current_rule = workflow[current]

        for rule in current_rule:
            meets_rule = False
            # Has operator
            if len(rule) > 1:
                category, operator, value, destination = rule
                part_value = 0
                if category == 'x':
                    part_value = part[0]
                elif category == 'm':
                    part_value = part[1]
                elif category == 'a':
                    part_value = part[2]
                elif category == 's':
                    part_value = part[3]

                if operator == '<':
                    meets_rule = part_value < value
                elif operator == '>':
                    meets_rule = part_value > value
            else:
                meets_rule = True
                destination = rule[0]

            # print(part, current, rule)
            # print(meets_rule)
            if meets_rule:
                if destination == ACCEPTED:
                    accepted += 1
                    accepted_part_sum += sum(part)
                    finished = True
                    break
                if destination == REJECTED:
                    finished = True
                    break
                current = destination
                break

print(accepted)
print(accepted_part_sum)
