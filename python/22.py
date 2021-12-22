def check_overlap(cube1, cube2):
    (x1_low, x1_high, y1_low, y1_high, z1_low, z1_high) = cube1
    (x2_low, x2_high, y2_low, y2_high, z2_low, z2_high) = cube2

    # all three axis need to overlap for the cube regions to overlap. edges are inclusive

    if x1_low <= x2_high and x1_high >= x2_low:
        if y1_low <= y2_high and y1_high >= y2_low:
            if z1_low <= z2_high and z1_high >= z2_low:
                return True

    return False

def find_new_cubes(this_cube_region, on_cube_region, instruction):
    new_regions = set()

    return new_regions

rules = []

with open('python\\22.in','r') as f:
    for line in f.readlines():
        rule = line.strip().replace(' ',',').replace('x=','').replace('y=','').replace('z=','').replace('..',',')
        instr,x1,x2,y1,y2,z1,z2 = rule.split(',')
        rules.append((instr, (int(x1), int(x2), int(y1), int(y2), int(z1), int(z2))))

## part 1 ##

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

on_cube_regions = set()

for i, rule in enumerate(rules):
    print(i)
    instruction, this_cube_region = rule
    (x_low, x_high, y_low, y_high, z_low, z_high) = this_cube_region

    cubes_overlapped = False
    removed_regions = set()
    new_regions = set()

    for on_cube_region in on_cube_regions:

        # check to see if the new region overlaps with this existing on cube region
        overlap = check_overlap(this_cube_region, on_cube_region)

        # if it does, mark the existing region for later deletion
        if overlap:

            print(f'{this_cube_region} overlaps {on_cube_region}')
            removed_regions.add(on_cube_region)

            # call the overlap function
            new_regions = find_new_cubes(this_cube_region, on_cube_region, instruction)

    # delete the marked regions
    on_cube_regions -= removed_regions
    on_cube_regions.update(new_regions)

    if not cubes_overlapped and instruction == 'on':
        on_cube_regions.add(this_cube_region)

# find the final number of on cubes
count = 0
for on_cube_region in on_cube_regions:
    (x_low, x_high, y_low, y_high, z_low, z_high) = on_cube_region
    count += (x_high - x_low + 1) * (y_high - y_low + 1) * (z_high - z_low + 1)

print(count)