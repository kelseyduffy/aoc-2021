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

# 11 hallway spots, 7 waiting spots

# there's only 4 possible moves into the hallway, 7 waiting spots total

# once in the hallway, only 1 possible route and space to move to, if bucket and pathway are clear

# Strategies:
# D's can't take extra steps, too costly. 13000 for them total
# C's shouldn't take extra steps, 1200 for them total to be direct
# B's and A's can move as necessary, A priorized over B

## part 1 ## 

# just do it by hand
# ........... #
#   D#C#D#B
#   C#A#A#B
# move B up to the right -> 30
# move B up to the right -> 30
# move D in -> 9000
# move D in -> 4000
# move A out in between C and D buckets -> 7
# move C in -> 800
# move C in -> 400
# move A in -> 6
# move A in -> 2
# move B in -> 70
# move B in -> 70

# total is 14415

## part 2 ##
