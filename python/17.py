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

