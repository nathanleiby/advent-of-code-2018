from toposort import toposort, toposort_flatten

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

def res(inp, num_workers=2, duration_boost=0):
    out = []

    from copy import deepcopy
    inp_c = deepcopy(inp)

    available_work = get_available_work(inp_c)
    ongoing_work = {} # { letter : remaining_seconds }

    current_second = -1
    while len(inp_c):
        current_second += 1

        # do work
        to_delete = []
        for k in ongoing_work:
            ongoing_work[k] -= 1
            if ongoing_work[k] == 0:
                to_delete.append(k)

        # remove complete work
        for k in to_delete:
            del(ongoing_work[k])
            remove_from_graph(inp_c, k)
        if len(to_delete):
            # ONLY run this once, even if multiple deletions
            # update available_work, in case k unblocked new work
            available_work += get_available_work(inp_c)
            available_work = sorted(list(set(available_work)))
            for o in ongoing_work:
                available_work.remove(o)

            print("available_work", available_work)

        # get more work
        while len(ongoing_work) < num_workers and len(available_work) > 0:
            next_item = available_work[0]
            available_work = available_work[1:]

            duration = ord(next_item) - 64 + duration_boost
            ongoing_work[next_item] = duration

            # record order, more relevant to problem 7 but just in case
            out += next_item

        print("second = ", current_second)
        print("ongoing_work = ", ongoing_work)

    return ("".join(list(out)), current_second)

# gets next item and mutates underlying graph to remove it
def get_available_work(graph):
    # { { 2 , 1 }, { 3 } , { 4 , 5 } } => { 1 , 2 }
    o = list(toposort(graph))
    if len(o):
        return sorted(list(o[0]))
    return []

def remove_from_graph(graph, item):
    # remove as a top-level key
    if item in graph:
        del(graph[item])
    # remove as a dep
    for k in graph:
        dep = graph[k]
        if item in dep:
            dep.remove(item)

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

print(res(ex_i))
assert(res(ex_i) == ("CAFBDE", 15))

with open('./7-input', 'r') as f:
    dag = s_to_dag(f.read())
    #print(dag)
    print("RESULT = ", res(dag, num_workers=5, duration_boost=60))
