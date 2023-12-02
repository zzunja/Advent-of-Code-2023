with open('input.txt', 'r') as f:
    data = [line.rstrip() for line in f]

sum = 0

ones = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
teens = {"eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}

for x in data:
    index = 0
    compareOnes = [i for i in ones if(i in x)]
    compareTeens = [i for i in teens if(i in x)]

    for y in compareTeens:
        begIndex = x.find(y)
        lastIndex = begIndex + len(y)

        x = x[:begIndex] + y[0] + x[begIndex:]
        x = x[:lastIndex] + y[len(y) - 1] + x[lastIndex:]
        x = x.replace(y, str(teens[y]))

    for y in compareOnes:
        begIndex = x.find(y)
        lastIndex = begIndex + len(y)

        x = x[:begIndex] + y[0] + x[begIndex:]
        x = x[:lastIndex] + y[len(y) - 1] + x[lastIndex:]
        x = x.replace(y, str(ones[y]))

    numData = ''.join([char for char in x if char.isdigit()]) #remove all characters

    if(len(numData) == 1): #if the length is one
        sum = sum + (int(numData[0]) * 10) + int(numData[0])
    else:
        sum = sum + (int(numData[0]) * 10) + int(numData[len(numData) - 1])
    

print(sum)