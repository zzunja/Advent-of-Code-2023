# could be optimized by a lot.
with open('test.txt') as f:
    data = f.read()

allGames = []
convert = {'T':'20', 'J':'1', 'Q':'22', 'K':'23', 'A':'24'}


#organize into best and worst hand
for line in data.split('\n'):
    bufferGames = []
    hand, bid = line.split(' ')
    tmpHand = list(hand)
    testHand = list(hand)
    for c, p in enumerate(tmpHand):
        if p in convert:
           tmpHand[c] = convert[p]
           testHand[c] = convert[p]
    tmpHand = [eval(q) for q in tmpHand]
    testHand = [eval(q) for q in testHand]

    print()
    if 1 in tmpHand:
        
        print(tmpHand)
        for c, i in enumerate(tmpHand):
            if i == 1:
                num = max(set(tmpHand), key = tmpHand.count)
                testHand[c] = num
    print(testHand)
    count = [testHand.count(x) for x in testHand]

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