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
# - [x] save the idx rather than re-computing it on each round (linear => constant)
#   - [x] for the non-mod 23 step => 10x speed improvement
#   - [x] for the mod 23 step => 1.5x speed bump
# - [ ] pre-allocate memory, then fill it in
# - [ ] use a different list data structure, e.g. np.array
# - [ ] use a different data structure altogether

from collections import Counter
def play(num_players,last_marble):
    marbles = [0]
    marble_number = 0
    cm_idx = 0
    current_player = 0
    player_scores = Counter()
    for p in range(num_players):
        player_scores[p] = 0

    lm_points = -1
    # until we've hit the last marble
    while lm_points != last_marble:
        # update marble number
        marble_number += 1

        # iterate through the players
        current_player = (current_player + 1) % num_players

        current_marble = marbles[cm_idx]
        if (marble_number % 23 == 0):
            # do a scoring move
            seven_left_idx = (cm_idx - 7) % len(marbles)
            val = marbles[seven_left_idx]
            player_scores[current_player] += (marble_number + val)

            # remove seven-left marble
            marbles = marbles[:seven_left_idx] + marbles[seven_left_idx+1:]
            cm_idx = (seven_left_idx) % len(marbles)
        else:
            # do a normal move
            left_of_new = (cm_idx + 1) % len(marbles)
            if left_of_new == len(marbles) - 1:
                marbles += [marble_number]
                cm_idx = len(marbles) - 1
            else:
                cm_idx = left_of_new+1
                marbles.insert(cm_idx, marble_number)

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
