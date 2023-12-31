with open('input.txt', 'r') as f:
    data = [line.rstrip() for line in f]

sum = 0

ones = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for x in data:
    # finds all the words in the line and puts it in a list. each one it finds is a seperate entry
    compareOnes = [i for i in ones if(i in x)]

    #same thing as the before loop, but with ones instead of teens
    for y in compareOnes:
        begIndex = x.find(y)
        lastIndex = begIndex + len(y)

        x = x[:begIndex] + y[0] + x[begIndex:]              # adds the first letter of the number to before the number in the list.
        x = x[:lastIndex] + y[len(y) - 1] + x[lastIndex:]   # adds the last letter of the number to after the number in the list.
        x = x.replace(y, str(ones[y]))                      # replaces the word with the number


    # remove all characters from the string
    numData = ''.join([char for char in x if char.isdigit()]) 

    if(len(numData) == 1): #if the length is one
        sum = sum + (int(numData[0]) * 10) + int(numData[0])
    else:
        sum = sum + (int(numData[0]) * 10) + int(numData[len(numData) - 1])
    

print(sum)