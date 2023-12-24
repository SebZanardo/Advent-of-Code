hail_stones = []
# NOTE: Need to manually set bound for test cases
LOWER_BOUND = 200000000000000
HIGHER_BOUND = 400000000000000

with open('input.txt', 'r') as file:
    for line in file.readlines():
        short_line = line.replace(" ", "")
        position, velocity = short_line.split("@")
        position = tuple(map(int, position.split(',')))
        velocity = tuple(map(int, velocity.split(',')))
        hail_stones.append((position, velocity))

# print(hail_stones)


def into_general_form(position, velocity):
    # Disregard Z-Axis for part1
    a = 1
    b = velocity[0]/velocity[1]
    c = (position[0]/-velocity[0]*velocity[1]+position[1])*b
    return a, b, c


def in_past(ox, oy, px, py, vx, vy):
    nx = vx/abs(vx)
    ny = vy/abs(vy)

    return (px > ox and nx < 0) or (px < ox and nx > 0) or (-py > oy and ny < 0) or (-py < oy and ny > 0)


count = 0
for i in range(len(hail_stones)):
    # 1. Find hailstones x, y equation in general format
    #   e.g ax + by + c = 0
    pos1, vel1 = hail_stones[i]
    a1, b1, c1 = into_general_form(pos1, vel1)
    for j in range(i+1, len(hail_stones)):
        pos2, vel2 = hail_stones[j]
        a2, b2, c2 = into_general_form(pos2, vel2)

        print('-'*10)
        print(a1, b1, c1)
        print(a2, b2, c2)

        # 2. Calculate point of intersection
        #   Note: a1 and a2 are always 1 so not needed

        # Parallel so never intersects
        if b2-b1 == 0:
            print('parallel')
            continue

        px = (b1*c2 - b2*c1)/(b2-b1)
        py = (c1-c2)/(b2-b1)

        print("px:", px, py)

        past = False
        if in_past(pos1[0], pos1[1], px, py, vel1[0], vel1[1]):
            print("a in past")
            past = True
        if in_past(pos2[0], pos2[1], px, py, vel2[0], vel2[1]):
            print("b in past")
            past = True

        if past:
            continue

        if px < LOWER_BOUND or px > HIGHER_BOUND or py > -LOWER_BOUND or py < -HIGHER_BOUND:
            print("outside test area")
            continue
        count += 1
print(count)
