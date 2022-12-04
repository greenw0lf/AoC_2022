import string

fl = open('inp_day_3.txt', 'r')

lines = fl.readlines()

letters = string.ascii_letters

priority = 0

for line in lines:
    comp1 = line[:len(line) // 2]
    comp2 = line[len(line) // 2:]
    for l in comp1:
        if comp2.find(l) != -1:
            priority += letters.index(l) + 1
            break

print('Part 1 solution: ' + str(priority))

i = 0
groups = 0

while i < len(lines):
    for l in lines[i]:
        if lines[i+1].find(l) != -1 and lines[i+2].find(l) != -1:
            groups += letters.index(l) + 1
            break
    i += 3

print('Part 2 solution: ' + str(groups))
