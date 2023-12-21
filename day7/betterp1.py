# could be optimized by a lot.
with open('input.txt') as f:
    data = f.read()

allGames = []
convert = {'T':'10', 'J':'11', 'Q':'12', 'K':'13', 'A':'14'}


#organize into best and worst hand
for line in data.split('\n'):
    bufferGames = []
    hand, bid = line.split(' ')
    tmpHand = list(hand)
    for c, i in enumerate(tmpHand):
        if i in convert:
           tmpHand[c] = convert[i]
    count = [tmpHand.count(x) for x in tmpHand]

    if max(count) == 1:
        ranking = 0
        bufferGames = [hand, int(bid), ranking]
    if max(count) == 5:
        ranking = 6
        bufferGames = [hand, int(bid), ranking]
    if max(count) == 2:
        if count.count(2) == 4:
            ranking = 2
            bufferGames = [hand, int(bid), ranking]
        else:
            ranking = 1
            bufferGames = [hand, int(bid), ranking]
    if max(count) == 3:
        if 2 in count:
            ranking = 4
            bufferGames = [hand, int(bid), ranking]
        else:
            ranking = 3
            bufferGames = [hand, int(bid), ranking]
    if max(count) == 4:
        ranking = 5
        bufferGames = [hand, int(bid), ranking]



    if len(allGames) == 0:
        allGames.append([hand, int(bid), ranking])
        continue
    for c, y in enumerate(allGames):
        lost = 0
        if y[2] < bufferGames[2]: 
            allGames.insert(c, bufferGames)
            break
        elif y[2] > bufferGames[2]: 
            continue
        else:
            #duplicate clause
            testOne = list(y[0])
            for l, i in enumerate(testOne):
                if i in convert:
                    testOne[l] = convert[i]

            for z, m in enumerate(testOne):
                if int(m) == int(tmpHand[z]):
                    continue
                if int(m) > int(tmpHand[z]):
                    break
                else:
                    allGames.insert(c, bufferGames)
                    lost = 1
                    break
        if lost == 1:
            break
    allGames.append([hand, int(bid), ranking]) #hack fix

#hack fix
newAllGames = []
for i in allGames:
    if i in newAllGames:
        continue
    else:
        newAllGames.append(i)


win = 0
for count, i in enumerate(newAllGames):
    newAllGames[count].append(len(newAllGames) - count)
print(newAllGames)
for i in newAllGames:
    win += int(i[1]) * i[3]

print(win)