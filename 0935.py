student = list(); name = set(); group = set(); gen = set(); dep = set()
n = int(input())
for i in range(n):
    stu = input().strip().split()
    student.append([stu[0], stu[1], stu[2], stu[3]])
    name.add(stu[0])
    group.add(stu[1])
    gen.add(stu[2])
    dep.add(stu[3])
finder = input().strip().split()
scopy = student.copy()
for i in range(len(finder)):
    if finder[i] in group:
        if len([s for s in scopy if s[1] == finder[i]]) == 0:
            scopy = [['Not Found']]
        else:
            scopy = [s for s in scopy if s[1] == finder[i]]
    if finder[i] in gen:
        if len([s for s in scopy if s[2] == finder[i]]) == 0:
            scopy = [['Not Found']]
        else:
            scopy = [s for s in scopy if s[2] == finder[i]]
    if finder[i] in dep:
        if len([s for s in scopy if s[3] == finder[i]]) == 0:
            scopy = [['Not Found']]
        else:
            scopy = [s for s in scopy if s[3] == finder[i]]
if len(scopy) == len(student):
    scopy = [['Not Found']]
for i in sorted(scopy):
    print(' '.join(i))
