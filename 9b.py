examples = [
    ((10, 1618), 8317),
    ((13, 7999), 146373),
    ((17, 1104), 2764),
    ((21, 6111), 54718),
    ((30, 5807), 37305),
]

actual = (470, 72170)

# Speed optimization ideas
# - [x] use native python insert => 1.5x to 2x speed increase
# - [x] use native python del(list[idx]) => no improvement
# - [ ] pre-allocate memory, then fill it in 

from collections import Counter
def play(num_players,last_marble):
    marbles = [0]
    marble_number = 0
    current_marble = 0
    current_player = 0
    player_scores = Counter()
    for p in range(num_players):
        player_scores[p] = 0

    lm_points = -1
    # until we've hit the last marble
    while lm_points != last_marble:
        #print(lm_points)
        # update marble number
        marble_number += 1

        # iterate through the players
        current_player = (current_player + 1) % num_players


        cm_idx = marbles.index(current_marble)
        if (marble_number % 23 == 0):
            # do a scoring move
            seven_left_idx = (cm_idx - 7) % len(marbles)
            val = marbles[seven_left_idx]
            player_scores[current_player] += (marble_number + val)

            # update current marble
            current_marble = marbles[(seven_left_idx + 1) % len(marbles)]
            # remove seven-left marble
            marbles = marbles[:seven_left_idx] + marbles[seven_left_idx+1:]

        else:
            # do a normal move
            left_of_new = (cm_idx + 1) % len(marbles)
            if left_of_new == len(marbles) - 1:
                # TODO: efficiency?
                marbles += [marble_number]
            else:
                # marbles = marbles[:left_of_new+1] + [marble_number] + marbles[left_of_new+1:]
                # 1.6x speedup
                marbles.insert(left_of_new+1, marble_number)

            current_marble = marble_number


        lm_points = marble_number
        
    # get max score
    player, score = player_scores.most_common()[0]
    return score



for e in examples:
    ex_i, ex_o = e[0], e[1]
    num_players, last_marble = ex_i[0], ex_i[1]
    res = play(num_players, last_marble)
    print("num_players={} last_marble={} max_score={}".format(num_players, last_marble, res))
    assert(res == ex_o)

print("RESULT => ", play(actual[0],actual[1]))
