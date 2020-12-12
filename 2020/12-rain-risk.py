import math

input = open('2020/12-input.txt').read().splitlines()

input = [[x[0], int(x[1:])] for x in input]

# part 1

location = [0, 0]
bearing = 0
for dir, amnt in input:
    if dir == 'L':
        bearing += amnt
    elif dir == 'R':
        bearing -= amnt
    elif dir == 'E':
        location[0] += amnt
    elif dir == 'N':
        location[1] += amnt
    elif dir == 'W':
        location[0] -= amnt
    elif dir == 'S':
        location[1] -= amnt
    elif dir == 'F':
        location[0] += amnt * math.cos(math.radians(bearing))
        location[1] += amnt * math.sin(math.radians(bearing))
    else:
        print(f'Bad instruction {dir}.')
        break
    bearing = bearing % 360

print(f'Manhattan distance: {abs(location[0]) + abs(location[1])}')

# part 2

def get_angle(x, y):
    atan_result = math.atan2(y, x)
    if atan_result < 0:
        atan_result += 2 * math.pi
    return atan_result


ship = [0, 0]
wayp = [10, 1]

for dir, amnt in input:
    if dir == 'N':
        wayp[1] += amnt
    elif dir == 'S':
        wayp[1] -= amnt
    elif dir == 'E':
        wayp[0] += amnt
    elif dir == 'W':
        wayp[0] -= amnt
    elif dir in ['L', 'R', 'F']:
        relative_x = wayp[0] - ship[0]
        relative_y = wayp[1] - ship[1]
        if dir in ['L', 'R']:
            dist_to_ship = math.sqrt(math.pow(relative_x, 2) + math.pow(relative_y, 2))
            print(relative_x, relative_y)
            current_angle = math.degrees(get_angle(relative_x, relative_y))
            new_angle = current_angle + amnt if dir == 'L' else current_angle - amnt
            new_x = dist_to_ship * math.cos(math.radians(new_angle)) + ship[0]
            new_y = dist_to_ship * math.sin(math.radians(new_angle)) + ship[1]
            wayp = [new_x, new_y]
        else:
            ship[0] += (amnt * relative_x)
            ship[1] += (amnt * relative_y)
            wayp[0] = ship[0] + relative_x
            wayp[1] = ship[1] + relative_y
    else:
        print(f'Bad direction {dir}.')
        break

print(f'Manhattan distance: {abs(ship[0]) + abs(ship[1])}')