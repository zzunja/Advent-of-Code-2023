import re

with open("input.txt") as f:
    data = f.read().splitlines()

numArr = []
for lines in data:
    numArr += re.split(r'\D+', lines)

numArr = [x for x in numArr if x.isdigit()]
numArr = list(set(numArr))

lineCount = 0
string = []
finish = 0
bufferList = []


for lines in data:
    for char in lines:
        if char not in '.' and not char.isnumeric():
            for indexLines in range(-1,2): # index of lines
                symbolIndex = lines.index(char)
                for indexChar in range(-1,2): # index of charater
                    if data[lineCount + indexLines][symbolIndex + indexChar].isnumeric():
                        #hack fix to try and get the right position
                        numberBehind = True
                        tmp = 0
                        while numberBehind == True:
                            if data[lineCount + indexLines][symbolIndex + indexChar + tmp].isnumeric():
                                tmp -= 1
                            else:
                                indexChar += tmp + 1
                                numberBehind = False
                    
                        #cuts 3 digits from the index we got from above
                        string = re.split(r'\D+', data[lineCount + indexLines][(symbolIndex + indexChar):(symbolIndex + indexChar) + 3])

                        for z in string: #thinik i could do this with list comprehension but idk how
                            if z in numArr:
                                bufferList.append(z)

                # this part is fixing something that doesnt even fucking matter sicne its so improbable that it doesnt happen in the data. kms
            bufferList = list(set(bufferList))
            finish += sum(map(int, bufferList))
            bufferList = [] 

            lines = lines[:symbolIndex] + '.' + lines[symbolIndex + 1:] # replace the symbol with a period

    lineCount += 1

print(finish)