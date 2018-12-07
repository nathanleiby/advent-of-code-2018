from toposort import toposort, toposort_flatten
# ex_i_old = {
#     'C': {'A', 'F'},
#     'A': {'B', 'D'},
#     'B': {'E'},
#     'D': {'E'},
#     'F': {'E'},
# }

ex_i = {
    'A': {'C'},
    'F': {'C'},
    'B': {'A'},
    'D': {'A'},
    'E': {'B', 'D', 'F'},
}
 
ex_i_str ="""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

def res(inp):
    out = []

    #### NEW
    # vertices = []
    # edges = []
    # for l in inp.splitlines():
    #     vertices += [l[5], l[36]]
    #     edges.append((l[5], l[36]))

    # vertices = list(set(vertices)) # de-dup

    # # sort the vertices
    # for i in range(len(vertices)):
    #     print("ROUND #", i+1)
    #     print("vertices:", vertices)
    #     print("edges:", edges)
    #     print("out:", out)

    #     for idx, v in enumerate(sorted(vertices)):
    #         print("trying", v, "..")
    #         # if all its reqs are met, add it to output
    #         valid = True
    #         for e in edges:
    #             if e[1] == v and e[0] not in out:
    #                 valid = False
    #                 break
    #         if valid:
    #             out += v
    #             vertices.pop(idx)
    #             break

    # return "".join(out)

    ### OLD
    from copy import deepcopy
    ex_i_c = deepcopy(inp)

    while len(ex_i_c):
        #print(ex_i_c)
        items = list(toposort(ex_i_c))
        topo1 = list(items)[0] # { { 1 , 2 }, { 3 } , { 4 , 5 } } => { 1 , 2 }
        first_item = sorted(list(topo1))[0]
        #print("\t=> {}".format(first_item))

        out += first_item
        # remove as a top-level key
        if first_item in ex_i_c:
            del(ex_i_c[first_item])
        # remove as a dep
        for k in ex_i_c:
            dep = ex_i_c[k]
            if first_item in dep:
                dep.remove(first_item)

    return "".join(list(out))

    # print(list(toposort(inp)))
    # for items in list(toposort(inp)):
    #     out += reversed(sorted(items))
    #     
    # return "".join(list(out))
    #

    # print("".join(list(toposort_flatten(ex_i, sort=True))))
    # all_steps = []
    # for d in deps:
    #     vals = items[k]


    #return "".join(list(toposort_flatten(ex_i, sort=True)))

def s_to_dag(s):
    out = {}
    lines = s.splitlines()
    for l in lines:
        first = l[5]
        then = l[36]
        if not out.get(then):
            out[then] = set()
        out[then].add(first)
    return out

#print(res(ex_i))
assert(res(ex_i) == "CABDFE")
#print(s_to_dag(ex_i_str))
assert(s_to_dag(ex_i_str) == ex_i)

with open('./7-input', 'r') as f:
    dag = s_to_dag(f.read())
    #print(dag)
    print("RESULT = ", res(dag))
