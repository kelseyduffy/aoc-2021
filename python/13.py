lines = []

with open('python/13.in','r') as f:
    for x in f.readlines():
        lines.append(x.strip())


folds = []
points = []

for line in lines:
    if line.startswith('fold'):
        pieces = line.replace('fold along ','').split('=')
        folds.append((pieces[0], int(pieces[1])))
    elif len(line) > 1:
        pieces = line.split(',')
        points.append((int(pieces[0]), int(pieces[1])))

## part 1 ##

folded_points = set()

for (x,y) in points:
    (dir, num) = folds[0]
    if dir == 'x':
        if x > num:
            x = 2 * num - x
    else:
        if y > num:
            y = 2 * num - y
    folded_points.add((x,y))

print(len(folded_points))

## part 2 ##

folded_points = set()

for (x,y) in points:
    for (dir,num) in folds:
        if dir == 'x':
            if x > num:
                x = 2 * num - x
        else:
            if y > num:
                y = 2 * num - y
    folded_points.add((x,y))

max_x = 0
max_y = 0
for (x,y) in folded_points:
    max_x = max(x, max_x)
    max_y = max(y, max_y)

password = ''
for y in range(max_y + 1):
    for x in range(max_x + 1):
        password += (' ', '#')[(x,y) in folded_points]
    password += '\n'

print()
print(password)