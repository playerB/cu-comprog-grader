n = int(input())
sortid = []
stu = []
allid = []
grade = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
for i in range(n):
    id, nowgrade = input().split()
    sortid.append(id)
    stu.append([id, nowgrade])
    allid.append(id)
newgrade = input().split()

if newgrade != []:
    for i in newgrade:
        myid = i[:-1]
        if myid in allid:
            if i[-1] == '-':
                stu[allid.index(myid)][1] = grade[grade.index(stu[allid.index(myid)][1]) + 1]
            if i[-1] == '+':
                stu[allid.index(myid)][1] = grade[grade.index(stu[allid.index(myid)][1]) - 1]
while True:
    i = input()
    if i == 'q':
        break
    myid = i[:-1]
    if myid in allid:
        if i[-1] == '-':
            stu[allid.index(myid)][1] = grade[grade.index(stu[allid.index(myid)][1]) + 1]
        if i[-1] == '+':
            stu[allid.index(myid)][1] = grade[grade.index(stu[allid.index(myid)][1]) - 1]

for student in range(len(sortid)):
    print(sortid[student], stu[student][1])