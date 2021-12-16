instruction = ''

with open('python\\test.in','r') as f:
    instruction = bin(int(f.readlines()[0].strip(), 16))[2:]

print(instruction)
print('110100101111111000101000')

i = 0
while(True):
    
    version = int(instruction[i:i+3], 2)
    i += 3

    type_id = int(instruction[i:i+3], 2)
    i += 3

    if type_id == 4:
        this_num_str = ''

        keep_going = True
        
        while(keep_going):
            keep_going = bool(int(instruction[i:i+1]))
            this_num_str += instruction[i+1:i+5]

            i += 5

        this_num = int(this_num_str, 2)

        print(this_num)

    else:
        pass

