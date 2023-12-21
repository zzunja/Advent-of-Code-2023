#this works, but ti woudl take 5 years to do.


with open('input.txt') as f:
    data = f.read()

seeds = data.split('\n')[0] 
seeds = seeds.split(': ')[1]
seeds = seeds.split()
games = data.split('\n\n')
games.remove(games[0])
games = list(filter(None, games))
win = float('inf')

rangeSeeds = seeds[1::2]
seeds = seeds[::2]

def returnSeed(individualSeed):
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
            if bestLocation > sourceRange - 1 and bestLocation < sourceRange + rangeLength:
                ranTime = bestLocation - sourceRange # so it looks a little better
                tmpDict[bestLocation] = ranTime + destRange
                mainDict.update(tmpDict)
        if bestLocation in mainDict:
            bestLocation = mainDict[bestLocation]
    return bestLocation

test = 0
for i in seeds:
    for y in range(int(i), int(rangeSeeds[test]) + int(i)):
        if float(returnSeed(y)) < win:
            win = float(returnSeed(y))
    test += 1
    print(test)



print(int(win))