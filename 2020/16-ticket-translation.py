import numpy as np

input = open('2020/16-input.txt').read().splitlines()

input = [x for x in input if len(x) > 0]

rules = {}
my_ticket = []
nb_ticket = []

for i, x in enumerate(input):
    if list(x)[0].isalpha() and list(x)[-1].isdigit():
        rule = x.split(': ')
        ranges = rule[1].split(' or ')
        ranges = [y.split('-') for y in ranges]
        ranges = [np.arange(int(y[0]), int(y[1]) + 1) for y in ranges]
        ranges = set(ranges[0]).union(set(ranges[1]))
        rules[rule[0]] = ranges
    elif input[i-1] == 'your ticket:':
        my_ticket += [int(y) for y in x.split(',')]
    elif list(x)[0].isdigit():
        nb_ticket += [[int(y) for y in x.split(',')]]
    else:
        continue

valid_number = set()

for rnge in rules.values():
    valid_number = valid_number.union(rnge)


error_rate = 0

for ticket in nb_ticket:
    error_rate += sum(set(ticket).difference(valid_number))

print(error_rate)

# part 2

ok_ticket = [x for x in nb_ticket if valid_number.issuperset(x)] + [my_ticket]
mapping = {}

i = 0
while i < len(ok_ticket[0]):
    vals = set([x[i] for x in ok_ticket])
    for k, v in rules.items():
        if v.issuperset(vals):
            if k in mapping.keys():
                mapping[k] += [i]
            else:
                mapping[k] = [i]
    i += 1


final_mapping = {}
assigned = []
while len(assigned) < 20:
    for k, v in mapping.items():
        possible_locs = list(set(v).difference(set(assigned)))
        if len(possible_locs) == 1:
            final_mapping[k] = possible_locs[0]
            assigned += possible_locs



prod = 1

for k, v in final_mapping.items():
    if k.startswith('departure'):
        prod *= my_ticket[v]

print(prod)
