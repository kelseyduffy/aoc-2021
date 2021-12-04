def is_winner(board) -> bool:
    for row in board:
        if sum(row) == -5:
            return True

    for q in range(5):
        if board[0][q] + board[1][q] + board[2][q] + board[3][q] + board[4][q] == -5:
            return True
    
    return False

nums = []

with open('python\\04.in','r') as f:
    for x in f.readlines():
        nums.append(x)

boards = []

## part 1 ##
"""
for x in range(2, len(nums), 6):
    
    thisboard = []
    for i in range(5):
        this_row = nums[x+i].strip().split(' ')
        this_row = [int(m) for m in this_row if m != '']
        thisboard.append(this_row)

    
    boards.append(thisboard)

for ball in nums[0].split(','):
    ball = int(ball)

    for f in range(len(boards)):
        for g in range(5):
            for h in range(5):
                if boards[f][g][h] == ball:
                    boards[f][g][h] = -1

    for board in boards:
        for row in board:
            if sum(row) == -5:
                winner = board
                row_tot = 0
                for row2 in winner:
                    row_tot += sum([u for u in row2 if u > -1])

                print(row_tot * ball)
                print('here') # throw a breakpoint here to stop at this point

        for q in range(5):
            if board[0][q] + board[1][q] + board[2][q] + board[3][q] + board[4][q] == -5:
                winner = board
                row_tot = 0
                for row2 in winner:
                    row_tot += sum([u for u in row2 if u > -1])

                print(row_tot * ball)
                print('here') # throw a breakpoint here to stop at this point


"""



## part 2 ##

for x in range(2, len(nums), 6):
    
    thisboard = []
    for i in range(5):
        this_row = nums[x+i].strip().split(' ')
        this_row = [int(m) for m in this_row if m != '']
        thisboard.append(this_row)

    
    boards.append(thisboard)

last_board = False
for ball in nums[0].split(','):
    ball = int(ball)

    for f in range(len(boards)):
        for g in range(5):
            for h in range(5):
                if boards[f][g][h] == ball:
                    boards[f][g][h] = -1

    if not last_board:
        boards = [board for board in boards if not is_winner(board)]
    
        if len(boards) == 1:
            last_board = True
    
    else:
        if is_winner(boards[0]):
            row_tot = 0
            for row2 in boards[0]:
                row_tot += sum([u for u in row2 if u > -1])

            print(row_tot * ball)
        
            break
