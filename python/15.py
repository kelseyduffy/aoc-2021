import sys

def find_path(scores, loops):
    R = len(scores)
    C = len(scores[0])

    max_possible_val = 9 * loops * (R + C) + 1

    min_scores_to_here = [([max_possible_val] * C * loops) for _ in range(R * loops)]

    min_scores_to_here[0][0] = 0

    walk(1, 0, R, C, scores, min_scores_to_here, 0, loops=loops)
    walk(0, 1, R, C, scores, min_scores_to_here, 0, loops=loops)

    return min_scores_to_here[-1][-1]


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
    
    """ this is safer but causes recursion limit to be hit, and answer is almost correct
    #walk up
    if x > 1:
        walk(x-1, y, R, C, scores, min_scores_to_here, current_score, loops)
    
    #walk left
    if y > 1:
        walk(x, y-1, R, C, scores, min_scores_to_here, current_score, loops)
    """

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

scores = []

with open('python\\15.in','r') as f:
    for line in f.readlines():
        scores.append([int(x) for x in line.strip()])


## part 1 ##

print(find_path(scores, loops = 1))

## part 2 ##

print(find_path(scores, loops = 5))
# correct answer 2935 from 15.in