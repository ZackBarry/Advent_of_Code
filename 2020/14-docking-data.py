import copy
from itertools import chain, combinations

input = open('2020/14-input.txt').read().splitlines()

mask = {}
records = {}
for instruction in input:
    if 'mask' in instruction:
        mask = {}
        mask_str = instruction[-36:]
        for i, val in enumerate(list(mask_str)):
            if val != 'X':
                mask[i] = val
    else:
        parts = instruction.split(' = ')
        write_to = int(parts[0][4:-1])
        number = int(parts[1])
        binary = list('{0:b}'.format(number).zfill(36))
        for k, v in mask.items():
            binary[k] = v
        records[write_to] = ''.join(binary)

sum = 0
for binary in records.values():
    sum += int(binary, 2)

print(sum)

# part two

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


mask = {}
floating = []
records = {}
for instruction in input:
    if 'mask' in instruction:
        mask = {}
        floating = []
        mask_str = instruction[-36:]
        for i, val in enumerate(list(mask_str)):
            if val == '1':
                mask[i] = val
            elif val == 'X':
                floating += [i]
            else:
                continue
    else:
        parts = instruction.split(' = ')
        write_to = int(parts[0][4:-1])
        b_write_to = list('{0:b}'.format(write_to).zfill(36))
        for k, v in mask.items():
            b_write_to[k] = v
        write_val = int(parts[1])
        floating_ones = powerset(floating)
        for indexes in floating_ones:
            this_write_to = copy.deepcopy(b_write_to)
            for i in floating:
                this_write_to[i] = '1'
            for index in indexes:
                this_write_to[index] = '0'
            this_write_to = int(''.join(this_write_to), 2)
            records[this_write_to] = write_val

sum = 0
for v in records.values():
    sum += v

print(sum)