
input = open('2020/06-input.txt').read()

input = input.split('\n\n')

input = [x.splitlines() for x in input]

out = {}
for i, l in enumerate(input):
    yes = {}
    people = len(l)
    outi = 0
    for x in l:
        for y in x:
            if y in yes.keys():
                yes[y] += 1
            else:
                yes[y] = 1
    for k, v in yes.items():
        if v == people:
            outi += 1
    out[i] = outi

j = 0
for x in list(out.values()):
    j += x

print(j)