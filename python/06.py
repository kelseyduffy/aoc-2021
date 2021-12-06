fishes = []

with open('python\\06.in','r') as f:
    for x in f.readlines():
       fishes = x.split(',')

start_fishes = [int(f) for f in fishes]

## part 1 ##

fishes = start_fishes
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

## part 2 ##

initial_fish_counts = []
for i in range(9):
    initial_fish_counts.append(sum(fish == i for fish in start_fishes))

#print(initial_fish_counts)

fishes = initial_fish_counts
for day in range(256): 
    new_fishes = [0] * 9
    for i in range(1, 9):
        new_fishes[i-1] = fishes[i]

    new_fishes[6] += fishes[0]
    new_fishes[8] = fishes[0]

    fishes = new_fishes
    
    
print(sum(fishes))
