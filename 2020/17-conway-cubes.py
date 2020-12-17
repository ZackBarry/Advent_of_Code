import numpy as np
import copy

input = open('2020/17-input.txt').read().splitlines()

grid = {}

for x in range(-20, 20):
    for y in range(-20, 20):
        for z in range(-20, 20):
            grid[(x,y,z)] = '.'


def get_neighbors(x,y,z):
    neighbors = []
    for xp in range(x-1, x+2):
        for yp in range(y-1, y+2):
            for zp in range(z-1, z+2):
                if [xp,yp,zp] != [x,y,z]:
                    neighbors += [(xp,yp,zp)]
    return neighbors


def count_state(coords, gridt):
    active = 0
    inactive = 0
    for coord in coords:
        if gridt[coord] == '#':
            active += 1
        else:
            inactive += 1
    return {'active': active, 'inactive': inactive}


for y, l in enumerate(input):
    points = list(l)
    for x, v in enumerate(points):
        grid[(x,y,0)] = v

stable_grid = copy.deepcopy(grid)

grid = copy.deepcopy(stable_grid)

import time
for i in range(0, 6):
    print(i)
    print(time.time)
    new_grid = copy.deepcopy(grid)
    for point, state in grid.items():
        if (-18 < point[0] < 18) and (-18 < point[1] < 18) and (-18 < point[2] < 18):
            neighbor_count = count_state(get_neighbors(point[0], point[1], point[2]), grid)
            if state == '#':
                if neighbor_count['active'] not in [2, 3]:
                    new_grid[point] = '.'
            if state == '.':
                if neighbor_count['active'] == 3:
                    new_grid[point] = '#'
    grid = copy.deepcopy(new_grid)


active = 0

for state in grid.values():
    if state == '#':
        active += 1

print(active)

# part 2


grid = {}

for x in range(-10, 16):
    for y in range(-10, 16):
        for z in range(-10, 16):
            for w in range(-10, 16):
                grid[(x,y,z,w)] = '.'


def get_neighbors4(x,y,z,w):
    neighbors = []
    for xp in range(x-1, x+2):
        for yp in range(y-1, y+2):
            for zp in range(z-1, z+2):
                for wp in range(w-1, w+2):
                    if [xp,yp,zp,wp] != [x,y,z,w]:
                        neighbors += [(xp,yp,zp,wp)]
    return neighbors


def count_state4(coords, gridt):
    active = 0
    inactive = 0
    for coord in coords:
        if gridt[coord] == '#':
            active += 1
        else:
            inactive += 1
    return {'active': active, 'inactive': inactive}


for y, l in enumerate(input):
    points = list(l)
    for x, v in enumerate(points):
        grid[(x,y,0,0)] = v

stable_grid = copy.deepcopy(grid)

grid = copy.deepcopy(stable_grid)

for i in range(0, 6):
    print(i)
    new_grid = copy.deepcopy(grid)
    for point, state in grid.items():
        if (-10 < point[0] < 15) and (-10 < point[1] < 15) and (-10 < point[2] < 15) and (-10 < point[3] < 15):
            neighbor_count = count_state4(get_neighbors4(point[0], point[1], point[2], point[3]), grid)
            if state == '#':
                if neighbor_count['active'] not in [2, 3]:
                    new_grid[point] = '.'
            if state == '.':
                if neighbor_count['active'] == 3:
                    new_grid[point] = '#'
    grid = copy.deepcopy(new_grid)


active = 0

for state in grid.values():
    if state == '#':
        active += 1

print(active)