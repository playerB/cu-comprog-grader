n = int(input())
travel = dict(); isother = False; idsorder = list()
for i in range(n):
    ids, t = input().strip().split(': ')
    travel[ids] = {e for e in t.split(', ')}
    idsorder.append(ids)
myid = input().strip()
for i in idsorder:
    if len(travel[myid].intersection(travel[i])) > 0:
        if i == myid: continue
        print(i)
        isother = True
if isother == False: print('Not Found')