with open('6-input', 'r') as f:
    data = f.read().strip() # read and remove whitespace

example_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

"""
Your goal is to find the size of the largest area that isn't infinite.

FINITE iff none of its boundaries are at the edge of the map
"""
def print_square(s):
    print("")
    if not DEBUG:
        return
    for l in s:
        print("".join(l))

import math
def mdistance(c1, c2):
    return math.fabs(c1[0] - c2[0]) + math.fabs(c1[1] - c2[1])

def do(inp):
    lines = inp.splitlines()
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    all_coords = {}
    for idx, l in enumerate(lines):
        coords = list(map(int, l.split(", ")))
        x,y  = coords[0], coords[1]
        all_coords[idx] = (x,y)
        print(x,y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    print("MAX X = ", max_x, "MAX Y = ", max_y)

    square_size = max(max_x+1, max_y+1)
    square = []
    for a in range(square_size):
        square.append(["."]*square_size)

    print_square(square)

    for c in all_coords:
        cc = all_coords[c]
        # print(cc)
        square[cc[1]][cc[0]] = str(c) # str(chr(c+65))

    # preview square before owners
    print_square(square)

    # assign an owner to each
    for l_y, _ in enumerate(square):
        for l_x, _ in enumerate(square): # find closest coord
            total_distance = 0
            for c in all_coords:
                cc = all_coords[c]
                sq_coord = (l_y, l_x)
                dis = mdistance(cc, sq_coord)
                total_distance += dis
            # example
            if total_distance < MAX_DISTANCE:
                square[l_x][l_y] = str("#")

    print_square(square)

    # compute size of each area
    from collections import Counter
    cnt = Counter()
    to_ignore = set()

    for idx_r, r in enumerate(square):
        for idx_c, c in enumerate(r):
            val = square[idx_r][idx_c]
            cnt[val] += 1 
            if idx_r == 0 or idx_r == (len(square) -1):
                to_ignore.add(val)

    exp_cnt_total = square_size**2
    print("COUNT VS SQUARE SIZE")
    total_cnt = 0
    for t in cnt:
        total_cnt +=  cnt[t]
    print(total_cnt)
    print(exp_cnt_total)

    print(cnt)
    print(to_ignore)
    for i in to_ignore:
        del(cnt[i])

    print("CLEANed UP OUTPUT... sorted")
    print(cnt)

    # TODO: Throw away if at edge
    # TODO: Why was top one d-q??
    # size of grid = 0,0 => max_x, max_y
    out = ""

    return out

expected = ""
MAX_DISTANCE =32
DEBUG = True
assert(do(example_input) == expected)

DEBUG = False
MAX_DISTANCE=10000
do(data)
