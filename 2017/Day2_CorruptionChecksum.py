import sys

# read in the data
InputFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\Advent_of_Code\2017\Input_Day2.txt')
Input = InputFile.read()
# strip() removes whitespace at the start and end of file
Input = Input.strip()
# split() without an argument splits on whitespace
rows = Input.split('\n')

# -------------------------------------------------------------------------
# Task 1: The spreadsheet consists of rows of apparently-random numbers. To
#         make sure the recovery process is on the right track, they need
#         you to calculate the spreadsheet's checksum. For each row,
#         determine the difference between the largest value and the
#         smallest value; the checksum is the sum of all of these
#         differences.
# -------------------------------------------------------------------------

checksum = 0

for row in rows:
    numbers = row.split('\t')
    smallest = int(numbers[0])
    largest = int(numbers[0])
    for number in numbers[1:]:
        if int(number) < smallest:
            smallest = int(number)
        if int(number) > largest:
            largest = int(number)
    difference = largest - smallest
    checksum += difference

print('The checksum is ' + str(checksum) + '.')

# -------------------------------------------------------------------------
# Task 1: It sounds like the goal is to find the only two numbers in each
#         row where one evenly divides the other - that is, where the
#         result of the division operation is a whole number. They would
#         like you to find those numbers on each line, divide them, and add
#         up each line's result.
# -------------------------------------------------------------------------

evenly = 0

for row in rows:
    numbers = row.split('\t')
    # check all the possible divisions
    for num1 in numbers:
        for num2 in numbers:
            # make sure even division is possible
            if int(num1) > int(num2):
                if int(num1) % int(num2) == 0:
                    evenly += int(num1) / int(num2)

print('The sum of the even divisions is ' + str(evenly) + '.')
