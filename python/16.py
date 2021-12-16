def parse_next_packet(i, instruction, version_total):

    version_total += int(instruction[i:i+3], 2)
    i += 3

    type_id = int(instruction[i:i+3], 2)
    i += 3

    if type_id == 4:
        this_num_str = ''

        keep_going = True
        
        while(keep_going):
            keep_going = bool(int(instruction[i]))
            i += 1

            this_num_str += instruction[i:i+4]
            i += 4

        value = int(this_num_str, 2)

    else:
        length_type_id = instruction[i]
        i += 1

        these_values = []

        if length_type_id == '0':
            # 15 bit representing the number of bits of sub packets contained
            num_sub_packet_bits = int(instruction[i:i+15], 2)
            i += 15

            # keep parsing out the next bits until you hit the limit
            stopping_point = i + num_sub_packet_bits
            while(i < stopping_point):
                i, version_total, this_value = parse_next_packet(i, instruction, version_total)
                these_values.append(this_value)

            # assert that it didn't go too far
            assert i == stopping_point

        else:
            # 11 bit representing the number of sub packets immedatiately following
            num_sub_packets = int(instruction[i:i+11], 2)
            i += 11

            for _ in range(num_sub_packets):
                i, version_total, this_value = parse_next_packet(i, instruction, version_total)
                these_values.append(this_value)
        
        if type_id == 0:
            value = sum(these_values)

        elif type_id == 1:
            value = 1
            for this_value in these_values:
                value *= this_value

        elif type_id == 2:
            value = min(these_values)

        elif type_id == 3:
            value = max(these_values)

        elif type_id == 5:
            value = these_values[0] > these_values[1]

        elif type_id == 6:
            value = these_values[0] < these_values[1]
            pass

        elif type_id == 7:
            value = these_values[0] == these_values[1]
            pass
    
    return i, version_total, value

instruction = ''

with open('python\\16.in','r') as f:
    for x in f.readlines()[0].strip():
        instruction += format(int(x, 16), '#06b')[2:]
        #instruction += bin(int(f.readlines()[0].strip(), 16))[2:] # doesn't contain leading zeros for the very first character

#print(instruction)
#print('110100101111111000101000') # test.in
#print('00111000000000000110111101000101001010010001001000000000') # test2.in

i = 0
version_total = 0

while(int(instruction[i:], 2) != 0):
    i, version_total, value = parse_next_packet(i, instruction, version_total)
    
## part 1 ##

print(version_total)

## part 2 ##

print(value)

    

