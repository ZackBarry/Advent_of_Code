#!/usr/bin/env python3

import sys
from collections import defaultdict, Counter
import math
from functools import cmp_to_key

day_number = sys.argv[0][-5:-3]

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    input_file = f'{day_number}-test.txt'
else:
    input_file = f'{day_number}-input.txt'

input = open(input_file).read().splitlines()


rank = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


def get_hand_rank(cards):
    counts = dict(Counter(cards))
    if len(set(cards)) == 1:
        # five of a kind of a kind or full house
        return 7
    elif len(set(cards)) == 2:
        # four of a kind or full house
        if 4 in set(counts.values()):
            return 6
        else:
            return 5
    elif len(set(cards)) == 3:
        # 3 of a kind or two pair
        if 3 in set(counts.values()):
            return 4
        else:
            return 3
    elif len(set(cards)) == 4:
        # one pair
        return 2
    else:
        return 1


def sort_hands(h1, h2):
    if h1['rank'] > h2['rank']:
        return 1
    elif h1['rank'] == h2['rank']:
        for c1, c2 in zip(h1['hand'], h2['hand']):
            if rank[c1] > rank[c2]:
                return 1
            elif rank[c1] < rank[c2]:
                return -1
    return -1


hands = []

for l in input:
    cards = list(l.split(' ')[0])
    bid = int(l.split(' ')[1])
    hands.append({'rank': get_hand_rank(cards), 'hand': cards, 'bid': bid})

hands.sort(key=cmp_to_key(sort_hands))

result = sum(hand['bid'] * (i + 1) for i, hand in enumerate(hands))

print(f'Part 1: {result}')

###################################

joker_rank = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}

def sort_joker_hands(h1, h2):
    if h1['rank'] > h2['rank']:
        return 1
    elif h1['rank'] == h2['rank']:
        for c1, c2 in zip(h1['hand'], h2['hand']):
            if joker_rank[c1] > joker_rank[c2]:
                return 1
            elif joker_rank[c1] < joker_rank[c2]:
                return -1
    return -1


def get_joker_rank(cards):
    card_count = dict(Counter(cards))

    number_to_letters = defaultdict(list)
    highest_count = 0
    for card, count in card_count.items():
        if card != 'J':
            number_to_letters[count].append(card)
            highest_count = max(highest_count, count)

    if highest_count == 0:
        # all cards were jokers
        most_valuable = 'A'
    else:
        highest_count_cards = number_to_letters[highest_count]
        most_valuable = sorted(highest_count_cards, key=lambda x: rank[x])[-1]
    new_cards = [x if x != 'J' else most_valuable for x in cards]

    return get_hand_rank(new_cards)



hands = []

for l in input:
    cards = list(l.split(' ')[0])
    bid = int(l.split(' ')[1])
    hands.append({'rank': get_joker_rank(cards), 'hand': cards, 'bid': bid})

hands.sort(key=cmp_to_key(sort_joker_hands))

result = sum(hand['bid'] * (i + 1) for i, hand in enumerate(hands))

print(f'Part 2: {result}')