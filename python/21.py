class player:
    def __init__(self, start_tile):
        self.score = 0
        self.tile = start_tile

class deterministic_die:
    def __init__(self):
        self.face = 0
        self.counter = 0

    def roll(self):
        self.face += 1
        if self.face > 100:
            self.face = 1
        self.counter += 1

        return self.face


with open('python/21.in','r') as f:
    line = f.__next__()
    player1 = player(int(line.split(': ')[1].strip()))
    line = f.__next__()
    player2 = player(int(line.split(': ')[1].strip()))

## part 1 ##

game_die = deterministic_die()

while(player1.score < 1000 and player2.score < 1000):
    
    # player 1
    this_roll = 0

    for _ in range(3):
        this_roll += game_die.roll()
    
    player1.tile += this_roll
    player1.tile = ((player1.tile - 1) % 10) + 1

    player1.score += player1.tile

    if player1.score >= 1000:
        print(player2.score * game_die.counter)
        break

    # player 2
    this_roll = 0

    for _ in range(3):
        this_roll += game_die.roll()
    
    player2.tile += this_roll
    player2.tile = ((player2.tile - 1) % 10) + 1

    player2.score += player2.tile

    if player2.score >= 1000:
        print(player1.score * game_die.counter)
        break
