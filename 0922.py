import numpy as np #ขี้เกียจใช้ nested loop ละ 555555

def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return np.array(m)

def mult_c(C, A):
    return (A*C).tolist()

def mult(A, B):
    return (A.dot(B)).tolist()
exec(input().strip())