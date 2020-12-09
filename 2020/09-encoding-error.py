
input = open('2020/09-input.txt').read().splitlines()

input = [int(x) for x in input]

# part 1

sums = []
nums = []
valid = True
i = 0

while valid:
    target = input[i]
    if i < 25:
        sums += [x + target for x in input[0:i]+input[i+1:]]
        nums += [target]
    else:
        if target in sums:
            sums += [x + target for x in nums]
            sums = sums[24:]
            nums += [target]
            nums = nums[1:]
        else:
            print(f'error with {target}, index {i}')
            valid = False
    i += 1

# part 2

target = 375054920

found = False
sums = []
i = 0

while not found:
    if i == 0:
        for x in input:
            sums += [[x, [x]]]
    else:
        for j, x in enumerate(input):
            if j >= i:
                sums[j-i][0] += x
                sums[j-i][1] += [x]
                if sums[j-i][0] == target:
                    print(f'answer is {min(sums[j-i][1]) + max(sums[j-i][1])}')
                    found = True
    i += 1
