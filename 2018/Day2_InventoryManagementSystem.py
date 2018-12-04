# read in the list of IDs
InputFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\Advent_of_Code\Input_Day2.txt')
Input = InputFile.read()
IDs = Input.split('\n')

# -------------------------------------------------------------------------
# Task 1: Read the list of product IDs, counting the number that contain
#         exactly two of any letter and then separately counting those with
#         exactly three of any letter. Multiply those two counts together
#         to get a rudimentary checksum.
# -------------------------------------------------------------------------

two_count = 0
three_count = 0

for product in IDs:
    letters = {}
    for letter in product:
        letters.setdefault(letter,0)
        letters[letter] += 1
    if 2 in letters.values():
        two_count += 1
    if 3 in letters.values():
        three_count += 1

print('There were', two_count, 'two counts and', three_count, 'three counts.',
      'The product is ', two_count * three_count, '.')

# -------------------------------------------------------------------------
# Task 2: Find the two IDs which differ by exactly one character at the
#         same position in both strings. Extract the letters that they have
#         in common.
# -------------------------------------------------------------------------

for product in IDs:
    for compare in IDs:
        diff_count = 0
        for i, (char1, char2) in enumerate(zip(product, compare)):
            if char1 != char2:
                diff_count += 1
                diff_location = i
        if diff_count == 1:
            common = product[:diff_location] + product[diff_location+1:]
            print('The common substring is ' + common + '.')
            break
