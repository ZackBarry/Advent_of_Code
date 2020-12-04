import numpy as np

input = open('2020/03-input.txt').read().splitlines()


def count_trees(map, steps_right, steps_down):
    width = len(map[0])
    map = [map[i] for i in np.arange(0, len(map), steps_down)]
    has_tree = [r[(r_num*steps_right) % width] == '#' for r_num, r in enumerate(map) if r_num > 0]
    return sum(has_tree)


# Part 1:
count_trees(map, 3, 1)

# Part 2:
np.prod([count_trees(input, r, d) for r, d in zip([1,3,5,7,1], [1,1,1,1,2])])