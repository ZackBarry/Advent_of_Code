import re
import itertools

input = open('2020/07-input.txt').read().splitlines()

# part 1
inputa = [re.sub(r'bags|bag|contain|no other|[,.1-9]', '', a).split() for a in input]

contained_in = {}

for rule in inputa:
    outer_bag = ' '.join(rule[0:2])
    if outer_bag not in contained_in:
        contained_in[outer_bag] = set()

    rule = rule[2:]
    while len(rule) > 0:
        inner_bag = ' '.join(rule[0:2])
        bags = contained_in.get(inner_bag)
        if bags:
            contained_in[inner_bag].add(outer_bag)
        else:
            contained_in[inner_bag] = set([outer_bag])
        rule = rule[2:]


def get_contained_by(bag):
    contained_by = contained_in[bag]
    if contained_by is None:
        return None
    else:
        return set(list(contained_by) + list(itertools.chain.from_iterable([list(get_contained_by(bag)) for bag in contained_by])))


len(get_contained_by('shiny gold'))

# part 2
inputb = [re.sub(r'bags|bag|contain|no other|[,.]', '', a).split() for a in input]

contains = {}

for rule in inputb:
    outer_bag = ' '.join(rule[0:2])

    this_contains = {}
    idx = 2
    while idx < len(rule):
        inner_count = rule[idx]
        inner_bag = ' '.join([rule[idx + 1], rule[idx + 2]])
        this_contains[inner_bag] = inner_count
        idx += 3

    contains[outer_bag] = this_contains


def get_number_contains(bag):
    inside_bags = contains[bag]
    if not inside_bags:
        return 0
    else:
        return sum([int(v) * (1 + get_number_contains(k)) for k, v in inside_bags.items()])


get_number_contains('shiny gold')