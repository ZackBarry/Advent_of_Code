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

Area = {}

# initialize by calculating each distance to the first coordinate

for i in range(left_border, right_border):
    for j in range(bottom_border, top_border):
        Area[(i, j)] = [0, man_dist((i, j), Coordinates[0])]

# now check to see which value from Coordinates is closes to each Area key

for point in Area.keys():
    for i, coord in enumerate(Coordinates):
        dist = man_dist(point, coord)
        if dist < Area[point][1]:
            Area[point][1] = dist
            Area[point][0] = i

# now iterate over Area to store each coord from Coordinates and the number of points
#  it is closest to in Finite_Areas

Finite_Areas = {}

for point in Area.keys():
    Finite_Areas.setdefault(Area[point][0], 0)
    Finite_Areas[Area[point][0]] += 1

# now find which coords in Coordinate are closest to infinite areas

Area2 = {}

for i in range(left_border - 1000, right_border + 1000):
    for j in [bottom_border - 1000, top_border + 1000]:
        Area2[(i, j)] = [0, man_dist((i, j), Coordinates[0])]

for j in range(bottom_border - 1000, top_border + 1000):
    for i in [left_border - 1000, right_border - 1000]:
        Area2[(i, j)] = [0, man_dist((i, j), Coordinates[0])]

for point in Area2.keys():
    for i, coord in enumerate(Coordinates):
        dist = man_dist(point, coord)
        if dist < Area2[point][1]:
            Area2[point][1] = dist
            Area2[point][0] = i

Infinite_Areas = {}

for point in Area2.keys():
    Infinite_Areas.setdefault(Area2[point][0], 0)
    Infinite_Areas[Area2[point][0]] += 1

print(sorted(Infinite_Areas.keys()))

max_area = -1

# tupled = [tuple(Coordinates[left_coord]), tuple(Coordinates[right_coord]), tuple(Coordinates[top_coord]), tuple(Coordinates[bottom_coord])]

for point, area in Finite_Areas.items():
    if point not in Infinite_Areas.keys():
        print(point)
        max_area = max(max_area, area)

# print(tupled)

print("The largest finite area is", max_area)

