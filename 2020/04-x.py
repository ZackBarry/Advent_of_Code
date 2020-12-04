
input = open('2020/04-input.txt').read()

input = input.split('\n\n')

inputc = [x.split() for x in input]

inputd = [[y[0:3] for y in x if y[0:3] != 'cid'] for x in inputc]

inpute = [sorted(x) for x in inputd]

valid = [len(x) == 7 for x in inpute]

from itertools import compress

p2a = list(compress(inputc, valid))

p2b = [sorted(x) for x in p2a]

p2c = [[y for y in x if y[0:3] != 'cid'] for x in p2b]

p2d = [[y[4:len(y)] for y in x] for x in p2c]

p2e = [
    [
        len(x[0]) == 4 and 1920 <= int(x[0]) <= 2020,
        len(x[5]) == 4 and 2010 <= int(x[5]) <= 2020,
        len(x[2]) == 4 and 2020 <= int(x[2]) <= 2030,
        (str.isdigit(x[4][0:len(x[4])-3]) and x[4][len(x[4])-2 : len(x[4])] == 'cm' and 150 <= int(x[4][0:len(x[4])-2]) <= 193)
          or (str.isdigit(x[4][0:len(x[4])-3]) and x[4][len(x[4])-2 : len(x[4])] == 'in' and 59 <= int(x[4][0:len(x[4])-2]) <= 76),
        x[3][0] == '#' and len(x[3]) == 7 and sum(y in list('0123456789abcdef') for y in x[3]) == 6,
        x[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        str.isdigit(x[6]) and len(x[6]) == 9
    ]
    for x in p2d]



# https://www.reddit.com/r/adventofcode/comments/k6e8sw/2020_day_04_solutions/gekep58/