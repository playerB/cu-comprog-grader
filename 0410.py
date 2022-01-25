import math
a = float(input())
n = 0
b = a
while True :
    n += 1
    b = b // 10
    if b == 0 :
        break
low = 0
up = n
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
