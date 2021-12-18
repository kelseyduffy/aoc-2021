from collections import deque

def reduce(snailfish_number):
    
    while(True):
        # explode the leftmost eligible pair then loop again
        exploded = False

        # check for explosion, set to true if the action is taken
        if exploded:
            continue
        
        # if nothing exploded, split the leftmost eligible number then loop again
        split = False

        # check for splitting, set to true if the action is taken
        if split:
            continue

        # if nothing exploded or split, break
        break

    return snailfish_number

def score(snailfish_number):
    return 0


snailfish_numbers = deque([])

with open('python\\test4.in','r') as f:
    for x in f.readlines():
        snailfish_numbers.append(x.strip())

## part 1 ##

""" the given snailfish numbers don't need to be reduced
for snailfish_number in snailfish_numbers:
    snailfish_number = reduce(snailfish_number)
"""

total_snailfish_number = snailfish_numbers.popleft()
while (len(snailfish_numbers) > 0):
    total_snailfish_number = f'[{total_snailfish_number},{snailfish_numbers.popleft()}]'
    total_snailfish_number = reduce(total_snailfish_number)

print(total_snailfish_number)
score = score(total_snailfish_number)

print(score)

## part 2 ##
