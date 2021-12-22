rules = []

with open('python\\22.in','r') as f:
    for line in f.readlines():
        rule = line.strip().replace(' ',',').replace('x=','').replace('y=','').replace('z=','').replace('..',',')
        instr,x1,x2,y1,y2,z1,z2 = rule.split(',')
        rules.append((instr, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)))

## part 1 ##

cubes = {}

#print(lines)

for i,rule in enumerate(rules):
    print(i)
    instruction, x_low, x_high, y_low, y_high, z_low, z_high = rule

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

