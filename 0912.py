n = int(input().strip()); allSet = list()
for i in range(n):
    allSet.append(set([int(a) for a in input().strip().split()]))
its = set(); un = set()
if n > 0: its = allSet[0]
for i in range(n):
    its = allSet[i].intersection(its)
    un = allSet[i].union(un)
print(len(un))
print(len(its))