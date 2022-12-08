from collections import defaultdict


def part_one(trees):
    num_rows = len(trees)
    num_cols = len(trees[0])
    can_see = 0

    for r in range(num_rows):
        for c in range(num_cols):
            tree = trees[r][c]
            visible = False

            if all([trees[r][_c] < tree for _c in range(0, c)]):
                visible = True
            elif all([trees[r][_c] < tree for _c in range(c + 1, num_cols)]):
                visible = True
            elif all([trees[_r][c] < tree for _r in range(0, r)]):
                visible = True 
            elif all([trees[_r][c] < tree for _r in range(r + 1, num_rows)]):
                visible = True

            can_see += visible
    
    return can_see


def part_two(trees):
    num_rows = len(trees)
    num_cols = len(trees[0])
    high_score = 0

    for r in range(num_rows):
        for c in range(num_cols):
            tree = trees[r][c]
            score = 1

            visible = 0
            for _c in list(range(0, c))[::-1]:
                visible += 1
                if trees[r][_c] >= tree:
                    break
            score *= visible
            
            visible = 0
            for _c in list(range(c + 1, num_cols)):
                visible += 1
                if trees[r][_c] >= tree:
                    break
            score *= visible

            visible = 0
            for _r in list(range(0, r))[::-1]:
                visible += 1
                if trees[_r][c] >= tree:
                    break
            score *= visible

            visible = 0
            for _r in list(range(r + 1, num_rows)):
                visible += 1
                if trees[_r][c] >= tree:
                    break
            score *= visible 

            high_score = max(score, high_score)
    
    return high_score


if __name__ == '__main__':
    input = open('08-input.txt').read().splitlines()

    rows = [[int(v) for v in list(r)] for r in input]

    print(f'Part 1: {part_one(rows)}')

    print(f'Part 2: {part_two(rows)}')
    