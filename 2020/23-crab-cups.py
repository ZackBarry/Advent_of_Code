from copy import deepcopy

# part 1

input = '418976235'

input = [int(x) for x in input]

current_cup = input[0]

for i in range(0, 100):
    current_index = input.index(current_cup)
    move_cups = []
    for j in range(0, 3):
        move_index = (input.index(current_cup) + 1) % len(input)
        move_cups += [input.pop(move_index)]
    sorted_input = sorted(deepcopy(input))
    destination_cup = sorted_input[sorted_input.index(current_cup) - 1]
    destination_index = input.index(destination_cup)
    input = input[0:destination_index+1] + move_cups + input[destination_index+1:]
    current_cup = input[(input.index(current_cup) + 1) % len(input)]

output = input[input.index(1)+1:] + input[:input.index(1)]
output = [str(x) for x in output]
print(''.join(output))

# part 2

input = '418976235'

input = [int(x) for x in input]

input += list(range(len(input), 1000000+1))

current_cup = input[0]

for i in range(0, 10000000):
    if i % 1000000 == 0:
        print(time.strftime('%H:%M:%S'))
    current_index = input.index(current_cup)
    move_cups = []
    for j in range(0, 3):
        move_index = (input.index(current_cup) + 1) % len(input)
        move_cups += [input.pop(move_index)]
    sorted_input = sorted(deepcopy(input))
    destination_cup = sorted_input[sorted_input.index(current_cup) - 1]
    destination_index = input.index(destination_cup)
    input = input[0:destination_index+1] + move_cups + input[destination_index+1:]
    current_cup = input[(input.index(current_cup) + 1) % len(input)]

cup_1_index = input.index(1)
first_cup = input[(cup_1_index + 1) % len(input)]
second_cup = input[(cup_1_index + 2) % len(input)]
print(f'{first_cup * second_cup}')