import os

with open(f'{os.getcwd()}/day4/python/input.txt') as f:
    data = f.read()

total = 0

for game in data.split('\n'):
    tmpTotal = 0
    winNum = []
    gameNum = []
    game = game.split(':')[1]
    winGame, game = game.split('|')
    
    for i in winGame.split(' '):
        winNum.append(i)
    winNum = list(filter(None, winNum)) # clears blank spaces
    for i in game.split(' '):
        gameNum.append(i)
    gameNum = list(filter(None, gameNum))

    #prob a better way to do this
    for i in winNum: 
        for y in gameNum:
            if int(i) == int(y):
                if tmpTotal == 0:
                    tmpTotal += 1
                else:
                    tmpTotal += tmpTotal
    total += tmpTotal

print(total)