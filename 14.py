DEBUG = False
def print_recipes(recipes, elf1, elf2):
    out = ""
    for idx, rec in enumerate(recipes):
        l = r = " "
        if idx == elf1:
            l = "("
            r = ")"
        if idx == elf2:
            l = "["
            r = "]"
        out += (l + str(rec) + r)
    if DEBUG:
        print(out)

import time

def res(input, expected=None):
    # QUALITY: 0-9
    # current recipe is an index in the array
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    iters = 0
    start = time.time()
    iter_start = start
    while len(recipes) < input+10:
        iters += 1
        if iters % 1000 == 0:
            now = time.time()
            elapsed = now - iter_start
            total_elapsed = now - start

            iter_start = now
            print("iters:", iters, "   # recipes = ", len(recipes), " iter time={:.1f}s (total = {:.1f}s)".format(elapsed, total_elapsed))
        print_recipes(recipes, elf1, elf2)
        # COMBINE (sum scores), then create a new recipe with score of each digit
        combined = recipes[elf1] + recipes[elf2]
        c_str = str(combined)
        new_recipes = list(map(int, [x for x in c_str]))
        recipes += new_recipes

        # step forward (1 + number of current recipe), looping if needed
        elf1 = (elf1 + 1+ recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1+ recipes[elf2]) % len(recipes)

    print_recipes(recipes, elf1, elf2)

    out = "".join(list(map(str, recipes))[input:input+10])

    # choose recipe

    print("OUTPUT")
    print(out)
    print("")

    if expected:
        print(input, "=>", out, "(expected: ", expected, ")")
        assert(out == expected)

    return out


print("EXAMPLES")

res(9, "5158916779")
res(5, "0124515891")
res(18, "9251071085")
res(2018, "5941429882")

print("ACTUAL")
actual = res(430971)
