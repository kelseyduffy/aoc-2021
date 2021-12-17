def check_hit(x_velocity, y_velocity):
    
    global x_min, x_max, y_min, y_max

    # all shots start at 0,0
    x = 0
    y = 0

    while x <= x_max and y >= y_min: # while it hasn't yet overshot the target area

        if x_min <= x <= x_max and y_min <= y <= y_max: # if it's in the target area
            return 1

        else: # step the x and y, then adjust the x and y velocities
            x += x_velocity
            y += y_velocity 
            
            y_velocity -= 1
            if x_velocity > 0:
                x_velocity -= 1

    return 0 # if it missed the target area


with open('python\\17.in','r') as f:
    target_area = f.readlines()[0].strip().replace('target area: ','')

x_range, y_range = target_area.split(',')
x_range = x_range.strip().replace('x=','')
y_range = y_range.strip().replace('y=','')

x_min, x_max = x_range.split('..')
y_min, y_max = y_range.split('..')

x_min = int(x_min)
x_max = int(x_max)
y_min = int(y_min)
y_max = int(y_max)

## part 1 ##
 
print(sum(range(-y_min)))

## part 2 ##

x_lower = 0
total = 0
while(total < x_min): # find the lowest x that reaches the beginning of the target area before stalling out
    x_lower += 1
    total += x_lower

# iterate across all possible x's and y's, summing up the results
print(sum([check_hit(x, y) for x in range(x_lower, x_max + 1) for y in range(y_min, -y_min + 1)]))