from collections import deque

def reduce(snailfish_number):
    
    while(True):
        # explode the leftmost eligible pair then loop again
        has_exploded = False

        level = 0
        for i in range(len(snailfish_number)):
            if snailfish_number[i] == '[':
                level += 1
            elif snailfish_number[i] == ']':
                level -= 1
            
            assert level < 6, f'unexpected level of {level}'

            if level == 5:
                has_exploded = True
                snailfish_number = explode(snailfish_number, i)
                break

        # check for explosion, set to true if the action is taken
        if has_exploded:
            continue
        
        # if nothing exploded, split the leftmost eligible number then loop again
        has_split = False

        is_digit = False
        for i in range(len(snailfish_number)):
            if snailfish_number[i] in { '[', ',', ']' }:
                is_digit = False
            else:
                if is_digit:
                    has_split = True
                    snailfish_number = split(snailfish_number, i-1)
                    break
                is_digit = True

        # check for splitting, set to true if the action is taken
        if has_split:
            continue

        # if nothing exploded or split, break
        break

    return snailfish_number


def explode(snailfish_number, i):

    # start at i, which should be a '[' char
    assert snailfish_number[i] == '[', f'character {i} of {snailfish_number} was supposed to be a [ but was instead {snailfish_number[i]}'

    # find the number as int to the right of the '[' character (could be two digits, until the ',')
    right_i = i + 1
    first_num_string = snailfish_number[right_i]
    right_i += 1
    if snailfish_number[right_i] != ',':
        first_num_string += snailfish_number[right_i]
        right_i += 1
    
    first_num = int(first_num_string) #right_i is now the character after the number

    # find the number (if any) as int to the left of the '[' (could be two digits)
    found_left_number = False
    left_i = i
    left_is_two_digits = False
    while left_i > 0:
        left_i -= 1
        if snailfish_number[left_i] in { '[', ',', ']' }:
            continue
        else:
            found_left_number = True
            end_left_num = left_i + 1
            if snailfish_number[left_i - 1] not in { '[', ',', ']' }:
                left_i -= 1
                left_is_two_digits = True
            break

    # add the two together and store that as the new number to the left
    if found_left_number:
        left_num_string = snailfish_number[left_i]
        if left_is_two_digits:
            left_num_string += snailfish_number[left_i + 1]
        
        next_left_num = int(left_num_string) + first_num

    # find the number as int to the right of the ',' (could be two digits) until the ']'
    right_i += 1
    second_num_string = snailfish_number[right_i]
    right_i += 1
    if snailfish_number[right_i] != ']':
        second_num_string += snailfish_number[right_i]
        right_i += 1
    
    end_of_pair_index = right_i + 1

    second_num = int(second_num_string)

    # find the number (if any) after that number to the right 
    right_i -= 1
    found_right_number = False
    right_num_string = ''
    while right_i < (len(snailfish_number) - 1):
        right_i += 1
        if snailfish_number[right_i] in { '[', ',', ']' }:
            continue
        else:
            right_num_string = snailfish_number[right_i]
            found_right_number = True
            end_of_right_num = right_i + 1
            if snailfish_number[right_i + 1] not in { '[', ',', ']' }:
                right_num_string += snailfish_number[right_i + 1]
                end_of_right_num += 1
            break

    # add the first to the second storing that as the new second number
    if found_right_number:
        next_right_num = int(right_num_string) + second_num


    # recombine the three parts into one string
    # (before left num - new left num - between left and exploded pair - 0 - between exploded pair and right - new right num - after right num)
    exploded_snailfish_number = ''

    if found_left_number:
        exploded_snailfish_number += snailfish_number[:left_i]                  # before left num
        exploded_snailfish_number += f'{next_left_num}'                         # new left num 
    else:
        end_left_num = 0

    exploded_snailfish_number += snailfish_number[end_left_num:i]               # between left and exploded pair 

    exploded_snailfish_number += '0'                                            # replace the exploded pair with a 0

    exploded_snailfish_number += snailfish_number[end_of_pair_index:right_i]    # between exploded pair and right

    if found_right_number:
        exploded_snailfish_number += f'{next_right_num}'                        # new right num 
        exploded_snailfish_number += snailfish_number[end_of_right_num:]        # before left num
    else:
        exploded_snailfish_number += snailfish_number[-1]                       # the accounting is off by 1 if you don't have a final piece

    return exploded_snailfish_number


def split(snailfish_number, i):
    # find the int to be split. it starts at i and goes an extra place (assert that it doesnt go 3?)
    splitting_num = int(snailfish_number[i:i+2])

    # the left piece is divided by two rounded down
    left = splitting_num // 2

    # the right is divided by two rounded up
    right = left + (splitting_num % 2)
    split_pair = f'[{left},{right}]' 

    # reassemble the number with the pre-{split}-post pieces together and return it
    #return f'{snailfish_number[:i]}{split_pair}{snailfish_number[i+2:]}'

    split_snailfish_number = snailfish_number[:i]
    split_snailfish_number += split_pair
    split_snailfish_number += snailfish_number[i+2:]

    return split_snailfish_number


def score(snailfish_number):
    
    # if the term is just a number, it's that number
    if snailfish_number.isnumeric():
        return int(snailfish_number)

    # remove outermost [ and ], and find the comma that separates the two inner terms
    i = 0
    level = 0
    for i in range(len(snailfish_number)):
        
        i += 1

        if snailfish_number[i] == '[': 
            level += 1
        elif snailfish_number[i] == ']':
            level -= 1
        elif snailfish_number[i] == ',' and level == 0:
            left_number = snailfish_number[1:i]
            right_number = snailfish_number[i+1:-1]
            break

    # return 3 * score(left) + 2 * score(right)
    return 3 * score(left_number) + 2 * score(right_number)


snailfish_numbers = deque([])

with open('python\\18.in','r') as f:
    for x in f.readlines():
        snailfish_numbers.append(x.strip())

## part 1 ##

""" the given snailfish numbers don't need to be reduced
for snailfish_number in snailfish_numbers:
    snailfish_number = reduce(snailfish_number)
"""

total_snailfish_number = snailfish_numbers.popleft()
while (len(snailfish_numbers) > 0):
    total_snailfish_number = f'[{total_snailfish_number},{snailfish_numbers.popleft()}]'
    total_snailfish_number = reduce(total_snailfish_number)

print(total_snailfish_number)
score = score(total_snailfish_number)

print(score)

## part 2 ##
