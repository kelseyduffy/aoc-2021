def walk(x, y, scores, min_scores_to_here, current_score):
    
    current_score += scores[x][y]

    if current_score >= min_scores_to_here[x][y]:
        return
    
    min_scores_to_here[x][y] = current_score

    #walk down
    if x < len(scores) - 1:
        walk(x+1, y, scores, min_scores_to_here, current_score)
    
    #walk right
    if y < len(scores[0]) - 1:
        walk(x, y+1, scores, min_scores_to_here, current_score)
    
    #walk up
    if x > 1:
        walk(x-1, y, scores, min_scores_to_here, current_score)
    
    #walk left
    if y > 1:
        walk(x, y-1, scores, min_scores_to_here, current_score)



scores = []

with open('python\\15.in','r') as f:
    for line in f.readlines():
        scores.append([int(x) for x in line.strip()])

R = len(scores)
C = len(scores[0])
max_possible_val = 9 * (R + C) + 1

min_scores_to_here = [([max_possible_val] * C) for _ in range(R)]

min_scores_to_here[0][0] = 0

walk(1, 0, scores, min_scores_to_here, 0)
walk(0, 1, scores, min_scores_to_here, 0)

#min_scores_to_here[99][99] = 1
print(min_scores_to_here[-1][-1])
