
entries = [int(x) for x in open('2020/01-input.txt').read().strip().split('\n')]


def find_addend_product(expenses, target_sum):
    """If a+b=2020, then a=2020-b. Calculate each possible 2020-b then find the common value."""
    complement_expenses = [target_sum - expense for expense in expenses]
    x = list(set(expenses) & set(complement_expenses))[0]
    return x * (target_sum - x)


def find_triaddend_product(expenses, target_sum):
    """If a+b+c=2020, then a+b=2020-c. Calculate each possible a+b and 2020-c then find the common value.

    :param expenses:
    :param target_sum:
    :return:
    """
    target_minus_c = {
        a+b: [a, b]
        for a in expenses
        for b in expenses
        if a != b
    }
    complement_expenses = [target_sum - expense for expense in expenses]
    c = target_sum - list(set(target_minus_c.keys()) & set(complement_expenses))[0]
    a, b = target_minus_c[target_sum - c]
    return a * b * c
