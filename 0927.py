def knows(R,x,y):
    return x in R.keys() and y in R[x]

def is_celeb(R,x):
    if x in R and (R[x] != {x} and R[x] != set()): return False
    for k in R.keys():
        if x not in R[k] and R[k] != set(): return False
    return True

def find_celeb(R):
    for k in R.keys():
        for j in R[k]:
            if is_celeb(R,j):
                return j
    return None

def read_relations() :
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        if d[0] not in R:
            R[d[0]] = set()
        R[d[0]].add(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)

exec(input().strip()) # do not remove this line