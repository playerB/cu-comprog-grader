import numpy as np
#try numpy
def read_poly(p):
    rp = []
    if p == []: return np.poly1d(0)
    for i in range(p[0][1], -1, -1):
        plnm = False
        for j in p:
            if i == j[1]:
                rp.append(j[0])
                plnm = True
                break
        if not plnm: rp.append(0)
    return rp

def return_poly(p):
    p = p.tolist()
    rp = []
    for i in range(len(p)):
        if p[i] != 0:
            rp.append((int(p[i]), len(p) - i -1))
    return rp

def add_poly(p1, p2):
    P1 = np.poly1d(read_poly(p1))
    P2 = np.poly1d(read_poly(p2))
    return return_poly(np.polyadd(P1, P2).c)

def mult_poly(p1, p2):
    P1 = np.poly1d(read_poly(p1))
    P2 = np.poly1d(read_poly(p2))
    return return_poly(np.polymul(P1, P2).c)

for i in range(3):
    exec(input().strip())