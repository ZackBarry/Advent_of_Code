#!/usr/bin/env python3

class Monkey:
    def __init__(self, 
        items, 
        opp_type, 
        opp_value, 
        divisor, 
        if_false, 
        if_true, 
        limit_worry, 
        lcm,
    ):
        self.items = items
        self.opp_type = opp_type
        self.opp_value = opp_value
        self.divisor = divisor
        self.if_false = if_false
        self.if_true = if_true
        self.limit_worry = limit_worry
        self.lcm = lcm
        self.inspections = 0

    def process(self):
        pass_to = [] 
        for item in self.items:
            self.inspections += 1
            if self.opp_type == '+':
                new_val = item + self.opp_value
            elif self.opp_type == 'squared':
                new_val = item * item
            else:
                new_val = item * self.opp_value
            if self.limit_worry:
                new_val = new_val // 3
            new_val = new_val % self.lcm
            if new_val % self.divisor == 0:
                pass_to.append({'item': new_val, 'monkey': self.if_true})
            else:
                pass_to.append({'item': new_val, 'monkey': self.if_false})
        self.items = []
        return pass_to


def round(monkeys):
    for i in range(0, len(monkeys.keys())):
        steps = monkeys[i].process()
        for s in steps:
            item = s['item']
            monkey = s['monkey']
            monkeys[monkey].items.append(item)
    return monkeys


def load_monkeys(data, limit_worry=True):
    monkey_args = []
    lcm = 1

    args = {}
    for r in data:
        r = r.strip()
        if len(r) == 0:
            monkey_args.append(args)
            args = {}
        elif r.startswith('Starting items:'):
            args['items'] = [int(x) for x in r[len('Starting items: '):].split(', ')]
        elif r.startswith('Operation: new = old * old'):
            args['opp_type'] = 'squared'
            args['opp_value'] = -1
        elif r.startswith('Operation: new = old '):
            tmp = r[len('Operation: new = old '):].split(' ')
            args['opp_type'] = tmp[0]
            args['opp_value'] = int(tmp[1])
        elif r.startswith('Test: divisible by '):
            args['divisor'] = int(r.split(' ')[-1])
            lcm *= int(r.split(' ')[-1])
        elif r.startswith('If true:'):
            args['if_true'] = int(r.split(' ')[-1])
        elif r.startswith('If false:'):
            args['if_false'] = int(r.split(' ')[-1])
    monkey_args.append(args)
    
    monkeys = {
        i: Monkey(limit_worry=limit_worry, lcm=lcm, **args) 
        for i, args in enumerate(monkey_args)
    }

    return monkeys


def calc_monkey_business(monkeys, rounds):
    for _ in range(rounds):
        monkeys = round(monkeys)

    activity = [m.inspections for m in monkeys.values()]
    
    return sorted(activity)[-1] * sorted(activity)[-2]


if __name__ == '__main__':
    data = open('11-input.txt').read().splitlines()
    
    print(f'Part 1: {calc_monkey_business(load_monkeys(data), 20)}')
    
    print(f'Part 2: {calc_monkey_business(load_monkeys(data, limit_worry=False), 10000)}')
