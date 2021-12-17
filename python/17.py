def check_hit(x_velocity, y_velocity, min_x, max_x, min_y, max_y):
    
    x = 0
    y = 0

    while x <= max_x and y >= min_y:
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return 1
        else:
            x += x_velocity
            y += y_velocity
            if x_velocity > 0:
                x_velocity -= 1
            elif x_velocity < 0:
                x_velocity += 1
            y_velocity -= 1
    
    return 0


with open('python\\17.in','r') as f:
    target_area = f.readlines()[0].strip().replace('target area: ','')

ranges = target_area.split(',')
x_range = ranges[0].strip().replace('x=','')
y_range = ranges[1].strip().replace('y=','')

xes = x_range.split('..')
yes = y_range.split('..')

x_min = int(xes[0])
x_max = int(xes[1])
y_min = int(yes[0])
y_max = int(yes[1])

## part 1 ##
 
print(sum(range(-y_min)))

## part 2 ##

x_lower = 0
while(True):
    x_lower += 1
    if sum(range(x_lower)) >= x_min:
        break

total_hits = 0

for x in range(x_lower - 1, x_max + 1):
    for y in range(y_min, -y_min + 1):
        total_hits += check_hit(x, y, x_min, x_max, y_min, y_max)

print(total_hits)
# try each pair within range of boundaries
# x upper -> x outer boundary (get it in 1)
# x lower -> x where sum(range(x)) = x inner boundary (guarantee that it can get to the start of the boundary)
# y upper -> -y_min (answer to part 1)
# y lower -> y outer boundary (get it in 1)