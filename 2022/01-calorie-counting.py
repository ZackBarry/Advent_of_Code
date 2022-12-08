#!/usr/bin/env python3

input = open('01-input.txt').read().splitlines()

elves = []
elf = 0
for i in input:
    if i == '':
        elves.append(elf)
        elf = 0
    else:
        elf += int(i)
elves.append(elf)

print(f'Part 1: {max(elves)}')

print(f'Part 2: {sum(sorted(elves)[-3:])}')