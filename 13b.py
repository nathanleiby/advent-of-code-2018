def intersection(car):
    # print("intersection:", car)
    old_dir = car[1]
    num_turns = car[2]
    x = num_turns % 3

    if x == 0:
        # "left"
        if old_dir == "<":
            return "v"
        elif old_dir == "v":
            return ">"
        elif old_dir == ">":
            return "^"
        else:
            return "<"
    elif x == 1:
        return old_dir
    elif x == 2:
        # "right"
        if old_dir == ">":
            return "v"
        elif old_dir == "^":
            return ">"
        elif old_dir == "<":
            return "^"
        else:
            return "<"


from copy import deepcopy


def print_grid(grid, cars=[]):
    # TODO: Optionally, show the cars
    grid_copy = deepcopy(grid)

    # show cars
    for c in cars:
        c_loc = c[0]
        c_dir = c[1]
        c_x, c_y = c_loc[0], c_loc[1]
        # flip col, row
        grid_copy[c_y][c_x] = c_dir

    for l in grid_copy:
        print("".join(l))


def grid_val(grid, loc):
    x, y = loc[0], loc[1]
    return grid[y][x]


compute_new_dir = {
    "/": {"<": "v", ">": "^", "v": "<", "^": ">"},
    "\\": {"<": "^", ">": "v", "v": ">", "^": "<"},
}


def res(input):
    # convert input to coordinates, and determine track at each location
    # 1. location
    # 2. direction
    # 3. # of turns

    # make a grid
    lines = input.splitlines()

    # find initial cars location.. save their locations as | if ^ v OR - if < >
    grid = []
    # TODO: name the cars uniquely, so it's easier to find collisions
    # Only add them back if they DID NOT collide
    # # TODO: name the cars uniquely, so it's easier to find collisions
    # Only add them back if they DID NOT collide
    cars = []
    car_number = 0
    for l_idx, l in enumerate(lines):
        out = []
        for c_idx, c in enumerate(l):
            if c in ["<", ">", "v", "^"]:
                if c in ["<", ">"]:
                    out += ["-"]
                else:
                    out += ["|"]
                # car = (x, y), direction, num_turns, unique_id
                cars.append(((c_idx, l_idx), c, 0, car_number))
                car_number += 1
            else:
                out += [c]
        grid.append(out)

    # handle movement
    crashed_cars = set()
    num_crashed = -1
    for round in range(0, 20000):
        if len(crashed_cars) != num_crashed:
            num_crashed = len(crashed_cars)
            print("ROUND ", round, "# cars crashed = ", num_crashed)

        new_cars = []
        print(len(cars))
        if len(crashed_cars) + 1 == len(cars):
            print("HERE")
            print(crashed_cars)
            for c in cars:
                if c[3] not in crashed_cars:
                    return c[0]

        cars.sort(key=lambda c: (c[0][1], c[0][0]))
        # if round == 164 or round == 165:
        #     print("ROUND #", round)
        #     for c in cars:
        #         print(c[0], c[1], c[3])
        #     print("")
        # if round == 165:
        #     break
        for c in cars:
            # move
            old_loc, old_dir, old_num_turns, old_car_num = c[0], c[1], c[2], c[3]
            old_x, old_y = old_loc[0], old_loc[1]
            old_tile = grid[old_y][old_x]
            # print(old_tile)

            # MOVE
            if old_dir == "v":
                new_loc = (old_x, old_y + 1)
            elif old_dir == "^":
                new_loc = (old_x, old_y - 1)
            elif old_dir == "<":
                new_loc = (old_x - 1, old_y)
            elif old_dir == ">":
                new_loc = (old_x + 1, old_y)
            else:
                print("Invalid Direction: {}".format(old_dir))
                raise ()

            # TURN
            # compute new_dir
            new_num_turns = old_num_turns
            new_dir = None
            new_x, new_y = new_loc[0], new_loc[1]
            new_loc_symbol = grid[new_y][new_x]
            if new_loc_symbol in compute_new_dir:
                new_dir = compute_new_dir[new_loc_symbol][old_dir]
            elif new_loc_symbol == "+":
                new_dir = intersection(c)
                new_num_turns += 1
            else:
                new_dir = old_dir

            new_c = (new_loc, new_dir, new_num_turns, old_car_num)
            new_cars.append(new_c)

            # check for crashes
            # if round == 164 and c[3] == 15:
            #     print(len(cars))

            #     print(cars)
            #     print(list(map(lambda x: x[3], cars)))

            #     import ipdb
            #     ipdb.set_trace()

            to_compare = cars + new_cars
            if new_c[3] not in crashed_cars:
                for other_car in to_compare:
                    if other_car[3] in crashed_cars:
                        # cant crash twice
                        continue
                    if other_car[3] == old_car_num:
                        # cant crash into self
                        continue
                    if new_loc == other_car[0]:
                        crashed_cars.add(new_c[3])
                        crashed_cars.add(other_car[3])
                        break


with open("./13b-ex-input", "r") as f:
    ex_i = f.read()

ex_o_expected = (6, 4)

ex_o = res(ex_i)
print("ex_o", ex_o)
assert ex_o == ex_o_expected

actual_i = None
with open("./13-input", "r") as f:
    actual_i = f.read()

actual_o = res(actual_i)
print(actual_o)
