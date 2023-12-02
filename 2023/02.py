#!/usr/bin/env python3

input = open('02-input.txt').read().splitlines()


def extract(line):
    id = int(line.split(' ')[1][:-1])

    pulls = line.split(':')[1].split(';')

    for p in pulls:
        colors = p.split(',')
        vals = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for c in colors:
            c = c.strip()
            number = int(c.split(' ')[0])
            color = c.split(' ')[1]
            vals[color] = number

        if vals['red'] > 12 or vals['green'] > 13 or vals['blue'] > 14:
            return 0

    return id


print(f'Part 1: {sum(extract(l) for l in input)}')


def extract(line):
    pulls = line.split(':')[1].split(';')
    pulls_vals = []

    for p in pulls:
        colors = p.split(',')
        vals = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for c in colors:
            c = c.strip()
            number = int(c.split(' ')[0])
            color = c.split(' ')[1]
            vals[color] = number

        pulls_vals.append(vals)

    red = max(v['red'] for v in pulls_vals)
    blue = max(v['blue'] for v in pulls_vals)
    green = max(v['green'] for v in pulls_vals)

    return red * blue * green


print(f'Part 2: {sum(extract(l) for l in input)}')