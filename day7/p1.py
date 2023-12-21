# could be optimized by a lot.

with open('input.txt') as f:
    data = f.read()

winning = []
convert = {'T':'10', 'J':'1', 'Q':'12', 'K':'13', 'A':'14'}
finish = 0

#organize into best and worst hand
for line in data.split('\n'):
    hand, bid = line.split()
    if len(winning) == 0:
        winning.append([hand,bid])
        continue
    count = -1
    currentHand = []
    compareHand = []
    for i in winning:
        count += 1
        #makes each character a seperate list
        currentHand = list(hand)
        compareHand = list(i[0])
        lost = 0
        #converts T-A into a digit
        for z, y in enumerate(currentHand):
            if not y.isdigit():
                currentHand[z] = convert[y]
        for z, y in enumerate(compareHand):
            if not y.isdigit():
                compareHand[z] = convert[y]
        tmpCurrentHand = currentHand
        tmpCompareHand = compareHand

        #removes everything thats not a duplicate
        currentHand = [item for item in currentHand if currentHand.count(item) > 1]
        compareHand = [item for item in compareHand if compareHand.count(item) > 1]

        currentHandRanking = len(currentHand) - 1
        compareHandRanking = len(compareHand) - 1
        
        #checks for 3 of a kind
        if len(currentHand) == 3:
            currentHandRanking = 3
        if len(compareHand) == 3:
            compareHandRanking = 3

        #checks for 4 of a kind or 2 pair
        if len(currentHand) == 4: 
            for l in currentHand:
                if l == currentHand[0]:
                    currentHandRanking = 5
                    continue
                currentHandRanking = 2
                break
        if len(compareHand) == 4: 
            for l in compareHand:
                if l == compareHand[0]:
                    compareHandRanking = 5
                    continue
                compareHandRanking = 2
                break
        
        
        #check for 5 of a kind or full house
        if len(currentHand) == 5:
            for l in currentHand:
                if l == currentHand[0]:
                    currentHandRanking = 6
                    continue
                currentHandRanking = 4
                break
        if len(compareHand) == 5:
            for l in compareHand:
                if l == compareHand[0]:
                    compareHandRanking = 6
                    continue
                compareHandRanking = 4
                break




        #check if its duplicate
        if compareHandRanking == currentHandRanking:
            for z, y in enumerate(tmpCurrentHand):
                if int(y) == int(tmpCompareHand[z]):
                    continue
                if int(y) < int(tmpCompareHand[z]):
                    lost = 1
                    break
                else:
                    break
        else:
            if currentHandRanking < compareHandRanking:
                lost = 1

        if lost == 0:
            winning.insert(count, [hand,bid])
            break
    winning.append([hand,bid]) #this will cause duplicates, but hack fix

#hack fix for removing duplicates caused
newinning = []
for i in winning:
    if i in newinning:
        continue
    else:
        newinning.append(i)

#gives the rank
for count, i in enumerate(newinning):
    newinning[count].append(len(newinning) - count)
print(newinning)
for i in newinning:
    finish += int(i[1]) * i[2]

print(finish)