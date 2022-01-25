import math
a = float(input())
low = 0
up = a
x = (low+up)/2
while True :
    if 10**x > a :
        up = x
    elif 10**x < a :
        low = x
    x = (low + up) / 2
    if abs(a-10**x)<(10e-10*max(a,x**2)) :
        break
print(round(x,6))
