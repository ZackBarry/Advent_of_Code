#!/usr/bin/env python3

input = open('02-input.txt').read().splitlines()

split = [x.split() for x in input]

amap = {
    'A': 1,
    'B': 2,
    'C': 3
}

xmap = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

vals = [1, 2, 3]
shapes = ['X', 'Y', "Z"]

total = 0
for round in split:
    x = amap[round[0]]
    y = xmap[round[1]]
    total += y
    if y == x:
        total += 3
    elif y == 1 and x == 3:
        total += 6
    elif y == 2 and x == 1:
        total += 6
    elif y == 3 and x == 2:
        total += 6

print(f'Part 1: {total}')

total = 0
for round in split:
    x = amap[round[0]]
    y2 = round[1]
    xindex = vals.index(x)
    if y2 == 'X':
        yindex = xindex - 1
        y = shapes[yindex]
    elif y2 == 'Y':
        total += 3
        y = shapes[xindex]
    elif y2 == 'Z':
        total += 6
        yindex = (xindex + 1) % 3
        y = shapes[yindex]
    total += xmap[y]

print(f'Part 2: {total}')

