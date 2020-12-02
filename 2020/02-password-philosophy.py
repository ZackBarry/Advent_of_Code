import re

input = open('2020/02-input.txt').read().splitlines()


def part_one(passwords):
    tuples = [re.sub(r'[-:]', ' ', p).split() for p in passwords]
    good_passwords = [int(t[0]) <= len(re.findall(t[2], t[3])) <= int(t[1]) for t in tuples]
    return sum(good_passwords)


def part_two(passwords):
    tuples = [re.sub(r'[-:]', ' ', p).split() for p in passwords]
    good_passwords = [(t[3][int(t[0])-1] == t[2]) ^ (t[3][int(t[1])-1] == t[2]) for t in tuples]
    return sum(good_passwords)
