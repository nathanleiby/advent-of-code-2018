
def rack_id(x):
    return x+10

def compute_power(x,y,serial_number):
    # Find the fuel cell's rack ID, which is its X coordinate plus 10.
    rid = rack_id(x)
    # Begin with a power level of the rack ID times the Y coordinate.
    pwr = rid * y
    # Increase the power level by the value of the grid serial number (your puzzle input).
    pwr += serial_number
    # Set the power level to itself multiplied by the rack ID.
    pwr *= rid
    # Keep only the hundreds digit of the power level
    # (so 12345 becomes 3; numbers with no hundreds digit become 0).
    pwr = (pwr // 100) % 10
    # Subtract 5 from the power level.
    pwr -= 5
    return pwr

def compute_square(pts, x, y, size, squares):
    total_power = 0
    if size > 1:
       total_power += squares[(x,y,size-1)]

    y2 = y+size-1
    for x2 in range(x, x+size):
        total_power += pts[(x2, y2)]
    x2 = x+size-1
    for y2 in range(y, y+size-1): # -1 to skip overlapping point
        total_power += pts[(x2, y2)]

    return total_power

def run(serial_number):
    # compute_power_levels
    pts = {}
    for x in range(1, 301):
        for y in range(1,301):
            pts[(x,y)] = compute_power(x,y, serial_number)


    max_power = -1
    max_power_coords = None
    MAX = 300
    squares = {}

    # TODO: Is there a dynamic programming solution here?
    import time
    big_start = time.time()
    for size in range(1, MAX+1):
        start = time.time()
        for x in range(1, MAX+2-size):
            for y in range(1, MAX+2-size):
                # compute power
                # compute sub-squares and reuse their values
                power = compute_square(pts, x, y, size, squares)
                squares[(x,y,size)] = power
                if power > max_power:
                    max_power = power
                    max_power_coords = (x, y, size)
        end = time.time()
        if size == 3 and serial_number == 18:
            test_pt = (33,45,3)
            actual = squares[test_pt]
            expected = 29
            print("OLD ANSWER for pt {} was {} expected {}".format(test_pt, actual, expected))
            assert(actual == expected)
        print("Size {:4} took {:.2f} seconds (total = {:.2f}s) ... {} => {}".format(size, end-start, end-big_start, max_power_coords, max_power))

    return pts, max_power, max_power_coords

# ex_i=18
# pts, max_power, max_power_coords = run(ex_i)
# print(max_power, max_power_coords)
# assert(max_power == 113)
# assert(max_power_coords == (90,269,16))

# ex_i=42
# pts, max_power, max_power_coords = run(ex_i)
# print(max_power, max_power_coords)
# assert(max_power == 119)
# assert(max_power_coords == (232,251,12))

ex_i=8141
pts, max_power, max_power_coords = run(ex_i)
print(max_power, max_power_coords)
