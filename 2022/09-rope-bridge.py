DIRS = {
    'R': [1, 0],
    'U': [0, 1],
    'L': [-1, 0],
    'D': [0, -1]
}

class Rope:
    def __init__(self, num_knots):
        self.num_knots = num_knots
        self.tail_index = num_knots - 1
        self.knots = [[0, 0]]
        self.tail_positions = set()

    def adjacent(self, h, t):
        dist_x = abs(self.knots[t][0] - self.knots[h][0])
        dist_y = abs(self.knots[t][1] - self.knots[h][1])
        return (dist_x <= 1 and dist_y <= 1)
    
    def log_tail(self):
        if len(self.knots) == self.num_knots:
            self.tail_positions.add((self.knots[-1][0], self.knots[-1][1]))
    
    def catchup(self, h, t):
        if self.knots[t][1] == self.knots[h][1]:  # same row
            self.knots[t][0] = (self.knots[t][0] + self.knots[h][0]) // 2
        elif self.knots[t][0] == self.knots[h][0]:  # same col
            self.knots[t][1] = (self.knots[t][1] + self.knots[h][1]) // 2
        else:  # diagonal
            if self.knots[t][0] < self.knots[h][0]:
                self.knots[t][0] += 1
            else:
                self.knots[t][0] -= 1
            if self.knots[t][1] < self.knots[h][1]:
                self.knots[t][1] += 1
            else:
                self.knots[t][1] -= 1
    
    def check_add_knot(self):
        if len(self.knots) < self.num_knots:
            if [0, 0] not in self.knots:
                self.knots.append([0, 0])

    def move(self, n, dir):
        delta_x = DIRS[dir][0]
        delta_y = DIRS[dir][1]

        for _ in range(n):
            self.knots[0][0] += delta_x
            self.knots[0][1] += delta_y
            for i in range(1, len(self.knots)):
                if not self.adjacent(i - 1, i):
                    self.catchup(i - 1, i)
            self.check_add_knot()
            self.log_tail()


if __name__ == '__main__':
    data = open('09-input.txt').read().splitlines()

    # part 1
    rope = Rope(num_knots=2)

    for instruction in data:
        dir = instruction.split(' ')[0]
        num = int(instruction.split(' ')[1])
        rope.move(num, dir)
    
    print(f'Part 1: {len(rope.tail_positions)}')

    # part 2
    rope = Rope(num_knots=10)

    for instruction in data:
        dir = instruction.split(' ')[0]
        num = int(instruction.split(' ')[1])
        rope.move(num, dir)
    
    print(f'Part 2: {len(rope.tail_positions)}')
