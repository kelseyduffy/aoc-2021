from typing import Collection


from collections import deque

# Rules
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
# move A out in between C and D buckets -> 7

# .......A.BB #
#   .#C#.#D
#   C#A#.#D

# move C in -> 800
# move C in -> 400

# .......A.BB #
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

# each room is a stack
# index 0 is the bottom; index 3 is the top
stack_a = [] # the first stack, where all the A's will eventual reside
stack_b = [] # all the B's at the end
stack_c = [] # all the C's at the end
stack_d = [] # all the D's at the end

lines = []
with open('python\\23.in','r') as f:
    for i,line in enumerate(f):
        if i > 1 and i < 6: # just grab the four rooms
            lines.append(line.strip().replace('#',''))

# build the initial stacks representing the rooms
for line in reversed(lines):
    stack_a.append(line[0])
    stack_b.append(line[1])
    stack_c.append(line[2])
    stack_d.append(line[3])

# the game state is represented by:
# - what's in each hallway spot
# - what's in each room

# stacks are mutable and therefore not hashable, and therefore can't be part of the 'game state'
# instead, the number of actions taken by a stack can be used
# - each amphipod can only move once into the hallway, and once into its final room
# - the stacks can therefore not be rearranged. it only pops all 4 initial amphipods then pushes all 4 finals

# this assumption relies on each stack needing to be completely emptied
assert stack_a[0] != 'A', 'room A does not need to fully empty'
assert stack_b[0] != 'B', 'room B does not need to fully empty'
assert stack_c[0] != 'C', 'room C does not need to fully empty'
assert stack_d[0] != 'D', 'room D does not need to fully empty'

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

visited_states = set()
upcoming_states = deque([])

costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

