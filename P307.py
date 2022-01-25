alldoc = dict()
n = int(input())
for i in range(n):
    docname = input().strip()
    alldoc[docname] = [e for e in input().strip().split()]

while True:
    docscore = list()
    search = input().strip()
    if search == '-1': break
    for i in alldoc:
        if search in alldoc[i]:
            c = alldoc[i].count(search)
            docscore.append([c/len(alldoc[i])/len(set(alldoc[i])), i])
    if len(docscore) > 0:
        print(sorted(docscore, reverse=True)[:1][0][1])
    else: print('NOT FOUND')
