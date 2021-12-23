lines = []

with open('python\\23.in','r') as f:
    for line in f.readlines():
        #lines.append([int(x) for x in line.strip()])
        #lines.append(int(line.strip()))
        lines.append(line.strip())

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

# just do it by hand

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

