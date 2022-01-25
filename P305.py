import numpy as np
def spiral_square(n) :
    sq = np.zeros((n, n), int)
    i = (n-1)//2; j = (n-1)//2; k = 1
    sq[i, j] = 1
    j += 1
    while k < n**2-1:
        while sq[i, j-1] != 0:
            k += 1
            sq[i, j] = k
            i -= 1
        while sq[i+1, j] != 0:
            k += 1
            sq[i, j] = k
            j -= 1
        while sq[i, j+1] != 0:
            k += 1
            sq[i, j] = k
            i += 1
        while sq[i-1, j] != 0:
            k += 1
            sq[i, j] = k
            j += 1
            if k >= n**2: break
    return sq.tolist()

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())