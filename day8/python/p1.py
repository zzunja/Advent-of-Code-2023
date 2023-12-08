with open("day8/input.txt") as f:
    data = f.read()

instruction = data.split('\n')[0]
instruction = list(instruction)
convert = {'L':1, 'R':2}
for z, y in enumerate(instruction):
    if not y.isdigit():
        instruction[z] = convert[y]
tmp = data.split('\n\n')[1]
tmp = tmp.split('\n')
input = []

for i in tmp:
    first = i.split(' ')[0]
    i = i.split('(')[1]
    second, third = i.split(', ')
    third = third[:len(third)-1]
    input.append([first, second, third])


index = 0
tmp = 0
tmp2 = 'AAA'
while True:
    if tmp == len(instruction):
        tmp = 0
    for i in input:
        if not i[0] == tmp2:
            continue
        tmp2 = i[instruction[tmp]]
        tmp += 1
        index += 1
        break
    if tmp2 == 'ZZZ':
        break
print(index)