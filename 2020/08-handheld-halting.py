
input = open('2020/08-input.txt').read().splitlines()

# part 1
acc = 0

inputa = [[y[0], int(y[1])] for y in [x.split() for x in input]]

done = {}

inpute = enumerate(inputa)
step = 0
while step not in done:
    done[step] = True
    action = inputa[step][0]
    number = inputa[step][1]
    if action == 'acc':
        print(number)
        print(inputa[step])
        acc += number
        step += 1
    if action == 'jmp':
        step += number
    if action == 'nop':
        step += 1


done = {}

last = len(inputa)
last_valid = last - 5
step = 0
it = 0

jmp_dict = {}
nop_dict = {}
for i, x in enumerate(inputa):
    if x[0] == 'jmp':
        jmp_dict[i + x[1]] = i
    elif x[0] == 'nop':
        nop_dict[i + x[1]] = i
    else:
        continue


def check_change(swap_index, swap_to):
    input_tmp = inputa
    input_tmp[swap_index][0] = swap_to
    it = 0
    step = 0
    acc = 0
    while it < 100000:
        action = input_tmp[step][0]
        number = input_tmp[step][1]
        if action == 'acc':
            step += 1
            acc += number
        elif action == 'jmp':
            step += number
        else:
            step += 1
        if step == len(inputa):
            print(f'found swap at {swap_index}, acc = {acc}')
            return f'found swap at {swap_index}, acc = {acc}'
        it += 1
    else:
        return None


def find_change():
    for i, x in enumerate(inputa):
        if x[0] == 'jmp':
            print(f'testing {i} to nop')
            out = check_change(i, 'nop')
            if out:
                return out
        elif x[0] == 'nop':
            print(f'testing {i} to jmp')
            out = check_change(i, 'jmp')
            if out:
                return out
        else:
            continue


find_change()



def find_changez(step=0):
    output = f'start: {step} '
    all_out = []
    it = 0
    while it < 100000:
        if step in jmp_dict.keys():
            find_change(jmp_dict[step])

        action = inputa[step - 1][0]
        number = inputa[step - 1][1]
        if action in ['acc', 'nop']:
            all_out += find_change(step - 1)
        elif action == 'jmp' and number == 1:
            all_out += find_change(step - 1)
        elif step in jmp_dict.keys():
            all_out += find_change(jmp_dict[step])
        elif action == 'jmp':
            out = check_change(step-1, 'nop')
            if out:
                output += ' suceeded'
            else:
                output += ' failed'
            break
        elif step in nop_dict.keys():
            out = check_change(nop_dict[step], 'jmp')
            if out:
                output += ' suceeded'
            else:
                output += ' failed'
            break
        else:
            print(f'missing case step={step}')
            break
        it += 1
    return all_out + [output]




step = len(inputa)-1
it = 0
while it < 100000:
    print(it)
    print(step)
    action = inputa[step-1][0]
    number = inputa[step-1][1]
    if action in ['acc', 'nop']:
        step -= 1
    elif action == 'jmp' and number == 1:
        step -= 1
    elif step in jmp_dict.keys():
        step = jmp_dict[step]
    elif action == 'jmp':
        print(f'change {step-1} to nop')
        break
    elif step in nop_dict.keys():
        print(f'change {nop_dict[step]} to jmp')
    else:
        print(f'missing case step={step}')
        break
    it += 1

inputa[387][0] = 'nop'
# part 2\

acc = 0

inputa = [[y[0], int(y[1])] for y in [x.split() for x in input]]

done = {}

inpute = enumerate(inputa)
step = 0
it = 0
while step != len(inputa) and it < 10000:
    action = inputa[step][0]
    number = inputa[step][1]
    if action == 'acc':
        print(number)
        print(inputa[step])
        acc += number
        step += 1
    if action == 'jmp':
        step += number
    if action == 'nop':
        step += 1
    it += 1