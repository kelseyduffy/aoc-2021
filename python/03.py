
counts = [0] * 12
lines = 0

## part 1 ##

with open('python\\03.in','r') as f:
    for x in f.readlines():

        lines += 1
        x = x.strip()

        for i in range(len(x)):
            counts[i] += int(x[i])

print(counts)

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