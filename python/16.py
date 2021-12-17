def parse_packet():

    global i, version_total, instruction

    version_total += int(instruction[i:i+3], 2)
    i += 3

    type_id = instruction[i:i+3]
    i += 3

    if type_id == '100':
        this_num_str = ''
        
        while(True):
            keep_going = instruction[i]
            i += 1

            this_num_str += instruction[i:i+4]
            i += 4

            if keep_going == '0':
                break

        return int(this_num_str, 2)

    else:
        length_type_id = instruction[i]
        i += 1

        values = []

        if length_type_id == '0':
            # 15 bit representing the number of bits of sub packets contained
            num_sub_packet_bits = int(instruction[i:i+15], 2)
            i += 15

            # keep parsing out the next bits until you hit the limit
            stopping_point = i + num_sub_packet_bits
            while(i < stopping_point):
                this_value = parse_packet()
                values.append(this_value)

        else:
            # 11 bit representing the number of sub packets immedatiately following
            num_sub_packets = int(instruction[i:i+11], 2)
            i += 11

            for _ in range(num_sub_packets):
                this_value = parse_packet()
                values.append(this_value)
        
        if type_id == '000':
            return sum(values)

        elif type_id == '001':
            value = 1
            for this_value in values:
                value *= this_value
            return value

        elif type_id == '010':
            return min(values)

        elif type_id == '011':
            return max(values)

        elif type_id == '101':
            return values[0] > values[1]

        elif type_id == '110':
            return values[0] < values[1]

        elif type_id == '111':
            return values[0] == values[1]
    

with open('python\\16.in','r') as f:
    hex_string = f.readlines()[0].strip()
        
instruction = bin(int(hex_string, 16))[2:] # doesn't contain leading zeros for the very first character

leading_zeros = '0' * (len(hex_string) * 4 - len(instruction))
instruction = leading_zeros + instruction

i = 0
version_total = 0

value = parse_packet()
    
## part 1 ##

print(version_total)

## part 2 ##

print(value)

    

