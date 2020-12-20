import copy

input = open('2020/19-input.txt').read().replace('"', '')

raw_rules = input.split('\n\n')[0].splitlines()
messages = input.split('\n\n')[1].splitlines()

rules = {}
for x in raw_rules:
    rule = x.split(': ')
    options = rule[1].split(' | ')
    options = [y.split() for y in options]
    rules[rule[0]] = options

# part 1


def check_rule(message, rule):
    if len(message) == 0 or len(rule) == 0:
        return False
    if len(message) < len(rule):
        return False
    lead = rule[0]
    if lead.isalpha():
        if message[0] == lead:
            if len(message) == 1:
                return True
            else:
                return check_rule(message[1:], rule[1:])
        else:
            return False
    else:
        lead_rule = rules[lead]
        for lr in lead_rule:
            new_rule = lr + rule[1:]
            result = check_rule(message, new_rule)
            if result:
                return True
    return False


root_rule = rules['0'][0]
valid = 0

for m in messages:
    print(m)
    if check_rule(m, root_rule):
        valid += 1

print(valid)

# part 2

# note: the check "len(message) < len(rule)" stops the infinite looping in its tracks!
rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]

root_rule = rules['0'][0]
valid = 0

for m in messages:
    print(m)
    if check_rule(m, root_rule):
        valid += 1

print(valid)