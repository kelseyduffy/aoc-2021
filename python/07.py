crabs = [int(num) for num in open('python\\07.in').read().strip().split(',')]
#crabs = [int(num) for num in open('python\\test.in').read().strip().split(',')]

## part 1 ##

print(min([sum([abs(crab - i) for crab in crabs]) for i in range(max(crabs))]))

## part 2 ##

print(min([sum([sum(range(abs(crab - i) + 1)) for crab in crabs]) for i in range(max(crabs))]))
