st = input().strip().lower()
lst = list(st)
d = {}
for k in lst:
    if k not in d:
        d[k] = -1
    elif k in d:
        d[k] -= 1
li = [[d[k], k] for k in d]
li.sort()
for i in range(len(li)) :
    if 'a' <= li[i][1] <= 'z' :
        print(li[i][1] + " -> " + str(-1*li[i][0]))