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


card_matches = dict()

for i, l in enumerate(input):
    parts = l.split(' | ')
    card = parts[0].split(' ')
    mine = parts[1].split(' ')

    card_numbers = [int(x.strip()) for x in card if x.strip().isnumeric()]
    mine_numbers = [int(x.strip()) for x in mine if x.strip().isnumeric()]

    matches = len([x for x in mine_numbers if x in card_numbers])

    card_matches[i] = matches


print(f'Part 1: {sum([math.pow(2, x - 1) for x in card_matches.values() if x != 0])}')

nested_matches = dict()

for i in range(len(input) - 1, -1, -1):
    value = 0
    matches = card_matches[i]

    for j in range(matches):
        value += nested_matches[i + j + 1]

    nested_matches[i] = value + 1

print(f'Part 2: {sum(nested_matches.values())}')