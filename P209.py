n = int(input())
v = list()
for i in range(n):
    c = input().split()
    fruit = [c[0]]
    for j in range(1, len(c)):
        fruit.append(float(c[j]))
    v.append(fruit)
c = input().strip().split()
if c[0] == 'show':
    for i in v:
        s = i[0]
        for j in range(1, len(i)):
            s += ' ' + str(i[j])
        print(s)
elif c[0] == 'get':
    s = ''
    for i in v:
        if i[0] == c[1]:
            s = i[0]
            for j in range(1, len(i)):
                s += ' ' + str(i[j])
            print(s)
    if len(s) == 0:
        print(c[1] + ' not found')
elif c[0] == 'avg':
    j = int(c[1])
    sumv = 0
    for i in v:
        sumv += i[j]
    print(round(sumv/len(i), 4))
elif c[0] == 'max':
    j = int(c[1])
    maxv = 0; maxvl = list(); maxff = ''
    for i in v:
        if i[j] > maxv:
            maxv = i[j]
            maxvl = [i[0]]
        elif i[j] == maxv:
            maxvl.append(i[0])
    maxff = sorted(maxvl)[:1]
    print(maxff[0], maxv)
elif c[0] == 'sort':
    j = int(c[1])
    print(' '.join([f for v, f in sorted([[i[j], i[0]] for i in v])]))