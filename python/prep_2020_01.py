nums = set()

with open('prep_2020_01.in','r') as f:
    for x in f.readlines():
        nums.add(int(x))

## part 1 ##

for num in nums:
    remainder = 2020 - num
    if remainder in nums:
        print(remainder * num)
        break

## part 2 ##

for num1 in nums:
    for num2 in nums:
        remainder = 2020 - num1 - num2
        if remainder in nums:
            print(remainder * num1 * num2)
            exit()
