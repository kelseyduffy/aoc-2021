

class player:
    def __init__(self, start_tile):
        self.score = 0
        self.tile = start_tile

class deterministic_die:
    def __init__(self):
        self.face = 0
        self.counter = 0

    def roll(self):
        self.face += 1
        if self.face > 100:
            self.face = 1
        self.counter += 1

        return self.face

def simulate(current_state):

    global known_states
    
    if current_state in known_states: # I think doing this is called memoization...? That's a word I learned last week, not sure if I actually learned it though
        return known_states[current_state]
    
    p1_score, p1_tile, p2_score, p2_tile, whose_turn = current_state

    p1_wins = 0
    p2_wins = 0
    for roll1 in range(1,4):
        for roll2 in range(1,4):
            for roll3 in range(1,4):
                if whose_turn == 1: # player one's turn
                    p1_new_tile = p1_tile + roll1 + roll2 + roll3
                    p1_new_tile = ((p1_new_tile - 1) % 10) + 1
                    p1_new_score = p1_score + p1_new_tile
                    if p1_new_score >= 21:
                        p1_wins += 1
                    else:
                        next_state = (p1_new_score, p1_new_tile, p2_score, p2_tile, 2)
                        next_roll_win_count = simulate(next_state)
                        p1_wins += next_roll_win_count[0]
                        p2_wins += next_roll_win_count[1]
                else:
                    p2_new_tile = p2_tile + roll1 + roll2 + roll3
                    p2_new_tile = ((p2_new_tile - 1) % 10) + 1
                    p2_new_score = p2_score + p2_new_tile
                    if p2_new_score >= 21:
                        p2_wins += 1
                    else:
                        next_state = (p1_score, p1_tile, p2_new_score, p2_new_tile, 1)
                        next_roll_win_count = simulate(next_state)
                        p1_wins += next_roll_win_count[0]
                        p2_wins += next_roll_win_count[1]
    
    known_states[current_state] = (p1_wins, p2_wins)
    return (p1_wins, p2_wins)

## part 1 ##

with open('python/21.in','r') as f:
    line = f.__next__()
    player1 = player(int(line.split(': ')[1].strip()))
    line = f.__next__()
    player2 = player(int(line.split(': ')[1].strip()))

winning_score = 1000

game_die = deterministic_die()

while(player1.score < winning_score and player2.score < winning_score):
    
    # player 1
    this_roll = 0

    for _ in range(3):
        this_roll += game_die.roll()
    
    player1.tile += this_roll
    player1.tile = ((player1.tile - 1) % 10) + 1

    player1.score += player1.tile

    if player1.score >= winning_score:
        print(player2.score * game_die.counter)
        break

    # player 2
    this_roll = 0

    for _ in range(3):
        this_roll += game_die.roll()
    
    player2.tile += this_roll
    player2.tile = ((player2.tile - 1) % 10) + 1

    player2.score += player2.tile

    if player2.score >= winning_score:
        print(player1.score * game_die.counter)
        break

## part 2 ##

with open('python/21.in','r') as f:
    line = f.__next__()
    p1_tile = int(line.split(': ')[1].strip())
    line = f.__next__()
    p2_tile = int(line.split(': ')[1].strip())

winning_score = 21
p1_score = 0
p2_score = 0

# game state = p1_score, p1_space, p2_score, p2_space, whose_turn_next
starting_game_state = (p1_score, p1_tile, p2_score, p2_tile, 1)

# value is (p1_wins, p2_wins)
known_states = {}

win_totals = simulate(starting_game_state)
#print(win_totals)
print(max(win_totals[0], win_totals[1]))

""" non recursive approach did not work, abandoning it :(
with open('python/test.in','r') as f:
    line = f.__next__()
    player1 = player(int(line.split(': ')[1].strip()))
    line = f.__next__()
    player2 = player(int(line.split(': ')[1].strip()))

# game state = p1_score, p1_space, p2_score, p2_space, whose_turn_next
#starting_game_state = '|'.join([player1.score, player1.tile, player2.score, player2.tile, 1])
starting_game_state = (player1.score, player1.tile, player2.score, player2.tile, 1)


# value is (p1_wins, p2_wins)

possible_states = {}

winning_score = 21

# simulate each possible guarenteed win-on-the-next-turn state, adding them to the dictionary

# seed 1: p1 score is 20 and it's their turn
p1_score = 20
whose_turn = 1
for p2_score in range(21):
    for p2_tile in range(1,11):
        for p1_tile in range(1,11):
            #possible_states['|'.join([p1_score, p1_tile, p2_score, p2_tile, whose_turn])] = (9,0) # all nine possible rolls have player 1 winning
            possible_states[(p1_score, p1_tile, p2_score, p2_tile, whose_turn)] = (9,0) # all nine possible rolls have player 1 winning

# seed 2: p2 score is 20 and it's their turn
p2_score = 20
whose_turn = 2
for p1_score in range(21):
    for p1_tile in range(1,11):
        for p2_tile in range(1,11):
            #possible_states['|'.join([p1_score, p1_tile, p2_score, p2_tile, whose_turn])] = (0,9) # all nine possible rolls have player 2 winning
            possible_states[(p1_score, p1_tile, p2_score, p2_tile, whose_turn)] = (0,9) # all nine possible rolls have player 2 winning

# go backwards through each possible starting
for highest_score in reversed(range(20)):
    
    # hand off to every already defined state with a higher score
    # eg. 19->20, 19->19; 18->20, 18->19, 18->18; etc
    for handoff_score in reversed(range(highest_score,winning_score)):

        # player 1's turn simulation
        p1_score = highest_score
        whose_turn = 1
        p2_score = handoff_score

        for p2_tile in range(1,11):
            for p1_tile in range(1,11):

                p1_wins = 0
                p2_wins = 0
                for roll1 in range(1,4):
                    for roll2 in range(1,4):
                        for roll3 in range(1,4):
                            p1_new_tile = p1_tile + roll1 + roll2 + roll3
                            p1_new_tile = ((p1_new_tile - 1) % 10) + 1
                            p1_new_score = p1_score + p1_new_tile
                            if p1_new_score >= 21:
                                p1_wins += 1
                            else:
                                next_state = (p1_new_score, p1_new_tile, p2_score, p2_tile, 2)
                                assert next_state in possible_states, f'state {next_state} not found in possible states'
                                next_roll_win_count = possible_states[next_state] # by going backwards this lookup is always valid
                                p1_wins += next_roll_win_count[0]
                                p2_wins += next_roll_win_count[1]

                # all three possible rolls have been determined, store the result
                this_state = (p1_score, p1_tile, p2_score, p2_tile, whose_turn)
                possible_states[this_state] = (p1_wins, p2_wins)

        # player 1's turn simulation
        p2_score = highest_score
        whose_turn = 2
        p1_score = handoff_score

        for p1_tile in range(1,11):
            for p2_tile in range(1,11):

                p1_wins = 0
                p2_wins = 0
                for roll1 in range(1,4):
                    for roll2 in range(1,4):
                        for roll3 in range(1,4):
                            p2_new_tile = p2_tile + roll1 + roll2 + roll3
                            p2_new_tile = ((p2_new_tile - 1) % 10) + 1
                            p2_new_score = p2_score + p2_new_tile
                            if p2_new_score >= 21:
                                p2_wins += 1
                            else:
                                next_state = (p1_score, p1_tile, p2_new_score, p2_new_tile, 1)
                                assert next_state in possible_states, f'state {next_state} not found in possible states'
                                next_roll_win_count = possible_states[next_state] # by going backwards this lookup is always valid
                                p1_wins += next_roll_win_count[0]
                                p2_wins += next_roll_win_count[1]

                # all three possible rolls have been determined, store the result
                this_state = (p1_score, p1_tile, p2_score, p2_tile, whose_turn)
                possible_states[this_state] = (p1_wins, p2_wins)

    # now go back and hand off to every just defined state to fill in the full set up to this level
    # eg. after 18->20, 18->19, 18->18, do 19->18; after 17->20, 17->19, 17->18, 17->17, do 19->17, 18->17
    for back_track_score in reversed(range(highest_score+1, winning_score-1)):
            # player 1's turn simulation
        p1_score = back_track_score
        whose_turn = 1
        p2_score = highest_score

        for p2_tile in range(1,11):
            for p1_tile in range(1,11):

                p1_wins = 0
                p2_wins = 0
                for roll1 in range(1,4):
                    for roll2 in range(1,4):
                        for roll3 in range(1,4):
                            p1_new_tile = p1_tile + roll1 + roll2 + roll3
                            p1_new_tile = ((p1_new_tile - 1) % 10) + 1
                            p1_new_score = p1_score + p1_new_tile
                            if p1_new_score >= 21:
                                p1_wins += 1
                            else:
                                next_state = (p1_new_score, p1_new_tile, p2_score, p2_tile, 2)
                                assert next_state in possible_states, f'state {next_state} not found in possible states'
                                next_roll_win_count = possible_states[next_state] # by going backwards this lookup is always valid
                                p1_wins += next_roll_win_count[0]
                                p2_wins += next_roll_win_count[1]

                # all three possible rolls have been determined, store the result
                this_state = (p1_score, p1_tile, p2_score, p2_tile, whose_turn)
                possible_states[this_state] = (p1_wins, p2_wins)

        # player 1's turn simulation
        p2_score = back_track_score
        whose_turn = 2
        p1_score = highest_score

        for p1_tile in range(1,11):
            for p2_tile in range(1,11):

                p1_wins = 0
                p2_wins = 0
                for roll1 in range(1,4):
                    for roll2 in range(1,4):
                        for roll3 in range(1,4):
                            p2_new_tile = p2_tile + roll1 + roll2 + roll3
                            p2_new_tile = ((p2_new_tile - 1) % 10) + 1
                            p2_new_score = p2_score + p2_new_tile
                            if p2_new_score >= 21:
                                p2_wins += 1
                            else:
                                next_state = (p1_score, p1_tile, p2_new_score, p2_new_tile, 1)
                                assert next_state in possible_states, f'state {next_state} not found in possible states'
                                next_roll_win_count = possible_states[next_state] # by going backwards this lookup is always valid
                                p1_wins += next_roll_win_count[0]
                                p2_wins += next_roll_win_count[1]

                # all nine possible rolls have been determined, store the result
                this_state = (p1_score, p1_tile, p2_score, p2_tile, whose_turn)
                possible_states[this_state] = (p1_wins, p2_wins)

#tester
#starting_game_state = (19, player1.tile, 19, player2.tile, 1)
win_totals = possible_states[starting_game_state]
print(win_totals)
print(max(win_totals[0], win_totals[1]))

# 12238260515606 is too low
# 79358986580181 is too high
"""
