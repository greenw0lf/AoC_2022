fl = open('inp_day_4.txt', 'r')

lines = fl.readlines()

count1 = 0
count2 = 0

for line in lines:
    elves = line.split(',')
    e1_low, e1_high = elves[0].split('-')
    e2_low, e2_high = elves[1].split('-')
    e2_high = e2_high.replace('\n', '')
    
    if int(e1_low) - int(e2_low) >= 0 and int(e2_high) - int(e1_high) >= 0:
        count1 += 1
    elif int(e2_low) - int(e1_low) >= 0 and int(e1_high) - int(e2_high) >= 0:
        count1 += 1
    
    print(e1_low, e1_high, e2_low, e2_high)
    print(int(e1_low) > int(e2_low) and int(e1_low) > int(e2_high))

    if int(e1_low) > int(e2_low) and int(e1_low) > int(e2_high):
        count2 += 1
    elif int(e2_low) > int(e1_low) and int(e2_low) > int(e1_high):
        count2 += 1

print('Part 1 solution: ' + str(count1))
print('Part 2 solution: ' + str(len(lines) - count2))