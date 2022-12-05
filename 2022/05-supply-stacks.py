from collections import defaultdict

input = open('05-input.txt').read().splitlines()


def load_crates(input):
    crates = defaultdict(list)
    for line in input:
        if '[' != line[0]:
            return crates
        for i, x in enumerate(list(line)):
            if x.isalpha():
                crate_number = 1 + (i - 1) // 4 
                crates[crate_number].append(x)


def move1(crates, number, a, b):
    for _ in range(number):
        to_move = crates[a][0]
        del crates[a][0]
        crates[b].insert(0, to_move)


def move2(crates, number, a, b):
    to_move = crates[a][:number]
    del crates[a][:number]
    crates[b] = to_move + crates[b]


def print_top(crates):
    out = ''
    for i in range(len(crates.keys())):
        out += crates[i + 1][0]
    return out


def part(move_func):
    crates = load_crates(input)
    for line in input:
        if line[:4] != 'move':
            continue
        temp = line.split(' ')
        number = start = end = 0
        for t in temp:
            if t.isnumeric():
                if number == 0:
                    number = int(t)
                elif start == 0:
                    start = int(t)
                else:
                    end = int(t)
        move_func(crates, number, start, end)
    return print_top(crates)


if __name__ == '__main__':
    print(f'Part 1: {part(move1)}')
    print(f'Part 2: {part(move2)}')