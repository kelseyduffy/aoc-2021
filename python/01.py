nums = []

with open('python\\01.in','r') as f:
    for x in f.readlines():
        nums.append(int(x))

## part 1 ##

inc = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        inc += 1

print(inc)


## part 2 ##

inc = 0

for i in range(3, len(nums)):
    if nums[i] >  nums[i-3]:
        inc += 1

print(inc)