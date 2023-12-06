with open('input.txt') as f:
    data = f.read()

#is there a better way to do this?
seeds = data.split('\n')[0] 
seeds = seeds.split(': ')[1]
seeds = seeds.split()
games = data.split('\n\n')
games.remove(games[0])
games = list(filter(None, games))
win = float('inf')

for individualSeed in seeds:
    bestLocation = int(individualSeed)
    for y in games:
        eachGarden = y.split(':')[1]
        eachGarden = eachGarden.split('\n')
        eachGarden = list(filter(None, eachGarden))
        mainDict = {}
        for z in eachGarden: # each line
            tmpDict = {}
            destRange, sourceRange, rangeLength = z.split(' ')
            destRange, sourceRange, rangeLength = int(destRange), int(sourceRange), int(rangeLength)
            if bestLocation in range(sourceRange, (sourceRange + rangeLength)):
                ranTime = bestLocation - sourceRange # so it looks a little better
                tmpDict[bestLocation] = ranTime + destRange
                mainDict.update(tmpDict)
        if bestLocation in mainDict:
            bestLocation = mainDict[bestLocation]
    if float(bestLocation) < float(win):
        win = float(bestLocation)

print(int(win))


