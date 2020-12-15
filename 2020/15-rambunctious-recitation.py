
input = [int(x) for x in open('2020/15-input.txt').read().splitlines()]

# part 1

track = {}
track_count = {}

for i, x in enumerate(input[0:-1]):
    track[x] = i

said = input[0:-1]
last_said = input[-1]
now_said = 0

i = len(input) - 1

while i < 2020:
    print(f'{i+1, last_said}')
    if last_said in track.keys():
        now_said = i - track[last_said]
    else:
        now_said = 0
    track[last_said] = i
    said += [last_said]
    last_said = now_said
    i += 1

# part 2

track = {}
track_count = {}

for i, x in enumerate(input[0:-1]):
    track[x] = i

said = input[0:-1]
last_said = input[-1]
now_said = 0

i = len(input) - 1

while i < 30000000:
    if (i+1) == 30000000:
        print(last_said)
    if last_said in track.keys():
        now_said = i - track[last_said]
    else:
        now_said = 0
    track[last_said] = i
    said += [last_said]
    last_said = now_said
    i += 1


