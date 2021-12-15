def walk(x, y, R, C, scores, min_scores_to_here, current_score, loops=1):
    
    this_score = scores[x%R][y%C] + x//R + y//C
    this_score = ((this_score - 1) % 9) + 1

    current_score += this_score

    if current_score >= min_scores_to_here[x][y]:
        return
    
    min_scores_to_here[x][y] = current_score

    #walk down
    if x < loops * len(scores) - 1:
        walk(x+1, y, R, C, scores, min_scores_to_here, current_score, loops)
    
    #walk right
    if y < loops * len(scores[0]) - 1:
        walk(x, y+1, R, C, scores, min_scores_to_here, current_score, loops)
    
    #walk up
    if x > 1:
        walk(x-1, y, R, C, scores, min_scores_to_here, current_score, loops)
    
    #walk left
    if y > 1:
        walk(x, y-1, R, C, scores, min_scores_to_here, current_score, loops)



scores = []

with open('python\\test.in','r') as f:
    for line in f.readlines():
        scores.append([int(x) for x in line.strip()])

R = len(scores)
C = len(scores[0])

## part 1 ##

max_possible_val = 9 * (R + C) + 1

min_scores_to_here = [([max_possible_val] * C) for _ in range(R)]

min_scores_to_here[0][0] = 0

walk(1, 0, R, C, scores, min_scores_to_here, 0)
walk(0, 1, R, C, scores, min_scores_to_here, 0)

print(min_scores_to_here[-1][-1])

## part 2 ##

max_possible_val = 9 * 5 * (R + C) + 1

min_scores_to_here = [([max_possible_val] * C * 5) for _ in range(R * 5)]

min_scores_to_here[0][0] = 0

walk(1, 0, R, C, scores, min_scores_to_here, 0, loops=5)
walk(0, 1, R, C, scores, min_scores_to_here, 0, loops=5)

print(min_scores_to_here[-1][-1])