lines = []

with open('python\\08.in','r') as f:
    for x in f.readlines():
        lines.append(x.strip())

## part 1 ##

total_1748s = 0

for line in lines:
    input, output = line.split(' | ')
    
    out_digits = output.strip().split(' ')
    for out_digit in out_digits:
        if len(out_digit) in [2, 3, 4, 7]:
            total_1748s += 1

print(total_1748s)

## part 2 ##

# 0     abc efg
# 1       c  f
# 2     a cde g      <- this is the only one without an 'f'
# 3     a cd fg
# 4      bcd f
# 5     ab d fg
# 6     ab defg
# 7     a c  f
# 8     abcdefg
# 9     abcd fg

total = 0
all_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

for line in lines:
    input, output = line.split(' | ')
    
    in_digits = input.strip().split(' ')
    out_digits = output.strip().split(' ')
    
    sixers = []
    fivers = []

    for in_digit in in_digits:
        
        if len(in_digit) == 2:
            cf = {x for x in in_digit}
            
        elif len(in_digit) == 4:
            bcdf = {x for x in in_digit}
            
        elif len(in_digit) == 3:
            acf = {x for x in in_digit}
            
        elif len(in_digit) == 7:
            abcdefg = {x for x in in_digit}

        elif len(in_digit) == 5:
            # they all have a, d, g
            # a cde g
            # a cd fg
            # ab d fg
            fivers.append({x for x in in_digit})

        elif len(in_digit) == 6:
            # they all have a, b, f, g
            # abc efg
            # ab defg
            # abcd fg
            sixers.append({x for x in in_digit})
    
    # a and g are in every fiver and sixer, so union all the sets to reduce down to them
    ag = all_letters 
    for entry in (fivers + sixers):
        ag = ag & entry

    # a d and g are in every fiver
    adg = all_letters
    for entry in fivers:
        adg = adg & entry

    # a b f and g are in every sixer
    abfg = all_letters
    for entry in sixers:
        abfg = abfg & entry
    
    a = acf - cf                # find the a character
    bd = bcdf - cf              # these two are the b and d, in some order
    eg = abcdefg - bcdf - a     # these two are the e and g, in some order
    g = ag - a                  # find which one is g
    e = eg - g                  # find e
    d = adg - ag                # find d
    b = bd - d                  # find b

    out_string = ''
    for out_digit in out_digits:

        this_digit = ''

        if len(out_digit) == 2:
            this_digit = '1'
            
        elif len(out_digit) == 4:
            this_digit = '4'
            
        elif len(out_digit) == 3:
            this_digit = '7'
            
        elif len(out_digit) == 7:
            this_digit = '8'

        elif len(out_digit) == 5:
            this_set = {x for x in out_digit}
            if e.issubset(this_set):           # a cde g
                this_digit = '2'
            elif b.issubset(this_set):         # ab d fg
                this_digit = '5'
            else:                              # a cd fg
                this_digit = '3'
            

        elif len(out_digit) == 6:
            this_set = {x for x in out_digit}
            if not d.issubset(this_set):       # abc efg
                this_digit = '0'
            elif e.issubset(this_set):         # ab defg
                this_digit = '6'
            else:                              # abcd fg
                this_digit = '9'

        out_string += this_digit
    
    total += int(out_string)
                  
print(total)            