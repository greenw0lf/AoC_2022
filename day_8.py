fl = open('inp_day_8.txt', 'r')

lines = fl.readlines()

forest = [[]]

i = 0
for line in lines:
    for c in line:
        if c != '\n':
            forest[i].append(int(c))
        else:
            forest.append([])
            i += 1

count = len(forest) + 2 * (len(forest) - 1) + len(forest) - 2

for i in range(1, len(forest) - 1):
    for j in range(1, len(forest) - 1):
        boolean = True
        for k in range(i+1, len(forest)):
            if forest[i][j] <= forest[k][j]:
                boolean = False
                break
        if boolean:
            count += 1
            continue
        boolean = True
        for k in range(0, i):
            if forest[i][j] <= forest[k][j]:
                boolean = False
                break
        if boolean:
            count += 1
            continue
        boolean = True
        for k in range(j+1, len(forest)):
            if forest[i][j] <= forest[i][k]:
                boolean = False
                break
        if boolean:
            count += 1
            continue
        boolean = True
        for k in range(0, j):
            if forest[i][j] <= forest[i][k]:
                boolean = False
                break
        if boolean:
            count += 1

print('Part 1 solution: ' + str(count))

max = 0

for i in range(1, len(forest) - 1):
    for j in range(1, len(forest) - 1):
        scores = [0, 0, 0, 0]
        for k in range(i+1, len(forest)):
            if forest[i][j] <= forest[k][j]:
                scores[0] = k - i
                break
        if scores[0] == 0:
            scores[0] = len(forest) - 1 - i
        for k in range(i-1, -1, -1):
            if forest[i][j] <= forest[k][j]:
                scores[1] = i - k
                break
        if scores[1] == 0:
            scores[1] = i
        for k in range(j+1, len(forest)):
            if forest[i][j] <= forest[i][k]:
                scores[2] = k - j
                break
        if scores[2] == 0:
            scores[2] = len(forest) - 1 - j
        for k in range(j-1, -1, -1):
            if forest[i][j] <= forest[i][k]:
                scores[3] = j - k
                break
        if scores[3] == 0:
            scores[3] = j
        if scores[0] * scores[1] * scores[2] * scores[3] > max:
            max = scores[0] * scores[1] * scores[2] * scores[3]

print('Part 2 solution: ' + str(max))
