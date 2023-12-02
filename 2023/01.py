#!/usr/bin/env python3

input = open('01-input.txt').read().splitlines()

result = 0

for x in input:
    f = l = None
    for y in x:
        if y.isnumeric():
            if f is None:
                f = y
            l = y
    result += int(f'{f}{l}')

print(f'Part 1: {result}')

len_to_number = {
    3: ['one', 'two', 'six'],
    4: ['four', 'five', 'nine'],
    5:  ['three', 'seven', 'eight']
}

number_to_int = {
    'one': 1,
    'two': 2, 
    'three': 3,
    'four': 4,
    'five': 5, 
    'six': 6,
    'seven': 7,
    'eight': 8, 
    'nine': 9
}

result = 0

for x in input:
    f = l = None
    for i, y in enumerate(x):
        if y.isnumeric():
            if f is None: 
                f = y
            l = y
        else:
            for _len, _numbers in len_to_number.items():
                if x[i:(i + _len)] in _numbers:
                    number = number_to_int[x[i:(i + _len)]]
                    if f is None:
                        f = number
                    l = number
    result += int(f'{f}{l}')

print(f'Part 2: {result}')