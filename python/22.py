def check_overlap(cube1, cube2):
    (x1_low, x1_high, y1_low, y1_high, z1_low, z1_high) = cube1
    (x2_low, x2_high, y2_low, y2_high, z2_low, z2_high) = cube2

    # all three axis need to overlap for the cube regions to overlap. edges are inclusive

    if x1_low <= x2_high and x1_high >= x2_low:
        if y1_low <= y2_high and y1_high >= y2_low:
            if z1_low <= z2_high and z1_high >= z2_low:
                return True

    return False

def find_new_cubes(new_cube, foundation_cube, instruction):
    
    global new_regions

    # if they're both on, don't double count the overlap
    if instruction == 'on':
        # add the new cube as is
        new_regions.add(new_cube)
        # add the pieces of the existing cube that are formed with the new cube chunking out of the foundation cube
        find_new_cubes(new_cube, foundation_cube, 'off')
        return

    (new_x_low, new_x_high, new_y_low, new_y_high, new_z_low, new_z_high) = new_cube
    (x_low, x_high, y_low, y_high, z_low, z_high) = foundation_cube

    # split the foundation cube into two pieces so it's not encompassing a side, and return the combined sets
    if x_low < new_x_low and x_high > new_x_high:
       
        # start with the portion that extends beyond the high side of the introding new cube, in the x direction (y, z checked on future loop)
        new_regions.add((new_x_high+1, x_high, y_low, y_high, z_low, z_high))

        # then add the pieces formed from the non-encompassing overlap
        find_new_cubes(new_cube, (x_low, new_x_high, y_low, y_high, z_low, z_high), 'off')
        return

    if y_low < new_y_low and y_high > new_y_high:
        
        # start with the portion that extends beyond the high side of the introding new cube, in the y direction (z checked on future loop, x already checked)
        new_regions.add((x_low, x_high, new_y_high+1, y_high, z_low, z_high))

        # then add the pieces formed from the non-encompassing overlap
        find_new_cubes(new_cube, (x_low, x_high, y_low, new_y_high, z_low, z_high), 'off')
        return

    if z_low < new_z_low and z_high > new_z_high:
        
        # start with the portion that extends beyond the high side of the introding new cube, in the z direction (x,y already checked)
        new_regions.add((x_low, x_high, y_low, y_high, new_z_high+1, z_high))

        # then add the pieces formed from the non-encompassing overlap
        find_new_cubes(new_cube, (x_low, x_high, y_low, y_high, z_low, new_z_high), 'off')
        return
    

    # find overlapping x range and non-overlapping x range
    non_overlap_x = None

    if x_low == new_x_low:
        #    |----------|          existing x
        #    |-------|--|--|       new x -> 3 possibilites for new x's high
        # if they perfectly overlap with each other, the overlap is the range and there's no existing x-cube extension
        
        # only in the case that x extends beyond new_x on the high side, there's a non-overlapping zone that needs to be captured
        if x_high > new_x_high:
            non_overlap_x = (new_x_high + 1, x_high)

    elif x_low > new_x_low:
        #       |----------|       existing x
        #    |----------|--|--|    new x -> 3 possibilites for new x's high

        # only in the case that x extends beyond new_x on the high side, there's a non-overlapping zone that needs to be captured
        if x_high > new_x_high:
            non_overlap_x = (new_x_high + 1, x_high)  # this is the only valid possibility
            
    
    elif x_low < new_x_low:
        #   |-----------|          existing x
        #     |------x--|--|       new x -> 2 possibilites for new x's high  (the completely emcompassing state was already eliminated above)
        non_overlap_x = (x_low, new_x_low - 1)

    # find overlapping y range and non-overlapping y range
    overlap_y = None
    non_overlap_y = None

    if y_low == new_y_low:
        overlap_y = (y_low, min(new_y_high, y_high)) 
        
        if y_high > new_y_high:
            non_overlap_y = (new_y_high + 1, y_high)

    elif y_low > new_y_low:
        overlap_y = (y_low, min(new_y_high, y_high))

        if y_high > new_y_high:
            non_overlap_y = (new_y_high + 1, y_high)
            
    elif y_low < new_y_low:
        overlap_y = (new_y_low, y_high)
        non_overlap_y = (y_low, new_y_low - 1)

    # find overlapping z range and non-overlapping z range
    overlap_z = None
    non_overlap_z = None

    if z_low == new_z_low:
        overlap_z = (z_low, min(new_z_high, z_high)) 
        
        if z_high > new_z_high:
            non_overlap_z = (new_z_high + 1, z_high)

    elif z_low > new_z_low:
        overlap_z = (z_low, min(new_z_high, z_high))

        if z_high > new_z_high:
            non_overlap_z = (new_z_high + 1, z_high)
            
    elif z_low < new_z_low:
        overlap_z = (new_z_low, z_high)
        non_overlap_z = (z_low, new_z_low - 1)

    # guaranteed x, y, and z are normal overlaps now. no encompassing sides
    # Now break the cube region into three pieces, adding them each separately
    # 1: (full x, full y, non-overlap z)
    if non_overlap_z:
        new_regions.add((x_low, x_high, y_low, y_high, non_overlap_z[0], non_overlap_z[1]))
    # 2: (full x, non-overlap y, overlap z)]
    if non_overlap_y:
        new_regions.add((x_low, x_high, non_overlap_y[0], non_overlap_y[1], overlap_z[0], overlap_z[1]))

    # 3: (non-overlap x, overlap y, overlap z) 
    if non_overlap_x:
        new_regions.add((non_overlap_x[0], non_overlap_x[1], overlap_y[0], overlap_y[1], overlap_z[0], overlap_z[1]))
    
    # In theory, 4 is (overlap x, overlap y, overlap z), but that's what we just eliminated
    # this is why overlap x is not a variable that needs to be known

    return

rules = []

with open('python\\22.in','r') as f:
    for line in f.readlines():
        rule = line.strip().replace(' ',',').replace('x=','').replace('y=','').replace('z=','').replace('..',',')
        instr,x1,x2,y1,y2,z1,z2 = rule.split(',')
        rules.append((instr, (int(x1), int(x2), int(y1), int(y2), int(z1), int(z2))))

## part 1 ##
# the 'brute force' method

cubes = {}

for i,rule in enumerate(rules):
    print(i)
    instruction, (x_low, x_high, y_low, y_high, z_low, z_high) = rule

    for x in range(x_low, x_high+1):
        for y in range(y_low, y_high+1):
            for z in range(z_low, z_high+1):
                if instruction == 'on':
                    cubes[(x,y,z)] = 1
                else:
                    cubes[(x,y,z)] = 0
    
    if i == 19: # only do the first 20 rules for part 1
        print(sum(v for _,v in cubes.items()))
        break

## part 2 ##
# the 'actual' method

on_cube_regions = set()
removed_regions = set()
new_regions = set()

for i, rule in enumerate(rules):
    print(i)
    instruction, this_cube_region = rule
    (x_low, x_high, y_low, y_high, z_low, z_high) = this_cube_region

    cubes_overlapped = False
    
    removed_regions.clear()
    new_regions.clear()

    for on_cube_region in on_cube_regions:

        # check to see if the new region overlaps with this existing on cube region
        overlap = check_overlap(this_cube_region, on_cube_region)

        # if it does, mark the existing region for later deletion
        if overlap:

            #print(f'{this_cube_region} overlaps {on_cube_region}')
            removed_regions.add(on_cube_region)

            # call the overlap function
            find_new_cubes(this_cube_region, on_cube_region, instruction)

    # delete the marked regions and add the new regions
    on_cube_regions -= removed_regions
    on_cube_regions.update(new_regions)

    # if the cube region didn't overlap with anything and it's on, add it as is to the on cube regions
    if not cubes_overlapped and instruction == 'on':
        on_cube_regions.add(this_cube_region)

# find the final number of on cubes
count = 0
for on_cube_region in on_cube_regions:
    (x_low, x_high, y_low, y_high, z_low, z_high) = on_cube_region
    count += (x_high - x_low + 1) * (y_high - y_low + 1) * (z_high - z_low + 1)

print(count)