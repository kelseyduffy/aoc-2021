lines = []

with open('python\\10.in','r') as f:
    for x in f.readlines():
        #lines.append(int(x.strip()))
        lines.append(x.strip())

## part 1 ##

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
expected = {'(': ')', '[': ']', '{': '}', '<': '>'}

total = 0

for line in lines:
    stack = []

    for x in line:
        if x in {'(', '[', '{', '<'}:
            stack.append(x)
        else:
            popped_char = stack.pop()
            if expected[popped_char] != x:
                total += scores[x]
                break

print(total)

## part 2 ##

scores = {'(': 1, '[': 2, '{': 3, '<': 4}
line_scores = []

for line in lines:
    stack = []
    corrupted = False

    line_score = 0

    for x in line:
        if x in {'(', '[', '{', '<'}:
            stack.append(x)
        else:
            popped_char = stack.pop()
            if expected[popped_char] != x:
                corrupted = True
    
    if not corrupted:   
        # line is incomplete
        while(len(stack) > 0):
            last_open = stack.pop()
            line_score *= 5
            line_score += scores[last_open]
    
        line_scores.append(line_score)

line_scores.sort()
print(line_scores[len(line_scores)//2])

