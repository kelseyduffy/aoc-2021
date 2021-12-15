import collections

steps = {}
starting_string = ''
final_char = ''

with open('python/14.in','r') as f:
    for i, line in enumerate(f):
        if i == 0: 
            starting_string = line.strip()
            final_char = starting_string[-1]
        if i < 2:
            continue
        (x,y) = line.strip().split(' -> ')
        steps[x] = y

## part 1 ##

polymer = starting_string
for _ in range(10):
    new_polymer = ''
    for i in range(len(polymer) - 1):

        new_polymer += polymer[i]
        new_polymer += steps[polymer[i:i+2]]
    
    new_polymer += polymer[-1]

    polymer = new_polymer

letter_counts = collections.Counter(polymer).most_common()
print(letter_counts[0][1] - letter_counts[-1][1])


## part 2 ##

polymer = {}
for i in range(len(starting_string) - 1):
    
    key = starting_string[i:i+2]
    polymer[key] = polymer.get(key, 0) + 1

for _ in range(40):
    new_polymer = {}
    
    for key in polymer:

        key1 = key[0] + steps[key]
        key2 = steps[key] + key[1]

        new_polymer[key1] = new_polymer.get(key1, 0) + polymer[key]
        new_polymer[key2] = new_polymer.get(key2, 0) + polymer[key]
    
    polymer = new_polymer

letter_counts = {}
for letter_pair in polymer:
    letter_counts[letter_pair[0]] = letter_counts.get(letter_pair[0], 0) + polymer[letter_pair]

letter_counts[final_char] = letter_counts.get(final_char, 0) + 1

max_letter = max(letter_counts, key=letter_counts.get)
min_letter = min(letter_counts, key=letter_counts.get)

print(letter_counts[max_letter] - letter_counts[min_letter])
