import numpy as np
import matplotlib.pyplot as plt

N = 50

ex_i = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

def parse_line(line):
    s = line.split("> velocity=<")
    position_s = s[0][len("position=<"):]
    velocity_s = s[1][:-1]
    p_split = position_s.split(",")
    v_split = velocity_s.split(",")
    return list(map(int, p_split)), list(map(int, v_split))


import asciiplotlib as apl
import pandas as pd

def ascii_draw(data):
    min_x = 10000 
    min_y = 10000 
    for pt in data:
        if pt[0] < min_x:
            min_x = pt[0].item()
        if pt[1] < min_y:
            min_y = pt[1].item()

    # rows
    print("MIN_X", min_x, "MIN_Y", min_y)
    for r in range(20):
        # cols
        rdata = []
        for c in range(100):
            found = False
            for pt in data:
                x = pt[0].item()
                y = pt[1].item()
                if x - min_x == c and y - min_y == r:
                    found = True
                    break
            if found:
                rdata.append("#")
            else:
                rdata.append(".")
        print("".join(rdata))

def res(input, file_prefix, step_size, num_steps, base_offset=0):
    lines = input.splitlines()
    pvs = []
    for l in lines:
        pvs.append(parse_line(l))

    positions = np.array(list(map(lambda x: x[0], pvs)))
    velocities = np.array(list(map(lambda x: x[1], pvs)))

    for i in range(num_steps):
        if i%10000 == 0:
            print(i)
        offset = base_offset + i*step_size
        data = positions + (offset)*velocities

        ascii_draw(data)

        x, y = data.T

        plt.scatter(x, y)
        plt.savefig("./10-output/10-{}-{}".format(file_prefix, offset))
        print(offset, plt.xlim(), plt.ylim())
        plt.close()


#res(ex_i, "example", 1, 5)
res(ex_i, "example", 1, 1, base_offset=3)

#dd = np.array([[1,2], [2,3], [3,4]])
#ascii_draw(dd)

with open("10-input", "r") as f:
    # res(f.read(), "actual", 100, 1000, base_offset=10500)
    # res(f.read(), "actual", 1, 200, base_offset=10500)

    res(f.read(), "actual", 1, 1, base_offset=10577)
