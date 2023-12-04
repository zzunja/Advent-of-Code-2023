#slowest piece of code ive ever written lmao
import os

with open(f'{os.getcwd()}/day4/python/input.txt') as f:
    data = f.read()

indexCard = 0
gameDict = {}

for i in data.split('\n'):
    i = i.split(':')[0]
    i = ''.join([char for char in i if char.isdigit()])
    gameDict[i] = 0

for game in data.split('\n'):
    indexCard += 1
    win = 1
    winNum =  []
    gameNum = []
    cardsWinning = []

    game = game.split(':')[1]
    winGame, game = game.split('|')

    for i in winGame.split(' '):
        winNum.append(i)
    winNum = list(filter(None, winNum)) # clears blank spaces
    for i in game.split(' '):
        gameNum.append(i)
    gameNum = list(filter(None, gameNum))

    for i in winNum:
        for y in gameNum:
            if i == y:
                gameDict[str(indexCard + win)] = gameDict[str(indexCard + win)] + 1
                cardsWinning.append(indexCard + win)
                win += 1

    #this is gonna be disgusting i alr knwo
    win = 1
    if gameDict[str(indexCard)] > 0:
        z = gameDict[str(indexCard + (int(win)) - 1)] # to make it more easy to read for me
        for i in range(z): # how many times the copy of the card card won
            for y in cardsWinning:
                gameDict[str(y)] += 1
    gameDict[str(indexCard)] += 1 #count the original card

print(sum(gameDict.values()))