def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

with open('test.txt', 'r') as f:
    data = [line.rstrip() for line in f]

# varaibles
index = 0
win = 0

#formating i think???
for i in data:  #strips the :, but stores the game ID
    temp = i.split(': ', 1)
    if len(temp) > 0:
        i = temp[1]
    numData = ''.join([char for char in temp[0] if char.isdigit()])


    #i could def remove one of tehse varaibles
    gameSet = []
    resultDic = {} 
    addWin = 1


    temp = 0 # for the while loop
    z = 0 # for the while loop

    # finds the position of all ; and stores the index in index
    index = find(i, ";") 
    index.append(len(i))

    # takes the game, makes each set into a list, stores it in gameSet
    while temp < len(index): 
        gameSet.append(i[z:index[temp]])
        z = index[temp] + 2
        temp += 1


    # splits the sets into each "grab" than does the math. i think
    for x in gameSet: 
        # store the index of all , to index
        index = find(x, ',')

        # splits the list from the , so they are individual "grab"
        if len(index) != 0:
            temp = x.split(', ')
        # this else is a just-in-case there is a set with a single "grab", it still gets it. otherwise it will use the last set
        else:
            temp = x

        # when i do the thing up there it doesnt format the single into a list, so i use this to check if it is either the list or single
        if type(temp) == list:
            z = 0
            while z < len(temp):
                temp2 = temp[z].split(' ')
                resultDic.update({temp2[1]:temp2[0]})
                z += 1
        else:
            temp3 = temp.split(' ')
            resultDic = ({temp3[1]:temp3[0]}) # ok i truly do not know why .update does not work here. the onyl answer is python is glazing the last thing or something. 
        

        # done with formating

        
        redCubes = 0
        greenCubes = 0
        blueCubes = 0

        #this is to make sure that it exist. if it doesnt it will get mad
        if 'red' in resultDic:
            redCubes = int(resultDic['red'])
        if 'green' in resultDic:
            greenCubes = int(resultDic['green'])
        if 'blue' in resultDic:
            blueCubes = int(resultDic['blue'])


        if redCubes > 12 or greenCubes > 13 or blueCubes > 14: 
            addWin = -1 
        
    if(addWin > 0):
        win += int(numData)

    print(win) 

# this might be the worst code i have ever written. 