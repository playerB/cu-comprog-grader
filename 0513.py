n = int(input())
collect = []
for i in range(0,n) :
    set1 = int(input())
    collect.append(set1)
set2 = input().split()
for j in range(0,len(set2)) :
    collect.append(int(set2[j]))
while True :
    set3 = int(input())
    if set3 == -1 :
        break
    collect.append(set3)
arrange = []
for i in range(0,len(collect)) :
    if i % 2 == 0 :
        arrange.append(collect[i])
    elif i % 2 == 1 :
        arrange.insert(0,collect[i])
print(arrange)