def flash(i, j, flashes, octopi):
    # reset to 0 and add the index to the set
    octopi[i][j] = 0
    flashes.add((i * len(octopi[0])) + j)

    # increase the neighbor count in all directions
    flash_neighbor(i-1, j-1, flashes, octopi)
    flash_neighbor(i-1, j, flashes, octopi)
    flash_neighbor(i-1, j+1, flashes, octopi)
    flash_neighbor(i, j-1, flashes, octopi)
    flash_neighbor(i, j+1, flashes, octopi)
    flash_neighbor(i+1, j-1, flashes, octopi)
    flash_neighbor(i+1, j, flashes, octopi)
    flash_neighbor(i+1, j+1, flashes, octopi)

def flash_neighbor(i, j, flashes, octopi):
    # check that we're not out of bounds
    if 0 <= i < len(octopi) and 0 <= j < len(octopi[0]):
        # if the octopus hasn't already flashed this round increase its number
        if octopi[i][j] > 0 or ((i * len(octopi[0])) + j) not in flashes:
            octopi[i][j] += 1

            # if it's above 9, flash it
            if octopi[i][j] > 9:
                flash(i, j, flashes, octopi)

octopi = []

with open('python\\11.in','r') as f:
#with open('python\\test.in','r') as f:
    for line in f.readlines():
        octopi.append([int(x) for x in line.strip()])

## part 1 ##

total = 0

for _ in range(100):

    # zero out the set of indexes that flashed this round
    flashes = set()

    # check each octopus
    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            # if it has already flashed this round, leave at 0
            if octopi[i][j] == 0 and ((i * len(octopi[0])) + j) in flashes:
                continue
            
            # otherwise bring it up 1
            octopi[i][j] += 1

            # if it's above 9, flash it
            if octopi[i][j] > 9:
                flash(i, j, flashes, octopi)

    # add the number of flashed octopi to the running total
    total += len(flashes)

print(total)

## part 2 ##

step = 100 # we just did 100 loops, start the counter from here to save 100 cycles
while(True):
    step += 1
    flashes = set()
    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            if octopi[i][j] == 0 and ((i * len(octopi[0])) + j) in flashes:
                continue
            
            octopi[i][j] += 1
            if octopi[i][j] > 9:
                flash(i, j, flashes, octopi)

    # once the flashes set contains all octopi, break out
    if len(flashes) == len(octopi) * len(octopi[0]):
        print(step)
        break