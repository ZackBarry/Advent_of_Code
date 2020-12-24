from copy import deepcopy

input = open('2020/22-input.txt').read().split('\n\n')

p1 = [int(x) for x in input[0].split(':\n')[1].splitlines()]
p2 = [int(x) for x in input[1].split(':\n')[1].splitlines()]

# part 1

while len(p1) > 0 and len(p2) > 0:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 < c2:
        p2 += [c2, c1]
    else:
        p1 += [c1, c2]

p1.reverse()
p2.reverse()

score = 0
for i, c in enumerate(p1 + p2):
    score += (i + 1) * c

print(score)

# part 2

p1 = [int(x) for x in input[0].split(':\n')[1].splitlines()]
p2 = [int(x) for x in input[1].split(':\n')[1].splitlines()]


def game(d1, d2):
    obs_d1 = []
    obs_d2 = []
    while len(d1) > 0 and len(d2) > 0:
        if d1 in obs_d1 and d2 in obs_d2:
            return 'p1', d1
        else:
            obs_d1 += [deepcopy(d1)]
            obs_d2 += [deepcopy(d2)]
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if c1 <= len(d1) and c2 <= len(d2):
            winner, _ = game(deepcopy(d1)[0:c1], deepcopy(d2)[0:c2])
            if winner == 'p1':
                d1 += [c1, c2]
            else:
                d2 += [c2, c1]
        else:
            if c1 < c2:
                d2 += [c2, c1]
            else:
                d1 += [c1, c2]
    if len(d1) > 0:
        return 'p1', d1
    else:
        return 'p2', d2


_, deck = game(p1, p2)
deck.reverse()

score = 0
for i, c in enumerate(deck):
    score += (i + 1) * c

print(score)