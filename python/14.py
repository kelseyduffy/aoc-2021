from typing import Counter


steps = {}
polymer = ''

with open('python\\14.in','r') as f:
    for i, line in enumerate(f):
        if i == 0: 
            polymer = line.strip()
        if i < 2:
            continue
        (x,y) = line.strip().split(' -> ')
        steps[x] = y


print(polymer)
print(steps)

## part 1 ##

for _ in range(10):
    new_polymer = ''
    for i in range(len(polymer) - 1):

        new_polymer += polymer[i]
        key = polymer[i:i+2]

        if key in steps:
            new_polymer += steps[key]
    
    new_polymer += polymer[-1]

    polymer = new_polymer

#print(polymer)

letter_counts = {}
for letter in polymer:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

max_letter = max(letter_counts, key=letter_counts.get)
min_letter = min(letter_counts, key=letter_counts.get)
print(letter_counts[max_letter] - letter_counts[min_letter])
