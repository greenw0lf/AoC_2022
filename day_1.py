fl = open('inp_day_1.txt', 'r')

lines = fl.readlines()

max = 0
sum = 0

for line in lines:
    if line != '\n':
        sum += int(line)
    else:
        max = sum if sum > max else max
        sum = 0

print('Part 1 solution: ' + str(max))

max1 = 0
max2 = 0
max3 = 0
sum = 0

for line in lines:
    if line != '\n':
        sum += int(line)
    else:
        if sum > max1:
            max3 = max2
            max2 = max1
            max1 = sum
        elif sum > max2:
            max3 = max2
            max2 = sum
        elif sum > max3:
            max3 = sum
        sum = 0

print(max)
print(max2)
print(max3)

print('Part 2 solution: ' + str(max + max2 + max3))