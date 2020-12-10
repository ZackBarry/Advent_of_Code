
input = open('2020/10-input.txt').read().splitlines()
input = [int(x) for x in input]
input.sort()
# part 1

i = 0
diff = {}
while i <= len(input):
    new = 0
    if i == 0:
        new = input[i] - 0
    elif i < len(input):
        new = input[i] - input[i-1]
    else:
        new = 3
    if new in diff:
        diff[new] += 1
    else:
        diff[new] = 1
    i += 1

diff[1] * diff[3]
# part 2

built_in = max(input) + 3
final = max(input)

with_diffs = [0]
i = 0
while i < len(input):
    diff = 0
    if i == 0:
        diff = input[i]
    else:
        diff = input[i] - input[i-1]
    with_diffs += [diff, input[i]]
    i += 1


def check_valid_remove(existing, index):
    if index % 2 != 0:
        print('error')
        return None
    new_diff = existing[index-1] + existing[index+1]
    if new_diff <= 3:
        return True
    else:
        return False


def remove_index(existing, index):
    if index % 2 != 0:
        print('error')
        return None
    return existing[0:(index-1)] + [existing[index-1] + existing[index+1]] + existing[(index+2):]


def count_valid(existing, index, total=0):
    if index == 0:
        print(existing)
        return 1
    else:
        if check_valid_remove(existing, index):
            new_existing = remove_index(existing, index)
            total += count_valid(new_existing, index - 2)
        total += count_valid(existing, index - 2)
    return total



my_sets = {}
current_set = []
for i, x in enumerate(with_diffs):
    if i == len(with_diffs) - 1:
        current_set += [x]
        my_sets[i] = current_set
    elif i % 2 != 0:
        if x == 3:
            my_sets[i] = current_set
            current_set = []
        else:
            current_set += [x]
    else:
        current_set += [x]


total = 1
for _, x in my_sets.items():
    print(f'this set: {x}')
    if len(x) <= 3:
        new_prod = 1
    else:
        new_prod = count_valid(x, len(x) - 3)
    print(new_prod)
    total *= new_prod