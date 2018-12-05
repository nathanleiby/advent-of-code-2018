example_input = "dabAcCaCBAcCcaDA"
example_output = "dabCBAcaDA"

def react_recursive(polymer):
    # print("react:", polymer)
    print("react: {} chars".format(len(polymer)))
    for idx, _ in enumerate(polymer):
        # end condition
        if idx == len(polymer) -1:
            return polymer
        cur, next = polymer[idx], polymer[idx+1]

        #print("cur {}, next {}".format(cur, next))
        if cur.islower() and next.isupper() and cur.upper() == next:
            return react(polymer[:idx] + polymer[idx+2:])

        if cur.isupper() and next.islower() and cur.lower() == next:
            return react(polymer[:idx] + polymer[idx+2:])

def react_iterative(polymer, start_idx):
    # print("react:", polymer)
    # print("react:", polymer[:20])
    # print("start_idx", start_idx)
    print("react: {} chars".format(len(polymer)))
    for idx in range(start_idx, len(polymer)):
        # end condition
        if idx == len(polymer) -1:
            return polymer, 0
        cur, next = polymer[idx], polymer[idx+1]

        #print("cur {}, next {}".format(cur, next))
        if cur.islower() and next.isupper() and cur.upper() == next:
            return polymer[:idx] + polymer[idx+2:], max([idx - 1, 0])

        if cur.isupper() and next.islower() and cur.lower() == next:
            return polymer[:idx] + polymer[idx+2:], max([idx -1, 0])

def react(polymer):
    last_output = ""
    input = polymer
    start_idx = 0
    while True:
        output, start_idx = react_iterative(input, start_idx)
        if output == input:
            break
        input = output
    return output

assert(react(example_input) == example_output)
assert(len(react(example_input)) == 10)


with open('./5-input', 'r') as f:
    polymer = f.read().strip()
    result = react(polymer)
    #print(result)
    print("RESULT => ", len(result))
