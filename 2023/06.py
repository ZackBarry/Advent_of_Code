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

times = [int(x.strip()) for x in input[0].split(' ')[1:] if x]
distances = [int(x.strip()) for x in input[1].split(' ')[1:] if x]



def get_ways(time, distance):
    wins = 0
    for charge_time in range(1, time + 1):
        went = charge_time * (time - charge_time)
        if went > distance:
            wins += 1
    return wins

result = 1

for t, d in zip(times, distances):
    result *= get_ways(t, d)

print(f'Part 1: {result}')

time = ''
distance = ''
for t, d in zip(times, distances):
    time += str(t)
    distance += str(d)

time = int(time)
distance = int(distance)


def wins(time, distance, charge):
    went = charge * (time - charge)
    return went > distance


l = 0
r = time

while l < r:
    m = l + (r - l) // 2
    if not wins(time, distance, m):
        l = m + 1
    else:
        r = m

lowest = l


l = 0
r = time

while l < r:
    m = l + (r - l + 1) // 2
    if not wins(time, distance, m):
        r = m - 1
    else:
        l = m

highest = l - 1

print(f'Part 2: {highest - lowest + 2}')