def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

with open('input.txt', 'r') as f:
    data = [line.rstrip() for line in f]

# varaibles
index = win = totalPower = 0 

#formating i think???
for i in data:  #strips the :, but stores the game ID
    temp = i.split(': ', 1)
    if len(temp) > 0:
        i = temp[1]

    #i could def remove one of tehse varaibles
    gameSet = []
    resultDic = {} 
    redCubes = greenCubes = blueCubes = 0

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
        if 'red' in resultDic:
            if redCubes < int(resultDic['red']):
                redCubes = int(resultDic['red'])
        if 'green' in resultDic:
            if greenCubes < int(resultDic['green']):
                greenCubes = int(resultDic['green'])
        if 'blue' in resultDic:
            if blueCubes < int(resultDic['blue']):
                blueCubes = int(resultDic['blue'])
    
    power = redCubes * blueCubes * greenCubes
    totalPower = power + totalPower

print(totalPower)

# this might be the worst code i have ever written. 