inputs = []

with open('python\\08.in','r') as f:
    for x in f.readlines():
        #inputs.append(int(x.strip()))
        inputs.append(x.strip())

## part 1 ##

seconds = []
counts = [0,0,0,0] # 1, 4, 7, 8, = 2, 4, 3, 7 letters resp.


for input in inputs:
    first, second = input.split(' | ')
    
    items = second.strip().split(' ')
    for item in items:
        if len(item) == 2:
            counts[0] += 1
        elif len(item) == 4:
            counts[1] += 1
        elif len(item) == 3:
            counts[2] += 1
        elif len(item) == 7:
            counts[3] += 1


print(sum(counts))

## part 2 ##

nums = [{'a','b','c','e','f','g'},      # 0     abc efg
        {'c','f'},                      # 1       c  f
        {'a','c','d','e','g'},          # 2     a cde g      <- this is the only one without an 'f'
        {'a','c','d','f','g'},          # 3     a cd fg
        {'b','c','d','f'},              # 4      bcd f
        {'a','b','d','f','g'},          # 5     ab d fg
        {'a','b','d','e','f','g'},      # 6     ab defg
        {'a','c','f'},                  # 7     a c  f
        {'a','b','c','d','e','f','g'},  # 8     abcdefg
        {'a','b','c','d','f','g'}]      # 9     abcd fg

total = 0

for input in inputs:
    first, second = input.split(' | ')
    
    all_items = first.strip().split(' ') + second.strip().split(' ')
    #items = second.strip().split(' ')

    for item in all_items:
        sixers = []
        fivers = []
        if len(item) == 2:
            cf = {x for x in item}
            
        elif len(item) == 4:
            bcdf = {x for x in item}
            
        elif len(item) == 3:
            acf = {x for x in item}
            
        elif len(item) == 7:
            abcdefg = {x for x in item}

        elif len(item) == 5:
            # they all have a, d, g
            # a cde g
            # a cd fg
            # ab d fg
            fivers.append({x for x in item})

        elif len(item) == 6:
            # they all have a, b, f, g
            # abc efg
            # ab defg
            # abcd fg
            sixers.append({x for x in item})
    
    # a and g are in every 5er and 6er, so union all the sets to reduce down to them
    ag = abcdefg 
    for entry in (fivers + sixers):
        ag = ag & entry

    # a d and g are in every 5er
    adg = abcdefg
    for entry in fivers:
        adg = adg & entry

    abfg = abcdefg
    for entry in sixers:
        abfg = abfg & entry
    
    

    a = acf - cf                # find the a character
    bd = bcdf - cf              # these two are the b and d, in some order
    eg = abcdefg - bcdf - a     # these two are the e and g, in some order
    g = ag - a                  # find which one is g
    e = eg - g                  # find e
    d = adg - ag                # find d
    b = bd - d                  # find b

    for entry in fivers:
        if e in entry:
            acdeg = entry
            break
    
    c = acdeg - a - d - e - g
    f = cf - c

    this_out_string = ''
    for out_piece in second.strip().split(' '):
        if len(item) == 2:
            this_out_string += '1'
            
        elif len(item) == 4:
            this_out_string += '4'
            
        elif len(item) == 3:
            this_out_string += '7'
            
        elif len(item) == 7:
            this_out_string += '8'

        elif len(item) == 5:
            this_set = {x for x in item}
            if e in this_set:           # a cde g
                this_out_string += '2'
            elif c in this_set:         # a cd fg
                this_out_string += '3'
            else:                       # ab d fg
                this_out_string += '5'
            

        elif len(item) == 6:
            this_set = {x for x in item}
            if d not in this_set:       # abc efg
                this_out_string += '0'
            elif c not in this_set:     # ab defg
                this_out_string += '6'
            else:                       # abcd fg
                this_out_string += '9'
    
    total += int(this_out_string)
            
            
print(total)
            
            