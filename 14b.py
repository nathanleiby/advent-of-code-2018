DEBUG = False
def print_recipes(recipes, elf1, elf2):
    if not DEBUG:
        return
    out = ""
    for idx, rec in enumerate(recipes):
        if rec == None:
            break
        l = r = " "
        if idx == elf1:
            l = "("
            r = ")"
        if idx == elf2:
            l = "["
            r = "]"
        out += (l + str(rec) + r)
    print(out)

import time

def sublistExists(list1, list2):
    sublist = ''.join(map(str, list2))
    full_list = ''.join(map(str, list1))
    no_nones = [x for x in full_list if x is not None]
    if sublist in no_nones:
        return True, full_list.index(sublist)
    return False, -1

def res(input, expected=None):
    # QUALITY: 0-9
    # current recipe is an index in the array
    elf1 = 0
    elf2 = 1

    iters = 0
    start = time.time()
    iter_start = start

    #if not expected:
    size = 10**8 + 10000

    recipes = [3,7] + ([None] * (size+100))
    num_recipes = 2
    backoff = 1
    #while recipes [-5:] != input:
    found = None
    #while not sublistExists(recipes[max(num_recipes-20,0):], list(map(str, input))):
    while True:
        iters += 1
        if iters % 10**backoff == 0:
            if backoff <= 5:
                backoff += 1
            check_start = time.time()
            found = sublistExists(recipes[:num_recipes], list(map(str, input)))
            check_end = time.time()
            # TODO: I could just check the last couple 
            print("time to check sublist = {}s".format(check_end - check_start))
            if found[0]:
                break
            now = time.time()
            elapsed = now - iter_start
            total_elapsed = now - start

            iter_start = now
            print("iters:", iters, "   # recipes = ", num_recipes, " iter time={:.1f}s (total = {:.1f}s)".format(elapsed, total_elapsed))

        print_recipes(recipes, elf1, elf2)

        # COMBINE (sum scores), then create a new recipe with score of each digit
        combined = recipes[elf1] + recipes[elf2]
        c_str = str(combined)
        new_recipes = list(map(int, [x for x in c_str]))
        for n_idx, n in enumerate(new_recipes):
            recipes[num_recipes+n_idx] = n
        num_recipes = num_recipes + len(new_recipes)

        # step forward (1 + number of current recipe), looping if needed
        elf1 = (elf1 + 1+ recipes[elf1]) % num_recipes
        elf2 = (elf2 + 1+ recipes[elf2]) % num_recipes

    print_recipes(recipes, elf1, elf2)

    out = found[1]

    # choose recipe

    #while not sublistExists(recipes[max(num_recipes-20,0):], list(map(str, input))):

    print("OUTPUT")

    print(out)
    print("")

    if expected:
        print(input, "=>", out, "(expected: ", expected, ")")
        assert(out == expected)

    return out


print("EXAMPLES")

res("51589", 9)
#res("01245", 5)
#res("92510", 18)
#res("59414", 2018)

print("ACTUAL")
actual = res("4309") # 3150712
actual = res("43097") # 15618532
actual = res("430971") # 20225706
