
input = open('2020/18-input.txt').read().splitlines()

input = [x.replace(' ', '') for x in input]


def evaluate(line, total=None, next_op=None):
    if len(line) == 0:
        return total
    elif line[0] == '(':
        if not next_op:

        if next_op == '*':
            return total *= evaluate(line[1:])
        else:
            return total += evaluate(line[1:])

        return evaluate(line[1:])
    elif line[0].isdigit():
        current = int(re.search('[0-9]*', line).group())
        if total:
            if next_op == '*':
                total *= current
            else:
                total += current
        line = line[len(str(current)):]
    elif

    line = list(line.replace(' ', ''))
