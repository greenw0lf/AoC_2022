outcomes_1 = ['B X', 'C Y', 'A Z', 'A X', 'B Y', 'C Z', 'C X', 'A Y', 'B Z']

outcomes_2 = ['B X', 'C X', 'A X', 'A Y', 'B Y', 'C Y', 'C Z', 'A Z', 'B Z']

fl = open('inp_day_2.txt', 'r')

lines = fl.readlines()

score1 = 0
score2 = 0

for line in lines:
    line = line.replace('\n', '')
    score1 += outcomes_1.index(line) + 1
    score2 += outcomes_2.index(line) + 1

print('Part 1 solution: ' + str(score1))
print('Part 2 solution: ' + str(score2))