import math
n = int(input())
down = math.sqrt(2*math.pi)*(n**(n+0.5))*(math.e**(-n+1/(12*n+1)))
up = math.sqrt(2*math.pi)*(n**(n+0.5))*(math.e**(-n+1/(12*n)))
print(down)
print(up)