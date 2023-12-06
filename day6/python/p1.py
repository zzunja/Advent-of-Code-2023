import os

with open(f'{os.getcwd()}/day6/input.txt') as f:
    data = f.read()
    
#formatting
time, distanceList = data.split('\n')
time = time.split(':')[1]
time = time.split(' ')
time = list(filter(None, time))
distanceList = distanceList.split(':')[1]
distanceList = distanceList.split(' ')
distanceList = list(filter(None, distanceList))
tmp = 0
trueWin = 1

for race in time: # for every new race
    win = 0
    y = 0
    milPerSecond = 1
    while y < int(time[tmp]): # new attempt
        y += 1
        milsecond = y
        speed = y
        milsecond = int(time[tmp]) - milsecond
        milPerSecond = speed * milsecond
        if milPerSecond > int(distanceList[tmp]):
            win += 1
    trueWin *= win
    tmp += 1

print(trueWin)


