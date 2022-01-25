def convex_polygon_area(p):
    sum1 = 0; sum2 = 0
    for i in range(len(p)):
        sum1 += p[i][0]*p[(i+1)%len(p)][1]
        sum2 += p[i][1]*p[(i+1)%len(p)][0]
    return abs(sum1-sum2)/2

def is_heterogram(s):
    h = ''
    for c in s.lower():
        if c not in h and 'a' <= c <= 'z': h += c
        elif c in h: return False
    return True

def replace_ignorecase(s, a, b):
    k = 0; snew = s; sl = s.lower(); al = a.lower()
    while sl.find(al, k) != -1:
        if al in sl[k:]:
            j = sl.find(al, k)
            snew = snew[:j] + b + snew[j+len(a):]
            sl = sl[:j] + b + sl[j+len(a):]
            k += len(b)
    return snew

def top3(votes):
    return [dara for vote, dara in sorted([[-v, k] for k, v in votes.items()])[:3]]

for k in range(2):
    exec(input().strip())