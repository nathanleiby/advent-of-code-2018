ex_i = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

# no meta
simple_i =  "2 0 1 0 0 0 0 0"

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
    all_nodes = []
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

    return(sum(all_meta))

print("")
print("== EXAMPLE ==")
ex_o = no_recursion(ex_i)

assert(ex_o == 138)

with open('./8-input', 'r') as f:
    dat = f.read()
    o = ""
    o = no_recursion(dat)
    print("RESULT => ", o)
