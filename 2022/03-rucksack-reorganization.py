#!/usr/bin/env python3

input = open('03-input.txt').read().splitlines()

rucks = []
for x in input:
    l = len(x) // 2
    rucks.append([x[:l], x[l:]])

common = []
for r in rucks:
    a = set(r[0])
    b = set(r[1])
    this_common = a.intersection(b)
    common.append(this_common.pop())

vals = list('abcdefghijklmnopqrstuvwxyz')
vals += [x.upper() for x in vals]

total = sum([vals.index(c) + 1 for c in common])

print(f'Part 1: {total}')

total = 0
i = 0
while i < len(input):
    a = set(input[i])
    b = set(input[i + 1])
    c = set(input[i + 2])
    ab = a.intersection(b)
    abc = ab.intersection(c)
    v = abc.pop()
    value = vals.index(v) + 1
    total += value
    i += 3

print(f'Part 2: {total}')
