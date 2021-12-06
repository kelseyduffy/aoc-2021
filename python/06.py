fishes = []

with open('python\\06.in','r') as f:
    for x in f.readlines():
       fishes = x.split(',')

fishes = [int(f) for f in fishes]

## part 1 ##
"""
for day in range(80):
    new_fishes = []
    for fish in fishes:
        if fish == 0:
            new_fishes.append(6)
            new_fishes.append(8)
        else:
            new_fishes.append(fish-1)

    fishes = new_fishes

print(len(fishes)) 
"""

## part 2 ##

initial_fish_counts = []
for i in range(9):
    initial_fish_counts.append(sum(fish == i for fish in fishes))

print(initial_fish_counts)

fishes_64 = {}
base_fishes = [0,1,2,3,4,5,6,7,8]

for fish in base_fishes:
    fishes = [fish]
    for day in range(40): # this test of 40 should do 80 on two loops, which is 352195 with this input
        new_fishes = []
        for fish in fishes:
            if fish == 0:
                new_fishes.append(6)
                new_fishes.append(8)
            else:
                new_fishes.append(fish-1)

        fishes = new_fishes
    
    this_base_fish_count_after_64 = []
    for i in range(9):
        this_base_fish_count_after_64.append(sum(fish == i for fish in fishes))
    
    fishes_64[fish] = this_base_fish_count_after_64

print(fishes_64)

fishes_counts_after_64 = [0] * 9
for j in range(9): # starting fishes
    for i in range(9): # what they each turn into
        fishes_counts_after_64[i] += initial_fish_counts[j] * fishes_64[j][i]

print(fishes_counts_after_64)
print(sum(fishes_counts_after_64))


fishes_count_after_128 = [0] * 9
for j in range(9): # starting fishes
    for i in range(9): # what they each turn into
        fishes_count_after_128[i] += fishes_counts_after_64[j] * fishes_64[j][i]

print(fishes_count_after_128)
print(sum(fishes_count_after_128))
