
## part 1 ##

counts = [0] * 12
lines = 0

with open('python\\03.in','r') as f:
    for x in f.readlines():

        lines += 1
        x = x.strip()

        for i in range(len(x)):
            counts[i] += int(x[i])

cutoff = lines/2

gamma_str = ''
epsilon_str = ''

for count in counts:
    if count > cutoff:
        gamma_str += '1'
        epsilon_str += '0'
    else:
        gamma_str += '0'
        epsilon_str += '1'

print(int(gamma_str,2) * int(epsilon_str,2))

## part 2 ##

starting_nums = []
o2_num = 0
co2_num = 0

with open('python\\03.in','r') as f:
    for line in f.readlines():
        starting_nums.append(line)

# O2 rating

o2_rating = [x for x in starting_nums]
binary_string = ''

for i in range(12):
    count = 0
    cutoff = len(o2_rating) / 2

    for x in o2_rating:
        if x[i] == '1':
            count += 1
    
    if count >= cutoff:
        binary_string += '1'
    else:
        binary_string += '0'
    
    o2_rating = [x for x in o2_rating if x.startswith(binary_string)]

    if len(o2_rating) == 1:
        o2_num = int(o2_rating[0], 2)
        break

# O2 rating

co2_rating = [x for x in starting_nums]
binary_string = ''

for i in range(12):
    count = 0
    cutoff = len(co2_rating) / 2

    for x in co2_rating:
        if x[i] == '1':
            count += 1
    
    if count < cutoff:
        binary_string += '1'
    else:
        binary_string += '0'
    
    co2_rating = [x for x in co2_rating if x.startswith(binary_string)]

    if len(co2_rating) == 1:
        co2_num = int(co2_rating[0], 2)
        break

print(o2_num * co2_num)