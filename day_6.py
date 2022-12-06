fl = open('inp_day_6.txt', 'r')

inp = fl.read()

for i in range(3,len(inp)):
    unique = True
    for j in range(i-3, i):
        if inp[j+1:i+1].find(inp[j]) != -1:
            unique = False
            break
    if unique:
        print("Part 1 solution: " + str(i+1))
        break

for i in range(13,len(inp)):
    unique = True
    for j in range(i-13, i):
        if inp[j+1:i+1].find(inp[j]) != -1:
            unique = False
            break
    if unique:
        print("Part 2 solution: " + str(i+1))
        break