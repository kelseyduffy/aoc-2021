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

# in the beginning, the void char starts as a 0
void_char = '0'

## part 1 ##

# each loop of the image processing
for _ in range(2):
    # add two rings of the void char around the existing image, expanding it, since these characters might actually update
    for i in range(len(image)):
        image[i].insert(0,void_char) 
        image[i].insert(0,void_char) 
        image[i].append(void_char)
        image[i].append(void_char)
    image.insert(0,[ch for ch in void_char * len(image[0])])
    image.insert(0,[ch for ch in void_char * len(image[0])])
    image.append([ch for ch in void_char * len(image[0])])
    image.append([ch for ch in void_char * len(image[0])])
    
    new_image = []
    for i in range(len(image)):
        new_row = []
        for j in range(len(image[0])):
            binary_string = ''
            for x in range(-1,2):
                for y in range(-1,2):
                    # concetenate 9 chars into binary string
                    if 0<=i+x<len(image)-1 and 0<=y+j<len(image[0]):
                        binary_string += image[i+x][j+y]
                    else:
                        # add what the void char was before since this is outside the defined boundaries
                        binary_string += void_char 
            
            # convert binary string to int
            index = int(binary_string,2)

            # look up index in enhancement algorithm
            new_row.append(enhancement[index])
        
        # make a new image, putting that character in the x,y spot in the new image
        new_image.append(new_row)

    # reset for next loop
    image = new_image

    # find the new void char for the next round
    binary_void_string = void_char * 9
    void_char = enhancement[int(binary_void_string,2)]

ones = 0
for row in image:
    ones += row.count('1')

print(ones)
