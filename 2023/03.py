#!/usr/bin/env python3

import sys
from collections import defaultdict

day_number = sys.argv[0][-5:-3]

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    input_file = f'{day_number}-test.txt'
else:
    input_file = f'{day_number}-input.txt'

input = open(input_file).read().splitlines()


# def is_part(row, col, map):
#     for dr in [-1, 0, 1]:
#         for dc in [-1, 0, 1]:
#             val = '.'
#             if 0 <= row + dr < len(map) and 0 <= col + dc < len(map[0]):
#                 val = map[row + dr][col + dc]
#             if not val.isnumeric() and val != '.':
#                 return True
#     return False


# result = 0

# for r, row in enumerate(input):
#     buffer = '0'
#     part = False
#     for c, char in enumerate(row + '.'):
#         if char.isnumeric():
#             buffer += char
#             part = part or is_part(r, c, input)
#         else:
#             result += int(buffer) if part else 0
#             buffer = '0'
#             part = False

# print(result)





def gear_indexes(row, col, map):
    indexes = set()
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            val = '.'
            if 0 <= row + dr < len(map) and 0 <= col + dc < len(map[0]):
                val = map[row + dr][col + dc]
            if val == '*':
                indexes.add((row + dr, col + dc))
    return indexes


gear_map = defaultdict(list)

for r, row in enumerate(input):
    buffer = '0'
    gears = set()
    for c, char in enumerate(row + '.'):
        if char.isnumeric():
            buffer += char
            gears.update(gear_indexes(r, c, input))
        else:
            number = int(buffer)
            if number != 0:
                for g in gears:
                    gear_map[g].append(number)
            buffer = '0'
            gears = set()

result = 0

for parts in gear_map.values():
    if len(parts) == 2:
        result += parts[0] * parts[1]

print(result)