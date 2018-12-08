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
        return n, list(map(int, i[num_meta:]))
    # recurse through all the children
    else:
        subnodes = []
        for c in range(num_children):
            ns, i = next_node(i)
            subnodes = subnodes + ns
            print("subnodes ... ", subnodes)
        return subnodes, i

class Node(object):
    num_children = -1
    num_meta = -1
    #children = []
    children_done = 0
    meta = []

# i is full list of #s
cur_node_num = ord('A') -1
def no_recursion(i):
    i = list(map(int, i.strip().split(" ")))

    nodes_to_process = []
    cur_idx = 0
    def next_node_name():
        global cur_node_num
        cur_node_num += 1 
        return chr(cur_node_num)

    all_meta = []
    while cur_idx < len(i):
        print("")
        print("cur_idx", cur_idx, "cur_val", i[cur_idx])
        #import ipdb
        #ipdb.set_trace()
        # add the first node
        print("NODES TO PROCESS:", list(map(lambda x: x.name, nodes_to_process)))
        if len(nodes_to_process) == 0:
            print("top branch")
            num_children, num_meta = int(i[cur_idx]), int(i[cur_idx+1])
            cur_node = Node()
            cur_node.name = next_node_name()
            cur_node.num_children = num_children
            cur_node.num_meta = num_meta
            nodes_to_process.append(cur_node)
            cur_idx += 2
        else:
            print("bottom branch")
            # process last node in list
            last_node = nodes_to_process[-1]
            #print("LN: nc={} c={}".format(last_node.num_children, last_node.children))
            # print(last_node, last_node.num_children, len(last_node.children))
            print("{} ... {}/{} ... num_meta={}".format(last_node.name, last_node.children_done, last_node.num_children, last_node.num_meta))
            #if len(last_node.children) != last_node.num_children:
            if last_node.children_done != last_node.num_children:
                num_children, num_meta = int(i[cur_idx]), int(i[cur_idx+1])
                cur_idx += 2

                child = Node()
                child.name = next_node_name()
                child.num_children = num_children
                child.num_meta = num_meta
                nodes_to_process.append(child)
                last_node.children_done += 1

            else:
                last_node.meta = i[cur_idx:cur_idx+last_node.num_meta]
                print("num_meta:", last_node.num_meta)
                print("meta:", last_node.meta)
                cur_idx += last_node.num_meta

                all_meta += last_node.meta

                nodes_to_process.pop()

    return(all_meta)


def res(inp):
    meta = build_tree(inp)
    print("M", meta)
    d = []
    for m in meta:
        d += m

    return(sum(d))

#print("== SIMPLE ==")
#meta = build_tree(simple_i)
#print("No recursion")
#m2 = no_recursion(simple_i)

#print(meta)
#print(m2)

print("")
print("== EXAMPLE ==")
ex_o = res(ex_i)
print("example => ", ex_o)

print("no recursion")
ex_o2 = no_recursion(ex_i)
print(sum(ex_o2))


assert(ex_o == 138)
assert(sum(ex_o2) == 138)

with open('./8-input', 'r') as f:
    dat = f.read()
    o = ""
    o = no_recursion(dat)
    print(o)
    print("RESULT => ", sum(o))
