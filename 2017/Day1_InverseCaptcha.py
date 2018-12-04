import sys

# read in the sequence of digits
InputFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\Advent_of_Code\2017\Input_Day1.txt')
Input = InputFile.read().strip()  # strip() removes whitespace at the start and end of file

# -------------------------------------------------------------------------
# Task 1: The captcha requires you to review a sequence of digits (your
#         puzzle input) and find the sum of all digits that match the next
#         digit in the list. The list is circular, so the digit after the
#         last digit is the first digit in the list.
# -------------------------------------------------------------------------

# calculate the sum
total = 0

for i in range(0, len(Input)):
    if i == len(Input) - 1:
        if Input[i] == Input[0]:
            total += int(Input[i])
            print(Input[i])
    elif Input[i] == Input[i+1]:
        total += int(Input[i])

print('The sum of the matching digits is ' + str(total) + '.')

# -------------------------------------------------------------------------
# Task 2: Now, instead of considering the next digit, it wants you to
#         consider the digit halfway around the circular list. That is, if
#         your list contains 10 items, only include a digit in your sum if
#         the digit 10/2 = 5 steps forward matches it. Fortunately, your
#         list has an even number of elements.
# -------------------------------------------------------------------------

halftotal = 0

offset = int(len(Input) / 2)

for i in range(0, len(Input)):
    if Input[i] == Input[(i + offset) % len(Input)]:
        halftotal += int(Input[i])

print('The sum of all the matching half sums is ' + str(halftotal) + '.')
