nums = []

def move_right(i, j, nums, basin, current_basin):

    # keep moving up until you hit a wall or a 9
    j += 1
    if j >= len(nums[0]):
        # hit a wall
        return

    elif basin[i][j] != 0:
        # you've been here before
        return

    elif nums[i][j] == 9:
        # hit a 9, set it in basin and stop moving to the right
        basin[i][j] = -1
        return

    # you're still in the basin, set the value to the current basin 
    basin[i][j] = current_basin

    # start moving up, left, then down from here
    move_right(i, j, nums, basin, current_basin)
    move_up(i, j, nums, basin, current_basin)
    move_left(i, j, nums, basin, current_basin)
    move_down(i, j, nums, basin, current_basin)

            
def move_up(i, j, nums, basin, current_basin):

    # keep moving up until you hit a wall or a 9
    i -= 1
    if i < 0:
        # hit a wall
        return

    if basin[i][j] != 0:
        # you've been here before
        return

    if nums[i][j] == 9:
        # hit a 9, set it in basin and stop moving to the right
        basin[i][j] = -1
        return

    # you're still in the basin, set the value to the current basin 
    basin[i][j] = current_basin

    # start moving left then down from here
    move_right(i, j, nums, basin, current_basin)
    move_up(i, j, nums, basin, current_basin)
    move_left(i, j, nums, basin, current_basin)
    move_down(i, j, nums, basin, current_basin)


def move_left(i, j, nums, basin, current_basin):

    j -= 1
    if j < 0:
        # hit a wall
        return

    if basin[i][j] != 0:
        # you've been here before
        return

    if nums[i][j] == 9:
        # hit a 9, set it in basin and stop moving to the right
        basin[i][j] = -1
        return

    basin[i][j] = current_basin

    move_right(i, j, nums, basin, current_basin)
    move_up(i, j, nums, basin, current_basin)
    move_left(i, j, nums, basin, current_basin)
    move_down(i, j, nums, basin, current_basin)


def move_down(i, j, nums, basin, current_basin):

    # keep moving up until you hit a wall or a 9
    i += 1
    if i >= len(nums):
        # hit a wall
        return

    if basin[i][j] != 0:
        # you've been here before
        return

    if nums[i][j] == 9:
        # hit a 9, set it in basin and stop moving to the right
        basin[i][j] = -1
        return
    
    basin[i][j] = current_basin

    move_right(i, j, nums, basin, current_basin)
    move_up(i, j, nums, basin, current_basin)
    move_left(i, j, nums, basin, current_basin)
    move_down(i, j, nums, basin, current_basin) 


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

basin = [[0] * len(nums[0]) for _ in range(len(nums))]

# track the current basin number
current_basin = 0

# start upper left 
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if basin[i][j] == 0:
            # this spot is currently unmarked
            if nums[i][j] == 9:
                # if this is a 9, it's not in a basin
                basin [i][j] = -1
            else:
                # this is the first cell in a new basin
                current_basin += 1

                # mark this cell
                basin[i][j] = current_basin

                # then recursively map the entire basin
                move_right(i, j, nums, basin, current_basin)
                move_up(i, j, nums, basin, current_basin)
                move_left(i, j, nums, basin, current_basin)
                move_down(i, j, nums, basin, current_basin)


basin_counts = [0] * (current_basin + 1)
for x_i in range(len(basin)):
    for x_j in range(len(basin[0])):
        if basin[x_i][x_j] != -1:
            basin_counts[basin[x_i][x_j]] += 1

basin_counts.sort(reverse=True)

print(basin_counts[0] * basin_counts[1] * basin_counts[2])
