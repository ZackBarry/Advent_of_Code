
entries = [int(x) for x in open('2020/01-input.txt').read().strip().split('\n')]


def part_one(expenses, target_sum):
    """If a+b=2020, then a=2020-b. Calculate each possible 2020-b then find the matching value."""
    complement = [target_sum - b for b in expenses]
    x = list(set(expenses) & set(complement))[0]
    return x * (target_sum - x)


def part_two(expenses, target_sum):
    """If a+b+c=2020, then c=2020-(a+b). Calculate each possible 2020-(a+b) then find the matching value."""
    complement = {
        2020-(a+b): [a, b]
        for a in expenses
        for b in expenses
        if a != b
    }
    c = list(set(complement.keys()) & set(expenses))[0]
    a, b = complement[c]
    return a * b * c
