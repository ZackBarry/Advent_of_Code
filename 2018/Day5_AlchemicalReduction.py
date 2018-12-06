import sys

# -------------------------------------------------------------------------
# Data: Data is composed of a polymer which is represented a string of
#       capital and lowercase letters.  If a lowercase and uppercase
#       version of a letter is adjacent to itself, it destroys itself:
#             cBaAbD -> cBbD -> cD
# -------------------------------------------------------------------------

# read in the polymer
InputFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\Advent_of_Code\2018\Input_Day5.txt')
polymer = InputFile.read().strip()  # strip() removes whitespace at the start and end of file

# -------------------------------------------------------------------------
# Task 1: How many units remain after fully reacting the polymer?
# -------------------------------------------------------------------------

# test if two letters react


def test_reaction(let1, let2):
    if let1.islower() and let2.isupper() or let1.isupper() and let2.islower():
        if let1.lower() == let2.lower():
            return True
    return False


# find the first reaction and remove it


def find_reaction(atoms):
    for i, letter in enumerate(atoms[:len(atoms) - 1]):
        if i + 1 > len(atoms) - 1:
            return atoms
        if test_reaction(letter, atoms[i+1]):
            if i + 2 > len(atoms) - 1:
                return atoms[:i]
            else:
                atoms = atoms[:i] + atoms[i+2:]
    return atoms


# keep passing the polymer to find_reaction until no reactions remain


def react_polymer(species):
    while True:
        current_len = len(species)
        species = find_reaction(species)
        if len(species) == current_len:
            return species


# determine the length after reacting everything

#reacted_polymer = react_polymer(polymer)

#print("Task 1 Solution: reacted length = " + str(len(reacted_polymer)) + ".")


# -------------------------------------------------------------------------
# Task 2: Determine the reacted lengths of the polymer if you first remove
#         all instances of a single letter, regardless of case.  Which
#         length is the shortest?
# -------------------------------------------------------------------------

# remove all instances of a certain letter


def remove_letter(species, letter):
    return species.replace(letter.lower(), "").replace(letter.upper(), "")


# remove each letter and find the resulting reacted length

letters = "abcdefghijklmnopqrstuvwxyz"

shortest_length = len(polymer) + 1
removed_letter = ""

for item in letters:
    print(item)
    new_polymer = remove_letter(polymer, item)
    if len(react_polymer(new_polymer)) < shortest_length:
        shortest_length = len(react_polymer(new_polymer))
        removed_letter = item

print("Task 2 Solution: The shortest length is " + str(shortest_length) + " after removing " + item + ".")

