def next_chunk(current_number, input_state):
    
    global lines, checked_states

    depth = len(current_number)
    
    if ((input_state['w'],input_state['x'],input_state['y'],input_state['z']),depth, current_number[-1]) in checked_states:
        return
    
    checked_states.add(((input_state['w'],input_state['x'],input_state['y'],input_state['z'], current_number[-1]), depth))

    # process the 18 lines at this depth
    this_state = {}
    for k in ['w','x','y','z']:
        this_state[k] = input_state[k]

    this_state['w'] = int(current_number[-1])
    
    start_line = (depth-1) * 18 + 1
    for raw_line in lines[start_line:start_line + 17]:
        line = raw_line.split(' ')
        if line[2] in {'w','x','y','z'}:
            val2 = this_state[line[2]]
        else:
            val2 = int(line[2])
            
        
        if line[0] == 'add':
            this_state[line[1]] = this_state[line[1]] + val2                    

        elif line[0] == 'mul':
            this_state[line[1]] = this_state[line[1]] * val2

        elif line[0] == 'div':
            this_state[line[1]] = this_state[line[1]] // val2

        elif line[0] == 'mod':
            this_state[line[1]] = this_state[line[1]] % val2

        elif line[0] == 'eql':
            this_state[line[1]] = 1 if this_state[line[1]] == val2 else 0

    if depth == 14 and this_state['z'] == 0:
        print(current_number)
        exit()

    elif depth == 14:
        return

    if depth == 7:
        print(f'7 depth: {current_number}')
    
    for val in ['9','8','7','6','5','4','3','2','1']:
        next_chunk(current_number+val,this_state)



lines = []


#with open('python/test.in','r') as f:
with open('python/24.in','r') as f:
    for line in f.readlines():
        #lines.append([x for x in line.strip()])
        #lines.append([int(x) for x in line.strip().split(' -> ')])
        lines.append(line.strip())

## part 1 ##

#inp a - Read an input value and write it to variable a.
#add a b - Add the value of a to the value of b, then store the result in variable a.
#mul a b - Multiply the value of a by the value of b, then store the result in variable a.
#div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
#mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
#eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.

# 14 digit input
# each digit feeds each of the 14 inputs, 1 at a time
# if the final z value is 0, it's a valid number
# find the highest 14 digit number

start_values = {'w':0, 'x':0, 'y':0, 'z':0}

checked_states = set()

current_number = ''

for val in ['9','8','7','6','5','4','3','2','1']:
    next_chunk(current_number+val,start_values)

