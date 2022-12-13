#!/usr/bin/env python3
from functools import cmp_to_key


def compare(a, b):
    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            if compare(x, y) != 0:
                return compare(x, y)
        return compare(len(a), len(b))
    elif isinstance(a, list):
        return compare(a, [b])
    elif isinstance(b, list):
        return compare([a], b)
    else:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1


if __name__ == '__main__':
    data = open('13-input.txt').read().splitlines()

    data = [eval(x) for x in data if x != '']

    ordered_indices = 0
    for i in range(len(data) // 2):
        if compare(data[2 * i], data[2 * i + 1]) == -1:
            ordered_indices += i + 1
    print(f'Part 1: {ordered_indices}')

    data += [[[2]], [[6]]]
    data.sort(key=cmp_to_key(compare))
    
    print(f'Part 2: {(data.index([[2]]) + 1) * (data.index([[6]]) + 1)}')
