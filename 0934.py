import numpy as np

def pattern1(nrows, ncols):
    return np.arange(1, nrows*ncols + 1).reshape((nrows, ncols)).tolist()

def pattern2(nrows, ncols):
    return np.arange(1, nrows*ncols + 1).reshape((ncols, nrows)).T.tolist()

def pattern3(N):
    matrix = np.zeros((N, N), int)
    matrix[np.triu_indices(N, 0)] = list(range(1, sum(range(N+1))+1))
    return matrix.tolist()

def pattern4(N):
    k = 0; numlist = list()
    for i in range(1, N + 1):
        lst = list()
        k += i
        for j in range(i):
            lst.append(k - j)
        lst += [0] * (N - i)
        numlist.append(lst)
    matrix = np.array(numlist)
    return matrix.T.tolist()

def pattern5(N):
    numlist = list()
    for i in range(N):
        numlist.append([0] * (N - i - 1))
        numlist[i] += [i + 1]
        for j in range(N - len(numlist[i])):
            numlist[i].append(numlist[i][-1] + N - j - 1)
    matrix = np.array(numlist).T
    return matrix[::-1].tolist()

def pattern6(N):
    numlist = list(); k = 0
    for i in range(N):
        numlist.append([0] * (N - i - 1))
    for i in range(N):
        if i % 2 == 0:
            for j in range(i, N):
                k += 1
                numlist[j].append(k)
        else:
            for j in range(N - 1, i - 1, -1):
                k += 1
                numlist[j].append(k)
    matrix = np.array(numlist).T
    return matrix[::-1].tolist()

exec(input().strip())