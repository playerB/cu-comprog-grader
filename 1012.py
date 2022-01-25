import numpy as np

def toCelsius(f):
    return (f-32)/9*5

def BMI(wh):
    return np.array(wh[:, 0])/np.array(wh[:, 1]/100)**2

def distanceTo(p,Points):
    return ((np.array(p[0])-np.array(Points[:, 0]))**2 + (np.array(p[1])-np.array(Points[:, 1]))**2)**(0.5)

exec(input().strip())