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

# wrong: 40521

# track the game state of a tuple of (h1, h2, ... , h11, a1, ... , a4, ... , d4) for what's in each and the score to get there
    # do i need to track which specific A's, B's, etc have been popped out yet?
        # i don't think so because you can only pop to the hallway and push to the destination
        # if it's already in the destination, don't pop it
        # if it's in the hallway, you can only push to one bucket
        # if you're in the whole bucket, you can only pop to the hallway
        # who's been popped yet doesn't need to be tracked
    # have we been to that state before? with a lower score? if so, abandon this option
# keep track of 4 stacks -> A stack, B stack, C stack, D stack
# name each of the A's A1 A2 A3 A4 so that they're treated individually in terms of move out tracking
# try each "next move" of popping the top one of a stack and putting it onto a random space
    # try each stack
    # try each destination space
    # check for blockers, if blocked, abandon this option
    # don't try to pop off the top of a stack that is collecting its actual letters at this point
        # identify it as maybe 'has_bad_letter' or something, or 'has_been_empty'
# also try each "move in" of any hallway piece
    # if the destination space is blocked, abandon this route
    # if the route to the destination is blocked, abandon this route
# moving directly from starting bucket to destination bucket via clear route should be handled by trying:
    # move to a hallway spot in between -> if the route is clear, this is guaranteed to exist
    # move to the bucket
    # these two cases are already handled above, so special case of going directly to final bucket is not necessary
# maybe use the priority queue from the path finding day before
    # insert each move into the queue, with the new score of the current game + the score for having done that move
    # always look at the lowest score state next
    # track whether we've been to a specific state before
    # keep going until it's the turn of the final winning state, that score is the lowest by definition
# just need to figure out how to detect a stalemate?
    # detect if the path is blocked by checking each hallway spot it passes through
    # if it's blocked, that specific pop to that specific hallway spot is abandoned
    # the whole thing should just take care of itself that way