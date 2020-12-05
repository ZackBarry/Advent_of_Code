
import numpy as np

input = open('2020/05-input.txt').read().splitlines()


def get_row(code):
    all = np.arange(0, 128)
    for i in code:
        if i == 'F':
            sub = np.arange(0, int(len(all) / 2))
            all = all[sub]
        else:
            sub = np.arange(int(len(all) / 2), len(all))
            all = all[sub]
    return int(all)


def get_col(code):
    all = np.arange(0, 8)
    for i in code:
        if i == 'L':
            sub = np.arange(0, int(len(all) / 2))
            all = all[sub]
        else:
            sub = np.arange(int(len(all) / 2), len(all))
            all = all[sub]
    return int(all)


def get_id(x):
    two = [x[0:7], x[7:11]]
    return get_row(two[0]) * 8 + get_col(two[1])


out = sorted([get_id(x) for x in input])

part1 = max(out)

part2 = int(np.array(out[0:len(out)-1])[np.array([out[i]+1 != out[i+1] for i, _ in enumerate(out) if i < len(out) - 1])]) + 1