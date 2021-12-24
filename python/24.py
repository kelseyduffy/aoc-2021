## part 1 ##

# each set of 18 rules is the same structure

# inp w           | w is the digit
# mul x 0         --| x = 0
# add x z         --| x = incoming_z
# mod x 26        --| x = (incoming_z % 26)
# div z _A_       --| z = incoming_x // _A_
# add x _B_       --| x = (incoming_z % 26) + _B_
# eql x w         --| x = 1 if [w == (incoming_z % 26) + _B_] else 0
# eql x 0         | x = 0 if [w == (incoming_z % 26) + _B_] else 1
# mul y 0         --| y = 0
# add y 25        --| y = 25
# mul y x         --| y = 0 if [w == (incoming_z % 26) + _B_] else 25
# add y 1         --| y = 1 if [w == (incoming_z % 26) + _B_] else 26
# mul z y         | z = (incoming_z // _A_) if [w == (incoming_z % 26) + _B_] else 26 * incoming_z
# mul y 0         --| y = 0
# add y w         --| y = w
# add y _C_       --| y = w + _C_
# mul y x         | y = 0 if [w == (incoming_z % 26) + _B_] else (w + _C_)
# add z y         | if [w == (incoming_z % 26) + _B_]: z = (incoming_z // _A_) else (26 * incoming_z) + (w + _C_)

# need to track the list of _A_, _B_, and _C_ values

# then recursively solve that equation for z
# - on each loop passing the next digit for each number
# - depth of 14
# - when 14, if z = 0, print number

def check_num(number, incoming_z):
    # | if [w == (incoming_z % 26) + _B_]: z = (incoming_z // _A_) else (26 * incoming_z) + (w + _C_)
    global a_sequence, b_sequence, c_sequence, num_sequence

    this_digit = int(number[-1])
    depth = len(number) - 1
    z = incoming_z

    if this_digit == (z % 26) + b_sequence[depth]:
        z = z // a_sequence[depth]
    else:
        z = 26 * z + this_digit + c_sequence[depth]
    
    if depth == 13 and z == 0:
        print(number)
        exit()

    if depth == 6:
        print(f'depth of 7: {number}')
    
    if depth < 13:
        for num in num_sequence:
            check_num(number+num, z)

# parse input

lines = []

#with open('python/test.in','r') as f:
with open('python/24.in','r') as f:
    for line in f.readlines():
        #lines.append([x for x in line.strip()])
        #lines.append([int(x) for x in line.strip().split(' -> ')])
        lines.append(line.strip())

# specifically grab the sequence of _A_, _B_, and _C_ values:
a_sequence = [int(line.split(' ')[2]) for line in lines[4::18]]
b_sequence = [int(line.split(' ')[2]) for line in lines[5::18]]
c_sequence = [int(line.split(' ')[2]) for line in lines[15::18]]

num_sequence = [str(i) for i in reversed(range(1,10))]

for num in num_sequence:
    check_num(num, 0)