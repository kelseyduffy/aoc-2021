# Game Rules
# -----
# Amber amphipods require 1 energy per step
# Bronze amphipods require 10 energy
# Copper amphipods require 100
# Desert ones require 1000

# 11 hallway spots, 7 waiting spots (can't block the 4 room entry spots)

# there's only 35 possible moves:
# - each of the 4 buckets to each of the 7 hallway spots (28)
# - each of the 7 hallway spots to the appropriate bucket (7)

# Strategies:
# D's can't take extra steps, too costly, must move directly into final bucket
# C's shouldn't take extra steps. Only do it if actively blocking a D
# B's and A's can move as necessary, A priorized over B

## part 1 ## 
# solve it by hand

# START
# ........... #
#   D#C#D#B
#   C#A#A#B

# move B up to the right -> 30
# move B up to the right -> 30

# .........BB #
#   D#C#D#.
#   C#A#A#.

# move D in -> 9000
# move D in -> 4000
# move A out in to the left -> 7

# .A.......BB #
#   .#C#.#D
#   C#A#.#D

# move C in -> 800
# move C in -> 400

# .A.......BB #
#   .#.#C#D
#   .#A#C#D

# move A in -> 6
# move A in -> 2

# .........BB #
#   A#.#C#D
#   A#.#C#D

# move B in -> 70
# move B in -> 70

# ........... #
#   A#B#C#D
#   A#B#C#D

# total is 14415

## part 2 ##
# coerce it into a weighted path finding algorithm

from collections import deque
import bisect

# only making this class so that the less than method can be defined for sorted insertions
class State:
    def __init__(self, state, score):
        self.state = state
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

# each room is a stack
# index 0 is by the hallway; index 3 is the back of the room
stack_a = [] # the first stack, where all the Amber amphipods will eventual reside
stack_b = [] # all the Bronzes at the end
stack_c = [] # all the Coppers at the end
stack_d = [] # all the Deserts at the end

lines = []
with open('python\\23.in','r') as f:
    for i,line in enumerate(f):
        if i > 1 and i < 6: # just grab the four rooms
            amphipods = line.strip().replace('#','') # get rid of the wall markers
            stack_a.append(amphipods[0])
            stack_b.append(amphipods[1])
            stack_c.append(amphipods[2])
            stack_d.append(amphipods[3])

# the game state is represented by:
# - what's in each hallway spot
# - what's in each room

# stacks are mutable and therefore not hashable, and therefore can't be part of the 'game state'
# instead, the number of actions taken by a stack can be used
# - each amphipod can only move once into the hallway, and once into its final room
# - the stacks can therefore not be rearranged. it only pops all 4 initial amphipods then pushes all 4 finals

# this assumption relies on each stack needing to be completely emptied
assert stack_a[3] != 'A', 'room A does not need to fully empty'
assert stack_b[3] != 'B', 'room B does not need to fully empty'
assert stack_c[3] != 'C', 'room C does not need to fully empty'
assert stack_d[3] != 'D', 'room D does not need to fully empty'

# Stack States:
# 0: all initial amphipods      |   W X Y Z
# 1: top space empty            |   W X Y .
# 2: top 2 spaces empty         |   W X . .
# 3: top 3 spaces empty         |   W . . .
# 4: room completely empty      |   . . . . 
# 5: first amphipod in place    |   A . . .
# 6: second amphipod in place   |   A A . .
# 7: third amphipod in place    |   A A A .
# 8: room in final state        |   A A A A

# game state is (hallway1, hallway2, hallway4, h6, h8, h10, h11, stack_a_state, b_state, c, d)
# - hallway spots 3, 5, 7, and 9 must always be '.' because you can't block a room

# at the beginning, the hallway is clear and the stacks are all state 0
initial_state = ('.','.','.','.','.','.','.',0,0,0,0)

# in the end, the hallway is clear and the stacks are all in state 8
final_state = ('.','.','.','.','.','.','.',8,8,8,8)

# keep track of states you've already checked
visited_states = set()

# keep track of the upcoming states to check in order of how cheap they are to get to
upcoming_states = deque([])

# when moving, apply the penalties per amphipod type
costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

# quicker stack lookups to eliminate repetitive code
final_stack = {'A': stack_a, 'B': stack_b, 'C': stack_c, 'D': stack_d}

# start at the initial state and loop until the final state is being visited
current_state = initial_state
score = 0

while (current_state != final_state):

    # if we've been here before, we've been here for cheaper than now. skip the moves and pop the next state
    if current_state not in visited_states:
        
        # record that we've been here now
        visited_states.add(current_state)

        # destructure the current state tuple for more readable code
        (h1,h2,h4,h6,h8,h10,h11,a,b,c,d) = current_state

        # if the A stack is not fully popped, pop the next one
        if a < 4:
            pass

        # if the B stack is not fully popped, pop the next one
        if b < 4:
            pass

        # if the C stack is not fully popped, pop the next one
        if c < 4:
            pass

        # if the D stack is not fully popped, pop the next one
        if d < 4:
            pass

        # push each hallway space to the correct final room
            # 1. find the right stack to push to
            # 2. check if the path is blocked
            # 3. find the number of moves required
            # 4. insert the resulting state with score + moved*cost into the upcoming states
            # There's an elegant way to do this, but I need to just get it working first, hard coded for now

        if h1 != '.':
            if h1 == 'A' and a > 3: # if it's an Amber and the amber ready is ready for entering
                if h2 == '.': # h2 is between h1 and A's entry
                    moves = 2                   # start with moves to get to the hallway spot outside the room
                    moves += (8-a)              # add the number of moves to get into the bottom most spot
                    cost = costs[h1] * moves    # convert this to a cost for the total move

                    # the next state is h1 cleared out and a advanced a state, scored at current score + this cost
                    # insert this state into the list of upcoming states, in order of cheapest cost
                    bisect.insort(upcoming_states, State(('.',h2,h4,h6,h8,h10,h11,a+1,b,c,d), score + cost))

            elif h1 == 'B' and b > 3:
                if h2 == '.' and h4 == '.': # h2 and h4 need to be clear
                    moves = 4
                    moves += (8-b)
                    cost = costs[h1] * moves

                    # the next state is h1 cleared out and b advanced a state, scored at current score + this cost
                    # insert this state into the list of upcoming states, in order of cheapest cost
                    bisect.insort(upcoming_states, State(('.',h2,h4,h6,h8,h10,h11,a,b+1,c,d), score + cost))

            elif h1 == 'C' and c > 3:
                if h2 == '.' and h4 == '.' and h6 == '.':
                    moves = 6
                    moves += (8-c)
                    cost = costs[h1] * moves
                    bisect.insort(upcoming_states, State(('.',h2,h4,h6,h8,h10,h11,a,b,c+1,d), score + cost))

            elif h1 == 'D' and d > 3:
                if h2 == '.' and h4 == '.' and h6 == '.' and h8 == '.':
                    moves = 8
                    moves += (8-d)
                    cost = costs[h1] * moves
                    bisect.insort(upcoming_states, State(('.',h2,h4,h6,h8,h10,h11,a,b,c,d+1), score + cost))

        if h2 != '.':
            if h2 == 'A' and a > 3: # no blockers
                moves = 1
                moves += (8-a)
                cost = costs[h2] * moves
                bisect.insort(upcoming_states, State((h1,'.',h4,h6,h8,h10,h11,a+1,b,c,d), score + cost))

            elif h2 == 'B' and b > 3:
                if h4 == '.': # h4 needs to be clear
                    moves = 3
                    moves += (8-b)
                    cost = costs[h2] * moves
                    bisect.insort(upcoming_states, State((h1,'.',h4,h6,h8,h10,h11,a,b+1,c,d), score + cost))

            elif h2 == 'C' and c > 3:
                if h4 == '.' and h6 == '.':
                    moves = 5
                    moves += (8-c)
                    cost = costs[h2] * moves
                    bisect.insort(upcoming_states, State((h1,'.',h4,h6,h8,h10,h11,a,b,c+1,d), score + cost))

            elif h2 == 'D' and d > 3:
                if h4 == '.' and h6 == '.' and h8 == '.':
                    moves = 7
                    moves += (8-d)
                    cost = costs[h2] * moves
                    bisect.insort(upcoming_states, State((h1,'.',h4,h6,h8,h10,h11,a,b,c,d+1), score + cost))


        if h4 != '.':
            if h4 == 'A' and a > 3: # no blockers
                moves = 1
                moves += (8-a)
                cost = costs[h4] * moves
                bisect.insort(upcoming_states, State((h1,h2,'.',h6,h8,h10,h11,a+1,b,c,d), score + cost))

            elif h4 == 'B' and b > 3: # no blockers
                moves = 1
                moves += (8-b)
                cost = costs[h4] * moves
                bisect.insort(upcoming_states, State((h1,h2,'.',h6,h8,h10,h11,a,b+1,c,d), score + cost))

            elif h4 == 'C' and c > 3:
                if h6 == '.':
                    moves = 3
                    moves += (8-c)
                    cost = costs[h4] * moves
                    bisect.insort(upcoming_states, State((h1,h2,'.',h6,h8,h10,h11,a,b,c+1,d), score + cost))

            elif h4 == 'D' and d > 3:
                if h6 == '.' and h8 == '.':
                    moves = 5
                    moves += (8-d)
                    cost = costs[h4] * moves
                    bisect.insort(upcoming_states, State((h1,h2,'.',h6,h8,h10,h11,a,b,c,d+1), score + cost))

        if h6 != '.':
            if h6 == 'A' and a > 3:
                if h4 == '.':
                    moves = 3
                    moves += (8-a)
                    cost = costs[h6] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,'.',h8,h10,h11,a+1,b,c,d), score + cost))

            elif h6 == 'B' and b > 3: # no blockers
                moves = 1
                moves += (8-b)
                cost = costs[h6] * moves
                bisect.insort(upcoming_states, State((h1,h2,h4,'.',h8,h10,h11,a,b+1,c,d), score + cost))

            elif h6 == 'C' and c > 3: # no blockers
                moves = 1
                moves += (8-c)
                cost = costs[h6] * moves
                bisect.insort(upcoming_states, State((h1,h2,h4,'.',h8,h10,h11,a,b,c+1,d), score + cost))

            elif h6 == 'D' and d > 3:
                if h8 == '.':
                    moves = 3
                    moves += (8-d)
                    cost = costs[h6] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,'.',h8,h10,h11,a,b,c,d+1), score + cost))

        if h8 != '.':
            if h8 == 'A' and a > 3:
                if h4 == '.' and h6 == '.':
                    moves = 5
                    moves += (8-a)
                    cost = costs[h8] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,'.',h10,h11,a+1,b,c,d), score + cost))

            elif h8 == 'B' and b > 3:
                if h6 == '.':
                    moves = 3
                    moves += (8-b)
                    cost = costs[h8] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,'.',h10,h11,a,b+1,c,d), score + cost))

            elif h8 == 'C' and c > 3: # no blockers
                moves = 1
                moves += (8-c)
                cost = costs[h8] * moves
                bisect.insort(upcoming_states, State((h1,h2,h4,h6,'.',h10,h11,a,b,c+1,d), score + cost))

            elif h8 == 'D' and d > 3: # no blockers
                moves = 1
                moves += (8-d)
                cost = costs[h8] * moves
                bisect.insort(upcoming_states, State((h1,h2,h4,h6,'.',h10,h11,a,b,c,d+1), score + cost))

        if h10 != '.':
            if h10 == 'A' and a > 3:
                if h4 == '.' and h6 == '.' and h8 == '.':
                    moves = 7
                    moves += (8-a)
                    cost = costs[h10] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,h8,'.',h11,a+1,b,c,d), score + cost))

            elif h10 == 'B' and b > 3:
                if h6 == '.' and h8 == '.':
                    moves = 5
                    moves += (8-b)
                    cost = costs[h10] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,h8,'.',h11,a,b+1,c,d), score + cost))

            elif h10 == 'C' and c > 3: 
                if h8 == '.':
                    moves = 3
                    moves += (8-c)
                    cost = costs[h10] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,h8,'.',h11,a,b,c+1,d), score + cost))

            elif h10 == 'D' and d > 3: # no blockers
                moves = 1
                moves += (8-d)
                cost = costs[h10] * moves
                bisect.insort(upcoming_states, State((h1,h2,h4,h6,h8,'.',h11,a,b,c,d+1), score + cost))

        if h11 != '.':
            if h11 == 'A' and a > 3:
                if h4 == '.' and h6 == '.' and h8 == '.' and h10 == '.':
                    moves = 8
                    moves += (8-a)
                    cost = costs[h11] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,h8,h10,'.',a+1,b,c,d), score + cost))

            elif h11 == 'B' and b > 3:
                if h6 == '.' and h8 == '.' and h10 == '.':
                    moves = 6
                    moves += (8-b)
                    cost = costs[h11] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,h8,h10,'.',a,b+1,c,d), score + cost))

            elif h11 == 'C' and c > 3: 
                if h8 == '.' and h10 == '.':
                    moves = 4
                    moves += (8-c)
                    cost = costs[h11] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,h8,h10,'.',a,b,c+1,d), score + cost))

            elif h11 == 'D' and d > 3:
                if h10 == '.':
                    moves = 2
                    moves += (8-d)
                    cost = costs[h11] * moves
                    bisect.insort(upcoming_states, State((h1,h2,h4,h6,h8,h10,'.',a,b,c,d+1), score + cost))

    # pop off the next cheapest state to visit and reloop
    next_state = upcoming_states.popleft()

    # destructure the class for the next loop
    current_state = next_state.state
    score = next_state.score

# when the final state is being visited for the first time, it has to be the cheapest way to get there. print the score
print(score)