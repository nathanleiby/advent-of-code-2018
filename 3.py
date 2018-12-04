import pandas as pd


# there are 3 states you can be in
# 1. no claim
# 2. one claim
# 3. >1 claim

# let's model this as a 1000x1000 matrix where the value at an index
# is equivent to the number of claims

# def process_claim(fabric, claim_string):
# convert claim string to location
# update the fabric

DEBUG = False

def convert_claim_to_loc(line):
    print(line)
    s = line.split("@")
    claim_num = int(s[0][1:])
    s2 = s[1].split(":")

    x_y, width_height = s2[0], s2[1]

    split_x_y = x_y.split(",")
    x, y = int(split_x_y[0]), int(split_x_y[1])

    split_width_height = width_height.split("x")
    width, height = int(split_width_height[0]), int(split_width_height[1])
    if DEBUG:
        print("x", x)
        print("y", y)
        print("width", width)
        print("height", height)
    return claim_num, x, y, width, height


def write_claim(df, claim):
    claim_num, x, y, width, height = claim
    # TODO: Possible to increment value by 1? e.g. via lambda
    # df.loc[range(y, y+height), range(x, x+width)] = 1
    df.loc[range(y, y+height), range(x, x+width)] = df.loc[range(y, y+height), range(x, x+width)] + 1

def count_multiple_claims(df):
    total = 0
    for i, row in df.iterrows():
        for j, val in row.iteritems():
            if val > 1:
                total += 1

    return total

# Testing things out with a small dataframe (10x10)
size = 10
df_small = pd.DataFrame(index=range(size), columns=range(size))
df_small = df_small.fillna(0)

converted = convert_claim_to_loc("#1 @ 306,433: 16x11")
assert converted == (1, 306, 433, 16, 11)
assert(count_multiple_claims(df_small) == 0)

print("")
print("BEFORE")
print(df_small)

write_claim(df_small, convert_claim_to_loc("#1 @ 1,3: 4x4"))
write_claim(df_small, convert_claim_to_loc("#2 @ 3,1: 4x4"))
write_claim(df_small, convert_claim_to_loc("#3 @ 5,5: 2x2"))

print("AFTER")
print(df_small)


assert(count_multiple_claims(df_small) == 4)

# OK So it's working for the example. let's try a new one!
size = 1000
df_big = pd.DataFrame(index=range(size), columns=range(size))
df_big = df_big.fillna(0)



with open("./3-input", "r") as f:
    lines = f.readlines()
    for line in lines:
        write_claim(df_big, convert_claim_to_loc(line))

print("RESULT = ", count_multiple_claims(df_big))
