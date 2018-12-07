import sys

# -------------------------------------------------------------------------
# Data: Data is composed of integer coordinates: x, y
# -------------------------------------------------------------------------

# read in the polymer
InputFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\Advent_of_Code\2018\Input_Day6.txt')
Coordinates = InputFile.read().strip()  # strip() removes whitespace at the start and end of file
Coordinates = Coordinates.split('\n')

for i, item in enumerate(Coordinates):
    coord = item.split(', ')
    coord = [int(coord[0]), int(coord[1])]
    Coordinates[i] = coord

# -------------------------------------------------------------------------
# Task 1: Which finite area is the largest?
# -------------------------------------------------------------------------

# function for calculating manhattan distance between two points


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[0] - p2[0])


# find the extreme x and y coordinates; limit search within the box they create

left_border = Coordinates[0][0]
left_coord = -1
right_border = Coordinates[0][0]
right_coord = -1
top_border = Coordinates[0][1]
top_coord = -1
bottom_border = Coordinates[0][1]
bottom_coord = -1

for i, coord in enumerate(Coordinates):
    if coord[0] < left_border:
        left_border = coord[0]
        left_coord = i
    if coord[0] > right_border:
        right_border = coord[0]
        right_coord = i
    if coord[1] > top_border:
        top_border = coord[1]
        top_coord = i
    if coord[1] < bottom_border:
        bottom_border = coord[1]
        bottom_coord = i

# have each ordered pair within the box as a tuple key of the Area dict; values are lists
#  where the first value is a coordinate index and the second is the distance from that
#  coordinate to the key

Interior = {}

# initialize by calculating each distance to the first coordinate

for i in range(left_border + 1, right_border):
    for j in range(bottom_border + 1, top_border):
        Interior[(i, j)] = [0, man_dist((i, j), Coordinates[0])]

# initialize by calculating each distance to the first coordinate

Border = {}

for i in range(left_border, right_border + 1):
    for j in [bottom_border, top_border]:
        Border[(i, j)] = [0, man_dist((i, j), Coordinates[0])]

for j in range(bottom_border, top_border + 1):
    for i in [left_border, right_border]:
        Border[(i, j)] = [0, man_dist((i, j), Coordinates[0])]

# now check to see which value from Coordinates is closes to each Interior key

for point in Interior.keys():
    for i, coord in enumerate(Coordinates):
        dist = man_dist(point, coord)
        if dist < Interior[point][1]:
            Interior[point][1] = dist
            Interior[point][0] = i
        elif dist == Interior[point][1]:
            # equidistant points are not owned by any point
            Interior[point][0] = -1

# now check to see which value from Coordinates is closes to each Border key

for point in Border.keys():
    for i, coord in enumerate(Coordinates):
        dist = man_dist(point, coord)
        if dist < Border[point][1]:
            Border[point][1] = dist
            Border[point][0] = i
        elif dist == Border[point][1]:
            # equidistant points are not owned by any point
            Border[point][0] = -1

# now iterate over Interior to store each coord from Coordinates and the number of points
#  it is closest to in Areas

Areas = {}

for point in Interior.keys():
    Areas.setdefault(Interior[point][0], 0)
    Areas[Interior[point][0]] += 1

# now find which coords in Coordinate are closest to a border point

BorderCords = []

for value in Border.values():
    if value[0] not in BorderCords:
        BorderCords.append(value[0])

# now find the largest finite area

max_area = 0

for point, area in Areas.items():
    if point not in BorderCords:
        print(point, area)
        max_area = max(max_area, area)

print("The largest finite area is", max_area)

