ex_i = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

# no meta
simple_i =  "2 0 1 0 0 0 0 0"
            #A - B - C - D
            #A
            #|\
            #B D
            #|
            #C

# def get_next_node(remaining):
#     i = remaining
#     num_children, num_meta = int(i[0]), int(i[1])
#     print("num_children={} num_meta={}".format(num_children, num_meta))
#     children = list(map(int, i[2:2+num_children]))
#     for c in children:

#         children, num_meta, new_remaining = get_next_node(remaining)
#         collect all meta
#     new_remaining = remaining[num_meta+num_children:]

#     meta = list(map(int, i[2+num_children:2+num_children+num_meta]))

#     print('children:', children)
#     print('meta:', meta)
#     print("")
#     assert(len(children) == num_children)
#     assert(len(meta) == num_meta)

#     return children, meta, new_remaining

# nums = inp.strip().split(" ")

# class Node(object):
#     children = [] # nodes
#     meta = [] # nums

import sys
#print(sys.getrecursionlimit())
#print(sys.setrecursionlimit(5000))


# NON-recursive.. just make a stack and keep digging until no children..
# then do meta and walk up until children again..
def build_tree(inp):
    nums = list(map(int, inp.strip().split(" ")))
    # get num_children, num_meta
    # for each child
    # misses the 0th thing
    return next_node(nums)

# nodes is the list of nodes so far
# i is list of remaining nums
# RETURN: list of nodes and their metadata
def next_node(i):
    print(i)
    num_children, num_meta = int(i[0]), int(i[1])
    print("num_children={} num_meta={}".format(num_children, num_meta))
    i = i[2:]
    meta = []


    # base case -- no more children to recurse, so we can collect meta
    if num_children == 0:
        # return the node and the meta
        n = i[:num_meta]
        print("meta ... ", n)
        return n, list(map(int, i[num_meta:]))
    # recurse through all the children
    else:
        subnodes = []
        for c in range(num_children):
            ns, i = next_node(i)
            subnodes = subnodes + ns
            print("subnodes ... ", subnodes)
        return subnodes, i


def res(inp):
    meta = build_tree(inp)
    print("M", meta)
    d = []
    for m in meta:
        d += m

    return(sum(d))

print("== SIMPLE ==")
meta = build_tree(simple_i)
print(meta)

print("")
print("== EXAMPLE ==")
ex_o = res(ex_i)
print("example => ", ex_o)
assert(ex_o == 138)

with open('./8-input', 'r') as f:
    dat = f.read()
    o = ""
    #o = res(dat)
    print("RESULT => ", o)
