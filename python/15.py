from collections import deque
import bisect

class Node:
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score

    def __lt__(self, other):
        return self.score < other.score


scores = []

with open('python/15.in','r') as f:
    for line in f.readlines():
        scores.append([int(x) for x in line.strip()])

R = len(scores)
C = len(scores[0])

## part 1 ##

visited_nodes = set()

next_to_visit = deque([])
current_node = Node(0,0,0)

while current_node.x != R-1 or current_node.y != C-1:

    if (current_node.x, current_node.y) not in visited_nodes:
        
        visited_nodes.add((current_node.x, current_node.y))

        if current_node.x < R-1 and (current_node.x + 1, current_node.y) not in visited_nodes: # go down
            bisect.insort(next_to_visit, Node(current_node.x+1, current_node.y, current_node.score + scores[current_node.x+1][current_node.y]))
        
        if current_node.y < C-1 and (current_node.x, current_node.y + 1) not in visited_nodes: # go right
            bisect.insort(next_to_visit, Node(current_node.x, current_node.y+1, current_node.score + scores[current_node.x][current_node.y+1]))

        if current_node.x > 0 and (current_node.x - 1, current_node.y) not in visited_nodes: # go up
            bisect.insort(next_to_visit, Node(current_node.x-1, current_node.y, current_node.score + scores[current_node.x-1][current_node.y]))
        
        if current_node.y > 0 and (current_node.x, current_node.y - 1) not in visited_nodes: # go left
            bisect.insort(next_to_visit, Node(current_node.x, current_node.y-1, current_node.score + scores[current_node.x][current_node.y-1]))
        
    current_node = next_to_visit.popleft()

print(current_node.score)

## part 2 ##

visited_nodes = set()

next_to_visit = deque([])
current_node = Node(0,0,0)

loops = 5

while current_node.x != (loops * R - 1) or current_node.y != (loops * C - 1):

    if (current_node.x, current_node.y) not in visited_nodes:
        
        visited_nodes.add((current_node.x, current_node.y))

        if current_node.x < loops * R - 1 and (current_node.x + 1, current_node.y) not in visited_nodes: # go down
            score_increase = scores[(current_node.x+1) % R][(current_node.y) % C] + ((current_node.x+1) // R) + (current_node.y // C)
            score_increase = ((score_increase - 1) % 9) + 1
            bisect.insort(next_to_visit, Node(current_node.x+1, current_node.y, current_node.score + score_increase))
        
        if current_node.y < loops * C - 1 and (current_node.x, current_node.y + 1) not in visited_nodes: # go right
            score_increase = scores[current_node.x % R][(current_node.y+1) % C] + (current_node.x // R) + ((current_node.y+1)// C)
            score_increase = ((score_increase - 1) % 9) + 1
            bisect.insort(next_to_visit, Node(current_node.x, current_node.y+1, current_node.score + score_increase))

        if current_node.x > 0 and (current_node.x - 1, current_node.y) not in visited_nodes: # go up
            score_increase = scores[(current_node.x-1) % R][(current_node.y) % C] + ((current_node.x-1) // R) + (current_node.y // C)
            score_increase = ((score_increase - 1) % 9) + 1
            bisect.insort(next_to_visit, Node(current_node.x-1, current_node.y, current_node.score + score_increase))
        
        if current_node.y > 0 and (current_node.x, current_node.y - 1) not in visited_nodes: # go left
            score_increase = scores[current_node.x % R][(current_node.y-1) % C] + (current_node.x // R) + ((current_node.y-1)// C)
            score_increase = ((score_increase - 1) % 9) + 1
            bisect.insort(next_to_visit, Node(current_node.x, current_node.y-1, current_node.score + score_increase))
        
    current_node = next_to_visit.popleft()

print(current_node.score)