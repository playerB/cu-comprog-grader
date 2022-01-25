def row_number(t, e):
    for i in range(len(t)):
        for c in t[i]:
            if c == e:
                return i

def flatten(t):
    listofints = list()
    for l in t:
        for c in l:
            if c != 0:
                listofints.append(c)
    return listofints

def inversions(x):
    count = 0; tmp = list(x)
    for i in tmp:
        x.remove(i)
        for j in x:
            if i > j: count += 1
    return count

def solvable(t):
    if len(t)%2 == 0:
        if inversions(flatten(t))%2 == 0:
            return row_number(t, 0)%2 == 1
        else:
            return row_number(t, 0)%2 == 0
    else: return inversions(flatten(t))%2 == 0

exec(input().strip())