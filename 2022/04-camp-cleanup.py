#!/usr/bin/env python3

input = open('04-input.txt').read().splitlines()

def split_into_pairs(x):
    out = []
    for y in x:
        y = y.split(',')
        a = y[0]
        b = y[1]
        a = a.split('-')
        a = [int(a[0]), int(a[1])]
        b = b.split('-')
        b = [int(b[0]), int(b[1])]
        out.append([a, b])
    return out

def contains(x, y):
    if x[0] <= y[0] and x[1] >= y[1]:
        return True
    elif y[0] <= x[0] and y[1] >= x[1]:
        return True
    else:
        return False

def overlaps(x, y):
    xrange = list(range(x[0], x[1] + 1))
    yrange = list(range(y[0], y[1] + 1))
    intersect = set(xrange).intersection(set(yrange))
    return len(list(intersect)) > 0

total = 0
for pairs in split_into_pairs(input):
    x = pairs[0]
    y = pairs[1]
    total += int(contains(x, y))
print(f'Part 1: {total}')

total = 0
for pairs in split_into_pairs(input):
    x = pairs[0]
    y = pairs[1]
    total += int(overlaps(x, y))
print(f'Part 2: {total}')