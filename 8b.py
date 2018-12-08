ex_i = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

# no meta
simple_i = "2 0 1 0 0 0 0 0"


class Node(object):
    def __init__(self, name="", num_children=0, num_meta=0):
        self.name = name
        self.num_children = num_children
        self.num_meta = num_meta
        self.children = []
        self.children_done = 0
        self.meta = []



def no_recursion(i):
    i = list(map(int, i.strip().split(" ")))

    nodes_to_process = []
    cur_idx = 0

    def next_node_name():
        global cur_node_num
        cur_node_num += 1
        return chr(cur_node_num)

    all_nodes = {}
    all_node_names = []

    all_meta = []
    while cur_idx < len(i):
        print("")
        print("cur_idx", cur_idx, "cur_val", i[cur_idx])
        # import ipdb
        # ipdb.set_trace()
        # add the first node
        print("NODES TO PROCESS:", list(map(lambda x: x.name, nodes_to_process)))
        if len(nodes_to_process) == 0:
            print("top branch")
            num_children, num_meta = int(i[cur_idx]), int(i[cur_idx + 1])
            cur_node = Node(
                name=next_node_name(), num_children=num_children, num_meta=num_meta
            )
            nodes_to_process.append(cur_node)

            all_nodes[cur_node.name] = cur_node
            all_node_names.append(cur_node.name)

            cur_idx += 2
        else:
            print("bottom branch")
            # process last node in list
            last_node = nodes_to_process[-1]
            # print("LN: nc={} c={}".format(last_node.num_children, last_node.children))
            # print(last_node, last_node.num_children, len(last_node.children))
            print(
                "{} ... {}/{} ... num_meta={}".format(
                    last_node.name,
                    last_node.children_done,
                    last_node.num_children,
                    last_node.num_meta,
                )
            )
            # if len(last_node.children) != last_node.num_children:
            if last_node.children_done != last_node.num_children:
                num_children, num_meta = int(i[cur_idx]), int(i[cur_idx + 1])
                cur_idx += 2

                child = Node(
                    name=next_node_name(), num_children=num_children, num_meta=num_meta
                )
                nodes_to_process.append(child)

                all_nodes[child.name] = child
                all_node_names.append(child.name)

                last_node.children_done += 1
                last_node.children.append(child)

            else:
                last_node.meta = i[cur_idx : cur_idx + last_node.num_meta]
                print("num_meta:", last_node.num_meta)
                print("meta:", last_node.meta)
                cur_idx += last_node.num_meta

                all_meta += last_node.meta

                nodes_to_process.pop()

    def get_node_val(some_node):
        print("get_node_val", some_node.name, some_node.meta)
        print(list(map(lambda n: n.name, some_node.children)))
        if some_node.num_children == 0:
            return sum(some_node.meta)
        else:
            total = 0
            for m in some_node.meta:
                try:
                    total += get_node_val(some_node.children[m-1])
                except:
                    total += 0
                print(total)
            return total

    result = get_node_val(all_nodes['A'])

    return result


print("")
print("== EXAMPLE ==")

cur_node_num = ord("A") - 1
ex_o = no_recursion(ex_i)

assert ex_o == 66

# reset first node name
cur_node_num = ord("A") - 1
with open('./8-input', 'r') as f:
    dat = f.read()
    o = ""
    o = no_recursion(dat)
    print("RESULT => ", o)
