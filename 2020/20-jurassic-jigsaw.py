from copy import deepcopy

input = open('2020/20-input.txt').read().split('\n\n')[:-1]

images = {}
for x in input:
    print(x)
    sep = x.splitlines()
    id = sep[0][5:-1]
    image = sep[1:]
    images[int(id)] = image

# part 1

right_border = {}
left_border = {}
top_border = {}
bottom_border = {}

for id, image in images.items():
    right_border[id] = [x[-1] for x in image]
    left_border[id] = [x[0] for x in image]
    top_border[id] = list(image[0])
    bottom_border[id] = list(image[-1])

right_match = {}
left_match = {}
top_match = {}
bottom_match = {}
all_match = {}

corner_prod = 1
found = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

for id in images.keys():
    right_match[id] = -1
    left_match[id] = -1
    top_match[id] = -1
    bottom_match[id] = -1
    all_match[id] = [-1,-1,-1,-1]
    right = right_border[id]
    left = left_border[id]
    top = top_border[id]
    bottom = bottom_border[id]
    found_matches = 0
    for idp in images.keys():
        if idp != id:
            rightp = right_border[idp]
            rightpr = rightp[::-1]
            leftp = left_border[idp]
            leftpr = leftp[::-1]
            topp = top_border[idp]
            toppr = topp[::-1]
            bottomp = bottom_border[idp]
            bottompr = bottomp[::-1]
            if right in [rightp, leftp, topp, bottomp, rightpr, leftpr, toppr, bottompr]:
                found_matches += 1
                right_match[id] = idp
                all_match[id][3] = idp
            elif left in [rightp, leftp, topp, bottomp, rightpr, leftpr, toppr, bottompr]:
                found_matches += 1
                left_match[id] = idp
                all_match[id][1] = idp
            elif top in [rightp, leftp, topp, bottomp, rightpr, leftpr, toppr, bottompr]:
                found_matches += 1
                top_match[id] = idp
                all_match[id][2] = idp
            elif bottom in [rightp, leftp, topp, bottomp, rightpr, leftpr, toppr, bottompr]:
                found_matches += 1
                bottom_match[id] = idp
                all_match[id][0] = idp
    found[found_matches] += 1
    if found_matches == 2:
        print(f'corner id: {id}')
        corner_prod *= id

print(corner_prod)

# part 2

def flip_image(image_id, direction):
    image = images[image_id]
    if direction == 'v':
        images[image_id] = image[::-1]
        top_m = top_match[image_id]
        bot_m = bottom_match[image_id]
        top_match[image_id] = bot_m
        bottom_match[image_id] = top_m
        top_b = top_border[image_id]
        bot_b = bottom_border[image_id]
        top_border[image_id] = bot_b
        bottom_border[image_id] = top_b
        r_b = right_border[image_id]
        right_border[image_id] = r_b[::-1]
        l_b = left_border[image_id]
        left_border[image_id] = l_b[::-1]
    elif direction == 'h':
        images[image_id] = [''.join(list(x)[::-1]) for x in image]
        r_m = right_match[image_id]
        l_m = left_match[image_id]
        right_match[image_id] = l_m
        left_match[image_id] = r_m
        r_b = right_border[image_id]
        l_b = left_border[image_id]
        right_border[image_id] = l_b
        left_border[image_id] = r_b
        t_b = top_border[image_id]
        top_border[image_id] = t_b[::-1]
        b_b = bottom_border[image_id]
        bottom_border[image_id] = b_b[::-1]


def rotate_image(image_id, degrees):
    image = images[image_id]
    new_image = []
    # rotate 90 degrees
    for i in range(0, len(image)):
        # first row is last col
        new_image += [''.join([x[-(i+1)] for x in image])]
    images[image_id] = new_image
    top_m = top_match[image_id]
    bot_m = bottom_match[image_id]
    r_m = right_match[image_id]
    l_m = left_match[image_id]
    right_match[image_id] = bot_m
    left_match[image_id] = top_m
    top_match[image_id] = r_m
    bottom_match[image_id] = l_m
    top_b = top_border[image_id]
    bot_b = bottom_border[image_id]
    r_b = right_border[image_id]
    l_b = left_border[image_id]
    right_border[image_id] = bot_b[::-1]
    left_border[image_id] = top_b[::-1]
    top_border[image_id] = r_b
    bottom_border[image_id] = l_b
    degrees -= 90
    if degrees != 0:
        rotate_image(image_id, degrees)


grid_by_row = {}

start_id = 2789 #1951 #2789 # has matches on the right and bottom
#flip_image(start_id, 'v') ### !!! for 1951 only

row_id = 0

while start_id != -1:
    this_row = [start_id]
    anchor_id = start_id
    right_id = right_match[start_id]

    while right_id != -1:
        anchor_right_border = right_border[anchor_id]
        if anchor_right_border == left_border[right_id]:
            print('ok')
        elif anchor_right_border == left_border[right_id][::-1]:
            flip_image(right_id, 'v')
        elif anchor_right_border == right_border[right_id]:
            flip_image(right_id, 'h')
        elif anchor_right_border == right_border[right_id][::-1]:
            flip_image(right_id, 'h')
            flip_image(right_id, 'v')
        elif anchor_right_border == top_border[right_id]:
            rotate_image(right_id, 90)
            flip_image(right_id, 'v')
        elif anchor_right_border == top_border[right_id][::-1]:
            rotate_image(right_id, 90)
        elif anchor_right_border == bottom_border[right_id]:
            rotate_image(right_id, 270)
        elif anchor_right_border == bottom_border[right_id][::-1]:
            rotate_image(right_id, 270)
            flip_image(right_id, 'v')
        this_row += [right_id]
        anchor_id = right_id
        right_id = right_match[anchor_id]

    grid_by_row[row_id] = this_row
    row_id += 1

    start_bottom_border = bottom_border[start_id]
    bottom_id = bottom_match[start_id]

    if bottom_id == -1:
        break

    if start_bottom_border == left_border[bottom_id]:
        rotate_image(bottom_id, 270)
        flip_image(bottom_id, 'h')
    elif start_bottom_border == left_border[bottom_id][::-1]:
        rotate_image(bottom_id, 270)
    elif start_bottom_border == right_border[bottom_id]:
        rotate_image(bottom_id, 90)
    elif start_bottom_border == right_border[bottom_id][::-1]:
        rotate_image(bottom_id, 90)
        flip_image(bottom_id, 'h')
    elif start_bottom_border == top_border[bottom_id]:
        print('ok')
    elif start_bottom_border == top_border[bottom_id][::-1]:
        flip_image(bottom_id, 'h')
    elif start_bottom_border == bottom_border[bottom_id]:
        rotate_image(bottom_id, 180)
        flip_image(bottom_id, 'h')
    elif start_bottom_border == bottom_border[bottom_id][::-1]:
        rotate_image(bottom_id, 180)

    start_id = bottom_id


full_grid = []

for row_id, image_ids in grid_by_row.items():
    for i in range(0, len(images[image_ids[0]])):
        if i not in [0, 9]:
            full_row = ''
            for id in image_ids:
                full_row += images[id][i][1:-1]
            full_grid += [full_row]


def check_monster(grid, r, c):
    t = grid[r][c:(c+20)]
    if len(t) < 20:
        return False
    m = grid[r+1][c:(c+20)]
    b = grid[r+2][c:(c+20)]
    t_obs = [obs for i, obs in enumerate(list(t)) if i in [18]]
    m_obs = [obs for i, obs in enumerate(list(m)) if i in [0,5,6,11,12,17,18,19]]
    b_obs = [obs for i, obs in enumerate(list(b)) if i in [1,4,7,10,13,16]]
    if [t_obs.count('#'), m_obs.count('#'), b_obs.count('#')] == [1,8,6]:
        return True


def rotate_full_grid(g):
    new_g = []
    for i in range(0, len(g)):
        # first row is last col
        new_g += [''.join([x[-(i+1)] for x in g])]
    return new_g


def flip_full_grid(g, dir):
    new_g = []
    if dir == 'v':
        new_g = g[::-1]
    elif dir == 'h':
        new_g = [''.join(list(x)[::-1]) for x in g]
    return new_g


found_monsters = 0
turns = 0
grid = deepcopy(full_grid)

while found_monsters == 0 and turns < 18:
    r = 0
    while r <= (len(grid) - 3):
        row = grid[r]
        c = 0
        while c <= (len(grid[r]) - 20):
            if check_monster(grid, r, c):
                print(f'{r}, {c}')
                found_monsters += 1
            c += 1
        r += 1
    grid = rotate_full_grid(grid)
    turns += 1
    if turns == 5:
        grid = flip_full_grid(grid, 'v')
    elif turns == 9:
        grid = flip_full_grid(grid, 'v')
        grid = flip_full_grid(grid, 'h')
    elif turns == 13:
        grid = flip_full_grid(grid, 'h')
        grid = flip_full_grid(grid, 'v')
        grid = flip_full_grid(grid, 'h')
    print(turns)


found_hashes = 0
for r in full_grid:
    found_hashes += r.count('#')

print(f'{found_hashes - found_monsters * 15}')

