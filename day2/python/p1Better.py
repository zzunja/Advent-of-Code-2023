with open("input.txt") as f:
    data = f.read()

win = 0

for game in data.split('\n'): #split at every new line. which is every game
    redCubes = blueCubes = greenCubes = 0
    id, game = game.split(': ')
    id = ''.join([char for char in id if char.isdigit()])
    
    for gameSet in game.split('; '):
        lose = 0
        gameDict = {}
        for individualGame in gameSet.split(', '):
            gameDict.update({individualGame.split(' ')[1] : individualGame.split(' ')[0]})
        
        #there is prob a better way to do this
        if 'red' in gameDict:
            redCubes = int(gameDict['red'])
        if 'green' in gameDict:
            greenCubes = int(gameDict['green'])
        if 'blue' in gameDict:
            blueCubes = int(gameDict['blue'])


        if redCubes > 12 or greenCubes > 13 or blueCubes > 14:
            lose = 1
            break
    
    if lose == 0:
        win = int(id) + win
print(win)