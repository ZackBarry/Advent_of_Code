import re
import sys

# -------------------------------------------------------------------------
# Background: Each line in the input file specifies a rectangle cut out of
#         a larger piece of fabric. A claim like #123 @ 3,2: 5x4 means that
#         claim ID 123 specifies a rectangle 3 inches from the left edge,
#         2 inches from the top edge, 5 inches wide, and 4 inches tall.
# -------------------------------------------------------------------------

# gather the input
InputFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\Advent_of_Code\Input_Day3.txt')
Input = InputFile.read()
Claims = Input.split('\n')

# -------------------------------------------------------------------------
# Task 1: How many square inches of fabric are within two or more claims?
# -------------------------------------------------------------------------

# dict for storing cut locations and counts

saved = {}

# regular expressions for getting the starting coordinate of the cut
#  and the cut's width/height

startRegex = re.compile(r'@ (\d+),(\d+)')
dimRegex = re.compile('(\d+)x(\d+)')


def get_coord(claim_str):
    match = startRegex.search(claim_str)
    return [int(match.group(1)), int(match.group(2))]


def get_dim(claim_str):
    match = dimRegex.search(claim_str)
    return [int(match.group(1)), int(match.group(2))]


# add cut coordinates to a coordinate dict


def add_cut(start, size):
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            # tuples can be used as dict keys whereas lists cannot
            saved.setdefault((start[0]+i, start[1]+j), 0)
            saved[(start[0]+i, start[1]+j)] += 1


# Calculate the fabric coordinates for each claim and add them to a dict
#  where the keys are coordinates and the values are the number of claims
#  which use that square.

for claim in Claims:
    # make sure the claim is valid
    if len(claim) > 0:
        coord = get_coord(claim)  # get starting coordinate
        dim = get_dim(claim)      # get width and height
        add_cut(coord, dim)

# Determine the number of cuts which occur in two or more claims

counts = saved.values()
duplicates = 0

for count in counts:
    if count > 1:
        duplicates += 1

print('The number of duplicate cuts is ' + str(duplicates) + '.')

# -------------------------------------------------------------------------
# Task 1: What is the ID of the only claim that doesn't overlap?
# -------------------------------------------------------------------------

# check a claim against the saved dict and return true if the cut is unique
#  return false otherwise


def check_cut(start, size):
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            # tuples can be used as dict keys whereas lists cannot
            if saved[(start[0]+i, start[1]+j)] > 1:
                return False
    return True


for claim in Claims:
    if len(claim) > 0:
        coord = get_coord(claim)
        dim = get_dim(claim)
        if check_cut(coord, dim):
            print('Claim', claim, 'is unique.')
