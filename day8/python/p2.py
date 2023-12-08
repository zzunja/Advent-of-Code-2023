from math import lcm

with open("day8/input.txt") as f:
    data = f.read()

instruction = data.split('\n')[0]
instruction = list(instruction)
convert = {'L':0, 'R':1}
for z, y in enumerate(instruction):
    if not y.isdigit():
        instruction[z] = convert[y]
tmp = data.split('\n\n')[1]
tmp = tmp.split('\n')
input = {}
start = []
distances = []

for i in tmp:
    first = i.split(' ')[0]
    i = i.split('(')[1]
    second, third = i.split(', ')
    third = third[:len(third)-1]
    input[first] = [second, third]
    if first[2:] == 'A':
        start.append(first)

def findDistance(x):
    distance = 0
    instructionCount = 0
    while not x.endswith('Z'):
        if instructionCount == len(instruction):
            instructionCount = 0
        tmp = input[x]
        x = tmp[instruction[instructionCount]]
        distance += 1
        instructionCount += 1
    return distance

for x in start:
    distances.append(findDistance(x))

print(lcm(*distances)) #lcm all the distances

