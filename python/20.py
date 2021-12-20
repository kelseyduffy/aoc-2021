enhancement = ''
image = []

with open('python/20.in','r') as f:
    for i, line in enumerate(f):
        if i == 0: 
            enhancement = line.strip().replace('.','0').replace('#','1')
        if i < 2:
            continue
        new_line = line.replace('.','0').replace('#','1')
        image.append([ch for ch in new_line.strip()])

print(enhancement)
print(image)

# add two rings of 0s for padding to never exceed list ranges with -1 or +1 indexes
for i in range(len(image)):
    image[i].insert(0,'0') 
    image[i].insert(0,'0') 
    image[i].append('0')
    image[i].append('0')
image.insert(0,[ch for ch in '0' * len(image[0])])
image.insert(0,[ch for ch in '0' * len(image[0])])
image.append([ch for ch in '0' * len(image[0])])
image.append([ch for ch in '0' * len(image[0])])

## part 1 ##

# each loop of the image processing
for counter in range(2):
    # add two rings of 0 around the existing image, expanding it, since these characters might actually update
    this_round_void_char = '0'
    if counter % 2 == 1:
        this_round_void_char = '1'
    for i in range(len(image)):
        image[i].insert(0,this_round_void_char) 
        image[i].insert(0,this_round_void_char) 
        image[i].append(this_round_void_char)
        image[i].append(this_round_void_char)
    image.insert(0,[ch for ch in this_round_void_char * len(image[0])])
    image.insert(0,[ch for ch in this_round_void_char * len(image[0])])
    image.append([ch for ch in this_round_void_char * len(image[0])])
    image.append([ch for ch in this_round_void_char * len(image[0])])

    # for each x and y in the expanded image, except for the first outer ring of 0's which are only there for safe lookups
    new_image = []
    for i in range(1,len(image)-1):
        new_row = [this_round_void_char]
        for j in range(1, len(image[0])-1):
            binary_string = ''
            for x in range(-1,2):
                for y in range(-1,2):
                    # concetenate 9 chars into binary string
                    # wrapping around to -1 is safe because the ends are also 0's
                    binary_string += image[i+x][y+j]
            
            # convert binary string to int
            index = int(binary_string,2)

            # look up index in enhancement algorithm
            new_row.append(enhancement[index])
        
        # make a new image, putting that character in the x,y spot in the new image
        new_row.append(this_round_void_char)
        new_image.append(new_row)

    # reset for next loop
    new_image.insert(0,[ch for ch in this_round_void_char * len(new_row)])
    new_image.append([ch for ch in this_round_void_char * len(new_row)])
    image = new_image

ones = 0
for row in image:
    ones += row.count('1')

print(ones)
