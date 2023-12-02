with open('input.txt', 'r') as f:
    data = [line.rstrip() for line in f]

sum = 0

for x in data:
    numData = ''.join([char for char in x if char.isdigit()]) #remove all digits

    if(len(numData) == 1): #if the length is one
        sum = sum + (int(numData[0]) * 10) + int(numData[0])
    else:
        sum = sum + (int(numData[0]) * 10) + int(numData[len(numData) - 1])
print(sum)