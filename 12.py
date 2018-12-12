ex_i = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""

ex_o_expected = 325

def parse_rule(rule):
    inputs = rule[0:5]
    output = rule[9]
    return tuple(inputs), output
 

def compute(ppots, edge):
    cur_pot = 0 - len(edge)
    total = 0
    for letter in ppots:
        if letter == "#":
            total += cur_pot

        cur_pot += 1
    return total

def run(input):
    lines = input.splitlines()
    pots_initial = lines[0][len("initial state: "):]
    # edge = "."*4*10 # extend edges  .. based on algo + generations TODO
    #edge = "."*30 # extend edges  .. based on algo + generations TODO
    edge = "."*1000 # extend edges  .. based on algo + generations TODO

    pots = edge + pots_initial + edge
    rules_map = {}

    rules = lines[2:]
    rules = list(map(parse_rule, rules))
    for r in rules:
        rules_map[r[0]] = r[1]

    for k in rules_map:
        print("{} => {}".format("".join(k), rules_map[k]))

    GENERATIONS = 300

    print(pots)
    last_val = 0
    for g in range(0, GENERATIONS):
        new_pots = ".."
        for i in range(2, len(pots) - 2):
            compare_vs = pots[i-2:i+3]
            #print("idx = {} COMPARE = {}".format(i, compare_vs))
            new_pots += rules_map.get(tuple(compare_vs), ".")
            #print(new_pots)
        new_pots += ".."
        pots = new_pots
        #print(pots)
        val  = compute(pots, edge)
        diff = val - last_val
        last_val = val
        print("val = {} diff = {}".format(val, diff))

        if "#" in [pots[2], pots[3], pots[4], pots[-2], pots[-3], pots[-4]]:
            print("G", g)
            raise "Boundary"

    return compute(pots, edge)

# ex_o = run(ex_i)
# print("ex_o:", ex_o)
# assert(ex_o == ex_o_expected)

actual_i = open("12-input", "r").read()
actual_o = run(actual_i)
print(actual_o)

# IDEA FOR B: look for a cycle, and figure out the length of that cycle

# UPDATE: after a point, it's +88 per generation
gen_300 = 26704
res = gen_300 + 88*49999999700
print(res)
