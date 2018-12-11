
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

def compute_3x3(pts, x, y):
    total_power = 0
    for x2 in range(x, x+3):
        for y2 in range(y, y+3):
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
    MAX = 301-2
    for x in range(1, MAX):
        for y in range(1, MAX):
            # compute power
            power = compute_3x3(pts, x, y)
            if power > max_power:
                max_power = power
                max_power_coords = (x, y)


    return pts, max_power, max_power_coords

ex_i=18
pts, max_power, max_power_coords = run(ex_i)
print(max_power, max_power_coords)

ex_i=42
pts, max_power, max_power_coords = run(ex_i)
print(max_power, max_power_coords)

ex_i=8141
pts, max_power, max_power_coords = run(ex_i)
print(max_power, max_power_coords)
