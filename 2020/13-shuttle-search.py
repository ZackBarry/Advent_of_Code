import sympy
import numpy as np

input = open('2020/13-input.txt').read().splitlines()

# part one

now = int(input[0])
buses = [int(x) for x in input[1].split(',') if x != 'x']

time_waiting = {}
for bus_id in buses:
    time_waiting[bus_id] = bus_id - now % bus_id

for k, v in time_waiting.items():
    if v == min(list(time_waiting.values())):
        print(f'answer = {k * v}')

# part two

loop_duration = buses

all_buses = input[1].split(',')
desired_offset = [all_buses.index(str(bus_id)) for bus_id in buses]

current_offset = list(np.repeat(0, len(desired_offset)))
rounds = 0
complete = False

while not complete and rounds < 10000000:
    rounds += 1
    current_offset[0] += loop_duration[0]
    for bus_index in np.arange(1, len(current_offset)):
        if bus_index > 1:
            print(f'success round {rounds}')
        #print(f'{rounds}, {bus_index}')
        current_value = current_offset[bus_index]
        increment = loop_duration[bus_index]
        desired_diff = desired_offset[bus_index]
        current_diff = current_offset[bus_index] - current_offset[0]
        if current_diff < desired_diff:
            adjustment = desired_diff - current_diff
            current_offset[bus_index] += (int(adjustment / increment) + 1) * increment
        if current_offset[bus_index] != desired_diff:
           # print(current_offset)
            break
    current_offset = [offset - loop_duration[0] for offset in current_offset]
    if current_offset == desired_offset:
        complete = True
        print(f'earliest time is {rounds * loop_duration[0]}')


    for current, schedule in zip(state[1: ], offsets[1: ]):
        diff_from_anchor = current - state[0]
        while diff_from_anchor < schedule[1]:

    diff = min(state) - state[0]
    if diff < max(offsets):



rows = []
b = [0]

for i, r in enumerate(offsets[1:]):
    this_row = list(np.repeat(0, len(buses)))
    this_row[0] = offsets[0][0]
    this_row[i+1] = r[0]
    b += [-r[1]]
    rows += [this_row]

a_matrix = sympy.Matrix(rows)
b_matrix = sympy.Matrix(b)
symbols = [sympy.symbols(f'b{records[1]}') for records in offsets]
sympy.linsolve((a_matrix, b_matrix), symbols)
