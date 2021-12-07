crabs = [int(num) for num in open('python\\07.in').read().strip().split(',')]
#crabs = [int(num) for num in open('python\\test.in').read().strip().split(',')]

## part 1 ##

min_dist = sum(crabs)

for i in range(max(crabs)):
    min_dist = min(sum([abs(crab - i) for crab in crabs]), min_dist)

print(min_dist)

## part 2 ##

min_dist = sum([sum(range(crab + 1)) for crab in crabs])

for i in range(max(crabs)):
    min_dist = min(sum([sum(range(abs(crab - i) + 1)) for crab in crabs]), min_dist)

print(min_dist)