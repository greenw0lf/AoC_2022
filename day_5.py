read_stack = [[], [], [], [], [], [], [], [], []]

stack = [[], [], [], [], [], [], [], [], []]

fl = open('inp_day_5.txt', 'r')

lines = fl.readlines()

for line in lines:
    if len(line) == 1:
        continue
    if line[1] != '1' and line[1] != 'o':
        for i in range(0, len(line), 4):
            if line[i] == '[':
                read_stack[i//4].append(line[i+1])
    elif line[1] == '1':
        i = 0
        for col in read_stack:
            while len(col) > 0:
                stack[i].append(read_stack[i].pop())
            i += 1
    else:
        words = line.split(' ')
        src = int(words[3]) - 1
        target = int(words[5]) - 1
        for i in range(int(words[1])):
            stack[target].append(stack[src].pop())
    
output = ''    
for st in stack:
    output += st[len(st) - 1]

print('Part 1 solution: ' + output)

stack = [[], [], [], [], [], [], [], [], []]

for line in lines:
    if len(line) == 1:
        continue
    if line[1] != '1' and line[1] != 'o':
        for i in range(0, len(line), 4):
            if line[i] == '[':
                read_stack[i//4].append(line[i+1])
    elif line[1] == '1':
        i = 0
        for col in read_stack:
            while len(col) > 0:
                stack[i].append(read_stack[i].pop())
            i += 1
    else:
        words = line.split(' ')
        src = int(words[3]) - 1
        target = int(words[5]) - 1
        n = int(words[1])
        stack[target] += stack[src][len(stack[src])-n:len(stack[src])]
        for i in range(n):
            stack[src].pop()
    
output = ''    
for st in stack:
    output += st[len(st) - 1]

print('Part 2 solution: ' + output)