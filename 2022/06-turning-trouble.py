#!/usr/bin/env python3


def end_index_n_unique(word, n):
    last_n = []
    for i in range(len(word)):
        last_n.append(word[i])
        if len(last_n) > n:
            del last_n[0]
        if len(set(last_n)) == n:
            return i
    return -1


if __name__ == '__main__':
    input = open('06-input.txt').read()

    print(f'Part 1: {end_index_n_unique(input, 4) + 1}')
    print(f'Part 2: {end_index_n_unique(input, 14) + 1}')
    