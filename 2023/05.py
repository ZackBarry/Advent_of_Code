#!/usr/bin/env python3

import sys
from collections import defaultdict
import math

day_number = sys.argv[0][-5:-3]

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    input_file = f'{day_number}-test.txt'
else:
    input_file = f'{day_number}-input.txt'

input = open(input_file).read().splitlines()

seeds = [int(x) for x in input[0].split(' ')[1:]]

# i = 3

# maps = []
# curr_map = {}

# while i < len(input):
#     if len(input[i]) != 0:
#         line = input[i]
#         destination = int(line.split(' ')[0])
#         source = int(line.split(' ')[1])
#         length = int(line.split(' ')[2])
#         for s in range(length):
#             curr_map[source + s] = destination + s
#         i += 1
#     else:
#         maps.append(curr_map)
#         curr_map = {}
#         i += 2

# maps.append(curr_map)

# def get_location(seed, maps):
#     for m in maps:
#         seed = m.get(seed, seed)
#     return seed

# print(min([get_location(s, maps) for s in seeds]))

i = 3

maps = []
curr_map = []

while i < len(input):
    if len(input[i]) != 0:
        line = input[i]
        destination = int(line.split(' ')[0])
        source = int(line.split(' ')[1])
        length = int(line.split(' ')[2])
        curr_map.append([source, destination, length])
        i += 1
    else:
        maps.append(curr_map)
        print(curr_map)
        curr_map = []
        i += 2

maps.append(curr_map)


def get_location(seed, maps):
    for m in maps:
        new_seed = seed
        for l in m:
            source = l[0]
            destination = l[1]
            length = l[2]
            if source <= seed < source + length:
                new_seed = destination + (seed - source)
        seed = new_seed

    return seed

print(min([get_location(s, maps) for s in seeds]))


new_seeds = []

j = 0
while j < len(seeds):
    new_seeds += list(range(seeds[j], seeds[j] + seeds[j + 1]))
    j += 2

print(min([get_location(s, maps) for s in new_seeds]))