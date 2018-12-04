# read in data and split into individual elements
InputFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\Advent_of_Code\Input_Day1.txt')
Input = InputFile.read()
Elements = Input.split('\n')

# -------------------------------------------------------------------------
# Task 1: sum all the elements
# -------------------------------------------------------------------------

Total = 0
for x in Elements:
    # make sure the length is such that addition/subtraction are possible
    if len(x) < 2:
        continue
    if x[0] == '+':
        Total += int(x[1:])
    else:
        Total -= int(x[1:])

print('The sum of the frequencies is:', Total)

# -------------------------------------------------------------------------
# Task 2: find the first time the running total duplicates (may require
#         multiple iterations of the Elements list)
# -------------------------------------------------------------------------

Totals = {}
Total = 0

place = 0
iteration_count = 0

while True:
    x = Elements[place % len(Elements)]
    # make sure the length is such that addition/subtraction are possible
    if len(x) >= 2:
        if x[0] == '+':
            Total += int(x[1:])
        else:
            Total -= int(x[1:])
        # check if the current total has already been reached
        if Total in Totals:
            break
        else:
            Totals[Total] = place
    # update the place
    place += 1

print(Total, 'first occurred after', Totals[Total], 'calibrations.',
      'It occurred again after', place, 'calibrations.')
