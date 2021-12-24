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

#if current_digit == (z % 26) + _B_:
#   z = z // _A_ # always either 26 or 1
#else:
#   z = 26 * z + current_digit + _C_

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

print(a_sequence)
print(b_sequence)
print(c_sequence)

# progress notes:
# looking at these a, b, and c sequences
# it's impossible for a==1 to match the %26+b condition because b>=10 in all cases and digit<10
# there's 7 where a = 26, 7 where a = 1. a = 1 multiplies z by 26, a = 26 divides it
# - also, there's never been less 1's than 26's at any point. allowing it to build up and come down cleanly
# therefore, assuming that you need to do 7 of each
# therefore, every a = 26 has to be coerced into matching the modulo expression
# when doing this math, the c values are suspiciously convenient, so this feels right
# - specifically, c is always less than 16, so that _C_ + digit < 26, keeping z%26 = _C_ + digit
# and the equations cover all 14 digits, so this definitely feels right

## functions ##
# d2  =  d5 + 2         <-- d2 must be {3,4,5,6,7,8,9} | d5 must be {1,2,3,4,5,6,7}
# d4  =  d3 + 8         <-- d4 must be 9 | d3 must be 1
# d6  =  d7 + 8         <-- d6 must be 9 | d7 must be 1
# d8  =  d1 + 2         <-- d8 must be {3,4,5,6,7,8,9} | d1 must be {1,2,3,4,5,6,7}
# d9  = d14 + 4         <-- d9 must be {5,6,7,8,9} | d14 must be {1,2,3,4,5}
# d10 = d11 + 6         <-- d10 must be {7,8,9} | d11 must be {1,2,3}
# d12 = d13 + 1         <-- d12 must be {2,3,4,5,6,7,8,9} | d13 must be {1,2,3,4,5,6,7,8}

# i guess solve this for the highest values of the digits?
print(79197919993985)

## part 2 ##

# lowest number is the lowest end of every range
print(13191913571211)

## work ##

# z = 0
#
# 1. _A_ = 1, _C_ = 7
# z = 0*26 + d1 + 7
#
# 2. _A_ = 1, _C_ = 8
# z = (d1+7)*26 + d2 + 8
#
# 3. _A_ = 1, _C_ = 10
# z = ((d1+7)*26 + d2 + 8)*26 + d3 + 10
# z = 26*26*d1 + 26*d2 + d3 + 190*26 + 10
#
# 4. _A_ = 26, _B_ = -2
# z%26 = d4 + 2 = d3 + 10
# >>> d4 = d3 + 8 <<<
# z = z//26 = 26*d1 + d2 + 190
#
# 5. _A_ = 26, _B_ = -10
# z%26 = d5 + 10 = d2 + 8
# >>> d2 = d5 + 8 <<<
# z = z//26 = d1 + 7
#
# 6. _A_ = 1, _C_ = 6
# z = (d1+7)*26 + d6 + 6
#
# 7. _A_ = 26, _B_ = -14
# z%26 = d7 + 14 = d6 + 6
# >>> d6 = d7 + 8 <<<
# z = z//26 = d1 + 7
#
# 8. _A_ = 26, _B_ = -5
# z%26 = d8 + 5 = d1 + 7
# >>> d8 = d1 + 2 <<<
# z = z//26 = 0 
# 
# 9. _A_ = 1, _C_ = 1
# z = 0*26 + d9 + 1
# 
# 10. _A_ = 1, _C_ = 8
# z = (d9+1)*26 + d10 + 8
# 
# 11. _A_ = 26, _B_ = -14
# z%26 = d11 + 14 = d10 + 8
# >>> d10 = d11 + 6 <<<
# z = z//26 = d9 + 1
# 
# 12. _A_ = 1, _C_ = 13
# z = (d9+1)*26 + d12 + 13
#
# 13. _A_ = 26, _B_ = -14
# z%26 = d13 + 14 = d12 + 13
# >>> d12 = d13 + 1 <<<
# z = z//26 = d9 + 1
#
# 14. _A_ = 26, _B_ = -5
# z%26 = d14 + 5 = d9 + 1
# >>> d9 = d14 + 4 <<<
# z = z//26 = 0
