steps = {}
starting_string = ''
final_char = ''

with open('python\\14.in','r') as f:
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
        key = polymer[i:i+2]

        if key in steps:
            new_polymer += steps[key]
    
    new_polymer += polymer[-1]

    polymer = new_polymer

letter_counts = {}
for letter in polymer:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

max_letter = max(letter_counts, key=letter_counts.get)
min_letter = min(letter_counts, key=letter_counts.get)
print(letter_counts[max_letter] - letter_counts[min_letter])

## part 2 ##

polymer = {}
for i in range(len(starting_string) - 1):
    key = starting_string[i:i+2]
    
    if key not in polymer:
        polymer[key] = 1
    else:
        polymer[key] += 1

for _ in range(40):
    new_polymer = {}
    
    for key in polymer:
        value = polymer[key]

        if key not in steps:
            if key in new_polymer:
                new_polymer[key] += value
            else:
                new_polymer[key] = value

        else:
            key1 = key[0] + steps[key]
            key2 = steps[key] + key[1]

            if key1 in new_polymer:
                new_polymer[key1] += value
            else:
                new_polymer[key1] = value

            if key2 in new_polymer:
                new_polymer[key2] += value
            else:
                new_polymer[key2] = value
    
    polymer = new_polymer

letter_counts = {}
for letter_pair in polymer:
    value = polymer[letter_pair]
    
    if letter_pair[0] in letter_counts:
        letter_counts[letter_pair[0]] += value
    else:
        letter_counts[letter_pair[0]] = value

if final_char in letter_counts:
    letter_counts[final_char] += 1
else:
    letter_counts[final_char] = 1

max_letter = max(letter_counts, key=letter_counts.get)
min_letter = min(letter_counts, key=letter_counts.get)

print(f'{letter_counts[max_letter] - letter_counts[min_letter]}')
