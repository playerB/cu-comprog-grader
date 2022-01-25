import numpy as np

def eq(A, B, p):
    size = 1
    for i in A.shape:
        size *= i
    equal = np.sum(A == B)
    if equal >= size*p/100:
        return True
    return False

def closest_point_indexes(points, p):
    distance = ((points[:, 0] - p[0])**2 + (points[:, 1] - p[1])**2)**(1/2)
    ind = np.arange(distance.shape[0])
    return ind[distance == np.min(distance)]

def number_of_inversions(A):
    c = A-A.reshape((A.shape[0], 1))
    for i in range(A.shape[0]):
        c[i:, i] = 0
    return np.sum(c < 0)

exec(input().strip())