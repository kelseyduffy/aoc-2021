nums = []

with open('python\\09.in','r') as f:
    for line in f.readlines():
        nums.append([int(x) for x in line.strip()])

## part 1 ##

mins = []

for i in range(len(nums)):
    for j in range(len(nums[0])):
        if i > 0 and nums[i][j] >= nums[i-1][j]:
            continue
        if i < len(nums) - 1 and nums[i][j] >= nums[i+1][j]:
            continue
        if j > 0 and nums[i][j] >= nums[i][j-1]:
            continue
        if j < len(nums[0]) - 1 and nums[i][j] >= nums[i][j+1]:
            continue
        mins.append(nums[i][j])

print(sum(mins) + len(mins))

## part 2 ##