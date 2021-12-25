import copy

cucumbers = []

#with open('python/test.in','r') as f:
with open('python/25.in','r') as f:
    for line in f.readlines():
        cucumbers.append([x for x in line.strip()])

## part 1 ##

# Every step, 
# the sea cucumbers in the east-facing herd attempt to move forward one location, 
# then the sea cucumbers in the south-facing herd attempt to move forward one location.

R = len(cucumbers)
C = len(cucumbers[0])

moved = True
round = 0

# loop until nothing is moving anymore
while(moved):
    round += 1
    moved = False
    
    newcumbers = copy.deepcopy(cucumbers)

    # check every cell looking for east facing cucumbers
    for r in range(R):
        for c in range(C):
            if cucumbers[r][c] == '>':
                # move it forward if there's space
                if cucumbers[r][(c+1)%C] == '.':
                    newcumbers[r][(c+1)%C] = '>'
                    newcumbers[r][c] = '.'
                    moved = True
    
    newnewcumbers = copy.deepcopy(newcumbers)
    # now check every south facing cucumber
    for r in range(R):
        for c in range(C):               
            if newcumbers[r][c] == 'v':
                if newcumbers[(r+1)%R][c] == '.':
                    newnewcumbers[(r+1)%R][c] = 'v'
                    newnewcumbers[r][c] = '.'
                    moved = True

    cucumbers = newnewcumbers

print(round)

## part 2 ##

print('Done!')