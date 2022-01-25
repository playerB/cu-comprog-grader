def first_fit(L, e):
    canInsert = False
    for i in L:
        if e + sum(i) <= 100 :
            i.append(e)
            canInsert = True
            break
    if not canInsert: L.append([e])
    return L

def best_fit(L, e):
    sumL = list()
    for i in L:
        sumL.append(sum(i))
    if len(sumL) > 0 and min(sumL) + e <= 100:
        maxsum = 0
        for i in sumL:
            if maxsum < i + e <= 100:
                maxsum = i + e
        L[sumL.index(maxsum - e)].append(e)
    else: L.append([e])
    return L

def partition_FF(D):
    FFl = list()
    for i in D:
        first_fit(FFl, i)
    return FFl

def partition_BF(D):
    BFl = list()
    for i in D:
        best_fit(BFl, i)
    return BFl


exec(input().strip())