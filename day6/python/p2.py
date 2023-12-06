import os

with open(f'{os.getcwd()}/day6/input.txt') as f:
    data = f.read()

#formatting
time, distanceList = data.split('\n')
time = time.split(':')[1]
time = ''.join([char for char in time if char.isdigit()])
distanceList = distanceList.split(':')[1]
distanceList = ''.join([char for char in distanceList if char.isdigit()])

#prints a 1 if it won, a 0 if it didnt
def calculate(y):
    milsecond = y
    speed = y
    milsecond = int(time) - milsecond
    milPerSecond = speed * milsecond
    if milPerSecond > int(distanceList):
        return(1)
    return(0)

win = y = 0
while y < int(time):
    if calculate(y) == 1:
        win += 1
        while True:
            if calculate(y) == 1:
                y -= 1
            else:
                y += 1
                break
        while True:
            if calculate(y) == 1:
                y += 1000
                win += 1000
            else:
                break
        y -= 1000
        while y < int(time):
            if calculate(y) == 1:
                y += 1
                win += 1
            else:
                y = int(time)
    else:
        y += 1000
    
print(win - 1001) # some reason it adds 1001 to the score