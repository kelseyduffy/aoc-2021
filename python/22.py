lines = []

with open('python\\22.in','r') as f:
    for line in f.readlines():
        #lines.append(int(line.strip()))
        
        instruction,coords = line.strip().split()
        x,y,z = coords.split(',')
        x_low, x_high = x.replace('x=','').split('..')
        x_low = int(x_low)
        x_high = int(x_high)
        y_low, y_high = y.replace('y=','').split('..')
        y_low = int(y_low)
        y_high = int(y_high)
        z_low, z_high = z.replace('z=','').split('..')
        z_low = int(z_low)
        z_high = int(z_high)

        lines.append((instruction, x_low, x_high, y_low, y_high, z_low, z_high))

## part 1 ##

cubes = {}

#print(lines)

for i,line in enumerate(lines):
    print(i)
    instruction, x_low, x_high, y_low, y_high, z_low, z_high = line

    for x in range(x_low, x_high+1):
        for y in range(y_low, y_high+1):
            for z in range(z_low, z_high+1):
                if instruction == 'on':
                    cubes[(x,y,z)] = 1
                else:
                    cubes[(x,y,z)] = 0
    
    if i == 19: # only do the first 20 rules for part 1
        print(sum(v for k,v in cubes.items()))
        break

