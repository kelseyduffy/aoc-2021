pairs = []

with open('python/05.in','r') as f:
#with open('python/test.in','r') as f:
    for x in f.readlines():
        first, second = x.split(' -> ')
        x1, y1 = first.split(',')
        x2, y2 = second.split(',')
        pairs.append([int(x1), int(y1), int(x2), int(y2)])

## part 1 ##

max_num = max(max(pairs))

counts = [([0] * (max_num + 1)) for i in range(max_num + 1)]

for pair in pairs:
    x1, y1, x2, y2 = pair
    if x1 == x2:
        # process a vertical line
        for i in range(min(y1, y2), max(y1, y2) + 1):
            counts[x1][i] += 1

    elif y1 == y2:
        # process a horizontal line
        for i in range(min(x1, x2), max(x1, x2) + 1):
            counts[i][y1] += 1

    # otherwise skip diagnals

total = 0
for row in counts:
    for cell in row:
        if cell >= 2:
            total += 1

print(total)

## part 2 ##

counts = [([0] * (max_num + 1)) for i in range(max_num + 1)]

for pair in pairs:
    x1, y1, x2, y2 = pair
    if x1 == x2:
        # process a vertical line
        for i in range(min(y1, y2), max(y1, y2) + 1):
            counts[x1][i] += 1

    elif y1 == y2:
        # process a horizontal line
        for i in range(min(x1, x2), max(x1, x2) + 1):
            counts[i][y1] += 1

    else:
        # process the vertical line
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        
        for i in range(abs(x1 - x2) + 1):
            counts[x1 + (i * x_step)][y1 + (i * y_step)] += 1

total = 0
for row in counts:
    for cell in row:
        if cell >= 2:
            total += 1

print(total)