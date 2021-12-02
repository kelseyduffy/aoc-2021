nums = []

depth = 0
horiz = 0 

## part 1 ##

with open('python\\02.in','r') as f:
    for x in f.readlines():
        parts = x.split(' ')

        if parts[0] == 'up':
            depth -= int(parts[1])

        elif parts[0] == 'down':
            depth += int(parts[1])

        if parts[0] == 'forward':
            horiz += int(parts[1])

print(horiz * depth)

## part 2 ##

aim = 0
depth = 0
horiz = 0 

with open('python\\02.in','r') as f:
    for x in f.readlines():
        parts = x.split(' ')

        if parts[0] == 'up':
            aim -= int(parts[1])

        elif parts[0] == 'down':
            aim += int(parts[1])

        if parts[0] == 'forward':
            horiz += int(parts[1])
            depth += int(parts[1]) * aim

print(depth * horiz)



