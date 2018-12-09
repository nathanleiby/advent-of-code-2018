examples = [
    ((10, 1618), 8317),
    ((13, 7999), 146373),
    ((17, 1104), 2764),
    ((21, 6111), 54718),
    ((30, 5807), 37305),
]

actual = (470, 72170)
actual_100x = (470, 7217000)

# Speed optimization ideas
# - [x] use native python insert => 1.5x to 2x speed increase
# - [x] use native python del(list[idx]) => no improvement
# - [x] save the idx rather than re-computing it on each round (linear => constant)
#   - [x] for the non-mod 23 step => 10x speed improvement
#   - [x] for the mod 23 step => 1.5x speed bump
# - [ ] use a different list data structure, e.g. np.array .. collections.deque? skiplist? doubly-linked list?
# - [ ] pre-allocate memory, then fill it in
# - [ ] use a different data structure altogether .. 


class Marble:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return "Marble Val={} Prev={} Next={}".format(self.val, self.prev.val, self.next.val)


from collections import Counter
def play(num_players,last_marble):
    marbles = [0]
    marble_number = 0
    cm_idx = 0
    current_player = 0
    player_scores = Counter()
    for p in range(num_players):
        player_scores[p] = 0

    # 0-marble
    x = Marble(0, "todo", "todo")
    x.prev = x
    x.next = x

    current_marble = x

    # until we've hit the last marble
    while marble_number != last_marble:
        # print_doubly_linked(x)
        # update marble number
        marble_number += 1
        if marble_number % 10000 == 0:
            print("\t ... {}".format(marble_number))

        # iterate through the players
        current_player = (current_player + 1) % num_players

        if (marble_number != 0 and marble_number % 23 == 0):
            # do a scoring move
            seven_left = current_marble.prev.prev.prev.prev.prev.prev.prev

            val = seven_left.val
            player_scores[current_player] += (marble_number + val)

            # update current marble
            current_marble = seven_left.next

            # remove seven-left marble
            seven_left.prev.next = seven_left.next
            del(seven_left)
        else:

            was_next = current_marble.next
            was_next_next = current_marble.next.next

            # add new marble
            new_n = Marble(val=marble_number, prev=was_next, next=was_next_next)
            was_next.next = new_n
            was_next_next.prev = new_n

            current_marble = new_n

        
    # get max score
    player, score = player_scores.most_common()[0]
    return score


def print_doubly_linked(x):
    cur_node = x
    out = []
    while True:
        out.append(cur_node.val)
        cur_node = cur_node.next
        if cur_node.val == 0:
            break
    print("L: ", "  ".join(map(str, out)))

for e in examples:
    ex_i, ex_o = e[0], e[1]
    num_players, last_marble = ex_i[0], ex_i[1]
    res = play(num_players, last_marble)
    print("num_players={} last_marble={} max_score={}".format(num_players, last_marble, res))
    assert(res == ex_o)

print("RESULT => ", play(actual[0],actual[1]))
print("RESULT NEW => ", play(actual_100x[0],actual_100x[1]))
